# Etsy Marketing Playbook (Agent-Ready)

**Version:** 2026-10-21 · **Owner:** US seller (Florida) · **Shops covered:**
- **SHOP-D:** Digital templates (instant downloads, e.g. Canva/PDF/printables)
- **SHOP-P:** Print-on-demand via Printify (sweatshirts, tees, posters)

## 0. How to read this file

Evidence tags on every claim:
- **[ETSY]**: Etsy Seller Handbook, Help Center, policy, or Etsy engineering source. Treat as authoritative.
- **[3P]**: Reputable third party (eRank, Marmalead, Alura, EverBee, Printify, trade press). Strong but secondhand.
- **[UNVERIFIED]**: Vendor claim, single source, or conflicting sources. Use as a hypothesis only.
- **[FOLKLORE]**: Common seller belief with no Etsy confirmation, or one Etsy has contradicted. Do not base decisions on it.
- **[RULE]**: An operating rule this playbook sets, derived from the evidence. Change it if your own data disagrees.

Note: etsy.com returned HTTP 403 to direct fetches during research (2026-10-21). Etsy citations below come from search-indexed copies of Etsy pages and from trade press quoting them. **Re-verify any number before relying on it when it affects money (fees, thresholds).**

---

## 1. How Etsy search works now

### 1.1 The pipeline

