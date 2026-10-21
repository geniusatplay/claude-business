# GPU Studio Inventory

Taken 2026-10-21 on Randy's RTX 4090 PC. Read-only check: nothing was installed, started, changed or deleted.

## 1. Hardware

| Item | Value |
|---|---|
| GPU | NVIDIA GeForce RTX 4090 (WDDM) |
| Driver | 596.21 |
| CUDA (driver max) | 13.2 |
| VRAM | 24,564 MiB total · 1,744 MiB used · 22,395 MiB free (only desktop apps; Blender 5.1 is open) |

| Drive | Used | Free |
|---|---|---|
| C: | 1,842.9 GB | **19.2 GB (low)** |
| D: | 5,804.7 GB | 1,647.3 GB |
| E: | 104.1 GB | 14.4 GB |

## 2. ComfyUI (`D:\AI\ComfyUI_windows_portable`)

- Folder exists: **yes**
- Running: **no** (nothing answers on 127.0.0.1:8188). It was left off.

### Models (`ComfyUI\models`)

| Folder | File | Size |
|---|---|---|
| checkpoints | bigkrea2RawV14_bf16.safetensors | 23.88 GB |
| checkpoints | test2v14Klein9b_base.safetensors | 16.91 GB |
| checkpoints | test_v14Klein9bDistilled_full_fp8.safetensors | 8.46 GB |
| diffusion_models | flux-2-klein-9b-kv-fp8.safetensors | 9.14 GB |
| diffusion_models | krea2_turbo_fp8_scaled.safetensors | 12.24 GB |
| unet | bigkrea2RawV14_fp8_e4m3fn.safetensors | 11.94 GB |
| loras | krea2_darkbrush.safetensors | 0.44 GB |
| loras | krea2_style_reference.safetensors | 0.43 GB |
| loras\Krea 2 | krea2_photoSlider14B.safetensors | 0.03 GB |
| loras\Krea 2\Utilities | depth-control-lora.safetensors | 0.80 GB |
| loras\Krea 2\Utilities | krea2_anypaint_rank32.safetensors | 0.21 GB |
| loras\Krea 2\Utilities | krea2_identity_edit_v1_2.safetensors | 1.70 GB |
| vae | flux2-vae.safetensors | 0.31 GB |
| vae | qwen_image_vae.safetensors | 0.24 GB |
| vae_approx | taef1_encoder/decoder, taesdxl_encoder/decoder, taesd_encoder/decoder | <0.01 GB each |
| text_encoders | qwen3vl_4b_fp8_scaled.safetensors | 4.88 GB |
| text_encoders | qwen_3_8b_fp8mixed.safetensors | 8.07 GB |
| upscale_models | 1xSkinContrast-High-SuperUltraCompact.pth | <0.01 GB |
| depthanything | depth_anything_v2_vitl.pth | 1.25 GB |
| sam3 | sam3.1_multiplex_fp16.safetensors | 1.63 GB |
| segformer_b2_clothes | model.safetensors | 0.10 GB |
| vitmatte\vitmatte-small-composition-1k | model.safetensors | 0.10 GB |
| vosr2\VOSR2\checkpoints | ema_model.safetensors | 5.19 GB |
| vosr2\VOSR2\Qwen-Image-vae-2d | diffusion_pytorch_model.safetensors | 0.17 GB |
| vosr2\VOSR2 | dinov2_vitl14.safetensors | 1.13 GB |
| LLM | Huihui-Qwen3.5-9B-abliterated.Q8_0.gguf | 8.87 GB |
| LLM | Huihui-Qwen3.5-9B-abliterated.mmproj-f16.gguf | 0.86 GB |

No model files in: clip, facerestore_models, or any GFPGAN, CodeFormer or Real-ESRGAN location. There is also no SDXL, SD1.5 or FLUX.1 checkpoint.

### custom_nodes
cg-use-everywhere, ComfyUI-ConditioningKrea2Rebalance, ComfyUI-Custom-Scripts, ComfyUI-KJNodes, ComfyUI-Krea-Moodboards, comfyui-krea2-controlnet, comfyui-krea2edit, ComfyUI-mxToolkit, ComfyUI-vslinx-nodes, comfyui_controlnet_aux, ComfyUI_LC123_nodes, ComfyUI_LC_MaskMaker_nodes, ComfyUI_LC_Vision_nodes, klein_mode_switch, RES4LYF, rgthree-comfy

