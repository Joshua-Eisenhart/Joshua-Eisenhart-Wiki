---
title: Spinor Memory
created: 2026-06-21
updated: 2026-06-21
type: concept
status: current-research-overlay
claim_ceiling: concept/design term; JSON-first v0 only; no quantum-memory or proof-authority claim
tags: [spinor-memory, project-memory, research-ratchet, noncommutative-memory]
---

# Spinor Memory

## Definition

**Spinor Memory** is a project-state memory representation that stores a claim/object as an oriented state under ordered admissibility transformations.

It is not a vector database replacement. It is not a proof engine. It is a state/read model for long-horizon research continuity.

## Contrast

```text
vector memory:
  retrieve semantically similar chunks

tensor/role memory:
  preserve role-filler structure

spinor memory:
  preserve orientation, chirality, phase/status, left/right action,
  operator order, gate history, and receipt lineage
```

## Minimal v0 meaning

In v0, `spinor` means:

```text
same projected content can be different as oriented state
```

Example:

```text
same claim text
+ owner_approved but not host_receipted
!=
same claim text
+ host_receipted and trust-root verified
```

## Required fields

- `object_id`
- `basin_id`
- `claim_text`
- `claim_ceiling`
- `orientation`
- `state_vector`
- `operator_trace`
- `allowed_next_ops`
- `blocked_ops`
- `graveyard_hits`
- `source_refs`
- `receipt_refs`

## Authority boundary

A Spinor Memory cell may orient and filter. It cannot promote. Authority comes from Effect/Eval/ClaimGate receipt chains.

See also:

- [[concepts/attractor-basin-digger]]
- [[projects/research-ratchet/spinor-memory-and-attractor-basin-digger-2026-06-21]]
- [[projects/research-ratchet/claimgate-authority-state-machine-2026-06-21]]
