# Open Source Lab: Market Scout Report

Prepared: 2026-10-21. Research Lab market scout.
Scope: fast, real, legal money from open-source software, GitHub projects and local open-source models on an RTX 4090. Startup cost $0-$30. US owner handles signups, ID and client contact.

**How to read this.** Every number has a source and a date where I had one. I label secondhand claims (blogs, SEO posts, hobby repos) as **[weak]**. **[primary]** means the project's or platform's own page, which I read directly on 2026-10-21. Nothing here is guaranteed. Several popular "AI agents earn money" narratives fell apart when I checked them.

---

## 0. Bottom line

1. **Autonomous agents racing for open-source bounties is close to dead as a fast-money play in late 2026.** Agents swarm bounties (8-158 competing PRs within hours on fresh Algora bounties [weak]). Major projects now ban or penalize AI-written and autonomous PRs (tinygrad, Zed, Ghostty [primary]). Bug-bounty programs are shutting because of AI slop: Google OSS VRP paused on 2026-10-01, curl ended its bounty in Jan/Feb 2026, and huntr closed its OSS program in mid-2026. A documented 3-day agent experiment (HackerNoon, 2026-09-22) earned **$0**.
2. **The money that pays fast is media services on the 4090, sold human to human.** Examples are photo restoration and cleanup, captions and transcripts, and audio cleanup. Here open-source models do 80-90% of the labor, and a human delivers to a buyer who is already asking. Restricted model licenses are the trap. CodeFormer, RMBG-2.0, FLUX.1-dev, FLUX.2-dev and klein-9B, XTTS and F5-TTS weights are **non-commercial**. Use only the permissive stack (Section 3).
3. **Clipping campaigns (Whop Content Rewards) are the other real, fast-paying channel.** About $40K/day was being paid to clippers (Forbes, via builtbyfoundry, 2026-09-28) [weak, but corroborated by multiple trackers]. It runs on Whisper and ffmpeg and doesn't duplicate any existing venture. The median payout per submission is tiny, though.
4. **Fastest path to a first real dollar:** paid photo-restoration and edit requests on Reddit's r/PhotoshopRequest. Use the 4090 pipeline (GFPGAN + Real-ESRGAN + inpainting with a commercially licensed model), with the owner hand-finishing and posting the result. Payment arrives the same day by PayPal or Venmo tip from a requester who already posted the job. Detail is in Section 9. The caveat is that requesters may impose a probation or free-work-first rule (see 3a).

---

## 1. Paid open-source bounties

### What the evidence says

| Program | How it pays | Typical size | Time to pay | AI policy (read 2026-10-21) |
|---|---|---|---|---|
| **Algora** | Stripe Connect on merge, KYC at payout | $50-$2,500 (Archestra $50-$300, Twenty $2,500, Isaac $850) [weak: gigs.sh, verified 2026-05-18] | 1-3 business days after merge [weak] | No platform-wide agent policy; Algora "doesn't publicly invite bots" [weak]. One hobby repo reads Algora's terms as prohibiting robotic access [weak, unverified]. Per-repo policies govern. |
| **tinygrad** (bounty spreadsheet) | Cash, per spreadsheet | Varies | On merge | **[primary] README:** "If you are a new contributor with something that looks even close to AI written, it will be closed without feedback and you may be banned from our GitHub... if you used AI, disclose what you used it for." Effectively closed to new AI-assisted contributors. |
| **Zed** | (Community programs, not core cash bounties) | n/a | n/a | **[primary] CONTRIBUTING:** "we don't accept contributions from autonomous agents"; needs a human who "genuinely understands" the code; don't use an LLM for maintainer communication. |
| **Ghostty** | No cash | n/a | n/a | **[primary] AI_POLICY:** all AI use must be disclosed. AI PRs only on pre-approved issues. "Bad AI drivers will be denounced" on a public list. No AI-generated media. Vouch system for new contributors. |
| **Cal.com** (repo now points to cal.diy) | Algora bounties historically | Varies | Algora terms | **[primary] CONTRIBUTING:** PRs under 500 LOC and 10 files. Copilot summaries allowed if verified. No outright ban found. |
| **Expensify App** | **Upwork contract** after proposal accepted | $250 per job is the common historical rate (example listing) [weak on current rate]. Paid $1.2M to 125 contributors in 2022 (company PR) | **At least 7 days after deploy to production**. 50% penalty per regression [primary] | **[primary]:** MelvinBot, Expensify's own AI agent, **posts the first proposal on many issues**. Humans may post only "meaningfully different" proposals. No PR until hired. Verified Upwork profile, signed commits. Your agent competes against the house agent. |
| **Tenstorrent (tt-metal)** | Cash; assignment requested by comment | $1-$3,000. Model bring-up "Medium" tier $501-$1,999 [community page; no 2026 date] | On merge; amount at Tenstorrent's "sole discretion" | Reassign after 2 weeks of silence. No AI rule found in search. Read BOUNTY_TERMS.md before starting. Needs real ML/C++ skill; the agent can do heavy lifting, but the human must understand the work. |
| **Opire** | Stripe; dev keeps 100%, creator pays 4% + Stripe (2024 listing) | Small | On merge | In the HackerNoon test, all 3 Opire rewards were closed or unavailable (2026-09). |
| **IssueHunt / Gitcoin bounties** | n/a | n/a | n/a | No evidence of meaningful 2026 activity. Gitcoin moved to grants years ago. Treat as **dead**. |

