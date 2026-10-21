# Arbitrage Desk: Research Report and Demo Scanner Spec

Prepared for the owner (US, age 35) by the Research Lab arbitrage analyst. Research date: 2026-10-21.

The scope is research plus a design for a DEMO (paper) scanner. Nothing here is a recommendation to trade real money.

---

## 0. Executive summary (the honest bottom line)

1. **Instant risk-free arbitrage that a retail account can actually capture is close to non-existent in liquid US markets in 2026.** Retail taker fees on US crypto venues run about 0.8–0.9% per side. Coinbase Advanced's US entry tier is reported at 0.50% maker / 0.90% taker as of Sept 2026, and Kraken Pro's base taker is up to 0.80%. Price gaps for BTC/ETH between Coinbase, Kraken and Gemini are usually a few basis points. On-chain data shows arbitrage profit per trade collapsing: Bitquery counted 139M arbitrage trades averaging about $0.69 surplus each, down more than 90% over six years. Professionals with VIP fees, co-location and pre-funded inventory take these spreads.
2. **The scanner will find many "gross" opportunities and very few "net" ones.** That result is the point of running DEMO mode first. The stats must be computed net of every fee, at executable order-book depth, and then re-checked after N seconds. Expect the still-valid rate on re-check to be low (often under 20–30%) for the fast types.
3. **The types that make real money for an individual are not instant.** They are inventory flips (Amazon FBA online arbitrage, eBay underpriced flips, books) and slow "risk arbitrage" (merger arb). Their margins are 10–30% per turn or a 4–8% annualized spread, they settle in weeks to months, and they carry real risk: returns, account suspensions, deal breaks.
4. **The prediction-market bundle and cross-venue checks (Kalshi, Polymarket US) are the most interesting "near-instant lock" for a scanner.** The edge is locked at trade time but paid out only when the event resolves. Fees run about 0.07 × P × (1−P) per contract on Kalshi and 0.0695 × p × (1−p) on Polymarket US. State legality is contested, and contract wording can differ between venues. Because the owner ruled out gambling, restrict this to non-sports markets and have the owner confirm he is comfortable with event contracts at all.
5. **The 8 picked for the demo scanner** (chosen for free or cheap data, automation allowed by the platform, and clean fee math):
   1. Kalshi intra-venue bundle arbitrage
   2. Kalshi vs. Polymarket US cross-venue
   3. Crypto funding-rate / basis cash-and-carry (US venues)
   4. Crypto cross-exchange spot (US venues)
   5. Crypto triangular on Kraken
   6. Stablecoin depeg monitor
   7. Merger-arbitrage spread tracker
   8. eBay underpriced-listing flip (eBay Browse API, optionally checked against Amazon via Keepa)

   The crypto types are in the demo mainly to measure how rarely they clear fees, not because they are expected to pay.

---

## 1. Ground rules and exclusions

**Excluded by the owner's rules or by law and platform terms:**

