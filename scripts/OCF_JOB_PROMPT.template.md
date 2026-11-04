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
