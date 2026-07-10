# ECA N9 Behavioral Depth And V2 Admission - 2026-07-10

Status: noncanonical wiki digest of a preregistered, validated
Codex-Ratchet scratch-diagnostic packet.

## Result

Julia and JAX independently evaluated all 32,640 unordered distinct pairs of
elementary cellular-automaton rules on every periodic nine-bit state.

The independent controller compared twelve fields in every record with zero
disagreements.

```text
accepted exact label:
EXACT_CROSS_RUNTIME_FINITE_ECA_REFINEMENT_DEPTH_CENSUS_N9
```

This is a `passes local rerun` scratch result, not canonical admission.

## Exact Depth Distribution

| Strict depth | Pair count |
|---:|---:|
| 0 | 120 |
| 1 | 1,886 |
| 2 | 7,570 |
| 3 | 15,592 |
| 4 | 5,448 |
| 5 | 1,530 |
| 6 | 318 |
| 7 | 136 |
| 8 | 0 |
| 9 | 24 |
| 10 | 16 |

Maximum strict depth across ring sizes 6 through 9 is therefore:

```text
N6: 3
N7: 4
N8: 6
N9: 10
```

This is an observed finite sequence. It is not evidence for a recurrence or
asymptotic growth law.

The 16 depth-ten pairs occupy four simultaneous reflection/conjugacy pair
orbits with canonical keys `2,60`, `2,102`, `8,153`, and `8,195`.

## What The Object Is Mathematically

For a finite state set `X`, observation set `O`, and action alphabet
`A={a,b}`, the fixture can be written as a deterministic coalgebra:

```text
c : X -> O x X^A
```

Here `O` is the fixed Hamming-weight/domain-wall probe and `X^A` contains the
two action successors.

The stable partition is behavioral equivalence for this finite observed
transition system. Partition refinement repeatedly separates states whose
observations or successor classes differ.

This connection is standard computer science, not a Ratchet invention.
[Wissmann, Dorsch, Milius, and Schroder](https://doi.org/10.23638/LMCS-16(1:8)2020)
give generic coalgebraic partition refinement algorithms that quotient finite
systems by behavioral equivalence. Their framework covers deterministic
automata and several weighted or probabilistic system types.

The classical algorithmic ancestry includes
[Paige and Tarjan's partition-refinement work](https://doi.org/10.1137/0216062).
The later
[coalgebra-encoding paper](https://arxiv.org/abs/2102.12842)
extends generic refinement into complete minimization, including reachable-part
and quotient-transition construction.

Project translation:

- the exact stable classes are finite behavioral objects;
- strict depth counts how many finite observation-history approximants are
  needed before this fixture stabilizes;
- the quotient is relative to the selected probe, action family, carrier, and
  boundary;
- changing any of those creates a different object problem.

## Important Implementation Kill

An intermediate JAX implementation sorted each state's two action-successor
labels before packing the refinement signature.

That would have erased which successor came from action `A` versus `B` and
merged states with locally exchanged futures.

The implementation was interrupted before the accepted run. The final source
uses ordered `(current,A-successor,B-successor)` signatures. Global action-swap
invariance is checked at the partition level, allowing harmless class-ID
renaming.

This is a concrete example of why a plausible symmetry can still change the
primary object.

## Learned-V2 Admission

Before N9 labels existed, 8,808 simultaneous rule-pair symmetry orbits were
split into two hidden batches of 4,404 orbits each.

The N9 result contains:

- 176 depth-at-least-seven fixtures;
- 44 qualifying symmetry orbits;
- 26 qualifying orbits in batch A;
- 18 qualifying orbits in batch B.

Among state pairs still equivalent after six refinements, later rounds change
at least `2.6937%` per qualifying fixture and `5.3499%` in aggregate.

Across the whole carrier, only `0.1166%` of ordered-pair targets change after
depth six.

## Admission Defect

The frozen admission specification did not explicitly state whether the
depth-six baseline MCC is computed over the full fixture or only the decisive
depth-six-equivalent subset.

On the full fixture, depth-six macro MCC is `0.9709778575`, failing the required
maximum `0.35`. A learner can therefore score extremely well without learning
late refinement.

On the decisive subset, the depth-six baseline predicts one class everywhere.
Its conventional MCC is `0`, passing the numeric threshold vacuously while
performing no discrimination.

The controller reports both readings and fails closed on the metric-scope
ambiguity.

```text
learned V2 admission:
INSUFFICIENT_DEPTH_NOVEL_MASS_FOR_LEARNED_V2
```

No PyTorch learner was trained. The threshold was not weakened.

## Leviathan

Lev's `createExec` runtime executed the accepted JAX source through a frozen
local-process allowlist and emitted matched start/completion events.

The scientific pair-ledger hash matched the direct run.

The installed Lev checkout was dirty and older than `lev-main`. This proves a
bounded executor path, not clean-current Lev readiness and not scientific
authority.

## Perception Consequence

The exact object factory is real on this finite carrier.

The current learned-perception benchmark is not real enough to run.

The next useful question is information-theoretic identifiability from partial
observations: which object relations are determined by a bounded observation
packet even when several hidden dynamics remain possible?

That scout must precede neural training. Otherwise model failure could merely
reflect missing information, while model success could merely identify the ECA
rules and replay the exact algorithm.

That scout is now complete. The frozen observation schedule moves from
underdetermined relations at budgets 1 and 2 to near-complete or complete rule
identification at budgets 4, 8, and 16. It exposes no admitted
consensus-without-identification window. See
[[projects/codex-ratchet/eca-observation-object-identifiability-2026-07-10]].

## Ceiling

Earned: exact finite N9 behavioral-equivalence depth census and a fail-closed
rejection of the current learned-V2 admission protocol.

Not earned: learned perception, unique engine intelligence, four substages, the
16-by-4-by-2 schedule, entropy-gradient dynamics, QIT promotion, MMMs,
ontologies, a universal attractor, Axis0, physics, life, or consciousness.

## Routes

- [[projects/codex-ratchet/eca-behavioral-refinement-depth-census-2026-07-10]]
- [[projects/codex-ratchet/finite-behavioral-object-engine-v1-2026-07-10]]
- [[projects/codex-ratchet/eca-observation-object-identifiability-2026-07-10]]
- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
- [[concepts/cross-view-attractor-nominalism-ledger-2026-07-10]]
