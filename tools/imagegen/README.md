# imagegen: OpenAI image pipeline CLI

Runs on the 4090 PC. Implements the flow in `CEO - Claude/Design and Code Studio/image-pipeline.md`.

## Setup (done once)
- Venv: `D:\AI\Tools\imagegen-venv` (Python 3.12 via uv), packages from `requirements.txt`.
- Key: `OPENAI_API_KEY` in `.secrets\.env` at the repo root. The script never prints it.
- TLS: this PC's proxy re-signs HTTPS, so the script verifies against the Windows certificate store (`truststore`).

## Commands
```powershell
$py = 'D:\AI\Tools\imagegen-venv\Scripts\python.exe'
& $py tools\imagegen\imagegen.py grid  brief.txt                          # 1024x1024, 2x2 grid, quality high
& $py tools\imagegen\imagegen.py crop  D:\AI\Studio\images\<date>\<file>.png tr
& $py tools\imagegen\imagegen.py final <crop>.png brief.txt --shape portrait   # 1024x1536 (tees, posters); landscape = 1536x1024 (mugs)
& $py tools\imagegen\imagegen.py frame scene.txt --aspect 9:16 --ref product.jpg
& $py tools\imagegen\imagegen.py models                                   # what the key can see
```
Global options come before the command: `--quality low|medium|high|auto` (default high), `--model <id>`.

- `grid` appends the standard 2x2-grid instruction and uses an opaque background.
- `final` sends the crop to the edit endpoint with `background: transparent`, PNG.
- `frame` uses the edit endpoint when `--ref` is given, otherwise plain generation.

## Output
Everything goes to `D:\AI\Studio\images\<UTC date>\HHMMSS_<kind>.png` with a `.json` sidecar: prompt, model, size, quality, background, API image id (when the API returns one), request id, created time, token usage. Crops keep the source sidecar.

## Model choice
The script lists the account's models and picks the newest `gpt-image*` alias. The current key is restricted (no `api.model.read` scope), so it falls back to `gpt-image-1`. Pass `--model` to use a newer one, or grant the key "Models: Read".

## Notes
- No images or secrets go in this repo.
- The API does not return a cost. Estimate it from `usage` in the sidecar using OpenAI's current price page.
