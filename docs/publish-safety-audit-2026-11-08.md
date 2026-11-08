# Publish Safety Audit — 2026-11-08

## Decision

**PASS (live-confirmed).** A host re-audit on 2026-11-08 (~12:15 IST) reproduced the clean result against the current live public sources — fresh shallow clone of public main, recursive credential/identifier scan with no hits, placeholder-only `api_key` references, Zenodo record HTML with no obvious private-data leak, and all five releases intact. This upgrades the earlier seed-backed pass with a freshness caveat to a live-confirmed pass; details are in the Live re-audit section below.

Residual honesty is unchanged: this is still a point-in-time check. If the published tree, a release, or the Zenodo record changes after this re-audit, this note does not cover those changes, and the fresh-clone scan should be repeated before any later publication date.

## Scope and method

- **GitHub scope in the supplied seed:** public repository main, identified as the v1.2.0 economics package.
- **Zenodo scope in the supplied seed:** public concept record 10.5281/zenodo.23945369, including a check of its public HTML for obvious private-data exposure.
- **Snapshot timestamp:** 2026-11-08 06:24:56.5577602 UTC, as recorded in launch/_linkedin_seed.json.
- **Repeatable method:** start from a fresh clone of public main, record the resolved commit and release, then perform a read-only scan of the published tree for credential-like values, host-specific absolute paths, and disallowed project or job identifiers. Separately inspect the public Zenodo concept-record page and its public metadata. Do not modify or delete any published record or release.
- **Reproduction status:** the original run could not reach GitHub or Zenodo and was seed-backed. The 2026-11-08 (~12:15 IST) re-audit completed the fresh shallow clone of public main and retrieved the public Zenodo record page successfully; the blocked-retrieval caveat no longer applies. Findings below combine the seed with the live re-audit, and the older local checkout was never substituted for a fresh clone.

## Findings recorded in the seed

1. **Credentials — PASS.** No real API keys, session tokens, or JWT credentials were reported in the published tree. The only key-shaped matches were explicit placeholders and a documented environment-variable name; neither is a usable secret.
2. **Host paths — PASS.** The seed reports no host-specific absolute paths in the published tree.
3. **Project and job identifiers — PASS.** The seed reports no disallowed product or job names. Workload references use generic anonymized labels.
4. **Zenodo page — PASS with scope limit.** The seed reports no obvious private-data leak in the public HTML of concept DOI 10.5281/zenodo.23945369. This is an HTML-level observation, not a claim that every linked file or future record version was re-audited in this run.
5. **Release preservation — PASS.** The seed records v1.0.0, v1.0.1, v1.0.2, v1.1.0, and v1.2.0 as intact. No release or record was changed or deleted for this work.
6. **Identifier note.** The seed notes a neighboring concept DOI, 10.5281/zenodo.23945368. The launch assets use only the requested concept DOI, 10.5281/zenodo.23945369; no new DOI is asserted.

## Live re-audit — 2026-11-08, host-verified

The following was verified directly against the live public sources on 2026-11-08 (~12:15 IST) and confirms seed findings 1–5:

- Fresh shallow clone of the public main branch: success.
- Recursive scan of the cloned tree for credential-like values and for disallowed host, project, and job identifiers: no hits.
- Configuration `api_key` references are placeholders only (environment-variable name; `<LAB_ROOT>/secrets/local_api_key.txt`; `<LOCAL_API_KEY>`).
- Public Zenodo record page HTML: no obvious private-data leak.
- Releases v1.0.0, v1.0.1, v1.0.2, v1.1.0, and v1.2.0 all present and intact.

## Intentional public disclosures

- The API address 127.0.0.1:8081 is documented as loopback-only. It is an intentional configuration disclosure, not a public network endpoint.
- The single-workstation hardware envelope, including the RTX 5080, 16 GB VRAM, and high-RAM thresholds, is intentional case-study data.
- The $0 figure means no local API charge in the measured ledger. It does not mean the workstation has zero electricity, hardware, or operating cost.
- Cloud amounts are same-footprint list-rate counterfactuals. They are not invoices, measured cloud usage, or claims of equal output quality. Separate OpenCode, live-process, and retained-log meters are non-additive and must not be summed.

## Residual notes and release guidance

- The 2026-11-08 re-audit inspected the live GitHub tree and Zenodo record page directly; the earlier blocked-retrieval caveat is superseded. Both checks are still point-in-time: before relying on this note for a later publication date, repeat the fresh-clone and record-page checks against the then-current public sources.
- The audit seed and the live re-audit are both dated 2026-11-08. Neither establishes that the public tree or record remained unchanged after those timestamps.
- Keep the carousel and post scoped to the supplied figures and qualifiers. Do not expose private filesystem paths or credentials.
- The seed reports that v1.2.0 is the economics continuation and that v1.0.x paper releases remain intact.

