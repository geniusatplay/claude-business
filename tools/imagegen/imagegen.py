"""Image pipeline CLI for the Design & Code Studio (OpenAI image API).

Commands:
  grid   PROMPT_FILE                      one 1024x1024 image: a 2x2 grid of four variations
  crop   IMAGE {tl,tr,bl,br}              cut one quadrant out of a grid image
  final  QUADRANT_IMAGE PROMPT_FILE --shape {portrait,landscape}
                                          edit endpoint, transparent PNG, 1024x1536 or 1536x1024
  frame  PROMPT_FILE --aspect {9:16,16:9} [--ref PHOTO]
                                          video first frame, optional reference photo
  models                                  list image models the key can use

Every image lands in D:\\AI\\Studio\\images\\<UTC date>\\ with a .json sidecar.
The key is read from <repo>\\.secrets\\.env (OPENAI_API_KEY) and is never printed.
"""
import argparse
import base64
import datetime as dt
import json
import os
import sys
from pathlib import Path

import truststore

truststore.inject_into_ssl()  # verify TLS against the Windows cert store (this PC's proxy re-signs HTTPS)

from openai import OpenAI  # noqa: E402
from PIL import Image  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
ENV_FILE = REPO / ".secrets" / ".env"
OUT_ROOT = Path(os.environ.get("STUDIO_IMAGES", r"D:\AI\Studio\images"))
FALLBACK_MODEL = "gpt-image-1"
GRID_SUFFIX = ("\n\nA 2x2 grid of four distinct variations of the same brief, separated by thin white "
               "gutters; each quadrant is a complete standalone design; no labels or numbers.")
FINAL_SUFFIX = ("\n\nReproduce exactly the design in the reference image, alone, centered, on a fully "
                "transparent background. No mockup, no shirt, no shadow, no border.")
SIZES = {"portrait": "1024x1536", "landscape": "1536x1024", "9:16": "1024x1536", "16:9": "1536x1024"}


def load_key():
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8-sig").splitlines():
            name, sep, value = line.strip().partition("=")
            if sep and name.strip().removeprefix("export ").strip() == "OPENAI_API_KEY":
                return value.strip().strip('"').strip("'")
    sys.exit(f"OPENAI_API_KEY not found in {ENV_FILE}")


def client():
    return OpenAI(api_key=load_key())


def image_models(c):
    models = [m for m in c.models.list() if m.id.startswith(("gpt-image", "chatgpt-image"))]
    return sorted(models, key=lambda m: (m.created or 0, m.id), reverse=True)


def pick_model(c, override):
    if override:
        return override
    try:
        # Prefer undated aliases (e.g. gpt-image-2 over gpt-image-2-2026-...) among the newest.
        models = image_models(c)
        aliases = [m for m in models if not m.id[-10:].replace("-", "").isdigit()]
        return (aliases or models)[0].id
    except Exception as e:  # listing not permitted or no image models listed
        print(f"model list failed ({type(e).__name__}); using {FALLBACK_MODEL}")
        return FALLBACK_MODEL


def out_dir():
    d = OUT_ROOT / dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    d.mkdir(parents=True, exist_ok=True)
    return d


def stem(kind):
    return f"{dt.datetime.now(dt.timezone.utc).strftime('%H%M%S')}_{kind}"


def save_response(raw, kind, meta):
    resp = raw.parse()
    d, base = out_dir(), stem(kind)
    paths = []
    for i, item in enumerate(resp.data):
        p = d / f"{base}{'' if len(resp.data) == 1 else f'_{i}'}.png"
        p.write_bytes(base64.b64decode(item.b64_json))
        usage = getattr(resp, "usage", None)
        side = {
            **meta,
            "kind": kind,
            "file": str(p),
            "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "api_image_id": getattr(item, "id", None) or getattr(resp, "id", None),
            "api_created": getattr(resp, "created", None),
            "api_request_id": raw.headers.get("x-request-id"),
            "revised_prompt": getattr(item, "revised_prompt", None),
            "usage": usage.model_dump() if usage else None,
        }
        p.with_suffix(".json").write_text(json.dumps(side, indent=2), encoding="utf-8")
        paths.append(p)
        print(f"saved {p}")
        if usage:
            print(f"usage: {usage.model_dump()}")
    return paths


