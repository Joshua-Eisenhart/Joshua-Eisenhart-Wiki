---
title: Attractor Basin Digger
created: 2026-06-21
updated: 2026-06-21
type: concept
status: proposal_design_current
claim_ceiling: basin classifier/control layer; not proof authority
---

# Attractor Basin Digger

## Definition

Attractor Basin Digger maps the stable project landscape around a bounded object.

It asks:

```text
What basin are we inside?
What is the basin center?
What invariants hold it together?
What leakage paths cause drift?
What graveyard collisions should stop repetition?
What move deepens the basin?
What move splits or kills the basin?
```

## Why it belongs with Spinor Memory

Spinor Memory preserves the state of a claim under ordered operators.

Attractor Basin Digger decides whether a proposed next operator preserves the active research basin.

Together:

```text
SpinorMemory = local orientation of claim/patch trajectory
BasinDigger  = global stability of the project object
```

## Output labels

```text
basin_deepening        improves admission power, proof spine, frontier clarity, or stability
basin_leakage          adds churn, UI, docs, model/swarm expansion, or overclaim without admission power
basin_split            shows two objects are being conflated and need separate branches
basin_kill             violates root constraints or falsifies the basin
insufficient_evidence  missing source/receipt/eval/proof prevents classification
```

## Basin map object

```text
AttractorBasinMap
  basin_id
  object_id
  basin_center
  basin_invariants
  basin_boundary
  live_frontier
  leakage_edges
  graveyard_collisions
  basin_deepening_moves
  basin_split_tests
  exit_criteria
  next_recommended_move
  claim_ceiling
  receipt_refs
```

## Current Research Ratchet basin

```text
Basin center:
  Lev-native Research Ratchet project harness

Invariants:
  proposal != promotion
  approval != admission
  observed effect precedes proof
  eval emits measurements
  receipt updates frontier
  trust-root verified enforcement for enforcing gates
  vector memory is recall, not project understanding
  spinor memory is orientation, not proof

Leakage:
  MassRun expansion without admission power
  UI/marketing/demo churn
  fixture authority overclaim
  docs-green as proof
  dashboard green as closure
  vector-only memory called long-horizon understanding
  full spinor/quantum claim before JSON-first v0 earns value
```

## Control-theoretic reading

A basin is a region of state space where repeated legal ticks pull work back toward the same object.

A move is basin-deepening if it lowers future drift risk or increases verified state.

A move is leakage if it increases local activity while weakening object retention.

## Codex-Ratchet sim connection

Codex sims should feed BasinDigger with measurable stability facts:

```text
survivor set G_{t+1}
induced geometry g_{t+1}
connection/curvature restriction
basin escape cases
order-sensitivity C_i(C_j(G)) != C_j(C_i(G))
quotient erasure / survival of spinor phase
state-space boundary and leakage edges
```

Every sim mode must declare whether it is free, restricted, quotiented, or ratcheted. Ratcheted mode is the most direct mathematical analogue of Attractor Basin Digger because it applies sequential constraints and recomputes induced geometry at each step.
