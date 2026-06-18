---
title: Event Graph Orchestration Start
created: 2026-06-17
updated: 2026-06-17
type: module-map
status: wave-1 starter
claim_ceiling: starter interaction map from manifests and selected barrels only
owner: runtime-map-worker
---

# Event Graph Orchestration Start

> Supersession note, 2026-06-18: this is an earlier starter map. For current upstream truth, begin with [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]] and the split full pages, especially [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]].

## Scope

This page maps the first-pass relationship among Event Bus, Graph, and Orchestration in current Leviathan. It uses only package manifests, selected public entrypoints, and root READMEs where present. It is not a full implementation audit.

Support labels:

- `observed file` — directly visible in files read.
- `inferred from package contract` — inferred from package metadata/exports/dependencies.
- `inferred architecture` — boundary interpretation consistent with repo module separation but not exhaustively proven.
- `not checked` — implementation not read in this pass.
- `open` — contradiction, unresolved code state, or needs follow-up.

Boundary rules for this page:

- **Event Bus connects lifecycle boundaries.** It is the event spine/persistence/replay/policy/frontmatter/lifecycle bridge surface. (`inferred from package contract`)
- **Graph does not schedule.** It composes entity graph state/context/projections and exposes bridge glue; scheduling remains orchestration. (`inferred architecture`)
- **Orchestration does not mutate policy.** It resolves/applies execution strategy and queue/loop/stage mechanics around policies/config, but policy ownership is not assigned to orchestration here. (`inferred architecture`)
- **FlowMind does not dispatch.** It is adjacent because orchestration depends on FlowMind and FlowMind's deprecated execution-contract copy points back to orchestration as canonical. (`observed file`; `inferred architecture`)

## Sources read

Project/wiki sources:

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/worker-swarm-plan-2026-06-17.md`

Repo/workspace sources:

- `/Users/joshuaeisenhart/GitHub/leviathan/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml`

Module sources:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/src/index.ts`

Readme existence notes:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/README.md` exists and was read. (`observed file`)
- No root README was found during bounded listing for `core/graph` or `core/orchestration`. (`observed file`)

## Module contracts at a glance

| Module | Package path | Package contract | Main public barrel signals | Dependencies observed | Boundary placement | Support |
|---|---|---|---|---|---|---|
| Event Bus | `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus` | `@lev-os/event-bus`; canonical event bus runtime for Leviathan; metadata says canonical runtime event spine with persistence and replay. | Domain events, `EventBus`, JSONL persistence, LevEvent persistence, runtime exports, context factories, aggregates, frontmatter, policy, bridge types, workflow loader. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/logger`, `xstate`, `zod`, `js-yaml`. | Lifecycle/event boundary connector; not execution adapter owner. | `observed file`; `inferred from package contract` |
| Graph | `/Users/joshuaeisenhart/GitHub/leviathan/core/graph` | `@lev-os/graph`; entity graph compositor with pluggable adapters. | `EntityGraph`, core graph/event types, `createLevEvent`, classify policy, temperature classifier, `ContextProjector`, `InMemoryGraphAdapter`, `JsonlEventStore`, bridge exports (`FlowRegistry`, `TriggerDispatcher`, `HookRegistry`). | `@lev-os/config`, `@lev-os/domain`. | Entity/context/projection/composition; not scheduler. | `observed file`; `inferred architecture` |
| Orchestration | `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration` | `@lev-os/orchestration`; deterministic orchestration APIs for workflow DAG and epic wave execution. | Queue, loop/iteration, scheduler strategies, status bridge, entity orchestration, stage policy resolution/application, `graph(...)`, worktree/epic execution helpers. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/flowmind`, `@lev-os/logger`. | Scheduling, queueing, DAG/loop/worker strategy; not policy mutation owner. | `observed file`; `inferred architecture` |
| FlowMind adjacency | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind` | `@lev-os/flowmind`; YAML IR compiler to targets. | Exports deprecated execution-contract copy and says canonical home is orchestration; exports graph executor/session/compiler/router/intent surfaces. | `@lev-os/config`, `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/logger`, `yaml`, `zod`. | Control-plane declaration/compilation, not dispatch owner. | `observed file`; `inferred architecture` |
| Domain substrate | `/Users/joshuaeisenhart/GitHub/leviathan/core/domain` | `@lev-os/domain`; pure domain objects and shared contracts. | Route/Target/Action/Manifest/status/event-source/DOR/validation/harness/cron/hooks/usage/execution-protocol/execution-contract types/protocol adapters. | No runtime dependencies listed. | Shared contracts below event/graph/orchestration. | `observed file` |

