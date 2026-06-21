---
title: Research Ratchet read-first — Spinor Memory, Attractor Basin Digger, and Leviathan deep patch
created: 2026-06-21
updated: 2026-06-21
type: router
status: current-research-overlay
claim_ceiling: wiki consolidation/router only; no repo promotion; no runtime admission; no full spinor-algebra claim
tags: [research-ratchet, spinor-memory, attractor-basin, leviathan, claimgate, codex-ratchet, graph-patch]
---

# Research Ratchet read-first — Spinor Memory, Attractor Basin Digger, and Leviathan deep patch

Load this after the Hermes/project front door and before using the Spinor Memory / Attractor Basin / Leviathan deep-patch material.

## One-line consolidation

**Leviathan is the runtime. Codex-Ratchet is the research discipline. ClaimGate is the authority transition spine. Research Ratchet is the project-harness protocol. Spinor Memory is the oriented project-state representation. Attractor Basin Digger is the stability controller.**

The deeper concept is not "a spinor database." It is:

> **proof-carrying, event-sourced world-model graph patches under admissible operators.**

Spinor Memory and Attractor Basin Digger are two sides of that deeper object:

- **Spinor Memory** stores the oriented state of a claim/object under ordered gates.
- **Attractor Basin Digger** decides whether the next proposed graph patch deepens, leaks, splits, kills, or lacks evidence relative to the active project basin.

## Claim ceiling

Allowed: JSON-first oriented project-memory design; graph-patch/world-model architecture proposal; Lev-native project harness design; ClaimGate lifecycle mapping; Codex sim/basin-dynamics work plan; non-authoritative memory/read-model layer.

Not allowed from this page alone: no canon promotion; no "quantum memory" claim; no full Clifford/spinor algebra claim; no claim that vector DBs are obsolete; no claim that Spinor Memory proves truth; no claim that Leviathan runtime integration is complete; no claim that v41 solves KMS/HSM, production host authority, or all external seams.

## Load order

1. [[projects/research-ratchet/world-model-graph-patch-2026-06-21]]
2. [[projects/research-ratchet/spinor-memory-and-attractor-basin-digger-2026-06-21]]
3. [[projects/research-ratchet/leviathan-deep-patch-plan-2026-06-21]]
4. [[projects/research-ratchet/claimgate-authority-state-machine-2026-06-21]]
5. [[projects/research-ratchet/codex-sim-basin-dynamics-plan-2026-06-21]]
6. [[concepts/spinor-memory]]
7. [[concepts/attractor-basin-digger]]

## Current synthesis

The project was initially framed as "spinor memory" because vectors flatten memory into proximity. The repo/wiki evidence points deeper: the system needs memory for **ordered admissibility transformations**. A vector index can find related chunks, but it does not preserve whether a claim is pre-approval, post-request, host-receipted, verified, graveyarded, split, or frontier-promoted.

The right object is therefore a **world-model graph patch**:

```text
proposal graph patch
  -> admission gate
  -> ACT / observed effect
  -> eval measurement
  -> receipt
  -> graph-state successor
  -> next tick plan
```

This matches the Lev core loop and the ClaimGate chain:

```text
proposal -> approval -> request -> receipt
```

and it matches the Codex discipline:

```text
one object -> mine first -> card -> fan-out -> verify -> fresh audit -> harden -> commit -> record
```

## Minimum new primitives

| Primitive | Meaning | Authority boundary |
| --- | --- | --- |
| `WorldModelGraph` | Accepted canon/code/docs/receipts as the current project state. | Read/write through receipts and ledgers. |
| `GraphPatchProposal` | Proposed ontology/doc/code/memory/runtime update. | No authority until admitted and receipted. |
| `SpinorMemoryCell` | Oriented state of a claim/object under gate history. | Projection/read model unless receipt-backed. |
| `MemoryOperator` | Typed gate/action that transforms a cell or graph patch. | Legal only if preconditions and authority state pass. |
| `OperatorTrace` | Ordered history of applied operators. | Part of identity; not metadata fluff. |
| `AttractorBasinMap` | Stable project basin, invariants, boundaries, leakage edges, graveyard collisions. | Controller/read model; does not promote. |
| `ColdStartPacket` | Portable reconstruction of current basin/frontier/claim ceilings for any model. | Compiled from receipts and source refs. |
| `EffectRef` / `EvalRef` / `ReceiptRef` | Observed action, measurement/proof, and state-transition seal. | Promotion depends on these, not prose. |

## Next build direction

```text
v0 = JSON-first graph-patch + SpinorMemoryCell + AttractorBasinDigger read model.
v1 = ColdStartPacket compiler from Codex/Wiki/ClaimGate receipts.
v2 = Lev Graph State / Event Bus integration.
v3 = vector-first, spinor-reranked retrieval.
v4 = Codex sim/basin receipt integration.
v5 = optional finite Clifford/GA experiment if v0-v4 earn it.
```

## Source anchors

This page is a consolidation/router. It does not promote any claim by itself. Primary anchors: `lev-os/leviathan/README.md`, `docs/specs/spec-flowmind.md`, `docs/specs/spec-effect.md`, `docs/specs/spec-eval.md`, `docs/specs/spec-semantic-control.md`, `Joshua-Eisenhart/Codex-Ratchet/system_v6/README.md`, `Joshua-Eisenhart/Codex-Ratchet/AGENTS.md`, `projects/codex-ratchet/current-canonical-plan-and-anti-drift-2026-06-08.md`, `projects/codex-ratchet/geometry-sim-program-canonical-2026-06-10.md`, uploaded ClaimGate audits, and the uploaded `research_ratchet_spinor_memory_project_harness_v0` package.
