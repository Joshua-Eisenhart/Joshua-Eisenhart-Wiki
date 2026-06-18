---
title: Event Bus / Causality Plane
date: 2026-06-17
packet: 2
status: current-runtime-map-with-blocker
owned_by: background-packet-2
---

# Event Bus / Causality Plane

## Evidence and status labels

Major claims below are tagged with **[observed file]**, **[inferred from package/code]**, **[inferred from docs]**, **[roadmap/design intent]**, **[open]**, or **[not checked]**.

Primary sources read for this page:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-architecture.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-bus.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/event-bus.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/jsonl-persistence.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/runtime/queue.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/runtime/tool-call-checkpointer.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/bridge/event-action-bridge.ts`
- Conflict-marker scan over `/Users/joshuaeisenhart/GitHub/leviathan` for `<<<<<<<`, `=======`, `>>>>>>>`.

Related starter page incorporated by reference: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-graph-orchestration-start.md`.

## Critical blocker: unresolved conflict markers

Unresolved conflict markers were observed in active runtime source, including:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/scm.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/bridge/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/context/pr.ts`
- Additional conflict markers in `core/build/**` and Rust TUI crates were also returned by the scan. **[observed file]**

Therefore this page maps intended/current ownership and observed files, but **does not claim Event Bus build/runtime health**. **[observed file]** Any claim that depends on successful compilation or clean import of `@lev-os/event-bus` is **[open]** until conflict markers are resolved and typecheck/smoke passes.

## Boundary summary

Event Bus is Leviathan's **causality plane**: the canonical runtime event spine connecting FlowMind, Orchestration, Graph, Daemon, Exec, plugins, and providers. **[inferred from docs]** The architecture docs state that all cross-plane lifecycle-significant transitions should emit canonical `LevEvent` with correlation IDs, and that Event Bus owns event transport, persistence, replay/recovery, and checkpointing. **[inferred from docs]**

The package is `@lev-os/event-bus`. **[observed file]** Package metadata exports `.`, `./events`, `./runtime`, `./context`, `./aggregates`, `./frontmatter`, `./policy`, `./bridge`, `./workflow`, `./actions`, `./guards`, and `./types`. **[observed file]** The package depends on `@lev-os/domain`, `@lev-os/config`, `@lev-os/logger`, `xstate`, `zod`, and `js-yaml`. **[observed file]**

## What Event Bus owns

| Concern | Status | Evidence |
|---|---:|---|
| Public event-bus package/API surface | **[observed file]** but conflicted | `core/event-bus/src/index.ts` |
| In-process event bus implementation | **[observed file]** | `core/event-bus/src/events/event-bus.ts` |
| JSONL event persistence | **[observed file]** | `core/event-bus/src/events/jsonl-persistence.ts` |
| Runtime queueing | **[observed file]** | `core/event-bus/src/runtime/queue.ts` |
| Tool-call checkpointing | **[observed file]** | `core/event-bus/src/runtime/tool-call-checkpointer.ts` |
| Event/action bridge | **[observed file]** | `core/event-bus/src/bridge/event-action-bridge.ts` |
| Provider-specific event capture/adapters | **[inferred from docs]** | specs + event providers not deep-read in this packet |
| Cross-plane policy ownership | **not owned** | FlowMind owns policy; orchestration owns scheduling; graph owns state |

## Canonical contract

The architecture doc gives the canonical `LevEvent` shape:

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

This shape is documented as the inter-module event schema. **[inferred from docs]** Active runtime code in Event Bus should converge on this contract, but because `core/event-bus/src/index.ts` contains conflict markers, Packet 2 treats the current implementation conformance as **[open]**.

## Internal module map

### Public barrel and subpaths

`package.json` exposes a broad set of event-bus subpaths. **[observed file]** `src/index.ts` was read and contains active conflict markers, so its export set cannot be trusted as clean source until the conflict is resolved. **[observed file]**

### Event bus core

`events/event-bus.ts` implements the core event-bus behavior read in Packet 2. **[observed file]** This is the source-level owner for publish/subscribe-style event transport, but no runtime smoke was run. **[not checked]**

### Persistence and replay support

`events/jsonl-persistence.ts` implements JSONL persistence. **[observed file]** The architecture and event-bus spec describe persistent local event/state logs as required for deterministic replay. **[inferred from docs]** Current replay health is not claimed because of conflict markers and no smoke run. **[open]**

### Runtime queue and checkpointing

`runtime/queue.ts` and `runtime/tool-call-checkpointer.ts` were read as current implementation owners for queue and checkpoint support. **[observed file]** These support the event/cause spine around tool calls and background processing, but their integration path was not executed. **[not checked]**

### Event/action bridge

`bridge/event-action-bridge.ts` is an implementation boundary for turning events into actions or coordinating event/action transitions. **[observed file]** A separate `bridge/index.ts` has conflict markers, so bridge exports may be unhealthy. **[observed file]**

## Cross-plane relationships

| Plane/module | Event Bus role | Boundary condition | Status |
|---|---|---|---:|
| FlowMind | Carries runtime/policy/session/kernel events across planes | FlowMind owns control policy; bus owns causality transport | **[inferred from docs]** |
| Orchestration | Carries task/workflow state, queue, worker, checkpoint events | Orchestration owns scheduling; bus owns event record | **[inferred from docs]** |
| Graph | Carries graph/entity change events and supports projection/replay | Graph owns state; bus owns event spine | **[inferred from docs]** |
| Exec | Carries `exec.started`, `exec.completed`, `exec.failed`, `exec.backpressure` events | Exec owns execution engine | **[inferred from docs]** + exec read |
| Daemon | Carries daemon, supervisor, task, worker lifecycle events | Daemon owns process/worker implementation | **[inferred from docs]** + daemon read |
| Plugins | Plugin events should enter via canonical bus/SDK surfaces | Plugin owns domain logic | **[inferred from docs]** |

## Current event domains from architecture docs

The architecture doc lists known event families including exec, daemon, supervisor, worker, and task events. **[inferred from docs]** Examples include `exec.started`, `exec.completed`, `exec.failed`, `daemon.started`, `daemon.heartbeat`, `supervisor.started`, `worker.started`, `task.created`, and `task.completed`. **[inferred from docs]** Treat these as documented current architecture, not as test-verified in this packet. **[not checked]**

## Invariants to preserve

1. `LevEvent` is the only inter-module event schema. **[inferred from docs]**
2. Cross-plane lifecycle transitions should emit through the event spine with correlation IDs. **[inferred from docs]**
3. Event Bus owns persistence/replay/checkpoint mechanics but not policy, graph mutation decisions, or orchestration scheduling. **[inferred from docs]**
4. Runtime health must not be asserted until conflict markers are removed and tests pass. **[observed file]**

## Not checked in this packet

- `pnpm`, `npm`, or package-level Event Bus tests. **[not checked]**
- TypeScript typecheck/build. **[not checked]**
- Event providers and event machines source deep-read. **[not checked]**
- Full replay/recovery smoke. **[not checked]**

## Open questions

- Which side of each conflict in `core/event-bus/src/**` is intended current runtime? **[open]**
- Whether all event-bus subpath exports resolve cleanly after conflicts are resolved. **[open]**
- Whether all documented event families are emitted by current code and carry correlation IDs. **[open]**
