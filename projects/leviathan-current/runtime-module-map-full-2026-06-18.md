---
title: Runtime Module Map Full — 2026-06-18
created: 2026-06-18
updated: 2026-06-18
type: runtime-map
packet: 2-full-pass
status: current snapshot with blockers
claim_ceiling: implementation/runtime map from selected code, manifests, docs, inventory commands; not package health; not maintainer acceptance
repo_snapshot:
  path: /Users/joshuaeisenhart/GitHub/leviathan
  head: a661ecbf410469becd7b89c3bfc5ee215721ae34
  remote: https://github.com/lev-os/leviathan.git
---

# Runtime Module Map Full — 2026-06-18

> Supersession note, 2026-06-18: this page is still useful as a module map, but its dirty-checkout and conflict-marker blockers came from the deleted damaged local checkout at `a661ecbf...`. For current upstream truth, read [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]], [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]], and [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]. The clean snapshot at `c90ec8499c83db3d17f6132ec734698a8de2dbce` was clean and had no `<<<<<<<`/`>>>>>>>` scan hits. Also note current workspace drift: `pnpm-workspace.yaml` includes `core/context-graph`, `core/reconciler`, `core/world-model`, `core/graph-algorithms`, and `plugins/sim-eval`; old `core/graph`, `plugins/core-sdlc`, and `crates/levd` claims need a future line-by-line rewrite. Runtime health is now mixed rather than merely unproven by omission: Packet 7/8 found named SDK/Poly proof green while default daemon Pentagon, `@lev-os/testing`, and event-dispatch proof-spine remain red or blocked.

## Claim labels

- **[observed implementation]** — directly read in current repo files or command output during this pass.
- **[contract/docs intent]** — documented in current docs/specs/manifest descriptions, not runtime-proven here.
- **[broken/conflict marker]** — source contains unresolved merge markers or command failed; do not treat the marked source as truth.
- **[tests not run]** — no package test/typecheck/build executed in this wiki pass.
- **[open gap]** — needs follow-up source tracing or command verification.
- **[advisory pressure]** — Fusion/GLM model pressure used only to shape wiki direction, not as evidence.

## Snapshot and repo state

Command run from `/Users/joshuaeisenhart/GitHub/leviathan`:

```bash
git rev-parse HEAD && git remote get-url origin && git status --short && git submodule status
```

Observed output began:

```text
a661ecbf410469becd7b89c3bfc5ee215721ae34
https://github.com/lev-os/leviathan.git
 m apps/nanoclaw
 m community/agentguard
 m community/agentping
 m community/lev-content
 D docs/vernacular.md
 M plugins/prompt-stack/vendors/jeffreysprompts.com
```

The same command exited `128` because `git submodule status` reported:

```text
fatal: no submodule mapping found in .gitmodules for path 'community/clawstore-pre-reset'
```

So this snapshot is **dirty** and submodule status is partially blocked. **[observed implementation] / [broken/conflict marker]**

## Runtime bottom line

LevOS/Leviathan is implemented as a mixed TypeScript/Node monorepo plus a Rust `crates/` workspace. Current docs define the core runtime as:

```text
FlowMind -> Orchestration -> Exec/Poly/Daemon/plugins
    with Graph as state/knowledge and Event Bus as causality spine
```

This pass confirms that the corresponding packages and source surfaces exist, but it does **not** claim green runtime health. The old Event Bus/build/skills/Rust TUI conflict-marker finding belongs to the deleted damaged checkout and is superseded for current upstream truth by the clean snapshot audit. Packet 7/8 later showed a mixed runtime proof state: named SDK/Poly proof green, default daemon Pentagon red due stale mini-app artifact paths, `@lev-os/testing` red due a Vitest/Bun-condition source-entry mismatch, and event-dispatch proof-spine blocked on package import/build resolution. **[observed implementation] / [tests not run]**

## Authority sources read

Wiki/project sources read before synthesis:

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/README.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/bounded-ingestion-plan.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/model-pressure/fusion-glm-wiki-direction-2026-06-18.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/runtime-module-map-start.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/flowmind-control-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/graph-state-knowledge-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-bus-causality-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/orchestration-execution-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/exec-poly-daemon-boundary.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/plugin-ownership-map.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-2-runtime-map-receipt-2026-06-17.md`

Repo docs/manifests read:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/turbo.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/.gitmodules`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.toml`

Selected implementation files read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/session.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-loader.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/loop/iterative-runner.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/event-bus.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/core.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/commands/skills.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-domain/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-events/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/levd/Cargo.toml`

