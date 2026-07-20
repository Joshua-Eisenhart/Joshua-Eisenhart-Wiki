---
title: Weyl chamber / quantum Otto cycle — attachment hypotheses (owner find, 2026-07-19)
created: 2026-07-19
type: project
tags: [weyl-chamber, otto-cycle, hypothesis, entanglement, terrains, entropic-monism]
sources:
  - concepts/weyl-chambers-two-qubit-gate-geometry
  - concepts/quantum-otto-cycle-engine-strokes
  - system_v8/loop3_senses/results/carrier_tournament_v1/receipt.json
  - system_v8/entanglement_gradient/results/coherent_information_ladder_v0/receipt.json
  - system_v5/julia_carrier/scratch_jax_snapshot_20260604/eng_carnot_axiswired_jax.py
  - system_v5/julia_carrier/scratch_jax_snapshot_20260604/eng_szilard_axiswired_jax.py
framing: hypothesis
status: no-receipts-yet
---

# Weyl chamber / quantum Otto cycle — attachment hypotheses

Every line in this page is a hypothesis. No sim has run against any of
these mappings. Nothing here is admissible, canonical, or even
tool-lego-fit-probed. Status label for the whole page: `exists` (as a
written hypothesis set) and nothing higher.

Read the literature pages first:
[[concepts/weyl-chambers-two-qubit-gate-geometry]] and
[[concepts/quantum-otto-cycle-engine-strokes]]. This page is where those
two literatures get pointed at the model — speculatively.

## Warning: a Brave-AI search session confabulated a fake protocol

A Brave-AI search session run in connection with this find generated a
document describing a "64-schedule monodromy computation protocol,"
written using this project's own vocabulary (64-schedule, monodromy,
stage transitions). That text is AI confabulation about this repository —
it was not derived from any published paper and does not correspond to
any sim, receipt, or doc in Codex-Ratchet. It must not be treated as
literature, as an owner directive, or as an existing protocol. Nothing in
this page relies on it, and nothing in this page should be extended using
it. If that text resurfaces later, it is not evidence, and its confident
tone is not a substitute for a citation.

## (a) The model's "Weyl sheets" are not the two-qubit Weyl chamber

The model's own vocabulary already contains "Weyl sheets" tied to
chirality — L/R objects (see 178/08,
`08_ENTROPIC_GEOMETRY_FLUX_AND_EXCEPTIONAL_MATH.md`, and
[[concepts/entropic-geometry-one-object]], Layer 6, "joint Weyl sheets,"
`(eta, alpha, beta)` parameters, BKM Hessian of joint Umegaki divergence).
That is a *different* object from either literature chamber described on
the Weyl-chamber literature page. State the distinction before hypothesizing
any relation:

- The model's Weyl sheets are chirality-indexed (L, R) geometric leaves
  carrying a joint divergence metric on `(eta, alpha, beta)`.
- The two-qubit gate Weyl chamber (Zhang-Vala-Sastry-Whaley) is a
  tetrahedron of local-equivalence classes of two-qubit unitaries in
  `(c1, c2, c3)`.
- The eigenvalue-ordering Weyl chamber is a simplex of density-matrix
  spectra.

