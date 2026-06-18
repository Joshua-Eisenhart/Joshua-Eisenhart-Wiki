---
title: Runtime Module Map Start
created: 2026-06-17
updated: 2026-06-17
type: runtime-map
status: wave-1 starter
claim_ceiling: starter implementation map from package manifests and selected entrypoints only
owner: runtime-map-worker
---

# Runtime Module Map Start

## Scope and support labels

This page is a starter runtime/module map for the current Leviathan repo. It is based only on package manifests, root workspace files, root READMEs where present, and selected entrypoint files listed below. It is **not** a full implementation proof.

Support labels used here:

- `observed file` — directly visible in a source file read for this pass.
- `inferred from package contract` — inferred from `package.json` metadata, exports, dependencies, bins, or scripts.
- `inferred architecture` — module-boundary interpretation consistent with the repo architecture notes and entrypoint contracts, but not exhaustively proven.
- `not checked` — outside this worker's bounded read.
- `open` — contradiction, missing source, or needs follow-up.

Boundary rules preserved for this starter map:

- FlowMind does not dispatch. It declares/compiles/executes within its control contract, but dispatch/scheduling is not assigned to FlowMind here. (`inferred architecture`)
- Orchestration does not mutate policy. It applies scheduling/queue/loop/stage mechanics around supplied policy/config contracts. (`inferred architecture`)
- Graph does not schedule. It composes/project/entities/events and may expose bridge glue, but scheduling belongs to orchestration. (`inferred architecture`)
- Event Bus connects lifecycle boundaries as the event spine and persistence/replay surface. (`inferred from package contract`)

## Sources read

Project/wiki sources:

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/worker-swarm-plan-2026-06-17.md`

Repo workspace sources:

- `/Users/joshuaeisenhart/GitHub/leviathan/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml`

Core package sources read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/README.md`

Readme/index existence notes:

- Root README found and read for `core/event-bus`, `core/poly`, and `core/domain`. (`observed file`)
- Root README was not found during file listing for `core/flowmind`, `core/orchestration`, `core/graph`, `core/exec`, or `core/daemon`. (`observed file`)
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/index.ts` was not found; package root export points to `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts`. (`observed file`)

## Workspace topology

| Area | Observed contract | Support |
|---|---|---|
| Root package | `/Users/joshuaeisenhart/GitHub/leviathan/package.json` defines private root package `@lev-os/root`, `type: module`, root bin `lev` -> `./core/poly/bin/lev`, and workspaces `core/*`, `packages/*`, `plugins/*`, `tooling/*`. | `observed file` |
| Workspace file | `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml` includes `core/*`, `packages/*`, `apps/*`, `apps/*/web`, desktop internals, `tooling/*`, `plugins/*`, and `context/schema`, with archive/known-missing exclusions. | `observed file` |
| Build/test spine | Root scripts include `build:poly`, `build:turbo`, `build:binaries`, `test:guard:flowmind-scheduler`, `test:guard:runtime-routing`, `test:plugins`, `test:exec:integration`, prompt-stack tests, CLI surface checks, and e2e suites. | `observed file` |
| Routing guard | Root `test:guard:flowmind-scheduler` fails if `flowmind-scheduler` appears in runtime code paths under `core`, `plugins`, `tests`, or `tooling`. | `observed file`; supports the FlowMind-not-dispatching boundary only narrowly |

## Core runtime/module table

| Plane / module | Package path | Package name | Entrypoint(s) read | Package contract | Key exports/signals observed | Dependencies observed | Boundary note | Status notes |
|---|---|---|---|---|---|---|---|---|
| Shared domain contracts | `/Users/joshuaeisenhart/GitHub/leviathan/core/domain` | `@lev-os/domain` | `package.json`, `src/index.ts`, `README.md` | Pure TypeScript domain objects, routing and manifest management. | `Route`, `Target`, `ActionTarget`, `ActionRegistry`, `FractalOwner`, `FractalEntry`, `Manifest`, `LevStatus`, event-source/DOR/validation/harness/daemon/cron/hooks/usage/execution-protocol contracts, execution-contract types, protocol adapters. | Package has no runtime dependencies listed; dev dep TypeScript only. | Domain is the shared contract layer rather than execution/scheduling/event persistence. (`inferred from package contract`) | README explicitly says pure TypeScript with no I/O dependencies. (`observed file`) |
| Flow/control declarations | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind` | `@lev-os/flowmind` | `package.json`, `src/index.ts` | FlowMind compiler: YAML IR to executable targets: smartdown, openprose, system prompt, prompt gen, schedule, hooks. | Parser, compiler, target compilers, schema/types, `GraphFlowExecutor`, session manager, router, transpiler, decompiler, memory compiler, tiered executor, AI provider, tool registry, kernel exports, intent compiler, run/review surfaces. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/logger`, `yaml`, `zod`. | Control/policy declarations and compilation; not the scheduler/dispatcher owner. (`inferred architecture`) | Local execution-contract re-exports are marked deprecated copies; canonical home noted as orchestration. (`observed file`) |
| Orchestration / scheduling / worker coordination | `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration` | `@lev-os/orchestration` | `package.json`, `src/index.ts` | Deterministic orchestration APIs for workflow DAG and epic wave execution. | Queue exports, loop/iteration orchestration, scheduler strategies, status bridge, entities pipeline, `resolveStageExecutionPolicy`, `applyStagePolicyToEpicOptions`, `graph(...)`, worktree helpers in entrypoint. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/flowmind`, `@lev-os/logger`. | Applies scheduling/queue/loop execution strategy; does not own policy mutation in this map. (`inferred architecture`) | Entrypoint is large and includes worktree/epic execution code; full behavior not checked. (`not checked`) |
| Entity graph / context projection | `/Users/joshuaeisenhart/GitHub/leviathan/core/graph` | `@lev-os/graph` | `package.json`, `src/index.ts` | Entity graph compositor: classify -> validate -> apply with pluggable adapters. | `EntityGraph`, graph types, `createLevEvent`, classify policy/types, temperature classifier, `ContextProjector`, `InMemoryGraphAdapter`, `JsonlEventStore`, bridge exports including `FlowRegistry`, `TriggerDispatcher`, `HookRegistry`. | `@lev-os/config`, `@lev-os/domain`. | Graph composes/project entities/events; does not schedule runtime work. Bridge exports are connection glue, not proof of scheduler ownership. (`inferred architecture`) | Entry comment says 4-step pipeline extract -> classify -> validate -> apply; package description says 3-step classify -> validate -> apply. Needs reconciliation. (`open`) |
| Event spine / lifecycle bus | `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus` | `@lev-os/event-bus` | `package.json`, `src/index.ts`, `README.md` | Canonical event bus runtime for Leviathan; package metadata says persistence and replay. | Domain event factories/types, `EventBus`, JSONL persistence, LevEvent persistence, context factories, runtime exports, aggregates, guards/actions, frontmatter, policy, bridge types, workflow loader. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/logger`, `xstate`, `zod`, `js-yaml`. | Connects lifecycle boundaries; execution adapters moved out to `@lev-os/exec`. (`observed file`) | `src/index.ts` contains unresolved Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), making current entrypoint integrity an open blocker. README status appears older than current exports. (`open`) |
| Execution SDK / adapter contract | `/Users/joshuaeisenhart/GitHub/leviathan/core/exec` | `@lev-os/exec` | `package.json`, `src/index.ts` | SDK-first canonical execution contract for CLI/MCP/poly surfaces. | `createExec(dispatch, opts)`, `ExecEngine`, provider semaphore, safe event emission for `exec.started/completed/failed/backpressure`, CLI/MCP/OpenCode adapters. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/logger`. | Execution is a factory-bound service; no module-level global engine state in entrypoint. (`observed file`) | Event emission is best-effort and should not break execution. (`observed file`) |
| Poly / CLI and cross-language runtime surface | `/Users/joshuaeisenhart/GitHub/leviathan/core/poly` | `@lev-os/poly` | `package.json`, `src/sdk/index.ts`, `README.md` | Poly registry system and root `lev` bin; unified runner registry for binaries, daemons, SDK commands. | `executeHandler`, `call`, `poly`, `runExecutionRequest`, transport registration into domain, handler protocols `bin:`, `grpc:`, `http(s):`, registry-backed daemon/binary routing. | `@lev-os/config`, `@lev-os/exec`, `@lev-os/daemon`, `@lev-os/domain`, `@lev-os/index`, `@lev-os/ui-renderers`, `@lev-os/event-bus`, `@lev-os/logger`, plus YAML/logging deps. | Poly is the runtime surface/binding layer; package root export is SDK entrypoint, not `src/index.ts`. (`observed file`) | README claims production-ready / 144 passing tests; not verified by test execution in this worker. (`not checked`) |
| Daemon runtime library | `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon` | `@lev-os/daemon` | `package.json`, `src/index.ts` | Daemon runtime library: lifecycle, supervision, health monitoring, task execution/scheduling. | `DaemonCore`, `QueueManager`, worker pools, process supervisor, dependency resolution, health monitor, adapters, PMDaemon adapter/commands, plugin manifest discovery, CLI lifecycle, orchestrator integration. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/logger`. | Daemon owns process supervision and daemon-side task surfaces; poly routes, daemon implements. (`observed file`) | Entrypoint says LevEvent I/O is intentionally not re-exported and canonical event I/O lives in event-bus. (`observed file`) |

## Starter runtime flow sketch

```text
User / CLI / SDK surface
  -> core/poly (`lev` bin, SDK request bridge, provider registry)
  -> core/exec (factory execution contract, provider semaphore, exec events)
  -> adapters / daemon / external providers

Intent / policy / control declaration
  -> core/flowmind (IR, parser/compiler, targets, graph/session execution surfaces)
  -> core/orchestration (DAG, queues, loop/iteration, stage/epic execution strategy)

Lifecycle / state / memory spine
  -> core/event-bus (domain/lifecycle events, persistence/replay, policy/frontmatter/bridge)
  -> core/graph (entity graph compositor, adapters, projections, event bridge)

Shared contracts under everything
  -> core/domain (routes, targets, actions, status, protocol and execution types)
```

Support: `inferred architecture` from the package contracts and selected entrypoints. This sketch needs validation against full code paths and tests.

## Cross-module observations

1. `@lev-os/domain` is the lowest-dependency shared contract layer among the read packages. (`observed file`)
2. `@lev-os/exec` uses `@lev-os/event-bus/events` to emit LevEvents for execution lifecycle, but event emission is best-effort. (`observed file`)
3. `@lev-os/poly` depends on `@lev-os/exec` but lazy-imports `createExec` to break the poly <-> exec cycle, then registers an execution transport in `@lev-os/domain`. (`observed file`)
4. `@lev-os/daemon` depends on event-bus but explicitly does not re-export canonical event I/O from its public barrel. (`observed file`)
5. `@lev-os/orchestration` depends on FlowMind and re-exports canonical execution-contract surfaces; FlowMind's local execution-contract barrel says its copy is deprecated and canonical home is orchestration. (`observed file`)
6. `@lev-os/graph` package dependencies do not include event-bus, but the entrypoint exposes event bridge types/classes and `JsonlEventStore`; exact runtime coupling needs follow-up. (`open`)
7. `@lev-os/event-bus/src/index.ts` currently contains unresolved merge conflict markers in the read copy. This is a high-priority blocker for treating that barrel as buildable. (`observed file`)

## Open questions

- Does the repo currently build with unresolved conflict markers in `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`? (`open`)
- Which package is the canonical home for the `LevEvent` type at runtime: `@lev-os/domain`, `@lev-os/event-bus/events`, graph's re-export, or multiple intentionally layered homes? (`open`)
- Is `core/poly/README.md` still current after package-root export changes to `src/sdk/index.ts` and registry build/runtime changes? (`open`)
- What is the active boundary between `core/event-bus` policy exports and orchestration stage policy application? (`open`)
- Is `GraphFlowExecutor` in FlowMind runtime execution, test harness, or production execution surface? Starter read did not inspect implementation. (`not checked`)
- Are `graph` bridge exports intended as active dispatch glue or compatibility/test surfaces? (`open`)

## Next read queue

1. `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` and `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md` for architecture/controller verification.
2. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/index.ts` and `src/events/lev-event-persistence.ts` for canonical LevEvent persistence details.
3. `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/src/event-source.ts`, `src/action.ts`, `src/execution-protocol.ts`, and `src/exec-events.ts` for cross-module contracts.
4. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/execution-contract/index.ts`, `src/graph/scheduler.ts`, and `src/queue/index.ts` for canonical scheduling/execution contract.
5. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/executor.ts`, `src/run.ts`, `src/router/index.ts`, and `src/kernel/index.ts` for FlowMind control/execution split.
6. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts`, `src/bridge/index.ts`, and `src/context/index.ts` for graph/event bridge behavior.
7. `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/bin/lev`, `src/surfaces/cli/index.ts`, and `src/commands/index.ts` for CLI runtime routing.
8. `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/core.ts`, `src/cli-lifecycle.ts`, and `src/orchestrator-integration.ts` for daemon/process runtime details.
