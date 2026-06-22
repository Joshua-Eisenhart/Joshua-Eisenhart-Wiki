---
title: World Engine Graph Patch Algebra
created: 2026-06-21
updated: 2026-06-21
type: concept
status: proposal_design_current
claim_ceiling: architecture concept; not implemented canon unless host-consumed by Lev/ClaimGate
---

# World Engine Graph Patch Algebra

## Core idea

The current Leviathan developer frame says:

```text
accepted canon/code goes into the world model
and the graph projects out from that
world engine -> wiki / memory / Lev flows / code -> graph
wiki/skills + folder structure = file-based graph working space
the engine is a plugin system
proposals are graph patches
```

This is the missing deeper abstraction underneath Spinor Memory.

## Definition

A **WorldModelGraph** is the typed graph of accepted project state:

```text
canon doctrine
code surfaces
wiki pages
skills
folder structure
FlowMind graphs
Eval suites
Effect receipts
ClaimGate receipts
sims/proofs
frontiers
branches
graveyards
```

A **GraphPatch** is any bounded proposed mutation to that world model:

```text
doc patch
ontology patch
code patch
sim patch
eval-pack patch
policy patch
gate patch
schema patch
frontier patch
branch split
rejection/graveyard patch
```

A **GateOperator** acts on a GraphPatch and classifies whether the patch can enter the accepted world-model state.

## Patch algebra

Graph patches are not commutative:

```text
owner_approve ∘ source_bind != source_bind ∘ owner_approve
host_consume ∘ owner_approve != owner_approve ∘ host_consume
eval_measure ∘ observe_effect != observe_effect ∘ eval_measure
canon_promote ∘ seal_receipt != seal_receipt ∘ canon_promote
```

This is the operational reason Spinor Memory appears. The system needs a representation that distinguishes the same content under different ordered operator histories.

## Relation to Leviathan

Leviathan already has the runtime split:

```text
FlowMind     = graph authoring / policy plane
Graph State  = world-model state / knowledge plane
Event Bus    = causality spine
Exec         = ACT through blessed ports
Effect       = EffectEnvelope + ObservedEffect + EffectReceipt
Eval         = measurements + proof discharge
Semantic Control = NextTickPlan from scored facts + lineage + policy
Ledger       = append-only refs
```

GraphPatch is the missing shared unit connecting these surfaces.

## Relation to Codex-Ratchet

Codex-Ratchet supplies the discipline:

```text
mine first
one object / one claim / one card
proof/sim gates
fresh audit
receipts as the record
claim ceilings
no copy-sweeps
imports re-earn status
```

So Codex does not dump text into the world model. It proposes bounded graph patches with source/proof/sim/eval evidence.

## Relation to ClaimGate

ClaimGate is the authority spine for accepting graph patches:

```text
proposal -> approval -> request -> receipt
```

v41 narrows enforcement: enforcing gates require trust-root verified owner and host authority. Therefore the graph patch state must preserve:

```text
proposal_only
owner_approved
host_requested
host_receipted
trust_root_verified
effect_observed
eval_measured
frontier_promoted
graveyarded
```

## Relation to Spinor Memory

Spinor Memory is not the graph itself. It is an orientation-preserving read model over graph patch trajectories.

```text
WorldModelGraph = what has been accepted
GraphPatch      = proposed mutation
ReceiptLog      = what actually happened
SpinorMemory    = orientation of a claim/patch under ordered operators
BasinDigger     = stability classification of a patch relative to the active object
```

## Claim ceiling

Do not call this a completed world engine. This is a graph-patch algebra proposal for deep-patching Leviathan and keeping Codex-Ratchet sims/proofs inside one admissibility system.
