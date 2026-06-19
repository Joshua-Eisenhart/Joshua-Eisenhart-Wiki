---
title: Leviathan Current Specs Mirror
created: 2026-06-19
updated: 2026-06-19
type: specs-mirror-index
status: current-source-router
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: repo-facing mirror policy and routing; not the canonical repo; not implementation proof
tags:
  - leviathan
  - specs
  - mirror
  - source-authority
---

# Leviathan Current Specs Mirror

This folder is the repo-facing mirror and status-router surface for `lev-os/leviathan`.

The repo remains the authority. This mirror exists so wiki pages can explain and route without pretending to be the live source of truth.

## Authority Boundary

Use this folder for:

- source authority order;
- dated source snapshots;
- contract/status mirrors;
- split-verdict dashboards;
- stale-path and stale-claim receipts;
- proof-routing notes.

Do not use this folder to silently settle contradictions the repo has not settled.

## Current Snapshot

Fresh source read:

```text
repo: https://github.com/lev-os/leviathan
branch: main
commit: b7bca2cdbed5862743395f7c0330e7d640132764
clone: /tmp/leviathan-current-20260619-3WQpXq
clone status: clean after clone
```

## Source Ladder

1. `docs/specs/**` for normative contracts.
2. `docs/ARCHITECTURE.md` for topology and ownership boundaries.
3. `docs/VISION.md` for stable strategic destinations.
4. `docs/ROADMAP.md` and `mvp.md` together for execution state while they disagree.
5. `docs/NORTH_STAR.md`, root `README.md`, and `docs/README.md` for product framing.
6. Current source paths under `core/**`, `plugins/**`, `crates/**`, `apps/**`, and `packages/**`.
7. `docs/design/**` for rationale and deep reference.
8. `.lev/pm/**`, `_inbox/**`, old local-path pages, chats, transcripts, and worker reports as provenance only.

## Current Split Verdicts

- Four-plane technical model wins over README three-plane shorthand for technical pages.
- Graph is still the architecture-plane noun, but current package path is `core/context-graph/**` / `@lev-os/context-graph`.
- `docs/ROADMAP.md` and `mvp.md` disagree about Pentagon/default daemon, `@lev-os/testing`, and security P0 status.
- Old damaged-checkout conflict-marker claims are historical unless a current clone/source scan reproduces them.

## Project Pages

- [[projects/leviathan-current/what-is-leviathan]]
- [[projects/leviathan-current/architecture-planes-and-ownership]]
- [[projects/leviathan-current/contract-surface-map]]
- [[projects/leviathan-current/current-state-and-roadmap]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
