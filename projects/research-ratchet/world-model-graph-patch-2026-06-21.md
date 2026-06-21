---
title: Research Ratchet world-model graph-patch architecture
created: 2026-06-21
updated: 2026-06-21
type: architecture
status: current-research-overlay
claim_ceiling: design proposal; no runtime admission; no canon promotion
tags: [research-ratchet, world-model, graph-patch, leviathan, event-sourcing, proof-carrying-state]
---

# Research Ratchet world-model graph-patch architecture

## Core claim

The missing abstraction under Spinor Memory and Attractor Basin Digger is:

> **proof-carrying world-model graph patch algebra.**

A project harness should not store memory as a bag of notes. It should maintain a world model whose accepted state is updated by typed, receipted graph patches.

The developer handoff phrase was: accepted canon/code goes into the world model, and the graph projects out from that. That implies:

```text
accepted canon/code/docs/receipts
  -> world model
  -> graph projections
  -> FlowMind policies/evaluator bindings
  -> graph patch proposals
  -> gates/effects/evals/receipts
  -> accepted successor world model
```

## Why this is deeper than a spinor database

Spinor Memory is useful because it names orientation and ordered transformation history. But the deeper infrastructure is not a database type. It is a state machine:

```text
state S_t
proposal P_t
operator sequence O_1...O_n
evidence E_t
policy verdict V_t
receipt R_t
successor S_(t+1)
```

The word `spinor` should be kept as a representation metaphor/design target for orientation-sensitive state, not as the root authority claim.

## Graph patch as the project unit

A `GraphPatchProposal` can propose ontology, docs, code, schemas, memory, sim rows, or runtime edges.

```json
{
  "kind": "GraphPatchProposal",
  "object_id": "research-ratchet",
  "patch_id": "patch:spinor-memory-v0",
  "patch_kind": "ontology_doc_code_memory",
  "source_refs": [],
  "claim_ceiling": "design proposal",
  "adds": [],
  "modifies": [],
  "removes": [],
  "required_gates": ["source_bound", "authority_checked", "observed_effect", "eval_measured", "receipt_sealed"],
  "forbidden_promotions": ["canon_without_receipt", "proof_from_dashboard_green", "spinor_memory_as_truth_engine"]
}
```

## Gate as operator

A gate is not just a yes/no filter. In the project harness it is a typed operator that transforms admissibility state:

```text
source_bind
owner_approve
host_request
host_consume
observe_effect
eval_measure
seal_receipt
promote_frontier
graveyard
split_branch
```

Order is part of identity:

```text
owner_approve -> host_consume
```

is not equivalent to:

```text
host_consume -> owner_approve
```

## Receipt as state-transition seal

A receipt is the durable witness that a transition was attempted, observed, measured, and/or admitted. The project state should update only from receipts and ledger refs, not from prose, dashboards, or route summaries.

```text
proposal prose       = claim source
typed observation    = measurement input
eval result          = proof/evidence projection
EffectReceipt        = observed-effect seal
ClaimGate receipt    = authority transition seal
graph successor      = derived accepted state
```

## Projections are not authority

Dashboards, scorecards, semantic indexes, vector DBs, wiki topic maps, and UI surfaces are projections. They can help operators read the state. They cannot mutate accepted state.

## Patch lifecycle

```text
INGEST source refs
OBSERVE current world model + receipts
PROPOSE graph patch
ADMISSION check authority/scope/readiness
ACT through blessed runtime
OBSERVE effect
VERIFY eval/proof/drift/gate measurements
ADAPT next tick plan
DECIDE accepted/rework/escalate/kill/split
UPDATE graph state + receipts + basin map
EMIT projections
```

## Architecture implication for Leviathan

Leviathan should get a project-harness graph layer, not just a memory plugin.

The layer should expose `GraphPatchProposal`, `PatchAdmission`, `PatchEffectLink`, `PatchEvalLink`, `PatchReceiptLink`, `WorldModelSnapshot`, `AttractorBasinMap`, `SpinorMemoryCell`, and `ColdStartPacket`.

This gives FlowMind a real policy substrate: it can ask whether a next patch is legal under the current graph state before routing work.