## Event Bus starter map

| Surface | Observed export/README signal | Starter interpretation | Support |
|---|---|---|---|
| Domain events | `DomainEvent`, aggregate/event metadata, idea/session/synth/SCM/common event types, `createDomainEvent`, `isDomainEvent` | Typed event vocabulary for lifecycle/domain changes. | `observed file` |
| Event bus | `EventBus`, `getEventBus`, `resetEventBus`, `matchPattern`, `createLifecycleEvent`, event filter/callback/persistence types | Runtime in-process/event subscription and lifecycle event API. | `observed file`; exact implementation not checked |
| Persistence | `JsonlPersistence`, `createJsonlPersistence`, `emitLevEvent` | JSONL and LevEvent persistence surface. | `observed file`; exact schema path not checked |
| Runtime | `export * from './runtime/index.js'` | Runtime checkpoint/recovery/hooks/queue surface exists. | `observed file`; implementation not checked |
| Context factories | `createIdeaContext`, `createSessionContext`, `createSynthContext`, `createPRContext` | Builds lifecycle context objects for entities/sessions/synth/PR. | `observed file` |
| Aggregates | Idea/session/synth/PR aggregate types and factories where exported | DDD aggregate/lifecycle machine facade. | `observed file`; source conflict affects exact values |
| Frontmatter | extract/create/update frontmatter, defaults, manager | File/frontmatter state bridge. | `observed file` |
| Policy | policy schemas/default/load/get functions, promotion/handler/action mapping types | Policy definition/loading surface in event-bus package. | `observed file`; policy mutation behavior not checked |
| Bridge | Footer/entity/escalation/SCM bridge types; barrel says value exports pruned and subpath should be used directly when needed | Event boundary adapter/bridge surface. | `observed file` |
| Workflow loader | workflow/stage/gate loader/evaluator functions | Workflow definition loading/validation/gate evaluation surface. | `observed file` |
| Execution adapters moved out | Barrel comments say CLI/MCP adapters moved to `@lev-os/exec/adapters`; event-bus is transport, not execution. | Supports separation of event transport from execution. | `observed file` |

### Event Bus integrity warning

`/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts` contains unresolved Git conflict markers around SCM event exports, Synth aggregate export, PR lifecycle exports, and SCM bridge exports. This makes the entrypoint's exact current buildability and export set an `open` blocker until verified or fixed by repo owners.

Support: `observed file`.

The README also says “Phase 1: Design — Complete” and Phase 2/3/4 pending, while the package/entrypoint now expose many runtime/persistence/aggregate/policy surfaces. This may be stale documentation or partial implementation drift. (`open`)

## Graph starter map

