---
title: Exec / Poly / Daemon Boundary
date: 2026-06-17
packet: 2
status: current-runtime-map
claim_ceiling: historical Packet 2 source map with current-source caveats; not current build proof; not runtime health proof
owned_by: background-packet-2
---

# Exec / Poly / Daemon Boundary

## Evidence and status labels

Major claims below are tagged with **[observed file]**, **[inferred from package/code]**, **[inferred from docs]**, **[roadmap/design intent]**, **[open]**, or **[not checked]**.

Primary sources read for this page:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-exec.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-poly.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-daemon.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-domain.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/types.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/client.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/adapters/cli.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/adapters/mcp.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/adapters/poly.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/extension-registry.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/registry-validator.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/surfaces/cli/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/surfaces/mcp/tools.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/core.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/supervisor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/worker-pool.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/plugin-manifest.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/orchestrator-integration.ts`

## Boundary summary

The hard-cut architecture separates three frequently-confused responsibilities:

1. **Exec** owns the execution SDK/engine contract. **[inferred from docs]**
2. **Poly** owns northbound binding/routing/surface generation: CLI, MCP, registry, SDK handler transport, extension registry, and plugin validation. **[inferred from docs]**
3. **Daemon** owns process supervision, health monitoring, worker pools, task queues, and daemon lifecycle implementation. **[inferred from docs]**

This page maps the current implementation files that support that split.

## Exec owner map

`@lev-os/exec` is the canonical execution contract package. **[observed file]** Package metadata exposes `.`, `./types`, `./semaphore`, `./adapters/poly`, and `./client`; the package depends on `@lev-os/event-bus`, `@lev-os/domain`, `@lev-os/config`, and `@lev-os/logger`. **[observed file]**

Read implementation files:

| File | Role | Status |
|---|---|---:|
| `core/exec/src/index.ts` | Main execution engine/export surface | **[observed file]** |
| `core/exec/src/types.ts` | Execution request/result/type contracts | **[observed file]** |
| `core/exec/src/client.ts` | Client-facing execution API | **[observed file]** |
| `core/exec/src/adapters/cli.ts` | CLI adapter into execution contract | **[observed file]** |
| `core/exec/src/adapters/mcp.ts` | MCP adapter into execution contract | **[observed file]** |
| `core/exec/src/adapters/poly.ts` | Poly adapter into execution contract | **[observed file]** |

The architecture doc says `createExec(dispatch)` returns a frozen `ExecEngine` with provider concurrency, event emission, and error wrapping. **[inferred from docs]** Packet 2 did not execute this code path. **[not checked]**

Exec boundary rules:

- Exec owns provider execution lifecycle and event wrapping. **[inferred from docs]**
- Exec should not own CLI command discovery or MCP tool generation; those are Poly. **[inferred from docs]**
- Exec should not own process supervision/health loops; those are Daemon. **[inferred from docs]**

## Poly owner map

`@lev-os/poly` is the binder/router package. **[observed file]** Package metadata declares the `lev` binary at `core/poly/bin/lev`, exports SDK/codegen/events/adapters/registry/plugin-validator/commands/surfaces subpaths, and depends on `@lev-os/exec`, `@lev-os/daemon`, `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/config`, `@lev-os/index`, `@lev-os/ui-renderers`, and support packages. **[observed file]**

Read implementation files:

| File | Role | Status |
|---|---|---:|
| `core/poly/src/sdk/index.ts` | SDK dispatch/handler execution surface; package main | **[observed file]** |
| `core/poly/src/extension-registry.ts` | Extension discovery/loading registry | **[observed file]** |
| `core/poly/src/registry-validator.ts` | Registry validation | **[observed file]** |
| `core/poly/src/surfaces/cli/index.ts` | CLI surface entry/binder | **[observed file]** |
| `core/poly/src/surfaces/mcp/tools.ts` | MCP tool surface definitions | **[observed file]** |

The Poly spec states Poly is binder-only: it parses, routes, dispatches, builds registries, validates plugins, and exposes surfaces, but should not implement business logic, daemon lifecycle logic, or the execution engine. **[inferred from docs]**

Poly boundary rules:

- `core/poly/bin/lev` is the canonical `lev` CLI binary. **[inferred from docs]** / **[observed file]**
- CLI/MCP/registry/plugin validator are Poly-owned surfaces. **[observed file]**
- Poly provides transport/handler dispatch that Exec can wrap, but Exec owns execution lifecycle. **[inferred from docs]**
- Poly may route daemon commands, but Daemon implements daemon lifecycle. **[inferred from docs]**

One source lookup for `core/poly/src/index.ts` returned file-not-found; package `main` points to `src/sdk/index.ts` instead. **[observed file]**

## Daemon owner map

`@lev-os/daemon` is the daemon runtime library. **[observed file]** Package metadata describes daemon lifecycle, supervision, health monitoring, and task execution; it exports only the package root and depends on `@lev-os/config`, `@lev-os/domain`, `@lev-os/event-bus`, and `@lev-os/logger`. **[observed file]**

Read implementation files:

| File | Role | Status |
|---|---|---:|
| `core/daemon/src/index.ts` | Public daemon API/barrel | **[observed file]** |
| `core/daemon/src/core.ts` | Daemon core loop/runtime | **[observed file]** |
| `core/daemon/src/supervisor.ts` | Process supervision/dependency lifecycle | **[observed file]** |
| `core/daemon/src/worker-pool.ts` | Worker pool/task execution | **[observed file]** |
| `core/daemon/src/plugin-manifest.ts` | Plugin daemon manifest handling | **[observed file]** |
| `core/daemon/src/orchestrator-integration.ts` | Orchestration/daemon lifecycle bridge | **[observed file]** |

Daemon boundary rules:

- Daemon owns process supervision, health checks, worker pools, queues, and lifecycle events. **[inferred from docs]**
- Daemon does not own CLI binary or command discovery; Poly routes those. **[inferred from docs]**
- Daemon can integrate with orchestration, but orchestration owns DAG/loop strategy. **[inferred from docs]**

## Boundary matrix

| Concern | Exec | Poly | Daemon | Status |
|---|---|---|---|---:|
| Provider execution request/result lifecycle | owner | caller/transport provider | not owner | **[inferred from docs]** |
| Per-provider concurrency/backpressure | owner | not owner | not owner | **[inferred from docs]** |
| CLI binary `lev` | not owner | owner | not owner | **[observed file]** |
| CLI command discovery/alias/envelope | not owner | owner | not owner | **[inferred from docs]** |
| MCP tool definitions | adapter target | owner | optional routed target | **[observed file]** |
| Handler URI dispatch/registry surface | not engine owner | owner | can be target | **[inferred from docs]** |
| Process start/stop/health/logs | not owner | routes/formats | owner | **[inferred from docs]** |
| Worker pool/task execution | not owner | not owner | owner | **[observed file]** |
| Plugin daemon manifest parsing | not owner | validation/registry adjacency | owner for daemon extraction/lifecycle | **[observed file]** |
| Event emission | emits exec events through bus | may emit/route | emits daemon/worker/task events | **[inferred from docs]**; bus health blocked |

## Cross-plane runtime path

A typical northbound call should follow this shape:

```text
CLI/MCP/API surface (Poly)
  -> registry/handler resolution (Poly)
  -> execution request wrapper (Exec)
  -> handler transport / provider call (Poly transport or adapter target)
  -> daemon/plugin process if needed (Daemon/plugin)
  -> canonical events (Event Bus)