## 3. Wan2GP

- Folder `D:\AI\Hynyuan video AI\v3\Wan2GPfixed\Wan2GP-main (4)\Wan2GP-main` exists: **yes**
- Conda env `wan2gp4` exists: **yes** (`C:\ProgramData\anaconda3\envs\wan2gp4`). Other envs: base, HunyuanVideo, LivePortrait, flash, sd-webui, wan2gp, and an unnamed one at D:\DeepSeek\env.
- `ckpts` totals **213.6 GB**. Despite the folder names, it currently holds **no Wan or Hunyuan weights**. The video models present are **LTX 2.5** and **MiniMax H3**.

| Folder | File | Size |
|---|---|---|
| ckpts | ltx-2.5-22b-distilled_diffusion_model_int8_convrot.safetensors | 18.15 GB |
| ckpts | ltx-2.5-22b_audio_embeddings_connector_bf16 / _int8_convrot | 0.75 / 0.38 GB |
| ckpts | ltx-2.5-22b_audio_vae_bf16.safetensors | 0.10 GB |
| ckpts | ltx-2.5-22b_diffusion_video_vae_bf16.safetensors | 1.37 GB |
| ckpts | ltx-2.5-22b_text_embedding_projection_bf16.safetensors | 2.15 GB |
| ckpts | ltx-2.5-22b_video_embeddings_connector_bf16 / _int8_convrot | 3.00 / 1.50 GB |
| ckpts | ltx-2.5-22b_video_vae_bf16.safetensors | 1.35 GB |
| ckpts | ltx-2.5-22b_vocoder_bf16.safetensors | 0.24 GB |
| ckpts | ltx-2.5-spatial-upscaler-x2-1.0_bf16.safetensors | 0.93 GB |
| ckpts | ltx-2.5-temporal-upscaler-x2-1.0_bf16.safetensors | 0.24 GB |
| ckpts | ltx-2.3-22b-ic-lora-hdr-scene-emb.safetensors | 0.01 GB |
| ckpts | MiniMax-H3-FL2VA-pruned_rank8_int8_convrot.safetensors | 19.61 GB |
| ckpts | MiniMax-H3-Ref2VA-pruned_rank8_int8_convrot.safetensors | 19.61 GB |
| ckpts | minimaxH3INT8INT4_fl2vaINT8Pruned.safetensors | 19.53 GB |
| ckpts | MiniMax-H3-video_vae_fp16.safetensors | 4.85 GB |
| ckpts | MiniMax-H3-audio_vae_fp32.safetensors | 0.56 GB |
| ckpts\minimax_h3 | minimax_h3_latent_upscaler_3d_bf16.safetensors | 0.64 GB |
| ckpts\gemma4-12b-ltx-v1 | gemma4-12b-ltx-v1_bf16.safetensors | 22.18 GB |
| ckpts\Qwen3-VL-32B-Instruct | Qwen3-VL-32B-Instruct-layer50_bf16.safetensors | 47.97 GB |
| ckpts\Qwen3-VL-32B-Instruct | Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors | 24.89 GB |
| ckpts\Qwen3_8_27B_Uncensored | Qwen3.8-27B-Uncensored-Q4_K_M.gguf | 15.66 GB |
| ckpts\Qwen3_8_27B_Uncensored | Qwen3.8-27B-Uncensored-vision-f16.gguf | 0.86 GB |
| ckpts\bigvgan_v2_44khz_128band_512x | bigvgan_generator.pt | 0.46 GB |
| ckpts\chinese-wav2vec2-base | pytorch_model.bin | 0.35 GB |
| ckpts\wav2vec | model.safetensors | 0.35 GB |
| ckpts\whisper-small | model.safetensors | 0.90 GB |
| ckpts\depth | depth_anything_v2_vitl.pth | 1.25 GB |
| ckpts\det_align | detface.pt | 0.17 GB |
| ckpts\flow | raft-things.pth | 0.02 GB |
| ckpts\mask | matanyone.safetensors | 0.13 GB |
| ckpts\mask | sam_vit_h_4b8939_fp16.safetensors | 1.19 GB |
| ckpts\pose | dw-ll_ucoco_384.onnx | 0.13 GB |
| ckpts\pose | yolox_l.onnx | 0.20 GB |
| ckpts\pyannote | pyannote_model_wespeaker-voxceleb-resnet34-LM.bin | 0.02 GB |
| ckpts\pyannote | pytorch_model_segmentation-3.0.bin | 0.01 GB |
| ckpts\rembg | u2net.onnx | 0.16 GB |
| ckpts\roformer | model_bs_roformer_ep_317_sdr_12.9755.ckpt | 0.60 GB |
| ckpts\scribble | netG_A_latest.pth | 0.02 GB |
| ckpts\seed-vc | DiT_seed_v2_uvit_whisper_base_f0_44k_bigvgan_pruned_ft_ema_v2.pth | 0.76 GB |
| ckpts\seed-vc | rmvpe.pt | 0.17 GB |
| ckpts\seed-vc | campplus_cn_common.bin | 0.03 GB |
| loras\ltx2 | ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors | 0.30 GB |
| loras and loras\minimax_h3 (duplicated) | 11 adult/NSFW MiniMax-H3 LoRAs (file names omitted) | 0.14–0.29 GB each |
| models\minimax_h3\lora_affine_maps | fl2va/ref2va/viggle rank8 + rank64 .sft | <0.01 GB |

