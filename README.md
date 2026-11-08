# Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23945369.svg)](https://doi.org/10.5281/zenodo.23945369)

**OCF V1 (OpenCode FlashNext)** — Orchestrated local coding with Strata, Qwen3.8-Flash-Next, and OpenCode on a 16 GB RTX 5080

**Author:** Arun C Michael  
**Architecture Status:** Verified Workstation Implementation (November 2026)  
**Stack:** NVIDIA RTX 5080 (16 GB) · Strata (`0.2.9`/`0.1.55`) · `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF` (`IQ3_S`) · OpenCode (`1.19.5`) · Cursor / Cloud IDE Orchestrator

---

## Overview

Can a 16 GB consumer GPU run an 83.62 GB (on-disk quantized weight) sparse coding model (`Qwen3.8-Flash-Next` `IQ3_S`) effectively alongside frontier IDE orchestrators like Cursor, Claude Code, or Windsurf?

**Yes—when memory placement, context compaction, and single-slot concurrency are engineered as a unified system.**

Authored and validated by **Arun C Michael**, this repository provides the architectural whitepaper, configuration templates, and operational verification ledger for **OCF V1 (OpenCode FlashNext)**. Instead of burning cloud tokens on iterative file reads, patch retries, and test loops, the cloud IDE acts strictly as a lightweight **Orchestrator and Verifier**, delegating bounded code synthesis to a local, single-slot FIFO queue backed by **OpenCode** and **Strata**.

---

## What's new in v1.2.0

- **Full all-workspace token economics (3–8 November 2026):** the complete retained OpenCode ledger records **5,290,865 output tokens** (5,090,841 coding + 200,024 compaction) across **224** coding sessions, with **94.79%** cache-read share of the recorded input (`20,537,861` fresh + `373,320,427` cache-read).
- **List-price cloud counterfactual band:** pricing the same recorded footprint at published rates yields **$8.43–$259.48** (Codex GPT-6.1 Sol `$131.32`; Cursor GPT-5.3 Codex `$175.34`, Teams-plus-CTR `$275.13`; Composer 2.5 `$98.16` metered), against a **$0** local API charge; illustrative decode-only electricity ₹54.76–₹98.57 is an assumption, not a wall-meter measurement.
- **Canonical report:** methodology, per-scenario rates, and sanitized artifacts in [`docs/full-token-cost-report-2026-11-08.md`](docs/full-token-cost-report-2026-11-08.md) (`results/full-ledger-2026-11-08.json` / `-summary.csv`). Paper Section 5.7 and claims V-16–V-22 summarize it.
- Meters remain non-additive (OpenCode ledger vs. Strata process vs. timing log); counterfactuals are not invoices, and no DOI is invented until Zenodo mints one.

---

## Core Engineering Highlights

1. **83.62 GB Sparse Model on a 16 GB GPU:** Combines GPU hot-layer/KV residency (`INT8` KV cache, `32,768` resident window), high-RAM host offloading, and `MTP` speculative decoding (`73.49%` draft acceptance) to sustain **54.25–58.84 tokens/s** weighted decode throughput across `131,072`-token context windows.
2. **Direct NVMe `PLE` Placement Saves 26.8 GiB Host RAM:** Pinning Per-Layer Embedding (`PLE`) lookup assets to `direct` NVMe SSD access eliminates an automatic `28.8 GB` decimal (`26.8 GiB`) system RAM preload, preserving host memory headroom for 128K context execution.
3. **Non-Reasoning Client Compaction (-73.5% Latency, -69.7% Tokens):** Prevents `OpenCode` compaction calls from inheriting `High/Deep` reasoning and `16,384`-token output caps. Pinning `reasoning: none` and `max_tokens: 4096` at the final request hook reduced paired-fixture summary tokens from **1,898 to 575** and compaction latency from **69.282 s to 18.360 s** while passing **55 / 55** resumed coding checks.
4. **Hardened Single-Slot FIFO Queue (`OCF V1`):** Coordinates multiple IDE agents across a single GPU inference slot (`slots = 1`) using a Windows named mutex, atomic `CreateNew` lock files, and `PID` + process start-time verification. Live job owners are never stolen regardless of runtime duration.
5. **Deterministic 600s Idle Unloading:** Automatically releases GPU and host model allocations after 10 minutes of inactivity down to normal desktop GPU usage (`612–824 MiB`), waking seamlessly on the next inference call in **30.515 seconds**.

