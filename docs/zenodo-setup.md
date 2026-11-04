# Zenodo DOI setup (operator checklist)

**Paper title (canonical):** Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080

**Repo:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram  
**Existing release:** https://github.com/aruncmichael-alt/ocf-v1-beyond-vram/releases/tag/v1.0.0  
**Author:** Arun C Michael  

No Zenodo API token was available in this environment, and interactive Zenodo OAuth was not already logged in. Minting therefore requires a short manual click path below. Repo metadata (`.zenodo.json`, `CITATION.cff`) is already prepared so archival is one enable + one new release away.

## Why a new release is required

Zenodo’s GitHub integration archives **new** GitHub releases after the webhook is enabled. Release **v1.0.0** already exists, so enabling the webhook alone will **not** auto-archive that past release. After connecting the repo, publish a follow-up tag (recommended: **v1.0.1**) so Zenodo ingests the tree and mints a DOI. Future releases will auto-mint version DOIs.

Official docs:

- Enable a repository: https://help.zenodo.org/docs/github/enable-repository/
- Archive a GitHub release: https://help.zenodo.org/docs/github/archive-software/github-upload/
- GitHub “Referencing and citing content”: https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- `.zenodo.json` / `CITATION.cff`: https://help.zenodo.org/docs/github/describe-software/

## Exact click path (Arun)

1. Open https://zenodo.org/login and choose **Log in with GitHub** (account that owns `aruncmichael-alt`).
2. Authorize the Zenodo GitHub app if prompted (`admin:repo_hook` is required so Zenodo can install a release webhook).
3. Open the Zenodo profile menu → **GitHub** (or go directly to https://zenodo.org/account/settings/github/).
4. Click **Sync now**.
5. Find **`aruncmichael-alt/ocf-v1-beyond-vram`** and toggle the slider **On**.
6. Confirm the repo appears as connected. (Org approval is N/A for a personal public repo.)
7. On GitHub, create a **new** release:
   - Tag: `v1.0.1` (or next semver)
   - Title: `Beyond VRAM Capacity: A Single-Workstation Case Study of Strata, Qwen3.8-Flash-Next, and OpenCode on an RTX 5080`
   - Body: point to the same PDF asset / note that this release triggers Zenodo archival of the whitepaper package
   - Optionally re-attach `Beyond-VRAM-Capacity-OCF-V1-Technical-Whitepaper.pdf`
8. Wait for Zenodo processing (minutes; occasionally longer under load).
9. On Zenodo → GitHub → select the repo → open the processed release → copy the **DOI** (version DOI and concept/parent DOI).
10. Replace `TODO(DOI)` / `10.5281/zenodo.XXXXXXXX` placeholders in:
    - `README.md` citation block
    - `CITATION.bib`
    - `CITATION.cff` (`identifiers` + preferred-citation `doi`)
11. Optionally add the Zenodo DOI badge to the README.
12. Commit and push the DOI updates; no force-push.

## Repo metadata already present

| File | Role |
| :--- | :--- |
| `.zenodo.json` | Zenodo-preferred metadata for GitHub release archival (overrides CFF for Zenodo when both exist) |
| `CITATION.cff` | GitHub “Cite this repository” UI + human-readable citation |
| `CITATION.bib` | BibTeX with URL; DOI line left as TODO until minting |

## Optional API path (if you create a token later)

1. Create a Zenodo personal access token (deposit:write / deposit:actions as needed) at https://zenodo.org/account/settings/applications/tokens/new/
2. Store it locally only (never commit); optional: `gh secret set ZENODO_TOKEN -R aruncmichael-alt/ocf-v1-beyond-vram`
3. Prefer the webhook path above over manual REST upload so subsequent GitHub releases stay linked.

## Out of scope here

- Inventing or fabricating a DOI before Zenodo mints one
- Submitting to arXiv / TechRxiv / OSF
- Redistributing GGUF weights
