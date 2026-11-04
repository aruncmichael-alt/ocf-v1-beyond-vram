# Twelve-Stage Reproduction Protocol

Extracted from the OCF V1 case study by Arun C Michael.

## 7. Twelve-Stage Reproduction Protocol

Engineers replicating this architecture on a compatible 16 GB GPU + high-RAM workstation should execute the following validated sequence:

1. **Verify Upstream Provenance and Checksums:** Confirm the upstream repositories (`Strata` `0.2.9`/`0.1.55`, `OpenCode` `1.19.5`, and `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF` revision `ed59f92082b1e93c0e96d60a8b11aab089b52f09`). Verify that the two GGUF weight shards match SHA-256 hashes `4c1eb2...` and `316b46...`.
2. **Create an Isolated Lab Root (`<LAB_ROOT>`):** Provision dedicated directories for Python `3.12.15`, client binaries, SQLite session state, and configurations so existing `Ollama` installations remain untouched. Ensure sufficient NVMe space for weights (83.62 GB), runtime/MTP assets, logs, and backups.
3. **Stage Active Assets on Local NVMe Storage (`<NVME_DIR>`):** Download official shards with a resumable tool directly onto internal NVMe storage. Reserve external USB HDDs strictly for cold backups.
4. **Configure the Single-Slot Strata Baseline:** Set `slots = 1`, `INT8` KV cache (`32,768` resident window), and explicit `PLE = direct` SSD access. Enable non-destructive preflight checks that return `HTTP 503` if another model holds the GPU or if RAM/commit headroom is insufficient.
5. **Bind Authenticated Loopback API and Run Smoke Tests:** Bind the server to `127.0.0.1:8081` using a local key file (`<LOCAL_API_KEY>`). Verify `/v1/models`, run a single-turn completion, and execute a scoped `OpenCode` read/edit test in a disposable repository.
6. **Record Baseline Telemetry by State:** Log decode speed, prefill time, first-token latency (TTFT), total duration, and memory occupancy separately for cold-start and warm-cached states alongside exact token counts.
7. **Validate 64K Before Enabling 128K Context:** Confirm retrieval and multi-file editing stability at `65,536` tokens before activating the `131,072`-token profile.
8. **Deploy the Pinned No-Thinking Compaction Alias and Checkpoint Guard:** Set the compaction trigger to `81,920` tokens (`114,688` input budget minus `32,768` buffer), disable inherited variants, and pin `reasoning = none` and `max_tokens = 4096` at the final outbound request hook. Enable structural checkpoint validation.
9. **Deploy Atomic FIFO Queue Ownership:** Configure the named mutex, atomic `CreateNew` lock file, and `PID` + process start-time checks. Verify lock contention and dead-owner recovery with a mock executor before running live model jobs.
10. **Verify 600-Second Idle Unloading:** Configure the 600-second idle unload timer. Allow 10 minutes of natural inactivity (without polling inference endpoints), confirm weight release in logs and GPU counters (`~612–824 MiB` residual desktop usage), and time a subsequent cold wake (`~30.5s` reference).
11. **Execute Bounded OCF Coding Jobs:** Have the orchestrator write `.handoff/OCF_<ID>_PROMPT.md` with explicit `Allowed` and `Forbidden` file lists, enqueue via `ocf-enqueue`, prohibit orchestrator edits while queued, and verify `git diff` plus unit tests upon completion.
12. **Export Sanitized Package Artifacts:** Use an explicit allowlist to export sanitized configuration templates and aggregate telemetry, keeping local credentials and proprietary source trees out of version control.

---
---
