# Etsy POD - Research Lab report (etsy-pod)

_Date: 2026-10-21. Ideas generated: 75. Passing GATE: 52. Owner: US/Florida, $0-$30 startup._

## 1. Fees and rules (verified Oct 2026)

### Etsy fees (US seller)
| Fee | Amount | Notes |
|---|---|---|
| Listing | $0.20 per listing | 4-month expiry; auto-renew charges another $0.20, and each sale of a multi-qty listing re-charges $0.20 |
| Transaction | 6.5% | On item price + shipping + gift wrap |
| Payment processing (US) | 3% + $0.25 | On full order total incl. sales tax and shipping |
| Offsite Ads | 15% (shops < $10k/yr, may opt out) / 12% (>= $10k, mandatory, for life) | Only on orders from an offsite ad click within 30 days; capped at $100/order |
| Shop setup fee | One-time, varies by location, may be waived | Shown in onboarding before final step; budget ~$15-$29 |
| Currency conversion | 2.5% | Only if bank currency is not USD |
| Etsy Plus (optional) | $10/month | Not needed at start |

**Model used for margins:** fees = 6.5% x price + 3% x (price x 1.07 tax) + $0.25 + $0.20 renewal = ~9.7% + $0.45 per order, free shipping baked into price. Offsite Ads excluded from base margin (opt out while under $10k); each idea's JSON also has `marginWithOffsiteAdUsd`.

### Production partners, AI and POD
- **POD is allowed** under Etsy's Creativity Standards as "designed by a seller": you create the original design and a third party prints it. Production partners can help but cannot be the sole creator.
- **Production partner disclosure:** Printify/Printful (and the specific print provider) must be added as production partners in Shop Manager, linked to each listing, and disclosed on the shop page/About section.
- **AI disclosure:** Etsy's Seller Policy requires disclosing in the listing description when an item is created with AI. Seller-prompted AI art from your own prompts/inputs is permitted; AI prompt bundles are banned. Third-party guides say AI-assisted POD should use "Designed by" (not "Made by"). Use wording like: "Original design created by [shop] using AI image tools (FLUX.1-schnell) and edited by hand; printed and shipped by our production partner Printify."
- **2026 enforcement:** No confirmed search demotion of POD. Enforcement targets unoriginal designs (untouched templates, clip-art bundles, look-alikes of protected work) and missing disclosures. Sellers report impression drops during enforcement waves (Marmalead), unconfirmed by Etsy.
- **Personalization:** Printify supports automated Etsy personalization (buyer text imports into design layers), but personalized orders **always go On Hold** for manual review/submission. Budget owner time for this.

