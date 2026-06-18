---
title: Graph State / Knowledge Plane
date: 2026-06-17
packet: 2
status: current-runtime-map
owned_by: background-packet-2
---

# Graph State / Knowledge Plane

## Evidence and status labels

Major claims below are tagged with **[observed file]**, **[inferred from package/code]**, **[inferred from docs]**, **[roadmap/design intent]**, **[open]**, or **[not checked]**.

Primary sources read for this page:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-graph.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-graph-adapters.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-architecture.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/bridge/event-adapter.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/events/jsonl-store.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/context/projector.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/adapters/memory.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/graph-adapters/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/graph-adapters/config.yaml`

Related starter page incorporated by reference: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-graph-orchestration-start.md`.

## Boundary summary

Graph is Leviathan's **state/knowledge plane**. **[inferred from docs]** It owns entity lifecycle, graph state, knowledge storage/traversal contracts, lineage/projections, and pluggable adapters; it does not own scheduling or worker dispatch. **[inferred from docs]** The architecture doc explicitly states the plane invariant: Graph owns entity lifecycle, state observation, knowledge storage, and traversal, and never triggers execution or dispatches workers. **[inferred from docs]**

The current implementation package is `@lev-os/graph`. **[observed file]** Its package description calls it an entity graph compositor with a `classify -> validate -> apply` pipeline and pluggable adapters, with exports for `.`, `./adapters`, and `./events`. **[observed file]**

## What Graph owns

| Concern | Status | Evidence |
|---|---:|---|
| Public graph API/barrel exports | **[observed file]** | `core/graph/src/index.ts` |
| Entity graph compositor / pipeline | **[observed file]** | `core/graph/src/compositor.ts` |
| Event-to-graph bridge | **[observed file]** | `core/graph/src/bridge/event-adapter.ts` |
| JSONL graph/event storage | **[observed file]** | `core/graph/src/events/jsonl-store.ts` |
| Context projection | **[observed file]** | `core/graph/src/context/projector.ts` |
| In-memory adapter | **[observed file]** | `core/graph/src/adapters/memory.ts` |
| Domain-specific/external graph adapters | **[observed file]** / plugin-owned | `plugins/graph-adapters/package.json`, `config.yaml` |
| Scheduling, retry, worker dispatch | **[inferred from docs]** / not owned | `docs/ARCHITECTURE.md`, orchestration sources |

## Package and module map

`core/graph/package.json` exposes `@lev-os/graph`, `@lev-os/graph/adapters`, and `@lev-os/graph/events`. **[observed file]** The package depends on `@lev-os/config` and `@lev-os/domain`, which places graph's core implementation near domain data contracts rather than execution transport. **[observed file]**

Implementation files sampled in this packet show this shape:

- `src/index.ts`: public export surface for graph types, compositor, adapters/events/context pieces. **[observed file]**
- `src/compositor.ts`: central graph mutation/composition pipeline. **[observed file]**
- `src/bridge/event-adapter.ts`: connects event data into graph operations. **[observed file]**
- `src/events/jsonl-store.ts`: JSONL-backed event/graph persistence primitive. **[observed file]**
- `src/context/projector.ts`: converts graph state into context/projection views. **[observed file]**
- `src/adapters/memory.ts`: in-memory adapter implementation. **[observed file]**

Full inventory found 29 TypeScript files under `core/graph/src`. **[observed file]** This packet read key boundary files but not every internal test/adapter file. **[not checked]**

## Compositor pipeline

The package description and `compositor.ts` establish the graph compositor as the owner of a classify/validate/apply-style entity pipeline. **[observed file]** At the architecture level, this is the graph's local state mutation boundary, not an orchestration boundary. **[inferred from docs]**

Packet 2 wording to preserve:

- Graph can classify/validate/apply entity graph changes. **[inferred from package/code]**
- Graph can persist/project graph-related events and state. **[inferred from package/code]**
- Graph should not schedule runtime workers or cause process execution. **[inferred from docs]**

## Event bridge and causality handoff

`bridge/event-adapter.ts` makes graph event-aware. **[observed file]** The event architecture says all plane-spanning lifecycle transitions should flow over canonical `LevEvent` with correlation IDs, and Graph should connect to Event Bus rather than becoming an event spine itself. **[inferred from docs]**

`events/jsonl-store.ts` indicates a local JSONL persistence mechanism in graph. **[observed file]** Treat this as graph-owned persistence/projection support, not proof of full event-bus replay health. **[inferred from package/code]** Event Bus currently has unresolved conflict markers, so Packet 2 must not claim a clean end-to-end graph/event replay runtime. **[observed file]**

## Context projection

`context/projector.ts` is Graph's context projection boundary. **[observed file]** In the architecture model, Graph supplies observed state/knowledge context to FlowMind and other consumers while preserving the distinction that policy remains FlowMind-owned and scheduling remains orchestration-owned. **[inferred from docs]**

## Adapter ownership

Core graph includes at least an in-memory adapter (`adapters/memory.ts`). **[observed file]** Domain-specific graph adapters are plugin-owned under `plugins/graph-adapters`; the plugin package metadata describes external backends including FalkorDB, Graphiti, and Cognee. **[observed file]**

Boundary guidance:

| Adapter class | Owner | Status |
|---|---|---:|
| Core memory adapter | `core/graph` | **[observed file]** |
| External/domain graph adapters | `plugins/graph-adapters` | **[observed file]** |
| Adapter spec and expected behavior | docs/specs | **[inferred from docs]** |
| Runtime validation of all external adapters | not completed in Packet 2 | **[not checked]** |

## Cross-plane relationships

| To plane/module | Graph role | Other owner role | Status |
|---|---|---|---:|
| FlowMind | Supplies observed graph/context state and graph IR concepts | Owns declaration/control/policy and sessions | **[inferred from docs]** |
| Event Bus | Publishes/consumes graph-relevant events via bridge; can use JSONL local store | Owns canonical event causality, persistence, replay/checkpointing | **[inferred from docs]**; bus conflicts observed |
| Orchestration | Supplies state/projections for execution decisions and can record outcomes | Owns DAG scheduling, iterative runner, queues | **[inferred from docs]** |
| Plugins | Provides core adapter contract; plugin adapters extend backends/domains | Plugins own external integration dependencies and domain-specific logic | **[observed file]** + **[inferred from docs]** |

## Current invariants to preserve

1. Graph is the state/knowledge owner, not a scheduler. **[inferred from docs]**
2. Graph adapter extensions should live in plugin packages when they bring domain-specific or external dependencies. **[inferred from docs]**
3. Event bridging should preserve canonical causality rather than inventing a second runtime event spine. **[inferred from docs]**
4. Context projection belongs in Graph; policy interpretation belongs in FlowMind. **[inferred from docs]**
5. Graph runtime-health claims should be qualified until Event Bus conflicts are resolved and end-to-end smoke is run. **[observed file]**

## Not checked in this packet

- Full graph tests or `bun test`. **[not checked]**
- External adapter implementation files inside `plugins/graph-adapters`. **[not checked]**
- Typecheck/build for graph package. **[not checked]**
- End-to-end graph/event replay over Event Bus. **[not checked]**

## Open questions

- Which graph events are canonical `LevEvent` versus graph-local JSONL records should be checked after event-bus conflicts are resolved. **[open]**
- Whether each external adapter has a contract test matching `spec-graph-adapters.md` remains unverified. **[open]**
- Whether Graph's context projector is the only context projection path used by FlowMind/agents should be traced in a later packet. **[open]**