Selected plugin files read:

- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/genui-exec-daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/genui-exec-daemon/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/voice/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/voice/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-sdlc/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-sdlc/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/graph-adapters/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/evolve-memory/package.json`

Conflict-marker files specifically read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/commands/skills.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-theme/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-widgets/src/attention_kanban.rs`

## Canonical planes and current implementation surfaces

| Plane / boundary | Current implementation surface | Observed current role | Boundary discipline | Status |
|---|---|---|---|---|
| FlowMind control/policy | `core/flowmind`, package `@lev-os/flowmind` | Manifest describes compiler from YAML IR to executable targets; `session.ts` implements progressive-disclosure session persistence under XDG state; `system-flowmind-loader.ts` loads/sorts/validates system FlowMind declarations and binds native implementations. | Owns declarations, policy, session cursor, compile/control gates. Does not own worker dispatch/retry/concurrency. | **[observed implementation] + [contract/docs intent]** |
| Orchestration execution strategy | `core/orchestration`, package `@lev-os/orchestration` | Manifest exports graph/loop/queue/entities/a2a/execution-contract; `iterative-runner.ts` implements loop execution with budget/idle/circuit-breaker events; `scheduler.ts` implements topological, critical-path, and runtime-dynamic scheduling strategies. | Owns DAG scheduling, iterative loops, queues, worker strategy. Does not mutate FlowMind policy. | **[observed implementation] + [contract/docs intent]** |
| Graph state/knowledge | `core/graph`, package `@lev-os/graph` | Manifest describes entity graph compositor; `compositor.ts` implements internal extract → classify → validate → apply pipeline, reader traversal, validation hooks, graph event persistence to an `EventStore`. | Owns entity graph state, traversal, projections. Does not schedule execution. | **[observed implementation] + [contract/docs intent]** |
| Event Bus causality spine | `core/event-bus`, package `@lev-os/event-bus` | Manifest exposes event/runtime/context/aggregates/frontmatter/policy/bridge/workflow/actions/guards/types; `events/event-bus.ts` implements in-process lifecycle pub/sub and persistence hooks. | Should own canonical event transport, persistence, replay/checkpointing. | **[observed implementation] but current barrel blocked by conflict markers** |
| Exec SDK | `core/exec`, package `@lev-os/exec` | `createExec(dispatch, opts)` creates frozen `ExecEngine`; per-provider semaphore; best-effort `exec.started`, `exec.completed`, `exec.failed`, `exec.backpressure` event emission. | Owns execution request/result lifecycle, concurrency/backpressure, provider dispatch wrapper. | **[observed implementation]**, but event path depends on Event Bus health |
| Poly binder/surfaces | `core/poly`, package `@lev-os/poly` | Manifest owns `lev` binary and SDK/codegen/events/registry/plugin-validator/commands/surface subpaths; SDK dispatches `bin:`, `grpc:`, `http(s):` handler URIs and lazily imports Exec to avoid cyclic dependency. | Owns CLI/MCP/registry/binder/codegen/surface routing, not execution engine or daemon lifecycle. | **[observed implementation]** |
| Daemon runtime | `core/daemon`, package `@lev-os/daemon` | `DaemonCore` owns heartbeat, polling, QueueManager integration, project events, BD-ready polling, tick providers, graceful shutdown. | Owns process supervision/health/task queues/worker lifecycle. | **[observed implementation]**, but event path depends on Event Bus health |
| Domain contracts | `core/domain`, package `@lev-os/domain` | Manifest says pure TypeScript/no I/O; exports domain event-source/DOR/validation/harness/daemon/telemetry/execution-contract/protocol-adapter subpaths. | Shared contract layer below runtime modules. | **[observed implementation]** |
| Rust runtime substrate | `crates/` workspace | `crates/Cargo.toml` lists Lev core/event/policy/declaration/runtime/scheduler/daemon/UI/kernel/memory/flowmind compiler crates. `lev-kernel` exposes manifold, ratchet, tape, ledger, bridge modules. | Rust side appears to hold lower-level runtime substrate/kernel/event/domain work; TS monorepo remains dominant app/runtime surface. | **[observed implementation]**, but Rust TUI conflict markers block health claims |
| Plugins | `plugins/*` package/config manifests | Plugins declare domain-specific commands, daemons, FlowMind programs, adapters, and surfaces. | Plugins extend runtime; they do not take over core plane ownership. | **[observed implementation]**, source not exhaustively audited |

