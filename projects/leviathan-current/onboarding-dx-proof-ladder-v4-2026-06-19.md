---
title: Leviathan Onboarding and DX Proof Ladder
created: 2026-06-19
updated: 2026-06-19
type: proof-ladder
status: current-source-synthesis
claim_ceiling: DX proof ladder only; quickstart existence is not quickstart proof
tags: [leviathan, onboarding, dx, proof-ladder, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
---

# Leviathan Onboarding and DX Proof Ladder

Onboarding and DX are gates, not paperwork. A README quickstart is not proof that a new user can reliably install and run the system.

## Quickstart surface

The README quickstart shape is:

```bash
git clone https://github.com/lev-os/leviathan.git
cd leviathan
corepack enable
pnpm install
pnpm build
```

## DX gates

- clean clone install;
- root build;
- `lev --help`, `lev doctor`, or `lev health`;
- first useful command;
- docs link validity;
- starter `.flow.yaml` path;
- no hidden local-only assumptions;
- clear developer setup vs operator runtime start;
- proof receipt with commit SHA and clean status.

## Safe verdict

DX readiness is open until a current clean-clone proof packet records the full path.

## Read next

- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
- [[projects/leviathan-current/security-gate-stack-v4-2026-06-19]]
