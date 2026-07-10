# Dual Ratchet: Geometry, Entropy, and the Jordan Floor

## Research Thesis

The most defensible version of the project is not “four operators are already
inside every stage.” It is:

> A macro-stage begins with a declared candidate family. A geometry ratchet and
> an entropy ratchet independently remove candidates. Their convergent survivor
> classes become the substages. The macro-stage's Axis-6 precedence sign is
> inherited by those survivors only after they are admitted.

This is a real research program. It is not yet a theorem and is not what the
current 64-channel scout implements.

## What The Literature Supports

Jordan, von Neumann, and Wigner established the algebraic setting in which the
symmetrized product can describe observables without using the full associative
product. The later octonionic literature makes clear that the exceptional
Jordan/Albert direction is mathematically legitimate but structurally special.

Petz's quasi-entropy work gives the associative entropy side a strong gate:
relative entropy and related quantities are constrained by data processing under
appropriate positive/completely positive maps. Equality conditions connect
lossless processing with recovery. That is a good model for an entropy pawl:
the candidate must survive a monotonicity test and explain equality cases.

Quantum information geometry supplies the matching geometry side. The BKM
metric arises from the second-order behavior of relative entropy, and the
monotone-metric literature characterizes broad families through operator
monotone functions. The BKM metric is distinguished by a dual-connection
property in the finite-dimensional setting studied by Grasselli and Streater.

Schupp and Szabo show that one can formulate states, traces, GNS constructions,
and completely positive dynamics for nonassociative observables by passing
through a universal enveloping construction. This is an implementation route,
not a shortcut: positivity, composition, and entropy must still be defined and
tested for the particular exceptional system.

## Proper Dual-Ratchet Contract

For each source macro-slot, define a candidate set `C` containing admissible
terrain/operator/order/action-side maps. Do not put `4` into the candidate
count, the clustering code, or the gate.

The geometry ratchet `G` should retain candidates only when they satisfy the
source-faithful quotient and dynamical tests:

- CPTP or explicitly declared Jordan-positive dynamics;
- nontrivial, nuisance-invariant channel fingerprints;
- order or noncommutation sensitivity against a commuting null;
- finite closure and reproducibility across seeds;
- no dependence on labels, row position, or candidate enumeration order.

The entropy ratchet `E` should retain candidates only when they satisfy the
entropy-side tests:

- Umegaki/BKM or the explicitly declared Jordan replacement is defined;
- the appropriate data-processing or monotonicity inequality holds;
- fixed-point and wrong-pawl controls behave as expected;
- entropy-kind distinctions survive the same nuisance controls;
- equality cases have a recovery or preservation interpretation where the
  theory requires one.

The candidate survivor is not `G(C)` or `E(C)` alone. It is the stable
intersection:

```text
S_EG = E(G(C))
S_GE = G(E(C))
S*   = stable_equivalence_classes(S_EG ∩ S_GE)
```

The four-substage claim is earned only if `S*` has four minimal classes per
macro-slot, the classes persist across seeds and candidate enumeration order,
and removing or permuting a class degrades a held-out task or object metric.

## Axis-6 Placement

Axis-6 must be treated as a composition choice, not as a post-hoc sign field.
For a terrain flow `T_tau` and candidate operator `O_k`, the two finite forms
are:

```text
Phi_up(tau,k)   = T_tau compose O_k
Phi_down(tau,k) = O_k compose T_tau
```

After survivor admission, a macro-stage may compose its four classes using one
declared sign. The fixed sign is then a consequence of the source slot's
precedence law. It is not evidence that all four classes were necessary.

## Current Local Evidence

The source-fidelity linter validates 16 slots and a 64-row candidate expansion.
The finite one-step scout distinguishes 64 hard-coded candidate channels under
one probe battery. A new fixed-sign system-ID instrument now executes both
conditional product-cycle orientations over all 16 slots, uses PySINDy and
PyKoopman as external identifiers, re-identifies all 16 macro maps, and finds
every beat removal and duplication changes held-out exact transitions.

This upgrades the evidence from a one-step atlas to a real sequential
candidate with local transition-level teeth. It still does not support the
stronger emergent claim: the four cells, cycle, canonical-first rotation,
source slots, exact derivative access, and house maps are premises rather than
survivors emitted by the two ratchets.

The later source-faithful learning packet now sharpens that result. It runs
both engines, all six oriented Ti/Te/Fi/Fe cycles, three learned-weight seeds,
and a 1,080-scenario JAX sweep while preserving one Axis-6 sign across all four
phases of each slot. Type 1 selects `Ti > Fe > Fi > Te` on all three seeds and
in all 540 JAX scenarios. Type 2 splits between two leading orders and fails
the declared stability gate. The full scientific verdict is therefore still
red.

PyDMD and deeptime independently distinguish the two generated Type-2
trajectory families, with clean accuracy `1.0` and `0.9444444444` and controls
near chance. That is a good recognizer result. It is not a selector because
both classes were supplied by the construction.

## Tool-Backed Entropy Floor

Three new repositories now separate the floor problem into exact, numerical,
and formal associative roles:

- ALCO 1.1.2 gives an independent exact J3(O) algebra oracle. The local packet
  passes 23/23 polynomial-identity gates and kills a corrupted Fano product.
- QICS 1.1.3 gives specialized numerical quantum-relative-entropy and
  operator-perspective cones. Its complete upstream suite passes 22/22 in an
  isolated environment. The local fixed-input oracle adds 11/11 producer
  checks, nine optimal solves, direct-spectral agreement within `8.17e-10`,
  six accepted contractions, six rejected non-CPTP controls, and a
  byte-identical rerun.
- Physlib gives a machine-checked finite-dimensional associative DPI path for
  sandwiched Renyi and ordinary quantum relative entropy.

These do not collapse into one result. ALCO has the exceptional carrier but no
spectral log or DPI. QICS and Physlib have the entropy/DPI machinery but live
on associative Hermitian operators and CPTP maps. The open bridge is exactly
what it should be: define the exceptional positive cone, spectral functional
calculus, entropy, and Jordan-positive maps, then test a bounded DPI without
smuggling in an unavailable tensor product.

## Research Consequences

The next selector should be named for the unresolved question, not the desired
cardinality. The two leading Type-2 orders need a preregistered independent
judge whose score is neither the generating loss nor a class label. Temporal
shuffle, block permutation, reversal, label shuffle, and a declared tie band
must be kill conditions.

The broader emergence sim remains
`engine_dual_ratchet_substage_emergence_v0`: its candidate family must not put
four into the candidate count or clustering rule.

Its positive result would be: four substage equivalence classes are emitted by
two independent ratchets and remain load-bearing in held-out work. Its failure
would still be useful: the project would retain the finite channel atlas while
demoting the four-substage engine interpretation.

The Jordan/octonion question is downstream of this gate. A successful finite
exceptional-Jordan entropy construction may deepen the carrier floor, but it
cannot retroactively validate an installed four-stage schedule.

## Sources

- [[projects/codex-ratchet/source-intake/dual-ratchet-math-article-register-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[projects/codex-ratchet/jordan-octonion-entropy-pawl-floor-receipt-2026-07-08]]
- [[projects/codex-ratchet/external-86-v84-92-foundations-engine-audit-receipt-2026-07-09]]
- [[concepts/sindy-koopman-system-identification-for-qit-engines-2026-07-09]]
- [[projects/codex-ratchet/repository-research-and-tool-validation-2026-07-09]]
- [[projects/codex-ratchet/packet-102-canonical-rerun-audit-2026-07-09]]
