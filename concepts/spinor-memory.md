---
title: Spinor Memory
created: 2026-06-21
updated: 2026-06-21
type: concept
status: proposal_design_current
claim_ceiling: JSON-first oriented memory/read-model; not quantum memory; not proof authority
---

# Spinor Memory

## Definition

Spinor Memory stores project claims as **oriented states under ordered admissibility transformations**.

The key object is not a note. It is:

```text
claim + frame + operator trace + gate status + receipt lineage + basin context
```

## Why this exists

Vector memory answers:

```text
What is semantically close?
```

Project-ratchet memory must answer:

```text
What is this claim after these gates acted on it in this order?
What status does it have?
What branch is it on?
What proof/effect receipts back it?
What transformations are still legal?
What basin does it belong to?
```

## v0 representation

```text
SpinorMemoryCell
  cell_hash
  object_id
  basin_id
  branch_id
  claim_text
  claim_ceiling
  authority_state
  verification_mode
  orientation
    left
    right
    chirality
    phase
  state_vector
  operator_trace
  allowed_next_ops
  blocked_ops
  graveyard_hits
  source_refs
  receipt_refs
  effect_refs
  eval_refs
  vector_ref
  supersedes
```

## The spinor reading

v0 does not need true spinor algebra. It needs the correct abstraction boundary:

```text
state under ordered operators
```

Later versions may attach:

```text
Clifford/multivector coefficients
rotor / left-right action
grade signature
phase/chirality invariants
operator noncommutation tables
```

But the v0 claim ceiling stays:

```text
JSON-first oriented project memory.
No quantum claim.
No canon promotion.
No proof authority.
```

## Noncommutation examples

```text
Gate(Axiom(Claim)) != Axiom(Gate(Claim))
source_bind -> owner_approve -> host_consume != host_consume -> owner_approve -> source_bind
observe_effect -> eval_measure != eval_measure -> observe_effect
```

## Required invariants

1. Same `claim_text` with different `operator_trace` produces different `cell_hash`.
2. Operator order matters.
3. `host_consume` before `owner_approve` fails.
4. `promote_frontier` before `ObservedEffect + Eval + Receipt` fails.
5. LLM prose cannot mutate lifecycle status.
6. Dashboard/scorecard green cannot promote status.
7. Fixture authority overclaim hits graveyard.
8. MassRun/UI/model expansion without admission power is basin leakage.
9. ColdStartPacket reconstructs object/frontier/basin without chat history.
10. SpinorMemory is a read/control model unless backed by EffectReceipt/Eval/ClaimGate refs.

## Role in Leviathan

Spinor Memory belongs under Graph State and Event Bus, with FlowMind policy hooks.

It should not be a side proof stack.

```text
FlowMind proposes operator
Exec performs ACT
Effect records ObservedEffect
Eval measures proof obligation
ClaimGate handles authority transition
Ledger records refs
SpinorMemory updates orientation from the sealed refs
```

## Role in Codex-Ratchet

Codex-Ratchet sims can emit SpinorMemoryCells when they produce order-sensitive, branch-sensitive, or claim-status-sensitive evidence.

Examples:

```text
A->B vs B->A sim result
free/restricted/quotiented/ratcheted mode classification
basin escape case
same-carrier geometry branch split
nonassoc associator witness survival/erasure under quotient
```

These cells are not proof. They are structured memory for the next gate.
