# Upstream OpenCode discussion note (ready to paste)

**Target:** OpenCode upstream discussion / Discord / GitHub Discussion (anomalyco/opencode)  
**Focus:** Wire-verified compaction finding  
**Title of work:** Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

---

## Suggested title

Wire-verified: empty `variants` still inherits High/Deep on compaction — pinning `reasoning: none` + 4K cut 69.3s → 18.4s (−73.5%) on OpenCode 1.19.5

## Body

Sharing a systems finding from a verified workstation case study using **OpenCode 1.19.5** as the local coding client in an OCF V1 single-slot FIFO setup (Strata + FlashNext on RTX 5080 16 GB).

**Paper / package:**  
https://github.com/aruncmichael-alt/ocf-v1-beyond-vram  

**PDF (release v1.0.0):**  
https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf  

**Author:** Arun C Michael

### Compaction inheritance bug / pitfall

Early config defined an empty `variants` map on a compaction alias that pointed at the same model weights. That was **not** enough: compaction calls still inherited the active coding profile’s **High/Deep** reasoning and **16,384** max output tokens.

### Fix (wire-verified)

At the final outbound request hook we pinned:

- `reasoning: none`
- `max_tokens: 4096`

Loopback captures confirmed coding requests still went out with high reasoning / 16K max tokens, while compaction went out with none / 4K.

### Paired-fixture result (OpenCode 1.19.5)

| Metric | Before (inherited High/Deep) | After (pinned none / 4K) |
| --- | ---: | ---: |
| Summary tokens | 1,898 | 575 (−69.7%) |
| Compaction API time | 69.282 s | 18.360 s (−73.5%) |
| Resumed coding checks | — | **55 / 55** pass |

Also useful context from the same study: 128K client budget with an 81,920-token compaction trigger on OpenCode’s internal accounting; structural checkpoint validation before resume.

Happy to answer questions about the request-hook approach vs config-only variants. Full claims ledger and reproduction notes are in the repo.