---

## Summary of Verified Workstation Results

### 1. Algorithmic Coding & 60K Retrieval Screen (64K Context, Temp 0)
| Metric | Dense Baseline (`Ollama` 26.9B `IQ3_S`) | Sparse Candidate (`Strata` `FlashNext` `IQ3_S` + `MTP`) |
| :--- | ---: | ---: |
| **Algorithm tasks passed** | 5 / 6 | **6 / 6** |
| **Deterministic executable test cases** | 504 / 505 | **505 / 505** |
| **Exact-output / tool verification checks** | 3 / 3 | **3 / 3** |
| **Decode throughput (coding answers)** | ~58 tokens/s | **70.6 – 89.9 tokens/s** |
| **60,071-token retrieval first-token latency** | 33.735 s | **29.890 s** |
| **60,071-token retrieval total duration** | 34.192 s | **30.479 s** |

### 2. Multi-Job Orchestrator Offload Wave
Across 5 bounded production tasks (4 serialized FIFO jobs + 1 direct execution), the local `OCF V1` stack processed **~772,000–773,000 local tokens** (with `98.09%` multi-turn prompt prefix reuse), restricting cloud orchestrator usage to **~50,000 tokens** (specification + diff/test verification).

---

## PDF Whitepaper

A formatted PDF build is published at [`release/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf`](release/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf).

## Repository Structure

```text
.
├── README.md                        # Executive overview and quick-start orientation
├── CITATION.cff / CITATION.bib      # Citation metadata (Zenodo DOI)
├── .zenodo.json                     # Zenodo GitHub-release archival metadata
├── paper/
│   └── case-study.md                # Full technical paper by Arun C Michael
├── docs/
│   ├── architecture.md              # Memory hierarchy, OCF V1 state machine, and lock protocol
│   ├── reproduction.md              # 12-stage practical reproduction guide
│   ├── limitations.md               # Scope conditions, queue wait trade-offs, and VRAM notes
│   └── zenodo-setup.md              # Operator checklist to mint a Zenodo DOI
├── launch/                          # Ready-to-paste community posts (do not Day-1 spray)
├── configs/
│   ├── strata.example.json          # Sanitized Strata 128K profile template
│   └── opencode.example.json        # Sanitized OpenCode 1.19.5 & compaction budget template
├── scripts/                         # Sanitized PowerShell FIFO queue & preflight helpers
├── benchmarks/
│   └── synthetic/                   # Non-proprietary retrieval, coding, and compaction fixtures
├── results/
│   ├── aggregate.csv                # Verified timing and throughput summaries
│   └── manifest.json                # Cryptographic SHA-256 artifact hashes and run metadata
├── SECURITY.md                      # Loopback binding, credential isolation, and redaction policy
├── THIRD_PARTY_NOTICES.md           # Upstream attribution for Strata, OpenCode, and ISTA-DASLab
└── .gitignore                       # Excludes .env, secrets, SQLite DBs, logs, and GGUF weights
```

---

## Citation

If you use the **OCF V1** orchestration architecture, compaction budgeting method, or empirical findings in your engineering work or research, please cite:

```bibtex
@techreport{michael2026beyondvram,
  author      = {Michael, Arun C},
  title       = {Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080},
  institution = {Independent Systems Engineering Case Study},
  year        = {2026},
  month       = {November},
  note        = {Verified workstation implementation of OCF V1 (OpenCode FlashNext) on NVIDIA RTX 5080 16 GB},
  url         = {https://github.com/aruncmichael-alt/ocf-v1-beyond-vram},
  doi         = {10.5281/zenodo.23945369}
}
```

Also see [`CITATION.cff`](CITATION.cff), [`CITATION.bib`](CITATION.bib), and [`docs/zenodo-setup.md`](docs/zenodo-setup.md) for the Zenodo DOI path.

---
---
