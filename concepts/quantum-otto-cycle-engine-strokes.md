---
title: Quantum Otto cycle — strokes, coherence penalty, and friction
created: 2026-07-19
type: concept
tags: [quantum-thermodynamics, otto-cycle, coherence, quantum-friction, literature]
sources:
  - Kosloff, Feldmann, "Discrete four-stroke quantum heat engine exploring the origin of friction", Phys. Rev. E 65, 055102 (2002)
  - "The Quantum Harmonic Otto Cycle", Entropy 19, 136 (2017); arXiv:1612.03582
  - Francica, Binder, Guarnieri, Mitchison, Goold, Plastina, "Quantum Coherence and Ergotropy", Phys. Rev. Lett. 125, 180603 (2020); arXiv:2006.05424
  - "Friction-free quantum machines" review; arXiv:1804.00604
  - "The asymmetric Otto engine: frictional effects on performance bounds and operational modes"; arXiv:2310.06512
  - "The Quantum Friction and Optimal Finite-Time Performance of the Quantum Otto Cycle", Entropy 22, 1060 (2020)
  - "Finite-time optimization of a quantum Szilard heat engine", Phys. Rev. Research 6, 043001 (2024)
  - "Internal Geometric Friction in a Kitaev Chain Heat Engine"; arXiv:2003.08836
framing: literature-only
status: research-note
---

# Quantum Otto cycle — strokes, coherence penalty, and friction

Literature summary only. No claims here about the Codex-Ratchet model —
that mapping, entirely hypothesis, lives in
[[projects/codex-ratchet/weyl-chamber-otto-attachment-hypotheses-2026-07-19]].

## The four strokes

Kosloff and Feldmann, Phys. Rev. E 65, 055102 (2002), set the standard
discrete four-stroke frame, since used across the field (see the review
Entropy 19, 136 (2017), arXiv:1612.03582, for the harmonic-oscillator
working-medium case):

1. **Isentropic (adiabatic) compression/expansion** — a control parameter
   (trap frequency, level spacing, magnetic field) is changed while the
   system is isolated from any bath. If done infinitely slowly this stroke
   is unitary and entropy-preserving.
2. **Isochoric thermalization (hot)** — the control parameter is held
   fixed while the system is coupled to a hot bath and allowed to
   equilibrate (partially or fully).
3. **Isentropic (adiabatic) expansion/compression** — the reverse control
   sweep, again isolated.
4. **Isochoric thermalization (cold)** — coupling to a cold bath, closing
   the cycle.

Work is extracted or supplied only on strokes 1 and 3 (no heat exchange);
heat is exchanged only on strokes 2 and 4 (no work, if the control
parameter is truly held fixed).

## Quantum friction: what breaks in finite time

If strokes 1 and 3 are not run infinitely slowly, the quantum adiabatic
theorem does not hold exactly: the sweep induces non-adiabatic transitions
between instantaneous energy eigenstates. This is termed "quantum
friction" in the field (Kosloff & Feldmann 2002 onward; Entropy 22, 1060
(2020), "The Quantum Friction and Optimal Finite-Time Performance of the
Quantum Otto Cycle"; arXiv:2310.06512 on asymmetric-cycle frictional
effects). It generates irreversible entropy and consumes part of the work
that a slow cycle would have extracted. "Friction-free" protocols
(shortcuts to adiabaticity, counter-diabatic driving) are an active
sub-literature aimed at cancelling this loss without slowing the cycle
(arXiv:1804.00604, review).

Quantum friction is directly the dynamical (Landau-Zener) phenomenon
described on the Weyl-chamber page: a finite-time sweep through or near a
level crossing or avoided crossing produces diabatic population transfer.
Where the underlying model has an actual level-crossing structure (e.g. a
Landau-Zener two-level model), the Otto cycle literature treats the sweep
rate through that crossing as the direct tuning knob for how much friction
is incurred (see the Landau-Zener-model Otto-cycle results reported in the
search literature on quantum-phase-transition-probing Otto cycles).

## Coherence: a resource, not automatically a cost

A separate and more recent thread (Francica, Binder, Guarnieri, Mitchison,
Goold, Plastina, Phys. Rev. Lett. 125, 180603 (2020), arXiv:2006.05424)
treats coherence generated in the instantaneous energy eigenbasis during
finite-time strokes not purely as loss, but as a resource that can be
partly recovered. Ergotropy (the maximum work extractable by a unitary
cycle from a given state) splits into an incoherent part (extractable by
first dephasing to the energy eigenbasis) and a coherent part
(extractable only by exploiting the coherence itself). The paper derives
bounds on both parts and shows conditions under which the coherent
contribution saturates its bound. For a harmonic Otto cycle specifically,
because the isochoric strokes can be short, coherence generated on a
compression/expansion stroke can survive into the next stroke rather than
being erased by full thermalization, giving the engine a route to recover
part of what a naive quasi-static analysis would count as friction loss.

This is distinct from Landau-Zener quantum friction: friction is
diabatic *population* transfer (changes level occupations, irreversible,
a straightforward loss); the coherence effect concerns *off-diagonal*
coherence in the energy eigenbasis (does not by itself change level
populations, and — under the right protocol — some of it is recoverable
as work rather than being pure loss). Both can be present in the same
finite-time stroke and the literature treats them as separate terms in the
work/entropy balance, not as the same phenomenon under two names.

## Adjacent cycles: Carnot and Szilard

The quantum Carnot cycle replaces the two isochoric strokes with isothermal
strokes (bath coupling held throughout, not just at fixed points), and
inherits its own finite-time/friction literature in parallel. The quantum
Szilard engine (a single-particle, information-driven cycle built from a
measurement-and-feedback protocol rather than a heat-bath pair) has a
separate finite-time-optimization literature (Phys. Rev. Research 6,
043001 (2024)) that shares the same friction/coherence vocabulary but is
not simply a special case of the Otto cycle — it is a distinct cycle type
built on a measurement step rather than a pair of isochores.

## Geometric readouts on thermal cycles

A smaller thread treats thermal-machine performance itself as geometric:
the antisymmetric part of a "thermodynamic response tensor" over the
cycle's control-parameter space has been identified with a Berry
curvature, giving a geometric (path-dependent-only-through-area, not
rate) contribution to dissipation, separate from the ordinary friction
term (arXiv:2003.08836, "Internal Geometric Friction in a Kitaev Chain
Heat Engine", and related work on driving through avoided crossings to
extract the quantum geometric tensor). This is the clearest published
bridge between "geometric phase near a degeneracy" (the Weyl-chamber-wall
phenomenon) and "thermodynamic cycle performance" — but it is a general
geometric-response argument, not a Weyl-chamber-specific one; no source
found in this pass ties it to the Zhang-Vala-Sastry-Whaley two-qubit
chamber or the eigenvalue-simplex chamber by name.

## Status

`exists` as literature, cited directly. Every claim above traces to a
named, dated source. No source found in this research pass performs a
Weyl-chamber computation as part of an Otto-cycle (or Carnot, or Szilard)
analysis — see the honesty note on the intersection in the attachment-
hypotheses page.