## FlowMind map

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json` defines `@lev-os/flowmind`, `bin.flowmind`, exports `.`, `./kernel`, `./cli`, `./memory-compiler`, and `./commands/flowmind`, with scripts `build`, `test`, `lint`, and `typecheck`. **[observed implementation]**

Implementation details read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/session.ts` implements `FlowmindSessionManager`. It starts sessions from files/hooks, persists session JSON under `getLevStatePath()/flowmind/sessions`, exposes `get()` without executing, and `next()` to execute and advance. It supports an injected `SessionStepExecutor` for agent/loop steps, otherwise uses built-in `FlowmindExecutor`. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-loader.ts` reads `*.flow.yaml`, validates `type: system-flowmind` and required fields, sorts by `boot_priority`, validates dependency DAG with Kahn's algorithm, and binds `constraint-manifold` native implementation. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` states FlowMind drives declarations/policy and compiles `.flow.yaml`, but does not dispatch workers. **[contract/docs intent]**

Safe wording: FlowMind currently has real implementation for declaration/session/system-flow loading, but runtime cross-plane health remains unverified because no FlowMind test/typecheck/smoke was run and Event Bus import health is blocked. **[tests not run] / [broken/conflict marker]**

## Orchestration map

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json` defines `@lev-os/orchestration`, exports graph/loop/queue/entities/a2a/execution-contract subpaths, and scripts `build`, `typecheck`, `test`. **[observed implementation]**

Implementation details read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/loop/iterative-runner.ts` is labeled the canonical orchestration runtime for `--until` loops. It executes an injected adapter task repeatedly, publishes iteration lifecycle callbacks, handles token/context pressure, circuit breaker, idle handling, semantic completion, and loop exit. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts` implements scheduler strategies: `TopoSortScheduler`, `CriticalPathScheduler`, and `RuntimeDynamicScheduler` via a strategy interface. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` states Orchestration owns DAG scheduling, `ecStart`/`ecNext`, worker dispatch, retry logic, iterative loops, and concurrency. **[contract/docs intent]**

Safe wording: Orchestration has concrete loop/scheduler code, but no orchestration package tests/typechecks were run in this pass. **[tests not run]**

## Graph map

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json` defines `@lev-os/graph`, exports `.`, `./adapters`, `./events`, scripts `build`, `typecheck`, and `test: bun test`, and depends on `@lev-os/config` and `@lev-os/domain`. **[observed implementation]**

Implementation detail read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts` identifies `EntityGraph Compositor` as the core runtime. It uses internal extract → classify → validate → apply, exposes a read-only `GraphReader`, runs validation hooks, persists `GraphEvent` records through an `EventStore`, and applies operations to adapters/backends. **[observed implementation]**
- The file states external contract as classify → validate → apply while internally using extract first. That should be preserved as an implementation-vs-contract distinction. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` states Graph owns state/knowledge/traversal and never dispatches workers. **[contract/docs intent]**

Safe wording: Graph has a real compositor/state/traversal implementation, but Graph tests were not run and this host lacks `bun`, which the graph package test script requires. **[observed implementation] / [tests not run]**

## Event Bus map and blocker

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json` defines `@lev-os/event-bus`, exports event/runtime/context/aggregate/frontmatter/policy/bridge/workflow/actions/guards/types subpaths, and scripts `build`, `dev`, `test`, `test:coverage`, `lint`, and `typecheck`. **[observed implementation]**

Implementation detail read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/event-bus.ts` implements an in-process `EventBus` with glob-style matching, memory history, optional persistence adapter, `emit`, `subscribe`, `history`, and `loadHistory`. **[observed implementation]**

Blocked barrel source:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts` contains conflict markers at lines including 30/32/38, 130/131/133, 141/142/146, and 240/242/247. It cannot be used as clean truth for package-level export health. **[broken/conflict marker]**

