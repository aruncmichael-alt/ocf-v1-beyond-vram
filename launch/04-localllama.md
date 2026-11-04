# r/LocalLLaMA draft (ready to paste)

**Subreddit:** r/LocalLLaMA  
**Tone:** candid engineering  
**Title of work:** Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

---

## Title

[Project] Beyond VRAM Capacity — 83.62 GB FlashNext IQ3_S on RTX 5080 16 GB via Strata + OpenCode (OCF V1); includes negative findings

## Body

I wrote up a verified workstation case study (not a vibes benchmark) on running **ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF** (`IQ3_S`, 83.62 GB on disk) on a **16 GB RTX 5080** with **Strata** + **OpenCode**, plus a single-slot FIFO so a cloud IDE can offload bounded coding slices locally.

**Repo:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram  
**PDF:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf  
**Author:** Arun C Michael

### What actually mattered

1. **PLE=`direct` NVMe** — automatic PLE preload ate ~**26.8 GiB** host RAM; pinning `direct` got it back for 128K.
2. **Compaction request hook** — empty OpenCode `variants` still inherited High/Deep; pinning `reasoning: none` + `max_tokens: 4096` cut paired compaction from **69.282 s → 18.360 s (−73.5%)**, tokens **1898 → 575**, **55/55** resume checks.
3. **Single-slot FIFO hardening** — Windows named mutex + PID/start-time locks so live owners never get stolen.
4. **600 s idle unload** → desktop GPU footprint (~612–824 MiB); cold wake **~30.5 s**. MTP acceptance in one active sample ~**73.5%**.

### Negative findings (please read these)

- Zero-reasoning coding screen: **heapq import** once (5/6 no-import compliance) and weak Markdown-fence compliance on one task — not a free lunch just because decode is fast.
- Passive log audit: transient **`0 MiB free VRAM`** warning despite a configured **1,536 MiB** reserve (desktop concurrency matters).
- Production FIFO wave: jobs waited **0 / 7 / 29 / 42 minutes** in queue — single slot is real; the **42-min wait** is the honest cost of serialization when multiple agents want the GPU.

Hashes for the two GGUF shards are in `results/manifest.json`. Fetch weights from HF; don’t ask me for a mirror.

Happy to answer systems questions. Zenodo DOI pending (GitHub→Zenodo webhook path documented in-repo).
