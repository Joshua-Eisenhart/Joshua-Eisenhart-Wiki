---
title: Basin-Manifold Claim Contract
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [concept, simulation, constraints, geometry, topology, proof]
sources:
  - /Users/joshuaeisenhart/wiki/hermes-current/math-geometry-learning-wiki-plan-2026-05-19.md
  - /Users/joshuaeisenhart/wiki/concepts/f01-n01-root-constraint-basin-pressure.md
framing: current
---

# Basin-Manifold Claim Contract

## What this page is

This page is the checklist for saying that something is a basin, manifold layer, geometric attractor, or central ratchet surface in the system.

It exists because a basin claim can be faked by attractive language:

- repeated motifs
- clustering
- visual similarity
- model agreement
- many screenshots pointing in the same direction
- a nice manifold metaphor
- a tool returning a plausible result

None of those is enough.

A basin/manifold claim has to survive a formal contract under [[f01-n01-root-constraint-basin-pressure]].

## Minimal claim shape

A real basin/manifold claim needs all of these:

1. admissibility predicate
2. state space
3. update rule
4. basin boundary
5. stability invariant
6. escape or failure cases
7. root tests for F01 and N01
8. at least one killed non-manifold explanation
9. canonical receipt if used for repo promotion

If any of these is missing, the honest status is candidate, metaphor, source-derived, or diagnostic-only.

## 1. Admissibility predicate

The page or sim must say what it means for a state, witness, carrier, or layer to be admitted.

Bad form:

> These states cluster into a basin.

Better form:

> A state is admitted if it satisfies finite carrier constraint C, noncommuting update witness W, and stability test S under update rule U for bounded horizon H.

The predicate should be explicit enough that a tool, sim, or reader can apply it.

## 2. State space

The state space must be named.

Examples:

- finite graph states
- finite cell-complex states
- density matrices on bounded Hilbert space
- tensor-network states with specified site count and bond rank
- finite registry states
- terrain-token states
- bundle/frame states under a specified structure group

If the state space is vague, the basin boundary will also be vague.

## 3. Update rule

A basin needs dynamics. The update rule says how states move.

Examples:

- Hamiltonian update
- Lindblad/open-system update
- graph rewrite
- cellular transition rule
- ring-checkerboard update
- tensor-network evolution
- constraint-admission iteration
- probe/receipt append rule

For N01, update order matters. The page should say what happens under reverse, shuffled, or commuted update order.

## 4. Basin boundary

A basin boundary separates admitted/stable states from escape/failure states.

A useful boundary can be:

- invariant threshold
- topological obstruction
- failed commutator witness
- broken gauge-invariant observable
- lost finite carrier
- entropy/information threshold
- collapse under ablation
- failure of recurrence/stability under bounded updates

No boundary means no basin claim.

## 5. Stability invariant

The basin must preserve something under the allowed updates.

Possible invariants:

- finite registry class
- homology/persistent-homology feature
- gauge-invariant observable
- commutator sign/pattern
- chirality orientation
- entropy range or monotone
- tensor rank/bond constraint
- loop/holonomy signature
- admissibility status under repeated probes

A stable-looking plot is not enough. Name the invariant.

## 6. Escape and failure cases

The page must say how the basin fails.

Useful failure cases:

- root-off
- F01-only
- N01-only
- pressure-off
- reverse/order-shuffle
- symmetric-flux
- ring-checkerboard ablation
- cellular-vs-continuous replacement
- quaternion-vs-complex replacement
- gauge-broken/transplanted
- Hopf/S3 removed
- cross-shell transplant
- null/tool-stub
- classical baseline
- apparent-basin-without-manifold

Failure cases are not embarrassment. They are how the basin boundary becomes real.

## 7. Killed non-manifold explanation

At least one non-manifold explanation must be killed before a manifold/basin explanation advances.

Examples:

- “It is just clustering.”
- “It is just a gauge artifact.”
- “It is just finite graph bookkeeping.”
- “It is just a continuous model projected onto finite samples.”
- “It is just a classical baseline.”
- “It is just model agreement.”
- “It is just a symbolic terrain table.”

A strong page says which simpler explanation failed and how.

## 8. Gauge discipline

Gauge representatives are not gauge-invariant observables.

A basin/manifold page should separate:

- representative choices
- coordinate choices
- gauge choices
- observables that survive gauge change
- invariants that remain after transplant/broken-gauge controls

If the claim only holds in one representation, it is not yet a geometry claim.

## 9. Tool receipts

Tools are useful only where load-bearing.

Examples:

- z3/cvc5: root checks, finite witness existence, UNSAT/constraint checks
- SymPy/Clifford: algebraic witnesses, commutators, spin/Clifford identities
- rustworkx/XGI/TopoNetX/GUDHI: graph/cell/topology witnesses
- PyTorch/PyG/e3nn: tensor/equivariant behavior
- auto_LiRPA/le-wm: robustness/world-model bounds

A tool mention is not evidence. A canonical receipt must say what the tool checked and why the check was load-bearing.

## Status ladder

Use this ladder for wiki pages:

| Status | Meaning |
|---|---|
| educational | teaches the math/concept without claiming system admission |
| source-derived | extracted from docs/screenshots/threads, not independently verified |
| candidate | plausible system fit, needs tests |
| diagnostic-only | ran or was observed but lacks full contract |
| keep but open | useful and real, but missing a required contract piece |
| killed | failed a decisive test |
| admitted | survived the relevant root tests, negatives, and receipts |

Default for new math/geometry pages should be educational or candidate, not admitted.

## Short test

Before making a strong claim, ask:

1. What is finite here?
2. What is noncommuting here?
3. What updates the state?
4. What defines the basin boundary?
5. What invariant survives?
6. What failure case escapes?
7. What simpler non-manifold explanation was killed?
8. What receipt proves the load-bearing claim?

If the page cannot answer those, it can still teach the concept, but it should not promote the basin/manifold claim.

## Status fence

Current status: claim-contract / wiki discipline page.

This page is a gate for stronger claims. It is not itself evidence that the manifold/basin claim is true.