1. **Query matching / candidate retrieval.** Etsy finds the listings that match the query. It uses titles, tags, attributes, categories and (per the Aug 2025 handbook) a holistic view of the listing. [ETSY: Seller Handbook "How Etsy Search Works", updated 2025-08-26]. Engineering detail: a retrieval stage pulls "several thousand items" based on the query **and user context**, using combined graph, transformer and term embeddings. That makes it partly semantic, not exact-match only. [ETSY: Jha et al., "Unified Embedding Based Personalized Retrieval in Etsy Search", arXiv 2306.04833, 2023]
2. **Ranking (two layers).** "Etsy search is composed of two ranking layers." A first pass narrows the candidates, then a second-pass neural model re-ranks them. [ETSY: Code as Craft, "Deep Learning for Search Ranking at Etsy"; Etsy WWW'21 paper]. Ranking inputs Etsy names: relevancy, listing quality, customer and market experience, shipping price, recency, and **Context-Specific Ranking (CSR)**, which personalizes results by what shoppers like this one tend to buy. [ETSY: Handbook 2025-08-26]
3. **Ads are a separate layer.** Etsy Ads buy promoted placement but "do not change the core ranking algorithm." [ETSY: Search, Advertisement & Recommendation Ranking Disclosures, updated 2025-10-16, via 3P summary]

**Mental model [3P: Marmalead, 2025-12-08]:** keywords make a listing *eligible*. Shopper behavior (clicks, favorites, add-to-carts, purchases) decides *how far it travels*.

### 1.2 Factor-by-factor rules

| Factor | What's known | Do | Don't |
|---|---|---|---|
| **Query matching** | Title, tags, attributes and categories are matched. Etsy handles plurals and misspellings and matches root words [3P: Alura tags guide 2025]. Word order in the title has **no direct ranking effect**, but leading with key terms raises clicks [ETSY: Handbook 2025]. | Cover every distinct buyer phrase across title + 13 tags + attributes. | Don't repeat the same word in many tags. Don't add plurals or misspellings as tags [3P]. |
| **Descriptions** | Etsy now uses descriptions to understand the listing [ETSY: Aug 2025 title guidance via eRank 2025-08-27]. Marmalead calls their relevancy weight "light" [3P 2025-12-08]. | Put key phrases naturally in the first 160 characters. | Don't keyword-stuff descriptions. |
| **Listing quality score** | Internal score built from shopper engagement on the listing. Not visible to sellers [3P: eRank; Marmalead]. A new listing starts with no history. **Renewing keeps the score; deleting and relisting resets it** [3P: eRank "Renew or Relist"]. | Renew expired listings that sold well. Fix the thumbnail and price first when engagement is low. | Never delete and re-create a listing with sales. |
| **CTR and conversion** | Conversion to sale is a confirmed direct factor [3P citing Etsy]. CTR = search visits ÷ search impressions [3P: Printify]. | Optimize the first photo for CTR and the photo stack and price for conversion. | Don't attract irrelevant clicks: misleading thumbnails hurt conversion and therefore quality. |
| **Recency boost** | Exists, but small and brief [3P: eRank]. Claimed durations range from 24–72 hours to 7–14 days to 14–21 days (2026) [UNVERIFIED, conflicting]. | Launch listings in steady batches so each gets its window. Publish seasonal items **6–8 weeks before peak** [3P]. | [FOLKLORE] "Renew daily for ranking." Each renewal costs $0.20 and eRank says it is rarely worth it. |
| **Shipping price (SHOP-P)** | Since **2024-10-01**, US domestic listings with shipping **under $6** are prioritized. Exempt: digital listings, non-US destinations, non-US sellers, listings over $35 from shops with a free-shipping guarantee, and calculated shipping [ETSY Aug 2024 handbook via eRank and Printful, 2024]. A Feb 2026 "hard threshold" re-statement exists only on vendor blogs [UNVERIFIED]. | Set shipping to **$0 (free) or under $6** on every POD listing and build the cost into the price. Turn on the **US free-shipping guarantee for orders of $35+** [ETSY: free-shipping program since 2019-07-30]. | Never charge $6+ flat domestic shipping on a tee or sweatshirt. |
| **Customer and market experience score** | Shop-level. Helped by positive reviews, complete shop policies and an About section. Hurt by recent cases opened and **intellectual property infringement reports** [ETSY Handbook, quoted by eRank]. Missing photos or a missing return policy reduce visibility [ETSY: Search Visibility page, 2024–2025]. | Fill in the About section and all policies (including a return policy, even if "no returns" for digital). Answer messages fast. Resolve issues before buyers open cases. | **Never** use trademarked or copyrighted phrases or characters (teams, brands, celebrities, Disney and the like). IP reports damage the whole shop. |
| **Search Visibility page** | Shop Manager page that lists the issues reducing visibility across listings, shop and customer service. Shown issues include dark, low-quality or collage primary images, too few images, shipping price, and response time [ETSY Help: "How to Use the Etsy Search Visibility Page"; EcommerceBytes 2025-04-23]. | Check it **every week** and fix everything it flags. | Don't ignore it. It is Etsy telling you the rules directly. |
| **Photos** | The 2024 update: use **at least 5 high-quality photos**, avoid dark images and collages [3P: eRank 2024]. Listings can hold **20 photos** (raised from 10 in Aug 2025) [3P: List Perfectly 2025]. Up to 2 videos per listing as of Sept 2026 [UNVERIFIED: Alura changelog 2026-09-25]. | Use 10+ photos and 1 video. | No collage as the first photo. No dark first photo. |
| **Reviews** | Ratings of 4–5 stars help. New listings still rank without reviews if there are no other quality issues [ETSY Handbook 2025]. | Ask once, politely, after delivery. | No incentives, swaps, or friends-and-family reviews (see §5.4). |
| **Personalization (CSR)** | Results are personalized by style, engagement history, price sensitivity, language and sometimes location [ETSY CSR; 3P Marmalead 2025-12-08]. The app was 46% of GMS through Q3 2025 [3P citing Etsy]. | Check results logged out or in incognito. Design every thumbnail for a **small phone screen**. | Don't panic over your own rank checks: what you see is personalized to you. |
| **Etsy's Picks** | Badge chosen by Etsy style experts for quality (ratings), reliability (service record) and style (photography and presentation). Sellers can't apply or pay. Badges are reviewed daily [ETSY Help: "What are Etsy's Picks?"]. | Invest in a cohesive, styled photo look. Keep reliability metrics high. | Don't chase it directly. It follows from quality. |
| **Star Seller** | Rolling 3-month window. Requirements: reply to **95% of first messages within 24 h**; **95% of orders shipped on time with tracking** (or an Etsy label); **4.8+ average rating** [ETSY Handbook 2024-08-28]. Also a minimum of 5 orders and first sale 90+ days old [3P: Outfy 2026; verify]. Ranking effect not confirmed by Etsy [UNVERIFIED]. It is a trust badge that likely lifts conversion. | Treat its thresholds as minimum standards from day 1. Digital orders count as shipped on time automatically [3P]. | [FOLKLORE] "Star Seller = big ranking boost." |

### 1.3 What changed in 2025–2026 (dated)

- **2025-04-23:** Etsy announced search-visibility alerts and new seller features [3P: EcommerceBytes].
- **2025-08 (Aug 26–27):** New **title guidance**: under about 15 words. Lead with what the item is, then 3 key traits (color, size, material). Move gift and occasion phrases to tags and attributes. Remove "sale" and "free shipping". Don't repeat words. An AI title tool is rolling out. Old-style titles are **not penalized** [ETSY via eRank 2025-08-27].
- **2025-08:** Photo cap raised to 20 [3P].
- **2025-10:** ChatGPT Instant Checkout launched for US Etsy listings, **limited to shops enrolled in Offsite Ads** [3P: Modern Retail 2025-10-06]. A 2026 report says it ended in March 2026 and was replaced by an @Etsy app inside ChatGPT [UNVERIFIED, single source].
- **2025-10-16:** Etsy updated its ranking disclosures [ETSY via 3P].
- **2026:** Vendor blogs claim a shorter recency window, a 40% heavier weighting on customer-experience signals, and description indexing [UNVERIFIED; the "40%" figure is FOLKLORE].
- **2026-09:** Second listing video reported [UNVERIFIED].

---

## 2. Keyword research

### 2.1 Sources, ranked by trust

1. **Etsy search bar autocomplete** (logged out, incognito): real shopper phrases. Free. Use it first. [RULE]
2. **Etsy Stats → search terms** (your own listings) and **Etsy Ads → Search terms** report (last 30 days of ad search terms per listing) [ETSY Help: "How to Review the Performance of Your Etsy Ads"]. This is the **only true Etsy query data** you get. A $1–3/day ad is worth running partly as a keyword-discovery tool. [RULE]
3. **eRank Keyword Explorer**: Etsy search volume estimates, competition and trend. Rated the stronger keyword tool [3P: SellerStacked 2026].
4. **EverBee**: stronger for product and sales validation (estimated listing sales and revenue). It reflects the last 30 days. Vendor-claimed accuracy is "about 80%" [UNVERIFIED].
5. **Caution:** no tool measures Etsy query volume. Every figure is modeled. One keyword showed 8 vs 400 monthly searches across two tools. Below about 500 searches/month, treat numbers as *directional* only [3P: selleraiready 2026-08]. Cross-check a low-volume term in two tools before relying on it. [RULE]

### 2.2 Long-tail strategy for a brand-new shop [RULE, based on 3P consensus]

- A new shop has no quality history, so it cannot win head terms ("sweatshirt", "resume template"). Target **3–5 word phrases** where the buyer's intent is specific:
  - SHOP-P: "retro nurse sweatshirt gift", "florida beach comfort colors tee", "funny teacher halloween shirt"
  - SHOP-D: "editable wedding seating chart", "canva real estate flyer template", "minimalist resume template word"
- **Selection criteria** in eRank:
  - Searches roughly 200–3,000 per month
  - Competition under about 20,000 results, or a ratio of competition ÷ searches under about 50
  - A trend that is not falling
  
  These are working thresholds [RULE]. Tune them after 60 days of data.
- **Validate demand:** at least 3 listings on page 1 for the phrase show recent sales (EverBee) or "X people bought this in the last 24 hours" badges. **No demand evidence means no listing.**
- **Niche stacking:** pick 3–5 niches per shop (for example nurses, teachers, Florida/coastal, dog moms, small-business owners). Build 10–20 listings per niche so CSR and cross-sell have depth.

### 2.3 Seasonality calendar

Publish **6–8 weeks before the peak**. Etsy's own Q4 checklist schedules optimization for **August** [3P citing Etsy]. Halloween searches start mid-September [3P 2026].

| Moment | Peak date (2026–27) | Publish by | SHOP-P ideas | SHOP-D ideas |
|---|---|---|---|---|
| Halloween | Oct 31, 2026 | Sep 1 | teacher/nurse Halloween tees | party invites, class signs |
| Thanksgiving / Friendsgiving | Nov 26, 2026 | Oct 1 | family matching tees | menu, place cards |
| Black Friday–Cyber Monday | Nov 27 – Nov 30, 2026 | Oct 15 (sale scheduled) | best-sellers on sale | bundles on sale |
| Christmas / Q4 gifts | Dec 25. **POD ship cutoff about Dec 10–14** (check Printify) | Oct 15 | family Christmas sweatshirts, custom posters | holiday cards, planners 2027, gift tags |
| New Year / planners | Jan 1 | Nov 15 | — | 2027 planners, budget trackers |
| Valentine's Day | Feb 14, 2027 | Dec 20 | couples and galentine tees | cards, coupons, classroom valentines |
| Easter | Mar 28, 2027 | Feb 1 | family Easter tees | egg-hunt printables |
| Mother's Day | May 9, 2027 | Mar 15 | mama and custom-name sweatshirts | coupon books, cards |
| Graduation / Teacher Appreciation | May–June 2027 | Mar 15 | class-of-2027, teacher tees | grad party signs, teacher thank-you |
| Father's Day | Jun 20, 2027 | Apr 25 | dad tees | cards, BBQ invites |
| Back to School | Aug 2027 | Jun 15 | teacher tees | classroom decor, schedules, labels |

Q4 concentrates a large share of yearly sales [3P]. The claim "38% of GMS in 8 weeks" is [UNVERIFIED]. Smaller secondary peaks come around Valentine's, Mother's Day and back to school [3P 2026-02-12].

**Today is 2026-10-21. The launch is late for Halloween and on time for Christmas only if listings go up this week.** Prioritize Christmas, family-matching, 2027 planner and gift listings now.

### 2.4 Picking the 13 tags (each up to 20 characters) [ETSY Handbook 2025-08-26]

Recipe [RULE]:
1. **Use all 13.** Make every tag a **multi-word phrase** [ETSY].
2. Tags 1–3: the exact long-tail phrases from research, the same ones that lead the title.
3. Tags 4–7: synonyms and alternate names (sweatshirt / crewneck / pullover; template / editable / printable). Include regional variants (US "sweatshirt", UK "jumper") only if you ship there [ETSY suggests regional phrasing].
4. Tags 8–10: recipient and occasion ("gift for nurse", "christmas gift mom"). Etsy now wants these **in tags, not the title** [ETSY 2025-08].
5. Tags 11–13: style, aesthetic and use ("retro aesthetic", "boho wedding", "comfort colors").
6. **Don't** spend tags on things already covered by your category or attributes (color, "shirt" when the category is T-shirts) [3P: Alura]. Don't add plurals or misspellings. Don't repeat one word across 5 tags [3P].
7. Every tag must be true of the item. Irrelevant tags win clicks that don't convert, which hurts quality.

---

## 3. Listing optimization

### 3.1 Title (limit 140 characters; Etsy guidance: under about 15 words) [ETSY 2025-08 via eRank 2025-08-27]

Structure: **[What it is, using the main keyword] + [2–3 key traits] + [variant/format fact]**. Keep it natural and readable. The first 3–5 words carry the click on mobile [3P: Marmalead 2025-12-08].

- SHOP-P good: `Retro Nurse Christmas Sweatshirt, Comfort Colors Style Crewneck, Unisex S-3XL`
- SHOP-P bad: `Nurse Shirt Nurse Gift Nurse Sweatshirt Christmas Gift for Nurse Funny Nurse Tee Free Shipping SALE`
- SHOP-D good: `Editable Wedding Seating Chart Template, Minimalist Canva Sign, 24x36 Printable`
- Example from eRank: `Personalised 100% Cotton Dad T-Shirt: Custom Kids' Names S-XL`

Rules:
- Do: name the noun first and keep it human.
- Don't: write "sale", "free shipping" or "best", repeat words, or include an occasion unless it is essential to the product ("Halloween costume").
- Old long titles are not penalized [ETSY]. **Don't mass-rewrite titles on listings that are selling.** Test new titles on listings with weak CTR [3P: eRank].
- Review Etsy's AI title suggestions before accepting them. The tool sees only the title, main image and description, not your sales data [3P: eRank].

### 3.2 Category and attributes

- Pick the **most specific category** possible (Clothing › Gender-Neutral Adult Clothing › Hoodies & Sweatshirts › Sweatshirts; Paper & Party Supplies › Paper › Templates).
- **Fill every attribute** offered: primary and secondary color, occasion, holiday, recipient, style, material, size, sleeve length. Attributes feed filters and act like extra keywords [ETSY 2025-08; 3P: Alura].
- Mark SHOP-D listings as **Digital** and SHOP-P listings as **Physical**.

### 3.3 Description

- **First 1–2 sentences:** what it is plus the main keyword, in natural language. They show in previews and help Etsy understand the listing [ETSY 2025-08].
- Then use scannable bullets:
  - SHOP-P: fabric/blend and garment brand (from Printify, e.g. Gildan 18000, Comfort Colors 1717), fit notes and size-up advice, care, a pointer to the size-chart photo, processing time plus shipping estimate, "Designed by [Shop], printed by our production partner".
  - SHOP-D: exactly what files the buyer gets, the software needed (Canva free account, Word, Adobe Reader), dimensions, the editable vs fixed parts, how delivery works (instant download PDF with template link), "No physical item will be shipped", license terms (personal vs commercial), and refund policy.
- **AI disclosure:** if AI was used in the design, say so in the description [ETSY Creativity Standards via 3P: Listadum 2026].

### 3.4 Photos and mockups (up to 20 photos)

**First photo** [ETSY Help: listing-editing guide; 3P]:
- Bright, high-resolution, product fills the frame, **not a collage**, legible at thumbnail size.
- SHOP-P: lifestyle model or flat-lay mockup with the design clearly readable. Use a consistent shop style.
- SHOP-D: the finished design shown in a realistic context (on a desk, at a wedding, on a phone). Add a small, tasteful "Editable" banner.

**Photo stack, SHOP-P (8–12):**
1. Hero mockup
2. Close-up of the design
3. 2nd model or color
4. Color chart (only colors actually offered)
5. **Size chart** with measurements from the Printify spec
6. Fabric/feel or back side
7. Gift or packaging context
8. Personalization instructions (if any)
9. "How to order"

**Photo stack, SHOP-D (8–12):**
1. Hero
2. **"What you get"** graphic (file list)
3. Editable vs fixed fields
4. Editing in Canva (screen mockup)
5. Size and format options
6. 2–4 variations or pages
7. "How it works in 3 steps"
8. Bundle upsell image

**Mockup rules:**
- Use mockups you own or have licensed for commercial use.
- Colors in mockups must match the real Printify print.
- Order a sample of best-sellers to take real photos.
- Never show a garment color or size you don't sell.

**Video** (silent; reported 3–15 s, max 100 MB [3P; verify]):
- SHOP-P: a model turning, or a hand-held garment showing the print.
- SHOP-D: a 10-second screen recording of editing the template.

**Alt text:** up to 250 characters per image [3P]. Write a plain description that uses the main keyword naturally ("Woman wearing sage green retro nurse Christmas sweatshirt"). Watch for the quote-character bug, which makes `"` count as 6 characters [3P: Etsy Community]. Its ranking effect is modest [3P: eRank].

### 3.5 Pricing psychology [RULE unless tagged]

**Fee math** (US seller) [3P, 2026; verify at etsy.com/legal/fees]:
- $0.20 listing fee (and on each renewal or multi-quantity sale)
- 6.5% transaction fee on item + shipping + gift wrap
- 3% + $0.25 payment processing
- Offsite Ads 15% when an order is attributed (12% once the shop passes $10K/yr), capped at $100 per order
- **Florida:** Etsy collects and remits sales tax as the marketplace facilitator (FL law since 2021-07) [UNVERIFIED for this file; confirm with an accountant].

**Price floor:** price ≥ (Printify base cost + shipping + 10% fee buffer + 15% Offsite Ads buffer) ÷ (1 − target margin). Target **≥ 30% net margin after fees, at full Offsite Ads**.

**SHOP-P:** build shipping into the price and show **free shipping**.
- Typical market bands to check against [3P observation; verify live]: tees $22–30, sweatshirts $35–48, posters $15–40 by size.
- End prices in .99 or .95.
- Price the S–XL variants evenly. 2XL and above may cost a little more.

**SHOP-D:**
- Single templates: $3–15 by complexity. Bundles: $15–49.
- Price as "less than a coffee" for small items.
- Anchor with a high-value bundle.
- Never sell at $1 or less, which signals low quality and is buried by the $0.20 fee plus $0.25 processing fee.

**Charm pricing and anchoring** (.99, compare-at via sale) are general retail practice, not Etsy-ranking factors. [3P]

### 3.6 Sales, discounts, coupons

- Etsy's 2025 marketing events required **≥ 25% off** for consideration in Etsy's promotional features. The Labor Day event used 15%, rising to 25% [ETSY Handbook, updated 2024-12-04]. Check the current year's event terms in Shop Manager → Marketing.
- **Scheduling cutoff:** Etsy cited Oct 27 for holiday sale scheduling [3P citing Etsy]. **Schedule the Cyber Week sale by 2026-10-27.**
- Rules [RULE]:
  - Run **2–4 sales a year**: Cyber Week, Valentine's or Mother's Day, back to school (SHOP-D), plus one shop-anniversary sale.
  - A shallow 10% sale reads as stingy [3P: Alura]. Use **20–30%** in events.
  - Never run a permanent sale. It erodes trust and anchoring. Never raise a price just to "discount" it (deceptive, and illegal under FTC fake-reference-price guidance).
- **Automated offers** [ETSY 2025 handbook via 3P]: turn on Abandoned-cart (10–15%), Favorited-item (10%) and Thank-you (next order 15%) coupons.

### 3.7 Bundles and cross-selling

- SHOP-D: create **bundles** (5-template social kit, a full wedding suite). List each bundle as its own listing with its own keywords. Reference the bundle in every single-item description ("Save 40% with the full suite: see shop section 'Wedding Suites'").
- SHOP-P: matching-family sets (Mama / Mini / Dada listings), and the same design across tee, sweatshirt and poster. Etsy's multi-quantity order discounts can be configured through sales with a minimum purchase [ETSY].
- Use **shop sections** by niche and occasion. Pin 4 featured listings, which should be your best converters.
- Last photo of every listing: "More designs in this collection" image, a visual cross-sell. Links in descriptions only to your own Etsy listings or shop.

---

## 4. Etsy Ads and Offsite Ads

### 4.1 Etsy Ads (on-Etsy, cost per click)

**Official facts** [ETSY Help: "How to Set Up and Manage an Etsy Ads Campaign"; "How to Review the Performance of Your Etsy Ads"]:
- Minimum budget $1/day.
- New sellers are capped at a $25/day maximum, recalculated weekly.
- An order is attributed if the buyer clicks the ad and purchases within 30 days.
- Etsy recommends running about **30 days before judging**.
- Search terms report covers the last 30 days per listing.

**When a new shop should start** [RULE]:
- Day 1–14: **no ads.** Get to 15–20 listings and collect organic baseline data.
- Day 15+: $1–3/day on the **5–10 listings with the best organic CTR or favorites**, mainly to buy search-term data.
- Q4 exception: if launching Oct–Nov, start $3–5/day on gift listings by day 7.

**Budget ladder** [3P consensus, mydesigns.io 2026 / psdmate 2026; RULE]:
- Test: $1–5/day, for 30 days.
- Scale: raise by about 25% per week only while ROAS stays above break-even.

**Reading the stats:**
- **CTR** = clicks ÷ views. **Conversion** = orders ÷ clicks. **Average CPC** = spend ÷ clicks [ETSY]. **ROAS** = ad revenue ÷ spend.
- **Break-even ROAS** = price ÷ net profit per unit (before ads) [3P]. Example: a $40 sweatshirt with $14 profit has break-even ROAS ≈ 2.9.
- High impressions with low CTR means a thumbnail or title problem. High CTR with low conversion means a price, photo-stack or reviews problem [3P: Alura].

**Kill / keep rules** (per listing, after about 30 days) [3P: mydesigns, listybox 2026; RULE]:
- **Kill:** spend ≥ $30 with 0 orders, *or* ROAS below break-even after 30 days.
- **Iterate:** CTR under 1% → change the first photo, then retest for 14 days.
- **Keep or scale:** ROAS ≥ 1.2 × break-even (commonly 3×+).
- Use the search terms report: add new converting phrases to tags and titles. Etsy Ads has no negative keywords, so fix irrelevant matches by changing tags [3P; verify].
- Remember ROAS ignores halo effects (ad clicks can build quality score) [3P: ProfitTree]. Don't kill a listing that sells organically right after an ad test.

### 4.2 Offsite Ads (Google, Meta, Pinterest and others, run by Etsy)

[ETSY: Fees & Payments Policy; Help "How Etsy's Offsite Ads Work"; 3P Alura]
- Every shop is **auto-enrolled**. The fee applies **only when an attributed order happens** (click then purchase within 30 days). There is no fee for clicks.
- **15% fee** while trailing-365-day sales are under **$10,000**, and these shops **may opt out**. Once a shop hits $10K, the fee is **12% for life** and participation is **mandatory**. Thresholds are recalculated on the 1st of each month. **Fee cap: $100 per order.**
- **Opt out:** Shop Manager → Settings → Offsite Ads → turn off [3P].

**Decision rule** [RULE]:
- **SHOP-D:** margins are about 90%, so **stay opted in.** A 15% fee on a sale you otherwise wouldn't get is profit.
- **SHOP-P:** stay in **only if** the price-floor formula in §3.5 already includes 15%. If margin after a 15% fee falls below 10%, raise prices or opt out.
- Note: the 2025 ChatGPT checkout channel was limited to Offsite Ads participants [3P 2025-10-06]. Future AI channels may follow that pattern [UNVERIFIED], which is a reason to stay in if margins allow.

---

## 5. Outside traffic within Etsy's rules

### 5.1 What Etsy allows and forbids

- **Allowed:** promoting your Etsy shop and listings on your own social accounts, Pinterest and email lists you collected legally.
- **Forbidden:** moving the *transaction* off Etsy. That includes making offers outside Etsy, pointing Etsy buyers to buy elsewhere, and using QR codes or messages to move buyers off-platform [ETSY: Off-Platform Transactions policy; Seller Policy].
- No external links in Etsy messages or listings that push off-Etsy purchase. Social and website links go on the shop's About page only [3P: azonpress; UNVERIFIED detail].
- **Share & Save:** use your Share & Save links (Shop Manager → Share & Save) on all external posts. You get **4% of the order total credited back** on qualifying orders within 30 days of a click [ETSY: Share & Save Terms; 3P EcommerceBytes 2023-09-06]. Your own links do not trigger Offsite Ads fees [ETSY fee terms].

### 5.2 Pinterest (highest-ROI external channel for both shops) [3P: Craftybase, sellertoolshq, Tailwind-based guides, 2026]

**Setup:**
- Business account, claimed website (etsy shop URL where possible), Rich Pins.
- 8–15 keyword-named boards: "Christmas Sweatshirts for Women", "Editable Wedding Signs", "Nurse Gift Ideas". Write a 2–3 sentence keyword description for each board.

**Pins:**
- Format 1000×1500 (2:3). Add a clear text overlay with the benefit or keyword ("Editable Seating Chart in Canva").
- Make **multiple designs per listing** (different headline, color, format) [3P].
- Title ≤ 100 characters with the keyword. Description of 3–5 natural keywords. **No hashtags** (Pinterest deprecated them [UNVERIFIED]).
- Link = Share & Save listing link.

**Volume:** 3–5 *fresh* pins/day, consistently, beats bursts [3P]. Add 1–2 curated pins/day from others. Batch-schedule weekly (Pinterest native scheduler or Tailwind). Tailwind Tribes were discontinued [UNVERIFIED].

**Seasonality:** Pinterest users plan early. Pin seasonal items **60–90 days before the event** [3P consensus; RULE].

**Expectations:** traction usually comes in **weeks 4–8** [3P].

**Measure:** Etsy Stats → traffic source "Pinterest" plus Share & Save credits.

### 5.3 Instagram Reels / TikTok / YouTube Shorts [3P: listybox, Gelato 2026; frequencies are UNVERIFIED rules of thumb]

- Cadence: **3–5 short videos/week**, cross-posted and tailored per platform. Batch-film once a week.
- **SHOP-P formats:**
  - Design-to-shirt reveal
  - Try-on or "outfit of the day"
  - "Which color would you pick?"
  - Niche jokes for the audience (nurse or teacher humor)
  - Unboxing the sample
- **SHOP-D formats:**
  - 15-second "edit this template in Canva" screen recording
  - Before/after
  - "Plan your wedding signage in 5 minutes"
  - Template tours
- Put the hook in the first 1–2 seconds. Add captions on screen. Use a soft CTA ("link in bio") pointing to the Share & Save shop link or a link-in-bio page with Etsy links.
- [UNVERIFIED] "External traffic boosts Etsy ranking." Etsy doesn't confirm it. Value external traffic for its *direct* sales only. Sales do feed conversion history.
- Disclose any paid or gifted creator content (FTC Endorsement Guides).

### 5.4 Hard prohibitions [ETSY policy; FTC Consumer Reviews Rule, effective 2024-10-21]

- **No** incentivized reviews: no discount, freebie or refund in exchange for a review, especially not for a 5-star one. One shop was restricted for this [3P: Etsy forum].
- **No** review swaps, review groups, friends-and-family purchases for reviews, or buying reviews or favorites.
- **No** fake orders, fake engagement, or click and favorite rings. **No** spam: no unsolicited DMs, no mass comments, no posting in Facebook groups against group rules.
- **No** trademarked terms, brand names or copyrighted characters in designs, titles or tags. Check every phrase in USPTO Trademark Search before publishing.
- **Allowed:** one polite review request (Etsy sends one automatically; you may add a short thank-you note or an insert card with no incentive).

---

## 6. Measurement

### 6.1 Data sources

- **Etsy Stats (Shop Manager):**
  - Visits, orders, conversion rate, revenue
  - Traffic sources: Etsy search, Etsy app & other pages, direct, social, Etsy Ads, Offsite Ads
  - Search terms
  - Per-listing views, favorites, orders, revenue
  - **Search impressions and CTR**, on the Stats and Search Visibility pages since Aug 2024 [3P: Putler/Printify]
- **Etsy Ads dashboard:** views, clicks, CTR, orders, revenue, spend, ROAS, and search terms per listing [ETSY].
- **Etsy Open API v3** (for agent automation) [3P + developers.etsy.com; verify by calling a real listing]:
  - Listing: `views`, `num_favorers`, `state`, `quantity`, `price`, `tags`, `title`, `creation_timestamp`, `last_modified_timestamp`, `ending_timestamp`, `featured_rank`.
  - Receipts and transactions give orders and revenue per `listing_id`.
  - **No impressions, carts or ad stats in the API** [UNVERIFIED but no evidence found]. Pull those from Shop Manager or eRank manually or by CSV.
- **eRank:** rank tracking, listing audit, and the Listing Changes Tracker (May 2026) to correlate edits with results [3P].

### 6.2 Per-listing metric table (track weekly; keep a rolling 30-day window)

| Metric | Formula | Source |
|---|---|---|
| Impressions (search) | — | Stats / Search Visibility |
| CTR | search visits ÷ search impressions | Stats |
| Views / visits | — | Stats, API `views` |
| Favorite rate | favorites ÷ views | Stats, API `num_favorers` (delta) |
| Cart adds | — | Stats (where shown) / eRank |
| Orders | — | Receipts API |
| Conversion | orders ÷ visits | computed |
| Revenue, net profit | revenue − fees − COGS − ads | computed |
| Ad spend, ROAS | — | Ads dashboard |

**Benchmarks** [3P, unofficial]:
- Shop conversion of 1–3% is typical, under 1% needs work, over 5% is top tier [Gelato blog].
- Etsy-wide conversion is about 3% (2025 modeled estimate) [3P: ECDB, Grips].
- Etsy publishes **no** CTR benchmark. Use your shop's median as the baseline [3P: Printify].

### 6.3 Decision rules [RULE: tune after 90 days]

Evaluate each listing after **≥ 30 days live and ≥ 300 search impressions** (a seasonal item is judged against its own season).

| Signal | Diagnosis | Action |
|---|---|---|
| Under 300 impressions in 30 days | Keyword or relevance problem | Rework title, tags and attributes toward lower-competition long-tail phrases. Re-check in 21 days. |
| Impressions OK, CTR under 50% of shop median | Thumbnail, title or price-at-glance problem | Replace the first photo (A/B one variable at a time). Check price against page-1 competitors. |
| Views ≥ 100, 0 favorites | Not appealing or wrong audience | Revisit design, mockup and keyword intent. |
| Favorites OK, conversion under 1% after ≥ 150 visits | Price, trust or info gap | Add size chart or what-you-get images and video, adjust price, add FAQ to description, enable a favorited-item coupon. |
| Conversion ≥ 2%, orders ≥ 3 in 30 days | **Winner** | Scale: make 3–5 variants (colors, niches, products), add to ads, pin more, add a bundle. |
| 2 iteration cycles (about 60 days) with no orders and no improving trend | **Loser** | Deactivate, or let it expire at renewal (no $0.20 renewal). Never delete a listing with sales history. |
| Listing with sales that dropped more than 50% month over month (outside seasonality) | Competition or visibility issue | Check the Search Visibility page, new competitors and price. Refresh photos. |

**Change discipline:** make one major change per listing per 14–21 days, and log it (date, what changed). Micro tag shuffles "do nothing" [3P: Marmalead 2025-12-08].

### 6.4 Weekly review routine (Mondays, about 60–90 minutes)

1. Search Visibility page: fix every flagged issue.
2. Messages: response-rate check (95% within 24 h). Review any cases or bad reviews and resolve them.
3. Pull the per-listing table (§6.2). Compare to last week. Apply the §6.3 rules to listings due for evaluation.
4. Ads: apply the kill/keep rules. Copy new converting search terms into tags.
5. Stats → search terms: add new organic phrases to related listings.
6. Seasonal calendar: confirm what must be published in the next 8 weeks (§2.3).
7. Plan this week: N new listings, M iterations, Pinterest batch, and a short-video batch.
8. Log decisions in the change log.

---

## 7. Launch playbook: first 30 days

### Days 0–2: Foundation (both shops)

- [ ] Shop name, logo, banner, and an **About section** (story, photo, production partner) [ETSY quality factor].
- [ ] **All policies complete**: returns/exchanges (SHOP-D: "no returns on digital downloads, but contact us for issues"; SHOP-P: Printify-compatible policy for defects and misprints), privacy, processing time.
- [ ] SHOP-P:
  - [ ] Add a **production partner** ("Printify") in shop settings and assign it to every listing. The listing label must read "Designed by [Shop]" [ETSY Creativity Standards; 3P: Printify Help].
  - [ ] Shipping profiles: free or under $6 domestic. US free-shipping guarantee at $35+. Processing time that matches Printify's real production time plus a buffer.
- [ ] SHOP-D: check instant-download file limits, and use template links for Canva Pro elements (never a flattened PDF with Pro assets) [3P: Gelato].
- [ ] Offsite Ads decision (§4.2). Set up Share & Save links.
- [ ] Turn on automated coupons: abandoned cart, favorited item, thank-you.
- [ ] Pinterest business account with 8–10 boards. Instagram and TikTok handles that match the shop name.
- [ ] Trademark-check the full niche phrase list.

### Days 3–10: First 20 listings

- [ ] Run keyword research (§2) for 3–5 niches. Build a sheet of 60+ long-tail phrases.
- [ ] Publish **2–3 listings per day** (not all at once). Each listing gets its own recency window and you can learn as you go [RULE; 3P recency evidence].
- [ ] **Q4 priority (October launch):** about 70% gift/holiday listings, 30% evergreen.
- [ ] Run the §8 pre-publish checklist on every listing.
- [ ] SHOP-P: order samples of the 3 strongest designs to shoot real photos and videos.

### Days 11–20: Traffic

- [ ] Reach 30+ listings (40+ is a better target for SHOP-D).
- [ ] Pinterest: 3–5 fresh pins/day, scheduled. Two pin designs per listing.
- [ ] Short video: 3–5/week.
- [ ] Day 15: start Etsy Ads at $1–3/day on the top 5–10 listings by CTR/favorites ($3–5/day in Q4).
- [ ] Create sections, choose featured listings, build the first bundle (SHOP-D) and matching set (SHOP-P).

### Days 21–30: First iteration

- [ ] First weekly review (§6.4). Swap the first photo on the bottom-CTR quartile.
- [ ] Use ads search terms for tags. Keep publishing 1–2 new listings per day.
- [ ] Schedule the Cyber Week sale (deadline about Oct 27) [3P]. Prepare the Christmas shipping-cutoff banner and announcement (SHOP-P).
- [ ] Day 30 target: 50 listings (SHOP-D) / 40 listings (SHOP-P), Search Visibility page clean, first sales, 95%/24 h response rate.

### After day 30: weekly routine

| Day | Task |
|---|---|
| Mon | Weekly review (§6.4) |
| Tue–Thu | 5–10 new listings/week aimed at seasonal windows 6–8 weeks out, plus variants of winners |
| Tue | Iterate 3–5 listings flagged by the decision rules (one major change each) |
| Fri | Batch 15–35 Pinterest pins and 3–5 short videos for next week |
| Daily | Messages within 24 h. SHOP-P: check Printify order status and tracking uploads |
| Monthly (1st) | Offsite Ads threshold check, Star Seller status, fee and margin audit, renewal decisions on expiring listings, seasonal calendar update |

---

## 8. Pre-publish checklist (the agent runs this on every listing)

Fail any **[BLOCK]** item and the listing does not publish.

**Compliance**
- [ ] [BLOCK] No trademarked or copyrighted names, logos, characters or phrases in the design, title, tags or description (checked in USPTO Trademark Search).
- [ ] [BLOCK] Original design ("designed by seller"). Not a resold template or someone else's work. AI use is disclosed in the description if applicable [ETSY Creativity Standards].
- [ ] [BLOCK] SHOP-P: the production partner (Printify) is assigned. SHOP-D: the listing is typed as a digital item, and Canva Pro assets are delivered only via template link.
- [ ] [BLOCK] No text that steers buyers off Etsy, no external purchase links, no review incentives.
- [ ] [BLOCK] Mockups are licensed for commercial use. Colors and sizes shown are actually offered.

**Search**
- [ ] [BLOCK] Title: under about 15 words and ≤ 140 characters. Leads with the item noun and main long-tail phrase. Includes 2–3 key traits. No "sale", "free shipping" or repeated words.
- [ ] [BLOCK] All 13 tags used, each ≤ 20 characters and multi-word, no duplicates, plurals or misspellings, all truthful. Recipient and occasion phrases are in the tags.
- [ ] Most specific category chosen. **All** attributes filled (color, occasion, holiday, recipient, style, material, size).
- [ ] Main keyword appears naturally in the first sentence of the description.
- [ ] Target phrase validated: demand evidence on page 1, competition within limits (§2.2).

**Visuals**
- [ ] [BLOCK] At least 5 photos (target 10+). First photo is bright, high-resolution, not a collage, and legible at thumbnail size on a phone.
- [ ] SHOP-P has a size chart and a color chart. SHOP-D has "What you get", "How it works" and editable-fields images.
- [ ] 1 video (3–15 s, silent).
- [ ] Alt text on every photo (≤ 250 characters, no straight double quotes).
- [ ] Last photo cross-sells the collection or bundle.

**Offer**
- [ ] [BLOCK] Price meets the floor formula (≥ 30% net margin with a 15% Offsite Ads buffer if opted in).
- [ ] [BLOCK] SHOP-P: domestic shipping is $0 or under $6, the free-shipping guarantee is on, and processing time matches Printify plus a buffer.
- [ ] Price is within the page-1 competitor band for the target phrase (or the premium is justified by visuals).
- [ ] Variations are correct (sizes and colors). Personalization instructions are clear with a character limit (if personalized).
- [ ] Description covers materials or files, sizing or software, delivery, care or license, and returns.

**Placement and tracking**
- [ ] Assigned to a shop section. Bundle or cross-sell reference added.
- [ ] Seasonal listings are published ≥ 6 weeks before the peak.
- [ ] Logged in the tracking sheet (listing_id, publish date, target keyword, tag set, price) to start the 30-day evaluation clock.
- [ ] 2 Pinterest pin designs queued with the Share & Save link.

---

## 9. Folklore watchlist (do NOT act on these)

- "Renew listings daily for a ranking boost." The recency effect is small and brief, and each renewal costs $0.20 [3P: eRank].
- "Titles must use all 140 characters." Contradicted by Etsy's 2025 guidance [ETSY 2025-08].
- "Etsy shadow-bans keyword stuffing." Vendor copy only. Stuffing is still bad because it hurts CTR.
- "Customer-experience signals got 40% more weight in 2026." No source.
- "Star Seller gives a big ranking boost." Unconfirmed.
- "Social traffic directly raises Etsy rank." Unconfirmed. Value it for direct sales only.
- "Longer tags (14–18 characters) drive more impressions per Etsy." Not found in Etsy sources.
- "Vacation mode on and off fixes invisibility." Anecdotal (Dec 2025 low-quality source).

## 10. Key sources (accessed 2026-10-21)

- Etsy Seller Handbook, "How Etsy Search Works" (updated 2025-08-26): https://www.etsy.com/seller-handbook/article/how-etsy-search-works/375461474487
- Etsy Seller Handbook, "Keywords 101" (2025-08-26): https://www.etsy.com/dk-en/seller-handbook/article/keywords-101-everything-you-need-to-know/382774281517
- Etsy Help, Search Visibility page: https://help.etsy.com/hc/articles/25869947521175
- Etsy Help, Etsy's Picks: https://help.etsy.com/hc/en-us/articles/16594038248855-What-are-Etsy-s-Picks
- Etsy Help, Offsite Ads: https://help.etsy.com/hc/articles/360000338367 · Fees policy: https://www.etsy.com/legal/fees
- Etsy Help, Ads setup: https://help.etsy.com/hc/en-us/articles/360033701174 · Ads performance: https://help.etsy.com/hc/articles/360034223613
- Etsy Off-Platform Transactions policy: https://www.etsy.com/legal/policy/off-platform-transactions/1254654515806
- Etsy Share & Save terms: https://www.etsy.com/legal/policy/etsys-share-save-terms-program-terms/1162874007996
- Etsy Star Seller handbook (2024-08-28): https://www.etsy.com/seller-handbook/article/1020956976086
- Etsy events handbook (2024-12-04): https://www.etsy.com/seller-handbook/article/1200179946791
- Etsy Code as Craft, two-layer ranking: https://www.etsy.com/codeascraft/deep-learning-for-search-ranking-at-etsy · Retrieval paper (2023): https://arxiv.org/abs/2306.04833
- eRank, 2025 title update (2025-08-27): https://help.erank.com/blog/seo/etsy-title-update-2025-how-to-write-better-etsy-listing-titles/
- eRank, Oct 1 shipping change (2024): https://help.erank.com/blog/etsys-october-1st-shipping-visibility-change/ · Printful summary: https://support.printful.com/hc/en-us/articles/41396421120913
- eRank, Renew vs relist: https://help.erank.com/blog/for-etsy-seo-renew-or-relist/
- Marmalead, "How Etsy's Algorithm Works in 2026" (2025-12-08): https://blog.marmalead.com/etsy-algorithm-2026/
- Alura, Tags guide: https://www.alura.io/academy/etsy-tags-guide · Ads metrics: https://www.alura.io/academy/understanding-etsy-ads-metrics · Offsite Ads: https://www.alura.io/docs/article/etsys-offsite-ads-explained
- Printify, Etsy Creativity Standards: https://help.printify.com/hc/en-us/articles/4578896595345
- EcommerceBytes, Search visibility alerts (2025-04-23): https://www.ecommercebytes.com/2025/04/23/etsy-to-offer-search-visibility-alerts-and-other-new-features/ · Share & Save (2023-09-06): https://www.ecommercebytes.com/2023/09/06/etsy-rewards-sellers-for-driving-traffic-to-their-listings/
- Modern Retail, ChatGPT checkout (2025-10-06): https://www.modernretail.co/technology/how-etsy-sellers-feel-about-the-new-chatgpt-checkout-integration/
- List Perfectly, 20 photos (2025): https://listperfectly.com/selling/etsy-20-images-per-listing-list-perfectly/
- Ads budget/kill guides (2026): https://mydesigns.io/blog/etsy-ads/ · https://listybox.com/blog/etsy-ads-guide-pod-sellers-2026/ · https://psdmate.com/blog/etsy-ads-guide-2026
- Keyword tool accuracy (2026-08): https://www.selleraiready.com/2026/08/everbee-accuracy-vs-etsy-own-data.html · https://www.sellerstacked.co/blog/erank-vs-everbee
- Pinterest for Etsy (2026): https://craftybase.com/blog/pinterest-for-etsy-seller-handmade · https://sellertoolshq.com/guides/etsy-pinterest-marketing/
- Conversion benchmarks: https://www.gelato.com/blog/etsy-conversion-rate · https://ecdb.com/resources/sample-data/retailer/Etsy/transaction-kpis
- Seasonal calendar (2026-02-12): https://www.listifyai.net/blog/etsy-holiday-calendar-2026
