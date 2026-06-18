---
title: FlowMind Control Plane Start
created: 2026-06-17
updated: 2026-06-17
type: module-map
status: wave-1 starter
claim_ceiling: starter control-plane map from package manifest and src/index only
owner: runtime-map-worker
---

# FlowMind Control Plane Start

> Supersession note, 2026-06-18: this is an earlier starter map. For current upstream truth, begin with [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]]. Use this page only as packet context where it differs from the current clean snapshot.

## Scope

This page maps FlowMind as a starter control-plane module. It only uses package metadata and the public barrel entrypoint, not full implementation files. Treat it as a first-pass contract map.

Support labels:

- `observed file` — directly read in source.
- `inferred from package contract` — inferred from package metadata, exports, dependencies, or comments in the public barrel.
- `inferred architecture` — boundary interpretation consistent with repo/module architecture but not exhaustively proven.
- `not checked` — implementation not read in this pass.
- `open` — needs follow-up or conflict resolution.

Boundary statement: **FlowMind does not dispatch** in this starter map. It declares, compiles, routes within control policy, and exposes execution/session surfaces, but runtime scheduling/worker dispatch belongs to orchestration/poly/daemon/exec surfaces depending on path. (`inferred architecture`)

## Sources read

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/worker-swarm-plan-2026-06-17.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/index.ts`

Existence note: no root `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/README.md` was found during this bounded file listing. (`observed file`)

## Package contract

| Field | Value / note | Support |
|---|---|---|
| Package path | `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind` | `observed file` |
| Package name | `@lev-os/flowmind` | `observed file` |
| Version | `0.1.0` | `observed file` |
| Description | `FlowMind compiler - YAML IR to executable targets (smartdown, openprose, system_prompt, prompt_gen, schedule, hooks)` | `observed file` |
| Main/types | `dist/index.js`, `dist/index.d.ts` | `observed file` |
| Exported subpaths | `.`, `./kernel`, `./cli`, `./memory-compiler`, `./commands/flowmind` | `observed file` |
| CLI bin | `flowmind` -> `./dist/cli.js` | `observed file` |
| Leviathan metadata | `type: core`, `namespace: flowmind`, description: FlowMind YAML IR compiler for behavior specifications | `observed file` |
| Dependencies | `@lev-os/config`, `@lev-os/domain`, `@lev-os/event-bus`, `@lev-os/logger`, `yaml`, `zod` | `observed file` |
| Dev/test signals | scripts for `build`, `dev`, `test`, `lint`, `typecheck`; AI SDK/Ollama provider dev deps | `observed file` |

## Public barrel module table

| Surface | Entrypoint exports / comments observed | Starter role | Boundary label |
|---|---|---|---|
| Schema/types | `CompileTarget`, `NodeType`, `FlowMindNode`, `FlowMindDocument`, triggers/properties/memory/safety/output/satisfaction, node op types, graph node/document types, loop config types, execution strategy types, prompt pipeline/context assembly config | Defines the control-plane IR and graph document shape. | `observed file`; `inferred from package contract` |
| Type guards/inference | `inferNodeType`, `isAgentNode`, `isGateNode`, `isSubgraphNode`, `isFunctionNode`, `isTerminal`, `requiresApproval` | Control-plane classification of nodes and approval/gate properties. | `observed file` |
| Parser | `parse`, `parseFile`, `validateFlowMindNode`, `FlowMindParseError`, `toExecutableFlow` | Turns FlowMind documents/files into validated control structures. | `observed file` |
| Serialization | `serializeGraphDocument`, `deserializeGraphDocument`, YAML codec, semantic equality | Moves graph documents to/from YAML with a codec. | `observed file` |
| Compiler | `compile`, `compileFile`, `compileNode`, `compileDocument`, `registerTarget`, `getAvailableTargets`, `isTargetSupported` | Compiles FlowMind IR into target artifacts. | `observed file` |
| Target compilers | `compileToSmartdown`, `compileToOpenprose`, `compileToSystemPrompt`, `compileToContextAssembly`, `compileToPromptGen`, `compileToSchedule`, `compileToHooks` | Emits target representations including prompt, schedule, hook, and context artifacts. | `observed file`; schedule/hooks output does not prove dispatch ownership (`inferred architecture`) |
| Executor exports | `GraphFlowExecutor`, `executeGraphFile`, `executeGraphDocument`, plus deprecated `FlowmindExecutor`, `executeFlowmind`, `executeHook`, `toFlowmindHook` | Provides graph/document execution surfaces in the FlowMind package. | `observed file`; implementation not read (`not checked`) |
| Session engine | `FlowmindSessionManager`, session status/view/executor types | Progressive-disclosure execution/session state surface. | `observed file` |
| Router | `export * from './router/index.js'`; comment says router decomposition aliases and trigger matcher/policy re-exports | Routing/matching inside FlowMind control semantics. | `observed file`; runtime dispatch boundary open (`open`) |
| Transpiler | `Opcode`, `Instructions`, `ProgramBuilder`, instruction/operand types and guards | Instruction-set compilation layer. | `observed file` |
| NLU decompiler | `decompile`, `loadFixtures`, decompiled flow/trigger/action/step/memory types | Natural-language/decompiler surface for FlowMind language v2. | `observed file` |
| Memory compiler | `detectSatisfaction`, `extractRule`, `compileToMemory`, `compileBatch`, satisfaction/rule/action/entity types | Converts satisfaction signals into executable memory candidates. | `observed file`; persistence path not checked (`not checked`) |
| Tiered executor | `createTieredExecutor`, tiered executor/capability/options types | T1/T2/T3 node execution selection. | `observed file`; implementation not checked (`not checked`) |
| AI provider | `createFlowMindProvider`, `detectProviders`, provider config/types | Provider adapter surface for model access. | `observed file`; production routing not checked (`not checked`) |
| Tool registry | `createToolRegistry`, `getDefaultToolRegistry`, action target/type types | Registers/looks up action targets for FlowMind tools. | `observed file` |
| Rule/embedding/model profile helpers | `mapToolToAction`, lifecycle/session assessment, embedding classifier, model profile selectors | Deterministic and embedding/model-assisted classification helpers. | `observed file` |
| Runtime kernel | `export * from './kernel/index.js'` | Kernel surface exists as subpath/package export. | `observed file`; implementation not read (`not checked`) |
| Adapter registry | `NodeAdapterRegistry`, `createAdapterRegistry`, adapter factory/entry/config types | Node adapter registration surface. | `observed file` |
| Intent compiler | Gate 0/1, breadcrumb assembler, `compileIntentSync`, `compileIntent`, seed types, `seedToGraphDocument`, `extractGraphSeed` | Pre-FlowMind ingress pipeline from intent to graph seed/document. | `observed file` |
| End-to-end prompt run | `runFromPrompt`, `compileFromPrompt` and result/option types | Public NL -> Intent -> Graph -> Execution pipeline surface. | `observed file`; exact executor/dispatcher path not checked (`not checked`) |
| Graph review | `reviewGraph`, `reviewFromPrompt` | CLI/inspection review surface for graph documents. | `observed file` |
| Execution contract copy | `ecStart`, `ecNext`, `createTestAdapter`, `executeWithContract`, contract/adapter types | Deprecated local copy; barrel comments say canonical home is `@lev-os/orchestration/execution-contract`. | `observed file` |

## Control-plane flow sketch

```text
Natural-language/task intent
  -> intent compiler gates / breadcrumb / seed extraction
  -> FlowmindGraphSeed
  -> GraphDocument / FlowMindDocument
  -> parser + schema validation + serialization
  -> compiler targets:
       - system prompt / context assembly / prompt gen
       - smartdown / openprose
       - schedule artifact / hooks artifact
  -> optional FlowMind execution/session/review surfaces
  -> orchestration/exec/poly/daemon own broader runtime scheduling/dispatch paths
