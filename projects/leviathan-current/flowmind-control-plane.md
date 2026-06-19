---
title: FlowMind Control Plane
date: 2026-06-17
packet: 2
status: current-runtime-map
claim_ceiling: historical Packet 2 source map with current-source caveats; not current build proof; not runtime health proof
owned_by: background-packet-2
---

# FlowMind Control Plane

## Evidence and status labels

Major claims below are tagged with one of: **[observed file]**, **[inferred from package/code]**, **[inferred from docs]**, **[roadmap/design intent]**, **[open]**, **[not checked]**.

Primary sources read for this page:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-flowmind.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-orchestration.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/schema.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/compiler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/executor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/session.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/run.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/router.policy.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-loader.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-executor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/actor-kernel.ts`

Related starter page incorporated by reference: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/flowmind-control-plane-start.md`.

## Boundary summary

FlowMind is the **control/policy plane** for Leviathan: it owns declaration, schema validation, compile-time policy/gates, system FlowMind loading, progressive-disclosure sessions, and runtime policy decisions expressed as FlowMind programs. **[inferred from docs]** The architecture doc states that FlowMind drives agents, workflows, policies, and harness configs as declarations, while preserving the hard plane boundary that FlowMind does not dispatch workers or own retry/concurrency loops. **[inferred from docs]**

The implementation surface is the package `@lev-os/flowmind`, exported from `core/flowmind/package.json`. **[observed file]** The package describes itself as a FlowMind compiler from YAML IR to executable targets, exposes `.` plus subpaths `./kernel`, `./cli`, `./memory-compiler`, and `./commands/flowmind`, and depends on `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/config`, `@lev-os/logger`, `yaml`, and `zod`. **[observed file]**

## What FlowMind owns

| Concern | Status | Evidence |
|---|---:|---|
| FlowMind schema, declarations, node/edge/graph types, validation types | **[observed file]** | `core/flowmind/src/schema.ts` |
| Compilation of FlowMind programs into graph/target representations | **[observed file]** | `core/flowmind/src/compiler.ts` |
| GraphFlow execution adapter layer for executing a compiled graph as steps | **[observed file]** | `core/flowmind/src/executor.ts` |
| Progressive-disclosure session state and persistence | **[observed file]** | `core/flowmind/src/session.ts` |
| CLI/file runner entrypoint for FlowMind programs | **[observed file]** | `core/flowmind/src/run.ts`, package `bin.flowmind` |
| Router policy matching and model/provider/capability policy | **[observed file]** | `core/flowmind/src/router.policy.ts` |
| System FlowMind loading/execution for kernel policy | **[observed file]** | `core/flowmind/src/kernel/system-flowmind-loader.ts`, `system-flowmind-executor.ts`, `actor-kernel.ts` |
| Cross-plane runtime scheduling, worker dispatch, retry loops, concurrency ownership | **[inferred from docs]** / **not owned** | `docs/ARCHITECTURE.md`, orchestration sources |

## Public package and runtime entrypoints

- `@lev-os/flowmind` main export: package-level runtime API. **[observed file]**
- `@lev-os/flowmind/kernel`: system FlowMind kernel-facing API. **[observed file]**
- `@lev-os/flowmind/cli` and `flowmind` binary: command/runtime invocation surface. **[observed file]**
- `@lev-os/flowmind/memory-compiler`: memory compiler subpath is exposed by package metadata but not deep-read in this packet. **[observed file]**, **[not checked]**
- `@lev-os/flowmind/commands/flowmind`: command integration surface. **[observed file]**, **[not checked]**

## Internal module map

### Schema and declarations

`schema.ts` is a large schema/type owner for FlowMind declarations. **[observed file]** It defines the control-plane data shapes consumed by compiler/runtime components; it is the primary source of truth for accepted declaration structure at implementation level. **[inferred from package/code]** The docs describe FlowMind as YAML IR and as a YAML superset used for agents, workflows, policies, hooks, and schedules. **[inferred from docs]**

### Compiler

`compiler.ts` implements the compiler boundary. **[observed file]** The compiler converts declarative FlowMind inputs into internal graph/target structures, preserving FlowMind's role as the planner/control layer rather than a process runner. **[inferred from package/code]** This aligns with the architecture invariant that FlowMind compiles `.flow.yaml` into a graph/intent IR and hands execution intent to orchestration. **[inferred from docs]**

### Executor and run surface