## 4. Blender

- Installed: `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe`, version **5.1**. It is currently running.
- Blender MCP tools in this session: **no**. A ToolSearch for "blender" found nothing.

## 5. Model identification and licensing

These are my best understanding, not legal advice. Several of these models came out recently and I couldn't confirm their terms, so **check every license on its model card before selling anything you make with it.**

| Model | Family | License (as I understand it) | OK to sell output? |
|---|---|---|---|
| flux-2-klein-9b-kv-fp8, test2v14Klein9b_base, test_v14Klein9bDistilled | FLUX.2 [klein] 9B (BFL). The "test…" checkpoints look like community fine-tunes or merges. | 9B klein: FLUX non-commercial license (only the 4B klein is Apache-2.0, as I recall) | **⚠ NO**, unless you buy a BFL commercial license. Unsure about the fine-tunes, which inherit the base license. |
| flux2-vae | FLUX.2 VAE | Apache-2.0 (I believe) | Yes |
| bigkrea2RawV14 (bf16 + fp8), krea2_turbo_fp8_scaled, all krea2_* LoRAs | "Krea 2" image model plus community LoRAs. The bigkrea2 one looks like a community fine-tune. | **Unsure.** I can't confirm the Krea 2 open-weights terms. | **? Verify** |
| qwen_3_8b_fp8mixed, qwen3vl_4b_fp8_scaled | Qwen3 / Qwen3-VL text encoders | Apache-2.0 | Yes |
| qwen_image_vae | Qwen-Image VAE | Apache-2.0 | Yes |
| Huihui-Qwen3.5-9B-abliterated (gguf) | Community "abliterated" (refusals removed) Qwen3.5 LLM | Probably inherits Apache-2.0 (unsure) | Probably. Uncensored, so take care with it. |
| taesd / taesdxl / taef1 | Tiny AutoEncoder previews | MIT | Yes |
| 1xSkinContrast-High-SuperUltraCompact | Community ESRGAN-style upscaler (OpenModelDB-type) | **Unsure.** Many of these are CC-BY-NC. | **? Verify** |
| depth_anything_v2_vitl (ComfyUI + Wan2GP) | Depth Anything V2 Large | CC-BY-NC-4.0 (only the Small model is Apache) | **⚠ NO** for commercial use |
| sam3.1_multiplex_fp16 | Meta SAM 3.x | Meta "SAM License" (custom). I believe it permits commercial use, but I'm unsure. | Likely yes. Verify. |
| sam_vit_h_4b8939 | Meta SAM 1 ViT-H | Apache-2.0 | Yes |
| segformer_b2_clothes | SegFormer clothes parser (mattmdjaga) | MIT weights, but trained on ATR data (research-only). Unsure. | ? Grey area |
| vitmatte-small-composition-1k | ViTMatte | MIT code; the Composition-1k data is research-only. Unsure. | ? Grey area |
| VOSR2 (ema_model, Qwen-Image VAE, dinov2_vitl14) | VOSR2 video/super-resolution model; DINOv2 backbone | VOSR2: **unsure**. DINOv2: Apache-2.0. | **? Verify** VOSR2 |
| LTX 2.5 22B (+ upscalers, IC-LoRAs) | Lightricks LTX-2.x video + audio | LTX-2 Community License as I understand it: free commercial use under ~$10M annual revenue, with conditions | Likely yes at our size. Verify the current terms. |
| gemma4-12b-ltx-v1 | Google Gemma 4 text encoder for LTX | Gemma terms (commercial OK, with a prohibited-use policy). Gemma 4 may be Apache-2.0. Unsure. | Likely yes |
| MiniMax-H3 (FL2VA, Ref2VA, VAEs, latent upscaler) | MiniMax (Hailuo) H3 video + audio model | **Unsure**, I can't confirm its terms | **? Verify** |
| 11 MiniMax-H3 NSFW LoRAs | Adult-content community LoRAs | Unknown community licenses | **⚠ Not for business use.** Keep them out of client and store pipelines. |
| Qwen3-VL-32B-Instruct (layer50) | Qwen3-VL 32B (text encoder/captioner) | Apache-2.0 | Yes |
| Qwen3.8-27B-Uncensored (gguf) | Community uncensored Qwen LLM | Probably inherits the base license. Unsure. | Probably. Uncensored. |
| matanyone | MatAnyone video matting | S-Lab License 1.0 (non-commercial) | **⚠ NO** |
| seed-vc DiT, rmvpe, campplus | Seed-VC voice conversion | GPL-3.0 code; weights unclear | ? Probably usable, but voice cloning has consent and legal risk |
| bigvgan_v2 | NVIDIA BigVGAN v2 vocoder | MIT | Yes |
| whisper-small | OpenAI Whisper | MIT | Yes |
| wav2vec / chinese-wav2vec2-base | wav2vec 2.0 variants | Apache-2.0 / MIT (unsure about the Chinese one) | Likely yes |
| pyannote segmentation-3.0, wespeaker | pyannote diarization | MIT (gated download) | Yes |
| raft-things | RAFT optical flow | BSD-3 | Yes |
| dw-ll_ucoco_384, yolox_l | DWPose / YOLOX | Apache-2.0 | Yes |
| u2net | U²-Net (rembg) | Apache-2.0 | Yes |
| bs_roformer ep_317 | BS-RoFormer vocal separator (community) | Unsure | ? Verify |
| detface | Face detector (unsure which one) | Unsure | ? |
| netG_A_latest (scribble) | CycleGAN/pix2pix-style scribble preprocessor | BSD (code); weights unclear | Likely fine (preprocessor only) |

