# Security Policy

This repository publishes sanitized architecture notes, configuration **templates**, and measurement ledgers for OCF V1.

## Do not publish

- Local API keys, bearer tokens, or `.env` files
- Host filesystem paths to personal or company repos
- Non-loopback endpoint bindings
- Proprietary job titles, monorepo names, or production payloads
- GGUF weight files (fetch upstream and verify SHA-256 in `results/manifest.json`)

## Recommended local posture

- Bind Strata only to `127.0.0.1`
- Keep API keys in an untracked secrets file referenced by config templates
- Treat USB HDD archives as cold storage only; never as active `PLE` lookup paths

Report security issues privately to the repository owner.
