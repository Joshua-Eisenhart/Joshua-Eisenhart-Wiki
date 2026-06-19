---
title: Leviathan V3 Deep Repo Nuance Bundle
date: 2026-06-19
type: codex-import-bundle
status: imported-from-chat-v3
source_repo: lev-os/leviathan
source_snapshot: 5dd98ac4ce7afeb9e4351787179c60208de6d23f
claim_ceiling: wiki/source synthesis; not runtime proof; not maintainer acceptance; not release certification
---

# Leviathan V3 Deep Repo Nuance Bundle

This page exists because the ZIP artifact could not be downloaded. It copies the useful content from the V3 deep-repo addendum into the wiki repo as ordinary Markdown.

Use this as a Codex-readable bundle for the next Leviathan wiki pass. It should be split into separate pages later, but this single page is enough for Codex to ingest the ideas without the ZIP.

## Current source baseline

Use the updated wiki baseline before older pages:

- `specs/leviathan-current/README` records the current source snapshot as `5dd98ac4ce7afeb9e4351787179c60208de6d23f`.
- The source ladder is: `docs/specs/**`, `docs/ARCHITECTURE.md`, `docs/VISION.md`, `docs/ROADMAP.md` + `mvp.md` together while they disagree, root `README.md` / `docs/NORTH_STAR.md` / `docs/README.md`, current source paths, design docs, then `.lev/pm/**`, `_inbox/**`, old local paths, chats, transcripts, and worker reports as provenance only.
- Current split verdicts include: four-plane technical model over README three-plane shorthand; graph noun vs `core/context-graph` package path; `ROADMAP.md` vs `mvp.md`; old damaged-checkout conflict claims demoted; narrow `@lev-os/eval` F01/N01 validation; System FlowMind YAML declarations not all runtime-enforced.

## Bottom-line assessment

Leviathan is real and interesting because it is not merely a prompt wrapper. It is trying to be an agent-human runtime where agents act through surfaces, under policy, with memory/context, events, receipts, execution boundaries, plugins, and human-loop surfaces.

Its strongest current identity:

```text
A pre-release, actively hardening agent-human runtime with strong contract-first architecture, broad source surfaces, and a narrow but real root-constraint validator.
```

Its weakest current identity:

```text
A high-entropy repo that often writes product/OS/enterprise/world-engine language ahead of runtime proof.
```

Good wiki language:

```text
Leviathan has real source-backed runtime surfaces and a serious architecture/spec stack. It should be described as pre-release and actively hardening, not enterprise-ready or fully launch-ready.
```

Bad wiki language:

```text
Leviathan is fully green, enterprise-ready, or already a validated world engine.
```

## What Leviathan is strongest at

### 1. Runtime architecture

The architecture is the strongest part. The root docs frame Leviathan as an open runtime for agent-human systems where agents can act through real surfaces, operate under explicit policy/control, remember and classify context, emit auditable events, and compose into products.

The important insight is not “better prompts.” It is runtime structure: context assembly, memory/graph state, execution boundaries, event models, policy, and gating.

### 2. Plane separation

The README uses a three-plane public shorthand: FlowMind, Graph, Event Bus.

Technical pages should use the stronger architecture split:

1. FlowMind = control / policy plane.
2. Orchestration = execution / scheduling plane.
3. Graph / context graph = state / knowledge plane.
4. Event Bus = causality / audit spine.

This is one of the best design choices. It prevents the common agent-framework collapse where one object does everything: policy, scheduling, memory, event emission, execution, UI, and provenance.

### 3. Contract-first operating style

Leviathan is unusually contract-heavy. It leans on specs, schemas, YAML declarations, receipts, event envelopes, proof gates, plugins, and explicit ownership. That gives it more survival potential than a prompt-only agent stack.

Relevant current surfaces include:

- `core/flowmind`
- `core/orchestration`
- `core/context-graph`
- `core/event-bus`
- `core/event-dispatch`
- `core/exec`
- `core/poly`
- `core/daemon`
- `core/eval`
- `core/testing`
- `core/reconciler`
- `core/world-model`
- `core/memory`
- `core/index`
- many plugins under `plugins/**`

### 4. Narrow but real F01/N01 root-constraint evaluator

`core/eval/src/constraint-manifold.ts` is the strongest currently inspectable Joshua-aligned implementation surface.