| Excluded | Why |
|---|---|
| Sports betting / matched betting / sportsbook arbitrage | Owner ruled out gambling. |
| Sports event contracts on Kalshi / Polymarket US | Functionally sports wagering, and the subject of active state litigation (NV, MA, MI, CT, AZ, IL). Demo uses non-sports markets only. |
| Amazon-to-eBay (or Amazon-to-Walmart) dropshipping | eBay bans dropshipping from other retailers. Walmart Marketplace requires the seller to be seller of record and does not allow fulfilling from another retailer's order with its packaging. Accounts get suspended. |
| API credit / API key resale (e.g., OpenAI) | OpenAI's Services Agreement says the customer "may not resell or lease access to its Account" and may not "buy, sell, or transfer API keys" to third parties ([OpenAI Services Agreement](https://openai.com/policies/services-agreement/)). It is allowed to build a product on the API and sell that, but that is a business, not arbitrage. |
| Gray-market software license keys | Under *Vernor v. Autodesk* (9th Cir. 2010) a user is a licensee rather than an owner when the license restricts transfer, so first-sale protection does not apply ([Wikipedia](https://en.wikipedia.org/wiki/Vernor_v._Autodesk,_Inc.), [EFF](https://www.eff.org/cases/vernor-v-autodesk)). Keys are often obtained by fraud or regional abuse, and chargeback risk is high. |
| Freight brokerage "rate arbitrage" | Legal only with FMCSA broker authority (MC number via OP-1, $300 fee, BOC-3, UCR) plus a **$75,000** BMC-84 bond or BMC-85 trust ([SupplyChain247 on the FMCSA rule](https://www.supplychain247.com/article/fmcsa_issues_final_rule_requiring_75000_bond_for_brokers_for_claims), [LicenseMap](https://getlicensemap.com/states/freight-broker/california)). It is an operating business with liability, not a scanner strategy. Small-parcel label resale needs a carrier or aggregator reseller agreement. |
| Pump schemes, insider trading, wash trading, bot-buying of tickets (federal BOTS Act), sneaker bots against retailer ToS | Illegal or bannable. |

These five rejected candidates are why the list of 20 below replaces some of the suggested examples. Prediction-market intra-venue bundle arbitrage was added as a cleaner variant.

---

## 2. The 20 candidate types: full evaluation

Scores: **Feasibility** (1–10) means how realistically the owner can execute legally and profitably at retail scale. **Speed** (1–10) means how fast profit is locked and settled; 10 is instant. Daily profit estimates are **realistic expected values after fees and before income tax**, averaged over time. Many days will be $0. Labor is not costed except where noted.

### 2.1 Merger arbitrage (risk arbitrage)

- **How it works:** After a cash acquisition is announced (e.g., $50/share), the target trades below the deal price (e.g., $48.50). Buy the target and collect the spread at close. For stock deals, also short the acquirer at the exchange ratio.
- **Legal / platform:** Fully legal in any US brokerage account. Shorting for stock-for-stock deals needs a margin account and borrow. Never trade on non-public deal information.
- **Capital:** Any amount. Diversify across 8 or more deals to survive a break.
- **Fees:** $0 commissions at most US brokers. SEC/FINRA TAF fees are pennies on sells. Short borrow fees apply to stock deals. Bid/ask spread. Tax: short-term gains taxed as ordinary income.
- **Net margin:** The median annualized US spread was about **7.7%** (Goldman Sachs, Aug 2025) and about **4%** (UBS, end-2025) ([Carmignac Q4 2025 letter](https://www.carmignac.com/en-gb/articles/carmignac-portfolio-merger-arbitrage-plus-letter-from-the-fund-managers-q4-2025-3610-12632)). The S&P Merger Arbitrage TR index returned **13.63% in 2025** and 2.64% YTD to 22 May 2026 ([YCharts ^SPMATR](https://ycharts.com/indices/^SPMATR)). The long-run strategy average for 1998–2022 was 4.4%/yr ([Carmignac](https://www.carmignac.com/en/articles/bumps-are-back-terminations-low-stars-align-for-merger-arbitrage-3412-11786)).
- **Settlement:** Months (deal close is typically 3–12 months away).
- **Risks:** A deal break can cost 20–40% on that position (asymmetric). Regulatory and antitrust delays cut the annualized return. Financing risk.
- **Data / APIs:** SEC EDGAR full-text search and submissions JSON (free; requires a User-Agent header with contact email; 10 req/s). 8-K Item 1.01, DEFM14A and SC TO-T filings mark deals. Quotes from a free or cheap feed (Stooq, Alpha Vantage free key, Finnhub free key, or broker API). Automation is allowed.
- **Scores:** Feasibility **8**, Speed **2**.
- **Daily profit (annualized 5–7% divided by 365, minus an expected break-loss allowance):** $100 → ~$0.01–0.02; $1k → ~$0.10–0.20; $10k → ~$1–2.

### 2.2 Amazon FBA online arbitrage (OA)

- **How it works:** Buy discounted items from online retailers (Walmart, Target, Kohl's clearance and similar), ship them to Amazon FBA, and sell at the Buy Box price.
- **Legal / platform:** Legal and permitted by Amazon in principle. In practice, **retail receipts are no longer accepted for ungating or authenticity reviews**, so sellers increasingly need distributor invoices or letters of authorization (LOAs). One inauthentic complaint can freeze the account and funds ([Seller Central forum: "Retail Arbitrage Is Allowed, But Amazon Rejects Retail Invoices"](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/b2ad0bb7-66d8-453f-b875-702c3e97892e), [EcomCircles guide](https://ecomcircles.com/blog/retail-arbitrage-amazon/)). Avoid gated and IP-sensitive brands. Never buy "ungating services", which are linked to forged invoices.
- **Capital:** $1k+ is practical. Overhead is the Professional plan at $39.99/mo plus tools (Keepa €29/mo; Keepa API from €49/mo).
- **Fees:** Referral fee ~15% for most categories. FBA fulfillment fee by size tier (2026 average increase ~$0.08/unit). A **3.5% fuel/logistics surcharge** on FBA fees since 17 Apr 2026. Inbound placement fee, monthly storage and aged-inventory surcharges (181+ days). Amazon prep services were discontinued 1 Jan 2026, so the seller preps or pays a prep center. Inbound shipping to the FC. Sales tax on purchases unless the seller holds a resale certificate. Income tax plus 15.3% self-employment tax on net ([Amazon 2026 fee update](https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026), [AMZPrep](https://amzprep.com/amazon-fba-fees/), [SellerSprite](https://www.sellersprite.com/en/blog/amazon-fba-fees-2026-complete-guide)).
- **Net margin:** OA sellers typically target ≥30% ROI and 15–25% margin before tax. Realized results after returns, stranded units and price tanks are commonly 10–20% of sale price (industry rule of thumb, no audited data).
- **Settlement:** Weeks. Inbound takes 1–3 weeks, the sale takes days to months, Amazon pays out on a ~14-day cycle, and Deliver-by-Date reserve holds apply.
- **Risks:** Buy Box price wars when many OA sellers chase the same lead. Returns. IP complaints. Suspension. Inventory stuck at FBA.
- **Data / APIs:** Keepa API (paid, token bucket; product request = 1 token/ASIN, +6 per offer page) ([Keepa docs](https://keepa.com/api-docs/plans-tokens.html)). Amazon SP-API (free with a seller account; getItemOffers, Product Fees API for exact fee estimates). Retailer prices come from affiliate feeds or manual sourcing; scraping retailers usually violates their ToS. Automating Amazon *data* via SP-API and Keepa is allowed. Auto-buying from retailers is not advisable.
- **Scores:** Feasibility **6**, Speed **3**.
- **Daily profit:** $100 → ~$0.20–0.50; $1k → ~$3–8; $10k → ~$25–70. Requires 10–25 hrs/week of labor at $10k.

### 2.3 eBay underpriced-listing flip ("sold vs. listed" gap)

- **How it works:** Find Buy-It-Now listings priced well below the recent sold median for the same product (GTIN/EPID). Buy, then relist with better photos and title, or bundle.
- **Legal / platform:** Legal. Buying and reselling is fine on eBay. Shill bidding and fee avoidance are prohibited.
- **Capital:** $100+.
- **Fees:** Final value fee ~**13.6%** of the total sale including shipping and sales tax for most categories, plus **$0.30 (≤$10) / $0.40 (>$10)** per order. Books/media ~15.3%. Sneakers >$150 ~8% ([size.ly calculator](https://www.size.ly/tools/ebay-fee-calculator), [HustleGotReal fee table](https://hustlegotreal.com/tools/ebay-fee-calculator/fees-by-category/)). Confirm on eBay's official fee page. Other costs: shipping both ways (buy-side shipping plus your outbound label), sales tax paid on the purchase, optional promoted-listing ad fee (2–10%). A 1099-K is issued above the reporting threshold.
- **Net margin:** Typically 15–35% on winners, minus duds and returns. Aim for ≥$15 absolute profit per item to make the labor worthwhile.
- **Settlement:** 1–4 weeks (buy, receive, relist, sell; payout 1–2 business days after funds are available).
- **Risks:** Condition misrepresentation by the seller. Your own buyer returns (eBay favors buyers). The comparable median being wrong.
- **Data / APIs:** eBay Browse API (free; **5,000 calls/day** default) for active listings. **Marketplace Insights API (sold items) is Limited Release**, available only to approved developers ([eBay call limits](https://developer.ebay.com/develop/get-started/api-call-limits), [Marketplace Insights overview](https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html)). For the reference price, use (a) the active-listing distribution of the same EPID, (b) Keepa Amazon price for the same UPC, or (c) the owner's manual Terapeak lookups in Seller Hub. Browse API automation is allowed within limits. Auto-purchase via the Order API is restricted.
- **Scores:** Feasibility **6**, Speed **4**.
- **Daily profit:** $100 → ~$0.50–1; $1k → ~$3–10; $10k → ~$15–50. Opportunity-limited more than capital-limited.

### 2.4 Book arbitrage (marketplace to buyback vendors)

- **How it works:** Buy used textbooks cheaply (thrift, library sales, eBay/Amazon/AbeBooks listings) where the best buyback quote across 30–40 vendors (BooksRun, eCampus, ValoreBooks and others, compared on BookScouter) exceeds cost plus shipping.
- **Legal / platform:** Legal. Watch for international editions and counterfeits, which vendors reject.
- **Capital:** $50+.
- **Fees:** Buy-side shipping. Buyback vendors usually provide free prepaid labels. Condition downgrades (quotes assume "excellent" condition). Payment by PayPal or check.
- **Net margin:** $3–15 per book on winners. Seasonal: buyback quotes peak in August/September and January.
- **Settlement:** 1–3 weeks. Payment typically 1–2 business days after the vendor receives and inspects ([BookScouter vendor page](https://bookscouter.com/vendors/876-textbooktiger), [MoneyPantry review](https://moneypantry.com/bookscouter-review/)).
- **Risks:** Quote changes before the book arrives (most vendors honor quotes for ~2 weeks). Rejection for condition.
- **Data / APIs:** No documented public BookScouter API was found (it may offer a partner API on request). ISBN prices on Amazon come via Keepa or SP-API. eBay Browse API covers book listings. Scraping BookScouter likely violates its ToS, so ask for API access.
- **Scores:** Feasibility **6**, Speed **3**.
- **Daily profit:** $100 → ~$0.50–1; $1k → ~$2–6; $10k → ~$5–20 (sourcing-limited).

### 2.5 Prediction market: intra-venue bundle (Kalshi)

- **How it works:** In a mutually exclusive, exhaustive event (e.g., "CPI YoY range", "Fed rate after meeting"), buy YES on every outcome when the sum of best YES asks plus fees is below $1.00. Alternatively buy NO on every outcome when the sum of NO asks is below (N−1) dollars. Exactly one outcome pays $1, so the profit is locked at entry.
- **Legal / platform:** Kalshi is a CFTC-designated contract market (DCM) and derivatives clearing organization (DCO). API trading is explicitly supported. State legality is **contested, chiefly for sports contracts**, and the CFTC has sued states to defend preemption. Owner constraint: **non-sports markets only.** He should also confirm he does not consider event contracts "gambling". Account eligibility depends on the owner's state.
- **Capital:** $100+. Capital is locked until resolution.
- **Fees:** Taker fee = **ceil(0.07 × C × P × (1−P))**, rounded up to the cent, with a maximum of 1.75¢/contract at P = 0.50. Makers pay 0 or a reduced rate on some series (sources conflict; read the official schedule). Settlement, ACH deposits and withdrawals reported free ([QuantVPS](https://www.quantvps.com/blog/kalshi-fees-explained), [BotForKalshi](https://www.botforkalshi.com/blog/kalshi-fees-explained), [River Markets](https://www.rivermarkets.com/insights/kalshi-fees.html)). Rounding up per order makes many small orders expensive. Tax treatment of event contracts is unsettled (possibly Section 1256 or ordinary income); flag for a CPA.
- **Net margin:** When present, typically 0.5–3% of capital deployed. Opportunities are infrequent and thin (a few contracts deep).
- **Settlement:** The profit is locked instantly. Cash is paid at resolution (hours to months).
- **Risks:** Partial fills leave you holding a directional position (leg risk). Market maker quotes move. Rule ambiguity. Capital lock-up reduces the annualized return.
- **Data / APIs:** Kalshi Trade API v2. Public market data and order books are readable without a key (per third-party docs; verify). Rate limits are tiered at roughly 10–20 rps for basic access ([Zuplo](https://zuplo.com/blog/2025/04/02/kalshi-api), [docs.rs kalshi-pmx](https://docs.rs/kalshi-pmx)). Automation is allowed.
- **Scores:** Feasibility **5**, Speed **9** to lock / **3** to settle.
- **Daily profit:** $100 → $0–0.10; $1k → $0–1; $10k → $0–8 (opportunity-limited).

### 2.6 Crypto funding-rate / basis cash-and-carry (US-permitted venues)

- **How it works:** Buy spot BTC/ETH and short an equal notional of a perpetual-style or dated future. Collect positive funding or the futures premium. The position is delta-neutral.
- **Legal / platform:** US-legal on CFTC-regulated venues. Coinbase Financial Markets "US perpetual-style futures" (nano BTC 0.01, nano ETH 0.10; 5-year expiry; 24/7; funding accrues hourly and settles twice daily) ([Coinbase funding mechanism](https://help.coinbase.com/en/derivatives/perpetual-style-futures/funding-rate), [FOW](https://www.fow.com/insights/coinbase-hails-arrival-of-perpetual-style-futures-in-us)). CME BTC/ETH futures via a futures broker. A secondary source reports the CFTC approved a Kalshi BTCPERP in May 2026 (verify). Offshore perp venues (Binance global, Bybit, OKX global) are **not** allowed for US persons.
- **Capital:** Practical minimum ~$2–5k (nano contract ≈ 0.01 BTC). Margin buffer needed.
- **Fees:** Spot taker up to 0.90% at Coinbase's US entry tier ([CryptoDaily, Sept 2026](https://cryptodaily.co.uk/2026/09/coinbase-advanced-fees-usdc-vip-tiers)). Futures fees are per-contract and modest (check CFM schedule). Four legs round-trip (buy spot, sell future, unwind both). Funding can turn negative (it was the most negative since 2023 in April 2026). Taxes: Section 1256 60/40 treatment on regulated futures vs. short-term on spot, which can create a mismatch.
- **Net margin:** Glassnode reports the **3-month annualized basis has been below the 2-year Treasury yield every month since Feb 2026**. Funding ran ~8–15% annualized in some August 2026 windows, and the BTC funding rate was ~0.01% per period on 20 Oct 2026 ([TFTC/Glassnode](https://www.tftc.io/bitcoin-futures-basis-below-treasury-yields-2026), [ConvexTrade](https://convextrade.com/metrics/btc-funding), [CF Benchmarks KFRI](https://www.cfbenchmarks.com/data/indices/KFRI)). At retail spot fees of ~1.8% round trip, you need **months** of positive funding just to break even, while T-bills pay more risk-free.
- **Settlement:** Funding accrues hourly. The real profit is realized over weeks or months.
- **Risks:** Funding flips negative. Liquidation of the short in a squeeze if margin is thin. Basis drift between spot venue and futures index. Exchange counterparty risk.
- **Data / APIs:** Coinbase public Exchange/Advanced REST (public endpoints ~10 rps/IP, burst 15) ([Coinbase rate limits](https://docs.cdp.coinbase.com/exchange/rest-api/rate-limits)). CFM product and funding data. CF Benchmarks funding index. Automation is allowed.
- **Scores:** Feasibility **5**, Speed **6** (accrual) / **3** (net profit).
- **Daily profit:** $100 → ~$0 (below contract size); $1k → ~$0–0.10; $10k → ~$0.30–3, often negative after fees in the current regime.

### 2.7 Prediction market: cross-venue (Kalshi vs. Polymarket US)

- **How it works:** When the same event is listed on both venues, buy YES on one and NO on the other when the combined cost plus both taker fees is below $1.
- **Legal / platform:** Both are CFTC DCMs. Polymarket US runs through QCX LLC / QC Clearing. Polymarket US launched to Americans in Dec 2025 / May 2026 (sources differ). It is restricted in some states: Nevada consistently, plus others under litigation (MA, MI, AZ, IL, CT; a single source claims Minnesota made it a felony from 1 Aug 2026) ([OddsAssist](https://oddsassist.com/prediction-markets/polymarket-us-states/), [Tech-Insider](https://tech-insider.org/prediction-markets/is-polymarket-legal-in-the-usa/)). **The international Polymarket (polymarket.com, on-chain) is not for US persons.** It can serve as a read-only price reference but must not be traded. Non-sports markets only.
- **Capital:** $200+ split across both venues, which doubles the capital you must pre-fund.
- **Fees:** Kalshi as in 2.5. **Polymarket US taker = 0.0695 × C × p × (1−p)** since 17 Sept 2026, with category-specific coefficients (e.g., 0.10 for table tennis) and maker 0 ([CFTC filing 21 Sept 2026](https://www.cftc.gov/filings/orgrules/rules09212628660.pdf), [CFTC filing 29 Sept 2026](https://www.cftc.gov/filings/orgrules/rules09292630356.pdf)). The break-even gap is about **3.5¢ per pair at 50¢ prices** ([TradoxVPS](https://tradoxvps.com/prediction-market-arbitrage-in-2026/)).
- **Net margin:** 0.5–3% when present.
- **Settlement:** Locked at entry. Paid at resolution on each venue separately.
- **Risks:** **Resolution-rule mismatch**, the biggest risk: the "same" event can be worded or sourced differently, so both legs can lose. Leg risk. Withdrawal timing. State eligibility.
- **Data / APIs:** Kalshi API. Polymarket US API (programmatic trading reportedly offered; check developer terms). Event matching requires a curated mapping table, which should be human-reviewed.
- **Scores:** Feasibility **4**, Speed **8** lock / **3** settle.
- **Daily profit:** $100 → $0–0.10; $1k → $0–1; $10k → $0–10.

### 2.8 Clearance / retail-store to eBay

- **How it works:** Buy in-store clearance (Walmart, Target, Home Depot, Lowe's) and sell on eBay. Apps such as BrickSeek-type inventory checkers help.
- **Legal / platform:** Legal. Some retailers limit quantities or refuse resellers.
- **Capital:** $100+.
- **Fees:** eBay fees as in 2.3, plus shipping, supplies, mileage and sales tax on purchase.
- **Net margin:** 20–40% on good finds. Lots of misses.
- **Settlement:** 1–6 weeks.
- **Risks:** Dead stock. Returns. Time.
- **Data / APIs:** Little legitimate automation; retailer inventory scraping violates most ToS. eBay Browse API can price the item. Mostly manual work (owner's phone).
- **Scores:** Feasibility **6**, Speed **3**.
- **Daily profit:** $100 → ~$0.50–1.50; $1k → ~$3–10; $10k → ~$10–35 (labor-bound).

### 2.9 Local flips (Facebook Marketplace / Craigslist / OfferUp)

- **How it works:** Buy underpriced local items (furniture, tools, electronics) and resell locally or on eBay.
- **Legal / platform:** Legal to buy and sell. **Automated scraping is prohibited.** Craigslist ToS bans scrapers and has won big judgments: $60.5M vs RadPad and a $31M settlement with Instamotor. Meta's terms ban automated collection ([ConductAtlas: Craigslist ToS](https://conductatlas.com/platform/craigslist/craigslist-terms-of-use/prohibition-on-scraping-and-automated-access/), [Proskauer](https://www.proskauer.com/blog/ending-data-scraping-dispute-craigslist-reaches-31m-settlement-with-instamotor-08-24-2017)).
- **Capital:** $50+.
- **Fees:** FB local pickup has no fee. FB shipped orders carry a selling fee of ~10%. Craigslist is free. Gas and time apply. Cash is often tax-reportable as business income.
- **Net margin:** 30–100% per item possible, but it is labor-heavy.
- **Settlement:** Days.
- **Risks:** Safety on meetups. Scams. Stolen goods. Time.
- **Data / APIs:** No legitimate automation. Use the platforms' built-in saved-search notifications on the owner's phone.
- **Scores:** Feasibility **6** (manual) / **1** (automated), Speed **5**.
- **Daily profit:** $100 → ~$1–5; $1k → ~$5–25; $10k → not capital-scalable (labor cap).

### 2.10 Price-mistake deals

- **How it works:** Catch mispriced listings (e.g., $40 for a $400 item), buy, and resell or keep.
- **Legal / platform:** Buying is legal. US retailers are generally **not obligated to honor obvious pricing errors**: an advertised price is an invitation to offer, and retailer terms let them cancel before shipment. Retailers routinely cancel; Corsair cancelled orders for a mispriced DDR5 kit in Jan 2026 ([3DTested](https://www.3dtested.com/pc-components/ram/corsair-cancels-usd240-48gb-ddr5-memory-kit-orders-due-to-pricing-error-companys-blunder-ignites-shopper-uproar-over-botched-ram-deal), [Consumerist](https://consumerist.com/tag/to-clarify/index.html)). Using bots or many accounts to exceed purchase limits can get accounts closed.
- **Capital:** Small per deal.
- **Fees:** Resale fees (eBay ~13.6%). Card holds while an order is pending.
- **Net margin:** Huge when honored (50%+), but most big errors are cancelled.
- **Settlement:** Weeks (shipping plus resale).
- **Risks:** Cancellation (the most likely outcome). Account bans for "reseller" behavior.
- **Data / APIs:** Slickdeals public RSS feeds, Keepa price-drop alerts, camelcamelcamel. Reading these feeds is allowed. Auto-checkout is not advisable.
- **Scores:** Feasibility **4**, Speed **4**.
- **Daily profit:** Lumpy. Long-run average ~$0–3/day at any capital level, because the constraint is availability, not capital.

### 2.11 Gift-card discount plus cashback stacking

- **How it works:** Buy discounted gift cards (CardCash/Raise sell at ~3–15% off), pay with a rewards card (1–5%), and shop through a cashback portal (1–10%). Use the result to source inventory for 2.2, 2.3 or 2.8. **Reselling gift cards for cash is negative-margin:** CardCash pays ~70–92% of face, and Raise sellers pay ~15% commission ([Yakima Herald roundup 2026](https://www.yakimaherald.com/news/nation_and_world/business/best-places-to-sell-gift-cards-for-cash-instantly-2026/article_25e8dae9-e593-58f5-aa69-7c074aa8f211.html), [MillennialMoneyMan](https://millennialmoneyman.com/sell-gift-cards/)).
- **Legal / platform:** Legal. Portals often exclude gift-card purchases from cashback. Manufactured spending can get credit cards closed. Gift-card fraud and money-laundering red flags apply (never buy from unverified sellers).
- **Capital:** Any.
- **Fees:** Discount spreads, card fees, and the risk of a drained or invalid card.
- **Net margin:** 5–15% cost reduction on purchases you would make anyway. Treat it as a margin booster for inventory types, not standalone arbitrage.
- **Settlement:** Cashback posts in 30–90 days.
- **Risks:** Card already drained. Portal not tracking. Clawbacks.
- **Data / APIs:** No public APIs for most portals or gift-card exchanges (Rakuten offers APIs to publishers only). Mostly manual.
- **Scores:** Feasibility **5**, Speed **4**.
- **Daily profit (incremental savings):** $100 → ~$0.02; $1k → ~$0.20–0.40; $10k → ~$2–4.

### 2.12 Crypto cross-exchange spot (US venues)

- **How it works:** Buy an asset on venue A, where the ask is lower, and sell simultaneously on venue B, where the bid is higher. Balances must be pre-funded on both sides; rebalance later.
- **Legal / platform:** Legal on US-licensed venues (Coinbase, Kraken, Gemini, Bitstamp-by-Robinhood, Crypto.com US). API trading is allowed.
- **Capital:** $1k+ per venue. Pre-funding doubles the capital you need.
- **Fees:** Taker at retail entry tiers: Coinbase Advanced US **0.50% maker / 0.90% taker** (reported Sept 2026), Kraken Pro **up to 0.80% taker** (official page updated 1 Oct 2026; tier by volume *or* assets on platform since July 2026) ([Kraken support](https://support.kraken.com/articles/201893638-fee-schedule), [Kraken fees summary](https://www.datawallet.com/crypto/kraken-fees-explained)). The round-trip hurdle is **~1.5–1.7%** at entry tiers. Other costs: rebalancing withdrawals (network fee per asset), ACH free / wire $. Tax: every leg is a taxable disposal; Form 1099-DA reports gross proceeds for 2025 and basis from 2026 ([Beancount 1099-DA guide](https://beancount.io/blog/2026/05/10/form-1099-da-digital-asset-broker-reporting-2026-crypto-investors-cost-basis-form-8949-guide)).
- **Net margin:** Typical major-pair spreads between big venues are far below 0.2%. Vendor analyses quote 0.1–2% spreads and 0.05–1.5% net *with* low fees, but those figures do not apply to retail tiers ([Opportuna](https://opportuna.io/blog/is-arbitrage-profitable), [BJF](https://bjftradinggroup.com/crypto-arbitrage/)). An academic CEX/DEX study found bots earning 6–33% monthly in 2023–24 windows, but only about $20k total ([ScienceDirect 2026](https://www.sciencedirect.com/science/article/pii/S0378426626000956)).
- **Settlement:** Instant if pre-funded. Rebalancing takes minutes to hours.
- **Risks:** Leg risk (one side fills, the other moves). Withdrawal suspensions. Gaps on illiquid alt pairs are usually caused by halted deposits or withdrawals and cannot be closed.
- **Data / APIs:** Coinbase, Kraken and Gemini public REST and WebSocket (free). Automation is allowed.
- **Scores:** Feasibility **3** (at retail fees), Speed **9**.
- **Daily profit:** $100 → $0; $1k → ~$0; $10k → ~$0–2 (rare windows during volatility).

### 2.13 Crypto triangular (single venue, e.g., Kraken)

- **How it works:** A three-leg loop such as USD→BTC→ETH→USD on one exchange, when the product of the rates exceeds 1 plus fees.
- **Legal / platform:** Legal. API allowed.
- **Capital:** $100+.
- **Fees:** **Three taker fees**: ~2.4% at Kraken base, ~2.7% at Coinbase US base. Maker legs cut fees but add execution risk.
- **Net margin:** Effectively **zero** at retail tiers. Market makers keep cross rates aligned within a few bps.
- **Settlement:** Instant.
- **Risks:** Leg risk. Minimum order sizes.
- **Data / APIs:** Kraken public order books (free).
- **Scores:** Feasibility **2**, Speed **10**.
- **Daily profit:** $0 at all three capital levels at retail fees. Included in the demo only as a fee-hurdle teaching tool.

### 2.14 Stablecoin depeg arbitrage

- **How it works:** When USDC/USDT/PYUSD trades below $1 on an exchange, buy it and redeem at par through the issuer or a 1:1 exchange conversion. Alternatively hold it until the peg recovers.
- **Legal / platform:** Legal. Direct issuer redemption (Circle Mint) is for **qualified businesses**. Retail relies on exchange conversions, and Coinbase paused USDC conversions during the March 2023 weekend. The GENIUS Act (2025) federal stablecoin framework strengthens redemption at par for permitted issuers.
- **Capital:** Any amount.
- **Fees:** Trading fee to buy the discounted coin, plus redemption or conversion fees, if any.
- **Net margin:** Near zero almost always. Large only in crises: USDC hit ~$0.87 on 11 March 2023 when $3.3B of reserves were at SVB, and recovered within days ([EigenPhi](https://eigenphi.substack.com/p/usdc-depegging-victims-signals-and-opportunities), [The Block](https://www.theblock.co/post/224172/usdc-stablecoin-market-cap-plunges)).
- **Settlement:** Hours to days, depending on redemption channels.
- **Risks:** **It is not risk-free.** A depeg happens because par is in question, so you are betting on recovery.
- **Data / APIs:** Kraken USDC/USD, USDT/USD and PYUSD/USD, and Coinbase public books (free).
- **Scores:** Feasibility **3**, Speed **8**.
- **Daily profit:** ~$0 on normal days at any capital. An event-driven tail, perhaps once in several years.

### 2.15 Liquidation pallets (B-Stock, Liquidation.com, Direct Liquidation)

- **How it works:** Buy returns or overstock pallets ($300–1,000+), then sort, test and resell piecemeal.
- **Legal / platform:** Legal. B-Stock marketplaces require business verification. Middlemen re-sell "Amazon return pallets" at markups (one case: a $400 lot resold as $650) ([Closo](https://closo.co/blogs/inventory-liquidation/how-to-buy-amazon-returns-pallets)).
- **Capital:** $500–5,000 plus storage space.
- **Fees:** Buyer premium, freight ($150–400+ LTL), disposal of junk, and resale fees.
- **Net margin:** Vendor claims are 30–60%. Realistic outcomes range from a loss to ~30%, with high variance; defect rates of ~30% are often cited, unverified.
- **Settlement:** Weeks to months.
- **Risks:** Manifest inaccuracy. Dead stock. Space and time.
- **Data / APIs:** B-Stock has no public buyer API. Manifests are downloadable per auction. eBay Browse and Keepa can price manifest lines (this automation is fine).
- **Scores:** Feasibility **4**, Speed **2**.
- **Daily profit:** $100 → n/a; $1k → ~$0–10 (high variance); $10k → ~$0–60.

### 2.16 Cross-marketplace (Amazon ↔ Walmart Marketplace) with owned inventory

- **How it works:** List the *same owned inventory* on Amazon and Walmart Marketplace, and route units to whichever channel nets more. This is the only legitimate form of "Amazon to Walmart"; fulfilling Walmart orders by buying on Amazon is prohibited dropshipping.
- **Legal / platform:** Legal with owned inventory. Walmart Marketplace requires an approved seller application with eligibility criteria.
- **Fees:** Walmart referral ~6–15% by category (default 15%). WFS fulfillment from $3.45 (≤1 lb). Storage ~$0.75/cu ft/mo. 2026 New-Seller Savings: 20–40% off referral fees on early GMV and 10% off WFS up to $2k ([Walmart New-Seller Savings](https://marketplace.walmart.com/nss-influencer), [Feedvisor](https://feedvisor.com/university/walmart-seller-fees/)).
- **Net margin:** A 2–10% uplift over single-channel selling. It is a margin optimizer, not arbitrage.
- **Settlement:** Weeks.
- **Risks:** Walmart account approval. Inventory split between FBA and WFS.
- **Data / APIs:** Walmart Marketplace API and Amazon SP-API (both free with seller accounts; owner keys).
- **Scores:** Feasibility **4**, Speed **3**.
- **Daily profit:** Incremental to 2.2 only: $1k → ~$0.20–1; $10k → ~$2–8.

### 2.17 Sneaker / collectible resale (StockX, GOAT, eBay)

- **How it works:** Buy at retail or below market (drops, outlet sales) and sell on StockX/GOAT or eBay Authenticity Guarantee.
- **Legal / platform:** Legal. **Bots and multiple accounts on Nike/SNKRS and retailer raffles violate their ToS** and lead to cancellations and bans.
- **Capital:** $200+.
- **Fees:** StockX ~7–9% seller fee by level plus 3% processing (unverified; sources conflict). GOAT 9.5% commission at Level 1 down to 7.5%, plus a seller fee and a **2.9% cash-out fee** ([GOAT fees](https://www.goat.com/en-gb/fees), [Closo StockX breakdown](https://closo.co/blogs/blog/stockx)). eBay is 8% for sneakers over $150. Shipping is often prepaid by the platform.
- **Net margin:** 0–20% on hyped items. Many releases now resell at or below retail.
- **Settlement:** 1–3 weeks (authentication, then payout).
- **Risks:** Market collapse in hyped items. Failed authentication. Raffle losses are an opportunity cost.
- **Data / APIs:** StockX has a seller API with approval. GOAT has no public API. eBay Browse covers listings. Scraping StockX or GOAT violates their ToS.
- **Scores:** Feasibility **3**, Speed **3**.
- **Daily profit:** $100 → ~$0–0.50; $1k → ~$0–5; $10k → ~$0–30.

### 2.18 Concert and event ticket resale (non-sports)

- **How it works:** Buy at face value at onsale and resell on StubHub, SeatGeek or Ticketmaster resale.
- **Legal / platform:** It varies by state and is changing fast. The federal **TICKET Act** (all-in pricing, disclosure, speculative-listing limits) had not become law as of April 2026 per CRS, and it has no price cap. The federal **BOTS Act** bans bot purchasing. **Vermont** caps resale at 110% at qualifying independent venues from 1 July 2026. **D.C.** caps live-entertainment resale at face +10% from 1 Jan 2027 (sports excluded; verify enactment). **Maine** LD 913 caps resale marketplace fees at 10% and bans speculative listings. New York and Massachusetts caps are proposed; verify. The FTC all-in fee rule has been in effect since 12 May 2025, and StubHub settled with the FTC for $10M in April 2026 ([TicketNews July 2026](https://www.ticketnews.com/2026/07/ticket-resale-price-caps-for-concerts-a-comprehensive-analysis/), [Ticksights 2026 state roundup](https://www.ticksights.com/us-state-ticket-resale-laws-2026/), [Vermont H.512](https://termsandconditionstemplate.com/vermont-ticket-resale-price-cap-h512-2026)). Many tickets are non-transferable or have transfer restrictions in Ticketmaster SafeTix.
- **Capital:** $200+.
- **Fees:** Seller fee ~10–15% (StubHub ~10–15%, SeatGeek ~10%), plus card fees ([Terms.law StubHub](https://terms.law/ToS-Watchdog/event-ticketing/stubhub/), [Terms.law SeatGeek](https://terms.law/ToS-Watchdog/event-ticketing/seatgeek/)).
- **Net margin:** Negative to +100%. This is speculation on demand, not arbitrage.
- **Settlement:** Payout after the event (days to months).
- **Risks:** Price collapse near the event. Cancellations. Account limits.
- **Data / APIs:** SeatGeek has a public platform API (listings). Ticketmaster Discovery API (events, not resale prices). StubHub has no general public API.
- **Scores:** Feasibility **3**, Speed **2**.
- **Daily profit:** $100 → ~$0; $1k → ~$0–5; $10k → ~$0–40 (high variance).

### 2.19 ETF price vs. NAV (premium/discount); closed-end fund discounts

- **How it works:** When an ETF trades away from its NAV, authorized participants (APs) create or redeem shares to close the gap.
- **Legal / platform:** Legal. **Retail cannot create or redeem.** Only APs (large broker-dealers) can, so for retail this is a mean-reversion trade, not arbitrage ([AlphaArchitect](https://alphaarchitect.com/arbitrage-and-the-trading-costs-of-etfs/), [VanEck AP explainer](https://www.vaneck.com/at/en/authorized-participants)). Closed-end fund discounts have no creation/redeem mechanism and can persist for years.
- **Capital:** Any amount.
- **Fees:** $0 commission, bid/ask spread.
- **Net margin:** US equity ETFs' premiums and discounts are typically a few bps. Bond, EM, commodity and some crypto ETFs show wider gaps during stress.
- **Settlement:** T+1.
- **Risks:** The gap persists or widens. iNAV can be stale (foreign holdings, bond pricing).
- **Data / APIs:** Issuers publish daily NAV and premium/discount history (SEC Rule 6c-11 requires website disclosure). iNAV tickers are available through some quote feeds. Automation is allowed.
- **Scores:** Feasibility **2**, Speed **5**.
- **Daily profit:** ~$0 expected at all capital levels. Useful as a watch-only signal.

### 2.20 Expired domain name flipping

- **How it works:** Backorder or catch expiring domains (ExpiredDomains.net, GoDaddy Auctions, DropCatch) and list them on Afternic, Sedo or Dan.
- **Legal / platform:** Legal unless the domain is trademark-infringing, which invites UDRP and ACPA lawsuits.
- **Capital:** $10–100 per domain plus renewals.
- **Fees:** .com wholesale ~$10.26/yr after the registry increase. Afternic commission **25%** standard, or **15%** if pointed at GoDaddy Aftermarket nameservers, plus 5% for Boost ([Afternic pricing](https://www.afternic.com/legal/agreements/pricing-and-fees), [GoDaddy help](https://www.godaddy.com/help/what-is-list-for-sale-27761)). Payouts take 15–30 days.
- **Net margin:** Portfolio annual sell-through is commonly ~1–2%. Most domains never sell, so renewals erode returns ([Namefi](https://namefi.io/r/en/blog/domain-renewal-costs-and-sell-through-rate)).
- **Settlement:** Months to years.
- **Risks:** Carrying cost. Trademark claims.
- **Data / APIs:** ExpiredDomains.net (free with login, scraping restricted), GoDaddy Auctions API (limited), registrar APIs.
- **Scores:** Feasibility **2**, Speed **1**.
- **Daily profit:** Negative to ~$0 expected for beginners at any capital level.

---

## 3. (a) Ranking of the 20 and the 8 picked for the demo

Ranking combines realistic net expected value for an individual, legality and account safety, capital efficiency, and labor. "Demo fit" means it can be scanned automatically with free or cheap, ToS-compliant data and has a clean fee model.

| # | Type | Feas. | Speed | Demo fit | One line |
|---|---|---|---|---|---|
| 1 | Merger arbitrage | 8 | 2 | Yes | Legal, cheap data (EDGAR), 4–8% annualized spreads. Slow, with deal-break tail risk. |
| 2 | Amazon FBA online arbitrage | 6 | 3 | Partial (Keepa/SP-API paid or owner keys) | The most proven individual money-maker (10–20% net), but gating and suspension risk are rising and labor is high. |
| 3 | eBay underpriced-listing flip | 6 | 4 | Yes (Browse API free) | Real 15–35% margins on finds. Sold data API is restricted, so reference prices are approximate. |
| 4 | Book arbitrage | 6 | 3 | Partial | Small, steady per-book profit with seasonal peaks. No public buyback API. |
| 5 | Kalshi intra-venue bundle | 5 | 9/3 | Yes | Locks the edge instantly, paid at resolution. Rare and thin. Non-sports only. |
| 6 | Crypto funding/basis carry (US) | 5 | 6/3 | Yes | Delta-neutral, but the 2026 basis is below T-bill yields and retail spot fees eat it. |
| 7 | Kalshi vs Polymarket US cross-venue | 4 | 8/3 | Yes | Break-even ~3.5¢ per pair. Resolution-mismatch and state-eligibility risk. |
| 8 | Clearance/retail to eBay | 6 | 3 | No (manual) | Good margins on finds, but no compliant automation. |
| 9 | Local flips (FB/CL) | 6 | 5 | No (scraping banned) | Highest per-hour return for small capital, all manual. |
| 10 | Gift-card/cashback stacking | 5 | 4 | No | A 5–15% cost booster for inventory types. Gift-card resale for cash loses money. |
| 11 | Price-mistake deals | 4 | 4 | Watch-only (RSS) | Lumpy, mostly cancelled. |
| 12 | Liquidation pallets | 4 | 2 | No | High variance, space and labor intensive. |
| 13 | Cross-marketplace Amazon↔Walmart (owned inventory) | 4 | 3 | Later | A margin optimizer for 2.2, not standalone. Walmart dropshipping from Amazon is prohibited. |
| 14 | Crypto cross-exchange spot | 3 | 9 | Yes | Instant, but the ~1.5–1.7% retail fee hurdle means it almost never clears. |
| 15 | Stablecoin depeg | 3 | 8 | Yes (monitor) | Zero most days. Crisis-only, and not truly risk-free. |
| 16 | Sneakers/collectibles | 3 | 3 | No | Hype has faded. Bots violate ToS. |
| 17 | Event tickets (non-sports) | 3 | 2 | No | Speculation, with a patchwork of state caps. |
| 18 | Crypto triangular | 2 | 10 | Yes (teaching) | Three taker fees (~2.4%+) mean it is never profitable at retail tiers. |
| 19 | ETF vs NAV | 2 | 5 | Watch-only | Retail cannot create/redeem, so it is not true arbitrage. |
| 20 | Expired domain flipping | 2 | 1 | No | 1–2% annual sell-through, so renewals eat returns. |

**The 8 picked for the DEMO scanner:**

1. Kalshi intra-venue bundle (#5)
2. Kalshi vs Polymarket US cross-venue (#7)
3. Crypto funding/basis carry on US venues (#6)
4. Crypto cross-exchange spot on US venues (#14)
5. Crypto triangular on Kraken (#18)
6. Stablecoin depeg monitor (#15)
7. Merger-arb spread tracker (#1)
8. eBay underpriced-listing flip (#3), with optional Keepa cross-check

**Why the picks differ from the top of the ranking:** The demo scanner needs machine-readable, ToS-compliant feeds and deterministic fee math. Amazon OA (#2) and books (#4) rank higher for real money but need paid or owner keys. Add them in phase 2 once the owner has Keepa and an Amazon seller account (SP-API). Including the crypto types (#14, #18) is deliberate: they produce the "found a lot gross, almost nothing net" evidence the owner should see before funding anything.

---

## 4. (b) Scanner design

### 4.1 Architecture

```
scheduler ──> fetchers (per type) ──> normalizer ──> opportunity engine (gross → fee model → net, depth-aware)
                                                          │
                                                          ├─> opportunity log (JSONL / SQLite)
                                                          └─> recheck queue (t + N seconds) ──> recheck worker
stats aggregator (rolling windows) ──> stats.json  ──> dashboard
```

- **Language:** Python 3.11 (`httpx`, `websockets`, `pydantic`) or Node 20. SQLite for the log; a single file is fine for the demo.
- **Simulation principle:** Every "would-have" trade is sized to **executable depth** by walking the order book. Fees are charged at **taker** rates unless the rule is explicitly a maker strategy. A **latency penalty** (re-read the book after `exec_latency_ms`) is applied before booking. A trade is booked once per unique opportunity (dedupe key) per cooldown window, so persistent quotes are not counted 1,000 times.
- **All fee parameters live in `fees.yaml`**, with source URL and date, so they can be updated as schedules change. Several 2026 fee figures above conflict between sources, so the config is the single place to correct them.

### 4.2 Per-type specification

**T1 – Kalshi intra-venue bundle**
- Fetch: `GET /trade-api/v2/events?status=open&with_nested_markets=true` (filter category ≠ Sports), then `GET /markets/{ticker}/orderbook` for each market in mutually-exclusive events. Poll every 15–30 s, staying within the rate tier.
- Rule (YES bundle): for size q (walk each book), `cost = Σ_i ask_yes_i(q) + Σ_i fee_kalshi(q, ask_yes_i)`. Opportunity if `q·1.00 − cost ≥ min_profit` and the event is flagged `mutually_exclusive` with complete outcome coverage. NO bundle: `cost = Σ ask_no_i + fees`, payout = (N−1)·q.
- Fee: `fee_kalshi(C,P) = ceil_cents(0.07·C·P·(1−P))` per order (use the series multiplier if present). Maker variant uses 0.0175 or 0 per the schedule.
- Re-check: 10 s and 60 s.
- Capital needed = cost. Settle date = event close.

**T2 – Kalshi vs Polymarket US**
- Fetch: Kalshi as above. Polymarket US market data API, or polymarket.com Gamma/CLOB as a **read-only reference flagged non-tradable for US** if US API access is not available. A curated `event_map.yaml` pairs equivalent markets and stores the resolution sources for both, with human sign-off.
- Rule: `cost = ask_yes_A + ask_no_B + fee_A + fee_B` (and the mirror). Opportunity if `1 − cost ≥ min_edge` (default ≥ 1¢ after fees) for size ≥ 10 contracts.
- Fee: Kalshi as above. Polymarket US `0.0695·C·p·(1−p)`, category overrides from config, maker 0.
- Re-check: 10 s and 60 s. Flag `resolution_risk` if the map confidence is below 1.0.

**T3 – Funding/basis carry (US)**
- Fetch: Coinbase spot BTC-USD/ETH-USD book. CFM perpetual-style futures mark price and current/predicted hourly funding. CME front-month basis (optional; delayed quote). Every 60 s.
- Rule: `expected_carry_30d = Σ projected funding (use trailing-7d mean, not the spot rate) + basis convergence`. `costs = spot_taker·2 + fut_fee·2 + slippage`. Opportunity if `annualized_net ≥ max(T-bill 3m yield + 2%, 5%)`.
- Booking: accrue simulated funding hourly on open demo positions; demo positions close after 30 days or when funding is negative for 24 h.
- Re-check: 1 h and 8 h (persistence of positive funding).
- Capital = spot notional + futures margin (≥ 30% buffer).

**T4 – Crypto cross-exchange spot**
- Fetch: WebSocket L2 books from Coinbase, Kraken, Gemini and Bitstamp for BTC, ETH, SOL, plus 10 liquid alts in USD/USDC quotes.
- Rule: for each pair (A, B) `edge = bid_B(q) − ask_A(q) − taker_A·ask_A − taker_B·bid_B − rebalance_cost_per_unit`. `rebalance_cost` = network withdrawal fee ÷ expected units per rebalance. Skip assets whose deposits or withdrawals are halted (status endpoints).
- Fee tiers are configurable. Show both "entry tier" (Coinbase 0.90% taker, Kraken 0.80%) and "VIP-ish" (0.10%) columns so the owner sees what volume would be needed.
- Re-check: 2 s, 10 s, 30 s.

**T5 – Kraken triangular**
- Fetch: Kraken WebSocket books for all USD, BTC, ETH and USDT crosses.
- Rule: for each cycle `X→Y→Z→X`, `product = Π (rate_leg after depth) · Π (1 − taker)`. Opportunity if `product − 1 ≥ min_edge`.
- Re-check: 1 s and 5 s.

**T6 – Stablecoin depeg**
- Fetch: USDC/USD, USDT/USD, PYUSD/USD, DAI/USD on Kraken and Coinbase every 10 s.
- Rule: `discount = 1 − ask(q)`. Opportunity if `discount − taker − exit_cost ≥ 0.3%`. Label it "**recovery bet**, not risk-free" unless a 1:1 conversion channel is configured as available.
- Re-check: 60 s and 1 h.

**T7 – Merger arb**
- Fetch: daily EDGAR full-text search for new 8-K 1.01, DEFM14A, SC TO-T and S-4 filings. A manual or semiautomated deal table (price, ratio, expected close, conditions). Quotes every 5 min in market hours.
- Rule: `gross_spread = deal_value − price`. `annualized = (gross_spread − fees − borrow_cost) / price × 365 / days_to_close`. Opportunity if `annualized ≥ 8%` and `downside_to_unaffected ≤ 3 × spread` (configurable).
- Booking: the demo position is held to close. "Potential profit" is booked as the expected value: `p_close · spread − (1 − p_close) · downside`, with `p_close` defaulting to 0.92 (typical historical completion; configurable).
- Re-check: next trading day.

**T8 – eBay underpriced flip**
- Fetch: eBay Browse `item_summary/search` with filters (category, condition, BIN, US) for a watchlist of EPIDs/GTINs. Batch calls to stay under 5,000/day. Reference price = median of the (a) comparable active listings and (b) Keepa Amazon new/used price, if keyed.
- Rule: `net = ref_price·(1 − fvf) − 0.40 − out_ship − in_cost(price + ship + sales_tax) − return_reserve(3–5% × ref)`. Opportunity if `net ≥ $15` and `net/in_cost ≥ 25%`.
- Re-check: 1 h and 24 h (is the listing still active).

### 4.3 Full fee model (`fees.yaml` excerpt)

```yaml
kalshi:        {taker_coef: 0.07, maker_coef: 0.0, round: ceil_cent_per_order, deposit_ach: 0, withdraw_ach: 0, src: "rivermarkets.com/insights/kalshi-fees.html", as_of: 2026-10}
polymarket_us: {taker_coef: 0.0695, maker_coef: 0.0, category_overrides: {table_tennis: 0.10}, src: "cftc.gov/filings/orgrules/rules09212628660.pdf", as_of: 2026-09-17}
coinbase_adv:  {maker: 0.0050, taker: 0.0090, tier: entry_us, src: "cryptodaily.co.uk 2026-09", as_of: 2026-09-16}
kraken_pro:    {maker: 0.0040, taker: 0.0080, tier: base, src: "support.kraken.com fee-schedule", as_of: 2026-10-01}
cfm_perp:      {fee_per_contract_usd: CONFIG_VERIFY, funding: hourly_accrual_twice_daily_settle}
withdraw_network: {BTC: live_from_api, ETH: live_from_api, SOL: live_from_api}
ebay:          {fvf: 0.136, per_order_le10: 0.30, per_order_gt10: 0.40, books_fvf: 0.153, src: "third-party calcs; verify eBay fee page"}
amazon_fba:    {referral_default: 0.15, fba_fee: sp_api_fees_estimate, fuel_surcharge: 0.035, monthly_plan: 39.99}
broker_equity: {commission: 0, sec_fee_bps_on_sells: CONFIG, borrow_apr: per_symbol}
slippage:      {model: walk_book, latency_ms: 500}
tax:           {mode: pre_tax_and_estimate, st_cap_gains_rate: 0.24, se_tax_for_resale: 0.153, state_rate: CONFIG}
```

`net = gross − Σ trading fees − Σ withdrawal/rebalance amortization − shipping − marketplace fees − financing/borrow − slippage − (optional) estimated tax`. Report both `netPreTax` and `netAfterTaxEst`.

### 4.4 Persistence re-check

- Every booked opportunity schedules re-checks at the type's N values (crypto 2/10/30 s; prediction markets 10/60 s; depeg 60 s/1 h; merger 1 day; eBay 1 h/24 h).
- At re-check, recompute the full net at the *same size* from fresh data. `still_valid = net_recheck ≥ min_profit`. Store `decay_pct = net_recheck / net_initial`.
- `stillValidPct` = share of opportunities valid at the **first** re-check. Also store a per-N breakdown.
- The demo also logs `half_life_s` per type (median time until net ≤ 0) as the best measure of "how instant is instant".

### 4.5 Stats JSON (emitted every minute to `stats.json`)

```json
{
  "generatedAt": "2026-10-21T15:04:00Z",
  "mode": "DEMO",
  "feeTier": "entry_us",
  "potentialTotal": 0.00,
  "h3": 0.00,
  "h6": 0.00,
  "today": 0.00,
  "opportunities": 0,
  "opportunitiesGrossOnly": 0,
  "avgNetMarginPct": 0.00,
  "capitalNeeded": 0.00,
  "capitalNeededPeak": 0.00,
  "stillValidPct": 0.0,
  "byType": {
    "kalshi_bundle":    {"potential": 0, "h3": 0, "h6": 0, "today": 0, "opportunities": 0, "grossOnly": 0, "avgNetMarginPct": 0, "capitalNeeded": 0, "stillValidPct": 0, "medianHalfLifeS": null, "settlement": "at_resolution"},
    "pm_cross_venue":   {"...": "same fields", "resolutionRiskFlagged": 0},
    "funding_carry":    {"...": "same fields", "annualizedNetPct": 0},
    "crypto_cross_ex":  {"...": "same fields"},
    "crypto_triangular":{"...": "same fields"},
    "stablecoin_depeg": {"...": "same fields"},
    "merger_arb":       {"...": "same fields", "annualizedPct": 0, "expectedValueBasis": true},
    "ebay_flip":        {"...": "same fields", "settlement": "weeks"}
  },
  "notes": ["DEMO: no orders placed; profits are hypothetical, sized to book depth, net of configured fees"]
}
```

**Definitions:**
- `potentialTotal` is the sum of `netPreTax` of booked opportunities since inception. `h3`, `h6` and `today` (owner's local timezone) are rolling windows.
- `capitalNeeded` is the maximum concurrent capital the strategy set would have tied up. This matters because prediction-market and merger capital stays locked.
- `avgNetMarginPct` is capital-weighted `net / capital`.
- `opportunitiesGrossOnly` counts the would-be opportunities that failed after fees. It shows how much the fees eat.

---

## 5. (c) Cloud vs. the owner's Windows PC, and accounts/keys

| Type | Run where (DEMO) | Keys/accounts needed for DEMO | Needed for LIVE later |
|---|---|---|---|
| Kalshi bundle | Cloud | None (public market data; verify) | Owner's Kalshi account (KYC) + API key. Trading should originate from a US IP; keep keys on the PC or an owner-controlled US VPS. |
| Kalshi vs Polymarket US | Cloud | Possibly a Polymarket US API key if data requires auth | Both accounts, KYC, state eligibility check. |
| Funding carry | Cloud | None | Coinbase account + CFM derivatives approval + API key (trade-only, no withdraw permission). |
| Crypto cross-exchange | Cloud | None | Accounts on 2–4 US exchanges, pre-funded. API keys with trade permission only, IP-allowlisted. |
| Kraken triangular | Cloud | None | Kraken API key. |
| Stablecoin depeg | Cloud | None | Exchange keys. |
| Merger arb | Cloud | Free quote API key (Finnhub / Alpha Vantage); EDGAR User-Agent with the owner's contact email | Brokerage account (margin for stock deals). Orders placed manually by the owner. |
| eBay flip | Cloud | eBay Developer Program app keys (free, owner signs up); optional Keepa API key (€49/mo) | Owner's eBay buyer/seller account. Purchases made manually. |
| Amazon OA (phase 2) | Cloud or PC | Keepa API; Amazon SP-API (needs a Professional seller account, $39.99/mo) | Seller account, invoices, prep. |
| Local flips, clearance, price mistakes, gift cards, tickets, sneakers | Owner's phone/PC, manual | Platform alerts in the owner's own logged-in apps | Same. |

**Principles:**
- The cloud runs read-only scanners and never holds trading or withdrawal-capable keys.
- Any future live execution should run on the owner's Windows PC (or a US VPS he controls), with keys stored in the Windows Credential Manager or environment variables, **trade-only permissions and withdrawals disabled**, and IP allowlisting.
- Datacenter IPs can be geoblocked or flagged by US prediction markets and some exchanges.
- Nothing that requires scraping logged-in pages (Facebook, Craigslist, retailer carts) is automated.

---

## 6. (d) Honest expectations: what "instant profit" really looks like

- **True instant, risk-free arbitrage (crypto cross-exchange, triangular) at retail fee tiers:** expect **~$0/day**. The demo will probably log hundreds of gross gaps per day and single digits or zero net, with a first-re-check still-valid rate well under 30% and half-lives of seconds. Only market makers with near-zero fees, co-location and inventory capture these. Getting to VIP tiers requires millions in monthly volume or large assets on platform. Kraken now allows tiers by assets held, which puts capital at custodial risk.
- **"Locked instantly, paid later" (prediction-market bundles and cross-venue):** occasional real edges of 0.5–3%, a few contracts deep, with capital locked until resolution. At $10k this is maybe a few dollars on a good day and $0 on most days. The main failure modes are a resolution mismatch on cross-venue pairs and partial fills.
- **"Delta-neutral carry" (funding/basis):** in Oct 2026 the basis has been **below Treasury yields since February**. After retail fees, a T-bill currently beats it. It is worth monitoring for regime change, such as funding spiking in a rally.
- **Slow arbitrage (merger arb):** realistically 4–8% annualized with occasional painful breaks. It is legal, simple and scalable, but it is not "instant": $10k earns ~$1–2/day on average.
- **Inventory flips (Amazon OA, eBay, books, clearance, local):** this is where an individual actually makes money, roughly **$15–70/day at $10k**. It is not passive and not instant. Expect 10–25 hours/week, 2–8 week cash cycles, returns, and Amazon/eBay account risk. Profit is income subject to ordinary tax plus 15.3% self-employment tax.
- **Expected demo headline after a week:**
  - "Potential" totals are dominated by merger arb (expected-value basis) and eBay flips (weeks to realize).
  - The fast crypto types show near-zero net with a large `opportunitiesGrossOnly`.
  - Prediction markets show occasional small locked edges.

  If the demo shows large instant crypto profits, assume a bug: a stale book, a missing fee, ignored depth, or a halted-withdrawal asset.
- **Before any real money:**
  - Run the demo ≥ 4 weeks.
  - Verify every fee in `fees.yaml` against the official page as of that date. Several 2026 figures above conflict between sources, notably Coinbase/Kraken tiers, the eBay store-tier FVF, StockX fees and Kalshi maker fees.
  - Confirm state eligibility for Kalshi and Polymarket US, and decide whether event contracts fit the "no gambling" rule.
  - Talk to a CPA about event-contract and futures taxation (Section 1256 vs. ordinary), crypto 1099-DA basis reporting (wash-sale rules still do not apply to crypto per mid-2026 sources), and resale business income.

---

## 7. Sources (accessed 2026-10-21)

**Prediction markets**
- Kalshi fees: [QuantVPS](https://www.quantvps.com/blog/kalshi-fees-explained), [BotForKalshi](https://www.botforkalshi.com/blog/kalshi-fees-explained), [River Markets](https://www.rivermarkets.com/insights/kalshi-fees.html), [pm.wiki arbitrage after fees](https://pm.wiki/uk/learn/prediction-market-arbitrage-after-fees)
- Polymarket US fee filings: [CFTC 21 Sept 2026](https://www.cftc.gov/filings/orgrules/rules09212628660.pdf), [CFTC 29 Sept 2026](https://www.cftc.gov/filings/orgrules/rules09292630356.pdf), [CFTC 14 Oct 2026](https://www.cftc.gov/filings/orgrules/rules10142633348.pdf), [CFTC 13 Oct 2026](https://www.cftc.gov/filings/orgrules/rules10132632911.pdf), [River Markets PM US](https://www.rivermarkets.com/insights/polymarket-us-fees.html)
- Polymarket US state status: [OddsAssist](https://oddsassist.com/prediction-markets/polymarket-us-states/), [Tech-Insider](https://tech-insider.org/prediction-markets/is-polymarket-legal-in-the-usa/), [BettingUSA](https://www.bettingusa.com/prediction-markets/reviews/polymarket/), [Yahoo Finance](https://finance.yahoo.com/news/polymarket-u-comeback-positions-prediction-122943953.html)
- Cross-venue arbitrage: [TradoxVPS](https://tradoxvps.com/prediction-market-arbitrage-in-2026/), [LaikaLabs](https://laikalabs.ai/prediction-markets/kalshi-vs-polymarket-fees-comparison), [NYC Servers](https://newyorkcityservers.com/blog/prediction-market-arbitrage-guide)
- Kalshi API: [Zuplo](https://zuplo.com/blog/2025/04/02/kalshi-api), [docs.rs kalshi-pmx](https://docs.rs/kalshi-pmx), [Kalshi legacy tiers](https://trading-api.readme.io/reference/tiers-and-rate-limits)

**Crypto**
- Coinbase fees: [CryptoDaily Sept 2026](https://cryptodaily.co.uk/2026/09/coinbase-advanced-fees-usdc-vip-tiers), [NerdWallet](https://www.nerdwallet.com/investing/reviews/coinbase)
- Coinbase API rate limits: [Coinbase Exchange](https://docs.cdp.coinbase.com/exchange/rest-api/rate-limits)
- Kraken fees: [Kraken support](https://support.kraken.com/articles/201893638-fee-schedule), [Datawallet](https://www.datawallet.com/crypto/kraken-fees-explained)
- Coinbase perpetual-style futures: [funding mechanism](https://help.coinbase.com/en/derivatives/perpetual-style-futures/funding-rate), [US perps 101](https://www.coinbase.com/learn/futures/us-perpetual-style-futures-101), [FOW](https://www.fow.com/insights/coinbase-hails-arrival-of-perpetual-style-futures-in-us), [JewelSwap](https://www.jewelswap.io/blog/perpetual-futures-explained)
- Basis and funding: [TFTC/Glassnode](https://www.tftc.io/bitcoin-futures-basis-below-treasury-yields-2026), [ConvexTrade](https://convextrade.com/metrics/btc-funding), [CF Benchmarks KFRI](https://www.cfbenchmarks.com/data/indices/KFRI)
- Arbitrage profitability: [Bitquery](https://bitquery.io/investigations/crypto-arbitrage-69-cents), [ScienceDirect 2026](https://www.sciencedirect.com/science/article/pii/S0378426626000956), [Opportuna](https://opportuna.io/blog/is-arbitrage-profitable), [BJF](https://bjftradinggroup.com/crypto-arbitrage/)
- Stablecoin depeg: [EigenPhi](https://eigenphi.substack.com/p/usdc-depegging-victims-signals-and-opportunities), [The Block](https://www.theblock.co/post/224172/usdc-stablecoin-market-cap-plunges), [Spark glossary](https://www.spark.money/glossary/stablecoin-redemption)
- Crypto tax: [Beancount 1099-DA](https://beancount.io/blog/2026/05/10/form-1099-da-digital-asset-broker-reporting-2026-crypto-investors-cost-basis-form-8949-guide), [Harness on wash sales](https://www.harness.co/articles/crypto-tax-loss-harvesting-in-2026-does-the-wash-sale-rule-still-not-apply)

**Securities**
- Merger arb: [Carmignac Q4 2025](https://www.carmignac.com/en-gb/articles/carmignac-portfolio-merger-arbitrage-plus-letter-from-the-fund-managers-q4-2025-3610-12632), [Carmignac](https://www.carmignac.com/en/articles/bumps-are-back-terminations-low-stars-align-for-merger-arbitrage-3412-11786), [YCharts SPMATR](https://ycharts.com/indices/^SPMATR)
- ETF NAV: [AlphaArchitect](https://alphaarchitect.com/arbitrage-and-the-trading-costs-of-etfs/), [VanEck](https://www.vaneck.com/at/en/authorized-participants), [ETF Trends](https://www.etftrends.com/2010/08/etf-creation-redemption-premiums-discounts/)

**E-commerce and resale**
- Amazon fees: [Amazon 2026 fee update](https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026), [AMZPrep](https://amzprep.com/amazon-fba-fees/), [SellerSprite](https://www.sellersprite.com/en/blog/amazon-fba-fees-2026-complete-guide)
- Amazon retail-arbitrage enforcement: [Seller forum](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/b2ad0bb7-66d8-453f-b875-702c3e97892e), [EcomCircles](https://ecomcircles.com/blog/retail-arbitrage-amazon/), [GoAura](https://goaura.com/blog/amazon-top-restricted-brands-in-2025)
- Keepa: [plans and tokens](https://keepa.com/api-docs/plans-tokens.html), [RevenueGeeks](https://revenuegeeks.com/software/keepa/api)
- eBay: [API call limits](https://developer.ebay.com/develop/get-started/api-call-limits), [Marketplace Insights](https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html), [size.ly](https://www.size.ly/tools/ebay-fee-calculator), [HustleGotReal](https://hustlegotreal.com/tools/ebay-fee-calculator/fees-by-category/)
- Walmart: [New-Seller Savings](https://marketplace.walmart.com/nss-influencer), [Feedvisor](https://feedvisor.com/university/walmart-seller-fees/), [GoAura](https://goaura.com/blog/walmart-seller-fees-breakdown)
- Gift cards: [Yakima Herald](https://www.yakimaherald.com/news/nation_and_world/business/best-places-to-sell-gift-cards-for-cash-instantly-2026/article_25e8dae9-e593-58f5-aa69-7c074aa8f211.html), [MillennialMoneyMan](https://millennialmoneyman.com/sell-gift-cards/)
- Books: [BookScouter](https://bookscouter.com/blog/where-to-sell-textbooks/), [MoneyPantry](https://moneypantry.com/bookscouter-review/)
- Sneakers: [GOAT fees](https://www.goat.com/en-gb/fees), [Closo StockX](https://closo.co/blogs/blog/stockx)
- Liquidation: [Closo](https://closo.co/blogs/inventory-liquidation/how-to-buy-amazon-returns-pallets)
- Tickets: [TicketNews](https://www.ticketnews.com/2026/07/ticket-resale-price-caps-for-concerts-a-comprehensive-analysis/), [Ticksights](https://www.ticksights.com/us-state-ticket-resale-laws-2026/), [Vermont H.512](https://termsandconditionstemplate.com/vermont-ticket-resale-price-cap-h512-2026), [Terms.law StubHub](https://terms.law/ToS-Watchdog/event-ticketing/stubhub/), [Terms.law SeatGeek](https://terms.law/ToS-Watchdog/event-ticketing/seatgeek/)
- Domains: [Afternic pricing](https://www.afternic.com/legal/agreements/pricing-and-fees), [GoDaddy](https://www.godaddy.com/help/what-is-list-for-sale-27761), [Namefi](https://namefi.io/r/en/blog/domain-renewal-costs-and-sell-through-rate)
- Scraping: [ConductAtlas Craigslist](https://conductatlas.com/platform/craigslist/craigslist-terms-of-use/prohibition-on-scraping-and-automated-access/), [Proskauer](https://www.proskauer.com/blog/ending-data-scraping-dispute-craigslist-reaches-31m-settlement-with-instamotor-08-24-2017), [Chat4Data on FB](https://chat4data.ai/fr-FR/blog/facebook-marketplace-scraper)
- Price errors: [3DTested Corsair](https://www.3dtested.com/pc-components/ram/corsair-cancels-usd240-48gb-ddr5-memory-kit-orders-due-to-pricing-error-companys-blunder-ignites-shopper-uproar-over-botched-ram-deal), [Consumerist](https://consumerist.com/tag/to-clarify/index.html), [LoveMoney](https://www.lovemoney.com/guides/14314/price-glitches-your-rights-when-stores-misprice-items)

**Legal exclusions**
- [OpenAI Services Agreement](https://openai.com/policies/services-agreement/)
- [Vernor v. Autodesk](https://en.wikipedia.org/wiki/Vernor_v._Autodesk,_Inc.), [EFF](https://www.eff.org/cases/vernor-v-autodesk)
- FMCSA broker bond: [SupplyChain247](https://www.supplychain247.com/article/fmcsa_issues_final_rule_requiring_75000_bond_for_brokers_for_claims), [LicenseMap](https://getlicensemap.com/states/freight-broker/california)

**Source-quality caveat:** Many 2026 fee figures come from third-party blogs and conflict with one another. The CFTC filings, Amazon, eBay developer, Kraken support and Coinbase help pages are the authoritative ones cited. Everything else is marked "verify" and must be confirmed on the official page before any live use.
