---
title: Plugin Ownership Map
date: 2026-06-17
packet: 2
status: current-runtime-map
owned_by: background-packet-2
---

# Plugin Ownership Map

## Evidence and status labels

Major claims below are tagged with **[observed file]**, **[inferred from package/code]**, **[inferred from docs]**, **[roadmap/design intent]**, **[open]**, or **[not checked]**.

Primary sources read for this page:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-poly.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-daemon.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-domain.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-graph-adapters.md`
- `package.json` and `config.yaml` under all 24 observed plugin directories in `/Users/joshuaeisenhart/GitHub/leviathan/plugins/*/`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/extension-registry.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/registry-validator.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/plugin-manifest.ts`

## Boundary summary

Plugins are domain/runtime extensions with explicit contracts. **[inferred from docs]** They attach domain-specific FlowMind programs, commands, templates, adapters, daemons, and surfaces without taking over the four core planes:

- FlowMind remains control/policy. **[inferred from docs]**
- Orchestration remains execution strategy/scheduling. **[inferred from docs]**
- Graph remains state/knowledge. **[inferred from docs]**
- Event Bus remains causality. **[inferred from docs]**
- Poly remains binder/registry/surface; Daemon remains daemon lifecycle; Exec remains execution contract. **[inferred from docs]**

The active plugin scan observed 24 plugin packages and 24 matching `config.yaml` files. **[observed file]** This differs from one architecture topology snippet that lists fewer/older plugins; Packet 2 treats the filesystem scan as current for plugin inventory. **[observed file]**

## Plugin registration mechanisms

Observed plugin contracts use:

- `package.json` `leviathan` metadata with `type: plugin` and `namespace`. **[observed file]**
- Optional `leviathan.activation`, `leviathan.mcp`, `leviathan.daemon`, and `leviathan.contributes.commands`. **[observed file]**
- `config.yaml` declarations for `poly`, `flowmind`, `daemon`, capabilities, and domain-specific settings. **[observed file]**
- Poly extension registry and registry validator for discovery/validation. **[observed file]**
- Daemon plugin manifest handling for daemon-enabled plugins. **[observed file]**

## Current plugin inventory

| Plugin | Package | Namespace | Ships with | Primary ownership | Runtime surfaces | Status |
|---|---|---|---:|---|---|---:|
| `auth-sniffer` | `@lev-os/auth-sniffer` | `auth-sniffer` | not declared | Browser cookie auth discovery with XDG persistence | MCP `auth_sniffer:*`; FlowMind program `skills/auth-sniffer.flow.yaml` | **[observed file]** |
| `beads` | `@lev-os/beads` | `beads` | false | Beads/bd lifecycle bridge into events | commands `beads:*`; activation `onCommand:beads:*`, `onDaemon`; poly SDK `create`, `update`, `watch` | **[observed file]** |
| `browser-cascade` | `@lev-os/browser-cascade` | `browser-cascade` | not declared | 3-tier browser automation cascade | config commands/capabilities | **[observed file]** |
| `core-bench` | `@lev-os/core-bench` | `core-bench` | true | Benchmark harness for SDLC agent quality | `lev bench` poly surface; FlowMind `bench-eval` | **[observed file]** |
| `core-gameai` | `@lev-os/core-gameai` | `core-gameai` | true | Game AI primitives: scoring/director/blackboard/leasing/BT/tracing/planner/learning | domain config/events | **[observed file]** |
| `core-platforms` | `@lev-os/core-platforms` | `core-platforms` | true | IDE/gateway platform adapters | poly SDK `sync`, `status`; binary `lev-adapter` | **[observed file]** |
| `core-scheduling` | `@lev-os/core-scheduling` | `core-scheduling` | true | Cron/interval/one-shot scheduling runtime | poly SDK cron CRUD/search/filter etc. | **[observed file]** |
| `core-sdlc` | `@lev-os/core-sdlc` | `core-sdlc` | true | SDLC/autodev entity pipeline and FlowMind programs | `sdlc exec`, `sdlc deepen`; FlowMind lifecycle/gates | **[observed file]** |
| `core-workshop` | `@lev-os/core-workshop` | `core-workshop` | not declared | Tool/plugin creation system | MCP `workshop:*` | **[observed file]** |
| `deploy` | `@lev-os/deploy` | `deploy` | false | Deterministic deploy adapters and `levd` runtime surface | poly CLI `levd` | **[observed file]** |
| `erc` | `@lev-os/erc` | `erc` | false | AIDD toolkit: churn/fix/prompt QA/Gyron/scans/reports | commands `erc:*`; poly surfaces; FlowMind programs | **[observed file]** |
| `evolve-memory` | `@lev-os/evolve-memory` | `evolve-memory` | false | Biomimetic memory and skill evolution | poly surfaces `evolve`; FlowMind memory/skill/consolidation flows | **[observed file]** |
| `genui-exec-daemon` | `@lev-os/genui-exec-daemon` | `genui-exec` | false | GenUI sandboxed execution daemon | daemon port 9860; MCP `genui-exec:*`; poly SDK `exec`, `exec-stream`, `status` | **[observed file]** |
| `graph-adapters` | `@lev-os/graph-adapters` | `graph-adapters` | not declared | External graph backends (FalkorDB, Graphiti, Cognee) | adapter plugin | **[observed file]** |
| `mastra` | `@lev-os/mastra` | `mastra` | optional | Mastra workflow adapter for FlowMind | poly workflow adapter | **[observed file]** |
| `notion` | `@lev-os/notion` | `notion` | not declared | Direct Notion API and robot-mode CLI | commands `notion:*`; activation `onCommand:notion:*` | **[observed file]** |
| `prompt-stack` | `@lev-os/prompt-stack` | `prompt-stack` | false | Backward-compatible prompt-stack runtime | activation `onCommand:prompt-stack:*`; prompt_stack config | **[observed file]** |
| `publisher` | `@lev-os/publisher` | `publisher` | false | Type-driven filesystem publishing for beads | activation `onDaemon`; publisher triggers | **[observed file]** |
| `slate` | `@lev-os/slate` | `slate` | false | Swarm-native Thread Weaving orchestration | commands `slate:*`; poly surfaces resolving to exec profiles | **[observed file]** |
| `vision` | `@lev-os/vision` | `vision` | not declared | Vision/capture/web automation | manual MCP `vision:*` | **[observed file]** |
| `voice` | `@lev-os/voice` | `voice` | not declared | Voice-first dashboard/plugin runtime | daemon port 3001; poly SDK `generate`, `route`, `session`; MCP `voice:*`; FlowMind `voice-session` | **[observed file]** |
| `wiggum-marketer` | `@lev-os/wiggum-marketer` | `wiggum-marketer` | false | Marketing runtime extension | integration config | **[observed file]** |
| `workflow-orchestrator` | `@lev-os/workflow-orchestrator` | `workflow` | optional | Bi-directional workflow orchestration plugin | poly SDK `execute`, `status`; MCP `workflow:*` | **[observed file]** |
| `writer` | `@lev-os/writer` | `writer` | false | Writer runtime extension | integration config | **[observed file]** |

## Foundation plugins versus domain plugins

Foundation plugins observed with `ships-with: true` include `core-bench`, `core-gameai`, `core-platforms`, `core-scheduling`, and `core-sdlc`. **[observed file]** These are runtime architecture extensions but remain plugin-owned, not core-plane owners. **[inferred from docs]**

Flat-name plugins such as `beads`, `voice`, `vision`, `notion`, and `genui-exec-daemon` are valid when plugin metadata declares `type: plugin` and a namespace. **[inferred from docs]** Their domain logic should remain in plugin packages. **[inferred from docs]**

## Surface ownership by plugin type

### Poly SDK / CLI / MCP plugins

Many plugins declare `poly.sdk`, `poly.surfaces`, or `leviathan.mcp`. **[observed file]** These declarations make plugin functionality available through Poly surfaces while keeping implementation in the plugin package. **[inferred from docs]** Examples: `beads`, `core-platforms`, `core-scheduling`, `core-sdlc`, `core-bench`, `erc`, `evolve-memory`, `genui-exec-daemon`, `vision`, `voice`, `workflow-orchestrator`. **[observed file]**

### FlowMind plugins

Plugins can ship FlowMind programs. **[observed file]** Observed examples include `auth-sniffer`, `core-bench`, `core-sdlc`, `erc`, `evolve-memory`, and `voice`. **[observed file]** These attach domain-specific workflows to the FlowMind control plane without moving core FlowMind ownership into plugins. **[inferred from docs]**

### Daemon plugins

Daemon-enabled plugin declarations were observed in `genui-exec-daemon` and `voice`. **[observed file]** `genui-exec-daemon` declares `leviathan.daemon` metadata and `config.yaml` `poly.daemon` settings for port 9860/health/restart policy. **[observed file]** `voice` declares a daemon config with process command, port 3001, health endpoint, restart policy, and capabilities. **[observed file]** Daemon lifecycle remains `@lev-os/daemon`-owned. **[inferred from docs]**

### Graph adapter plugins

`graph-adapters` is the dedicated plugin for external graph backends. **[observed file]** This keeps optional external dependencies and domain-specific adapters out of `core/graph`, while core Graph owns contracts and core adapter machinery. **[inferred from docs]**

## Boundary cautions

- Plugin package/config declarations were read, but plugin source was not exhaustively audited. **[not checked]**
- Some plugins may include scripts or commands with side effects; no plugin commands were run. **[not checked]**
- Event Bus conflicts mean plugin event integration cannot be declared runtime-healthy. **[observed file]**
- Secrets were not retained; if future plugin config/source reads encounter credentials, they must be redacted as `[REDACTED]`. **[inferred from task rule]**

## Invariants to preserve

1. Plugins own domain-specific behavior; core planes own universal lifecycle boundaries. **[inferred from docs]**
2. Plugin commands/tools should be registered through Poly/registry contracts. **[inferred from docs]**
3. Plugin daemon lifecycle should be supervised by Daemon, not implemented by Poly. **[inferred from docs]**
4. Plugin FlowMind programs should feed the FlowMind compiler/session/control plane, not replace it. **[inferred from docs]**
5. External graph adapters belong in `plugins/graph-adapters`, not in core Graph unless intentionally promoted. **[inferred from docs]**

## Not checked in this packet

- Full plugin TypeScript source inventory beyond manifest/config summary. **[not checked]**
- Plugin test suites, builds, or runtime smoke. **[not checked]**
- Validation output from Poly registry builder/plugin validator. **[not checked]**
- Whether each declared handler file exists and compiles. **[not checked]**

## Open questions

- Which plugins are actively installed/enabled by default versus merely present in the repo. **[open]**
- Whether `ships-with` absence means false, inherited default, or unspecified for each plugin. **[open]**
- Whether all plugin `poly.sdk` handlers are discoverable by the current registry builder after conflict cleanup. **[open]**
