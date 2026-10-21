# Quant Trading Lab: Research Report (Demo/Paper Only)

Prepared by: Research Lab quant researcher. Date: 2026-10-21.
Scope: three paper desks (FX, US stocks, US options), research, validation, risk, architecture on a Windows PC with an RTX 4090, a 4-week plan, and compliance notes.

**Nothing in this report is investment advice.** It covers a research and simulation program that uses no real money. Every performance figure quoted below comes from the cited literature. None of it is a forecast.

---

## 0. Executive summary and honest framing

- **Base rate.** Most backtested strategies fail live. McLean and Pontiff (2016, *Journal of Finance*) studied 97 published cross-sectional predictors. Returns were 26% lower out-of-sample and 58% lower after publication ([paper](https://www.gwern.net/doc/economics/2016-mclean.pdf)). Harvey, Liu and Zhu (2016) argue that with hundreds of factors tested, a new factor needs a t-stat above about 3.0, not 2.0. Treat any backtest Sharpe above 2 on daily data as a bug until proven otherwise.
- **What paper trading does not prove.** Alpaca's own docs say paper fills ignore market impact, queue position, slippage from latency, price improvement, dividends, regulatory fees and borrow fees. Order size is not checked against NBBO size ([Alpaca paper docs](https://docs.alpaca.markets/us/docs/paper-trading)). The Tradier and tastytrade sandboxes use 15-minute delayed quotes ([Tradier](https://docs.tradier.com/docs/market-data), [tastytrade](https://developer.tastytrade.com/sandbox)). So paper P&L is an upper bound on what live trading would earn. Our accounting must subtract modeled costs from it ("cost-adjusted paper P&L").
- **Recommended platforms:** FX goes to the **OANDA demo (v20 REST API)**. Stocks go to **Alpaca paper**. Options go to **Alpaca paper (Level 3 multi-leg)**. A second options venue is optional: Tradier sandbox or tastytrade sandbox, used for cross-checks only. IBKR paper is the best realism upgrade, but it requires opening and funding a live IBKR account.
- **Realistic expectations.** Over 4 weeks, P&L on any desk is statistically meaningless as evidence of skill. A strategy with an annualized Sharpe of 1.0 has roughly a 39% chance of showing a loss in any given month (Φ(−1/√12), assuming normal returns). The 4-week program can validate the infrastructure, cost models and execution behavior. It cannot validate alpha.

---

## 1. Paper/demo platforms

### 1.1 Comparison table

| Platform | Desk fit | Signup | API limits | Data in demo | Options | Python SDK | Cost | Automation rules |
|---|---|---|---|---|---|---|---|---|
| **OANDA demo (fxTrade Practice, v20)** | FX (and CFDs outside US) | Email signup for a demo. US clients go through OANDA Corp (CFTC/NFA). Create a token under "Manage API Access" ([QuantConnect guide](https://www.quantconnect.com/docs/v2/our-platform/live-trading/brokerages/oanda)) | 120 REST requests/s per IP, 20 active streams, 2 new connections/s; HTTP 429 when exceeded ([OANDA dev guide](https://developer.oanda.com/rest-live-v20/development-guide)) | Real-time streaming prices on the practice host `api-fxpractice.oanda.com` | No | `v20` (official), `oandapyV20` (community) | $0 | The API is built for automation. US accounts follow NFA rules: FIFO, no hedging, and leverage capped at 50:1 on majors and 20:1 on others ([OANDA US help](https://help.oanda.com/us/en/faqs/account-types-and-leverage-us.htm)). The demo should be configured to mimic these. |
| **Alpaca paper** | US stocks, ETFs, options (crypto too) | Paper-only account worldwide with just an email ([Alpaca](https://alpaca.markets/learn/start-paper-trading)) | Trading API 200 req/min per account. Market data 200 req/min on free Basic, 10,000/min on Algo Trader Plus ([Alpaca forum, staff](https://forum.alpaca.markets/t/is-there-a-way-to-increase-the-200-min-api-call-limit-for-the-trading-endpoint/18110)) | Stocks: real-time IEX only, which is about 2-3% of volume. Options: the free "indicative" feed, a derivative of OPRA with trades delayed 15 minutes. Full OPRA/SIP costs about $99/mo with Algo Trader Plus ([Alpaca option data](https://docs.alpaca.markets/us/docs/historical-option-data)) | Yes. Enabled by default in paper. Level 3 multi-leg (`mleg`) spreads and iron condors, plus index options SPX/SPXW/XSP/VIX ([L3 docs](https://docs.alpaca.markets/us/docs/options-level-3-trading), [index options](https://alpaca.markets/blog/alpaca-introduces-index-options-paper-trading/)) | `alpaca-py` (official) | $0. Optional $99/mo data upgrade | API-first broker, so automation is explicitly supported. Paper starts at $100k. Fills match NBBO with about 10% random partial fills ([paper docs](https://docs.alpaca.markets/us/docs/paper-trading)) |
| **Interactive Brokers paper** | All three, with the most realistic simulator | **Requires a live IBKR account**, which means KYC and funding. A paper account with $1M simulated equity is then created automatically ([IBKR](https://ibkb.interactivebrokers.com/article/1719)) | TWS API pacing limits of about 50 msgs/s, plus historical-data pacing rules | Delayed by default. Real-time only if the live account pays for subscriptions and enables "share market data" ([IBKR KB 1719](https://ibkb.interactivebrokers.com/article/1719)) | Full (all levels the live account is approved for) | `ib_async` (successor to `ib_insync`), official `ibapi` | $0 for paper, but the live account must be funded and real-time data costs money | Automation is allowed. TWS or IB Gateway must run with a daily restart |
| **Tradier sandbox** | Stocks and options (cross-check) | Free developer signup with a sandbox token | About 60-120 req/min per endpoint group (check docs) | **15-minute delayed** equities and options. No indices, no Greeks, no streaming ([Tradier docs](https://docs.tradier.com/docs/market-data), [FAQ](https://docs.tradier.com/docs/faq)) | Yes, including multileg | Community SDKs or plain REST | $0 | Fills are based on delayed data, so it is unreliable for intraday work ([TradersPost](https://blog.traderspost.io/article/broker-paper-trading-comparison)) |
| **tastytrade sandbox (cert)** | Options (cross-check) | Needs an OAuth client registered with tastytrade. Separate sandbox credentials ([tastytrade](https://developer.tastytrade.com/getting-started)) | Not published. Strict User-Agent format | **15-minute delayed quotes**. The sandbox **resets every 24h**, deleting trades and positions ([sandbox docs](https://developer.tastytrade.com/sandbox)) | Yes | `tastytrade` (community, tastyware) | $0 | Fills are simulated by custom rules, not by the market. Good for order-plumbing tests only. The daily reset breaks P&L history. |

### 1.2 Recommendation per desk
- **FX: OANDA demo (v20).** It has a real-time streaming practice feed, generous rate limits, is free, and has a mature Python client. Settings to apply: US-style constraints (50:1 / 20:1 leverage, FIFO, no hedging) enforced in our own risk layer. Our cost model should use OANDA's actual quoted spreads plus 0.2-0.5 pip of extra slippage.
- **US stocks: Alpaca paper.** It is free, real-time IEX, and supports bracket and OCO orders. Caveats: IEX quotes can be stale or wide on illiquid names, so trade only liquid large caps and ETFs. Consider $99/mo SIP only if intraday strategies reach week 3.
- **US options: Alpaca paper (Level 3).** It supports defined-risk multi-leg orders, including index options (SPX, XSP). The big caveat is the free indicative options feed, which Alpaca staff say is "for debugging, not strategy validation" ([forum](https://forum.alpaca.markets/t/what-is-the-indicative-pricing-feed-for-options/14595)). Controls: fill-model every options trade at mid ± 50-100% of the half-spread in our own ledger. Trade only SPY, QQQ, IWM, XSP and SPX on the liquid near-the-money strikes.
- **Upgrade path:** if the owner opens a funded IBKR account later, IBKR paper with shared real-time data becomes the most realistic simulator for all three desks.

---

## 2. Historical data for backtesting

| Asset | Source | What | Limits / caveats |
|---|---|---|---|
| FX | **Dukascopy** historical export (free) | Ticks and bars, 2003+, majors and crosses | Bulk downloads via `duka`, `dukascopy-node` or Tickstory ([duka](https://github.com/smorrel1/duka), [dukascopy-node](https://docsearch.algolia.com/mcp/docs/repo/leo4815162342/dukascopy-node)). It is a single-venue ECN feed, so spreads differ from OANDA. Check the data usage agreement. |
| FX | **HistData.com** (free) | 1-minute bars and some ticks | No volume. Timezone is EST without DST, so normalize it. Not verified in this search. |
| FX | **OANDA v20 candles** (demo token) | Bid/ask/mid candles from S5 to M, many years | 5,000 candles per request. Paginate. Bid and ask are both available, which is excellent for cost modeling. |
| FX | FRED / central banks | Policy rates and interbank rates for carry, CPI and PPP for value | Free. Monthly or daily. |
| Stocks | **Alpaca historical** (free) | Minute and daily bars, 2016+ | 200 req/min. Free plan has delayed SIP history restrictions (recent 15 min) and IEX for real-time. |
| Stocks | **Massive (formerly Polygon.io)** free tier | EOD bars | 5 calls/min, about 2 years history ([summary](https://apicostcalc.com/blog/polygon-massive-rebrand-api-pricing.html)). Paid tiers are needed for ticks. |
| Stocks | yfinance / Stooq | Daily bars, adjusted | Unofficial and rate-limited. **Survivorship-biased**, because delisted names are missing. Use only for quick sanity checks. |
| Stocks | **Ken French Data Library**, AQR data sets | Factor returns (momentum, value, TSMOM) | Free, academic quality. Good benchmarks. |
| Stocks | Sharadar / Norgate (cheap, paid) | **Survivorship-free** daily data including delisted names | About $30-60/mo. Recommended before trusting any cross-sectional backtest. |
| Options | **Alpaca historical options** | Option bars and trades since Feb 2024 | The free indicative feed is not real OPRA. Short history. |
| Options | **OptionsDX** | EOD and intraday chains with IV and Greeks on about 10 tickers (SPY, SPX, QQQ…), 2010-2023 | Some free and some paid ([summary](https://davidariasfinance.com/scripts/free-options-data/)) |
| Options | **DoltHub options datasets** | Community-maintained EOD chains | Free SQL. Gaps and quality vary. Validate them. |
| Options | Cboe DataShop, ORATS, OptionMetrics (via WRDS), ThetaData | Research-grade chains and IV surfaces | Paid. ThetaData (about $30-80/mo) is the cheapest decent option-tick source. ORATS is good for EOD surfaces. |
| Vol indices | **Cboe VIX/VIX9D/VIX3M history** (free CSV) | Daily index levels | Good regime and VRP inputs. |

**Data rules:** keep raw data immutable in Parquet, partitioned by date and symbol. Store bid and ask, not just mid. Record the vendor and download time. Every backtest must log the dataset hash.

---

## 3. Strategy catalog (33 families)

Evidence tiers: **A** means peer-reviewed and replicated out-of-sample across markets or decades. **B** means peer-reviewed but weaker, decayed or capacity-limited, or strong practitioner evidence. **C** means practitioner or anecdotal only, or mostly backtests.

| # | Family | Desk(s) | Core idea | Key evidence | Tier | Live realism notes |
|---|---|---|---|---|---|---|
| 1 | Time-series momentum / trend following | FX, ETFs | Go long or short each asset by the sign of its 12-month (or blended 1-3-12m) return, sized by inverse vol | Moskowitz, Ooi & Pedersen (2012, JFE). Hurst, Ooi & Pedersen "A Century of Evidence on Trend-Following" (2017) | A | Works over long horizons. Long flat or choppy stretches (2011-2019 was weak). Needs many uncorrelated markets. One FX desk alone is thin. |
| 2 | Cross-sectional momentum | Stocks | Long the past 12-1 month winners, short the losers | Jegadeesh & Titman (1993). Asness, Moskowitz & Pedersen (2013) | A | Momentum crashes (Daniel & Moskowitz 2016). Long-only top-decile variant is more practical for paper. |
| 3 | Residual / idiosyncratic momentum | Stocks | Momentum on factor-model residuals | Blitz, Huij & Martens (2011) | B | Lower crash risk. Needs a factor model. |
| 4 | Industry momentum | Stocks, sector ETFs | Rotate into the best-performing sectors | Moskowitz & Grinblatt (1999) | B | Simple and cheap with sector ETFs. |
| 5 | Short-term reversal (1-week/1-month) | Stocks | Buy last week's losers and sell last week's winners | Jegadeesh (1990). Lehmann (1990) | B | Profits are largely eaten by costs in large caps. Mostly survives in liquidity-provision form. |
| 6 | Intraday / overnight mean reversion | Stocks, ETFs | Fade large opening gaps or extreme intraday moves | Practitioner. Heston, Korajczyk & Sadka (2010) for intraday periodicity | C/B | Very cost-sensitive. IEX-only data hurts. |
| 7 | Pairs trading (distance method) | Stocks | Trade the spread of historically close pairs | Gatev, Goetzmann & Rouwenhorst (2006, RFS) | B | Documented decay after 2000. Do & Faff (2010) |
| 8 | Cointegration stat-arb (Engle-Granger, Johansen) | Stocks, ETFs, FX crosses | Trade a stationary linear combination | Engle & Granger (1987). Johansen (1991). Vidyamurthy (2004) | B | Cointegration breaks out-of-sample often. Re-test the relationship on a rolling basis. |
| 9 | Ornstein-Uhlenbeck spread trading | Stocks, FX | Model the spread as OU and trade at ±k·σ_eq | Avellaneda & Lee (2010, Quant Finance), PCA residual stat-arb | B | Avellaneda-Lee returns decayed sharply after 2003. |
| 10 | Kalman-filter dynamic hedge ratio | Pairs | Time-varying beta via a state-space model | Elliott, van der Hoek & Malcolm (2005). Chan (2013, practitioner) | B/C | Reduces lag in the hedge ratio. Overfitting risk in the noise parameters. |
| 11 | FX carry | FX | Long high-yield and short low-yield currencies | Lustig, Roussanov & Verdelhan (2011). Koijen et al. "Carry" (2018) | A | Crash-prone ("up the stairs, down the elevator"). Brunnermeier, Nagel & Pedersen (2008). Broker swap/financing rates in the demo may differ from interbank rates. |
| 12 | FX value (PPP deviation) | FX | Long undervalued currencies vs PPP or real exchange rate | Asness, Moskowitz & Pedersen (2013). Menkhoff et al. (2017) | A/B | Slow, multi-year horizon. Nothing to evaluate in 4 weeks. |
| 13 | FX momentum (cross-sectional) | FX | Long recent winner currencies | Menkhoff, Sarno, Schmeling & Schrimpf (2012, JFE) | B | Concentrated in less liquid EM currencies that OANDA US may not offer. |
| 14 | Dollar factor / macro risk-on-off | FX | Trade the USD basket on global risk signals | Lustig, Roussanov & Verdelhan (2014) | B | Low frequency. |
| 15 | Volatility risk premium (short index vol, defined risk) | Options | Implied vol exceeds realized vol on average. Sell put spreads or iron condors on SPX/SPY | Carr & Wu (2009). Bakshi & Kapadia (2003). Israelov & Nielsen (2015) | A for the premium's existence, B for defined-risk implementation | Negative skew. Many small wins and rare large losses (Feb 2018, Mar 2020, Aug 2024). Spreads cut both tail and premium. |
| 16 | Put-write / buy-write indices | Options | Systematic CBOE PUT/BXM-style overwriting | Whaley (2002). Cboe index history | A/B | Equity-like drawdowns. A cash-secured put needs a lot of buying power. Use XSP or spreads instead. |
| 17 | VRP timing (VIX term structure / IV-RV spread) | Options | Sell vol only when the term structure is in contango and IV − RV > threshold | Practitioner. Simon & Campasano (2014) on VIX futures | B/C | Filters improve drawdown in backtests. The number of parameters invites overfitting. |
| 18 | 0DTE / short-dated index premium selling | Options | Sell same-day iron condors | Anecdotal and practitioner. Academic work on 0DTE flows is mixed (Bandi et al. 2023+) | C | Gamma risk is extreme. Paper fills on indicative data are unreliable. **Deprioritize.** |
| 19 | Earnings IV crush (defined-risk) | Options | Sell straddles or condors before earnings | Practitioner. Patell & Wolfson (1979). Dubinsky et al. (2019) on earnings jumps | B/C | Implied moves are fairly priced on average. Edge is thin after costs. |
| 20 | Volatility targeting / volatility-managed portfolios | All (overlay) | Scale exposure by σ_target/σ_forecast | Moreira & Muir (2017, JF). Harvey et al. (2018) "The Impact of Volatility Targeting" | A for risk control, B for Sharpe uplift | Reliably smooths risk. Sharpe uplift is disputed (Cederburg et al. 2020). **Use it as a risk overlay everywhere.** |
| 21 | Regime detection (HMM / Markov switching) | All (overlay) | Two- or three-state HMM on returns and vol. Cut risk in the high-vol state | Hamilton (1989). Ang & Bekaert (2002). Nystrup et al. (2015-2017) | B | Regimes are identified with a lag. Benefit is mainly drawdown reduction. Forward-filter only, never smoothed probabilities, which look ahead. |
| 22 | Opening-range breakout (ORB) | Stocks, ETFs | Trade the break of the first 5-30 min range | Zarattini, Barbon & Aziz (2023/24, SSRN) on "stocks in play". Crabel (1990, practitioner) | C/B | SSRN backtests are not peer-reviewed. Very sensitive to fills and to IEX-only data. |
| 23 | Intraday momentum (first half-hour predicts last half-hour) | ETFs (SPY) | Trade the last 30 min in the direction of the first 30 min | Gao, Han, Li & Zhou (2018, JFE) | B | Small edge per trade. Costs matter. |
| 24 | Overnight vs intraday return effect | Stocks, ETFs | Equity premium accrues mostly overnight. Hold close-to-open | Lou, Polk & Skouras (2019, JFE). Cliff, Cooper & Gulen (2008) | B | Turnover twice a day. Gap risk. Costs kill most of the gain in naive form. |
| 25 | Turn-of-month / calendar seasonality | Stocks, ETFs | Long the last day plus the first 3 days of the month | Lakonishok & Smidt (1988). McConnell & Xu (2008) | B | Small, cheap and robust-ish. Few trades, so slow to evaluate. |
| 26 | Pre-FOMC drift | ETFs | Long SPX 24h before FOMC announcements | Lucca & Moench (2015, JF) | B | Reported weakening after publication. Only 8 events per year. |
| 27 | Post-earnings-announcement drift (PEAD) | Stocks | Long positive-surprise stocks | Ball & Brown (1968). Bernard & Thomas (1989) | A historically, B now | Strongly decayed in large caps (Martineau 2022). Needs earnings-surprise data. |
| 28 | Low-volatility / betting-against-beta | Stocks, ETFs | Long low-beta, short high-beta | Frazzini & Pedersen (2014). Baker, Bradley & Wurgler (2011) | A | Monthly rebalance. A month of paper trading says nothing. |
| 29 | Quality / value / multi-factor | Stocks | Fundamentals-based factor portfolios | Fama & French (1993, 2015). Asness et al. "Quality minus junk" (2019) | A | Needs point-in-time fundamentals. Slow. |
| 30 | Gradient boosting on engineered features | All | LightGBM/XGBoost classifier or regressor on returns, vol and microstructure features | Gu, Kelly & Xiu (2020, RFS) show trees and NNs beat linear models in the cross-section | B in academia, C as retail live evidence | Gains concentrate in microcaps and high turnover. Replications show cost sensitivity ([Tidy Finance](https://www.tidy-finance.org/blog/gu-kelly-xiu-replication/)). The literature reports about 1%/month predictability before costs ([Kelly & Xiu survey](https://www.nber.org/system/files/working_papers/w31502/w31502.pdf)). |
| 31 | Deep sequence models (LSTM / temporal CNN / transformers) on returns | All | Predict next-period returns or direction from price history | Fischer & Krauss (2018, EJOR): LSTM on S&P 500, returns vanished after about 2010. Lim, Zohren & Roberts on deep momentum networks (2019) | C/B | Raw-price deep learning has a poor out-of-sample record at daily-and-slower horizons. Accuracy above 52-53% on direction is rare and usually leakage. **Treat any >55% hit rate as a leakage alarm.** |
| 32 | Reinforcement learning (DQN/PPO) for trading | All | An agent learns positions directly | Mostly backtest papers (FinRL etc.). Deng et al. (2016) | C | Extremely overfit-prone, non-stationary reward, little credible live evidence. Research sandbox only. Never promote without beating a simple benchmark under CPCV. |
| 33 | Deep-learning volatility forecasting (vs HAR-RV) | Options overlay, sizing | Forecast realized vol for sizing and VRP timing | Corsi (2009) HAR-RV is the strong baseline. Bucci (2020). Christensen et al. (2023) | B | **The most realistic GPU use case.** Vol is far more predictable than returns. |
| 34 | Ensemble / meta-labeling | All | A secondary ML model decides bet size or whether to take a primary signal | López de Prado (2018, AFML, practitioner-academic) | B/C | Useful for filtering trades. Easy to leak information. Use purged CV. |
| 35 | Risk parity / inverse-vol multi-asset | ETFs, FX | Equal risk contribution | Asness, Frazzini & Pedersen (2012). Qian (2005) | B | A benchmark and allocation tool more than alpha. |

**What the evidence implies for us:** the families most likely to show anything positive on paper are slow and simple: trend, carry, VRP with defined risk, and the vol-targeting overlay. ML should be used first where it has a real edge, in **volatility forecasting and trade filtering**, and only second for direct return prediction.

### 3.1 Key formulas

**Returns and performance**
- Sharpe ratio (annualized, periodic data with *q* periods per year): `SR = (mean(r) − r_f) / std(r) · √q`
- Sortino ratio: `Sortino = (mean(r) − MAR) / DD · √q`, where `DD = sqrt(mean(min(0, r − MAR)^2))` is downside deviation
- Max drawdown: `MDD = max_t (peak_t − equity_t) / peak_t`, with `peak_t = max_{s≤t} equity_s`
- Calmar ratio: `CAGR / MDD`
- Sharpe standard error (Lo 2002; Mertens 2002, non-normal): `σ(ŜR) ≈ sqrt( (1 − γ₃·SR + (γ₄−1)/4 · SR²) / (T−1) )`, where γ₃ is skew and γ₄ is (non-excess) kurtosis

**Probabilistic and deflated Sharpe** (Bailey & López de Prado 2012, 2014)
- Probabilistic Sharpe ratio: `PSR(SR*) = Φ( (ŜR − SR*)·sqrt(T−1) / sqrt(1 − γ₃·ŜR + (γ₄−1)/4 · ŜR²) )`
- Deflated Sharpe ratio: `DSR = PSR(SR₀)`, with the benchmark set to the expected maximum Sharpe of N independent trials under the null:
  `SR₀ = sqrt(V[ŜR_n]) · ( (1−γ)·Φ⁻¹(1 − 1/N) + γ·Φ⁻¹(1 − 1/(N·e)) )`, γ ≈ 0.5772 (Euler-Mascheroni), V = variance of the trial Sharpes
- Minimum track record length (per-period SR units): `MinTRL = 1 + (1 − γ₃·ŜR + (γ₄−1)/4 · ŜR²) · (Φ⁻¹(1−α) / (ŜR − SR*))²`
  - Example: with daily SR 0.063 (annualized 1.0), normal returns, SR* = 0 and α = 0.05, MinTRL ≈ 1 + 1·(1.645/0.063)² ≈ **680 trading days (about 2.7 years)**. This is why 4 weeks cannot prove anything.

**Probability of backtest overfitting (PBO)** (Bailey, Borwein, López de Prado & Zhu 2017, CSCV)
- Split the T×N matrix of trial returns into S blocks (even, e.g., 16). For each of C(S, S/2) combinations, the training set is half the blocks and the test set is the complement. Pick the best trial n* in-sample and find its out-of-sample relative rank ω̄ ∈ (0,1). Compute the logit `λ = ln(ω̄/(1−ω̄))`.
- `PBO = P(λ ≤ 0)`, the fraction of combinations where the in-sample winner ranks below the out-of-sample median. **Reject any configuration family with PBO > 0.2** (our rule).

**Sizing: Kelly**
- Binary bet with win probability *p*, odds *b* (win b per 1 risked): `f* = p − (1 − p)/b`
- Continuous returns (Gaussian approximation): `f* = (μ − r_f)/σ²`. Multi-asset: `f* = Σ⁻¹(μ − r_f)`
- Growth at fraction f: `g(f) = r_f + f(μ − r_f) − f²σ²/2`. Half-Kelly keeps 75% of the growth and halves volatility.
- **Fractional Kelly rule for the lab:** use at most **0.25× Kelly** with shrunk estimates of μ. Estimation error in μ makes full Kelly ruinous in practice (MacLean, Thorp & Ziemba 2011).

**Options: Black-Scholes-Merton** (with continuous dividend yield q)
- `d₁ = [ln(S/K) + (r − q + σ²/2)·τ] / (σ√τ)`, `d₂ = d₁ − σ√τ`
- Call: `C = S·e^{−qτ}·Φ(d₁) − K·e^{−rτ}·Φ(d₂)`. Put: `P = K·e^{−rτ}·Φ(−d₂) − S·e^{−qτ}·Φ(−d₁)`
- Delta: `Δ_C = e^{−qτ}Φ(d₁)`, `Δ_P = e^{−qτ}(Φ(d₁) − 1)`
- Gamma: `Γ = e^{−qτ} φ(d₁) / (S σ √τ)`
- Vega: `ν = S e^{−qτ} φ(d₁) √τ` (per 1.00 vol, divide by 100 per vol point)
- Theta (call): `Θ_C = −S e^{−qτ} φ(d₁) σ / (2√τ) − rK e^{−rτ}Φ(d₂) + qS e^{−qτ}Φ(d₁)` (per year, divide by 365 per day)
- Rho (call): `ρ_C = K τ e^{−rτ} Φ(d₂)`
- VRP measure: `VRP_t = IV_t² − E_t[RV²_{t,t+τ}]` (variance terms), or in practice `IV(30d ATM) − RV(next 30d)`. Ex-ante proxy: `VIX − HAR-RV forecast`.
- Defined-risk spread max loss: `MaxLoss = (width of strikes − net credit) × 100 × contracts`

**Mean reversion: Ornstein-Uhlenbeck**
- `dX_t = θ(μ − X_t)dt + σ dW_t`, with equilibrium std `σ_eq = σ / sqrt(2θ)`
- Discrete AR(1) fit: `X_{t+1} = a + b·X_t + ε`. Then `θ = −ln(b)/Δt`, `μ = a/(1−b)`, and **half-life `= ln(2)/θ = −ln(2)·Δt / ln(b)`**
- Equivalent ADF-style form: `ΔX_t = λX_{t−1} + c + ε`, half-life `= −ln(2)/λ` (Chan 2013)
- Entry and exit: z-score `z = (X − μ)/σ_eq`. Enter at |z| > 2, exit at z ≈ 0. Abandon if the half-life exceeds about 2× the holding window or the rolling ADF/Johansen test fails.

**Cointegration**
- Engle-Granger: OLS `y = α + βx + u`, then ADF on û with EG critical values (more negative than plain ADF, about −3.34 at 5% for 2 variables).
- Johansen: VECM `ΔY_t = ΠY_{t−1} + Σ Γ_i ΔY_{t−i} + ε`. The trace and max-eigenvalue tests on the rank of Π give the cointegrating vectors.

**Kalman hedge ratio**
- State `β_t = β_{t−1} + w_t`, w ~ N(0, Q). Observation `y_t = [1, x_t]·[α_t, β_t]' + v_t`, v ~ N(0, R). The innovation e_t and its variance give the z-score `e_t/√S_t`.

**Volatility targeting**
- `w_t = σ_target / σ̂_t`, capped at a leverage limit. `σ̂_t` comes from EWMA (λ = 0.94 daily) or HAR-RV: `RV_{t+1} = β₀ + β_d·RV_t + β_w·RV_t^{(5)} + β_m·RV_t^{(22)} + ε`

**Trend signal (Moskowitz-Ooi-Pedersen)**
- `r^{TSMOM}_{t,t+1} = sign(r_{t−12,t}) · (σ_target / σ̂_t) · r_{t,t+1}`, with σ_target = 40% per asset in the paper. We use 10% at portfolio level.

---

## 4. Validation methodology (trust rules)

### 4.1 Biases to eliminate
- **Look-ahead bias:** every feature at time t uses data stamped strictly ≤ t. Signals are computed at bar close and executed at the next bar's open or later. No `shift(-1)` in feature code (an automated lint rule). HMMs use forward filtering only. Scalers and normalizers are fit inside each training fold. Corporate actions are applied point-in-time.
- **Survivorship bias:** cross-sectional stock backtests require a universe that includes delisted names (Norgate or Sharadar), or are restricted to a fixed, ex-ante-defined ETF list. yfinance is used only for ETFs.
- **Selection / multiple testing:** log **every** trial (parameters, data hash, metrics) to an experiment registry such as MLflow or Optuna storage. The trial count N feeds the deflated Sharpe ratio. Optuna studies count all trials.
- **Data snooping across desks:** the holdout period (the last 20-25% of history) is locked. It may be evaluated **once** per strategy family, after all tuning.

### 4.2 Cross-validation
- **Walk-forward analysis (WFA):** use a rolling or anchored train window (e.g., 3y train / 6m test, stepping 6m). Report the concatenated out-of-sample equity curve only. Walk-forward efficiency = OOS annualized return / IS annualized return. **Require ≥ 0.5.**
- **Purged k-fold with embargo** (López de Prado 2018, AFML ch. 7): when labels span [t₀, t₁] (e.g., a 5-day forward return), purge from training any sample whose label window overlaps the test fold. Embargo h = 1-2% of T (or at least the label horizon) after each test fold. Used for all ML models. `sklearn` TimeSeriesSplit alone is insufficient.
- **Combinatorial purged CV (CPCV)** (AFML ch. 12): split into N groups and test on k groups at a time. This yields C(N,k) splits and φ = k/N·C(N,k) backtest paths (e.g., N = 6, k = 2 gives 15 splits and 5 paths). It produces a distribution of out-of-sample Sharpe ratios instead of one number. **Rule: the 25th-percentile path Sharpe must be > 0.**
- **CSCV/PBO** on each parameter grid (section 3.1), with PBO ≤ 0.2.

### 4.3 Costs and slippage (mandatory in every backtest)
- **FX:** use the actual bid/ask from OANDA candles plus 0.3 pip of slippage on majors (1 pip on crosses). Include financing/swap at OANDA demo rates for positions held over 5pm NY. Double costs in the news windows around NFP, CPI and FOMC.
- **Stocks:** commission is $0, but include SEC and FINRA TAF fees on sells. Slippage is half the quoted spread plus `η·σ_daily·sqrt(Q/ADV)` (square-root impact, η ≈ 0.1-0.3, per Almgren et al. 2005). Minimum 2 bps per side for large caps and ETFs, 5-10 bps for mid caps.
- **Options:** fills at mid ± 50% of the bid-ask half-spread for SPY and SPX near the money. Use 75-100% for wings and illiquid strikes. Commissions are modeled at $0.65/contract even though paper is free, to stay realistic for later live trading. Multi-leg orders pay per leg.
- **Stress test:** the strategy must remain profitable at **2× modeled costs**. Report the breakeven cost per trade.

### 4.4 Statistical hurdles
- Deflated Sharpe ratio > 0.95, computed with the true trial count.
- t-stat of mean OOS return ≥ 3.0 (Harvey-Liu-Zhu hurdle) for new signals. ≥ 2.0 is acceptable for "textbook" tier-A families replicated on our own data.
- Multiple-testing control across the catalog: Benjamini-Hochberg FDR at 10%, or Holm-Bonferroni for the small final shortlist. White's Reality Check or Hansen's SPA test against a buy-and-hold or random-entry benchmark.
- Minimum number of trades: ≥ 100 OOS trades for intraday or swing strategies, or ≥ 5 years OOS for monthly strategies.
- Parameter stability: performance must be smooth in a ±20% neighborhood of the chosen parameters (no "spike" optima).
- Regime robustness: report the 2008, 2020, 2022 and Aug-2024 sub-periods separately. No single year may supply more than 40% of total P&L.

### 4.5 Promotion rules (the gate)

| Stage | Entry criteria | Duration | Exit to next stage |
|---|---|---|---|
| **R0 Idea** | Logged hypothesis with an economic rationale and a citation | none | Code review passed, no leakage lints |
| **R1 Backtest** | WFA + purged CV/CPCV, costs ×1 and ×2 | none | DSR > 0.95, PBO ≤ 0.2, WFE ≥ 0.5, profitable at 2× costs, MDD within budget |
| **R2 Paper (incubation)** | Frozen code and parameters (git tag) | **≥ 8 weeks minimum** (4 weeks in this sprint is a preliminary read only), and ≥ 30 trades for higher-frequency strategies | Cost-adjusted paper Sharpe within the 90% CI predicted by the backtest. Realized slippage ≤ 1.5× modeled. Zero risk-rule breaches. Zero unhandled errors |
| **R3 Extended paper** | Passed R2 | 3-6 months, until MinTRL is meaningful for that SR | Owner sign-off plus independent review |
| **R4 Live consideration** | Out of scope now | n/a | See section 8. Would start at ≤ 10% of target size |

**Demotion:** a strategy is pulled back to R1 if its paper drawdown exceeds 1.5× the backtest's 95th-percentile drawdown for the same horizon, if live-vs-backtest tracking error is significantly larger than expected, or if any code change is made (any change restarts the paper clock).

---

## 5. Risk rules for the demo desks

The rules apply to paper because the point of paper trading is to rehearse the discipline. All rules are enforced in a central `risk_manager` that sits **between strategy and broker** and can veto any order.

**Capital model:** each desk has a notional risk budget. Use $100k on Alpaca stocks and $100k on Alpaca options. These must be separate Alpaca paper accounts, because Alpaca allows multiple paper accounts. Use $100k on the OANDA demo. Sizing rules use desk equity, not the platform's inflated buying power.

| Rule | FX | Stocks | Options |
|---|---|---|---|
| Per-trade risk (stop distance × size) | ≤ 0.5% of desk equity | ≤ 0.5% | Max loss per trade ≤ **1%** of desk equity (defined-risk only) |
| Per-strategy allocation | ≤ 33% of desk risk budget | same | same |
| Sizing method | Vol-target at 10% annualized per desk, capped at 0.25× Kelly | same | Contracts = floor(1% equity / max loss per spread) |
| Gross leverage cap | ≤ 5:1 notional (well below the 50:1 legal cap) | ≤ 1.5× equity | Total max-loss of open positions ≤ 10% of equity |
| **Max daily loss** (halt new entries, flatten intraday) | −2% of desk equity | −2% | −3% (measured on mark-to-mid, with spread-width haircut) |
| Weekly loss limit | −4%, desk halts for the rest of the week | −4% | −5% |
| **Max drawdown kill switch** | −10% from the desk high-water mark: flatten all, disable the desk, require manual review | −10% | −12% |
| Strategy-level kill | −1.5× backtest 95th-percentile DD or 3σ adverse tracking, whichever is first | same | same |
| Correlation limits | Net exposure per currency ≤ 3× per-trade risk. Pairs sharing a currency count together | Sector ≤ 25% gross, single name ≤ 5%, beta-adjusted net ≤ ±50% | Net portfolio delta ≤ ±0.3% equity per 1% SPX move. Net vega cap. ≤ 2 expiries per underlying. No more than 50% of max loss in one week's expiry |
| Cross-desk | If pairwise rolling 60-day correlation of strategy P&L is > 0.7, treat them as one strategy for sizing | | |
| Event rules | No new entries 15 min before or after tier-1 releases (NFP, CPI, FOMC) | No new entries in the last 5 min | No short premium through earnings for single names. Close or roll at 21 DTE or 50% max profit. **Close any short strike with Δ > 0.30** or when price breaches a short strike |
| Banned | Martingale or averaging down, uncapped grid | Shorting hard-to-borrow (not simulated in paper) | **Naked short options, undefined risk, 0DTE short gamma** (week 1-4), early-assignment-prone short ITM American options near ex-dividend |
| Operational | Stale-data guard: if no tick for > 30s (FX) or > 2 min (stocks/options) during market hours, no new orders | Order rate limiter under the API limits. Duplicate-order guard (client order IDs) | Leg-risk guard: only atomic `mleg` orders, never legging in |

The kill switches write `{"desk_halted": true, "reason": ...}` to the stats JSON and to an alert channel. Restart requires a manual flag file.

---

## 6. Architecture on the Windows PC (RTX 4090)

### 6.1 Layout
```
C:\QuantLab\
  env\          (uv/conda env, Python 3.11 or 3.12)
  data\raw\     (immutable vendor dumps, Parquet)   data\features\   data\models\
  src\
    connectors\  oanda.py  alpaca_stocks.py  alpaca_options.py   (thin broker adapters)
    data\        downloaders, cleaners, PIT universe
    research\    notebooks, vectorbt sweeps, CPCV/PBO/DSR utilities
    strategies\  one module per strategy, common interface: on_bar(), target_positions()
    risk\        risk_manager.py (veto layer, kill switches)
    exec\        order manager, reconcile.py
    ledger\      SQLite/DuckDB trade + fill + equity-snapshot store
    reporting\   stats_writer.py -> stats.json
  logs\  runs\  (MLflow / Optuna storage)
```

### 6.2 Stack
- **Research and backtests:** **vectorbt** (open-source version) for fast vectorized parameter sweeps and PBO grids. Backtrader is in maintenance mode, so skip it. **NautilusTrader** is an event-driven engine with the same code for backtest and live, and it has Interactive Brokers and other adapters. Its docs list Windows (x86_64) as supported, tested on Windows Server ([docs](https://nautilustrader.io/docs/latest/getting_started/installation)). If wheels misbehave on Windows 11, run it under **WSL2**. **zipline-reloaded** is useful only for daily equity factor research with a custom bundle. **QuantConnect LEAN** (local, Docker) has the best options backtesting out of the box. Its data costs money but it can ingest our own data. Recommendation: vectorbt for discovery, plus a simple, custom event-driven live loop on the broker SDKs. Add Nautilus only if the custom loop becomes limiting.
- **ML:** PyTorch with CUDA 12.x (install the CUDA wheel from pytorch.org; the 4090 has 24 GB VRAM). LightGBM and XGBoost with `device="cuda"`. scikit-learn. **Optuna** with a SQLite or Postgres study store, `MedianPruner`, and a CPCV objective, with all trials recorded for DSR. MLflow for experiment tracking.
- **Stats:** statsmodels (ADF, Johansen via `coint_johansen`, Engle-Granger `coint`), `arch` (GARCH, HAR), `hmmlearn`, `pykalman` or a hand-rolled filter, `scipy`, `quantstats` or `empyrical-reloaded` for metrics.
- **Brokers:** `v20` or `oandapyV20`, and `alpaca-py`.
- **Storage:** Parquet plus **DuckDB** for research. SQLite (WAL mode) for the live ledger.
- **Where the GPU actually helps:** large Optuna sweeps of GBMs, vol-forecasting nets (HAR vs LSTM/TCN), meta-labeling classifiers, and Monte Carlo and bootstrap for PBO/CPCV, done with CuPy or PyTorch tensors. It does **not** help the live loop, which is I/O-bound.

### 6.3 Scheduling and process model
- **Windows Task Scheduler** (or NSSM to run as services) starts three long-running desk processes (`desk_fx`, `desk_stocks`, `desk_options`), plus a `stats_writer` every 15 minutes, a nightly data refresh at 18:30 ET, and a nightly reconciliation that compares broker positions and fills to the ledger.
- Inside each desk use APScheduler or asyncio loops. FX runs 24/5 (Sunday 17:00 to Friday 17:00 New York). Stocks and options run 09:30-16:00 ET, and use `exchange_calendars` / `pandas_market_calendars` for holidays and half days.
- Power and resilience: disable sleep. Windows Update active hours set outside market hours. A watchdog restarts crashed processes. On restart, **reconcile with the broker before trading**.
- Secrets: API keys in Windows Credential Manager via `keyring` or a `.env` outside the repo. Never commit them.

### 6.4 Logging
- `structlog` or the `logging` module emitting JSON lines to `logs\{desk}\YYYY-MM-DD.jsonl`, rotated daily. Every order carries `client_order_id = {desk}-{strategy}-{uuid}`.
- Log signals, risk decisions (approve/veto and why), order submits and acks, fills (price, qty, fees, modeled slippage vs mid at decision time), and heartbeat every 60s.
- Alerts (kill switch, stale data, reconciliation mismatch) go to a Discord or Telegram webhook or email.

### 6.5 Stats JSON every 15 minutes
Write the JSON atomically (write to a temp file, then `os.replace`) so the dashboard never reads a half-written file. Two P&L views:
1. **Broker P&L**, from account equity snapshots.
2. **Cost-adjusted P&L**, which is broker P&L minus our extra modeled slippage and commissions that the paper engine does not charge. **The dashboard should headline the cost-adjusted figure.**

Schema (`C:\QuantLab\reporting\stats.json`):
```json
{
  "generated_at": "2026-10-21T15:45:00-04:00",
  "mode": "paper",
  "currency": "USD",
  "portfolio": {
    "equity": 301234.56,
    "pnl": {"total": 1234.56, "last_3h": -45.10, "last_6h": 120.33, "today": 210.00},
    "pnl_cost_adjusted": {"total": 980.12, "last_3h": -60.00, "last_6h": 95.10, "today": 170.40},
    "trades": {"total": 142, "today": 9},
    "win_rate": 0.54,
    "sharpe_annualized": 1.12,
    "sortino_annualized": 1.60,
    "max_drawdown_pct": -0.031,
    "current_drawdown_pct": -0.008
  },
  "desks": {
    "fx":      {"platform": "oanda_demo",   "halted": false, "equity": 100512.0, "pnl": {"total": 512.0, "last_3h": 10.0, "last_6h": 44.0, "today": 61.0}, "trades": 60, "win_rate": 0.48, "sharpe": 0.9, "max_drawdown_pct": -0.02, "open_positions": 3},
    "stocks":  {"platform": "alpaca_paper", "halted": false, "equity": 100400.0, "pnl": {"total": 400.0, "last_3h": -55.1, "last_6h": 40.3, "today": 99.0}, "trades": 70, "win_rate": 0.57, "sharpe": 1.2, "max_drawdown_pct": -0.025, "open_positions": 8},
    "options": {"platform": "alpaca_paper", "halted": false, "equity": 100322.56, "pnl": {"total": 322.56, "last_3h": 0.0, "last_6h": 36.0, "today": 50.0}, "trades": 12, "win_rate": 0.75, "sharpe": null, "max_drawdown_pct": -0.04, "open_positions": 4, "max_loss_open": 3800.0, "net_delta": -12.5, "net_vega": -140.0}
  },
  "strategies": [
    {"id": "fx_tsmom_v1", "desk": "fx", "stage": "R2", "paper_start": "2026-11-09", "pnl_total": 210.0, "trades": 14, "win_rate": 0.43}
  ],
  "risk": {"kill_switch": false, "breaches_today": [], "stale_feeds": []},
  "notes": "Sharpe null when fewer than 20 daily returns. Paper P&L excludes market impact; see pnl_cost_adjusted."
}
```

Computation rules:
- `last_3h` / `last_6h` = equity(now) − equity(now − 3h or 6h), using the nearest equity snapshot at or before that time. Snapshots are taken every 5 minutes into the ledger, marked to market. Options are marked at mid.
- `today`: FX uses the 17:00 New York roll. Stocks and options use the 16:00 ET prior close. Portfolio "today" uses midnight America/New_York, and the boundary must be documented in the JSON.
- `win_rate` = closed round-trips with net P&L > 0 divided by all closed round-trips (fees included).
- `sharpe_annualized` comes from **daily** equity returns × √252 (√260 for FX). Show `null` until there are at least 20 daily observations, so the dashboard does not display noise as signal.
- `max_drawdown_pct` comes from the equity high-water mark since inception.

Minimal writer sketch:
```python
import json, os, tempfile, datetime as dt
import numpy as np, pandas as pd

def window_pnl(eq: pd.Series, hours: float) -> float:
    now = eq.index[-1]; past = eq[:now - pd.Timedelta(hours=hours)]
    return float(eq.iloc[-1] - (past.iloc[-1] if len(past) else eq.iloc[0]))

def stats_block(eq: pd.Series, day_start: pd.Timestamp, trades: pd.DataFrame) -> dict:
    daily = eq.resample("1D").last().dropna().pct_change().dropna()
    sharpe = float(daily.mean() / daily.std() * np.sqrt(252)) if len(daily) >= 20 and daily.std() > 0 else None
    dd = (eq / eq.cummax() - 1).min()
    closed = trades[trades.status == "closed"]
    return {
        "pnl": {"total": float(eq.iloc[-1] - eq.iloc[0]),
                "last_3h": window_pnl(eq, 3), "last_6h": window_pnl(eq, 6),
                "today": float(eq.iloc[-1] - eq[:day_start].iloc[-1]) if len(eq[:day_start]) else 0.0},
        "trades": int(len(closed)),
        "win_rate": float((closed.net_pnl > 0).mean()) if len(closed) else None,
        "sharpe_annualized": sharpe,
        "max_drawdown_pct": float(dd),
    }

def write_atomic(path: str, payload: dict) -> None:
    d = os.path.dirname(path)
    with tempfile.NamedTemporaryFile("w", dir=d, delete=False, suffix=".tmp") as f:
        json.dump(payload, f, indent=2, default=str); tmp = f.name
    os.replace(tmp, path)   # atomic on NTFS
```
Schedule this with Task Scheduler every 15 minutes (`schtasks /create /sc minute /mo 15 ...`), or as an APScheduler job inside a supervisor process. Optionally also push the JSON to the dashboard host.

---

## 7. Four-week plan

### Week 1: Setup and data
- Open the OANDA demo (US), the Alpaca paper accounts (one for stocks, one for options, with Level 3 enabled), and optionally the Tradier sandbox. Store the keys.
- Build the Python environment with CUDA PyTorch and verify `torch.cuda.is_available()`.
- Write the broker adapters, the ledger, the risk manager skeleton, and `stats_writer`. Do a **dry-run of the dashboard JSON** with zero strategies.
- Data: Dukascopy plus OANDA bid/ask candles (2010+, H1/D) for about 20 FX pairs. Alpaca daily and minute bars for about 50 liquid ETFs and the S&P 100. Decide whether to buy survivorship-free equity data (recommended, about $30-60/mo). OptionsDX or other EOD chains for SPY/SPX, plus VIX/VIX3M history.
- Build the validation library: purged k-fold, CPCV, PBO (CSCV), DSR, MinTRL, and the cost models. Unit-test them on synthetic random-walk data. **Every strategy must fail on random data.**
- Deliverable: a working "hello world" order on each desk, reconciled, and appearing in `stats.json`.

### Week 2: Baselines and backtests
For each desk, backtest 6-8 candidates from the catalog. Baselines come first, so every complex model must beat them.
- **FX candidates:** (1) TSMOM 1-3-12m blend, vol-targeted. (2) Cross-sectional carry on G10 via OANDA financing rates. (3) Carry + trend combination (carry only when trend agrees). (4) PPP value, slow. (5) Cointegrated crosses OU (e.g., AUD/NZD, EUR/CHF-type pairs). (6) HMM regime overlay. (7) GBM trade filter (meta-labeling) on the trend signal.
- **Stocks/ETF candidates:** (1) Cross-sectional 12-1 momentum on S&P 100 or sector ETFs, monthly. (2) ETF TSMOM / dual momentum. (3) Turn-of-month SPY. (4) Intraday momentum, first 30 min to last 30 min (Gao et al.). (5) ETF pairs with Kalman hedge ratios (e.g., XLE/XOP-type, GLD/GDX-type). (6) Short-term reversal on large caps with strict costs. (7) ORB on "stocks in play", labeled tier C.
- **Options candidates (all defined-risk):** (1) 30-45 DTE SPX/XSP put credit spreads at about 16Δ, managed at 50% profit or 21 DTE. (2) Iron condors on SPY with a VRP filter (VIX − HAR-RV forecast > 0, VIX term structure in contango). (3) The same with an HMM regime gate. (4) Vol-targeted sizing of (1). (5) Defined-risk earnings condors, tier C.
- Run WFA, purged CV and CPCV, PBO and DSR, with costs at 1× and 2×. Use Optuna with every trial logged. Use the GPU for GBM/LSTM vol-forecast comparisons against the HAR-RV baseline.
- Deliverable: a scorecard per strategy covering OOS Sharpe and CI, DSR, PBO, WFE, max DD, turnover, breakeven cost, and the stage decision.

### Week 3: Paper trading the top 3 per desk
- Freeze code and parameters (git tag). Deploy the top 3 per desk that passed R1. If fewer than 3 pass, deploy fewer, plus the simple baseline as a control. **Do not lower the bar to fill slots.**
- Monitor each day: realized vs modeled slippage, order rejects, risk vetoes, data gaps, reconciliation breaks. No parameter changes; any change resets the paper clock.
- Low-frequency strategies (monthly momentum, value) will produce only 1-2 rebalances. Their value this week is purely operational.

### Week 4: Review and promotion decisions
- For each strategy, compare cost-adjusted paper P&L to the backtest's predicted distribution for a 2-week horizon. Pass means it lies within the 90% band, not that it made money.
- Decisions: **continue paper (R2 → finish 8+ weeks)**, demote to R1, or retire. **No strategy goes live after this sprint.** MinTRL arithmetic makes that impossible to justify.
- Write a post-mortem covering infrastructure issues, cost-model calibration (update η and the spread multipliers from observed fills), and the next research queue.

### Honest expectations per desk
- **FX:** this is the cleanest simulator: real-time demo prices and realistic spreads. Trend and carry are the best-documented edges, but they have **low Sharpe (about 0.3-0.7 per desk historically before diversification)**, multi-month dry spells, and few trades. In 4 weeks, expect P&L of about ±1-2% of desk equity that is indistinguishable from noise. Intraday FX ML strategies almost always die once costs are included.
- **Stocks:** paper fills are optimistic (no impact, IEX-only data). Factor strategies (momentum, low-vol) are real but slow, with monthly rebalancing. Intraday strategies (ORB, intraday momentum) produce more trades but have the weakest evidence and the most fill-sensitivity. Expect paper intraday results to overstate live results materially. Any intraday Sharpe above 2 on paper should be treated as an artifact.
- **Options:** the most misleading simulator. The indicative quotes are not real OPRA quotes, and the fill model is generous. Short-premium defined-risk spreads will very likely **show a high win rate (70-85%) and a positive month** in calm markets. This is exactly the pattern that hides tail risk. One volatility event can erase months of credits. Judge this desk on max-loss discipline and on P&L per unit of max loss, never on win rate.
- **ML in general:** the most likely positive contribution is better volatility forecasts and trade filtering. Expect direct return-prediction models to fail purged CV or to not survive 2× costs. That is a normal outcome, not a disappointment.

---

## 8. Legal and compliance notes (US individual)

**Not investment, legal or tax advice. Consult a licensed professional before trading real money.**

- **Paper trading:** no regulatory requirements beyond each platform's terms of service. Do not market paper results as a track record to others. Doing so could raise CFTC or SEC advertising and performance-presentation issues if it is ever used to solicit money.
- **Pattern day trader rule (important 2026 update):** the SEC approved FINRA's amendments to Rule 4210 on April 14, 2026. They **eliminate the PDT designation and its $25,000 minimum equity requirement** and replace them with an intraday margin standard that applies to all margin accounts. The effective date was June 4, 2026, with firms allowed to phase in until **October 20, 2027** ([FINRA Reg Notice 26-10](https://www.finra.org/rules-guidance/notices/26-10), [WilmerHale](https://www.wilmerhale.com/en/insights/client-alerts/20260423-sec-approves-amendments-to-finra-rule-4210-replacing-day-trading-margin-requirements-with-a-modernized-intraday-margin-standard), [FINRA investor insight](https://www.finra.org/investors/insights/intraday-margin-requirements)). Practical meaning: **some brokers may still enforce the old PDT rule until they migrate**, so check the specific broker. Cash accounts are still subject to Regulation T settlement rules (T+1) and good-faith or free-riding violations. Reg T margin (50% initial) still applies.
- **Options approval levels:** brokers approve levels from an application covering experience, income, net worth and objectives (FINRA Rule 2360). Typical ladder: L1 covered calls and cash-secured puts, L2 long options, L3 spreads, L4 naked. Alpaca's ladder ends at L3 for spreads ([Alpaca](https://docs.alpaca.markets/us/docs/options-trading-overview)). Defined-risk spreads need L3 and a margin account at most brokers. The options desk design here deliberately needs no more than L3.
- **Forex (retail, US):** only CFTC-registered RFEDs/FCMs that are NFA members may serve US retail clients. OANDA Corp is one. Leverage is capped at 50:1 on majors and 20:1 on others. NFA Compliance Rule 2-43 enforces FIFO and bans hedging the same pair. US residents cannot legally trade FX CFDs or crypto CFDs with offshore brokers.
- **Wash-sale rule (IRC §1091):** a loss is disallowed if substantially identical securities are bought within 30 days before or after the sale, including options on the same stock and purchases in an IRA. High-turnover automated equity strategies generate many wash sales. Brokers report wash sales per account, but the taxpayer must handle them across accounts. **Mark-to-market trader-tax-status election (§475(f))** removes wash-sale tracking but has strict requirements and deadlines. Get a CPA's opinion.
- **Tax treatment notes for later:** broad-based index options (SPX, XSP) are **Section 1256 contracts**: 60/40 long/short-term gains, marked to market at year-end, and not subject to wash-sale rules. SPY options are not. Spot FX gains fall under §988 (ordinary income) unless a §988(a)(1)(B) opt-out is made in a timely way.
- **Automation-specific:** follow each broker's API terms (rate limits, no abusive order messaging). Avoid manipulative patterns such as layering, spoofing or wash trading: in live markets these are illegal regardless of intent, so build guards against self-crossing orders now.

**Before any live money (checklist):**
1. Strategy completed R3 (3-6+ months paper) with cost-adjusted results consistent with the backtest, and the MinTRL math supports the observed Sharpe at 95% confidence, or the owner explicitly accepts the statistical uncertainty.
2. Independent code review of the risk manager and kill switches. Disaster-recovery test (power loss, network loss, broker outage) with positions open.
3. Live accounts opened with proper KYC, the appropriate options level, and a margin agreement where needed. Real-time data subscriptions (SIP/OPRA) in place.
4. Written risk policy: the owner's maximum capital at risk, which should be money the owner can afford to lose entirely, and the same loss limits as section 5, but tighter.
5. Tax setup reviewed by a CPA (wash sales, §1256, §988, possible trader tax status). Recordkeeping of every trade.
6. Start at ≤ 10% of the intended size for at least 3 months, and compare live vs paper slippage before any scale-up.
7. If the lab ever manages money for anyone else, registration issues apply (investment adviser or CTA/CPO). Stop and get counsel.

---

## Sources

**Platforms**
- Alpaca paper trading docs: https://docs.alpaca.markets/us/docs/paper-trading
- Alpaca paper onboarding: https://alpaca.markets/learn/start-paper-trading
- Alpaca index options in paper: https://alpaca.markets/blog/alpaca-introduces-index-options-paper-trading/
- Alpaca options Level 3: https://docs.alpaca.markets/us/docs/options-level-3-trading
- Alpaca options overview: https://docs.alpaca.markets/us/docs/options-trading-overview
- Alpaca historical option data and feeds: https://docs.alpaca.markets/us/docs/historical-option-data
- Alpaca indicative feed (forum): https://forum.alpaca.markets/t/what-is-the-indicative-pricing-feed-for-options/14595
- Alpaca rate limits (forum, staff): https://forum.alpaca.markets/t/is-there-a-way-to-increase-the-200-min-api-call-limit-for-the-trading-endpoint/18110
- OANDA v20 development guide (rate limits): https://developer.oanda.com/rest-live-v20/development-guide
- OANDA US leverage: https://help.oanda.com/us/en/faqs/account-types-and-leverage-us.htm
- QuantConnect OANDA guide: https://www.quantconnect.com/docs/v2/our-platform/live-trading/brokerages/oanda
- IBKR paper market data: https://ibkb.interactivebrokers.com/article/1719
- Tradier market data: https://docs.tradier.com/docs/market-data
- Tradier FAQ: https://docs.tradier.com/docs/faq
- TradersPost broker paper trading comparison: https://blog.traderspost.io/article/broker-paper-trading-comparison
- tastytrade sandbox: https://developer.tastytrade.com/sandbox
- tastytrade getting started: https://developer.tastytrade.com/getting-started
- NautilusTrader installation: https://nautilustrader.io/docs/latest/getting_started/installation

**Data**
- Dukascopy historical export: https://www.dukascopy.com/swiss/lv/marketwatch/historical/
- duka downloader: https://github.com/smorrel1/duka
- Free options data survey: https://davidariasfinance.com/scripts/free-options-data/
- Massive (Polygon) pricing summary: https://apicostcalc.com/blog/polygon-massive-rebrand-api-pricing.html

**Evidence and regulation**
- McLean & Pontiff (2016): https://www.gwern.net/doc/economics/2016-mclean.pdf
- Kelly & Xiu, "Financial Machine Learning" (NBER w31502): https://www.nber.org/system/files/working_papers/w31502/w31502.pdf
- Tidy Finance Gu-Kelly-Xiu replication: https://www.tidy-finance.org/blog/gu-kelly-xiu-replication/
- FINRA Regulatory Notice 26-10: https://www.finra.org/rules-guidance/notices/26-10
- FINRA intraday margin investor insight: https://www.finra.org/investors/insights/intraday-margin-requirements
- WilmerHale on SEC approval of Rule 4210 amendments: https://www.wilmerhale.com/en/insights/client-alerts/20260423-sec-approves-amendments-to-finra-rule-4210-replacing-day-trading-margin-requirements-with-a-modernized-intraday-margin-standard

**Literature (standard references, cited by author and year in the text):** Moskowitz, Ooi & Pedersen (2012, JFE); Hurst, Ooi & Pedersen (2017); Jegadeesh & Titman (1993, JF); Asness, Moskowitz & Pedersen (2013, JF); Daniel & Moskowitz (2016, JFE); Gatev, Goetzmann & Rouwenhorst (2006, RFS); Avellaneda & Lee (2010, QF); Engle & Granger (1987, Econometrica); Johansen (1991, Econometrica); Lustig, Roussanov & Verdelhan (2011, RFS); Koijen, Moskowitz, Pedersen & Vrugt (2018, JFE); Menkhoff et al. (2012, JFE); Carr & Wu (2009, RFS); Bakshi & Kapadia (2003, RFS); Moreira & Muir (2017, JF); Harvey et al. (2018, JPM); Hamilton (1989, Econometrica); Gao, Han, Li & Zhou (2018, JFE); Lou, Polk & Skouras (2019, JFE); Lucca & Moench (2015, JF); Frazzini & Pedersen (2014, JFE); Gu, Kelly & Xiu (2020, RFS); Fischer & Krauss (2018, EJOR); Corsi (2009, JFEc); Bailey & López de Prado (2012, 2014, J. Risk / JPM); Bailey, Borwein, López de Prado & Zhu (2017, J. Computational Finance); López de Prado (2018, *Advances in Financial Machine Learning*); Harvey, Liu & Zhu (2016, RFS); Lo (2002, FAJ); MacLean, Thorp & Ziemba (2011); Almgren et al. (2005, Risk). Zarattini et al. ORB work is SSRN (not peer-reviewed).

*Items not verified in this session's searches and flagged as "check before relying":* exact Tradier sandbox rate limits, HistData.com specifics, whether the OANDA US demo enforces FIFO and no-hedging automatically, and current Massive and Alpaca plan prices. Confirm these on the vendor sites at signup.