```

Support: `inferred architecture` from the public barrel and package contract. Implementation of each arrow is `not checked` unless noted in the tables.

## Boundary guard notes

| Boundary | Starter finding | Support |
|---|---|---|
| FlowMind vs scheduling | Root package includes a guard script named `test:guard:flowmind-scheduler` that fails on `flowmind-scheduler` references in runtime code paths. | `observed file`; narrow support only |
| FlowMind vs orchestration | FlowMind re-exports deprecated execution-contract copies and explicitly says the canonical home is `@lev-os/orchestration/execution-contract` because orchestration depends on FlowMind, so FlowMind cannot depend on orchestration. | `observed file` |
| FlowMind vs event bus | Package depends on `@lev-os/event-bus`, but selected entrypoint read did not prove exact event publication/listening behavior. | `observed file`; `not checked` |
| FlowMind vs domain | Package depends on `@lev-os/domain`; selected barrel exports use action target and execution-contract concepts that likely touch domain contracts. | `inferred from package contract`; exact imports not fully checked |
| FlowMind schedule/hooks targets | Target compilers include schedule and hooks. In this map that means FlowMind can produce schedule/hook artifacts, not that it owns runtime dispatch. | `observed file`; `inferred architecture` |

## Claims with support labels

- FlowMind's package contract is primarily compiler/control-plane oriented: YAML IR to executable target artifacts. (`observed file`)
- FlowMind's public surface has grown beyond pure compilation to include graph execution/session/review, intent compilation, kernel, memory compiler, model/provider, and adapter registry surfaces. (`observed file`)
- The local FlowMind execution-contract copy is not canonical according to comments in `src/index.ts`; orchestration is named as canonical home. (`observed file`)
- FlowMind is not mapped as the dispatch scheduler in this page even though it exposes execution and schedule/hook target compilers. (`inferred architecture`)
- The exact runtime semantics of `GraphFlowExecutor`, `runFromPrompt`, router policy, and kernel actor files were not checked in this pass. (`not checked`)

## Open questions

1. What is the exact distinction between `GraphFlowExecutor`, orchestration's execution contract, and exec/poly provider execution? (`open`)
2. Does FlowMind's router only match/route control declarations, or does any implementation trigger external dispatch directly? (`open`)
3. How do schedule/hook target artifacts hand off to event-bus/daemon/orchestration at runtime? (`open`)
4. Is `FlowmindExecutor` still used in active paths despite being marked legacy/deprecated in the barrel? (`open`)
5. Which of `kernel`, `actor-kernel`, `system-flowmind-executor`, and `validation-gate-executor` are production runtime paths vs experimental/test surfaces? (`open`)
6. Is `runFromPrompt` intended as a CLI/demo E2E pipeline or a supported runtime API? (`open`)

## Next read queue

1. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/schema.ts` — IR definitions and boundaries.
2. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/compiler.ts` and `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/targets/*.ts` — target artifact semantics.
3. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/executor.ts` — `GraphFlowExecutor` and legacy executor boundary.
4. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/session.ts` — progressive-disclosure session engine.
5. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/router/index.ts`, `router.policy.ts`, and `router/trigger-matcher.ts` — routing vs dispatch distinction.
6. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/run.ts` and `src/review.ts` — E2E prompt pipeline and inspection surface.
7. `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/index.ts` and adjacent kernel files — actor/kernel semantics.
8. `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/execution-contract/index.ts` — canonical execution-contract comparison.