**The skeptic's data points:**
- **HackerNoon, 2026-09-22.** "I sent an AI agent to hunt open source bounties for three days; it earned $0." Of 46 curated bounty issues, **0 were startable**. One $250 bounty had sat open since 2024 with 134 comments and no maintainer reply. One maintainer closed 12 outside PRs in one minute. Most rival candidates were also AI agents.
- **DEV "Open Source Money Map", posted 2026-06-01 [weak, self-reported].** Algora merge rate about 15%, with 8-158 competing PRs within hours. The author's 30-day total was **~$430 for 55 hours ($7.82/hr)**, mostly crypto tokens on small repos.
- **Hobby-repo claim [weak, unverified].** 98.9% of the $1.07M advertised on Algora issues sits in repos that merged 0 of 20,000+ outside PRs. If even roughly true, most advertised bounty dollars are not realistically winnable.
- **August 2026.** GitHub shipped repo-level controls to disable PRs or restrict them to collaborators [weak, secondhand]. Maintainers can now close the door wholesale.

**Verdict for bounties as a Lab line:**
- How it pays: per merged PR (Stripe, Upwork or crypto).
- Startup cost: $0, plus agent compute.
- Agents do: triage, reproduction, the draft fix and tests.
- The human must: understand the fix, write the proposal and comments in their own voice, disclose AI use, handle KYC, Upwork and the CLA, and own the reputation.
- Time to first dollar: 2-8 weeks realistically, and often never.
- Earnings: typically $0-$500/month for newcomers. The top people are specialists who are regulars in one repo.
- Risks: wasted hours, public "denouncement" or bans, reputation damage to the owner's GitHub.
- **Feasibility 4/10. Speed 2/10. Verdict: NO-GO as a speed play.** **Conditional GO** only as a narrow experiment: pre-assigned issues only (Tenstorrent "request assignment", Expensify "proposal accepted"), one repo at a time, full disclosure, and a human who can explain every line.

---

## 2. Bug bounties and security disclosure (HackerOne, Bugcrowd, huntr)

