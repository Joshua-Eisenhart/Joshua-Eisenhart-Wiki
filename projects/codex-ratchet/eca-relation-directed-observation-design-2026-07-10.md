# ECA Relation-Directed Observation Design - 2026-07-10

Status: noncanonical wiki research digest of the Codex-Ratchet
`eca_relation_directed_observation_design_v1` packet. The repo receipt is the
execution authority; this page is interpretation and research routing.

## Question

Can a small globally shared observation subset make stable object relations
identifiable while preserving several compatible hidden dynamics and several
full stable partitions?

This is stricter than ordinary system identification. The desired measurement
must collapse disagreement about a queried relation without collapsing the
whole version space to one hidden system.

## Exact Process

The packet treated measurement choice as finite target-aware experimental
design, not learning:

1. freeze 128 train-only pair-orbit design fixtures;
2. screen every size-two through size-four subset of 16 trajectories, 2,500
   candidates total;
3. exact-score the top 32 per size using stable-relation truth;
4. independently reproduce the search in JAX and Julia;
5. freeze S2 `[0,1]`, S3 `[0,1,9]`, and S4 `[3,5,9,12]` before confirmation
   source files exist;
6. independently reconstruct 325 reserved validation fixtures;
7. score all three winners plus two baselines at every size;
8. open the historically consumed test block only if at least two sizes pass.

A fresh audit caught and repaired two controller overstatements before
confirmation: normalized projections had been called complete records, and the
controller had not independently derived the shortlists and winners. Corrected
commit `8615977aa` repaired both without changing the winners.

## Result

JAX and Julia agree on all 2,925 shared validation fixture/design records. The
controller independently recomputes every gate.

| Size | Global relation coverage | Worst fixture | Diverse fixtures | Systems identified | Result |
|---:|---:|---:|---:|---:|:---:|
| 2 | 73.38% | 20.98% | 279/325 | 0 | fail |
| 3 | 76.43% | 20.98% | 277/325 | 0 | fail |
| 4 | 80.73% | 20.98% | 165/325 | 38 | fail |

No size passes. S2 is exactly the hash-order baseline. Every size misses
diversity and global/per-fixture coverage floors; S4 also violates the
no-system-identification gate.

```text
candidate_exists = false
robust_design_family = false
reused_test_opened = false
```

## Research Context

### Version spaces and disagreement

The packet's compatible-rule set is a finite version space. Wiener, Hanneke,
and El-Yaniv analyze disagreement-based active learning through the size of a
smallest sample subset that induces the same version space
([JMLR 2015](https://jmlr.org/beta/papers/v16/wiener15a.html)). Hanneke's
active-learning analysis makes collapse of the disagreement region a central
complexity object
([JMLR 2012](https://www.jmlr.org/papers/v13/hanneke12a.html)).

The Ratchet target differs in an important way. It does not want maximum
version-space collapse. It wants selective collapse:

```text
relation disagreement decreases
while
model diversity and partition diversity survive
```

The failed fixed subsets show that those objectives conflict under the current
carrier and probe family. More observations monotonically constrain compatible
dynamics, but robust relation coverage is nonmonotone because the score becomes
zero when diversity disappears.

### Distinguishing sequences

Active automata learning offers a better next abstraction than a larger fixed
subset. Adaptive distinguishing sequences choose later experiments from prior
responses rather than committing to one global packet. Frohme develops this
route for active automata learning
([arXiv:1902.01139](https://arxiv.org/abs/1902.01139)). Vaandrager, Garhewal,
Rot, and Wissmann formulate active learning around constructive apartness and
show how adaptive distinguishing sequences fit naturally
([arXiv:2107.05419](https://arxiv.org/abs/2107.05419)).

For the object engine, the analogue is not "identify the rule." It is:

```text
choose the next intervention that separates relation hypotheses
without unnecessarily separating dynamics that induce the same relation
```

This suggests a policy over observation actions, with stopping when the target
relation is stable across the surviving version space.

### Model-discrimination experimental design

Classical optimal design often chooses experiments to estimate parameters or
discriminate rival models. Atkinson and Fedorov's T-optimal line explicitly
targets experiments that separate competing models
([Biometrika 1975](https://doi.org/10.2307/2335364)). Modern Bayesian
model-discrimination design frames the objective as expected information gain
over model identity
([Statistics and Computing 2022](https://link.springer.com/article/10.1007/s11222-022-10078-2)).

The Ratchet objective is again deliberately different: model discrimination is
a constraint and a negative control, not the goal. A successful object
measurement should discriminate stable relations while retaining multiple
models. That is a constrained model-discrimination problem with a quotient
target.

## What Was Learned

The machinery has teeth in a narrow scientific sense: it generated a
precommitted design, exposed two controller defects through adversarial audit,
ran independent engines, and rejected the favored design without moving the
thresholds or opening test data.

The proposed perception regime did not survive. This is not learned
perception, because stable-relation truth directly scores train candidates and
no learner infers the design policy. It is an exact oracle experimental-design
scout.

The fixed-global-subset assumption is now the main falsified object. The next
experiment should test adaptive policies, not merely search larger subsets.

## Next Ratchet

Preregister an adaptive finite policy with:

- state: current compatible ordered rule pairs and induced relation classes;
- action: one new trajectory/intervention choice;
- objective: maximum reduction in relation disagreement;
- diversity constraint: minimum effective hypotheses and partition relations;
- cost: number of interventions and observed state transitions;
- stopping rule: every queried relation stable or budget exhausted;
- baselines: system-ID information gain, hash order, random policy, and fixed
  S2/S3/S4 packets;
- confirmation: untouched rule-family blocks and policy traces;
- failure rule: no threshold repair after validation.

Only after an adaptive policy produces a broad consensus-without-identification
window should PyTorch be admitted to learn policy selection or approximate the
exact relation oracle.

## Claim Ceiling

Earned: exact cross-runtime rejection of three frozen target-aware observation
designs on a reserved finite family, with the test block correctly unopened.

Not earned: a measurement-design candidate, learned perception, spontaneous
object formation, semantic objecthood, QIT stages, four substages, the 64-stage
schedule, MMMs, ontologies, Axis0, physics, life, or consciousness.

## Routes

- [[projects/codex-ratchet/eca-observation-object-identifiability-2026-07-10]]
- [[projects/codex-ratchet/finite-behavioral-object-engine-v1-2026-07-10]]
- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
- [[concepts/mimetic-holodeck-perception-and-engine-teeth-2026-07-05]]
- [[concepts/object-formation-mesh-perception-2026-07-05]]
