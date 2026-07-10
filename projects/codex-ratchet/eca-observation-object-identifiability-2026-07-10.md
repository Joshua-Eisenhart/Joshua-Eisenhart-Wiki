# ECA Observation Object Identifiability - 2026-07-10

Status: noncanonical wiki research digest of Codex-Ratchet commit `0f8b65bfc`.
The repo packet is the execution authority; this page is interpretation and
research routing.

## Question

Can bounded raw trajectories determine a stable object relation without first
determining the complete hidden dynamics?

This is the missing information gate between an exact finite object factory and
a learned perception claim. A learner should not be trained when the target is
underdetermined, and it should not be called perceptual when success can come
from identifying the hidden rules and replaying the exact algorithm.

For observation packet `D`, the exact version space is

```text
V(D) = every ordered distinct rule pair consistent with every observed
       action-labelled transition
```

For query states `x,y`, every hypothesis in `V(D)` induces a stable behavioral
relation. The target is three-valued:

```text
must_equal     every compatible dynamics says same object
must_separate  every compatible dynamics says different objects
ambiguous      compatible dynamics disagree
```

Ambiguity is not a negative label.

## Frozen Finite Census

- periodic nine-bit elementary cellular automata;
- 531 symmetry-representative test rule pairs;
- 5 cumulative trajectory budgets: `1,2,4,8,16`;
- 9,636 same-initial-probe state queries per fixture;
- 65,280 ordered distinct rule-pair hypotheses;
- independent Julia and JAX exact implementations;
- 2,655 cross-runtime fixture-budget records;
- all 20 frozen fields equal in every record.

The common ledger SHA256 is
`4ca51e158058737a30fd994943deb8cfff0bcd1b1b9c141639f34b985255b5cc`.

## Result

| Budget | Global identifiable | Worst fixture | Rules identified | Consensus without ID | Reading |
|---:|---:|---:|---:|---:|---|
| 1 | 69.47% | 20.98% | 0/531 | 3,554,550 | too much missing information |
| 2 | 77.68% | 20.98% | 0/531 | 3,974,454 | too much missing information |
| 4 | 99.55% | 69.74% | 461/531 | 0 | nearly system identification |
| 8 | 100% | 100% | 531/531 | 0 | complete system identification |
| 16 | 100% | 100% | 531/531 | 0 | complete system identification |

Budgets 1 and 2 contain millions of balanced consensus labels across many
compatible dynamics, but fail the preregistered 95% global and 80% per-fixture
coverage floors. Budget 4 has excellent aggregate coverage but one family
remains below the floor while 86.82% of hidden systems are already uniquely
identified. Budgets 8 and 16 identify all hidden systems.

```text
perception_like_regime_admitted = false
earliest_admitted_budget = null
```

The current observation design crosses from underdetermination to system
identification without exposing two consecutive broad, reliable
consensus-without-identification budgets.

## Research Context

The version-space construction is a finite exact form of set-theoretic system
identification: observations constrain a feasible model set instead of forcing
a point estimate. Pearson describes set-theoretic parameter estimation as
retaining every model compatible with bounded-error constraints, with an exact
feasible set as the primary object
([SIAM J. Matrix Analysis and Applications](https://doi.org/10.1137/0609042)).
The ECA packet is discrete and noiseless, but the epistemic distinction is the
same: singleton feasible set means system identification; a larger feasible
set preserves structural uncertainty.

The object relation itself is behavioral equivalence for a finite observed
transition system. Wissmann, Dorsch, Milius, and Schroder develop generic
coalgebraic partition refinement for quotienting finite systems by behavioral
equivalence
([Logical Methods in Computer Science](https://doi.org/10.23638/LMCS-16(1:8)2020)).
The Ratchet packet uses the exact finite relation, not a learned embedding or a
semantic label.

The useful new conjunction is:

```text
set-valued identification uncertainty
plus
behavioral-equivalence consensus across every surviving model
```

That conjunction separates three failures that ordinary classification scores
blur together:

1. the observations do not determine the queried relation;
2. the relation is determined only because the whole dynamics is identified;
3. the relation is invariant across multiple genuinely different dynamics.

Only the third is a candidate foundation for object perception.

## What This Teaches The Engine Program

The finite object factory is real: exact stable behavioral objects can be
constructed and compared across independent runtimes.

The current perception benchmark is not yet real enough to train. PyTorch is
correctly absent. Adding a learner now would measure either forced guessing or
system identification, not the claimed object intelligence.

The next observation-design search should optimize a constrained window:

```text
maximize relation identifiability
subject to version-space diversity remaining high
and full-partition diversity remaining nontrivial
```

Candidate interventions include shorter mixed trajectories, deliberately
non-identifying probes, adaptive queries chosen for relation consensus rather
than rule discrimination, and cross-view packets that preserve multiple model
realizations. Any selected design needs a new preregistration and untouched
families before neural learning.

## Claim Ceiling

Earned: an exact cross-runtime finite census showing that this frozen
observation design has no stable consensus-without-identification window.

Not earned: learned perception, unique engine intelligence, four substages,
the 16-by-4-by-2 schedule, QIT promotion, MMMs, ontologies, Axis0, physics,
life, or consciousness.

## Routes

- [[projects/codex-ratchet/eca-n9-behavioral-depth-and-v2-admission-2026-07-10]]
- [[projects/codex-ratchet/finite-behavioral-object-engine-v1-2026-07-10]]
- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
- [[concepts/mimetic-holodeck-perception-and-engine-teeth-2026-07-05]]
- [[concepts/object-formation-mesh-perception-2026-07-05]]
