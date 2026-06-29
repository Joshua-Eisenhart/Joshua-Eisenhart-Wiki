---
title: Research Ratchet
created: 2026-06-21
updated: 2026-06-21
type: project-front-door
status: proposal_design_current
claim_ceiling: architecture/update pack; not host-consumed canon; not proof of full runtime integration
sources:
  - projects/codex-ratchet/current-canonical-plan-and-anti-drift-2026-06-08
  - projects/codex-ratchet/geometry-sim-program-canonical-2026-06-10
  - concepts/current-canonical-spine
  - Lev docs/specs/spec-eval.md
  - Lev docs/specs/spec-effect.md
  - Lev docs/specs/spec-flowmind.md
  - Lev docs/specs/spec-semantic-control.md
  - ClaimGate v39/v40/v41 audits and packages
---

# Research Ratchet

Research Ratchet is the project-harness protocol that proposes a bridge from Codex-Ratchet discipline to Leviathan runtime surfaces.

It exists so long-horizon project coherence is held by infrastructure rather than by whichever model is currently loaded.

## One-line definition

> Research Ratchet is a proposal for an event-sourced admissibility system for maintaining a world-model graph under receipt-backed graph patches.

## The deeper abstraction

The current work started under the name **Spinor Memory**, but the deeper object is broader:

```text
event-sourced admissibility geometry over a world-model graph
```

In that frame:

```text
WorldModelGraph  = accepted canon/code/wiki/skills/flows/folder-state as typed graph
GraphPatch       = any proposed ontology/doc/code/sim/policy update
GateOperator     = admissibility operator over a proposed patch
Receipt          = event-sourced proof/effect transition record
SpinorMemory     = orientation/read model over ordered patch/gate history
AttractorBasin   = stability region around the active bounded project object
BasinDigger      = control layer that classifies next moves as deepen/leak/split/kill/insufficient-evidence
ClaimGate        = authority chain for promotion/admission transitions
Leviathan        = target host/runtime surface when host-consumed and receipted
Codex-Ratchet    = research discipline and sim/proof mining surface
```

## North star

```text
A future ColdStartPacket should let a model reload the project basin without
relying on chat history.
```

The model receives:

```text
ColdStartPacket
  + AttractorBasinMap
  + SpinorMemoryCells
  + FrontierLedger
  + GateLedger
  + ConstraintLedger
  + ReceiptIndex
  + GraveyardLedger
```

Then it can do one bounded move inside the right landscape.

## Why Spinor Memory and Attractor Basin Digger go together

Spinor Memory preserves **orientation under ordered operations**.

Attractor Basin Digger preserves **stability of the whole project object**.

They are coupled:

```text
SpinorMemory says: this claim has this operator history and orientation.
AttractorBasinDigger says: this proposed next move keeps or loses the basin.
```

A vector memory can retrieve nearby text. A spinor/basin memory can distinguish:

```text
same words, different status
same claim, different branch
same patch, different gate order
same receipt, different authority state
same code change, basin-deepening vs basin leakage
```

## Authority boundary

Research Ratchet does not promote claims by memory.

Promotion requires the authority spine:

```text
proposal -> owner approval -> host request -> host receipt -> effect/eval proof -> ledger/frontier update
```

Spinor Memory is a read/control model unless backed by receipt refs. Attractor Basin Digger is a classifier unless backed by evidence and policy.

## Related pages

- [[projects/research-ratchet/wiki-update-intake-2026-06-21]]
- [[projects/research-ratchet/missing-primitives-and-open-questions-2026-06-21]]
- [[concepts/world-engine-graph-patch-algebra]]
- [[concepts/spinor-memory]]
- [[concepts/attractor-basin-digger]]
- [[concepts/admissibility-geometry-and-gates]]
- [[projects/leviathan-current/research-ratchet-deep-patch-plan-2026-06-21]]
- [[projects/codex-ratchet/spinor-memory-sim-integration-2026-06-21]]
- [[projects/research-ratchet/cold-start-packet-current-2026-06-21]]
- [[projects/research-ratchet/next-10-ratchet-clicks-2026-06-21]]
