# LinkedIn post

5.29M tokens. $0 local API. Same mix lists ~$98-$259 on cloud.

Across the Nov 3-8 snapshot, the retained OpenCode ledger recorded 5,290,865 output tokens - 5,090,841 coding plus 200,024 compaction - across 224 coding sessions on one workstation.

The case study ran an 83.6 GB model with 16 GB of GPU memory, using host RAM and NVMe offload. This describes one measured workstation configuration, not a general hardware guarantee.

The cloud figures price the same recorded token mix at listed rates: Composer $98.16, Sol $131.32, Cursor GPT-5.3 Codex $175.34, and Grok $259.48. The ~$98-$259 band is a same-footprint list-rate counterfactual, not a measured invoice or quality comparison. The $0 figure is the local API charge in this ledger; electricity and other workstation operating costs are not included.

Cache reads covered 94.79% of recorded input. v1.2.0 is the economics continuation; the v1.0.x paper releases remain. Swipe the carousel, then read the whitepaper (Section 5.7) and the full token report, linked below.

**Snapshot figures**

- 5,290,865 output tokens (5,090,841 coding + 200,024 compaction)
- 224 coding sessions
- 94.79% cache-read share of recorded input
- $0 local API charge
- ~$98-$259 same-footprint cloud list-rate counterfactual (Composer-Grok comparison set)

**Links**

- Repository: https://github.com/aruncmichael-alt/ocf-v1-beyond-vram
- v1.2.0 economics release: https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/tag/v1.2.0
- DOI: https://doi.org/10.5281/zenodo.23945369
- Zenodo concept record: https://zenodo.org/records/23945369
- Full token report: https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/blob/main/docs/full-token-cost-report-2026-11-08.md
- Paper, Section 5.7: https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/blob/main/paper/case-study.md

#LocalAI #OpenSource #Inference #LLM #AIEngineering
