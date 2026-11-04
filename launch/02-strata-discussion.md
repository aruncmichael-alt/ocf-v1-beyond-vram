# Upstream Strata discussion note (ready to paste)

**Target:** Strata upstream discussion / issues / Discord (Niko1221/Strata)  
**Focus:** PLE direct NVMe, idle unload, MTP acceptance, 128K single-slot  
**Title of work:** Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

---

## Suggested title

PLE=`direct` NVMe saved ~26.8 GiB host RAM; 128K single-slot + 600s idle unload / ~30.5s cold wake on Strata 0.2.9 (RTX 5080)

## Body

Publishing verified workstation measurements from integrating **Strata Terminal 0.2.9 / Control 0.1.55** (`CUDA 13`, `sm120`) with OpenCode in a single-slot OCF V1 queue on an RTX 5080 (16 GB).

**Repo:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram  
**PDF:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf  
**Author:** Arun C Michael

### PLE placement

Under automatic PLE placement, startup preloaded lookup tables into host DRAM — an additional **28.8 GB decimal (~26.8 GiB)** RAM spike. Pinning PLE to **`direct` NVMe** eliminated that preload and made host memory use deterministic across restarts. Goal was RAM headroom for 128K, not an SSD-vs-RAM speed claim (relative lookup speed was out of scope).

### 128K / single slot

- Context: **131,072** tokens, **`slots = 1`**
- KV: **INT8**, resident window **32,768**
- Model: `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF` `IQ3_S` (83.62 GB on-disk shards; hashes in repo `results/manifest.json`)

### Idle unload / cold wake

- Idle unload configured to **600 s**
- Observed unload interval ~616 s (threshold + teardown/log flush)
- Post-unload system GPU usage down to **824 MiB** then **612 MiB** (desktop/driver, not resident LM)
- Cold wake: **30.515 s**

### MTP

Active sample telemetry: weighted decode **54.25 tok/s** (48 requests) with **~73.49%** MTP draft acceptance and **98.09%** prompt-prefix reuse in that cohort.

Upstream hybrid placement / idle unload / MTP did the heavy lifting; OCF V1 is the orchestration + measurement layer around a single GPU slot. Feedback welcome on whether documenting `direct` PLE as the default recommendation for high-RAM 128K profiles would help other adopters.
