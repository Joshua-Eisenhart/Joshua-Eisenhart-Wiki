---
title: Codex sims as basin dynamics and operator validation
created: 2026-06-21
updated: 2026-06-21
type: sim-plan
status: current-research-overlay
claim_ceiling: sim planning/router; no sim result promotion
tags: [codex-ratchet, sims, attractor-basin, spinor-network, operator-validation, tri-engine]
---

# Codex sims as basin dynamics and operator validation

## Core idea

Codex-Ratchet sims should feed the Research Ratchet by testing **basin dynamics under operators**, not by producing broad narrative confidence.

A sim is a bounded probe over one object, one claim, one gate, and one claim ceiling.

## Existing Codex discipline to preserve

Keep the v6 constraints:

- old sims/wiki = mine/fuel, not status;
- no copy-sweeps;
- imports re-earn status;
- one sim folder per object;
- receipts are the record;
- Julia/JAX/PyTorch by role, not TMR-as-evidence;
- Julia arbitrates structure;
- JAX sweeps;
- PyTorch graph/network/autograd;
- validator and fresh audit are required before any load-bearing claim.

## Sim modes for basin work

Every sim should declare one of four modes:

| Mode | Question |
| --- | --- |
| Free | Does this layer satisfy exact invariants alone? |
| Restricted/stacked | Does it preserve, move within, move between, or leave lower geometry? |
| Quotiented | Which distinctions survive the quotient/readout? |
| Ratcheted | What geometry remains after sequential constraints, and how does it change? |

Ratcheted mode is most relevant to Attractor Basin Digger:

```text
G_(t+1) = { x in G_t : C_(t+1)(x) }
```

but the receipt must also recompute induced geometry, measures, invariants, basins, and leakage.

## Basin receipt shape

A basin-dynamics sim should emit a receipt like:

```json
{
  "kind": "BasinDynamicsSimReceipt",
  "object_id": "stage-5-attractor-basin",
  "sim_mode": "ratcheted",
  "carrier_ref": "...",
  "operator_sequence": ["C_i", "C_j"],
  "order_control": ["C_j", "C_i"],
  "survivor_set_hash": "sha256:...",
  "induced_geometry_hash": "sha256:...",
  "basin_map_hash": "sha256:...",
  "leakage_edges": [],
  "graveyard_controls": [],
  "julia_canon_ref": "...",
  "jax_consumer_ref": "...",
  "pytorch_graph_ref": "...",
  "proof_refs": [],
  "claim_ceiling": "scratch_diagnostic",
  "promotion_allowed": false
}
```

## Sim-to-Leviathan bridge

Codex sims should not directly mutate Lev world state. They should produce graph-patch inputs:

```text
Codex sim receipt
  -> ClaimGate/Research Ratchet proposal
  -> Lev admission gate
  -> Effect/Eval proof wrapper
  -> accepted graph patch if gates pass
```

## What sims should test for Spinor Memory

1. Same claim text with different gate history yields different cell state.
2. `host_consume` before `owner_approve` fails.
3. `promote_frontier` before Effect/Eval/Receipt fails.
4. A vector-near retrieved artifact with wrong lifecycle state is downgraded.
5. Basin Digger labels proposed moves as deepening/leak/split/kill/insufficient.
6. Quotient tests report what phase/chirality/lift/bracketing distinctions are erased.
7. Ratcheted mode detects noncommuting constraint order: `C_i(C_j(G))` not congruent to `C_j(C_i(G))`.

## What not to simulate yet

Do not attempt a giant full-stack world-engine sim yet. The correct next pieces are bounded: one `SpinorMemoryCell` operator-order test; one `AttractorBasinDigger` classification test; one `GraphPatchProposal` legality test; one Codex sim envelope for ratcheted-mode basin dynamics; one Lev Effect/Eval wrapper proof path.