| Surface | Observed export/comment | Starter interpretation | Support |
|---|---|---|---|
| Compositor | `EntityGraph` from `./compositor.js`; entry comment says entity graph compositor | Central graph processing object. | `observed file` |
| Pipeline claim | Entry comment says “4-step pipeline: extract -> classify -> validate -> apply”; package description says “classify -> validate -> apply” | There is a minor contract wording mismatch requiring follow-up. | `open` |
| Core graph types | `Claim`, `Entity`, `EventStore`, `GraphAdapter`, `GraphEvent`, `GraphOperation`, `GraphReader`, `LevEvent`, `ValidationHook`, etc. | Graph-level contracts for entities, evidence, operations, validation. | `observed file` |
| LevEvent factory | `createLevEvent` re-exported from graph types/comment says from `@lev-os/domain` | Graph uses or exposes canonical event creation but exact canonical type source should be checked. | `observed file`; `open` |
| Classifier | `defaultClassify`, classify policy/rule/action types, temperature scoring classifier | Entity classification policy/scoring surface. | `observed file` |
| Context projector | `ContextProjector`, projector config, context projection, token budget/zoom | Context assembly/projection from graph state. | `observed file` |
| Adapters | `InMemoryGraphAdapter`, `JsonlEventStore` | Adapter/event store implementations exposed. | `observed file` |
| Event bridge | `createEventBridge`, event adapter normalizers, `FlowRegistry`, `TriggerDispatcher`, `HookRegistry`, schema validation hook | Graph can bridge events/flows/hooks, but this is not scheduling ownership in this starter map. | `observed file`; `inferred architecture` |

### Graph boundary note

The export name `TriggerDispatcher` can sound like scheduling/dispatch ownership. In this starter map it is treated as bridge glue for routing event/flow interactions, not as proof that Graph schedules runtime work. The implementation files were not read, so this remains `open` pending `core/graph/src/bridge/*` inspection.

## Orchestration starter map

| Surface | Observed export/comment | Starter interpretation | Support |
|---|---|---|---|
| Package role | Description: deterministic orchestration APIs for workflow DAG and epic wave execution. | Orchestration owns scheduling/coordination strategy. | `observed file` |
| Queue | `InMemoryTaskQueue`, `DurableTaskQueue`, `JSONLStore`, `SlowTaskRouter`, queue record/status/priority/worker types | Task queue layer and slow-task routing. | `observed file` |
| Loop/iteration | compile/execute until loops, iterative runner, idle/completion detection, token usage/context pressure, heartbeat FSM, tick provider, session writer | Runtime loop/iteration orchestration and convergence mechanics. | `observed file` |
| Scheduler strategies | `SchedulerRegistry`, `TopoSortScheduler`, `CriticalPathScheduler`, `RuntimeDynamicScheduler` | DAG/task scheduling strategies. | `observed file` |
| Status bridge | `isTerminalSuccess`, `isTerminalFailure`, `isTerminal`; comment says replacement with unified status model is planned | Temporary status compatibility surface. | `observed file`; roadmap detail not checked |
| Entity loop orchestration | `export * from './entities/index.js'` | Entity pipeline/loop orchestration surface. | `observed file`; implementation not checked |
| Stage policy resolution/application | `DEFAULT_STAGE_POLICIES`, `resolveStageExecutionPolicy`, `applyStagePolicyToEpicOptions` | Applies default/override execution knobs like concurrency/maxIterations/stopOnFailure/budget/scope to options. | `observed file` |
| Workflow graph execution | `graph(workflow, opts)` begins by constructing session/node status/workdir/exec options | Public DAG execution function. | `observed file`; full function not read in this pass |
| Worktree support | Entry code includes worktree config/creation/commit/squash/cleanup helpers for epic task execution | Orchestration can coordinate isolated worktree execution. | `observed file`; full path not checked |
| Execution contract | Package exports `./execution-contract` subpath; FlowMind comments name this as canonical home | Canonical execution-contract layer relative to FlowMind. | `observed file` |

### Orchestration boundary note

`resolveStageExecutionPolicy` and `applyStagePolicyToEpicOptions` merge and apply stage execution policy defaults/overrides to orchestration options. This is mapped as policy application, not policy mutation. The event-bus package owns policy schemas/loading in its public barrel; exact cross-package policy ownership needs follow-up. (`observed file`; `inferred architecture`; `open`)

## Starter interaction sketch

