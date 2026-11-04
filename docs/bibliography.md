1. **Strata Hybrid Inference Runtime**
   * **Primary Repository:** `https://github.com/Niko1221/Strata`
   * **Verified Releases Used:** Terminal `0.2.9` / Control `0.1.55` (`CUDA 13`, `sm120` build).
   * **Verification Date:** 3–4 November 2026 (IST).
   * **Technical Role:** Provides hybrid GPU/DRAM/NVMe model execution, `INT8` resident KV window management, `PLE` direct storage access, `MTP` speculative decoding, loopback OpenAI-compatible API serving, and 600-second automatic idle unloading.

2. **ISTA-DASLab Quantized Sparse Model Artifacts**
   * **Primary Repository:** `https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF`
   * **Verified Commit Revision:** `ed59f92082b1e93c0e96d60a8b11aab089b52f09`
   * **Verified Shards:**
     * Shard 1 (`54,817,524,224` bytes) — SHA-256: `4c1eb2ceb4915e1192f4f386021897bde56a97f40a0bb78bb86465e0f7d2aca3`
     * Shard 2 (`28,800,138,432` bytes) — SHA-256: `316b46f3a2dbd68c900f43136ab9449f9dcc3725dfd8c794847c204bc161e113`
   * **Verification Date:** 3–4 November 2026 (IST).
   * **Technical Role:** Supplies the `IQ3_S` quantized sparse model weights (`83.62 GB` combined across two GGUF shards) and associated `MTP` draft assets served under the alias `qwen3.8-flash-next-iq3_s`.

3. **OpenCode Autonomous Coding Client**
   * **Primary Repository:** `https://github.com/anomalyco/opencode`
   * **Verified Release Used:** `1.19.5` (paired with portable Python `3.12.15`).
   * **Verification Date:** 3–4 November 2026 (IST).
   * **Technical Role:** Executes bounded repository read/edit tool loops, manages session token accounting, filters historical summary pairs, and triggers context compaction at the configured `81,920`-token bound.

4. **OCF V1 Integration and Workstation Telemetry**
   * **Author:** Arun C Michael
   * **Verification Window:** 3–4 November 2026 (IST).
   * **Technical Role:** Primary empirical record encompassing the `OCF V1` FIFO orchestration runners, atomic mutex + `PID`/start-time lock manager, wire-verified compaction request hook, 6-task (`505`-case) coding screen, 64K/128K long-context fixtures (`108` checks), paired compaction benchmark (`55` checks), and engine telemetry snapshots (`585`, `890`, and `48` request cohorts).

---
---