def read_prompt(path):
    return Path(path).read_text(encoding="utf-8").strip()


def cmd_models(a):
    c = client()
    try:
        for m in image_models(c):
            print(m.id, dt.datetime.fromtimestamp(m.created or 0, dt.timezone.utc).date())
    except Exception as e:
        print(f"cannot list models: {type(e).__name__}: {getattr(e, 'message', e)}")
    print("chosen:", pick_model(c, a.model))


def cmd_grid(a):
    c = client()
    model = pick_model(c, a.model)
    prompt = read_prompt(a.prompt_file) + GRID_SUFFIX
    params = dict(model=model, prompt=prompt, size="1024x1024", quality=a.quality,
                  background="opaque", output_format="png", n=1)
    raw = c.images.with_raw_response.generate(**params)
    save_response(raw, "grid", {**params, "prompt_file": str(Path(a.prompt_file).resolve())})


def cmd_crop(a):
    img = Image.open(a.image)
    w, h = img.size
    x = 0 if a.quadrant[1] == "l" else w // 2
    y = 0 if a.quadrant[0] == "t" else h // 2
    part = img.crop((x, y, x + w // 2, y + h // 2))
    p = out_dir() / f"{stem('crop')}_{a.quadrant}.png"
    part.save(p)
    side = {"kind": "crop", "file": str(p), "source": str(Path(a.image).resolve()),
            "quadrant": a.quadrant, "size": f"{part.width}x{part.height}"}
    src_side = Path(a.image).with_suffix(".json")
    if src_side.exists():
        side["source_sidecar"] = json.loads(src_side.read_text(encoding="utf-8"))
    p.with_suffix(".json").write_text(json.dumps(side, indent=2), encoding="utf-8")
    print(f"saved {p}")


def cmd_final(a):
    c = client()
    model = pick_model(c, a.model)
    prompt = read_prompt(a.prompt_file) + FINAL_SUFFIX
    params = dict(model=model, prompt=prompt, size=SIZES[a.shape], quality=a.quality,
                  background="transparent", output_format="png", n=1)
    with open(a.image, "rb") as f:
        raw = c.images.with_raw_response.edit(image=f, **params)
    save_response(raw, "final", {**params, "reference": str(Path(a.image).resolve()),
                                 "prompt_file": str(Path(a.prompt_file).resolve())})


def cmd_frame(a):
    c = client()
    model = pick_model(c, a.model)
    prompt = read_prompt(a.prompt_file)
    params = dict(model=model, prompt=prompt, size=SIZES[a.aspect], quality=a.quality,
                  output_format="png", n=1)
    meta = {**params, "aspect": a.aspect, "prompt_file": str(Path(a.prompt_file).resolve())}
    if a.ref:
        with open(a.ref, "rb") as f:
            raw = c.images.with_raw_response.edit(image=f, **params)
        meta["reference"] = str(Path(a.ref).resolve())
    else:
        raw = c.images.with_raw_response.generate(**params)
    save_response(raw, "frame", meta)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", help="override the auto-picked newest image model")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("models").set_defaults(fn=cmd_models)
    p = sub.add_parser("grid"); p.add_argument("prompt_file"); p.set_defaults(fn=cmd_grid)
    p = sub.add_parser("crop"); p.add_argument("image"); p.add_argument("quadrant", choices=["tl", "tr", "bl", "br"])
    p.set_defaults(fn=cmd_crop)
    p = sub.add_parser("final"); p.add_argument("image"); p.add_argument("prompt_file")
    p.add_argument("--shape", default="portrait", choices=["portrait", "landscape"]); p.set_defaults(fn=cmd_final)
    p = sub.add_parser("frame"); p.add_argument("prompt_file"); p.add_argument("--aspect", default="9:16", choices=["9:16", "16:9"])
    p.add_argument("--ref", help="reference photo (e.g. the real product)"); p.set_defaults(fn=cmd_frame)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