```text
Lifecycle and audit events
  Event Bus
    - event vocabulary
    - EventBus pub/sub
    - JSONL / LevEvent persistence
    - frontmatter / policy / workflow-loader / bridge surfaces

Entity/context state
  Graph
    - EntityGraph compositor
    - classify / validate / apply pipeline
    - context projector
    - adapters and JSONL event store
    - event/flow/hook bridge glue

Scheduling and execution strategy
  Orchestration
    - DAG graph execution
    - queues and slow-task routing
    - loop/iteration/heartbeat/tick providers
    - scheduler strategies
    - stage/epic options and worktree coordination

Control declarations beside these
  FlowMind
    - graph/control document, parser/compiler/targets
    - execution/session/review surfaces
    - deprecated local execution-contract copy; canonical copy in orchestration

Shared contracts
  Domain
    - routes/targets/actions/status/protocols/execution types
```

Support: `inferred architecture` from package contracts and public barrels.

## Dependency observations

| Observation | Support |
|---|---|
| Event Bus depends on Domain, Config, Logger, XState, Zod, and JS-YAML. | `observed file` |
| Graph depends only on Domain and Config among internal runtime modules read; it does not list Event Bus as a package dependency. | `observed file` |
| Orchestration depends on FlowMind, Domain, Config, and Logger, but not Event Bus in package manifest. | `observed file` |
| FlowMind depends on Event Bus and Domain, while also saying its local execution-contract copy cannot depend on orchestration because orchestration depends on FlowMind. | `observed file` |
| Exec/Daemon are outside this page's main triad, but both depend on Event Bus for event I/O/lifecycle integration in their package manifests. | `observed file` from runtime map pass |

## Claims with support labels

- Event Bus is the strongest candidate for the canonical lifecycle/event spine from package metadata and public exports. (`inferred from package contract`)
- Graph is an entity graph compositor with adapters, classification, validation, context projection, and event bridge glue. (`observed file`)
- Orchestration is the scheduling/coordination package for DAGs, queues, loops, heartbeats, stage policies, and epic/worktree execution. (`observed file`)
- Graph's bridge exports should not be read as graph owning scheduling until bridge implementations are checked. (`inferred architecture`; `not checked`)
- Orchestration's stage policy helpers apply policy-shaped execution knobs but do not prove orchestration owns or mutates policy definitions. (`observed file`; `inferred architecture`)
- Event Bus barrel integrity is currently blocked by unresolved merge conflict markers. (`observed file`; `open`)

## Open questions

1. Does `core/event-bus/src/index.ts` currently parse/build despite conflict markers? If not, what active import paths avoid it? (`open`)
2. Where is the canonical `LevEvent` schema/type source: Domain, Event Bus events, Graph types, or layered aliases? (`open`)
3. Why does Graph expose `JsonlEventStore` and event bridge surfaces without listing Event Bus as a dependency? Is the bridge generic, type-only, or using compatible local contracts? (`open`)
4. How do Event Bus policy exports relate to Orchestration stage policies and FlowMind safety/control declarations? (`open`)
5. Is Event Bus README stale relative to current source exports, or are many exports still stubs/design surfaces? (`open`)
6. What is the active runtime route from an emitted `LevEvent` to Graph processing to FlowMind trigger execution, if any? (`open`)
7. Which orchestration execution paths are current: DAG `graph(...)`, entities pipeline, a2a dispatcher, queue router, loop runner, epic/worktree helpers? (`open`)

## Next read queue

Event Bus:

1. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/index.ts`
2. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/lev-event-persistence.ts`
3. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/runtime/index.ts`
4. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/policy/index.ts`
5. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/bridge/index.ts`
6. `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/DESIGN.md`

Graph:

1. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts`
2. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/types.ts`
3. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/events/index.ts`
4. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/bridge/index.ts`
5. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/bridge/trigger-dispatcher.ts`
6. `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/context/index.ts`

Orchestration:

1. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/types.ts`
2. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/index.ts`
3. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts`
4. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/queue/index.ts`
5. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/loop/index.ts`
6. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/entities/index.ts`
7. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/a2a/index.ts`
8. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/execution-contract/index.ts`
