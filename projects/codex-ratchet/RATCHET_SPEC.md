# THE RATCHET — ORDER-OPEN WORKING PROCESS SPECIFICATION v0.5

_Current process authority, 2026-07-10. This specification supersedes v0.4. The v0.4 root-history loop remains a
limited predecessor, but its fixed authored gate order, inflated carrier count, prewritten “next” queue, and L5
answer-key re-audit do not survive the new audit boundary._

## 0. Compact law

> **Root only in constrained distinguishability. Propose structures, gates, subgates, orders, gradients, weakness
> relations, and controls freely. Execute finite populations. Admit only a packet-relative MSS antichain supported by
> a witnessed entropy–geometry coface gradient. Preserve every alternative and death. Nothing about list order is
> canon.**

```text
ROOT = CONSTRAINED_DISTINGUISHABILITY
EXPLORATION TEMPERATURE = HIGH
ADMISSION TEMPERATURE   = LOW
```

Repositories, wiki pages, owner messages, equations, established mathematics, simulations, and model outputs are
proposal and evidence reservoirs. Presence, age, repetition, salience, and a filename containing `canon` do not admit
anything.

## 1. What is and is not installed

At the root, an observation may constrain whether two finite presentations can remain distinguishable. Object,
identity, equivalence, support, quotient, number, probability, entropy formula, geometry, carrier, cellular automaton,
Hilbert space, manifold, gate, rung, and ladder are possible earned presentations. None is silently primitive.

The active owner pressures remain hypotheses under test:

- **F01 — finitude:** every execution has finite evidence, proposal population, histories, controls, and budget. This
  does not prove a fundamental cell size or prevent later refinement.
- **N01 — noncommutation:** order can be load-bearing, so order-sensitive candidates and schedule hypotheses must be
  tested. N01 does not install a matrix algebra or make every pair noncommute.
- **MSS — weakest current survivor:** minimality is always indexed by a finite candidate grammar, evidence surface,
  weakness relation, and budget. A newly generated weaker survivor reopens the tooth.
- **T01 — grouping pressure:** nonassociative candidates enter when grouping distinctions are live; their destination
  is not preselected.

Even this list is an active pressure set, not a completed axiomatization.

## 2. The state that ratchets

```text
variation_pool        structures, compilers, probes, gradients, controls, negatives
demand_pool           finite distinction edges with provenance
schedule_population   proposed gate boundaries, decompositions, and orders
tested_frontiers      packet-relative MSS antichains indexed by active demands
evidence_ledger       append-only executions, kills, residuals, projections, and audits
dig_pool              unordered authored seeds plus separately derived questions
```

There is no authoritative `next_dig_queue`. A serialized order is only a deterministic file encoding or an operational
scheduling choice. It has no epistemic priority.

An admitted packet-relative presentation can later be weakened, split, internally rebuilt, demoted, or killed without
deleting its historical receipt.

## 3. Entropy and geometry are one finite coface

Let `X` be a finite observation surface, `D` a finite set of demanded distinction edges, and
`pi: X -> Q_pi` a proposed presentation/quotient. Define

\[
C_D(\pi)=\{(x,y)\in D:\pi(x)=\pi(y)\},
\qquad
L_D(\pi)=|C_D(\pi)|.
\]

`C_D(pi)` is one object with two readings:

- geometrically, demanded edges have been collapsed inside quotient blocks;
- informationally/entropically, demanded distinctions remain unresolved.

Entropy is therefore not a scalar payload running on a prior geometry in this process. The quotient surface and its
unresolved distinction mass are the same finite coface. More refined entropy or geometric constructions may later be
earned from it; Shannon, von Neumann, BKM, Fisher, or another formula is not installed here.

For a proposed move `pi -> rho`, the shipped scalar contrast is

\[
g_D(\pi\to\rho)=L_D(\pi)-L_D(\rho).
\]

The vector of family-wise losses is retained as an order-valued rival. A tooth needs a positive live contrast and a
control on which the contrast vanishes. Failure of current gradient proposals means `DIG_CONTINUES`, not that the
basin is globally flat.

## 4. Gates, subgates, and their order are hypotheses

A **demand family** is a proposed grouping of finite distinction edges. A **gate-boundary hypothesis** is a block of
one or more demand families. A **schedule hypothesis** is an ordered set-partition of all currently selected families.

For demand families `{a,b,c,d}`, the process must be able to test:

- one fused gate `{a,b,c,d}`;
- every two-block and three-block decomposition in every order;
- every fully split permutation;
- later, newly proposed subfamilies, fusions, dependencies, and boundary revisions.

There are 75 ordered set-partitions of four named families. The shipped run executes all 75. It does not use the order
in which the families appear in JSON as a ladder.

Only a witnessed dependency may prune schedules. An operational priority, compute cost, or researcher preference does
not constitute such a dependency. If schedules converge, that is basin evidence for the endpoint within the packet;
it does not canonize one path. If they diverge, the branches remain live and the divergence is itself N01 evidence.

The implementation has ordinary computational dependencies—evidence must exist before it can be evaluated—but their
software execution order is not an ontological layer order.

## 5. Mass exploration without count inflation

Each finite gate may receive very large proposal populations. A population may be streamed in chunks, but chunking is
operational only. Every run records:

- proposals generated, executed, unexecuted, and the continuation cursor;
- batch boundaries and digests;
- actual behavioural equivalence classes;
- parameter aliases that produced the same behaviour;
- parked and unimplemented compilers;
- the finite grammar and the fact that the global space remains open.

Two names or parameter rows that induce the same finite partition are not independent structures. A proposed graph,
CA, QCA, transducer, density operator, or nonassociative carrier counts as an independent executed candidate only when
its compiler produces independently testable behaviour. Otherwise it is an alias, encoding witness, or parked
proposal.

