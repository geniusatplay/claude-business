# Image pipeline (OpenAI image API)

Owner: Pixie, Prompt Writer (Design & Code Studio). Runs on the 4090 PC. Key: `OPENAI_API_KEY` in `.secrets/.env` only.
Model: the newest OpenAI image model available on the account (check the models list at run time; `gpt-image-1` or later).

## Flow for every design
1. **Brief** from the venture manager: product and print area, niche and buyer, style, colour count, exact text (spelled out), things to avoid.
2. **Grid round:** one image, 1024×1024, quality high, opaque white background, a 2×2 grid with four clearly different variations.
3. **Review:** a panel of 3 (Thea design, Argus market, Cato IP/rules) scores each quadrant and names the winner (top-left, top-right, bottom-left or bottom-right). Under 85 means new concepts; 85–94 means a revised grid (max 5 rounds); 95+ goes to the final.
4. **Final:** crop the winning quadrant and send it as the reference to the image edit endpoint, asking for that exact design alone: transparent background (`background: "transparent"`, PNG), centered, no mockup, no shirt, no shadow, no border. Size 1024×1536 for tees and posters, 1536×1024 for mug wraps.
5. **Upscale** on the 4090 with Real-ESRGAN (BSD-3, commercial use OK) to the print size (tees 4500×5400 px at 300 DPI). Check the edges are clean and the text is spelled correctly.
6. **Mockups:** use Printify's own generated mockups so listings show the real product (Etsy requires accurate photos).
7. **Log** every prompt, setting, image ID and review score in the venture's archive folder.

## Prompt rules (Prompt Writer)
- State the output format first: "Print-ready graphic design only, isolated on a plain background, no t-shirt, no mockup, no model, no frame."
- Name the style exactly (e.g., "vintage screen-print, 3 solid spot colours: forest green #2F5D3A, cream #F3E9D2, brick red #A23B2A, distressed texture, bold outlines").
- Spell all text in quotes, give its font style and placement, and add "text must read exactly as written, no extra words".
- Give composition: subject, pose, framing, centre weight, empty margin for printing.
- For the grid: "A 2×2 grid of four distinct variations of the same brief, separated by thin white gutters; each quadrant is a complete standalone design; no labels or numbers."
- Exclusions every time: no logos, no brand names, no real people or celebrities, no copyrighted characters, no watermark, no signature.
- Keep colour count low (2–5) for clean DTG/screen printing; avoid fine gradients near edges.

## Video first frames (affiliate clothing videos)
- 9:16 (1024×1536) or 16:9 (1536×1024) scene, photographic, with the product shown accurately.
- Use Randy's own photo of the real product (or seller-provided assets with permission) as the edit reference, never Amazon listing images (Amazon's Associates policy bans altering them or using them for AI). The garment must match exactly. Label AI visuals, disclose #ad spoken and on screen, and keep opinions in Randy's own voice.
- Then animate the frame on the 4090 with Wan2GP.

## Approved models on the 4090 PC (per Randy, 2026-10-21)
- **Krea 2** (ComfyUI): approved for business images.
- **MiniMax H3** (Wan2GP): approved for business video. Always render at **720p**, **15–20 seconds** per clip.
- **LTX 2.5** (Wan2GP): video fallback.
- **OpenAI image API**: print designs and video first frames.
- **Not for business work:** FLUX.2 klein 9B, Depth Anything V2 Large, MatAnyone (non-commercial licenses), and all NSFW LoRAs.
- Write all outputs to D: (C: is nearly full).
