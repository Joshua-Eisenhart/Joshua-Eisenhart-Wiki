---
title: Orchestration Execution Plane
date: 2026-06-17
packet: 2
status: current-runtime-map
claim_ceiling: historical Packet 2 source map with current-source caveats; not current build proof; not runtime health proof
owned_by: background-packet-2
---

# Orchestration Execution Plane

## Evidence and status labels

Major claims below are tagged with **[observed file]**, **[inferred from package/code]**, **[inferred from docs]**, **[roadmap/design intent]**, **[open]**, or **[not checked]**.

Primary sources read for this page:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-orchestration.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-flowmind.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-architecture.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/types.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/dag.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/loop/iterative-runner.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/queue/durable-task-queue.ts`

Related starter page incorporated by reference: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-graph-orchestration-start.md`.

## Boundary summary

Orchestration is Leviathan's **execution plane**: it owns deterministic multi-step orchestration, DAG scheduling, worker coordination, retry/iteration loops, queues, and execution strategy. **[inferred from docs]** The architecture doc states that FlowMind controls policy and declarations while Orchestration owns `ecStart`/`ecNext`, DAG scheduling, worker dispatch, retry logic, iterative loops, and concurrency. **[inferred from docs]**

The package is `@lev-os/orchestration`. **[observed file]** Its package metadata describes deterministic orchestration APIs for workflow DAG and epic wave execution, and exports `.`, `./graph`, `./loop`, `./queue`, `./entities`, `./a2a`, and `./execution-contract`. **[observed file]**

## What Orchestration owns

| Concern | Status | Evidence |
|---|---:|---|
| Public orchestration API and high-level runtime functions | **[observed file]** | `core/orchestration/src/index.ts` |
| Shared orchestration types/contracts | **[observed file]** | `core/orchestration/src/types.ts` |
| DAG/topological sorting | **[observed file]** | `core/orchestration/src/graph/dag.ts` |
| Scheduling strategies | **[observed file]** | `core/orchestration/src/graph/scheduler.ts` |
| Iterative execution loop/retry/budget behavior | **[observed file]** | `core/orchestration/src/loop/iterative-runner.ts` |
| Durable task queue | **[observed file]** | `core/orchestration/src/queue/durable-task-queue.ts` |
| FlowMind declaration/policy mutation | **not owned** | FlowMind owns declarations/policy |
| Graph state/knowledge persistence | **not owned** | Graph owns state/knowledge plane |
| Event causality spine | **not owned** | Event Bus owns causality plane |

## Package and module map

`core/orchestration/package.json` declares dependencies on `@lev-os/config`, `@lev-os/domain`, `@lev-os/flowmind`, and `@lev-os/logger`. **[observed file]** This dependency shape supports Orchestration consuming FlowMind/domain contracts rather than owning declaration schema. **[inferred from package/code]**

The full source inventory found 75 TypeScript files under `core/orchestration/src`. **[observed file]** Packet 2 read key boundary files but not every submodule. **[not checked]**

### Public API/barrel

`src/index.ts` is a large public entrypoint for orchestration. **[observed file]** It should be treated as the current API surface for high-level orchestration functions and exports, subject to a later exhaustive API diff. **[inferred from package/code]**

### Types

`src/types.ts` defines shared orchestration contracts. **[observed file]** These are the local execution-plane types used by graph/scheduler/loop/queue modules. **[inferred from package/code]**

### DAG graph

`src/graph/dag.ts` owns DAG/topological behavior. **[observed file]** The architecture doc notes consolidation of DAG and scheduler algorithms in `core/orchestration/src/graph/`, including topological sorting and cycle detection. **[inferred from docs]**

### Scheduler

`src/graph/scheduler.ts` owns scheduling strategies. **[observed file]** The architecture doc names `TopoSortScheduler`, `CriticalPathScheduler`, and `RuntimeDynamicScheduler` as scheduler strategies under `core/orchestration/src/graph/`. **[inferred from docs]**

### Iterative runner

`src/loop/iterative-runner.ts` owns the iterative execution loop. **[observed file]** Architecture docs distinguish this from FlowMind sessions: `FlowmindSessionManager.next()` picks the next step, while `executeIterativeLoop()` handles how to run it with retries, budget, and context pressure. **[inferred from docs]**

### Durable queue

`src/queue/durable-task-queue.ts` implements a durable task queue. **[observed file]** Packet 2 treats queueing and task readiness/claiming semantics as execution-plane behavior, while lifecycle event transport belongs to Event Bus. **[inferred from docs]**

## Cross-plane relationships

| Plane/module | Orchestration role | Other owner role | Status |
|---|---|---|---:|
| FlowMind | Receives compiled intent and executes strategy/loops | FlowMind owns declarations/policy/session cursor | **[inferred from docs]** |
| Graph | Reads/writes state through graph/context contracts as execution progresses | Graph owns state/knowledge lifecycle and projections | **[inferred from docs]** |
| Event Bus | Emits task/workflow/worker lifecycle events | Event Bus owns canonical event spine and replay | **[inferred from docs]**; bus conflicts observed |
| Exec | Can delegate actual provider/tool execution to Exec | Exec owns provider execution engine and backpressure | **[inferred from docs]** + exec files read |
| Daemon | Can integrate with daemon lifecycle/queues/workers for background execution | Daemon owns processes, supervisors, worker pools | **[inferred from docs]** + daemon files read |
| Plugins | Domain plugins attach workflows/commands at proposal/workflow level | Plugins own domain-specific commands/templates/FlowMinds | **[inferred from docs]** |

## Runtime path pattern

The current intended execution layering is:

```text
FlowMind declaration/session
  -> compiled intent / next step
  -> Orchestration DAG / scheduler / iterative runner / queue
  -> Exec or daemon/plugin-specific adapter
  -> Event Bus lifecycle events
  -> Graph state/context updates
```

This flow is **[inferred from docs]** and supported by package/code boundaries read in Packet 2. It was not executed as an end-to-end smoke. **[not checked]**

## Invariants to preserve

1. Orchestration does not mutate FlowMind policy or rewrite `.flow.yaml` declarations. **[inferred from docs]**
2. Orchestration owns scheduling, retry loops, durable execution queues, and execution strategy. **[inferred from docs]**
3. DAG/scheduler algorithms should stay consolidated in `core/orchestration/src/graph/`. **[inferred from docs]**
4. Iterative runner semantics are distinct from entity-level SDLC/plugin loops. **[inferred from docs]**
5. Event emissions should use canonical Event Bus contracts, but runtime event health remains blocked until event-bus conflicts are resolved. **[observed file]**

## Not checked in this packet

- Orchestration package tests/typecheck. **[not checked]**
- All 75 TypeScript files under `core/orchestration/src`. **[not checked]**
- Runtime smoke of `executeIterativeLoop()` or queue persistence. **[not checked]**
- A2A and entities subpath implementations. **[not checked]**

## Open questions

- Which runtime paths call `executeIterativeLoop()` today and whether all do so through public APIs. **[open]**
- Whether durable queue persistence semantics are file, XDG, database, or adapter-backed in all modes. **[open]**
- Whether all scheduler strategies have current contract tests. **[open]**