`executor.ts` provides a GraphFlow execution implementation and is a substantial runtime file. **[observed file]** Its presence means FlowMind does have an implementation for stepping through compiled graph logic, but the architecture boundary still treats retry/concurrency/worker dispatch as orchestration-owned. **[inferred from docs]** The safe current-map wording is: FlowMind can execute its own declaration/step semantics, but runtime process/work scheduling is not FlowMind's ownership boundary. **[inferred from docs]**

`run.ts` is the lightweight run entrypoint read in this packet. **[observed file]** Package metadata also declares the `flowmind` binary through `dist/cli.js`. **[observed file]** Full CLI behavior was not exhaustively tested. **[not checked]**

### Session engine

`session.ts` implements `FlowmindSessionManager` and progressive-disclosure session behavior. **[observed file]** The architecture doc states the lifecycle as `start(program) -> paused -> get(step) -> next(execute) -> paused -> ... -> completed`, with state persisted under `XDG_STATE_HOME/lev/flowmind/sessions/<id>.json`. **[inferred from docs]** The implementation file was read as source support for FlowMind owning this session manager boundary. **[observed file]**

Important boundary: session progression chooses **which step** to run; orchestration's iterative runner owns **how** execution is retried/budgeted/adapted. **[inferred from docs]**

### Router policy

`router.policy.ts` is a separate policy surface for routing/model/provider policy. **[observed file]** Packet 2 treats this as FlowMind-owned policy because it is in the FlowMind package and supports the control-plane function of expressing routing constraints. **[inferred from package/code]** Exhaustive rule semantics were not validated by tests. **[not checked]**

### Kernel/system FlowMinds

`kernel/index.ts` exports system FlowMind pieces. **[observed file]** `system-flowmind-loader.ts`, `system-flowmind-executor.ts`, and `actor-kernel.ts` implement the kernel-facing runtime for loading and executing system FlowMind declarations. **[observed file]** This matches the architecture principle that system FlowMinds govern the kernel and that constraints/policies/provenance should be declarations rather than hard-coded imperative policy. **[inferred from docs]**

## Cross-plane relationships

| To plane/module | FlowMind role | Other owner role | Status |
|---|---|---|---:|
| Orchestration | Produces compiled intent/declarations; controls policy; session chooses next step | Owns DAG scheduling, iterative loops, retries, worker dispatch | **[inferred from docs]** + orchestration files read |
| Graph | Uses graph concepts/IR and context; does not own graph persistence/traversal | Owns state/knowledge graph lifecycle and projection | **[inferred from docs]** |
| Event Bus | Emits/consumes canonical runtime events where lifecycle crosses boundaries | Owns causality spine, persistence, replay/checkpointing | **[inferred from docs]**; event-bus health blocked by conflicts |
| Exec | Selects/declares execution profiles/policy in FlowMind configs | Owns execution engine/provider dispatch contract | **[inferred from docs]** + exec package read |
| Poly | FlowMind command/SDK surfaces can be exposed through poly | Poly owns CLI/MCP/registry/binder surfaces | **[inferred from docs]** + poly package read |

## Current invariants to preserve

1. FlowMind is declaration/control/policy-first, not a process supervisor. **[inferred from docs]**
2. FlowMind sessions are the canonical progressive-disclosure session engine; prompt-stack is backward-compatible legacy/plugin surface for older stacks. **[inferred from docs]**
3. Runtime state should use XDG paths, including FlowMind session persistence. **[inferred from docs]**
4. FlowMind may interact with the event bus, but runtime health still requires current event/daemon proof rather than old Packet 2 source-map evidence. **[open]**
5. FlowMind's package exports should remain aligned with package metadata and with the hard-cut module map. **[observed file]**

## Not checked in this packet

- Full FlowMind test suite or `tsc` typecheck. **[not checked]**
- Full `src/index.ts`, `src/cli.ts`, memory compiler sub-tree, and all 95 FlowMind TypeScript files. **[not checked]**
- Runtime CLI smoke. **[not checked]**
- Secret scan beyond not retaining any encountered secrets; no secrets were copied into this page. **[not checked]**

## Open questions

- Whether `executor.ts` currently crosses any boundary that docs intend orchestration to own should be validated with focused source review and tests. **[open]**
- Whether all FlowMind programs discovered through config-inline and file-based mechanisms are compiled through the same compiler path should be tested. **[open]**
- Whether all FlowMind lifecycle events are canonical `LevEvent` and include correlation IDs should wait until event-bus conflicts are resolved. **[open]**