Changing batch size must not change the population digest or final behavioural frontier.

## 6. Packet-relative MSS

The v0.5 engine installs one explicit finite weakness hypothesis: partition refinement. For presentations `pi` and
`rho`,

\[
\pi\preceq\rho
\quad\text{when every block of }\rho\text{ lies inside a block of }\pi.
\]

Thus `pi` is no more discriminating than `rho`. For active demand set `D`,

\[
Surv(D)=\{\pi:L_D(\pi)=0\},
\qquad
M(D)=\min_{\preceq} Surv(D).
\]

`M(D)` may contain incomparable members. The engine never chooses one by taste. Partition refinement is preferable to
v0.4's assumption-count ordering for this finite surface because it is computed directly from which observations each
candidate merges. It is still a proposed weakness relation; rival categorical, computational, resource, predictive,
or dynamical preorders remain live digs.

## 7. Tooth adjudication

For each schedule step, compare the prior frontier with the frontier after activating the proposed demand block.

```text
PROVISIONAL_TOOTH_WITHIN_SCHEDULE_PACKET
    the prior frontier collapses a live demanded edge;
    a packet-minimal repair carries every active edge;
    at least one declared gradient couples to that repair;
    claim-relevant controls pass.

NO_LIFT_NEEDED__DIG_CONTINUES
    the prior frontier already carries the added demand block.

UNRESOLVED_GATE__DIG_CONTINUES
    no adequate candidate, gradient, discriminator, or control has yet survived.
```

A tooth is provisional relative to that schedule and packet. Intermediate teeth can differ across schedule
hypotheses. No tooth becomes scientific manifold canon from a generated process fixture.

## 8. Controls and negatives

Controls are generated for the active claim. The v0.5 process requires, where applicable:

- demand erasure: removing the newly activated distinction edges erases their coface loss;
- adequacy: every admitted frontier member actually carries all active edges;
- leakage fence: gate labels and hidden generator rules never enter candidate feature keys;
- relisting: reversing the serialized demand-family list leaves schedule coverage and final behavioural frontier
  unchanged;
- rechunking: changing candidate batch size leaves the population and frontier unchanged;
- order/decomposition coverage: fused, split, and permuted gate hypotheses all execute;
- mutation rejection: validators reject any attempt to mark an order or decomposition canonical;
- evidence audit fencing: killed receipts cannot be silently re-admitted.

A control that can only produce the desired answer is not a control. A self-certifying formula copied from the answer
key is not evidence.

## 9. Digs are derived, seeds are labeled

The output keeps two separate stores:

```text
authored_seed_proposals   questions supplied before execution
derived_from_this_run     questions whose triggers are present in run receipts
```

Neither store is a canonical order. A derived dig includes the exact trigger—plural frontier, alias census, schedule
divergence, missing external contact, unexecuted cursor, or failed control. A prewritten seed may be valuable, but it
may not be described as discovered by the run.

## 10. Executed v0.5 process result

Run:

```text
python3 ratchet/ratchet_engine.py --run \
  ratchet/examples/root_order_open_packet_v0_5.json \
  --output ratchet/runs/root_order_open_run_v0_5.json
```

Observed:

```text
finite generated rows                         81
parameter proposals executed              32,400
actual behavioural partition classes       3,147
parameter aliases exposed                  29,253
candidate batches                              64
demand-family subsets evaluated                16
behaviour-by-demand-subset evaluations      50,352
ordered gate/decomposition schedules           75
gate granularities exercised               1,2,3,4 blocks
distinct intermediate trajectories             44
distinct final packet frontiers                  1
scientific manifold layers admitted               0
physical entropy types admitted                    0
```

The 75 schedules reach one final behavioural partition in this generated fixture while taking 44 intermediate
trajectories. This earns only the statement that the endpoint converges under the tested order/decomposition
population. It does not earn the order, the four family boundaries, the winning presentation as a physical object, or
any manifold rung.

## 11. v0.4 audit disposition

- The root-history loop survives as a limited predecessor: it computed real errors and a real flip.
- “36 independent structures” is killed. Only six depth/mode fits behaved independently; carrier names were cosmetic
  wrappers.
- The L5 scalar-stratum demotion is killed as scientific evidence. Six positive candidates repeated the answer-key
  formula, and two gradient ablations were hardcoded. Its negative failures and orientation datum remain source
  observations only.
- The v0.4 shipped dig queue was fully pre-authored. v0.5 separates seeds from receipt-derived digs.
- No claim that “L1–L5 are all earned” is imported by this process bundle.

## 12. Anti-fake-running invariants

A purported Ratchet run fails if it:

- iterates an authored gate list once and calls that order earned;
- fixes gate boundaries or the number of substeps before testing alternatives;
- converts an operational priority into epistemic rank;
- advertises parameter aliases or carrier labels as independent executions;
- validates prewritten receipts without executing candidate behaviours;
- uses an answer-key formula as both candidate and ground truth;
- describes an authored seed queue as derived work;
- admits a tooth without a positive live coface gradient;
- hides negative, unresolved, parked, truncated, or killed proposals;
- chooses one incomparable frontier member by taste;
- treats one finite grammar as global exhaustion;
- treats endpoint convergence as proof of a canonical path;
- says the scientific manifold was ratcheted when only a process fixture ran.

## 13. Integrity commands

```text
python3 ratchet/ratchet_engine.py --self-test
python3 ratchet/ratchet_engine.py --validate ratchet/runs/root_order_open_run_v0_5.json
python3 ratchet/bundle_ratchet_lint.py
```

The full legacy simulation harness remains a reproduction lane for its scoped receipts. A green legacy harness does not
promote those receipts through v0.5.
