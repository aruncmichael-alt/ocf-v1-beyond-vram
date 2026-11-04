# Grok handover — remaining publish steps (Zenodo DOI)

**Cold-start handoff.** Git publish is done. Your job is to mint the real Zenodo DOI and wire it into citation surfaces. Do **not** invent a DOI. Do **not** post to Reddit / HN / Day-1 spray.

---

## Status

| Track | State |
| :--- | :--- |
| **GIT** | **DONE** — public repo, `main` pushed, release **v1.0.0** live with PDF asset |
| **DOI** | **NOT DONE** — Zenodo↔GitHub webhook not yet enabled; placeholders remain |

---

## Canonical metadata (exact — do not rewrite)

- **Title:** `Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080`
- **Author:** Arun C Michael
- **Publisher account:** personal GitHub `aruncmichael-alt` only (never company `arunbiopower`)

---

## Key links

| Item | URL |
| :--- | :--- |
| Repo | https://github.com/aruncmichael-alt/ocf-v1-beyond-vram |
| Release v1.0.0 | https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/tag/v1.0.0 |
| PDF (v1.0.0 asset) | https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf |
| Latest title-align / Zenodo-prep commit | https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/commit/369e5bed60038591f84e094b36e258d35e53b2b4 (`Add Zenodo metadata, citation DOI placeholders, and launch drafts.` — aligns README/citation surfaces to the canonical title and documents the webhook DOI path) |
| Prior publish commit | https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/commit/67abba1ab2a08c18e3d9a0788882c22e811306b7 |
| Operator Zenodo checklist (already in repo) | https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/blob/main/docs/zenodo-setup.md |
| This handover (raw) | https://raw.githubusercontent.com/aruncmichael-alt/ocf-v1-beyond-vram/main/docs/GROK_HANDOVER_REMAINING_PUBLISH.md |

Local clone (if working on disk): `C:\Users\Administrator\Documents\ocf-v1-beyond-vram`  
Origin: `https://github.com/aruncmichael-alt/ocf-v1-beyond-vram.git`

---

## Account / safety rules (hard)

1. Operate as **`aruncmichael-alt`** for all GitHub + Zenodo-GitHub actions on this repo.
2. **Never** make company account **`arunbiopower`** the publisher, owner, or release author for this work.
3. After finishing, restore default: `gh auth switch --user arunbiopower`.
4. **No** global `git config` changes (`git config --global …`).
5. **No** force-push. **No** `--no-verify` unless Arun explicitly asks.
6. **No** secrets in commits (tokens, `.env`, Zenodo PAT, etc.).
7. **No** GGUF / model-weight upload or redistribution — point users at upstream Hugging Face and `results/manifest.json` digests only.
8. **Do not mint a fake DOI.** Wait for Zenodo’s real `10.5281/zenodo.…` after the webhook archives **v1.0.1**.
9. **Do not** post to Reddit, Hacker News, or spray `launch/` drafts on Day 1 as part of this DOI task.

Commit authorship for DOI follow-up commits (local `-c` only, not global):

```bash
git -c user.name="Arun C Michael" -c user.email="aruncmichael-alt@users.noreply.github.com" commit ...
```

---

## What is already done (do not redo)

- Public repo on `aruncmichael-alt/ocf-v1-beyond-vram`, `main` clean and synced.
- Release **v1.0.0** published with title matching the canonical string and PDF asset attached.
- Metadata prepared:
  - `.zenodo.json` — Zenodo archival metadata (title/creators/keywords/related identifiers)
  - `CITATION.cff` — GitHub Cite UI; DOI identifiers still TODO
  - `CITATION.bib` — BibTeX; DOI line commented TODO
  - `README.md` citation block — DOI commented TODO (`10.5281/zenodo.XXXXXXXX`)
  - `docs/zenodo-setup.md` — click-path checklist
  - `launch/` — post drafts + posting order (optional **after** DOI)

**Why v1.0.0 alone cannot mint the DOI:** Zenodo’s GitHub integration archives **new** releases **after** the webhook is enabled. v1.0.0 already exists, so you must cut **v1.0.1** (or next semver) once the repo is toggled On.

---

## Exact Zenodo steps (execute in order)

### A. Connect Zenodo ↔ GitHub (`aruncmichael-alt`)

1. Open https://zenodo.org/login → **Log in with GitHub** as **`aruncmichael-alt`** (not arunbiopower).
2. Authorize the Zenodo GitHub app if prompted (`admin:repo_hook` so Zenodo can install the release webhook).
3. Open https://zenodo.org/account/settings/github/ (or profile menu → **GitHub**).
4. Click **Sync now**.
5. Find **`aruncmichael-alt/ocf-v1-beyond-vram`** and toggle the slider **On**.
6. Confirm the repo shows as connected.

Official docs:

- https://help.zenodo.org/docs/github/enable-repository/
- https://help.zenodo.org/docs/github/archive-software/github-upload/
- https://help.zenodo.org/docs/github/describe-software/
- https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content

### B. Cut release **v1.0.1** (triggers archival)

On GitHub → Releases → Draft a new release:

| Field | Value |
| :--- | :--- |
| **Tag** | `v1.0.1` (create from `main` HEAD) |
| **Title** | `Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080` |
| **Body** | Note that this release triggers Zenodo archival; link v1.0.0 PDF and repo; state DOI will appear on Zenodo after processing |
| **Assets** | Optionally re-attach `Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf` (same file as v1.0.0) |

Example release body sketch:

```markdown
## Zenodo archival trigger (v1.0.1)

Same package as [v1.0.0](https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/tag/v1.0.0).
This follow-up tag exists so Zenodo’s GitHub webhook can archive the tree and mint a DOI
(v1.0.0 predates webhook enablement).

**PDF:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf

Do not redistribute GGUF weights; verify shards via `results/manifest.json` from upstream HF.
```

CLI alternative (still as `aruncmichael-alt`):

```bash
gh auth switch --user aruncmichael-alt
cd "C:\Users\Administrator\Documents\ocf-v1-beyond-vram"
git pull origin main
# After Zenodo slider is On:
gh release create v1.0.1 --title "Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080" --notes-file - <<'EOF'
## Zenodo archival trigger (v1.0.1)
Same package as v1.0.0; this tag triggers Zenodo webhook archival.
PDF: https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/download/v1.0.0/Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf
EOF
# Optionally: attach PDF with --notes + asset upload via gh release upload
```

### C. Wait for Zenodo; copy the **real** DOI

1. Wait minutes (sometimes longer under load).
2. Zenodo → GitHub → `ocf-v1-beyond-vram` → open the processed **v1.0.1** record.
3. Copy:
   - **Version DOI** (this release), e.g. `10.5281/zenodo.NNNNNNNN`
   - **Concept / parent DOI** (all versions) if shown — keep both; prefer version DOI in citation `doi = {…}` unless style guides say otherwise.

### D. Paste DOI into repo files (replace placeholders only)

Update these three surfaces with the **real** DOI — never leave `XXXXXXXX` or invent an id:

1. **`README.md`** — citation BibTeX block: uncomment / set `doi = {10.5281/zenodo.<REAL>}` and remove the `TODO(DOI)` comment lines.
2. **`CITATION.bib`** — same: add real `doi = {…}` line; remove TODO comments.
3. **`CITATION.cff`**:
   - Replace or extend `identifiers:` with a `type: doi` entry for the real DOI.
   - Under `preferred-citation:`, add `doi: 10.5281/zenodo.<REAL>`.
   - Bump `version:` / `url:` to v1.0.1 if you want citation metadata to track the archival release (optional but recommended).
4. Optionally add a Zenodo DOI badge to `README.md`.
5. Optionally bump `.zenodo.json` `"version"` to `"1.0.1"` and refresh the notes (nice-to-have; Zenodo already ingested from the release).

### E. Commit + push (no force)

```bash
gh auth switch --user aruncmichael-alt
cd "C:\Users\Administrator\Documents\ocf-v1-beyond-vram"
git pull origin main
git add README.md CITATION.bib CITATION.cff
# plus any optional badge / .zenodo.json / release-note edits
git -c user.name="Arun C Michael" -c user.email="aruncmichael-alt@users.noreply.github.com" commit -m "$(cat <<'EOF'
Record Zenodo DOI from v1.0.1 archival release.

EOF
)"
git push origin main
gh auth switch --user arunbiopower
```

### F. Optional: edit GitHub release notes

Edit **v1.0.1** (and optionally **v1.0.0**) release notes to include the live DOI badge / link once minted.

---

## After DOI — optional post order (do **not** Day-1 spray)

Only after the real DOI is in README/CITATION and pushed. Follow `launch/README.md`:

1. OpenCode discussion — `launch/01-opencode-discussion.md`
2. Strata discussion — `launch/02-strata-discussion.md`
3. Hugging Face model discussion — `launch/03-huggingface-model-discussion.md`
4. LocalLLaMA — `launch/04-localllama.md`
5. Show HN / r/Cursor **last** — `launch/05-show-hn.md`, then `launch/06-cursor-subreddit.md`

Insert the real DOI into drafts before posting. **This DOI handover does not authorize posting.** Prefer slow sequential posts; captcha/login = stop and hand back to Arun.

---

## Out of scope

- Fabricating a DOI
- arXiv / TechRxiv / OSF / conference submission
- GGUF redistribution
- Auto-posting all `launch/` channels
- Changing git global config / force-push / company-account publish

---

## Success checklist

- [ ] Zenodo logged in as **`aruncmichael-alt`**
- [ ] Repo `aruncmichael-alt/ocf-v1-beyond-vram` slider **On** at https://zenodo.org/account/settings/github/
- [ ] GitHub release **v1.0.1** published (webhook-era tag)
- [ ] Zenodo shows a processed record for that release
- [ ] Real `10.5281/zenodo.…` copied (version DOI; note concept DOI if present)
- [ ] `README.md`, `CITATION.bib`, `CITATION.cff` updated — **no** `XXXXXXXX` / TODO DOI left
- [ ] Commit + push to `main` with local author `-c` (no global config, no force-push)
- [ ] Optional: release notes + DOI badge updated
- [ ] `gh auth switch --user arunbiopower` restored
- [ ] No GGUF uploaded; no secrets committed; no Reddit/HN Day-1 spray unless Arun separately asks after DOI

---

## Quick reference — placeholder locations today

| File | What to replace |
| :--- | :--- |
| `README.md` | `% TODO(DOI): …` / `% doi = {10.5281/zenodo.XXXXXXXX}` |
| `CITATION.bib` | Same TODO / commented doi line |
| `CITATION.cff` | `# TODO(DOI): …` identifiers block + preferred-citation doi comment |

When finished, reply with: Zenodo record URL, version DOI, concept DOI (if any), commit URL of the DOI wire-up, and confirmation that `gh` is back on **`arunbiopower`**.
