# Show HN draft (ready to paste)

**Target:** https://news.ycombinator.com/submit  
**Emphasize:** systems / orchestration, not ML hype  
**Title of work:** Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

---

## Title (≤80 chars preferred)

Show HN: Beyond VRAM Capacity – local coding orchestration on a 16GB GPU

Alternate (closer to canonical paper title; longer):

Show HN: Beyond VRAM Capacity – Strata + OpenCode case study on RTX 5080

## URL

https://github.com/aruncmichael-alt/ocf-v1-beyond-vram

## Text (optional; keep short)

**Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080** (Arun C Michael).

This is a systems write-up, not a model leaderboard. An 83.62 GB on-disk sparse IQ3_S coding model does not fit in 16 GB VRAM; usability came from memory placement, client compaction control, and a hardened single-slot FIFO so a cloud IDE can orchestrate while local OpenCode+Strata do the token-heavy edits.

Concrete, measured pieces:

- PLE pinned to direct NVMe → ~26.8 GiB host RAM not eaten by lookup preload
- OpenCode compaction: empty variants still inherited High/Deep; wire-pinned no-thinking/4K → 69.3s to 18.4s (−73.5%)
- 600s idle unload / ~30.5s cold wake; MTP acceptance ~73.5% in sampled telemetry
- Negative results included (heapq import, 0 MiB free VRAM warning, FIFO waits up to 42 min)

PDF: https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf
