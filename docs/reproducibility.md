### 5.1 Pre-Flight Reproducibility Checklist

- [x] **1. Artifact Integrity Verified:** Confirmed `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF` revision `ed59f92082b1e93c0e96d60a8b11aab089b52f09` and matched SHA-256 checksums for Shard 1 (`4c1eb2...`) and Shard 2 (`316b46...`).
- [x] **2. Hardware Envelope Verified:** Confirmed NVIDIA RTX 5080 (16 GB / 16,303 MiB), internal NVMe SSD (`<NVME_DIR>`), and high-RAM host system (`96 GiB DDR4` reference envelope).
- [x] **3. Isolated Environment Provisioned:** Deployed portable Python `3.12.15`, `Strata` `0.2.9`/`0.1.55`, and `OpenCode` `1.19.5` under `<LAB_ROOT>` without altering existing `Ollama` installations.
- [x] **4. Direct NVMe Lookup Pinned:** Configured `PLE` to `direct` SSD mode on `<NVME_DIR>`, preventing the 26.8 GiB host-RAM preload spike.
- [x] **5. Loopback Authentication Enforced:** Bound API strictly to `127.0.0.1:8081` with `<LOCAL_API_KEY>` loaded from an untracked secret file.
- [x] **6. Compaction Hook Wire-Tested:** Verified `81,920`-token compaction trigger (`114,688 - 32,768`), disabled inherited variants, and confirmed `reasoning: none` + `max_tokens: 4096` on the wire alongside structural checkpoint validation.
- [x] **7. Atomic FIFO Lock Validated:** Confirmed Windows named mutex, `CreateNew` lock file creation, and `PID` + process start-time checks across concurrent worker processes.
- [x] **8. 600s Idle Unload Verified:** Confirmed automatic weight release after 600 seconds of inactivity and verified `~30.5s` cold wake on subsequent inference.

---

### 5.2 Verified Public Manifest Schema (`results/manifest.json`)

```json
{
  "author": "Arun C Michael",
  "experiment_id": "ocf-v1-rtx5080-runtime-snapshot-01",
  "evidence_type": "verified_workstation_observation",
  "observation_window_ist": "2026-11-03 to 2026-11-04",
  "gpu_class": "NVIDIA RTX 5080 16 GB (16303 MiB reported)",
  "engine": "Strata 0.2.9 / 0.1.55 (CUDA 13, sm120)",
  "client": "OpenCode 1.19.5",
  "model_repository": "ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF",
  "model_revision": "ed59f92082b1e93c0e96d60a8b11aab089b52f09",
  "local_model_alias": "strata/qwen3.8-flash-next-iq3_s",
  "gguf_shards": [
    {
      "shard": 1,
      "size_bytes": 54817524224,
      "sha256": "4c1eb2ceb4915e1192f4f386021897bde56a97f40a0bb78bb86465e0f7d2aca3"
    },
    {
      "shard": 2,
      "size_bytes": 28800138432,
      "sha256": "316b46f3a2dbd68c900f43136ab9449f9dcc3725dfd8c794847c204bc161e113"
    }
  ],
  "context_limit_tokens": 131072,
  "inference_slots": 1,
  "kv_cache_type": "INT8",
  "kv_resident_window_tokens": 32768,
  "ple_placement": "direct_nvme",
  "idle_unload_seconds": 600,
  "cold_wake_seconds": 30.515,
  "active_sample_metrics": {
    "completed_requests": 48,
    "output_tokens": 27707,
    "decode_seconds": 510.7722,
    "prefill_seconds": 86.43,
    "prompt_token_reuse_ratio": 0.9809,
    "mtp_draft_acceptance_ratio": 0.7349,
    "weighted_decode_tokens_per_second": 54.25,
    "excludes": ["queue_wait", "tools", "cold_load", "prefill"]
  }
}
```

---

### 5.3 Verified OCF Job Specification Template (`.handoff/OCF_<JOB_ID>_PROMPT.md`)

```markdown
# OCF Job Specification: <JOB_ID>

## Goal
Implement the bounded feature or defect fix specified below within the Allowed files.

## Variant
deep

## Allowed Files (Read/Write Permitted)
- `<REPO_ROOT>/src/module/target_implementation.ts`
- `<REPO_ROOT>/tests/module/target_implementation.test.ts`

## Forbidden Files (Strictly Read-Only / Do Not Touch)
- All files outside the Allowed list above
- `<REPO_ROOT>/package.json`
- Deployment scripts, CI workflows, and `.env` configurations

## Host Verification Command
`npm test -- tests/module/target_implementation.test.ts`

## Execution & Orchestrator Rules (STOP)
- Stop immediately once the Allowed files satisfy the Goal.
- Do not execute deployment commands or git commits from inside the local agent.
- Orchestrator Lock Rule: Cursor / cloud orchestrators must NOT edit Allowed files while this job is `queued` or `running`.
```

---

### 5.4 Sanitized Configuration Reference Schemas (`configs/`)

```json
// configs/strata.example.json — Parameterized 128K Single-Slot Profile
{
  "server": {
    "host": "127.0.0.1",
    "port": 8081,
    "api_key_file": "<LAB_ROOT>/secrets/local_api_key.txt",
    "idle_unload_seconds": 600
  },
  "model": {
    "alias": "qwen3.8-flash-next-iq3_s",
    "shards": [
      "<MODEL_DIR>/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf",
      "<MODEL_DIR>/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00002-of-00002.gguf"
    ],
    "vision": false,
    "mtp": {
      "enabled": true,
      "speculative_count": 4
    },
    "ple": {
      "placement": "direct",
      "storage_path": "<NVME_DIR>/ple_assets"
    }
  },
  "runtime": {
    "slots": 1,
    "context_length": 131072,
    "kv_cache": {
      "type": "INT8",
      "resident_window": 32768
    },
    "vram_reserve_mib": 1536,
    "preflight_guards": {
      "min_free_vram_mib": 14000,
      "min_available_ram_gib": 75,
      "min_commit_headroom_gib": 85,
      "refuse_if_ollama_loaded": true
    }
  }
}
```

```json
// configs/opencode.example.json — Parameterized Client & Compaction Budget
{
  "provider": {
    "name": "strata",
    "base_url": "http://127.0.0.1:8081/v1",
    "api_key_env": "LOCAL_STRATA_API_KEY"
  },
  "models": {
    "coding": {
      "id": "strata/qwen3.8-flash-next-iq3_s",
      "context_window": 131072,
      "input_budget": 114688,
      "max_output_tokens": 16384,
      "reasoning": "high"
    },
    "compaction": {
      "id": "strata/qwen3.8-flash-next-iq3_s",
      "trigger_tokens": 81920,
      "compaction_buffer_tokens": 32768,
      "inherit_variants": false,
      "request_hook_override": {
        "reasoning": "none",
        "max_output_tokens": 4096
      },
      "checkpoint_validator": {
        "required_ordered_sections": [
          "Goals",
          "Constraints",
          "Completed Work",
          "Current State",
          "Next Steps"
        ],
        "forbid_duplicate_headings": true,
        "require_balanced_fences": true,
        "require_end_marker": true,
        "require_stop_finish_reason": true
      }
    }
  }
}
```

---
---