### Restricted models in short
- **Non-commercial (don't sell output without a separate license):** FLUX.2 klein 9B and its derivatives, Depth Anything V2 Large, MatAnyone.
- **Unknown, check before use:** Krea 2 and its fine-tunes/LoRAs, MiniMax H3, VOSR2, 1xSkinContrast, BS-RoFormer, segformer/vitmatte (dataset terms).
- **Not suitable for the business:** the NSFW MiniMax-H3 LoRAs.

## 6. Gaps for the planned job types
- **Photo restoration:** no GFPGAN, CodeFormer, Real-ESRGAN or SUPIR. facerestore_models is empty. These would need to be added before restoration jobs can run (not done; inventory only).
- **Print-on-demand designs:** the only full image models are FLUX.2 klein 9B (non-commercial) and Krea 2 (license unknown). There is no clearly commercial-safe image generator yet. An Apache-licensed option such as FLUX.2 klein 4B or Qwen-Image may be worth adding.
- **AI video:** LTX 2.5 is likely usable commercially at our size. MiniMax H3's terms are unknown. There are no Wan 2.x or Hunyuan weights, despite the folder names.
- **Blender:** 5.1 is installed, but there's no MCP bridge in this session.
- **Disk:** C: has only 19 GB free. Keep caches and outputs on D:.
