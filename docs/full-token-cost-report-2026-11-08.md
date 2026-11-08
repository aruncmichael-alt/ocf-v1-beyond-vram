# Full Token and Cost Report: Strata/OpenCode

**Snapshot:** 2026-11-08 10:57:12 IST (UTC+05:30)  
**Observation window:** 2026-11-03 01:01:44 through 2026-11-08 10:57:12 IST  
**Scope:** Complete retained all-workspace OpenCode ledger at the snapshot, plus separately reported Strata process and timing-log views.  
**Release target:** Zenodo v1.2.0

## 1. Snapshot, scope, and method

This note reports the full retained ledger rather than the earlier 29-run result-file subset. OpenCode totals are the headline economics measure. The Strata current-process counters and retained timing log are separate observations; neither is an additional quantity to add to the OpenCode totals or to each other.

The snapshot was assembled read-only from the Strata metrics API, OpenCode SQLite opened in read-only mode, the retained Strata timing log, installed receipts, and queue status. The supplied JSON and CSV retain the resulting measurements and summary. The reported cache share is cache-read tokens divided by fresh-input plus cache-read tokens. Cloud scenarios apply the seed's per-million input, cache-read, and output rates to the recorded OpenCode token mix; they are counterfactuals, not measured cloud usage.

Artifacts: [full ledger JSON](../results/full-ledger-2026-11-08.json) and [summary CSV](../results/full-ledger-2026-11-08-summary.csv).

## 2. Executive result

The finalized OpenCode ledger records **5,290,865 output tokens**: **5,090,841 coding** and **200,024 compaction**. It also records **20,537,861 fresh-input tokens** and **373,320,427 cache-read tokens** across **224 coding sessions**. Cache reads were **94.79%** of fresh plus cached input.

At the seed's listed rates, the five base cloud scenarios range from **$8.43 to $259.48** for this recorded token footprint. The Cursor GPT-5.3 Codex Teams-plus-CTR case is **$275.13**, including a **$99.79** CTR add-on and excluding subscription charges. These are token-price counterfactuals; cloud models can tokenize, reason, call tools, and complete work differently. They do not establish quality parity or equivalent work.

The local API charge is **$0**. Illustrative decode-only electricity is **₹54.76–₹98.57**, based on assumed wall power and tariff inputs rather than a wall-meter reading.

## 3. Latest active configuration

Values below are transcribed from `config_public` in the seed. The API address shown is loopback-only. Host memory is described as a high-RAM host; this report does not publish its absolute capacity.

| Setting | Snapshot value |
|---|---|
| Runtime | Strata engine 0.1.55 |
| Model | qwen3.8-flash-next-iq3_s |
| API | `http://127.0.0.1:8081/v1` (loopback only) |
| GPU | NVIDIA RTX 5080; 16,303 MiB reported VRAM |
| Context | 131,072 tokens |
| Coding output ceiling | 16,384 tokens |
| Coding reasoning | high |
| OCF write variant | deep |
| Compaction | flashnext-compaction; no thinking; 4,096-token output cap; trigger at 81,920 tokens |
| Inference slots | 1 |
| KV cache | int8; 32,768-token resident window |
| Expert cache | 3,613 slots; 7,072 MiB primary allocation |
| Host arena | 47,962 MiB |
| Pool workers | 7 |
| Prefill cap | 8,192 tokens |
| MTP | spec=6, mtp_max=4, lookup=3 |
| Idle unload | 600 seconds |
| Cold wake | 30.515 seconds |
| Memory guard | 65 GiB RAM and 70 GiB commit thresholds; receipt dated 2026-11-05 |
| Host memory class | high-RAM host |

## 4. OpenCode token-generation ledger

| Measure | Coding | Compaction | Combined |
|---|---:|---:|---:|
| Sessions counted in category | 224 | 79 | Not summed |
| Assistant steps | 8,542 | 116 | 8,658 |
| Fresh input tokens | 17,500,678 | 3,037,183 | 20,537,861 |
| Cache-read tokens | 373,320,427 | 0 | 373,320,427 |
| Output tokens | 5,090,841 | 200,024 | 5,290,865 |

Compaction is **3.78%** of combined OpenCode output. Sessions are category-specific counts from the seed and are not presented as a deduplicated total. Total recorded input is 393,858,288 tokens; cache-read share is 373,320,427 ÷ 393,858,288 = **94.79%**.

## 5. Current Strata process — non-additive view

This process began on 2026-11-06 and is a separate Strata counter snapshot. **Do not add these values to the OpenCode ledger or retained timing log.**

| Measure | Value |
|---|---:|
| Process start | 2026-11-06 08:18:55 IST |
| Completed requests | 4,575 |
| Fresh input | 9,282,990 tokens |
| Cached input | 192,807,626 tokens |
| Total input including cache | 202,090,616 tokens |
| Output | 2,510,522 tokens |
| Decode time | 45,831.455 seconds |
| Weighted decode throughput | 54.78 tok/s |
| Cache-read share | 95.41% |

## 6. Retained Strata timing log — non-additive view

This retained engine log is another measurement view, not an extension to sum onto the OpenCode ledger or current process.

| Measure | Value |
|---|---:|
| Completed records | 9,032 |
| Output | 5,377,055 tokens |
| Fresh input | 21,697,444 tokens |
| Cached input | 376,113,421 tokens |
| Decode time | 98,565.983 seconds (27.38 hours) |
| Weighted output throughput | 54.55 tok/s |
| Median request throughput | 55.7 tok/s |
| Request throughput range | 2.3–94.1 tok/s |

## 7. Largest retained OCF jobs (anonymized)

The job labels below are anonymized. “Work” and “compaction” are kept separate, and the total is their sum.

