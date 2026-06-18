---
title: Leviathan Architecture Planes and Ownership
created: 2026-06-17
updated: 2026-06-17
type: architecture-wiki-page
status: packet-1 current-authority synthesis
claim_ceiling: docs/specs/code-scout synthesis; not full implementation audit
sources:
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/AGENTS.md
  - /Users/joshuaeisenhart/GitHub/leviathan/core/*/package.json
---

# Architecture Planes and Ownership

## Canonical architecture cut

`docs/ARCHITECTURE.md` is the current canonical topology and ownership reference for the repo. It describes a “canonical hard cut”: no active legacy bridge paths, explicit owners, and `LevEvent`-only inter-module runtime events.

## Four-plane runtime boundary

The architecture page names four hard planes:

| Plane | Owner path | What it owns | What it must not do |
|---|---|---|---|
| **FlowMind** | `core/flowmind/**` | Declarations, constraints, compile/runtime policy, `.flow.yaml` → graph/execution intent. | Does not dispatch workers, retry, or own concurrency. |
| **Orchestration** | `core/orchestration/**` | DAG scheduling, execution strategy, worker dispatch, retries, iterative loops, queues, A2A jobs. | Does not mutate policy or rewrite `.flow.yaml`. |
| **Graph** | `core/graph/**` | Entity lifecycle, state/knowledge, graph operations, lineage, projections, context assembly. | Does not schedule execution or dispatch workers. |
| **Event Bus** | `core/event-bus/**` | Canonical event spine, persistence, replay, recovery/checkpoints, cross-plane lifecycle events. | Does not allow lifecycle-significant silent/direct cross-plane calls. |

Plain version:

```text
FlowMind says what is admissible.
Orchestration decides how work proceeds.
Graph remembers and relates state.
Event Bus records and propagates runtime facts.
```

## Adjacent runtime owners

| Owner | Path | Plain role | Observed package/source support |
|---|---|---|---|
| **Exec** | `core/exec/**` | Canonical execution SDK. | `@lev-os/exec`, `createExec(dispatch)`, ProviderSemaphore, exec event types. |
| **Poly** | `core/poly/**` | Binder/router/control-surface generation: CLI, MCP, HTTP, gRPC, SDK transport. | `@lev-os/poly`, `core/poly/bin/lev`, `src/surfaces/*`. |
| **Daemon** | `core/daemon/**` | Process/daemon runtime: supervisor, queue, worker pools, health. | `@lev-os/daemon`, `core.ts`, `supervisor.ts`, `worker-pool.ts`. |
| **Domain** | `core/domain/**` | Stable shared types and contracts, including `LevEvent` and execution-contract data. | `@lev-os/domain`. |
| **UI / LevUI IR** | `core/ui/**` | Abstract UI renderer / IR layer. | `@lev-os/ui-renderers`, LevUI specs; draft maturity. |
| **AgentPing** | `community/agentping/**` | Default human-loop surface host and UI kit. | Docs/specs; implementation status needs Packet 3. |

## Plugin ownership

The active architecture routes plugins by domain:

- platform integrations → `plugins/core-platforms/**`;
- SDLC lifecycle → `plugins/core-sdlc/**`;
- graph adapter extensions → `plugins/graph-adapters/**`;
- voice → `plugins/voice/**`;
- deployment → `plugins/deploy/**`;
- prompt-stack → backward-compatible shim; canonical sessions move toward FlowMind.

## Legacy aliases to avoid

Current docs and `AGENTS.md` say these are not active ownership paths:

- `core/cli/` — removed; CLI lives under `core/poly/src/surfaces/cli/`.
- `core/polyglot-runners/` — legacy alias; active binder/runtime surface is `core/poly/`.
- `core/daemons/` — retired alias; active daemon runtime is `core/daemon/`.

## Cheap code/package confirmation

Observed file/package anchors:

- root `package.json` exposes `lev` → `./core/poly/bin/lev`;
- `pnpm-workspace.yaml` includes `core/*`, `packages/*`, `plugins/*`, `tooling/*`;
- `core/flowmind/package.json` exists and exports parser/compiler/kernel/session surfaces;
- `core/orchestration/package.json` exports graph/loop/queue/entities/a2a/execution-contract surfaces;
- `core/graph/package.json` exports adapters/events and contains `src/compositor.ts`;
- `core/event-bus/package.json` exports events/runtime/context/aggregates/frontmatter/policy/bridge/workflow/actions/guards/types;
- `core/exec/package.json` exports `createExec`, types, semaphore, adapters, client;
- `core/poly/package.json` owns CLI/control surfaces;
- `core/daemon/package.json` owns daemon process/runtime surfaces.

These observations prove source/package existence, not runtime correctness.

## Important conflict to preserve

`docs/specs/spec-kernel.md` uses a different “four-plane” story and has stale path language around `core/poly` / `core/daemon`. Because `docs/ARCHITECTURE.md` is marked active canonical hard cut and agrees with package/source surfaces, this wiki should prefer `ARCHITECTURE.md` for the plane model.

Status:

```text
ARCHITECTURE.md plane model survived Packet 1.
spec-kernel.md needs a later stale-reference audit before being treated as equal authority.
```