```

This path is **[inferred from docs]** and supported by observed package boundaries. It was not smoke-tested. **[not checked]**

## Current blockers and cautions

- Exec/Daemon event emissions cannot be claimed end-to-end healthy from this old Packet 2 source map alone; use a current proof packet for runtime health. **[open]**
- No tests/typechecks were run for Exec, Poly, or Daemon in Packet 2. **[not checked]**
- Poly has a large source tree (122 TypeScript files found under `core/poly/src`); Packet 2 read boundary files and docs, not every command/codegen/surface implementation. **[observed file]** / **[not checked]**
- Daemon has 50 TypeScript files found under `core/daemon/src`; Packet 2 read core boundary files, not every adapter/health/queue implementation. **[observed file]** / **[not checked]**

## Invariants to preserve

1. Do not reintroduce `core/cli/`; CLI belongs to Poly. **[inferred from docs]**
2. Do not treat Poly as the execution engine; Exec owns execution lifecycle. **[inferred from docs]**
3. Do not move daemon supervision into Poly; Daemon owns lifecycle implementation. **[inferred from docs]**
4. Package exports should stay consistent with hard-cut topology. **[observed file]**
5. Runtime events must converge on Event Bus after conflict resolution. **[open]**

## Open questions

- Which Poly command handlers still contain direct spawn/exec launcher behavior and whether each is an allowed thin launcher. **[open]**
- Whether daemon plugin manifest extraction is fully validated against all plugin package/config declarations. **[open]**
- Whether `createExec(dispatch)` lifecycle events pass through the conflicted event-bus package in the currently checked-out tree. **[open]**
