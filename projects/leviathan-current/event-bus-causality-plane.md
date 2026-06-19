---
title: Event Bus / Causality Plane
created: 2026-06-17
updated: 2026-06-19
type: runtime-plane-map
status: current-source-reader
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: source/package map for causality plane; not event-dispatch proof; not daemon/live automation proof
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/core/event-bus/package.json
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ROADMAP.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/mvp.md
---

# Event Bus / Causality Plane

## Current Correction

The old Packet 2 event-bus page was written against a damaged local checkout and treated conflict markers as current upstream blockers. That finding is historical.

For current upstream truth, use the 2026-06-19 fresh clone at `b7bca2cdbed5862743395f7c0330e7d640132764`. This page is now a source/package map, not a build or runtime proof packet.

## Boundary Summary

Event Bus is the causality plane. It owns the canonical event spine for lifecycle-significant transitions across FlowMind, Orchestration, Graph, Exec, Poly, Daemon, and plugins.

Current architecture rule:

```text
Cross-plane boundaries must emit canonical LevEvent with correlation IDs for lifecycle-significant transitions.
```

Operational modules may use local tables, queues, files, or indexes internally when those mutations are leased/gated and mirrored into the receipt/event/proof trail.

## Current Package Surface

Observed from `core/event-bus/package.json` at `b7bca2cd`:

- `@lev-os/event-bus`
- exports `.`
- exports `./events`
- exports `./runtime`
- exports `./context`
- exports `./aggregates`
- exports `./frontmatter`
- exports `./policy`
- exports `./bridge`
- exports `./workflow`
- exports `./actions`
- exports `./guards`
- exports `./types`

This proves package-surface existence only.

## Proof Status

`docs/ROADMAP.md` and `mvp.md` disagree about how far event/daemon automation has advanced:

- `docs/ROADMAP.md` says manual events mode works, but daemon expansion should wait until S5/Pentagon and security gates are repaired.
- `mvp.md` says manual dispatch/projection is working and default daemon/Pentagon proof is green, but live EventBus subscription, cron firing, daemon loop, and real executor handoff remain unproven.

Safe wording:

```text
Manual event/projection surfaces are source-claimed as working. Always-on daemon/event automation still needs current proof before launch-readiness claims.
```

## Not Checked Here

No package tests, build, daemon smoke, event-dispatch test, or Pentagon gate was run for this page. Use [[projects/leviathan-current/current-state-and-roadmap]] and [[projects/leviathan-current/proof-backed-status-dashboard]] for current proof routing.
