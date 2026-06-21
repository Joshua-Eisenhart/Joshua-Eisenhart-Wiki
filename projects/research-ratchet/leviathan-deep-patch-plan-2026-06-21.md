---
title: Leviathan deep patch plan — Research Ratchet graph-state harness
created: 2026-06-21
updated: 2026-06-21
type: implementation-plan
status: current-research-overlay
claim_ceiling: patch plan only; not landed runtime
tags: [leviathan, flowmind, graph-state, eval, effect, semantic-control, research-ratchet]
---

# Leviathan deep patch plan — Research Ratchet graph-state harness

## Purpose

Patch Leviathan so the project harness is not just chat memory or retrieval. It should be a runtime graph-state system that can preserve and update an oriented project object through gated, receipted state transitions.

## Placement inside Lev

Use the existing Lev split:

```text
FlowMind = authoring/control/policy plane
Graph State = state/knowledge/world model plane
Event Bus = causality spine
Exec = blessed ACT path
Effect = reality envelope
Eval = proof/measurement brain
Semantic Control = adaptive loop decision
Ledger = append-only refs
```

Research Ratchet should be implemented as a Graph State + Event Bus + FlowMind policy package, with Effect/Eval/ClaimGate refs as the only authority-bearing inputs.

## New package boundary

Candidate package:

```text
packages/research-ratchet-graph-state/
```

or, if core-owned:

```text
core/graph-state/research-ratchet/
```

Objects: `WorldModelGraph`, `GraphPatchProposal`, `PatchAdmission`, `SpinorMemoryCell`, `MemoryOperator`, `OperatorTrace`, `AttractorBasinMap`, `ColdStartPacket`, `BasinClassification`, and `PatchReceiptLink`.

## Runtime hooks

| Lev surface | Hook | Research Ratchet behavior |
| --- | --- | --- |
| FlowMind | `onPlanProposed` | Validate patch operator against basin policy and current cell. |
| Orchestration | `onLaneScheduled` | Keep topology and branch/fanout lineage explicit. |
| Exec | `onActStarted/onActResult` | Attach ACT refs; no proof decision. |
| Effect | `onObservedEffect/onEffectReceipt` | Attach observed effect and sealed effect refs. |
| Eval | `onMeasurement/onGateProof/onProofBundle` | Attach measurement/proof refs and compute evidence status. |
| Semantic Control | `onNextTickPlan` | Read basin/cell state to plan next move without weakening source intent. |
| Ledger | `onSeal` | Append successor cells and graph snapshots. |
| ClaimGate | `onProposal/onApproval/onRequest/onReceipt` | Update authority lifecycle state. |

## FlowMind integration

FlowMind should not mutate project authority directly. It should compile graph-patch proposals into runtime-neutral actions:

```yaml
graph_patch:
  patch_id: patch:spinor-memory-v0
  object_id: research-ratchet
  intended_effect: add_spinor_memory_read_model
  required_gates:
    - source_bound
    - authority_checked
    - observed_effect
    - eval_measured
    - receipt_sealed
  forbidden_promotions:
    - canon_without_receipt
    - proof_from_llm_prose
```

Then FlowMind branches on code-owned gate results and policy facts, not model prose.

## Eval integration

Eval should treat Research Ratchet as a Project Harness:

- eval suites for operator legality;
- adversarial probes for false-green paths;
- probe ledger for cheap paths and prior gaming attempts;
- non-static gap ledger for live host/trust-root/provider/receipt issues;
- proof bundle refs for authority transitions;
- scorecards as projections, never truth stores.

## Effect integration

Every mutating graph patch must flow through Effect:

```text
EffectEnvelope
  -> ADMISSION_GATE
  -> ACT
  -> ObservedEffect
  -> VERIFY_GATE
  -> EffectReceipt
```

If a patch would update accepted graph state without ObservedEffect, it must be blocked.

## Event sourcing

All accepted changes should be rebuildable from an append-only stream:

```text
GraphPatchProposed
PatchAdmissionChecked
EffectObserved
EvalMeasured
ClaimGateTransitionReceipted
PatchAccepted
PatchRejected
PatchGraveyarded
BasinMapUpdated
ColdStartPacketCompiled
```

## ColdStartPacket

This is the externalized big circle for weaker models:

```json
{
  "kind": "ColdStartPacket",
  "object_id": "research-ratchet",
  "active_basin": "lev-native-project-harness",
  "frontier": "...",
  "claim_ceiling": "...",
  "active_cell_hashes": [],
  "graveyard_hits": [],
  "next_allowed_moves": [],
  "forbidden_moves": [],
  "receipt_index_refs": []
}
```

## Phases

1. **v0 read-model:** JSON cells, operators, basin classifier, schema validation.
2. **v1 packet compiler:** compile ColdStartPacket from wiki/Codex/ClaimGate refs.
3. **v2 Lev hooks:** FlowMind plan check, Effect/Eval/ledger refs.
4. **v3 hybrid retrieval:** vector-first, spinor/basin rerank.
5. **v4 graph-patch event sourcing:** rebuild project state from event log.
6. **v5 mathematical experiment:** optional operator algebra / finite Clifford representation.