**Hypothesis, unearned:** all three are "Weyl chamber"-family objects
because all three arise from quotienting a larger space by a Weyl group
action (of `su(4)` for the gate chamber, of `U(N)` for the spectral
chamber, and of whatever symmetry group governs the model's L/R
chirality split for the model's sheets). If that shared ancestry is real,
the model's sheets might sit inside, or be a further quotient of, one of
the two literature chambers. This has not been checked. It could equally
be a coincidence of naming (the word "Weyl" attaches to any construction
built from a Weyl-group quotient, in many unrelated corners of math). No
sim, no representation-theoretic derivation, and no map between the
model's `(eta, alpha, beta)` coordinates and either literature chamber's
coordinates exists yet.

## (b) Wall crossings as model stage transitions and 64-schedule monodromy

**Hypothesis, unearned:** the walls of a Weyl chamber (spectral
degeneracy, in the eigenvalue-ordering sense) might formalize what the
model calls "stage transitions" — points where the active structure
changes qualitatively — and the model's 64-schedule sims might exhibit
monodromy (a state that returns to its starting point in schedule-space
but picks up a nontrivial transformation) precisely because a schedule
loop encircles a wall.

This is attractive because it would give the model's stage-transition
language a literature-grounded mechanism (Landau-Zener at the dynamical
level, Uhlmann/Berry phase at the geometric level — both described on the
literature page). It is also exactly the shape of claim the confabulated
Brave-AI protocol pretended to already answer. It has not been checked
against a single 64-schedule receipt. The concrete, falsifiable version of
this hypothesis: pick a 64-schedule sim result already in the repo, compute
the density-matrix spectrum at each schedule step, and check whether any
schedule loop that shows monodromy in the existing result also crosses or
closely approaches a spectral degeneracy. That check has not been run.

## (c) Perfect-entangler polyhedron and the entanglement-centrality doctrine

The owner's standing doctrine treats entanglement as centrally load-bearing
for carrier viability (`user_igt_two_engine_discovery`-adjacent doctrine;
[[concepts/entropic-geometry-one-object]] entropy-licensing table, "cut
entropy, mutual information, coherent information where operands exist").
An existing receipt is directly relevant as a *result*, independent of this
hypothesis: `system_v8/loop3_senses/results/carrier_tournament_v1/receipt.json`
records a product (unentangled) carrier lane
(`product_single_qubit_per_stage`) scoring near chance
(`estimate` values clustering around 0.475, against
`computed_chance_accuracy` 0.4956) versus entangled anchor lanes
(`senses_v2_anchor`) scoring materially higher (`estimate` values
clustering around 0.84-0.90, e.g. 0.8397, 0.8776). That result — a product
carrier underperforming an entangled anchor — is real and already in the
repo; the owner's recollection of roughly "0.475 vs 0.878" matches these
values closely enough to be the same finding, cited here for the exact
receipt path rather than re-derived.

**Hypothesis, unearned:** the perfect-entangler polyhedron (the specific
sub-region of the two-qubit Weyl chamber where a gate can generate
maximal entanglement from a product state) might give a *geometric*
account of why the product lane underperforms — i.e. the carrier's
generating gate, if it could be located in the chamber, might sit outside
or near the boundary of the perfect-entangler region, and that location
might correlate with (not "cause," in this project's banned-verb sense —
"co-vary with") the tournament score. Nobody has computed which chamber
point the carrier tournament's gates correspond to. This is a plausible
follow-on probe, not a result.

## (d) Otto strokes and the model's S-up/S-down terrain strokes plus the Carnot/Szilard weld

The model's terrain vocabulary already has an S-up (opening,
entropy-increasing) and S-down (retention, entropy-decreasing) stroke
pair. Existing sims `system_v5/julia_carrier/scratch_jax_snapshot_20260604/eng_carnot_axiswired_jax.py`
and `.../eng_szilard_axiswired_jax.py` are queued engine legs for a
Carnot/Szilard weld, per the standing lane table in this repo's project
instructions.

**Hypothesis, unearned:** the quantum Otto cycle's four-stroke structure
(isentropic / isochoric-hot / isentropic / isochoric-cold) might map onto
a two-stroke S-up/S-down terrain pair extended to four by splitting each
terrain stroke into an isolated (isentropic) phase and a bath-coupled
(isochoric) phase. If that mapping holds, the Otto-cycle literature's
"quantum friction" term (finite-time non-adiabaticity) would translate
directly into a cost on the model's S-up/S-down strokes whenever they are
run at finite rate rather than quasi-statically, and the coherence-work
literature (Francica et al., PRL 125, 180603) would give a second,
partially-recoverable term distinct from friction. None of this has been
checked against the `eng_carnot`/`eng_szilard` sims, which as of this
writing are queued, not run against this mapping.

## (e) The entanglement pawl: routing around degeneracy walls

An existing result in `system_v8/entanglement_gradient/results/coherent_information_ladder_v0/receipt.json`
shows, on a 3-qubit nested-cut ladder under a dissipative drive, the
entangling-lane `SAB` (a coherent-information-adjacent quantity) reaching
its most negative value at tick 0 (`entangling_min_SAB`: cut1 -0.487,
cut2 -0.303) and the product-lane control staying non-negative throughout
(`P1_product_SAB_nonnegative: true`). This is consistent with the owner's
recollection of coherent information collapsing very early under
dissipation, though the receipt as read in this pass does not itself
state a "2 ticks" figure — that specific tick-count should be re-checked
against the full `data.sign_map` time series in the receipt before being
repeated as a number, rather than assumed correct from memory.

**Hypothesis, unearned, reframed as a question:** if the model's
dissipative terrain-flow can be understood as a trajectory through the
eigenvalue-ordering Weyl chamber, does the observed early collapse of
coherent information correspond to the trajectory passing directly
through a wall (a genuine degeneracy), or does it stay in the chamber's
interior the whole time and the collapse is a bulk (non-geometric) effect
of the dissipation channel itself? If the former, an Otto-style
finite-time control (routing the schedule to avoid or slow-pass the wall)
might be a genuine lever for preserving the resource longer. If the
latter, the Weyl-chamber framing adds no leverage here and the
degeneracy-avoidance idea should be dropped. This has not been
distinguished by any computation yet — it is a fork in the hypothesis,
not a claim either way, and it should not be collapsed to one branch
before a sim checks it.

## Status and next step

Everything above is `exists`-as-hypothesis only. The concrete, cheapest
falsifiable next step, if the owner wants to spend a cycle on this: take
one already-computed 64-schedule or carrier-tournament result, compute
the density-matrix spectrum at each step, and check for wall-crossings
against the existing monodromy/collapse findings. That is a read-only
diagnostic on existing data, not a new build, and it would directly test
hypothesis (b) and give the first real receipt for this whole page.

---

## Round 2: spinor-Otto ladder — real literature vs thin vs nonexistent (2026-07-19)

This section is a second literature pass, requested to ground a
preregistered build card (`system_v8/otto_weld/SPINOR_OTTO_LADDER_CARD_v0.md`,
Codex-Ratchet repo, uncommitted — card only, no sim code written against
it yet). Same discipline as round 1: every claim below is either a cited
real paper, marked thin (a handful of tangential hits, no direct
literature), or marked nonexistent (searched, not found). Nothing here is
a repo receipt unless cited as one.

### (a) Spin-1/2 quantum Otto engines and the NMR carbon-13 experiment — REAL, well-established

Peterson et al. ran a proof-of-concept quantum Otto cycle on the
spin-1/2 of the ¹³C nucleus in ¹³C-labelled chloroform (CHCl₃ diluted in
acetone-D6), driven on a 500 MHz Varian NMR spectrometer, and measured
finite-time efficiency in excess of 42% at maximum power (arXiv,
Peterson et al. 2019 — cited as "efficiency in excess of 42% at maximum
power" against the reversible Otto bound `eta = 1 - Bc/Bh`). This is a
genuine, oft-cited experimental result, not a theory proposal.

Quantum friction — the energetic cost of coherence generated by
finite-time, non-adiabatic driving through a non-commuting Hamiltonian
sequence — is a real, separately-established concept. Two representative
papers: "Irreversible Work and Internal Friction in a Quantum Otto Cycle
of a Single Arbitrary Spin" (arXiv:1605.02522) treats an arbitrary driven
spin as the Otto working fluid and derives how the control-field ramp
profile sets the friction/extractable-work tradeoff; "Vanishing efficiency
of speeded-up quantum Otto engines" (arXiv:1906.07473) is the sharper
negative result — push the cycle to short enough time and efficiency
degrades toward zero even though power may still rise. Both are directly
relevant to Rung 1's "fast ramp must show a coherence-generation work
penalty" control below.

**Verdict: real, load-bearing literature.** The 42%-vs-`1-Bc/Bh` NMR
number is a genuine external target Rung 1 can be checked against
(within stated tolerance, on this sim's own idealized GKSL model, not a
claim of reproducing the NMR apparatus).

### (b) Coupled-spin / two-qubit Otto cycles and entanglement-enhanced work — REAL, but heterogeneous and partly definitional

Two-qubit and coupled-spin Otto cycles are an active, real literature.
"Finite-time two-spin quantum Otto engines: shortcuts to adiabaticity vs.
irreversibility" (arXiv:2102.11657) runs a two spin-1/2 anisotropic-XY
Otto cycle and compares shortcut-to-adiabaticity driving against plain
non-adiabatic driving. "Efficiency Enhancement up to Unity in a
Generalized Quantum Otto Engine... Two-Qubit Heisenberg XXZ Chain"
(arXiv:2503.21590) reports a generalized cycle with two distinct
reservoir-coupling configurations reaching unity efficiency in a
particular limit, and states as a finding that positive work extraction
tracks the sum of population differences between entangled and
unentangled states across the non-equilibrium stage — i.e. that paper
does assert an entanglement/work-extraction link, stated in terms of
level-population differences, not in terms of a two-qubit Weyl-chamber
gate coordinate.

Read honestly: the literature supports "entanglement dynamics and work
extraction co-vary in specific coupled-spin Otto models," stated at the
level of populations and energy-level restructuring. It does **not**
contain a paper that frames the interaction stroke as "traversing the
perfect-entangler region of the two-qubit gate Weyl chamber" — that
specific geometric framing (interaction stroke as a path through
Zhang-Vala-Sastry-Whaley coordinates `(c1,c2,c3)`) is this project's own
construction, carried over from round 1's item (c), not a published
result. Rung 2 below is explicit that the perfect-entangler-region framing
is the model's addition to a real but differently-framed literature, not
itself literature.

**Verdict: real underlying phenomenon (entanglement/work-extraction
covariation in coupled-spin Otto cycles), thin-to-nonexistent for the
specific Weyl-chamber-gate-geometry framing** this project wants to use
to locate the interaction stroke.

### (c) G2 in physics — the 7-dim rep and Weyl chamber are real math; a G2 quantum-thermodynamics or multi-level-engine literature is thin to nonexistent

G2 is real, well-studied pure mathematics: rank 2, dimension 14,
7-dimensional fundamental representation (the smallest nontrivial
representation, realized as the imaginary octonions), Weyl group of
order 12, and — the structural fact the build card below leans on — the
G2 Weyl chamber literature (e.g. Wildberger's construction, the
Springer-reference treatments of G2's root system) does describe a
12-wall chamber built from two root lengths at 30-degree relative angles,
consistent with the "30-degree cone, 12 walls" framing in the task. This
is standard representation theory, not a novel claim.

Multi-level quantum heat engines are also real and well-established as a
*separate* literature: "Quantum Heat Engine With Multi-Level Quantum
Systems" (arXiv:quant-ph/0504118) is a canonical early paper proposing a
universal class of multi-level QHEs, including a worked 3-level case —
but its multi-level structure is generic (arbitrary energy-level sets),
not organized by any exceptional-group symmetry.

Searching directly for the intersection — G2 (or any exceptional Lie
group) organizing a quantum thermodynamic cycle, an Otto engine, or a
multi-level working substance — returned essentially nothing. The closest
hits were pure representation-theory papers on G2's semisimple conjugacy
classes (Springer, "Quantum Exceptional Group G2 and its Semisimple
Conjugacy Classes" — "quantum" there means quantum-group deformation of
the classical group, an unrelated sense of "quantum" from quantum
thermodynamics) with no thermodynamic content at all.

**Verdict: the group theory (dim 14, 7-dim rep, 12-wall/30-degree Weyl
chamber) is real math and can be cited straight. A G2-organized quantum
thermodynamic engine is not a thing that exists in the literature — Rung
3 of the build card below would be the first one anywhere the owner has
found, not a replication of prior work. State this plainly rather than
implying precedent.**

### (d) Jordan-algebraic quantum thermodynamics / Gibbs states on the Albert algebra — nearly nonexistent, as expected

Jordan algebras and the exceptional Jordan algebra (Albert algebra,
`H3(O)`, 3x3 octonionic Hermitian matrices under `X∘Y = 1/2(XY+YX)`) are
real, well-studied mathematical-physics objects with genuine recent
literature on their own terms: "The Standard Model, The Exceptional
Jordan Algebra, and Triality" (arXiv:2006.16265), and — closer to a
thermodynamic-sounding title — "Vinberg's T-Algebras From Exceptional
Periodicity to Black Hole Entropy" (arXiv:2312.12371), which discusses
"entropy" only in the black-hole-entropy-formula sense (an algebraic
invariant playing the role of an entropy function in supergravity moduli
spaces), not a Gibbs/thermal statistical-mechanics entropy. A search
specifically for a Jordan-algebraic Gibbs state, a Jordan-algebra
partition function, or a thermal density-operator formalism built
natively on `H3(O)` (rather than on the standard complex-matrix Jordan
algebra, which is just a restatement of ordinary quantum statistical
mechanics) returned nothing.

**Verdict: essentially no literature.** There is real math on `H3(O)`
itself and on its automorphism group `F4`, but no real literature putting
a Gibbs/thermal state or a von-Neumann-style entropy functional directly
on the Albert algebra as a thermodynamic object. Rung 4 of the build
card is explicitly the model's own territory, stated as such — not a
gap-fill of an existing but obscure field.

### (e) Geometric/topological phases in thermodynamic cycles — REAL, established field

This is the one item in this round that is unambiguously a live,
established field rather than a thin corner. Representative results:
"Geometric Quantum Thermodynamic Engine under an Isothermal Operation: An
Application of a Thouless Pumping" (arXiv:2505.06851) builds a cyclic
open-system engine where finite work per cycle survives even in the
adiabatic limit, arising from the parametric dependence of the
instantaneous steady state rather than curvature; "Demon driven by
geometric phase" (arXiv:2205.15193) and "Geometrical Formulation of
Adiabatic Pumping as a Heat Engine" (arXiv:2003.05567) are further
instances of the same general result: a closed loop in a Hamiltonian's
parameter space produces a geometric (Berry-phase-like, or
Berry-Sinitsyn-Nemenman-curvature) contribution to transported work or
charge, on top of the ordinary dynamical-phase contribution. The
Thouless-pumping framing (adiabatic geometric pumping, no average bias,
current/heat still flows) traces back to Thouless's original charge-pump
construction and is experimentally confirmed in multiple platforms
(charge transport, spin pumping, superconducting charge pumps).

**Verdict: real, mature field.** This is the strongest-literature item
of the five, and it is the one most directly usable as an honest external
anchor for any later monodromy/wall-crossing work this project pursues
(hypothesis (b) in round 1 above) — a genuine geometric-phase mechanism
for path-dependent work exists in the literature, independent of whether
this project's own 64-schedule sims turn out to exhibit it.

### Quarantine, reaffirmed

As in round 1: any pasted Brave-AI (or similarly generated) synthesis
that uses this project's own vocabulary — "topological Otto cycle,"
"`M_64` monodromy," or any similarly-shaped term that sounds like a named
protocol — is confabulation dressed in project language, not literature,
unless a specific arXiv ID or DOI is attached and independently checked.
None of the five literature areas above produced a paper matching that
shape. If such a synthesis resurfaces in this project's channels, treat
it exactly as round 1 treated the "64-schedule monodromy computation
protocol" text: quote it, name the source as an AI search session, and do
not build against it.

### Sources (round 2)

- Peterson et al., NMR quantum Otto engine, ¹³C-labelled CHCl₃, ~42%
  efficiency at maximum power (cited via search; verify arXiv ID directly
  before citing in a paper — this pass surfaced the finding through
  secondary citations, not a direct fetch of the original preprint).
- [Vanishing efficiency of speeded-up quantum Otto engines](https://arxiv.org/abs/1906.07473)
- [Irreversible Work and Internal Friction in a Quantum Otto Cycle of a Single Arbitrary Spin](https://arxiv.org/abs/1605.02522)
- [Finite-time two-spin quantum Otto engines: shortcuts to adiabaticity vs. irreversibility](https://arxiv.org/abs/2102.11657)
- [Efficiency Enhancement up to Unity in a Generalized Quantum Otto Engine... Two-Qubit Heisenberg XXZ Chain](https://arxiv.org/abs/2503.21590)
- [Quantum Heat Engine With Multi-Level Quantum Systems](https://arxiv.org/pdf/quant-ph/0504118)
- [Quantum Exceptional Group G2 and its Semisimple Conjugacy Classes](https://link.springer.com/article/10.1007/s10468-019-09913-4)
- [An easy construction of G2 (Wildberger)](https://web.maths.unsw.edu.au/~norman/papers/G2Construction.pdf)
- [G2 (mathematics) — Wikipedia](https://en.wikipedia.org/wiki/G2_(mathematics))
- [The Standard Model, The Exceptional Jordan Algebra, and Triality](https://arxiv.org/pdf/2006.16265)
- [Vinberg's T-Algebras From Exceptional Periodicity to Black Hole Entropy](https://arxiv.org/pdf/2312.12371)
- [Geometric Quantum Thermodynamic Engine under an Isothermal Operation: An Application of a Thouless Pumping](https://arxiv.org/pdf/2505.06851)
- [Demon driven by geometric phase](https://arxiv.org/pdf/2205.15193)
- [Geometrical Formulation of Adiabatic Pumping as a Heat Engine](https://arxiv.org/pdf/2003.05567)

### Status

`exists`-as-literature-summary only. No sim in this round. The build
card this section grounds (`system_v8/otto_weld/SPINOR_OTTO_LADDER_CARD_v0.md`
in the Codex-Ratchet repo) is card-only and uncommitted, staged for
owner review before any rung is built.
