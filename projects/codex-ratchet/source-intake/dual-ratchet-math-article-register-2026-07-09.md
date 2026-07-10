# Dual-Ratchet Math Article Register - 2026-07-09

## Intake Status

This is an external research register, not a local sim receipt. The articles
below were located from primary or author-hosted scholarly sources and read for
their relevance to the proposed geometry/entropy dual ratchet, Jordan
algebras, Umegaki relative entropy, monotone metrics, and octonionic carriers.

The local `raw/` tree remains immutable under wiki policy. This register is the
processed source surface; the concept synthesis is
[[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]].

## Sources

### Jordan, von Neumann, Wigner (1934)

[On an Algebraic Generalization of the Quantum Mechanical Formalism](https://doi.org/10.2307/1968117), *Annals of Mathematics* 35(1), 29-64.

The foundational paper replaces the associative product with the symmetrized
Jordan product in the observable setting and classifies finite-dimensional
formally real cases. Project relevance: it supports treating a Jordan product
as a mathematically serious nonassociative observable layer. It does not prove
that a particular QIT engine must select the Albert algebra or four substages.

### Petz (1985-1986)

[Quasi-entropies for states of a von Neumann algebra](https://doi.org/10.1016/0024-3795(85)90036-0) and [Quasi-entropies for finite quantum systems](https://doi.org/10.1016/0034-4877(86)90067-4).

These works place relative entropy and related quasi-entropies inside an
operator-algebraic monotonicity framework. Project relevance: the entropy
ratchet can use data processing and equality/recovery as a gate family rather
than treating Umegaki as an arbitrary scalar. The results are associative
operator-algebra results; they do not automatically lift to exceptional
Jordan systems.

### Grasselli and Streater (2000)

[On the Uniqueness of the Chentsov Metric in Quantum Information Geometry](https://arxiv.org/abs/math-ph/0006030).

The paper identifies the Bogoliubov-Kubo-Mori metric as the unique monotone
metric, up to scale, for which the plus and minus affine connections are dual
in the stated finite-dimensional setting. Project relevance: it gives a
source-backed reason to keep geometry and relative-entropy Hessians together.
It does not establish a dual ratchet or a discrete four-stage decomposition.

### Hansen (2006)

[Characterization of symmetric monotone metrics on the state space of quantum systems](https://arxiv.org/abs/math-ph/0601056).

This paper completes the Morozova-Chentsov-Petz characterization of symmetric
monotone metrics through operator-monotone functions. Project relevance: a
geometry ratchet should state which monotone metric family it admits and which
function selects it. A finite sim that observes one metric identity is not a
classification theorem.

### Baez (2002)

[The Octonions](https://arxiv.org/abs/math/0105155), *Bulletin of the AMS* 39.

This is the standard mathematical orientation for octonions, alternativity,
triality, and exceptional structures. Project relevance: it marks the precise
carrier boundary where associativity is unavailable. It does not imply that
octonions are forced by a qubit engine or that octonionic matrix entropy is
already defined by the associative von Neumann formula.

### Schupp and Szabo (2023)

[An algebraic formulation of nonassociative quantum mechanics](https://arxiv.org/abs/2311.03647).

The authors construct a probabilistic nonassociative quantum formalism using
universal enveloping algebras, states, traces, GNS constructions, and
completely positive dynamics, with finite-dimensional Jordan and octonion
examples. Project relevance: this is the strongest direct source for the
proposed octonionic QIT direction. It supplies a route to define states and
dynamics, but it is not a proof that the current Leviathan engines implement
that formalism or that DPI holds for the exceptional rung.

### Liebmann, Rühaak, Henschenmacher (2019)

[Non-Associative Algebras and Quantum Physics - A Historical Perspective](https://arxiv.org/abs/1909.04027).

This survey places Jordan and octonionic quantum proposals in historical and
mathematical context and explicitly warns that several later proposals remain
speculative. Project relevance: it is a guard against laundering a historical
possibility into a forced engine result.

### ALCO 1.1.2 (2025)

[ALCO: Tools for algebraic combinatorics](https://bnasmith.github.io/alco/)
is a GAP package with explicit octonion and Jordan-algebra implementations.
Its simple Euclidean Jordan algebra constructor includes the exceptional
rank-3, degree-8 Albert algebra. Project relevance: it is an independent exact
oracle for J3(O) polynomial identities. It does not implement a spectral
logarithm, entropy, positive channel, or data-processing theorem.

### QICS 1.1.3 (2025)

[QICS](https://github.com/kerry-he/qics) is a specialized primal-dual conic
solver for quantum-information optimization. Its native cone set includes
quantum entropy, quantum relative entropy, conditional entropy, operator
perspectives, Renyi, and sandwiched-Renyi quantities. Project relevance: it can
serve as an independent numerical oracle for the associative entropy ratchet.
Its cones are Hermitian-matrix/operator constructions and do not constitute an
exceptional-Jordan entropy lift.

### Physlib Quantum-Information DPI (2026)

[Physlib](https://github.com/leanprover-community/physlib) now contains a
[Lean module for the data-processing inequality](https://github.com/leanprover-community/physlib/blob/master/QuantumInfo/Entropy/DPI.lean).
The module develops sandwiched-Renyi DPI for finite-dimensional states and CPTP
maps, then obtains the ordinary quantum-relative-entropy case. Project
relevance: this is a machine-checked associative reference for the entropy
pawl and a stronger oracle than another floating-point mirror. It remains a
complex-Hermitian, CPTP, tensor-product theory; it does not prove DPI for J3(O)
or supply an exceptional composite.

[Lean-Quantum: Toward AI-Assisted Formalization of Quantum Information](https://arxiv.org/abs/2607.05492)
describes the current formal infrastructure and the sandwiched-Renyi DPI route.
It is a timely formalization source, not evidence that the Ratchet engines use
the theorem correctly.

### PyDMD and deeptime

[PyDMD](https://github.com/PyDMD/PyDMD) implements multiple dynamic-mode and
Koopman-oriented methods, including Hankel DMD and BOP-DMD.
[deeptime's VAMP implementation](https://deeptime-ml.github.io/latest/notebooks/vamp.html)
estimates a finite-lag Koopman operator and supplies VAMP scores for ranking
features. Project relevance: they are independent kinetic recognizers for
candidate stage orders. Recognition of generated classes is not a derivation
or truth selector.

## Source-to-Project Translation

| External result | Permitted local use | Not permitted |
|---|---|---|
| Jordan product and formal-real classification | candidate observable/carrier layer | forced H -> O or four substages |
| DPI and recovery | entropy-ratchet gate and equality control | exceptional-Jordan theorem |
| BKM/monotone metrics | geometry-ratchet metric family | unique project geometry without a gate |
| octonion structure | nonassociative candidate and kill controls | engine octonion admission |
| nonassociative QM formalism | implementation design reference | claim that current code implements it |
| ALCO exact Jordan algebra | independent J3(O) polynomial oracle | spectral entropy or DPI |
| QICS entropy cones | associative numerical entropy/perspective oracle | exceptional-Jordan theorem |
| Physlib DPI | machine-checked associative CPTP reference | J3(O) or engine admission |
| PyDMD/deeptime | independent kinetic recognizers | true-order selection from supplied classes |

## Research Gaps Left Open

1. A mathematically explicit exceptional-Jordan relative entropy with a proven
   data-processing theorem for the maps used by the engines.
2. A dual-ratchet experiment where geometry and entropy independently emit the
   same four minimal survivor classes.
3. A proof that the Axis-6 sign is inherited by every surviving substage rather
   than inserted as a schedule label.
4. A source-faithful bridge from the surviving maps to Type-1/Type-2 loops.
5. A formal boundary theorem or explicit replacement for composition at the
   exceptional J3(O) rung; the associative Physlib theorem cannot be imported
   by analogy.

## Local Validation Router

The source register does not inherit local execution status. Current pinned
checkouts, upstream tests, and bounded integrations are recorded at
[[projects/codex-ratchet/repository-research-and-tool-validation-2026-07-09]].
