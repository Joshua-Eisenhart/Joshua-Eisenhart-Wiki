# ECA Behavioral Refinement Depth Census - 2026-07-10

Status: noncanonical wiki digest of a validated Codex-Ratchet
scratch-diagnostic census.

## Question

Does probe-relative behavioral identity on the finite ECA carrier always settle
after one refinement, or do genuinely multiround object partitions occur?

This question was forced by the V1 learned-object audit. V1's fixtures needed
only one strict refinement, while the PyG architecture received exact
paired-successor edges and six refinement-shaped message-passing rounds. Its
perfect ensemble score therefore did not establish learned perception.

## Exact Object

The carrier is a periodic binary ring of size 6, 7, or 8.

The action family is an unordered pair of distinct elementary
cellular-automaton rules.

The initial probe is:

```text
(Hamming weight, periodic domain-wall count)
```

The partition update is:

```text
P_(d+1)(x) = canon(P_d(x), P_d(T_a(x)), P_d(T_b(x))).
```

`strict_refinement_depth` counts only rounds where the partition changes.

`first_equality_round` is one greater and records the first unchanged update.

This distinction repairs the ambiguous depth language that made V1 look deeper
than it was.

## What Ran

Julia independently enumerated all full-state transition maps and partitions.

JAX x64 independently ran the same census in compiled exhaustive batches.

Each engine covered all 32,640 unordered distinct ECA rule pairs on each ring.

The controller compared 97,920 pair records field by field.

PyTorch was correctly absent because this census contains no learning task.

Neither exact engine read the other's result.

## Result

| Ring | States | Maximum strict depth | Deepest-pair count |
|---:|---:|---:|---:|
| 6 | 64 | 3 | 104 |
| 7 | 128 | 4 | 40 |
| 8 | 256 | 6 | 4 |

The complete size-8 depth-six set is:

```text
(19,35)
(19,49)
(55,59)
(55,115)
```

The two engines agree on every rule identity, strict depth, first equality
round, class-count trajectory, surviving ordered-pair trajectory, stable class
count, compact partition hash, and exact transition-pair hash.

## Why The Full Ledger Matters

The first cross-runtime comparison was red despite identical aggregate depth
histograms.

JAX included the duplicate equality observation while Julia kept only strict
changes.

The engines also used different label and transition-pair hash encodings.

Those contracts were repaired and both engines rerun.

The final controller reports zero disagreements across every field of every
fixture and detects four injected receipt corruptions.

This repeats the V1 lesson: matching summary outputs can conceal a different
operation or encoding underneath.

## Interpretation

The bounded carrier has a real tail of multiround probe-relative identity
formation.

The tail deepens as the finite carrier grows from 64 to 256 states under the
same probe and action definition.

This supports a stronger learned benchmark than V1's depth-one fixtures.

It does not show that a neural system can infer the equivalence relation.

It does not show that refinement depth is a QIT stage count.

It does not derive four substages from the dual ratchet.

It does not establish a universal attractor basin.

## Benchmark Consequence

The census exposed all deepest witnesses before V2 preregistration.

Those fixtures therefore cannot be described as hidden or untouched tests.

The four depth-six witnesses also provide too little independent test-family
mass for the planned learned-perception claim.

A valid V2 must freeze its object, split, learner boundary, architecture,
threshold protocol, seeds, and controls before training.

It should consume bounded observations or sampled trajectories rather than
stable labels, partition histories, paired-successor graphs, depths, or hashes.

Every seed must beat optimizer-erased, shuffled-label, random-core, and shallow
exact baselines without ensemble rescue.

The decisive subset must contain state pairs that are still equivalent at the
largest training depth but split later.

The preregistered N9 extension and its failed learned-benchmark admission are
now recorded at
[[projects/codex-ratchet/eca-n9-behavioral-depth-and-v2-admission-2026-07-10]].
N9 reaches strict depth ten, but the full-fixture depth-six baseline remains too
strong and the frozen MCC scope is ambiguous, so no learner was run.

## Current Claim Ceiling

Earned:

```text
EXACT_CROSS_RUNTIME_FINITE_ECA_REFINEMENT_DEPTH_CENSUS_N6_TO_N8
```

Not earned: learned perception, causal learning, unique runtime intelligence,
four substages, the 16-by-4-by-2 engine schedule, QIT promotion, MMMs, ontology
admission, Axis0, physics, life, or consciousness.

## Routes

- [[projects/codex-ratchet/finite-behavioral-object-engine-v1-2026-07-10]]
- [[projects/codex-ratchet/eca-n9-behavioral-depth-and-v2-admission-2026-07-10]]
- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[concepts/cross-view-attractor-nominalism-ledger-2026-07-10]]