It defines:

- `F01_FINITUDE`
- `N01_NONCOMMUTATION`
- `E001_FINITUDE_VIOLATION`
- `E002_NONCOMMUTATION_VIOLATION`
- fatal severity
- provenance events
- finitude checks for execution bounds and finite explicit encodings
- non-commutation checks for dependency references, duplicate IDs, and DAG acyclicity via Kahn-style topological detection

Safe claim:

```text
Leviathan currently implements a narrow F01/N01 root-constraint validator in `@lev-os/eval` and wires it into System FlowMind loading.
```

Unsafe claim:

```text
Leviathan implements the full Codex Ratchet mathematical/proof/admissibility system.
```

### 5. System FlowMind loading

`core/flowmind/src/kernel/system-flowmind-loader.ts` is a real boot-surface mechanism. It reads `*.flow.yaml`, parses YAML, validates required fields, sorts by `boot_priority`, checks dependency DAGs, and binds native implementations. It binds `constraint-manifold` to `createConstraintManifold` from `@lev-os/eval`.

Safe claim:

```text
System FlowMind loading exists and can bind native implementations, especially the constraint manifold.
```

### 6. Plugin breadth

`plugins/PLUGINS.md` reports:

- 61 plugins with `config.yaml`
- 59 with README
- 47 with `src/`
- 38 with tests

This is real breadth. But breadth is not maturity. Plugin posture must be tracked separately from package presence.

## Where Leviathan is weak

### 1. Product proof lags product language

The README and North Star often use strong language: one runtime, every agent, every surface, operating system, enterprise, world model, moat.

The repo itself still says:

- universal context graph is not fully landed;
- system is not fully enterprise-ready;
- architecture is ahead of some implementation areas;
- surfaces and workflows are moving;
- current execution truth must be read through roadmap/proof receipts.

The wiki should call this ambition, not proof.

### 2. ROADMAP vs MVP split

`docs/ROADMAP.md` and `mvp.md` disagree about some execution-state claims.

The current wiki should preserve this split instead of picking the optimistic or pessimistic document by vibe.

Known split areas:

- Pentagon / Run Fabric proof;
- default daemon gate;
- `@lev-os/testing`;
- security P0 status;
- daemon/event automation;
- launch readiness.

Safe claim:

```text
Execution state is split-verdict. Read `ROADMAP.md` and `mvp.md` together, then use command receipts/proof dashboards for current truth.
```

### 3. System FlowMind is partly real, partly aspirational

`system-flowmind-executor.ts` explicitly says:

```text
For MVP, YAML stages pass at boot — they are declarations, not runtime checks. Runtime evaluation of YAML rules is Phase 2+.
```

So the honest split is:

- native F01/N01 validator: implemented narrowly;
- loader/order/dependency handling: implemented;
- YAML-declared ABAC, ratchet admission, provenance chain, translator boundary, TELO-style promotion, and other declared contracts: not all runtime-enforced yet.

### 4. QIT / world-model is the highest overclaim-risk zone

The QIT and world-model material is conceptually rich and strongly connected to Joshua Eisenhart. It is also the easiest place to slide into mythology.

Safe claim:

```text
Leviathan contains Joshua-origin QIT / engine / world-model design material and plugin-shell surfaces.
```

Unsafe claim:

```text
Leviathan already runs a validated QIT world engine.
```

`plugins/qit-engines/config.yaml` says `ships-with: false`. That matters. It has provenance and contract shape, not product proof.

`core/world-model/README.md` is even more explicit: the package gates nothing, is not bound to production decisions, produces zero gate decisions, and is loadable but not load-bearing until a real reconciler production scenario binds it.

### 5. Graph naming and package drift

The architecture uses the noun “Graph” as a runtime plane. Current source surfaces include `core/context-graph` and `core/graph-algorithms`. Older docs may still say `core/graph/**`.

Safe language:

```text
Graph remains the architecture-plane noun, but current source/package discussion should check `core/context-graph` and `core/graph-algorithms` before citing `core/graph`.
```

### 6. Repo entropy

Leviathan is high-entropy. It contains:

- active source code;
- specs;
- design docs;
- roadmap docs;
- `_inbox` proposals;
- `.lev/pm` provenance and session material;
- archived material;
- generated plugin manifests;
- workshop/intake material;
- wiki-produced synthesis;
- model-pressure output.

