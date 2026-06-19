---
title: Leviathan Contract Surface Map
created: 2026-06-17
updated: 2026-06-19
type: contract-map
status: current-source-reader
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: source authority and contract routing map; not exhaustive implementation audit; not proof that contracts pass tests
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
  - https://github.com/lev-os/leviathan/tree/b7bca2cdbed5862743395f7c0330e7d640132764/docs/specs
---

# Contract Surface Map

This page routes claims to the source surface that is allowed to settle them.

## Authority Ladder

The current docs tree says to prefer:

1. `docs/specs/**` for normative contracts.
2. `docs/ARCHITECTURE.md` for topology and ownership boundaries.
3. `docs/VISION.md` for stable strategic destinations.
4. `docs/ROADMAP.md` for honest current state and active work.
5. `docs/design/**` for rationale and deep reference.
6. `docs/_inbox/**` for useful but noncanonical source material.

For wiki work, read `mvp.md` beside `docs/ROADMAP.md` because those two currently disagree on proof status.

## What Each Surface Settles

| Claim kind | Primary source | Wiki rule |
|---|---|---|
| Module ownership and runtime boundaries | `docs/ARCHITECTURE.md` | Use architecture unless current package paths visibly contradict it; then preserve the contradiction. |
| Contract semantics | `docs/specs/**` | Use for "should" and "must" language; do not treat draft specs as test proof. |
| Current execution status | `docs/ROADMAP.md`, `mvp.md`, proof receipts | Preserve split verdicts until fresh commands reconcile them. |
| Product vision | `docs/NORTH_STAR.md`, `docs/VISION.md`, README | Label as vision/product frame, not implementation health. |
| Code/package existence | `package.json`, source files, workspace files | Label as observed source/package existence. |
| Runtime proof | command outputs, result receipts, CI | Required for green/pass language. |
| Chat/handoff/provenance | `_inbox/**`, transcripts, `.lev/pm/**` | Starts as provenance; promote only after current source match. |

## Current High-Risk Contract Splits

| Topic | Current split | Wiki wording |
|---|---|---|
| Plane model | README uses three-plane shorthand; architecture and roadmap clarify four-plane technical boundary. | Use four-plane model on technical pages; mention README shorthand where helpful. |
| Graph path | Architecture still names Graph as plane and has old `core/graph/**` wording; current package is `core/context-graph` / `@lev-os/context-graph`. | Keep "Graph" as concept; use `core/context-graph/**` for implementation path. |
| Proof status | `docs/ROADMAP.md` says Pentagon/default daemon/testing/security are red or open; current `mvp.md` says named/default Pentagon, `@lev-os/testing`, and scoped security are green. | Call this a source-doc split; rerun commands before promoting. |
| Plugin paths | Old wiki pages mention `plugins/core-platforms/**` and `plugins/core-sdlc/**`; current architecture uses `plugins/platforms/**` and `plugins/sdlc/**`. | Current pages use flat paths; old names are historical aliases only. |

## Spec Mirror

Use [[specs/leviathan-current/README]] for repo-facing mirror policy. Use `projects/leviathan-current` for human explanations, dashboards, packets, and receipts.