- **huntr [primary, huntr FAQ]:** the OSS vulnerability program stopped accepting submissions on **2026-06-30** and locked them on **2026-07-31**. Unprocessed reports won't be paid. huntr is moving to challenge-based competitions. The Model File Vulnerability program "remains open for standard submissions at this time". Historic per-report payouts were small ($25-$40 in 2021 Open Collective records).
- **Google OSS VRP:** paused new product-vulnerability reports from **2026-10-01** until at least Q1 2027, citing "a significant rise in automated submissions, the vast majority of which are not valid" (BleepingComputer, Infosecurity Magazine, Oct 2026). The Patch Rewards Program, up to $15K, stays open.
- **curl:** ended its HackerOne bounty. From Feb 2026, reports go to GitHub unpaid. Only about 5% of mid-2025 submissions were genuine (TechRadar; OpenSSF WG issue #178).
- **Policy census [weak, stingrai.io]:** of 53 VDP and bounty programs, none ban AI-written reports outright. Most that address AI require a human in the loop and verified findings. Django closes unverified AI-looking reports and may ban repeat offenders.
- **HackerOne:** reports a 210% increase in *valid* AI-related reports (mostly prompt injection), which is AI as a target, not AI as a reporter. I didn't retrieve HackerOne's current rule text on AI-written reports.
- **Legal scope:** testing outside a program's written scope can violate the CFAA and the program's safe harbor. Only test in-scope assets, on your own local installs of open-source code, and never against production systems that aren't explicitly in scope.

**Realistic for a newcomer?** No. The open-source bounty money that once rewarded volume is being withdrawn precisely because of AI volume, and valid findings need real security skill. The HackerNoon agent also hit 13 content-filter blocks in one day on security vocabulary.
- **Feasibility 2/10. Speed 1/10. Verdict: NO-GO.** Revisit only if the owner wants to learn security long-term. huntr's challenge competitions are the one thing to watch.

---

## 3. Productized media services on the 4090 (the strongest category)

### 3a. Photo restoration, cleanup and upscale
- **Demand and price.** Professional restoration runs about $35-$350+ per image, and a studio lists minor work from $35 and major from $75 (fash.com price guide; McBain Camera) [vendor pages]. Freelance photographers charge $25-$75 standard and $100+ for heavy damage [weak]. AI-only services can be under $10 [weak]. Pricing is splitting into a cheap AI tier and a premium human-finished tier.
- **Where buyers already are:**
  - **r/PhotoshopRequest paid requests.** Buyers post a job with a price and pay the editor whose result they choose. Rules from subreddit mirrors, 2025-2026 [weak, check the live sidebar]:
    - Final images are judged, not the tools.
    - Raw, unblended generator output is unacceptable; editors must mask and composite and leave untouched areas alone.
    - Original resolution must be kept (an AI downscale-upscale counts as low-res). Two strikes means probation from paid requests.
    - Older rules required participation in free requests before paid ones and capped editors at two submissions per request.
    - Never DM the requester first; that is a ban.
  - Fiverr "photo restoration" gigs, an Etsy listing (coordinate with the existing Etsy venture), and local: funeral homes (memorial photos), genealogy societies, photo-scanning shops, senior centers.
- **Open-source stack and licenses (license files read 2026-10-21):**
  - OK commercially: **GFPGAN** (Apache-2.0), **Real-ESRGAN** (BSD-3), **BiRefNet** (MIT) for background removal, **FLUX.1-schnell** and **FLUX.2-klein-4B** (Apache-2.0) for inpainting and generation.
  - **CodeFormer is S-Lab License 1.0, NON-COMMERCIAL. Do not use it on paid work.** Many ComfyUI restoration workflows include it by default.
  - **RMBG-2.0 (BRIA) is CC BY-NC 4.0, non-commercial.**
  - **FLUX.1-dev, FLUX.2-dev and FLUX.2-klein-9B are non-commercial** for self-hosting (BFL help page, Apr 2026).
- **Disclosure:** Fiverr requires sellers to disclose AI use if the client asks and to honor "no AI" requests (Fiverr Help Center). Best practice is to disclose by default ("AI-assisted, hand-finished") and never alter faces or identity without consent.
- **Agents vs. human:**
  - Agents: build and tune the ComfyUI batch pipeline, run it, draft gig copy, prepare before-and-after sets, and pre-screen requests for feasibility.
  - Human: hand-finish in GIMP or Krita (both free), check faces and hands for AI artifacts, post and deliver, and talk to the client.
- **Time to first dollar:** hours to days on r/PhotoshopRequest. On Fiverr, 1-4 weeks is typical for a new gig [judgment].
- **Earnings:** typically $5-$40 per small paid request (unverified, from common practice). Fiverr restoration orders run $10-$50. Local and premium jobs are $35-$75+.
- **Feasibility 8/10. Speed 8/10. Verdict: GO.**

### 3b. Transcription, subtitles and captions (Whisper)
- **Prices.** Fiverr entry gigs are $5 per 5-10 minutes; a 2026 guide quotes $20-$50 for 20-minute audio [weak]. A Fiverr category page shows $39-$67 for subtitles (dated). Some sellers charge $20/60 minutes.
- **Market direction.** Commodity transcription is shrinking. Fiverr Q2 2026: revenue -10% y/y, active buyers -21.9% to 2.7M, Q3 guidance -18% to -26% y/y, attributed to "low-value transactional work" moving to AI (Fiverr 6-K, Jul 2026). Upwork-side commentary says data entry and transcription projects declined [weak].
- **The angle that still pays** is not "transcription". It's a deliverable an AI app doesn't do end to end:
  - Burned-in, styled captions plus SRT/VTT in several languages for YouTubers and podcasters.
  - A podcast "repurpose pack": transcript, show notes, chapters, captioned vertical clips.
  - Accessible captions for local churches, schools and city meetings.
- **Stack:** Whisper (MIT) or faster-whisper, plus ffmpeg, plus Premiere for styled captions (already owned). For audio cleanup, use open denoisers and check each model's license.
- **Agents vs. human:** agents run the pipeline, QA timestamps and draft deliverables. The human proofreads names and jargon (Whisper hallucinates on silence and music) and handles clients.
- **Time to first dollar:** 1-3 weeks via Fiverr or outreach. Faster through warm contacts.
- **Feasibility 7/10. Speed 6/10. Verdict: GO,** as a packaged repurposing service rather than per-minute transcription.

### 3c. Product photos, background removal, voice-over
- Background removal alone is free in Canva and phones, so it's a weak standalone product. Bundle it with restoration or with Etsy and Shopify seller photo packs. That overlaps existing Etsy and Shopify ventures, so sell it to *their* sellers as a service, not as a product.
- AI product-photo generation: Fiverr reports AI UGC video ads +265% and AI video ads +63% (Q2 2026 call). That demand is real but drifts into ads and creative, which competes with general Fiverr work.
- **Voice-over with TTS:** **Kokoro is Apache-2.0 (license read).** XTTS-v2 (Coqui CPML) and F5-TTS weights are non-commercial [from my own knowledge, verify]. Never clone a real person's voice without written consent. Fiverr bans impersonation and deepfakes.
- **Feasibility 6/10. Speed 5/10. Verdict: HOLD.** Use as add-ons, not a separate experiment.

---

## 4. Self-hosted open-source setups for small businesses

**Covers:** n8n, Nextcloud, Ghost, Plausible, Cal.com, Twenty, Chatwoot, Ollama.

- **Cost anchors:**
  - Hosting runs $8-$14/mo for a small production n8n setup (Hetzner CX23 at about €5.49).
  - Managed n8n starts at $2.99-$7/mo (PikaPods, InstaPods, OpenHosst). That's the price ceiling for "hosting only".
  - A vendor estimate puts DIY's real monthly cost at $85-$175 once maintenance labor is counted (1-2 hours/mo at $75-$100/hr) [vendor, weak].
  - n8n v3.0 reportedly drops npm installs (~Oct 2026) [single source]. Quote Docker-based setups.
- **Demand evidence:** **weak.** I couldn't find marketplace data on budgets for setup services. Local AI for law and dental is usually pitched as HIPAA-eligible cloud with a BAA (Azure, AWS), not on-prem Ollama (vendor blog, May 2026). On-prem LLM buyers exist but sales cycles are slow and compliance-heavy.
- **How this differs from existing ventures:** the existing Upwork and Fiverr dev-automation venture sells one-off builds. This would be a **recurring "managed open-source" retainer** ($49-$149/mo per client for updates, backups and monitoring) sold to local businesses replacing SaaS (Calendly → Cal.com, Intercom → Chatwoot, Google Analytics → Plausible).
- **Finding clients:**
  - Local chambers of commerce and BNI groups.
  - Owners complaining about SaaS price hikes in local Facebook groups.
  - Privacy-sensitive professionals (therapists, accountants).
  - Communities around each project (Discord and forums "help wanted" threads).
- **Agents vs. human:** agents write Docker Compose and Ansible, run hardening checks, monitor and write runbooks. The human sells, holds the client relationship, and takes responsibility for data. Liability is real: you become their data custodian.
- **Time to first dollar:** 3-8 weeks.
- **Feasibility 6/10. Speed 3/10. Verdict: CONDITIONAL GO, not in the first wave.** Offer it to clients won through the other experiments.

---

## 5. Data labeling and AI-training microwork (Outlier, DataAnnotation, Prolific)

**Stated plainly:** these platforms pay a vetted human to do the work personally. Using AI to produce answers, or letting someone or something else work the account, is a terms violation and the common cause of permanent deactivation.
- Third-party guides list "using AI to write responses" as a compliance violation.
- Outlier's terms reportedly bar account sharing and "assisted" completion. A clustered ban wave hit 2026-07-13 to 07-26.
- Workers report deactivations for "prohibited tools" during screening [all weak, secondhand]. I didn't find Prolific's exact AI text, but research-participant platforms exist precisely to collect *human* responses, so AI use defeats the purpose and is treated as fraud.

- **The Lab's agents can contribute nothing here.** Only the owner, working personally, can, and that's a job, not a Lab venture. Work is also unstable (empty dashboards are common).
- **Feasibility for the Lab: 1/10. Speed: n/a. Verdict: NO-GO** for agents. The owner can apply personally as side income if they want, outside the Lab.

---

## 6. Templates and plugins on marketplaces; GitHub Sponsors

- **n8n Creator Hub:**
  - Paid templates exist with "Buy for $X" buttons, but only for **verified creators** (3 approved templates first).
  - **n8n does not process payments.** The creator tracks payment and delivers, and non-delivery can mean suspension [weak, quoting n8n guidelines].
  - Creators complain that qualifying is a grind. About 13,200 templates were listed as of 2026-10-12, so it's crowded.
  - The n8n affiliate program pays 30% for 12 months on Cloud referrals (€100 minimum, PayPal) [weak].
- **Raycast:** no evidence of paid public extensions; the store is free, with a "Pro" subscription for Raycast itself. **Obsidian and VS Code:** no native paid marketplace (my knowledge, unverified for 2026). Sales would go through Gumroad, which is an existing venture.
- **GitHub Sponsors:** long-tail. Most maintainers' expectations go unmet (arXiv 2111.13323: 8,028 maintainers). 60% of maintainers are unpaid hobbyists (Tidelift via The Register, 2023). Time to first dollar is months, and it needs an audience.
- **Feasibility 4/10. Speed 2/10. Verdict: NO-GO for speed.** These largely duplicate Gumroad and Chrome extensions anyway. Exception: publish free n8n templates only as lead generation for Section 4.

---

## 7. Other options found

### 7a. Whop Content Rewards (clipping)
- **How it pays:** brands and creators fund a budget, and clippers earn per 1,000 *verified* views on clips they post to their own TikTok, Reels, Shorts or X accounts.
- **Rates:** median $1.00/1K across 50 campaigns (range $0.05-$3.00) as of 2026-09-28. Median $1.30 across 100 campaigns as of 2026-10-12.
- **Fees and limits:** Whop takes 10%. There are per-clip minimum view thresholds and caps.
- **Reality check:** the Yomi Denzel campaign paid about $258,800 across **48,253 submissions**, about **$5.36 per submission on average**, with a heavily skewed distribution. Forbes (Apr 2026) reported about $40K/day paid to clippers.
- **Open-source fit:** Whisper (captions), ffmpeg, auto-reframe and scene-detection scripts, plus Premiere for polish. Agents find the best moments in long videos, cut and caption. The human posts from real accounts (no bots; fake views are excluded and get accounts banned) and follows each brief.
- **Rules:** content must be authorized clips of the campaign owner. Use the platforms' own AI-content labels if any synthetic element is used. TikTok and YouTube penalize "reused content", so add real editing value.
- **Startup:** $0. **Time to first dollar:** days to 2 weeks (new accounts start with low reach).
- **Feasibility 7/10. Speed 6/10. Verdict: GO** as a 2-week test.

### 7b. Agent-native crypto bounty boards (Superteam Earn, Gig.bot, AIGEN, MergeOS)
- Roughly 80% of Superteam bounties block AI or require KYC [weak, an agent operator's self-report, Feb 2026]. APIs are flaky and winners are announced weeks later.
- Token payouts (AIGEN, MRG) have unclear cash value, and token-farming repos look like "credibility repos" with inflated merge rates.
- US tax and securities ambiguity applies.
- **Verdict: NO-GO** for measurable USD.

### 7c. Technical writing for paid programs (DigitalOcean $50-$200, LogRocket $200-$400 per article) [weak, 2026-06]
- This is human-authored work. Many programs prohibit AI-written articles, so it doesn't fit an agent lab.
- **NO-GO** unless the owner writes.

---

## 8. Scorecard

| # | Option | Startup | Time to first $ | Feasibility | Speed | Verdict |
|---|---|---|---|---|---|---|
| 3a | Photo restoration and cleanup (4090) | $0-$10 | hours to days (Reddit), 1-4 wk (Fiverr) | 8 | 8 | **GO** |
| 3b | Whisper caption and repurposing packs | $0-$15 | 1-3 wk | 7 | 6 | **GO** |
| 7a | Whop clipping | $0 | days to 2 wk | 7 | 6 | **GO** |
| 1 | Assigned-issue bounties (Tenstorrent, Expensify) | $0 | 2-8 wk | 4 | 2 | **Conditional GO (small test)** |
| 4 | Managed self-hosted OSS retainers | $0-$10 | 3-8 wk | 6 | 3 | Conditional GO (wave 2) |
| 3c | Product photo, BG removal, TTS voice-over | $0 | 1-4 wk | 6 | 5 | HOLD (add-on) |
| 6 | Templates, plugins, Sponsors | $0 | months | 4 | 2 | NO-GO |
| 2 | Bug bounties (H1, Bugcrowd, huntr) | $0 | months | 2 | 1 | NO-GO |
| 5 | Data labeling microwork | $0 | n/a for agents | 1 | n/a | NO-GO (human-only, AI banned) |
| 7b | Crypto agent bounty boards | $0 | weeks | 2 | 3 | NO-GO |

---

## 9. The Open Source Lab: 4 parallel 2-week experiments

**Shared rules for all four:**
- Use only commercially licensed models: Whisper, faster-whisper, GFPGAN, Real-ESRGAN, BiRefNet, FLUX.1-schnell and FLUX.2-klein-4B, Kokoro. Keep a `LICENSES.md` per pipeline. **Ban CodeFormer, RMBG-2.0, FLUX-dev, XTTS and F5 from paid work.**
- Disclose AI assistance by default.
- The human posts and handles all client contact.
- No bots on Reddit, TikTok or GitHub.
- Track every hour and dollar in one sheet.

### Experiment A: "Restoration Desk" (fastest dollar)
- **Build (days 1-2):** agents assemble a ComfyUI workflow for GFPGAN face restore, Real-ESRGAN 2-4x upscale, FLUX.1-schnell or klein-4B inpainting for scratches and tears, and colorization (check that model's license). The output is a layered file for hand-finishing in GIMP or Krita.
- **Sell:**
  - The owner joins r/PhotoshopRequest, reads the live rules, and does the required free requests to qualify.
  - Then compete on paid restoration requests (2 submissions max per request; full resolution; no DMs).
  - In parallel, one Fiverr gig "Old photo restoration, hand-finished, 24h" at $15/$35/$60. If Etsy is used, place it under the existing Etsy venture so listings aren't duplicated.
  - Offer 5 free restorations to a local funeral home or genealogy society for testimonials.
- **Budget cap:** $10 (Fiverr gig extras or a nominal ad; none required).
- **Success metric (14 days):** at least $50 collected, or at least 5 paid jobs, and at least 60% of submissions chosen as winner or fully accepted.
- **Kill:** $0 after 10 days of active submitting, average under $8/hour of human time, or a probation strike for AI artifacts.

### Experiment B: "Caption and Repurpose Packs"
- **Product:** for a 60-minute podcast or YouTube video, deliver a cleaned transcript, SRT/VTT (English plus 1-2 languages), chapters, show notes, and 3 captioned vertical clips. Priced $25 (starter) / $60 / $120.
- **Agents** run faster-whisper large-v3 on the 4090, an LLM via Ollama for chapters and notes (use a permissively licensed model such as Qwen or Mistral Apache-2.0 variants, and check each), and ffmpeg plus Premiere templates for clips. **The human** proofreads names and jargon.
- **Sell:**
  - Owner sends 30 personalized emails or DMs to small podcasters, each with a free 3-minute sample made from that podcaster's own public episode, with no unsolicited bulk outreach.
  - Add a Fiverr gig in Video & Animation > Subtitles (a different category from the existing dev gigs).
- **Budget cap:** $15.
- **Success metric:** at least 2 paying clients, or at least $75 revenue, and at least 1 repeat or retainer inquiry.
- **Kill:** under 2 positive replies from 30 outreaches by day 10, or under $10/hour of human time on delivered jobs.

### Experiment C: "Clip Lab" (Whop Content Rewards)
- **Setup:** owner creates or uses a Whop account and 1-2 genuine short-form accounts (TikTok and YouTube Shorts). Pick 3 campaigns at at least $1.50/1K whose briefs allow captioned highlight clips.
- **Agents** download the authorized source content per each brief, use Whisper transcripts plus scoring to find hooks, then auto-cut, reframe and caption. **The human** reviews, adds original edits and posts 3-5 per day manually.
- **Budget cap:** $0 (no paid boosting; inducements are excluded from views).
- **Success metric:** at least $25 approved payouts within 14 days, or one clip at 50K+ verified views.
- **Kill:** under 10K total verified views after 30 clips, any account strike for reused content, or a campaign rejection rate above 50%.

### Experiment D: "Assigned Bounty Sniper" (narrow, low probability, high ticket)
- **Scope:**
  - Only issues where you can get **assigned or accepted before coding**: Tenstorrent tt-metal "bounty" issues (request assignment by comment; $501-$1,999 for model bring-up), and Expensify "Help Wanted" jobs (proposal must be accepted; paid via Upwork at least 7 days after deploy).
  - Optionally Algora bounties only in repos with a recent outside merge (agents check that the repo merged at least 1 non-member PR in the last 30 days and the maintainer replied within 72 hours).
  - **Skip tinygrad, Zed, Ghostty and any repo whose policy bans or restricts AI.**
- **Agents** triage about 50 listings per day, reproduce bugs, and draft the root-cause analysis and fix with tests. **The human** must understand and explain the fix, write the proposal in their own words, disclose AI assistance, sign the CLA and commits, and handle Upwork or Stripe KYC.
- **Budget cap:** $0 cash; compute within existing plans; at most 10 owner-hours over 2 weeks.
- **Success metric:** at least 1 assignment or accepted proposal within 14 days (the payout itself may land later).
- **Kill:** 0 assignments after 5 well-formed requests or proposals, any maintainer flagging slop, or owner time above 10 hours.

**Wave 2 (after week 2):** turn the best client relationships from A and B into the managed self-hosting retainer (Section 4), for example Plausible plus Cal.com plus Chatwoot for a local business at $79/mo.

---

## 10. The single fastest path to a first real dollar

**Paid restoration requests on r/PhotoshopRequest, powered by the 4090 restoration pipeline (Experiment A).**
- **Why fastest:** the buyer and the price already exist in each post. There's no gig ranking cold start, no maintainer review queue and no view threshold. Payment is a direct tip the same day once the requester picks a result.
- **Steps:**
  1. Agents build the licensed pipeline today.
  2. The owner reads the live sidebar rules and completes any required free requests.
  3. The owner submits hand-finished, full-resolution restorations to 3-5 paid posts per day.
- **Main risks:** the free-request prerequisite (if still enforced) can delay the first paid entry by days, and you're competing against many skilled editors. If restoration loses there, the same pipeline goes straight into the Fiverr gig.

---

## Sources (accessed 2026-10-21)
**Primary (read directly)**
- tinygrad README, contributing section: https://raw.githubusercontent.com/tinygrad/tinygrad/master/README.md
- Zed CONTRIBUTING (AI Policy): https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md
- Ghostty AI_POLICY.md: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md
- Cal.com CONTRIBUTING: https://raw.githubusercontent.com/calcom/cal.com/main/CONTRIBUTING.md
- Expensify CONTRIBUTING and MelvinBot guide: https://raw.githubusercontent.com/Expensify/App/main/contributingGuides/CONTRIBUTING.md and https://raw.githubusercontent.com/Expensify/App/main/contributingGuides/HOW_TO_WORK_WITH_MELVINBOT.md
- License files: CodeFormer (S-Lab NC), GFPGAN (Apache-2.0), Real-ESRGAN (BSD-3), BiRefNet (MIT), Whisper (MIT), Kokoro (Apache-2.0), all on GitHub.
- huntr 2.0 FAQ: https://blog.huntr.com/huntr-2-0-faq
- Fiverr AI guidelines: https://help.fiverr.com/hc/en-us/articles/37333301560593
- Fiverr Q2 2026 6-K: https://www.sec.gov/Archives/edgar/data/0001762301/000117891326003624/exhibit_99-1.htm and https://www.marketbeat.com/instant-alerts/fiverr-international-q2-earnings-call-highlights-2026-07-29/
- BFL licensing help: https://help.bfl.ai/articles/3670520907-can-i-use-the-api-for-a-commercial-application
- RMBG-2.0: https://github.com/Bria-AI/RMBG-2.0
- Tenstorrent bounty program: https://community.tenstorrent.com/t/announcing-the-tenstorrent-bounty-program/46

**News**
- Google OSS VRP pause: https://bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge and https://www.infosecurity-magazine.com/news/google-suspends-opensource-bug/
- curl bounty end: https://www.techradar.com/pro/security/curl-will-stop-bug-bounties-program-due-to-avalanche-of-ai-slop and https://github.com/ossf/wg-vulnerability-disclosures/issues/178
- HackerNoon agent experiment (2026-09-22): https://hackernoon.com/i-sent-an-ai-agent-to-hunt-open-source-bounties-for-three-days-it-earned-$0

**Weak / secondhand**
- DEV Open Source Money Map (2026-06-01): https://dev.to/zeroknowledge0x/the-open-source-money-map-every-way-developers-are-actually-making-money-in-2026-with-real-45ba
- gigs.sh Algora guide: https://gigs.sh/p/algora
- Algora topic, 98.9% claim: https://github.com/topics/algora?o=asc&s=stars
- AI report policy census: https://www.stingrai.io/blog/ai-generated-vulnerability-report-policies-census
- OSS AI policy shifts: https://codenote.net/en/posts/oss-ai-slop-contribution-policy-shift/
- Whop clipping (2026-09-28): https://www.builtbyfoundry.io/blog/what-is-clipping-1-dollar-per-1000-views-50-campaigns and https://shopiator.com/blog/whop-content-reward-campaigns
- Photo restoration prices: https://fash.com/costs/photo-restoration-prices and https://www.mcbaincamera.com/retouching.php
- r/PhotoshopRequest rules mirrors: https://r.datuan.dev/r/PhotoshopRequest and https://redlib.groet-infra.nl/r/PhotoshopRequest
- Fiverr transcription pricing: https://hereflowai.com/best-fiverr-gigs-beginners-2026/ and https://www.fiverr.com/categories/video-animation/subtitles-captions
- n8n hosting costs: https://sliplane.io/blog/n8n-pricing and https://builts.ai/blog/n8n-review-small-business/
- n8n Creator Hub: https://www.browseract.com/blog/how-to-make-money-with-n8n-workflow-automation and https://community.n8n.io/t/where-can-i-sell-my-n8n-workflow-i-am-looking-for-marketplaces-not-the-creator-hub/212963
- Outlier and DataAnnotation bans: https://breakingeven.online/blog/outlier-ban-wave-july-2026 and https://aitrainer.work/guides/dataannotation-empty-dashboard-explained/
- GitHub Sponsors study: https://arxiv.org/abs/2111.13323v1 and https://www.theregister.com/2023/10/03/github_patreon_developers/
- Superteam and agent boards: https://dev.to/neilvolner/i-am-an-ai-agent-given-50-to-make-money-here-is-what-actually-happened-3gjg
- Dental cloud-AI pitch: https://callsphere.ai/blog/llm-comparison-dental-front-desk-lowest-latency-may-2026
