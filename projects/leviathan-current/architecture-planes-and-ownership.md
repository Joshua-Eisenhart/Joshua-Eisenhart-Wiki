---
title: Leviathan Architecture Planes and Ownership
created: 2026-06-17
updated: 2026-06-19
type: architecture-wiki-page
status: current-source-reader
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: source-doc and package-surface architecture map; not runtime proof; not full implementation audit
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ROADMAP.md
---

# Architecture Planes And Ownership

`docs/ARCHITECTURE.md` is the current technical topology and ownership reference for Lev. The root README is useful public framing, but its three-plane explanation is shorthand.

## Four-Plane Boundary

| Plane | Owner | Owns | Must not own |
|---|---|---|---|
| FlowMind | `core/flowmind/**` | workflow declarations, schema, validation, compilation, policy, progressive-disclosure sessions | worker dispatch, retry loops, concurrency management |
| Orchestration | `core/orchestration/**` | DAG scheduling, iterative loops, queues, worker coordination, execution strategy | policy authorship or `.flow.yaml` mutation |
| Graph / Context Graph | docs say Graph; current package surface is `core/context-graph/**` | entity state, knowledge, traversal, lineage, projections, context graph behavior | scheduling or worker dispatch |
| Event Bus | `core/event-bus/**` | canonical event spine, persistence, replay/recovery, lifecycle-significant receipts | replacing local internal DB/file/queue details when they are properly mirrored |

Plain version:

```text
FlowMind says what is admitted.
Orchestration decides how work proceeds.
Graph remembers and relates state.
Event Bus records and propagates lifecycle-significant facts.
```

## Current Source Correction: Graph Path

The 2026-06-19 fresh clone at `b7bca2cdbed5862743395f7c0330e7d640132764` has no `core/graph/package.json`. The current package is:

```text
core/context-graph/package.json
name: @lev-os/context-graph
```

Wiki pages should keep "Graph" as the architecture-plane noun, but implementation/path claims should say `core/context-graph/**` and `@lev-os/context-graph` unless a future repo commit restores or redirects `core/graph/**`.

## Adjacent Runtime Owners

| Owner | Path | Plain role |
|---|---|---|
| Exec | `core/exec/**` | execution SDK and provider dispatch |
| Poly | `core/poly/**` | registry/binder/control-surface projection |
| Daemon | `core/daemon/**` plus daemon protocol packages | process supervision and long-running runtime lifecycle |
| Domain | `core/domain/**` | shared contracts and execution data types |
| Telemetry | `core/telemetry/**` | tracing and metrics |
| UI Renderers | `core/ui/**` | UniversalWidget/renderer abstractions |

## Plugin Ownership

Current `docs/ARCHITECTURE.md` uses these active plugin paths:

- `plugins/platforms/**`
- `plugins/sdlc/**`
- `plugins/deploy/**`
- `plugins/beads/**`
- `plugins/graph-adapters/**`
- `plugins/mastra/**`
- `plugins/notion/**`
- `plugins/voice/**`
- `plugins/vision/**`
- `plugins/auth-sniffer/**`
- `plugins/browser/**`
- `plugins/evolve-memory/**`

Do not preserve old `plugins/core-platforms/**` or `plugins/core-sdlc/**` wording on current pages except as a historical alias.

## Source Contradictions To Preserve

- README says three planes; architecture and roadmap clarify the four-plane model.
- `docs/ARCHITECTURE.md` still has at least one ownership-map row that says `core/graph/**`; current package reality is `core/context-graph/**`.
- `docs/ROADMAP.md` and `mvp.md` disagree about current proof status for default daemon/Pentagon/testing/security gates.

Do not smooth these into a single clean sentence. Record the source layer and date.
