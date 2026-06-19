---
title: Leviathan Docs Authority vs Status Drift
created: 2026-06-19
updated: 2026-06-19
type: assessment
status: current-source-synthesis
claim_ceiling: source/wiki synthesis only; status truth still requires current proof receipts
tags: [leviathan, docs-authority, roadmap, mvp, proof-status, v4]
sources:
  - projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19.md
  - projects/leviathan-current/proof-backed-status-dashboard.md
  - projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18.md
---

# Leviathan Docs Authority vs Status Drift

Leviathan has a good docs authority hierarchy, but current status truth still depends on proof receipts because `docs/ROADMAP.md` and `mvp.md` disagree on important readiness gates.

## Authority hierarchy

| Layer | Role |
|---|---|
| specs | normative contracts |
| architecture | ownership/topology |
| vision | strategic destination |
| roadmap + mvp | execution state, currently split |
| design docs | rationale/deeper reference |
| inbox/archive/PM material | provenance and planning |

## Current split

`docs/ROADMAP.md` is more conservative: it keeps Pentagon/Run Fabric provider proof, `@lev-os/testing`, daemon state, stale S5 projection cleanup, and security P0 as mixed or open.

`mvp.md` is more optimistic: it reports named/default Pentagon proof, `@lev-os/testing`, and scoped security P0 as green while still blocking full launch on daemon/event automation and downstream surfaces.

## Wiki rule

Do not pick one prose status page as winner. Adjudicate row by row using current proof receipts.

## Read next

- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
- [[projects/leviathan-current/security-gate-stack-v4-2026-06-19]]
