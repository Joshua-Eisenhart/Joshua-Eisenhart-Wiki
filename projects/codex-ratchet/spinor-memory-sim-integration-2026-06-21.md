---
title: Codex-Ratchet Spinor Memory Sim Integration
created: 2026-06-21
updated: 2026-06-21
type: project-plan
status: proposal_design_current
claim_ceiling: sim-integration plan; no new sim admission
---

# Codex-Ratchet Spinor Memory Sim Integration

## Purpose

Codex-Ratchet sims should feed Research Ratchet memory and basin classification without weakening the existing gates.

The goal is not to make sims into memory prose. The goal is to make sims produce structured evidence about ordered operators, basin stability, quotient erasure, and branch survival.

## Existing Codex discipline to preserve

```text
No copy-sweeps.
Imports re-earn status.
One object / one claim / one card.
JAX and Julia = current primary nonclassical execution engines.
PyTorch may appear only as legacy/comparison/bounded helper unless a fresh receipt makes it load-bearing.
Receipts are the record.
Builder word is never evidence.
Fresh audit is required for load-bearing claims.
Claim ceilings never collapse.
```

## Sim modes must be explicit

Every Spinor/Basin-linked sim must state one mode:

```text
free        layer alone against exact invariants
restricted  operation confined by lower geometry
quotiented  which distinctions survive a quotient/readout
ratcheted   sequential constraints with induced geometry recomputed each step
```

Ratcheted mode is a candidate sim analogue for Research Ratchet-style basin
dynamics, pending finite carrier, operator-order, controls, and receipt-backed
validation:

```text
G_{t+1} = {x in G_t : C_{t+1}(x)}
g_{t+1} = g_t restricted to G_{t+1}
A_{t+1} = A_t restricted to G_{t+1}
F_{t+1} = dA_{t+1}
```

Every ratcheted-mode receipt must state whether it uses ordinary conditioning, induced/coarea surface measure, or a lower-dimensional/disintegrated measure.

## Candidate sim outputs for Spinor Memory

A gated sim may emit candidate fields for later SpinorMemory ingestion. The sim
does not directly update accepted memory or authority state.

```text
object_id
sim_mode
claim_ceiling
operator_trace
bracket_order
left_action_history
right_action_history
quotient_readout
surviving_distinctions
erased_distinctions
basin_boundary
escape_cases
control_flips
evidence_refs
receipt_hash
```

## Candidate sim outputs for Attractor Basin Digger

A gated sim may emit candidate fields for later BasinDigger classification. The
classifier remains a control/readout surface unless backed by evidence and
policy.

```text
basin_id
candidate_patch_id
basin_center_ref
invariant_results
leakage_edges
escape_cases
split_tests
kill_tests
next_deepening_moves
insufficient_evidence_fields
```

## Examples

```text
A->B vs B->A discriminator
  tests whether operator order is load-bearing

S^3 spinor carrier vs S^2/B^3 quotient
  reports what density/Bloch quotient erases

associator witness before/after quotient
  tests whether nonassoc signal survives readout

constraint sequence C_i(C_j(G)) vs C_j(C_i(G))
  tests geometry-level noncommutation

basin escape under update rule
  maps leakage edge for BasinDigger
```

## Integration with Leviathan

Codex sim outputs become candidate GraphPatch evidence, not direct admission.

```text
Codex sim receipt
  -> SpinorMemory candidate cell
  -> BasinDigger classification
  -> Lev EvalSuite measurement
  -> ClaimGate authority transition only if promotion requested and approved
```

## Sim acceptance gates

```text
one bounded object / claim / card
mode declared
finite carrier or bounded state space named
update/operator rule explicit
operator and bracket order preserved
controls and escape cases named
quotient erasure named where relevant
JAX and Julia roles explicit when claim-bearing
PyTorch fenced as legacy/comparison/bounded helper unless a real ablation makes it load-bearing
proof tier and receipt refs named
receipt hash stable
claim ceiling honest
fresh audit attached
```

## Claim ceiling

This page is an integration plan. It does not admit a sim result, promote a carrier, close M(C), or prove physics/world-engine claims.