Safe wording: Event Bus has meaningful implementation files, but `@lev-os/event-bus` package health and any cross-plane path importing the conflicted barrel are **open** until conflict markers are resolved and typecheck/smoke commands pass. **[open gap]**

## Exec / Poly / Daemon map

### Exec

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json` defines `@lev-os/exec`, exports `.`, `./types`, `./semaphore`, `./adapters/poly`, `./client`, and scripts `build`, `typecheck`, `test`. **[observed implementation]**

Read implementation: `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts` implements `createExec(dispatch, opts)`, returns frozen `ExecEngine`, uses `ProviderSemaphore`, logs events to `getLevDataHome()/events.jsonl`, and makes event emission best-effort so disk/event errors do not break execution. **[observed implementation]**

Caution: Exec imports `@lev-os/event-bus/events`; if Event Bus subpath resolution is affected by conflicts, real runtime health is not established here. **[open gap]**

### Poly

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json` defines `@lev-os/poly`, `bin.lev`, main `src/sdk/index.ts`, direct source exports, build registry scripts, and dependencies on Exec, Daemon, Domain, Index, UI, Event Bus, Config, Logger. **[observed implementation]**

Read implementation: `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts` implements `executeHandler()` for `bin:`, `grpc:`, `http:`, and `https:` handlers; binary execution uses `spawn`, gRPC currently falls back to HTTP, registry YAML is loaded with cache, and `createExec` is lazy-imported to break poly↔exec cycles. **[observed implementation]**

Caution: Poly surface/build health was not checked; no registry build was run. **[tests not run]**

### Daemon

Observed package contract: `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json` defines `@lev-os/daemon`, root export only, and scripts `build`, `test`, `typecheck`. **[observed implementation]**

Read implementation: `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/core.ts` implements `DaemonCore` with heartbeat timer, poll timer, BD poll timer, `QueueManager`, tick providers, `daemon.started`, `daemon.heartbeat`, `daemon.stopped`, task events, XDG daemon directory setup, and project event logging. **[observed implementation]**

Caution: Daemon event types and event emitters are present, but no daemon smoke was run. **[tests not run]**

## Plugin map

Manifest inventory command observed 24 plugin `package.json` files and 24 matching `config.yaml` files under `/Users/joshuaeisenhart/GitHub/leviathan/plugins/*`. **[observed implementation]**

Selected plugin surfaces read:

| Plugin | Files read | Runtime surface observed | Status |
|---|---|---|---|
| `genui-exec-daemon` | `plugins/genui-exec-daemon/package.json`, `plugins/genui-exec-daemon/config.yaml` | Daemon metadata on port `9860`, health `http://localhost:9860/health`, MCP tools `exec`, `exec-stream`, `status`, poly SDK handler declarations. | **[observed implementation]**, not run |
| `voice` | `plugins/voice/package.json`, `plugins/voice/config.yaml` | Fastify/WebSocket voice daemon on port `3001`, voice routing/generation/session SDK handlers, MCP prefix `voice:`, FlowMind program `flows/voice-session.flow.yaml`, trigger subscriptions to exec/daemon health events. | **[observed implementation]**, not run |
| `core-sdlc` | `plugins/core-sdlc/package.json`, `plugins/core-sdlc/config.yaml` | SDLC plugin exports command surfaces (`work`, `review`, `sdlc`, `loop`, `autodev`), declares FlowMind programs for spec lifecycle, commit gate, PEV, exec-validate, plan deepen, hygiene, and poly surfaces such as `sdlc exec`, `sdlc deepen`, `sdlc hygiene`, `sdlc autodev`. | **[observed implementation]**, not run |
| `graph-adapters` | `plugins/graph-adapters/package.json` | External graph adapter plugin with exports `./bd`, `./file`, `./code`, depends on `@lev-os/graph`. | **[observed implementation]**, not run |
| `evolve-memory` | `plugins/evolve-memory/package.json` | Biomimetic memory/skill evolution plugin; scripts only `test` and `test:e2e`, depends on Domain and Orchestration. | **[observed implementation]**, but workflow mismatch noted in build/test page |

