---
title: Leviathan Contract Surface Map
created: 2026-06-17
updated: 2026-06-17
type: contract-map
status: packet-1 current-authority synthesis
claim_ceiling: selected specs/docs scout; not exhaustive implementation audit
sources:
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-flowmind.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-orchestration.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-graph.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-bus.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-exec.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-poly.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-daemon.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-kernel.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-agentping.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-agentping-surfaces.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-agentping-host-relationship.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-levui-ir.md
---

# Contract Surface Map

## Contract hierarchy

`docs/README.md` gives the repo's own documentation priority order:

1. `docs/specs/**` — normative contracts.
2. `docs/ARCHITECTURE.md` — topology and ownership boundaries.
3. `docs/ROADMAP.md` — current execution state.
4. `docs/design/**` — rationale and deep reference.
5. `docs/_inbox/**` — useful but not runtime truth.

This page follows that order, with one caveat: when a spec conflicts with the active architecture page and current package paths, the conflict is preserved rather than smoothed.

## Specs index status

`docs/specs/README.md` says there are 61 specs total. Selected high-signal specs read in Packet 1:

| Area | Spec | Visible state |
|---|---|---|
| FlowMind | `spec-flowmind.md` | approved |
| Orchestration | `spec-orchestration.md` | approved |
| Graph | `spec-graph.md` | status mismatch: index says parity, frontmatter says approved |
| Event Bus | `spec-event-bus.md` | approved |
| Exec | `spec-exec.md` | approved |
| Poly | `spec-poly.md` | approved |
| Daemon | `spec-daemon.md` | status mismatch: index says approved, frontmatter says parity |
| Kernel | `spec-kernel.md` | parity; contains stale path conflicts |
| AgentPing | `spec-agentping.md` | draft |
| AgentPing surfaces | `spec-agentping-surfaces.md` | draft |
| AgentPing host relationship | `spec-agentping-host-relationship.md` | draft |
| LevUI IR | `spec-levui-ir.md` | draft |

## Cross-cutting contract: `LevEvent`

Architecture requires `LevEvent`-only inter-module event semantics for runtime lifecycle boundaries.

Shape named in `ARCHITECTURE.md`:

```ts
interface LevEvent<T = unknown> {
  version: 1;
  id: string;
  type: string;
  source: string;
  time: string;
  data: T;
}
```

The Event Bus owns persistence, replay, durable queues, session recovery, and explicit bridges. Direct lifecycle-significant cross-plane calls are disallowed by architecture.

## FlowMind contracts

FlowMind owns:

- system flow declarations in `core/flowmind/system/*.flow.yaml`;
- plugin flow declarations through plugin config / flow files;
- parser/compiler/schema/session APIs;
- `FlowmindSessionManager` session lifecycle;
- execution handoff into domain/orchestration data types;
- action/instruction vocabularies such as `spawn`, `condition`, `execute`, `emit`, `gate`, `loop`, `parallel`.

FlowMind does not own worker dispatch or concurrency.

## Orchestration contracts

Orchestration owns:

- DAG scheduling and topological sorting;
- scheduler strategies;
- task queues and durable JSONL queue surfaces;
- iterative loop execution;
- A2A job dispatch contracts;
- entity pipeline budget/validation/promotion surfaces;
- execution-contract functions that consume FlowMind/domain intent.

Known open areas from roadmap/code scout: budget/resource enforcement and full A2A orchestration have source surfaces but are not yet proven fully wired.

## Graph contracts

Graph owns:

- `EntityGraph.process(event)` style mutation pipeline;
- adapter shape: extract, apply, query, optional watch;
- graph event store / JSONL persistence;
- FlowMind `context_assembly` target;
- core adapters under `core/graph/src/adapters/**`;
- external runtime-dependency adapters under `plugins/graph-adapters/**`.

The Packet 1 scout found mixed status inside `spec-graph.md`: early sections describe shipped behavior, while later appendix/proposal material contains unchecked implementation phases. Treat graph implementation claims carefully until Packet 2.

## Exec contracts

Exec owns:

- `createExec(dispatch, opts)` → frozen `ExecEngine`;
- per-provider concurrency through `ProviderSemaphore`;
- dispatch contract: provider, method, args, options;
- event emission: `exec.started`, `exec.completed`, `exec.failed`, `exec.backpressure`;
- DI client facade over `ExecTransport`.

## Poly contracts

Poly owns:

- `core/poly/bin/lev`;
- CLI surface under `core/poly/src/surfaces/cli/`;
- MCP, HTTP, gRPC, and WebSocket surface generation/routing;
- registry/codegen/plugin-validator surfaces;
- SDK dispatch protocols.

Poly is a binder/router, not the owner of business logic, daemon lifecycle, or execution engine.

## Daemon contracts

Daemon owns:

- process supervisor;
- dependency DAG;
- queue manager;
- worker pools and warm worker pools;
- health monitoring;
- telemetry collection;
- process/brew/pmdaemon adapters;
- plugin daemon manifest discovery/validation;
- canonical daemon commands such as start, stop, restart, status, health, logs, list, exec.

## AgentPing / surface contracts

AgentPing specs are draft-level in this pass.

Visible contract targets:

- HTTP API on `:7890`;
- Web UI on `:7891`;
- WebSocket `/api/v1/ws`;
- agent registration;
- ping lifecycle;
- heartbeat protocol;
- surface registration and priority/fallback routing;
- ping types such as notification, approval, selection, input, step approval, confirmation, progress, data request, escalation, context update.

Host boundary:

```text
Lev is protocol / IR / policy authority.
AgentPing is default dashboard host and UI kit.
AgentPing core should not import @lev-os/*.
```

## LevUI IR contracts

LevUI IR is the host/provider-agnostic abstract UI layer under `core/ui`. Packet 1 read it as draft-state. Treat it as important architecture direction, not closed implementation proof.

## Stale references / contradictions found

These are useful failure signals, not cleanup noise:

1. `ARCHITECTURE.md` references `docs/specs/spec-daemons.md`, but the file is `spec-daemon.md`.
2. `spec-kernel.md` conflicts with canonical `core/poly` / `core/daemon` path ownership.
3. `spec-daemon.md` appears to repeat `core/daemon` as a legacy alias even while treating it as canonical.
4. `spec-kernel.md` lists stale FlowMind execution-contract paths that architecture/specs place under domain/orchestration.
5. `spec-graph.md` status differs between frontmatter and specs index.
6. `spec-daemon.md` status differs between frontmatter and specs index.
7. `spec-graph.md` mixes shipped behavior with proposal appendix material.
8. Orchestration/NTM language appears inconsistent: some current-state text remains while ownership tables mark NTM bridge/session pool deleted.
9. `spec-agentping.md` points to an NTM AgentPing bridge path not found in the scout.
10. Poly dashboard-spike language appears stale: one scenario says it should not exist; limitations say it exists; file search did not find it.
11. Event Bus ephemeral-store language appears mixed between current summary and deletion notes.
12. Specs README active chores look stale: listed root paths appear under `_done/`.

## Use rule for future pages

When a later page cites a contract:

- cite the exact spec/file;
- mark `approved`, `parity`, `draft`, `roadmap`, or `stale/conflict`;
- do not promote a draft/spec target to implemented runtime behavior unless code/tests earn that rung.