### Can one person run a second Etsy shop?
**Yes.** Etsy allows multiple shops, but:
1. **One shop per account.** Make a new Etsy account with a **different email address** (Etsy cannot move or merge shops between accounts).
2. **Same real identity.** Use your true legal identity, tax info and bank details; do not invent identities (that would be deception and breaks Etsy's rules).
3. **Disclose** all shops you run in the Public Profile of each account.
4. **Risks:** linked accounts are reviewed together, so a policy strike or suspension in one shop can hit all shops. A second shop cannot be used to dodge a suspension, relist removed items, or run duplicate catalogs to game search. Etsy may also flag new shops sharing payment details for verification, so expect holds/ID checks.
5. Recommendation: build etsy-pod as its own shop and brand with a distinct catalog (no copies of another shop's items), disclose the link in both profiles, and keep it fully compliant.

### Print + shipping cost (Printify Free plan vs Printful, US, first item)
Sources disagree; verify live with the APIs below before pricing. Figures used in this model are marked **bold**.

| Product | Printify base | Printful base | US ship (1st item) | Used in model (base+ship) |
|---|---|---|---|---|
| Unisex tee B+C 3001 | $11.29 (Printify page, Oct 2026; ~$9-10 on Premium) | $11.92 | Printify $3.99-4.50 / Printful $4.95 | **$16.50** |
| Comfort Colors 1717 | ~$15-16 | ~$17-18 | ~$4.50 | **$20.00** |
| Hoodie Gildan 18500 | $19.86-22 | $22.63-26.50 | $5.35-8.49 | **$29.49** |
| Crewneck Gildan 18000 | ~$15-17 | ~$20-22 | ~$7-8.49 | **$25.49** |
| 11oz mug | $4.93-7.95 ($3.68 Premium) | $6.75-7.95 | $4.55-6.49 | **$11.89** |
| 18x24 matte poster | $8.37-11.50 | $13.75 | ~$4.99 | **$15.00** |
| Tote | $9.67-10.50 | $15.25 | ~$4.99 | **$14.99** |
| 3x3 kiss-cut sticker | $1.20-2.80 | $1.99 | ~$4.29 | **$6.29** |

Printify Premium ($24.99/mo annual, $39 monthly) cuts base ~20% - only worth it above ~100 orders/month. Printful Growth is $24.99/mo. Start on free plans (startup budget). Stickers cannot clear $6 margin as single-item sales; use them only as add-ons.

## 2. Method and GATE
- 10 scores (1-10), overall = weighted 15/15/10/10/10/10/10/5/10/5 (demand, profitability, feasibility, automation, profitCapture, speed, scalability, competition, risk, startupCost).
- **GATE:** demand >= 7, margin >= $6 at a competitive price, risk >= 8, measurable via Etsy Open API v3 + Printify/Printful API, feasibility >= 7.
- **Caveat on demand:** Etsy blocks automated fetches, and no live eRank/EverBee/Google Trends pull was possible, so demand scores are desk estimates from 2026 niche reports (eRank Q1-2026 top searches via Printify, MerchOne, Teeinblue) and known Bestseller patterns. Every GATE pass is **provisional** until checked with the measurement plan (competitor count via `findAllListingsActive`, eRank search volume, Google Trends 5-year line).
- Revenue figures are typical (median-ish) gross sales for a 20-40 listing line in a new shop with no ads. Many new POD shops earn less. Q4 ideas get a 2.5x first-quarter boost because the gift window is open now.

### Measurement endpoints (all ideas)
- **Etsy Open API v3:** `findAllListingsActive` (GET /v3/application/listings/active?keywords=) for competitor counts; `getListingsByShop` and `getListing` (fields `views`, `num_favorers`) for traction; `getShopReceipts` (GET /v3/application/shops/{shop_id}/receipts) and `getShopReceiptTransactionsByShop` for units and revenue; `createDraftListing`/`updateListing` for publishing.
- **Printify API:** GET /v1/catalog/blueprints/{blueprint_id}/print_providers/{pp_id}/variants.json and /shipping.json (cost); POST /v1/shops/{shop_id}/products.json + /products/{id}/publish.json (listing); GET /v1/shops/{shop_id}/orders.json (`total_price`, `total_shipping`) for real COGS.
- **Printful API (hat idea):** GET /v2/catalog-products/{id}/prices, POST /v2/shipping-rates, GET /v2/orders.
- Margin per sale = receipt grandtotal - Etsy fees (from payment ledger) - POD order cost.

## 3. Top 5 passing ideas

### #1 Dog-breed ugly-sweater-pattern Christmas sweatshirts
- Product: Crewneck sweatshirt (Gildan 18000, Printify); cost $25.49 -> price $42.99; **margin $12.88** ($6.43 on an Offsite-Ads sale); **overall 8.35**
- rev3mo $420, rev12mo $2470, first dollar ~42 days, 4 h/week; Chrome: yes: listing drafts, tags, disclosures and Printify publishing; owner approves
  - demand 8: Q4 dog-lover gifts surge (desk estimate; verify with eRank/EverBee + findAllListingsActive count)
  - profitability 9: $12.88 margin at $42.99 after fees + print/ship $25.49
  - feasibility 9: Static design; ComfyUI FLUX.1-schnell + vector cleanup
  - automation 8: Listings bulk-created via Printify API; orders auto-route
  - profitCapture 7: Keeps 30% of sale (drops to $6.43 on a 15% Offsite Ads sale)
  - speed 9: Q4 gift window open now (Oct 21) - list this week
  - scalability 10: Many variants (breeds/states/professions/names)
  - competition 4: Moderate
  - risk 9: Original patterns
  - startupCost 8: ~$4-8 listing fees for 20-40 listings + Etsy setup fee (location-based, may be waived); no inventory
- Verdict: GO - launch batch 1 (verify demand with eRank + findAllListingsActive first)

### #2 Dog-breed line-art 'Dog Mom' sweatshirts (200+ breeds)
- Product: Crewneck sweatshirt (Gildan 18000, Printify); cost $25.49 -> price $42.99; **margin $12.88** ($6.43 on an Offsite-Ads sale); **overall 8.25**
- rev3mo $180, rev12mo $2640, first dollar ~49 days, 4 h/week; Chrome: yes: listing drafts, tags, disclosures and Printify publishing; owner approves
  - demand 9: 'dog mom sweatshirt' one of Etsy's deepest POD demand pools (desk estimate; verify with eRank/EverBee + findAllListingsActive count)
  - profitability 9: $12.88 margin at $42.99 after fees + print/ship $25.49
  - feasibility 8: Static design; ComfyUI FLUX.1-schnell + vector cleanup
  - automation 8: Listings bulk-created via Printify API; orders auto-route
  - profitCapture 7: Keeps 30% of sale (drops to $6.43 on a 15% Offsite Ads sale)
  - speed 8: Evergreen; can list within days
  - scalability 10: Many variants (breeds/states/professions/names)
  - competition 3: Very saturated; breed long-tail is the wedge
  - risk 9: Breeds are generic; avoid AKC marks
  - startupCost 8: ~$4-8 listing fees for 20-40 listings + Etsy setup fee (location-based, may be waived); no inventory
- Verdict: GO - launch batch 1 (verify demand with eRank + findAllListingsActive first)

### #3 Vintage 'Evergreen Tree Farm Est.' Christmas sweatshirts
- Product: Crewneck sweatshirt (Gildan 18000, Printify); cost $25.49 -> price $42.99; **margin $12.88** ($6.43 on an Offsite-Ads sale); **overall 8.1**
- rev3mo $360, rev12mo $2130, first dollar ~44 days, 4 h/week; Chrome: yes: listing drafts, tags, disclosures and Printify publishing; owner approves
  - demand 8: Christmas sweatshirts dominate Q4 POD search (desk estimate; verify with eRank/EverBee + findAllListingsActive count)
  - profitability 9: $12.88 margin at $42.99 after fees + print/ship $25.49
  - feasibility 9: Static design; ComfyUI FLUX.1-schnell + vector cleanup
  - automation 8: Listings bulk-created via Printify API; orders auto-route
  - profitCapture 7: Keeps 30% of sale (drops to $6.43 on a 15% Offsite Ads sale)
  - speed 9: Q4 gift window open now (Oct 21) - list this week
  - scalability 8: Many variants (breeds/states/professions/names)
  - competition 3: Crowded
  - risk 9: Fictional farm name; check no real farm trademark
  - startupCost 8: ~$4-8 listing fees for 20-40 listings + Etsy setup fee (location-based, may be waived); no inventory
- Verdict: GO - launch batch 1 (verify demand with eRank + findAllListingsActive first)

### #4 'Grandma Est.' sweatshirt with grandkids' names
- Product: Crewneck sweatshirt (Gildan 18000, Printify); cost $25.49 -> price $42.99; **margin $12.88** ($6.43 on an Offsite-Ads sale); **overall 8.05**
- rev3mo $450, rev12mo $2640, first dollar ~39 days, 7 h/week; Chrome: partial: Claude in Chrome can draft listings, fill Production Partner/AI disclosure fields, release held personalized orders; final publish/approve by owner
  - demand 9: Grandma name sweatshirts are perennial Etsy Bestsellers (desk estimate; verify with eRank/EverBee + findAllListingsActive count)
  - profitability 9: $12.88 margin at $42.99 after fees + print/ship $25.49
  - feasibility 8: Template + Printify automated personalization layers
  - automation 6: Personalized orders always held for review in Printify
  - profitCapture 7: Keeps 30% of sale (drops to $6.43 on a 15% Offsite Ads sale)
  - speed 9: Q4 gift window open now (Oct 21) - list this week
  - scalability 9: Many variants (breeds/states/professions/names)
  - competition 3: Saturated; win on typography + Q4 timing
  - risk 9: Text-based, no IP
  - startupCost 8: ~$4-8 listing fees for 20-40 listings + Etsy setup fee (location-based, may be waived); no inventory
- Verdict: GO - launch batch 1 (verify demand with eRank + findAllListingsActive first)

### #5 Minimalist KJV scripture wall art (public-domain text)
- Product: 18x24 matte poster (Printify); cost $15.0 -> price $29.99; **margin $11.63** ($7.13 on an Offsite-Ads sale); **overall 8.05**
- rev3mo $100, rev12mo $1480, first dollar ~54 days, 4 h/week; Chrome: yes: listing drafts, tags, disclosures and Printify publishing; owner approves
  - demand 8: Christian wall art listed as top 2026 niche (desk estimate; verify with eRank/EverBee + findAllListingsActive count)
  - profitability 8: $11.63 margin at $29.99 after fees + print/ship $15.00
  - feasibility 9: Static design; ComfyUI FLUX.1-schnell + vector cleanup
  - automation 8: Listings bulk-created via Printify API; orders auto-route
  - profitCapture 8: Keeps 39% of sale (drops to $7.13 on a 15% Offsite Ads sale)
  - speed 8: Evergreen; can list within days
  - scalability 9: Many variants (breeds/states/professions/names)
  - competition 3: Crowded
  - risk 9: KJV is public domain in US; avoid NIV/ESV (copyrighted)
  - startupCost 8: ~$4-8 listing fees for 20-40 listings + Etsy setup fee (location-based, may be waived); no inventory
- Verdict: GO - launch batch 1 (verify demand with eRank + findAllListingsActive first)

## 4. Ranked table (all ideas)

| Rank | Idea | Product | Cost | Price | Margin | Dem | Prof | Feas | Auto | Cap | Spd | Scal | Comp | Risk | Start | Overall | Hrs/wk | rev3mo | rev12mo | 1st $ days | Gate | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Dog-breed ugly-sweater-pattern Christmas sweatshirts | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 8 | 9 | 9 | 8 | 7 | 9 | 10 | 4 | 9 | 8 | 8.35 | 4 | $420 | $2470 | 42 | PASS | GO - launch batch 1 (verify demand with eRank + findAllListingsActive first) |
| 2 | Dog-breed line-art 'Dog Mom' sweatshirts (200+ breeds) | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 9 | 9 | 8 | 8 | 7 | 8 | 10 | 3 | 9 | 8 | 8.25 | 4 | $180 | $2640 | 49 | PASS | GO - launch batch 1 (verify demand with eRank + findAllListingsActive first) |
| 3 | Vintage 'Evergreen Tree Farm Est.' Christmas sweatshirts | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 8 | 9 | 9 | 8 | 7 | 9 | 8 | 3 | 9 | 8 | 8.1 | 4 | $360 | $2130 | 44 | PASS | GO - launch batch 1 (verify demand with eRank + findAllListingsActive first) |
| 4 | 'Grandma Est.' sweatshirt with grandkids' names | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 9 | 9 | 8 | 6 | 7 | 9 | 9 | 3 | 9 | 8 | 8.05 | 7 | $450 | $2640 | 39 | PASS | GO - launch batch 1 (verify demand with eRank + findAllListingsActive first) |
| 5 | Minimalist KJV scripture wall art (public-domain text) | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 8 | 8 | 9 | 8 | 8 | 8 | 9 | 3 | 9 | 8 | 8.05 | 4 | $100 | $1480 | 54 | PASS | GO - launch batch 1 (verify demand with eRank + findAllListingsActive first) |
| 6 | Neutral boho abstract canvas wall art | 12x16 gallery canvas | $30.0 | $54.99 | $19.2 | 7 | 10 | 9 | 8 | 8 | 8 | 8 | 2 | 9 | 8 | 8.05 | 4 | $110 | $1630 | 61 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 7 | State-flower botanical prints for all 50 states | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 7 | 8 | 9 | 8 | 8 | 8 | 9 | 5 | 9 | 8 | 8.0 | 4 | $110 | $1600 | 55 | PASS | GO - batch 2 (after batch 1 data) |
| 8 | 'Book Club Era' style bookish sweatshirts (no titles/authors) | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 8 | 9 | 9 | 8 | 7 | 8 | 9 | 3 | 8 | 8 | 8.0 | 4 | $150 | $2130 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 9 | Pet memorial breed-silhouette watercolor canvas with name/dates | 12x16 gallery canvas | $30.0 | $54.99 | $19.2 | 8 | 10 | 8 | 6 | 8 | 8 | 9 | 4 | 8 | 8 | 8.0 | 7 | $220 | $3160 | 52 | PASS | GO - batch 2 (after batch 1 data) |
| 10 | Retro 'Cat Club' cat-lover sweatshirts | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 8 | 9 | 9 | 8 | 7 | 8 | 8 | 3 | 9 | 8 | 8.0 | 4 | $150 | $2130 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 11 | Personalized family-names plush throw blanket | 50x60 velveteen plush blanket | $36.0 | $59.99 | $17.71 | 8 | 10 | 8 | 6 | 7 | 9 | 8 | 4 | 9 | 8 | 8.0 | 7 | $590 | $3440 | 42 | PASS | GO - batch 2 (after batch 1 data) |
| 12 | Speech-language pathologist (SLP) sweatshirts | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 7 | 9 | 9 | 8 | 7 | 8 | 8 | 6 | 9 | 8 | 8.0 | 4 | $180 | $2640 | 53 | PASS | GO - batch 2 (after batch 1 data) |
| 13 | 'Grandpa Est.' hoodie with grandkids' names | Hoodie | $29.49 | $49.99 | $15.2 | 8 | 10 | 8 | 6 | 7 | 9 | 8 | 4 | 9 | 8 | 8.0 | 7 | $490 | $2870 | 42 | PASS | GO - batch 2 (after batch 1 data) |
| 14 | 'Retired & Hiking' retro mountain sweatshirts for retirees | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 7 | 9 | 9 | 8 | 7 | 8 | 8 | 5 | 9 | 8 | 7.95 | 4 | $160 | $2300 | 55 | PASS | GO - batch 2 (after batch 1 data) |
| 15 | Mental-health affirmation sweatshirts ('You are enough') | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 8 | 9 | 9 | 8 | 7 | 8 | 7 | 2 | 9 | 8 | 7.85 | 4 | $120 | $1790 | 56 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 16 | Watercolor animal alphabet nursery poster set | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 7 | 8 | 9 | 8 | 8 | 8 | 8 | 3 | 9 | 8 | 7.8 | 4 | $80 | $1130 | 59 | PASS | GO - batch 2 (after batch 1 data) |
| 17 | Vintage topographic mountain posters from public-domain USGS data | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 7 | 8 | 8 | 8 | 8 | 7 | 9 | 5 | 9 | 8 | 7.8 | 4 | $110 | $1600 | 55 | PASS | GO - batch 2 (after batch 1 data) |
| 18 | Retro sunset 'Pickleball Club' Comfort Colors tees for 50+ players | Comfort Colors 1717 tee | $20.0 | $32.99 | $9.34 | 8 | 7 | 9 | 8 | 7 | 8 | 8 | 3 | 9 | 8 | 7.7 | 4 | $110 | $1630 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 19 | Retro-wave nurse specialty tees (L&D, NICU, ER, Oncology) | Comfort Colors 1717 tee | $20.0 | $32.99 | $9.34 | 8 | 7 | 9 | 8 | 7 | 8 | 9 | 3 | 8 | 8 | 7.7 | 4 | $110 | $1630 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 20 | Personalized kids' name dinosaur room posters | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 4 | 9 | 8 | 7.7 | 7 | $120 | $1720 | 52 | PASS | GO - batch 2 (after batch 1 data) |
| 21 | Coffee + books lover 20oz tumblers | 20oz stainless tumbler | $20.5 | $34.99 | $10.64 | 7 | 8 | 9 | 8 | 7 | 8 | 8 | 3 | 9 | 8 | 7.7 | 4 | $90 | $1320 | 59 | PASS | GO - batch 2 (after batch 1 data) |
| 22 | Speech-language pathologist (SLP) mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 7 | 7 | 9 | 8 | 7 | 8 | 8 | 6 | 9 | 8 | 7.7 | 4 | $110 | $1600 | 53 | PASS | GO - batch 2 (after batch 1 data) |
| 23 | Personalized family-names Christmas ceramic ornament | Ceramic ornament | $11.5 | $21.99 | $7.9 | 9 | 6 | 8 | 6 | 8 | 9 | 8 | 3 | 9 | 8 | 7.6 | 7 | $230 | $1350 | 39 | PASS | GO - batch 2 (after batch 1 data) |
| 24 | Baby's First Christmas 2026 ornament with name + birth stats | Ceramic ornament | $11.5 | $21.99 | $7.9 | 9 | 6 | 8 | 6 | 8 | 9 | 8 | 3 | 9 | 8 | 7.6 | 7 | $230 | $1350 | 39 | PASS | GO - batch 2 (after batch 1 data) |
| 25 | Zodiac constellation + birth-month mugs | 11oz white ceramic mug | $11.89 | $21.99 | $7.51 | 8 | 6 | 9 | 8 | 8 | 8 | 8 | 2 | 9 | 8 | 7.6 | 4 | $60 | $910 | 56 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 26 | 'Promoted to Grandma' pregnancy-reveal mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 8 | 7 | 9 | 6 | 7 | 9 | 8 | 3 | 9 | 8 | 7.6 | 7 | $220 | $1290 | 44 | PASS | GO - batch 2 (after batch 1 data) |
| 27 | Profession-specific retirement gag mugs (retired teacher/nurse/cop) | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 7 | 7 | 9 | 8 | 7 | 8 | 8 | 4 | 9 | 8 | 7.6 | 4 | $80 | $1180 | 57 | PASS | GO - batch 2 (after batch 1 data) |
| 28 | Custom-number soccer/hockey mom sweatshirts | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 8 | 9 | 8 | 6 | 7 | 8 | 8 | 3 | 8 | 8 | 7.6 | 7 | $150 | $2130 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 29 | Birth-month flower + name minimalist mugs for moms/best friends | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 8 | 7 | 8 | 6 | 7 | 8 | 9 | 4 | 9 | 8 | 7.55 | 7 | $100 | $1490 | 52 | PASS | GO - batch 2 (after batch 1 data) |
| 30 | Cottagecore mushroom field-guide mugs | 11oz white ceramic mug | $11.89 | $21.99 | $7.51 | 7 | 6 | 9 | 8 | 8 | 8 | 8 | 4 | 9 | 8 | 7.55 | 4 | $70 | $1000 | 57 | PASS | GO - batch 2 (after batch 1 data) |
| 31 | Sourdough baker 'starter' illustrated mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 7 | 7 | 9 | 8 | 7 | 8 | 7 | 5 | 9 | 8 | 7.55 | 4 | $90 | $1390 | 55 | PASS | GO - batch 2 (after batch 1 data) |
| 32 | Retro trail line-art mugs for retired hikers (generic peaks, no NPS marks) | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 7 | 7 | 9 | 8 | 7 | 8 | 8 | 4 | 8 | 8 | 7.5 | 4 | $80 | $1180 | 57 | PASS | GO - batch 2 (after batch 1 data) |
| 33 | Mahjong club tote bags for women's weekly mahjong groups | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 7 | 6 | 9 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 7.5 | 4 | $120 | $1730 | 51 | PASS | GO - batch 2 (after batch 1 data) |
| 34 | 'Just one more chapter' bookish tote bags | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 8 | 6 | 9 | 8 | 7 | 8 | 8 | 2 | 9 | 8 | 7.5 | 4 | $70 | $1040 | 56 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 35 | Personalized 'Grandpa's Fishing Buddies' mug with kids' names | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 8 | 7 | 8 | 6 | 7 | 9 | 8 | 3 | 9 | 8 | 7.5 | 7 | $220 | $1290 | 44 | PASS | GO - batch 2 (after batch 1 data) |
| 36 | Backyard chicken-keeper humor mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 7 | 7 | 9 | 8 | 7 | 8 | 7 | 4 | 9 | 8 | 7.5 | 4 | $80 | $1180 | 57 | PASS | GO - batch 2 (after batch 1 data) |
| 37 | Nurse appreciation tumblers by specialty | 20oz stainless tumbler | $20.5 | $34.99 | $10.64 | 7 | 8 | 9 | 8 | 7 | 7 | 8 | 3 | 8 | 8 | 7.5 | 4 | $90 | $1320 | 59 | PASS | GO - batch 2 (after batch 1 data) |
| 38 | Personalized family-name garden flags (seasonal sets) | Garden flag | $13.5 | $24.99 | $8.61 | 7 | 7 | 8 | 6 | 8 | 8 | 8 | 5 | 9 | 8 | 7.45 | 7 | $90 | $1340 | 55 | PASS | GO - batch 2 (after batch 1 data) |
| 39 | Ghosts reading books Halloween sweatshirt | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 9 | 9 | 9 | 8 | 7 | 3 | 6 | 2 | 9 | 8 | 7.4 | 4 | $160 | $2300 | 51 | PASS | PASS but seasonal window closed - queue for next season |
| 40 | Couple line-art 'Est.' wedding-date mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 8 | 7 | 8 | 6 | 7 | 8 | 8 | 3 | 9 | 8 | 7.4 | 7 | $90 | $1290 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 41 | Funny introvert 'social battery' tees | Unisex tee | $16.5 | $28.99 | $9.23 | 8 | 7 | 9 | 8 | 7 | 8 | 6 | 1 | 9 | 8 | 7.4 | 4 | $70 | $980 | 58 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 42 | Custom teacher-name classroom tote bags | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 8 | 6 | 8 | 6 | 7 | 9 | 8 | 3 | 9 | 8 | 7.35 | 7 | $210 | $1240 | 44 | PASS | GO - batch 2 (after batch 1 data) |
| 43 | Bachelorette group tees by destination city (Nashville, Scottsdale) | Unisex tee | $16.5 | $28.99 | $9.23 | 9 | 7 | 8 | 6 | 7 | 7 | 8 | 2 | 8 | 8 | 7.3 | 7 | $110 | $1550 | 51 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 44 | '100 Days of School' teacher tees | Unisex tee | $16.5 | $28.99 | $9.23 | 8 | 7 | 9 | 8 | 7 | 5 | 7 | 3 | 9 | 8 | 7.3 | 4 | $100 | $1440 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 45 | 'Reel Cool Dad' fishing tees | Unisex tee | $16.5 | $28.99 | $9.23 | 8 | 7 | 9 | 8 | 7 | 6 | 6 | 2 | 9 | 8 | 7.25 | 4 | $80 | $1210 | 56 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 46 | Personalized bridal-party tote bags | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 8 | 6 | 8 | 6 | 7 | 8 | 8 | 3 | 9 | 8 | 7.25 | 7 | $80 | $1240 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 47 | End-of-year teacher appreciation tumblers | 20oz stainless tumbler | $20.5 | $34.99 | $10.64 | 8 | 8 | 9 | 6 | 7 | 5 | 7 | 3 | 9 | 8 | 7.25 | 7 | $120 | $1730 | 54 | PASS | GO - batch 2 (after batch 1 data) |
| 48 | Custom family 'Campfire Crew' camping tees | Unisex tee | $16.5 | $28.99 | $9.23 | 7 | 7 | 8 | 6 | 7 | 7 | 8 | 4 | 9 | 8 | 7.2 | 7 | $90 | $1320 | 57 | PASS | GO - batch 2 (after batch 1 data) |
| 49 | Retro 'Mama' sweatshirt with kids' names on sleeve | Crewneck sweatshirt | $28.99 | $42.99 | $9.38 | 9 | 7 | 7 | 6 | 4 | 9 | 8 | 2 | 9 | 8 | 7.2 | 7 | $390 | $2300 | 41 | PASS | PASS but saturated - only with a clearly fresh design angle |
| 50 | Embroidered 'Girl Dad' dad hats | Embroidered dad hat | $20.94 | $32.99 | $8.4 | 7 | 6 | 8 | 8 | 6 | 7 | 7 | 3 | 9 | 8 | 7.0 | 4 | $80 | $1240 | 59 | PASS | GO - batch 2 (after batch 1 data) |
| 51 | Valentine couple initials mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 7 | 7 | 8 | 6 | 7 | 6 | 7 | 3 | 9 | 8 | 6.95 | 7 | $70 | $980 | 59 | PASS | GO - batch 2 (after batch 1 data) |
| 52 | 'Est. 2027' pregnancy announcement onesies | Baby bodysuit | $15.5 | $24.99 | $6.61 | 7 | 5 | 8 | 6 | 6 | 8 | 7 | 4 | 9 | 8 | 6.8 | 7 | $80 | $1140 | 57 | PASS | GO - batch 2 (after batch 1 data) |
| 53 | Florida native birds vintage field-guide posters (spoonbill, sandhill crane) | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 6 | 8 | 9 | 8 | 8 | 8 | 7 | 7 | 9 | 8 | 7.75 | 4 | $120 | $1720 | 56 | fail | NO-GO: demand<7 |
| 54 | 'Bird Nerd' birdwatching sweatshirts | Crewneck sweatshirt | $25.49 | $42.99 | $12.88 | 6 | 9 | 9 | 8 | 7 | 8 | 7 | 6 | 9 | 8 | 7.75 | 4 | $150 | $2130 | 58 | fail | NO-GO: demand<7 |
| 55 | Occupational therapy (OT) tees | Comfort Colors 1717 tee | $20.0 | $32.99 | $9.34 | 6 | 7 | 9 | 8 | 7 | 8 | 7 | 6 | 9 | 8 | 7.45 | 4 | $110 | $1630 | 58 | fail | NO-GO: demand<7 |
| 56 | Quilting club mugs | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 6 | 7 | 9 | 8 | 7 | 8 | 7 | 6 | 9 | 8 | 7.45 | 4 | $90 | $1290 | 58 | fail | NO-GO: demand<7 |
| 57 | Retro motel-sign tees for Florida beach towns | Unisex tee | $16.5 | $28.99 | $9.23 | 6 | 7 | 9 | 8 | 7 | 8 | 8 | 5 | 8 | 8 | 7.4 | 4 | $80 | $1210 | 60 | fail | NO-GO: demand<7 |
| 58 | Vintage botanical illustration desk mats for WFH | Desk mat | $22.0 | $34.99 | $9.14 | 6 | 7 | 9 | 8 | 6 | 8 | 7 | 7 | 9 | 8 | 7.4 | 4 | $140 | $2010 | 56 | fail | NO-GO: demand<7 |
| 59 | Vet tech humor tees | Unisex tee | $16.5 | $28.99 | $9.23 | 6 | 7 | 9 | 8 | 7 | 8 | 7 | 5 | 9 | 8 | 7.4 | 4 | $80 | $1210 | 60 | fail | NO-GO: demand<7 |
| 60 | Vintage-style Florida orange-crate label posters (fictional brands) | 18x24 matte poster | $15.0 | $29.99 | $11.63 | 5 | 8 | 9 | 8 | 8 | 8 | 6 | 6 | 8 | 8 | 7.35 | 4 | $80 | $1130 | 63 | fail | NO-GO: demand<7 |
| 61 | Retro 'Lifting Club' gym tees | Unisex tee | $16.5 | $28.99 | $9.23 | 6 | 7 | 9 | 8 | 7 | 8 | 7 | 3 | 9 | 8 | 7.3 | 4 | $50 | $750 | 64 | fail | NO-GO: demand<7 |
| 62 | Wine humor tumblers | 20oz stainless tumbler | $20.5 | $34.99 | $10.64 | 6 | 8 | 9 | 8 | 7 | 8 | 6 | 2 | 9 | 8 | 7.3 | 4 | $50 | $690 | 66 | fail | NO-GO: demand<7 |
| 63 | Firefighter/first-responder family tees | Unisex tee | $16.5 | $28.99 | $9.23 | 6 | 7 | 9 | 8 | 7 | 8 | 7 | 5 | 8 | 8 | 7.3 | 4 | $80 | $1210 | 60 | fail | NO-GO: demand<7 |
| 64 | Librarian humor tote bags | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 6 | 6 | 9 | 8 | 7 | 8 | 7 | 6 | 9 | 8 | 7.3 | 4 | $80 | $1240 | 58 | fail | NO-GO: demand<7 |
| 65 | 'Yarn hoarder' knitting project tote | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 6 | 6 | 9 | 8 | 7 | 8 | 7 | 5 | 9 | 8 | 7.25 | 4 | $70 | $1040 | 60 | fail | NO-GO: demand<7 |
| 66 | Hometown coordinates + topo mug | 15oz white ceramic mug | $14.5 | $25.99 | $8.52 | 6 | 7 | 8 | 6 | 7 | 8 | 8 | 5 | 9 | 8 | 7.2 | 7 | $70 | $1080 | 60 | fail | NO-GO: demand<7 |
| 67 | Vintage beekeeping field-guide tote bags | Cotton canvas tote | $14.99 | $24.99 | $7.12 | 5 | 6 | 9 | 8 | 7 | 8 | 6 | 8 | 9 | 8 | 7.15 | 4 | $90 | $1340 | 59 | fail | NO-GO: demand<7 |
| 68 | Original painterly landscape 500-pc puzzles | 500-pc jigsaw puzzle | $24.0 | $36.99 | $8.95 | 5 | 7 | 9 | 8 | 6 | 8 | 6 | 7 | 9 | 8 | 7.15 | 4 | $110 | $1680 | 61 | fail | NO-GO: demand<7 |
| 69 | Original boho floral phone cases | Tough phone case | $13.5 | $22.99 | $6.81 | 6 | 5 | 9 | 8 | 7 | 8 | 7 | 2 | 9 | 8 | 6.95 | 4 | $30 | $460 | 66 | fail | NO-GO: demand<7 |
| 70 | Original pixel-art 'retro arcade' desk mats | Desk mat | $22.0 | $34.99 | $9.14 | 6 | 7 | 8 | 8 | 6 | 8 | 7 | 5 | 6 | 8 | 6.9 | 4 | $100 | $1450 | 60 | fail | NO-GO: demand<7, IP risk |
| 71 | AI-stylized custom pet portrait from buyer photo on canvas | 12x16 gallery canvas | $30.0 | $54.99 | $19.2 | 9 | 10 | 5 | 3 | 8 | 5 | 6 | 2 | 7 | 8 | 6.75 | 12 | $200 | $2940 | 51 | fail | NO-GO: IP risk, feasibility<7 |
| 72 | Personalized marathon finisher tees with time | Unisex tee | $16.5 | $28.99 | $9.23 | 7 | 7 | 7 | 6 | 7 | 6 | 6 | 5 | 6 | 8 | 6.55 | 7 | $110 | $1550 | 55 | fail | NO-GO: IP risk |
| 73 | Bookish kiss-cut sticker sheets | Kiss-cut sticker sheet | $10.29 | $14.99 | $2.79 | 7 | 2 | 9 | 8 | 4 | 9 | 8 | 2 | 9 | 8 | 6.55 | 4 | $30 | $450 | 61 | fail | NO-GO: margin $2.79<6 |
| 74 | Personalized pet bandanas | Pet bandana | $12.5 | $19.99 | $5.1 | 7 | 3 | 8 | 6 | 6 | 8 | 7 | 3 | 9 | 8 | 6.45 | 7 | $50 | $750 | 59 | fail | NO-GO: margin $5.10<6 |
| 75 | Nurse water-bottle kiss-cut stickers | 3x3 kiss-cut sticker | $6.29 | $7.99 | $0.47 | 7 | 2 | 9 | 8 | 2 | 9 | 8 | 2 | 9 | 8 | 6.35 | 4 | $20 | $240 | 61 | fail | NO-GO: margin $0.47<6 |

Per-score one-line reasons for every idea are in `etsy-pod.json` (`scoreReasons`).

## 5. Compliance checklist (every listing)
- Original design only; no trademarks, celebrities, brands, team/league logos, fandom IP, book titles or lyrics; run a USPTO TESS search on any phrase-based design.
- Description includes an AI disclosure line; production partner (Printify + print provider) is linked to the listing and named on the shop page.
- Mockups show the real product; no fake reviews or invented scarcity; state print-on-demand production and shipping times honestly.
- Opt out of Offsite Ads until margins are proven; collect sales tax via Etsy (marketplace facilitator).

## 6. Sources
- [Etsy Fees & Payments Policy (updated Oct 5, 2026)](https://www.etsy.com/legal/fees/)
- [Etsy Help: What are the Fees and Taxes for Selling on Etsy?](https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy)
- [Etsy Help: Etsy Fee Basics](https://help.etsy.com/hc/en-us/articles/360035902374-Etsy-Fee-Basics)
- [Etsy: How to sell on Etsy (US)](https://www.etsy.com/sell)
- [Etsy Help: How Etsy's Offsite Ads Work](https://help.etsy.com/hc/en-us/articles/360000338367-How-Etsy-s-Offsite-Ads-Work)
- [Etsy Help: How to Open a Second Shop on Etsy](https://help.etsy.com/hc/en-us/articles/360017604474-How-to-Open-a-Second-Shop-on-Etsy)
- [Etsy Community: same card/bank on new shop flagged](https://community.etsy.com/t5/Technical-Issues/I-opened-a-new-shop-with-the-same-credit-card-and-bank-account/td-p/138857926)
- [Etsy's Creativity Standards](https://www.etsy.com/legal/creativity)
- [Etsy Seller Policy](https://www.etsy.com/legal/sellers/)
- [Etsy Seller Handbook: Etsy's stance on AI creations](https://www.etsy.com/seller-handbook/article/1275449912004)
- [Etsy Seller Handbook: Production Partner Policy](https://www.etsy.com/seller-handbook/article/1276487437920)
- [Etsy Seller Handbook: Protecting Creativity](https://www.etsy.com/seller-handbook/article/1276491338090)
- [Printify vs Printful (Printify, data Oct 2026)](https://printify.com/printify-vs-printful/)
- [Printify Help: Automated personalization for Etsy](https://help.printify.com/hc/en-us/articles/40720228428433)
- [Printify Help: What is product personalization](https://help.printify.com/hc/en-us/articles/28903711308177-What-is-product-personalization-on-Printify)
- [Printify blog: Can you have more than one Etsy shop](https://printify.com/blog/can-you-have-more-than-one-etsy-shop/)
- [Printify blog: Best-selling items on Etsy 2026 (eRank Q1 2026 data)](https://printify.com/blog/best-selling-items-on-etsy/)
- [Printful Pricing 2026 (inso.codes)](https://www.inso.codes/apps/pricing/printful-pricing)
- [Printful Review 2026 (MerchTitans)](https://merchtitans.com/blog/printful-review-2026)
- [PodVector: Printful shipping cost](https://podvector.ai/articles/printful/costs-and-charges/printful-shipping-cost-full-breakdown-for-pod-sellers)
- [PodVector: Printify prices](https://podvector.ai/articles/printify/costs-and-charges/printify-prices-full-breakdown-for-pod-sellers)
- [Kitmere: Printify pricing explained](https://kitmere.com/guides/printify-pricing-explained/)
- [Printful vs Printify 2026 (ecommerceparadise)](https://ecommerceparadise.com/printful-vs-printify/)
- [Craftybase: Etsy fees 2026](https://craftybase.com/blog/the-complete-guide-to-etsy-fees)
- [Marmalead: Etsy POD in 2026](https://blog.marmalead.com/etsy-print-on-demand/)
- [Growtsy: Did Etsy ban POD in 2026?](https://www.growtsy.com/etsy-print-on-demand)
- [ShieldMyShop: Production partner disclosure guide 2026](https://www.shieldmyshop.com/blog/2026-05-21-etsy-production-partner-disclosure-pod-guide)
- [MerchOne: Etsy POD niches 2026](https://merchone.com/blog/etsy-print-on-demand-niches/)
- [Teeinblue: POD trends 2026](https://teeinblue.com/blogs/en/print-on-demand-trends)
- [Etsy Open API v3 reference (via Jentic mirror)](https://jentic.com/apis/etsy.com/etsy.md)
