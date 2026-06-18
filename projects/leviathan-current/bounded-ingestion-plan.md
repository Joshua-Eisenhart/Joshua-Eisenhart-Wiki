---
title: Leviathan Current Bounded Ingestion Plan
created: 2026-06-17
updated: 2026-06-18
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

The local checkout `/Users/joshuaeisenhart/GitHub/leviathan` was deleted on 2026-06-18 after the wiki lane mutated it. New ingestion must read from the live GitHub website/remote:

- `https://github.com/lev-os/leviathan`
- `https://raw.githubusercontent.com/lev-os/leviathan/main/<path>`
- `https://api.github.com/repos/lev-os/leviathan/contents/<path>?ref=main`

For stable evidence, record the remote commit SHA and cite raw URLs with that SHA. If website/raw/API access is insufficient, Josh has authorized downloading Leviathan again as a clean fresh clone from `https://github.com/lev-os/leviathan.git`. Prefer a disposable clone under `/tmp`, keep it read-only for the wiki pass, record the remote URL, SHA, and clean status, and delete it after the pass. If a persistent checkout is needed, clone fresh rather than recovering the deleted damaged checkout.

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
- Historical local repo path, remote, HEAD, dirty-state caveat, and file counts are recorded.
- New packets record GitHub website/raw/API source URLs plus the remote commit SHA used.
- Authority order is explicit.

### Packet 1 — Current authority docs

Status: **completed 2026-06-17**.

Read and synthesize only current authority docs through GitHub website/raw/API source mode:

- root `README.md` via `https://github.com/lev-os/leviathan` or raw URL
- `docs/README.md` via raw URL
- `docs/NORTH_STAR.md` via raw URL
- `docs/ROADMAP.md` via raw URL
- `docs/ARCHITECTURE.md` via raw URL
- `docs/specs/README.md` via raw URL
- high-signal `docs/specs/*.md` contracts via raw/API listing

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

Status: **source-map completed 2026-06-17; full runtime/build-test map completed 2026-06-18; runtime verification still open**.

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

Use raw URLs, GitHub website file views, the Contents API, or a clean fresh clone for this packet. Do not rely on `/Users/joshuaeisenhart/GitHub/leviathan` unless it has been freshly recloned and its SHA/clean status are recorded.

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

Full runtime/build-test pass landed:

- `runtime-module-map-full-2026-06-18.md`
- `runtime-build-test-surface-map-2026-06-18.md`
- `packet-2-full-runtime-map-receipt-2026-06-18.md`

Success check:

- Every page cites exact files read.
- Every implementation claim has a support label: `observed file`, `inferred architecture`, `roadmap claim`, `not checked`, or `open`.
- Packet 2 preserves the observed conflict markers as a runtime blocker instead of claiming event-bus health.
- Runtime verification remains open: no package tests/typechecks or end-to-end smokes were run in Packet 2.

### Packet 3 — Product surfaces and human-loop layer

Status: **partial product-surface map completed 2026-06-18; GenUI/voice/product-positioning pages still open**.

Read:

- AgentPing and surface docs/code in repo and submodules.
- AgentLease / permission / policy / approval surfaces where present.
- UI/voice/GenUI surfaces.
- related existing `projects/levos` product notes.

Landed pages:

- `agentping-human-loop-surfaces.md`
- `agentlease-scoped-authority.md`
- `packet-3-product-surfaces-receipt-2026-06-18.md`

Still-open planned pages:

- `genui-voice-and-surface-strategy.md`
- `product-positioning-and-open-source-flywheel.md`

Claim ceiling:

- Distinguish implemented surfaces from positioning, roadmap, and idea-ledger material.
- AgentPing and AgentLease are source-supported product/runtime concepts; runtime health and full product integration remain unverified until bounded tests/builds run.

### Packet 4 — Josh constraint contribution map

Status: **constraint-boundary tranche completed 2026-06-18; runtime-translation map still open**.

Read:

- `wizard/harness-consolidated/14_leviathan_os_constraint_map.md`
- current Leviathan constraints docs/specs
- FlowMind kernel/system declaration docs
- previous `projects/levos` pages
- selected Josh/JP chat candidates after provenance split

Landed pages:

- `josh-root-constraints-in-leviathan.md`
- `lev-five-constraints-vs-f01-n01.md`
- `codex-ratchet-vs-leviathan-boundary.md`
- `packet-4-constraint-boundary-receipt-2026-06-18.md`

Still-open planned page:

- `constraint-runtime-translation-map.md`

Success check:

- Finitude/non-commutation are root where sources support that.
- Nominalized reality/ratchet/locality remain derived unless a repo source explicitly treats them as independent kernel constraints.
- No Codex Ratchet sim claim is imported as a Lev implementation claim.

### Packet 5 — Chat/transcript provenance processing

Status: **promotion protocol plus first bounded tranche completed 2026-06-18; broad ledger work still open**.

Use `source-inventory-2026-06-17.json` chat candidates as the queue.

For each source, classify passages as:

- Josh-owner statement.
- JP / Lev-dev statement.
- assistant/model elaboration.
- repo evidence reference.
- product speculation.
- design intent.
- implementation status.

Landed pages:

- `chat-evidence-promotion-protocol.md`
- `chat-tranche-1-processing-2026-06-18.md`
- `packet-5-chat-tranche-receipt-2026-06-18.md`

Still-open broader pages:

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