This is powerful as memory, but dangerous as truth. The wiki must keep source level labels on every claim.

## Delusion / overclaim risk register

Blocked unless a fresh proof packet earns it:

- Leviathan is enterprise-ready.
- Leviathan is launch-ready.
- Leviathan fully implements Codex Ratchet.
- Leviathan proves Joshua's QIT engine math.
- The QIT plugin is a working runtime engine.
- The world-model is production-wired.
- The default daemon/event loop is fully proven.
- All System FlowMinds enforce YAML logic at runtime.
- C3-C5 are formally derived from C1/C2 in current repo proof.
- AgentPing is fully product/prod-ready.
- AgentLease is universally enforced across Lev.
- Plugin count implies product maturity.

Use safer labels:

- `implemented-narrowly`
- `source-backed`
- `contract-backed`
- `design-backed`
- `plugin-shell`
- `ships-with:false`
- `proof-split`
- `owner-testimony`
- `provenance-only`
- `needs-current-proof-packet`

## Joshua Eisenhart contribution surfaces

Policy correction:

```text
Josh = Joshua Eisenhart = Codex Ratchet maker.
Nothing in Codex Ratchet should be described as coming from Leviathan OS.
If Leviathan and Codex Ratchet converge on root constraints, ratchet vocabulary, QIT state language, or admissibility structure, the default interpretation is not “Leviathan influenced Codex Ratchet.” The stronger default is Joshua-origin material entering Leviathan, independent convergence, or JP Smith's runtime architecture providing a compatible host for Joshua's constraints.
```

Evidence-backed Joshua contribution lanes in Leviathan:

1. Root constraints and constraint manifold vocabulary.
   - C1/F01 finitude and C2/N01 non-commutation appear in current FlowMind/eval surfaces.
2. Constraint tiering discipline.
   - C1/C2 are roots; C3-C5 are governance/derived-aligned unless promoted by evidence.
3. Ratchet/admissibility framing.
   - FlowMind ratchet hosting and ratchet admission language maps Joshua's Thread B / MEGABOOT / constraint ladder into Lev design surfaces.
4. Translator boundary.
   - Probabilistic-above / deterministic-below and no-inference hard-cut language is Joshua-aligned.
5. QIT engine vocabulary.
   - `docs/design/lev-qit-engine-glossary-eisenhart.md` is explicitly Joshua Eisenhart / iMessage corpus material.
6. QIT plugin source lineage.
   - `plugins/qit-engines/config.yaml` lists Josh source material including iMessages, Codex Ratchet, and Josh wiki intake.
7. Chain-not-collapse doctrine.
   - QIT plugin config preserves the idea that convergence to roots must preserve chain index and recombination path.
8. World-engine direction.
   - QIT / Holodeck / FEP / lawful state transition framing is Joshua-derived design/product material, not current product proof.

What this does not prove:

- It does not prove Joshua wrote all corresponding implementation code.
- It does not prove JP's runtime architecture is merely Joshua's system.
- It does not prove Codex Ratchet borrowed from Leviathan.
- It does not prove Leviathan implements all of Codex Ratchet.

## JP Smith / Leviathan contribution surfaces

Evidence-backed JP / Lev lane:

- Runtime architecture and implementation lane.
- FlowMind compiler/executor/parser/assembler direction.
- Runtime modules, package topology, plugin architecture, CLI, SDK, daemon, event bus, graph/context, and human-loop product surface framing.
- Host shape for Joshua's constraints: FlowMind/System FlowMinds/ratchet hosting.
- Original Wizard idea, by Joshua's owner-confirmed statement.
- Agent-human runtime product category: surfaces, AgentPing, AgentGuard, FlowMind, policy, events, runtime structure.

Cleanest bridge:

```text
Joshua contributed the constraint/admissibility/QIT/ratchet kernel ideas that Leviathan can host.
JP Smith contributed the Leviathan/FlowMind runtime architecture and the original Wizard idea that influenced Joshua's Wizard lineage.
Codex Ratchet remains Joshua's separate mathematical/proof/admissibility project, not a derivative of Leviathan OS.
```

## Deep subsystem topics to split into separate pages

### Constraint manifold eval

Topic page target:

```text
projects/leviathan-current/constraint-manifold-eval-deep-dive-2026-06-19.md
```

Core claims:

- `@lev-os/eval` has a narrow native F01/N01 validator.
- It checks finite bounds, finite explicit encodings, reference resolution, duplicate step IDs, and DAG cycles.
- It emits provenance allow/deny events.
- It does not enforce C3-C5 as native roots.
- It does not prove all runtime paths call the validator.

### System FlowMind loader / executor

Target:

```text
projects/leviathan-current/system-flowmind-loader-executor-audit-2026-06-19.md
```

Core claims:

- Loader reads/parses/sorts/binds System FlowMinds.
- Native binding exists for `constraint-manifold`.
- Executor fail-closes immutable native violations.
- YAML stages pass at boot for MVP.
- Phase 2+ is needed for deterministic YAML rule interpretation.

### World-model reactor / reconciler

Target:

```text
projects/leviathan-current/world-model-reactor-reconciler-map-2026-06-19.md
```

Core claims:

- `core/reconciler` is a surprise-gated, content-addressed loop.
- It has G1 admissibility, G2 materiality, G3 surprise.
- Current proof is hash/bootstrap / M1 style.
- Real world-model predictor binding remains a later seam.

### World-model quarantine

Target:

```text
projects/leviathan-current/world-model-experimental-quarantine-2026-06-19.md
```

Core claims:

- `core/world-model` is explicit experimental/unwired.
- It gates nothing and produces zero gate decisions.
- It contains real math/readout tests, but not production decisions.
- Determinism across runtimes remains gated.

### QIT engines plugin shell

Target:

```text
projects/leviathan-current/qit-engines-provenance-and-plugin-shell-2026-06-19.md
```

Core claims:

- `plugins/qit-engines` is `ships-with:false`.
- It has capabilities/config/schema language.
- It explicitly names Josh source lineage.
- It is a plugin contract shell / design substrate until handlers/tests/product proof exist.

### Plugin ecosystem posture matrix

Target:

```text
projects/leviathan-current/plugin-ecosystem-posture-matrix-v3-2026-06-19.md
```

Core claims:

- Plugin breadth is real.
- Plugin maturity must be split by `ships-with`, README, src, tests, poly surfaces, runtime tests, and product integration.
- No plugin should be promoted just because it appears in the manifest.

### Surface strategy: voice, vision, browser, GenUI

Target:

```text
projects/leviathan-current/surface-strategy-voice-vision-browser-genui-2026-06-19.md
```

Core claims:

- Voice config has serious session/routing/realtime/TTS architecture, but `ships-with:false` and `autostart:false`.
- Vision config has capture providers and PII/privacy settings, but `ships-with:false` and explicit provider selection.
- Browser plugin has FlowMind-driven browser ops and explicit engine routing, but product proof needs command/test receipts.
- GenUI is product-surface direction, not automatic shipped product proof.

### SDLC / autodev proof culture

Target:

```text
projects/leviathan-current/sdlc-autodev-proof-culture-2026-06-19.md
```

Core claims:

- SDLC plugin is one of the clearest places Lev becomes self-managing.
- It declares flows for spec lifecycle, commit gates, PEV, adversarial review, browser import, office-hours, eng-review, cross-model challenge, review-readiness, autodev, and Pentagon SDK/Poly binding.
- But live dispatch and full self-managing SDLC demo remain proof-gated.

### Memory / index / context economics

Target:

```text
projects/leviathan-current/memory-index-context-economics-2026-06-19.md
```

Core claims:

- Memory design uses hexagonal ports/adapters and five-fold memory type routing.
- It has provenance tracking and context budget management.
- README still contains many TODO / target claims, so it must be read as architecture + work-in-progress.

### Poly / Exec / Daemon split

Target:

```text
projects/leviathan-current/poly-exec-daemon-split-deep-dive-2026-06-19.md
```

Core claims:

- Exec owns execution SDK.
- Poly owns binder/router/projections.
- Daemon owns process/lifecycle supervision.
- CLI lives under Poly.
- Do not collapse these into one runtime blob.

### Event bus / dispatch proof ladder

Target:

```text
projects/leviathan-current/event-bus-dispatch-proof-ladder-2026-06-19.md
```

Core claims:

- Event Bus is architecture-level causality/audit spine.
- Help surfaces are not the same as live event automation.
- Manual projection does not prove daemon subscription, cron firing, trigger dispatch, executor handoff, or always-on automation.

### Security / release readiness

Target:

```text
projects/leviathan-current/security-release-readiness-gap-2026-06-19.md
```

Core claims:

- High audit passing is not full security readiness.
- Low/moderate vulnerabilities, env leakage classification, daemon/event automation, MCP servers, DX, examples, and launch docs remain separate gates.

### MCP / A2A readiness

Target:

```text
projects/leviathan-current/mcp-a2a-protocol-readiness-2026-06-19.md
```

Core claims:

- MCP/A2A language is strategically central.
- Current readiness must be separated by client adapters, server implementations, generated surfaces, help commands, and live end-to-end smoke tests.

### Onboarding / DX gap

Target:

```text
projects/leviathan-current/onboarding-dx-quickstart-gap-2026-06-19.md
```

Core claims:

- README quickstart exists.
- DX is not automatically good just because the quickstart exists.
- Installation, examples, `lev init`, docs validation, and first successful smoke need proof.

### Rust crates integration

Target:

```text
projects/leviathan-current/rust-crates-integration-map-2026-06-19.md
```

Core claims:

- Rust crates are important parallel surfaces.
- Crate existence is not binding proof to TS runtime.
- Each crate needs role: active runtime, parallel rewrite, validator, archive, or future substrate.

### Archive / inbox demotion

Target:

```text
projects/leviathan-current/archive-inbox-provenance-demotion-2026-06-19.md
```

Core claims:

- `_inbox/**` is not runtime truth.
- `_archive/**` is historical/non-owning.
- `.lev/pm/**` is provenance/decision context unless promoted.
- Old local checkout citations are historical only.

### Product category and moat nuance

Target:

```text
projects/leviathan-current/product-category-and-moat-nuance-2026-06-19.md
```

Core claims:

- Strong category: runtime substrate for agent-human systems.
- Possible moat: contracts, receipts, event/graph memory, policy, plugin surfaces, AgentPing/AgentGuard ecosystem, proof culture.
- Delusion risk: claiming moat before product adoption/runtime proof.

## Codex execution instructions

1. Read this page first.
2. Read:
   - `specs/leviathan-current/README`
   - `projects/leviathan-current/proof-backed-status-dashboard`
   - `projects/leviathan-current/nuanced-assessment-and-josh-provenance-2026-06-19`
   - `projects/leviathan-current/no-ratchet-from-leviathan-policy`
   - `projects/leviathan-current/wizard-origin-provenance-note-2026-06-19`
3. Split this bundle into the target pages listed above.
4. Patch `projects/leviathan-current/index.md` to include the new target pages.
5. Run wiki link/claim checks.
6. Do not edit `lev-os/leviathan` unless Josh explicitly asks.

## Non-negotiable attribution rules

- Codex Ratchet is Joshua Eisenhart's separate mathematical/proof/admissibility project.
- Do not say Ratchet comes from Leviathan.
- Do not say Leviathan proves or subsumes Ratchet.
- Do not say JP originated Ratchet root constraints.
- Do credit JP Smith for the original Wizard idea per owner-confirmed note.
- Do credit JP/Lev for the runtime/FlowMind/engine architecture lane.
- Do credit Joshua for the root constraint / admissibility / QIT / ratchet material where the repo and owner testimony support it.

## Current best one-paragraph verdict

Leviathan is a real, ambitious, high-entropy agent-runtime project with unusually good architectural instincts around policy/state/event/execution separation and unusually rich design memory. Its best parts are the contract-first runtime boundary, FlowMind as a policy language, event/receipt discipline, plugin breadth, and explicit host boundary for Joshua Eisenhart's root-constraint work. Its weak parts are equally clear: it over-narrates its future, mixes proof levels, carries stale docs beside current docs, and risks turning QIT/world-model language into product mythology before the runtime earns it. The wiki should describe Leviathan as a pre-release, actively hardening agent-human runtime whose current implementation includes narrow root-constraint enforcement and many runtime/plugin surfaces, and whose design/provenance layer contains substantial Joshua Eisenhart constraint/QIT material hosted by JP Smith's FlowMind/Leviathan runtime architecture.
