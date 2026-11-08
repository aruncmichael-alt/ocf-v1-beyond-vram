# Publish Link & Privacy Audit — 2026-11-08

**Verdict: PASS**

Batch: `OCF_PUBLISH_LINK_AUDIT`. Scope: verify the four tracked-link comment URLs resolve to correct public destinations, and scan all tracked publishable content for private data or secrets. No paper, carousel, or token-report source files were modified. Only this report was written.

## 1. Link destination verification (PASS)

The four required URLs appear verbatim in tracked content (verified via `git grep`, excluding `.handoff/`):

| # | URL | Representative tracked locations | Host HTTP check (seed, 2026-11-08T10:07:32Z) |
|---|-----|----------------------------------|----------------------------------------------|
| 1 | `https://github.com/aruncmichael-alt/ocf-v1-beyond-vram` | `launch/07-linkedin-post.md:23`, `launch/_linkedin_seed.json:27`, `README.md:106`, `CITATION.cff:28`, `CITATION.bib:8`, `.zenodo.json:29` | GitHub HTML: 504 (transient from host); GitHub API repo: 200, public `aruncmichael-alt/ocf-v1-beyond-vram` |
| 2 | `https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf` | `.zenodo.json:39`, `launch/README.md:9`, `launch/01`–`06` discussion files, `README.md:61` (local path ref) | API confirms asset `Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf` present on release `v1.0.0`; direct download hit the same transient 504 |
| 3 | `https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/blob/main/docs/full-token-cost-report-2026-11-08.md` | `launch/07-linkedin-post.md:27`, `launch/_linkedin_seed.json:37`, `launch/build_linkedin_carousel.py:45`, carousel PDF embedded URI action (page link) | 200 (both `token_report_blob` and `token_report_raw`) |
| 4 | `https://doi.org/10.5281/zenodo.23945369` | `launch/07-linkedin-post.md:25`, `launch/_linkedin_seed.json:39`, `README.md:3,107`, `CITATION.bib:9`, `CITATION.cff:30,33,51`, `.zenodo.json:44` | 200 (`doi` and `zenodo_record`) |

Notes:
- The seed's verdict hint: "Links are correct public destinations; GitHub HTML/PDF download had transient 504 from this network but API confirms public repo + PDF asset."
- No DOI strings were invented. Only the concept DOI `10.5281/zenodo.23945369` is asserted anywhere in tracked content; `.zenodo.json` notes explicitly instruct waiting for the Zenodo GitHub-release webhook to mint the v1.2.0 version DOI.
- The carousel PDF embeds URL 3 as a real URI action (`/S /URI /Type /Action /URI`), matching the post.

## 2. Local counterpart existence (PASS)

All local counterparts confirmed present (`Test-Path` = True):

- `docs/full-token-cost-report-2026-11-08.md`
- `release/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf`
- `paper/case-study.md`
- `results/full-ledger-2026-11-08.json`
- `launch/07-linkedin-post.md`
- `docs/publish-safety-audit-2026-11-08.md`

## 3. Privacy / secret scan of tracked publishable content (PASS)

**Scan scope:** all git-tracked files under `docs/`, `paper/`, `results/`, `configs/`, `launch/`, `benchmarks/`, plus root `README.md`, `SECURITY.md`, `CITATION.bib`, `CITATION.cff`, `.zenodo.json`. Excluded: `.git/`, `.handoff/` (working directory, not published). A repo-wide rescan excluding `.handoff/` was also run.

**Forbidden patterns searched (case-insensitive where relevant):**

- Host paths / machine identity: `Administrator`, `AI NANOFAR`, `FlashNext-Experiment`, `C:\Users\`
- Product / job / org identifiers: `POWERBOT`, `SNBOTS`, `SUPERNOVA`, `arunbiopower`, `empower-recruiter`, `NANOFAR`
- Real secrets: `gho_`/`ghs_` GitHub tokens, `sk-` + long token, JWT pairs (`eyJ…​.eyJ`)

**Results: zero real leaks found.**

- Text-file scan (all in-scope tracked files, and repo-wide excluding `.handoff/`): no hits for any forbidden pattern.
- Binary PDFs (`release/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf`, `launch/OCF-V1-LinkedIn-Carousel-3page.pdf`): an initial loose case-insensitive search flagged a substring `EYj` inside the carousel's base85-encoded stream noise. Confirmed false positive: strict secret patterns (`eyJ…​.eyJ`, `gho_`/`ghs_` + long tokens, `sk-` + long tokens) return **0 hits** in the raw bytes of both PDFs, and stream decoding (Flate/ASCII85, ~1.44 MB decoded from the whitepaper) yields **0 hits** in decoded content and text operators.
- Intentional placeholders present and allowed (PASS): `LOCAL_STRATA_API_KEY`, `<LOCAL_API_KEY>`, `<LAB_ROOT>/secrets/` references in configs/docs; job labels `Job-A`…`Job-J` in launch/docs.

## 4. Constraints honored

- Only `docs/publish-link-and-privacy-audit-2026-11-08.md` was created.
- No edits to the paper, launch carousel, or token report.
- No external orchestrators used.