Plugin boundary: plugins attach domain-specific behavior, FlowMind programs, daemon processes, and surfaces; they are not the owners of FlowMind, Graph, Orchestration, Event Bus, Exec, Poly, or Daemon. **[contract/docs intent]**

## Rust/crates runtime map

`/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.toml` defines a Rust workspace with runtime substrate crates including `lev-core`, `lev-events`, `lev-policy`, `lev-declaration`, `lev-runtime`, `lev-scheduler`, `levd`, `lev-stream`, `lev-config`, `lev-graph`, `lev-observe`, `lev-audit`, `lev-wire`, `lev-sandbox`, `lev-memory`, `lev-flow`, `lev-logger`, `lev-kernel`, `lev-entity-graph`, `lev-supervisor`, `lev-mcp`, `lev-memory-engine`, `lev-flowmind-compiler`, and `lev-abac`. **[observed implementation]**

Selected crates read:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/Cargo.toml` describes a constraint enforcement kernel for manifold, ratchet admission, campaign tape, and bridge. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/lib.rs` exports `manifold`, `ratchet`, `tape`, `ledger`, and `bridge`. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs` implements a simple `RatchetAdmission`: at least one nonempty evidence reference admits; once admitted, repeated admission stays admitted. This is not proof of the richer FlowMind/contract ratchet doctrine. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-domain/Cargo.toml` describes canonical domain types and schema generation. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-events/Cargo.toml` describes Rust event spine/schema/bus/JSONL persistence. **[observed implementation]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/levd/Cargo.toml` describes the Rust Lev daemon binary. **[observed implementation]**

Caution: Rust workspace health is not claimed. Conflict markers were read in Rust TUI files: `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-theme/src/lib.rs` and `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-widgets/src/attention_kanban.rs`. **[broken/conflict marker] / [tests not run]**

## Broken/conflict marker map

A Python read-only scan excluding `.git`, `node_modules`, `target`, `dist`, `.turbo`, and `.next` observed `56` files with lines starting `<<<<<<<`, `=======`, or `>>>>>>>`. Many are archive/workshop/report material, but active runtime blockers include:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/context/pr.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/bridge/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/scm.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/commands/skills.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/skill-orchestrator/cli-bridge.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/skill-orchestrator/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/skill-orchestrator/__tests__/cli-bridge.test.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/commands/__tests__/skills-sync.test.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-theme/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-widgets/src/attention_kanban.rs`

Any source content inside a conflict hunk is treated as **blocked**, not truth. **[broken/conflict marker]**

## Current safe runtime flow statement

Safe, bounded statement:

```text
FlowMind declares/loads/sessions policy and program steps.
Orchestration supplies loop/scheduler/queue execution strategy.
Exec wraps provider/tool execution with semaphore and lifecycle events.
Poly exposes and routes northbound surfaces/handler transports.
Daemon supervises long-running processes, queue workers, and task polling.
Graph persists/projects entity state and graph operations.
Event Bus is intended as the causality spine, but current package-level health is blocked by conflict markers.
Plugins attach domain-specific commands, FlowMinds, daemons, adapters, and surfaces through explicit manifests/configs.
```

Support: mixed **[observed implementation]** and **[contract/docs intent]**. Not an end-to-end smoke. **[tests not run]**

## Open gaps

1. Resolve active conflict markers before asserting Event Bus, Build skills, or Rust TUI health. **[broken/conflict marker]**
2. Run package-level typechecks/tests with clean output before saying any package is green. **[tests not run]**
3. Verify whether all plugin handler paths declared in `config.yaml` and `package.json` exist and compile. **[open gap]**
4. Verify the Event Bus `LevEvent` contract across TypeScript `core/event-bus`, `core/domain`, `core/exec`, `core/daemon`, `core/graph`, and Rust `crates/lev-events`. **[open gap]**
5. Verify the Rust workspace with conflict markers removed or excluded; current scan blocks health claims. **[open gap]**
6. Reconcile docs claiming current event families with concrete emitted event code after Event Bus conflicts are resolved. **[open gap]**
7. Treat Fusion/GLM pressure as advisory only; it helped prioritize this full map and build/test health page, but all claims above are grounded in files/commands listed here. **[advisory pressure]**
