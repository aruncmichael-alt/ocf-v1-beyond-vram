# Hugging Face model community discussion (ready to paste)

**Target:** Community tab on  
https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF  
**Title of work:** Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

---

## Suggested title

Verified IQ3_S shards + PLE=`direct` NVMe on RTX 5080 16 GB (Strata); systems case study by Arun C Michael

## Body

Reporting a verified single-workstation integration of this repo’s **IQ3_S** GGUF shards with Strata + OpenCode (OCF V1) on an NVIDIA RTX 5080 (16 GB).

**Case study:**  
https://github.com/aruncmichael-alt/ocf-v1-beyond-vram  

**PDF (v1.0.0):**  
https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf  

**Author:** Arun C Michael

### Artifact identity (do not redistribute weights from the case-study repo)

- Upstream revision verified: `ed59f92082b1e93c0e96d60a8b11aab089b52f09`
- Shard 1: `54,817,524,224` bytes — SHA-256 `4c1eb2ceb4915e1192f4f386021897bde56a97f40a0bb78bb86465e0f7d2aca3`
- Shard 2: `28,800,138,432` bytes — SHA-256 `316b46f3a2dbd68c900f43136ab9449f9dcc3725dfd8c794847c204bc161e113`
- Combined on-disk weights: **83.62 GB** (decimal)

Always fetch from this HF repo and verify hashes; the case-study package intentionally excludes GGUF binaries.

### Systems finding most relevant to this model

Automatic PLE placement preloaded ~**26.8 GiB** of lookup assets into host RAM. Pinning PLE to **direct NVMe** removed that spike and made 128K single-slot operation practical on a high-RAM host with Strata `0.2.9` / `0.1.55`.

Other measured notes (full ledger in the paper): MTP draft acceptance ~**73.49%** in an active sample; idle unload **600 s** / cold wake ~**30.515 s**; coding-screen and retrieval comparisons vs a dense Ollama IQ3_S baseline are in the PDF.

Happy to clarify measurement conditions — this is a systems/orchestration case study, not a claim of unconditional frontier-API parity.
