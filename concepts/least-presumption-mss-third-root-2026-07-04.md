---
title: Least presumption as third root — MSS, dropped and rediscovered
created: 2026-07-04
updated: 2026-07-04
type: concept
tags: [concept, mss, least-presumption, nonassociativity, owner-doctrine, foundations, scratch-diagnostic]
framing: nominalist-constraint-admissibility
status: owner-voice capture + doctrine history; promotion_allowed=false
promotion_allowed: false
sources:
  - "Claude memory: user_least_presumption_weakest_structure.md"
  - "system_v7/sims/MSS_BASIS_CONSTRAINT_CONSOLIDATION_20260703.md"
  - "mss_and_rung_climb_foundations_DRAFT_20260615.md"
related:
  - "[[platonic-nominalism]]"
  - "[[owner-thesis-and-cosmology]]"
  - "[[igt-discovery-and-two-engines-2026-07-04]]"
  - "[[iff-chain-identity-duality-2026-07-03]]"
---

# Least presumption as third root — MSS, dropped and rediscovered

Provenance: worked out in sessions 2026-07-01 to 2026-07-04 (threads running in
the Desktop repo clone); salvaged from Claude memory 2026-07-04. Source memory
file: `user_least_presumption_weakest_structure.md`.

Status: owner-voice doctrine capture. Nothing here is admitted math beyond
what is separately named as already-simmed. promotion_allowed: false.

## Bottom line

The owner added a third root constraint on 2026-07-03: least presumption. It
is not a statement about objects — it is a meta-constraint over selection.
The system already had this rule, under the name MSS (Minimal Survivable
Structure), recorded on 2026-06-15. It was never wired into a gate, so it got
dropped without anyone deciding to drop it. It has now been rediscovered and
the fix is to make it a gate so it cannot be silently lost again.

## The third root: least presumption

Owner, 2026-07-03: "The ultimate constraint of axioms is LEAST PRESUMPTION. A
least-presumed thing is the weakest surviving structure. The most simple
process. The weakest thing."

Unlike the first two roots — F01 (finitude, bounds size) and N01 (forbids
commuting) — least presumption does not constrain objects directly. It
constrains the *selection process*: among admissible structures, keep the
weakest one that still persists. It is implied by the digging process itself
— you keep removing presumptions until you hit the weakest thing that still
survives.

## The fourth, emergent: nonassociativity

T01 (explicit bracketing / nonassociativity) is reframed as emergent, not
posited. Associativity, `(a·b)·c = a·(b·c)`, is an extra coherence assumption
that grouping does not matter. Least presumption drops that assumption by
default, so nonassociativity is the default and associativity is what has to
be added.

The division-algebra ladder is the worked example: R → C → H → O each step
presumes less (losing order, then commutativity, then associativity).
Octonions are the weakest structure that still survives as a division
algebra; sedenions, weaker still, die (zero divisors, they fail to persist).

This status is marked plausible synthesis, not canon: the 2026-07-03
consolidation verdict says MSS implies "don't assume associativity," but the
sims say nonassociativity is installed at the Cl(0,6)/3-qubit rung, not
forced by the bare root.

## Already in the corpus — MSS, named, dropped, ungated

Found on 2026-07-03 via indexed search. This was not new work. MSS (Minimal
Survivable Structure) was recorded on 2026-06-15 in
`mss_and_rung_climb_foundations_DRAFT_20260615.md`, defined as:

> Admit ONLY the weakest structure that survives + still evolves; "presume
> the least" is itself the implicit constraint; NOT Occam (Occam picks dead
> minima), NOT a root axiom — an admission META-GATE.

It governed a whole methodology restart (wiki session 2026-06-14, "v7
methodology overhaul — MSS and restart"), and was already simmed: `sim_
minimal_surviving_set.py`, `finite_distinguishability_quotient_forced_or_
installed_carrier_v0` (three engines), `sim_teleological_selection_
constraint_narrowing.py`.

The drop mechanism: the Desktop estate (system_v5) has zero MSS hits. MSS
existed as prose and scattered sims, wired into no gate, so it fell out of
enforcement — the same failure class as route-salience drift. The fix
proposed: turn MSS into a gate (a forced-vs-installed test in the sim-contract
linter) so it cannot be dropped again.

MSS is NOT Occam's razor: Occam can pick a dead minimal thing; MSS requires
an evolvable survivor. It is not a root axiom either — it is a meta-gate
(M0) sitting above admissions. Keep `Min(Surv(C))` plural: anti-collapse
applies at the base too.

## The direction correction on build order

Owner correction, 2026-07-03: an earlier framing ("the dig was the ratchet")
was backwards. Breaking down to the roots — removing presumptions — only
resembles a ratchet. It is not the ratchet.

The ratchet is the upward, constructive climb. It starts from the weakest
evolving persistent structure (the MSS-selected floor) and builds from weak
structure to stronger structure, level by level, installing what each level
forces. Two separate things:

- MSS is the floor-picker — it selects the weakest surviving seed at the
  bottom.
- The ratchet is the upward climb off that floor.

MSS sets where the climb starts; the ratchet is the climb itself. This
reconciles the nonassociativity question: the floor is weakest, so it is
nonassociative/magmoid; the ratchet installs stronger structure (commutativity,
associativity, geometry, operators) going up, where forced. The earlier
reading that called nonassociativity "installed not root-forced" was reading
down the ratchet and mislabelling the start point as installed — the floor is
where you start, and associativity gets installed as you climb off it.

## Owner statement: density matrices are closer to MSS than spinors

Owner correction, 2026-07-04: there is no single canonical order for the
geometry layers. Specifically, density matrices are closer to MSS than
spinors. Admission order is not the same as carrier presentation:

> MSS ladder = quotient floor → ρ installed rung-4 → spinor lift admitted
> ONLY when quotient-erased distinctions are load-bearing.

The doctrine that "spinors are the carrier, density is the readout" answers
what the runtime must keep (the 720-degree structure), not what is admitted
first.

A related correction, same date: bigger circles must come first. Under MSS
admission, structure runs superset to subset — each equality law carves a
smaller circle out of a bigger one. Cayley-Dickson (R→C→H→O) is construction
order, not presumption order; reals as the maximal stack of equal signs sit
far down the ratchet. The same pattern applies to complexity classes
(EXP ⊇ PSPACE ⊇ NP ⊇ P — the bigger class is the least-presumed one).

An external referee (nemotron-super-49b) argued for the same ordering from a
different route: a classical distribution is a density matrix plus a choice
of maximal abelian subalgebra (which fixes the measurement frame), so
classical structure is one extra installed object on top of density matrices,
not the other way round. This is one external argument recorded on the
ledger, not canon — the fleet-draft machinery-counting order (ω before ρ) and
the presumption order remain both on record, per anti-collapse.

## Status ceiling

All of the above is doctrine and provenance history, cross-referenced against
already-simmed and already-drafted material. Nothing here promotes any rung
to canonical. The forced-vs-installed distinction, and the plural
`Min(Surv(C))`, must be preserved in any future write-up.