| Job | Work output tokens | Compaction tokens | Total output tokens |
|---|---:|---:|---:|
| Job-A | 102,163 | 63,913 | 166,076 |
| Job-B | 43,684 | 110,975 | 154,659 |
| Job-C | 33,637 | 91,684 | 125,321 |
| Job-D | 90,433 | 3,242 | 93,675 |
| Job-E | 80,348 | 10,729 | 91,077 |
| Job-F | 74,228 | 4,747 | 78,975 |
| Job-G | 74,200 | 3,966 | 78,166 |
| Job-H | 67,077 | 5,491 | 72,568 |
| Job-I | 62,384 | 9,017 | 71,401 |
| Job-J | 67,650 | 1,285 | 68,935 |

## 8. Cloud cost comparison

Each scenario prices the same recorded OpenCode quantities: 20.537861 million fresh-input tokens, 373.320427 million cache-read tokens, and 5.290865 million output tokens. Rates are USD per million tokens. Totals preserve the exact assumptions in the seed; they do not project how a cloud model would actually consume tokens.

| Scenario | Fresh input rate | Cache-read rate | Output rate | USD per 1M OpenCode output | USD per 1M combined recorded tokens | Modeled total |
|---|---:|---:|---:|---:|---:|---:|
| Codex GPT-6.1 Sol standard | $2.00 | $0.10 | $10.00 | $24.82 | $0.3290 | **$131.32** |
| Codex GPT-6 Luna standard | $0.10 | $0.01 | $0.50 | $1.59 | $0.0211 | **$8.43** |
| Cursor GPT-5.3 Codex | $1.75 | $0.175 | $14.00 | $33.14 | $0.4393 | **$175.34** |
| Cursor Composer 2.5 | $0.50 | $0.20 | $2.50 | $18.55 | $0.2459 | **$98.16** |
| Cursor Grok 4.7 | $2.00 | $0.50 | $6.00 | $49.04 | $0.6501 | **$259.48** |

**Cursor plan treatment.** GPT-5.3 Codex is a third-party model; the **$175.34** figure is its metered token-price scenario before subscription charges or plan credits. The seed's Teams-plus-CTR case adds **$99.79**, for **$275.13** before subscription charges. Cursor's [CTR documentation](https://prod.cursor.com/help/models-and-usage/token-rate) lists a rate of $0.25 per million eligible input, output, and cached tokens for Teams and Enterprise; applied to the seed's modeled footprint, that rounds to the stated add-on. CTR applicability depends on plan and eligible usage. Composer 2.5's $98.16 is a metered value; the seed notes a weekly pool may cover some or all of it. Actual plan spend depends on plan, pool use, and usage eligibility. Grok 4.7 is also a Cursor model; its listed metered value may not equal a user's incremental cash charge when included usage applies.

Pricing references supplied with the seed:

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [Cursor models and pricing](https://cursor.com/docs/models-and-pricing)
- [Cursor GPT-5.3 Codex model pricing](https://prod.cursor.com/docs/models/gpt-5-3-codex)
- [Cursor Token Rate (CTR)](https://prod.cursor.com/help/models-and-usage/token-rate)

Provider pricing and plan terms can change. The numeric report values remain those in the dated seed, and the linked pages serve as pricing references rather than a guarantee of a future invoice.

## 9. Local Strata cost

| Component | Value | Basis |
|---|---:|---|
| Local API | **$0** | Local loopback API; no cloud API charge in this ledger |
| Decode duration | 27.38 hours | Retained timing-log value; non-additive measurement |
| Assumed wall power | 250–450 W | Illustrative assumption, not a wall-meter observation |
| Assumed electricity tariff | ₹8/kWh | Seed assumption |
| Illustrative energy | 6.84–12.32 kWh | Decode-duration estimate |
| Illustrative electricity | **₹54.76–₹98.57** | Decode-only estimate |
| Illustrative electricity per million retained output tokens | ₹10.18–₹18.33 | Uses 5,377,055 retained-log output tokens |

The electricity estimate excludes prefill, idle time, tools, orchestration, and depreciation. It is not a complete ownership-cost estimate.

## 10. Interpretation and limits

1. **Keep the three measurement views separate.** Do not sum the OpenCode ledger, current-process counters, or retained timing-log values; the seed explicitly marks them non-additive.
2. **Cloud rows are same-footprint arithmetic only.** They apply listed rates to the local recorded token counts and do not establish quality parity, identical tokenization, or equivalent cloud execution paths.
3. **Output is not accepted code.** Generated output includes reasoning, tool activity, failures, and compaction, not just code retained by a project.
4. **Some orchestration usage is outside the meters.** Cursor/Codex preparation and review tokens are not included in Strata's counters.
5. **The snapshot is time-bounded.** In-flight queue work may settle after 2026-11-08 10:57:12 IST.
6. **Plan values are not guaranteed invoices.** Subscription charges, included usage pools, CTR eligibility, and weekly pool consumption can change the incremental bill; the seeded Composer value may be covered by a pool.
7. **Electricity is illustrative and incomplete.** It uses assumed wall power and tariff for decode time only, omitting prefill, idle, tools, orchestration, and depreciation; the $0 local API figure does not mean the workstation has no operating cost.

## 11. Reproduction concept

A read-only audit can be performed with a local script at `<LAB_ROOT>/audit_live.py`. It should read Strata metrics through the loopback API, open the OpenCode SQLite database in read-only mode, parse the retained Strata timing log and installed receipts, inspect queue status, then emit a sanitized JSON ledger and CSV summary. The script concept requires no published host paths or credential values; the inference API reference remains loopback-only. The checks for this report confirmed the headline sums, input splits, cache share, job totals, and JSON-to-CSV summary values.
