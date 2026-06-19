---
title: Codex Ratchet Repo Authority and Front Door Refresh
created: 2026-06-19
type: project-router
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, front-door, authority]
sources:
  - Codex-Ratchet/README.md
  - Codex-Ratchet/AGENTS.md
  - Codex-Ratchet/REPO_LAYOUT.md
  - Joshua-Eisenhart-Wiki/projects/codex-ratchet/read-first.md
---


# Codex Ratchet Repo Authority and Front Door Refresh — 2026-06-19

## Purpose

Use this as a small bridge between the dense wiki front door and the current repo authority surfaces.

It does not replace `projects/codex-ratchet/read-first.md`. It tells agents what to exact-read before they make a claim.

## Authority order for wiki-side work

1. Current user request.
2. Live repo instructions and authority files:
   - `Codex-Ratchet/AGENTS.md`
   - `Codex-Ratchet/CODEX.md` if present
   - `Codex-Ratchet/CLAUDE.md` only as reference/process language, not Codex law.
3. Repo process docs:
   - `system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md`
   - `system_v5/docs/LLM_CONTROLLER_CONTRACT.md`
   - `system_v5/docs/LEGO_SIM_CONTRACT.md`
   - `system_v5/ops/SIM_FULL_WIZARD_PARALLEL_RUNBOOK.md`
4. Repo result/validator/readiness artifacts for status claims.
5. Wiki pages as salience, routing, source-processing, and provenance.

## Read-first set for a fresh Codex Ratchet wiki edit

```text
projects/codex-ratchet/front-door-slim-load-order-2026-06-19
projects/codex-ratchet/read-first
specs/codex-ratchet/README
specs/codex-ratchet/process-contract-refresh-mirror-2026-06-19
specs/codex-ratchet/status-labels-crosswalk-2026-06-19
```

## Exact-read before status claims

Before any page says `current`, `verified`, `admitted`, `canonical`, `done`, `passed`, or `solved`, exact-read the source file or result path. Do not rely on CocoIndex rank, summary memory, or a worker report.

## What this page licenses

- Creating small spec mirrors.
- Adding route cards to the project front door.
- Adding source-processing pages with explicit claim ceilings.
- Creating templates and checklists.

## What this page does not license

- Editing repo status.
- Promoting a sim.
- Treating a scratch diagnostic as admission.
- Treating wiki prose as executable evidence.
- Replacing the dense front door without review.
