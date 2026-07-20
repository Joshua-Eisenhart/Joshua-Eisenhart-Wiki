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
