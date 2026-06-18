---
title: Leviathan Current Bounded Ingestion Plan
created: 2026-06-17
updated: 2026-06-17
type: ingestion-plan
status: active plan
claim_ceiling: work plan; not completed ingestion
---

# Leviathan Current Bounded Ingestion Plan

## Goal

Turn the current `lev-os/leviathan` repo plus relevant Josh/JP chat material into a markdown wiki that can explain:

- what Leviathan is;
- what currently exists;
- what is intended but not landed;
- how the runtime works;
- where Josh's root constraints appear;
- where JP's implementation choices and product strategy appear;
- which claims are repo-current, design-intent, chat-derived, legacy, or speculative.

## Hard boundary

This is wiki work, not repo mutation. Do not edit the Leviathan repo during ingestion unless Josh explicitly assigns a repo patch task.

## Packet sequence

### Packet 0 — Scaffold and inventory

Status: **completed 2026-06-17**.

Artifacts:

- `README.md`
- `read-first.md`
- `source-inventory-2026-06-17.md`
- `source-inventory-2026-06-17.json`

Success check:

- Project folder exists.
- Current repo path, remote, HEAD, dirty-state caveat, and file counts are recorded.
- Authority order is explicit.

### Packet 1 — Current authority docs

Status: **completed 2026-06-17**.

Read and synthesize only current authority docs:

- root `README.md`
- `docs/README.md`
- `docs/NORTH_STAR.md`
- `docs/ROADMAP.md`
- `docs/ARCHITECTURE.md`
- `docs/specs/README.md`
- high-signal `docs/specs/*.md` contracts

Output pages:

- `what-is-leviathan.md`
- `current-state-and-roadmap.md`
- `architecture-planes-and-ownership.md`
- `contract-surface-map.md`

Landed pages:

- `what-is-leviathan.md`
- `current-state-and-roadmap.md`
- `architecture-planes-and-ownership.md`
- `contract-surface-map.md`
- `josh-contribution-signal-radar.md` (starter Packet 4 radar added early because contribution discovery is central to Josh's request)

Stop condition:

- If specs contradict architecture or roadmap, preserve the contradiction instead of smoothing it.

### Packet 2 — Runtime/module map

Status: **source-map completed 2026-06-17; runtime verification still open**.

Read code and package contracts by ownership boundary, not whole repo at once:

- `core/flowmind/`
- `core/orchestration/`
- `core/graph/`
- `core/event-bus/`
- `core/exec/`
- `core/poly/`
- `core/daemon/`
- `plugins/core-*` plus broader plugin manifests/configs
- `core/domain/`

Starter pages landed:

- `runtime-module-map-start.md`
- `flowmind-control-plane-start.md`
- `event-graph-orchestration-start.md`

Full source-map pages landed:

- `flowmind-control-plane.md`
- `graph-state-knowledge-plane.md`
- `event-bus-causality-plane.md`
- `orchestration-execution-plane.md`
- `exec-poly-daemon-boundary.md`
- `plugin-ownership-map.md`
- `packet-2-runtime-map-receipt-2026-06-17.md`

Success check:

- Every page cites exact files read.
- Every implementation claim has a support label: `observed file`, `inferred architecture`, `roadmap claim`, `not checked`, or `open`.
- Packet 2 preserves the observed conflict markers as a runtime blocker instead of claiming event-bus health.
- Runtime verification remains open: no package tests/typechecks or end-to-end smokes were run in Packet 2.

### Packet 3 — Product surfaces and human-loop layer

Read:

- AgentPing and surface docs/code in repo and submodules.
- AgentLease / permission / policy / approval surfaces where present.
- UI/voice/GenUI surfaces.
- related existing `projects/levos` product notes.

Output pages:

- `agentping-human-loop-surfaces.md`
- `agentlease-scoped-authority.md`
- `genui-voice-and-surface-strategy.md`
- `product-positioning-and-open-source-flywheel.md`

Claim ceiling:

- Distinguish implemented surfaces from positioning, roadmap, and idea-ledger material.

### Packet 4 — Josh constraint contribution map

Read:

- `wizard/harness-consolidated/14_leviathan_os_constraint_map.md`
- current Leviathan constraints docs/specs
- FlowMind kernel/system declaration docs
- previous `projects/levos` pages
- selected Josh/JP chat candidates after provenance split

Output pages:

- `josh-root-constraints-in-leviathan.md`
- `lev-five-constraints-vs-f01-n01.md`
- `constraint-runtime-translation-map.md`
- `codex-ratchet-vs-leviathan-boundary.md`

Success check:

- Finitude/non-commutation are root where sources support that.
- Nominalized reality/ratchet/locality remain derived unless a repo source explicitly treats them as independent kernel constraints.
- No Codex Ratchet sim claim is imported as a Lev implementation claim.

### Packet 5 — Chat/transcript provenance processing

Use `source-inventory-2026-06-17.json` chat candidates as the queue.

For each source, classify passages as:

- Josh-owner statement.
- JP / Lev-dev statement.
- assistant/model elaboration.
- repo evidence reference.
- product speculation.
- design intent.
- implementation status.

Output pages:

- `chat-provenance-ledger.md`
- `josh-jp-shared-ideas-ledger.md`
- `unresolved-interpretations-and-questions.md`

Hard rule:

- No chat-derived claim becomes repo-current truth until matched to current file/code/test evidence or explicitly marked as intent/speculation.

### Packet 6 — Current wiki synthesis

Only after packets 1–5 have receipts, write the explanatory layer:

- `leviathan-in-plain-english.md`
- `how-leviathan-functions.md`
- `what-leviathan-can-do-now.md`
- `what-leviathan-could-become.md`
- `open-questions-for-josh-and-jp.md`

Success check:

- A new LLM can answer basic questions without reading the whole repo.
- Every major statement routes back to current docs/code, design intent, or provenance ledger.

## Model/worker routing

Use separate model lanes because this is too large for one context:

- **Controller/editor**: Hermes in this chat, bounded and verified.
- **Heavy read/write workers**: codex2 or Claude Code Sonnet/high for source packet drafting when useful.
- **Preferred pressure/synthesis lanes**: OpenRouter Fusion and GLM 5.2 should be tried before Opus 4.8 when available, because Josh currently expects them to be stronger for this Leviathan read.
- **Other pressure lanes**: Grok/Gemini/Opus only when their independent read changes the questions, gaps, or falsifiers.

Worker/model outputs are receipts and pressure, not truth. The controller must reread written files and verify path/link/claim ceilings before marking pages as usable.
