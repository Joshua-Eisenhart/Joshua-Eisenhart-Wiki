---
title: The Axis-0 Stall Resolved — Axis-0 = Axis-1 XOR Axis-2
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. Exact structural identity verified against repo operator table (igt-pattern lines 475-478). Candidate resolution of the Axis-0 stall; the Xi bridge is still to be built.
framing: codex-ratchet
sources:
  - concepts/igt-pattern-explicit-math-reference.md (operator table lines 475-478; axis splits)
  - concepts/axis-0-1-2-qit-packet.md (Axis-0 needs bipartite rho_AB; discrete N/S projection)
provenance: Claude Science session 2026-07-01. Synced for review, NOT canon.
---

# The Axis-0 Stall Resolved: Axis-0 = Axis-1 XOR Axis-2

> **SYNC STATUS: not canon.** scratch_diagnostic. Exact, but the Xi bridge is still open.

## The result

After **14** distinct single-cut Axis-0 readouts (entropy production, response dD/dlambda,
trajectory activity, future multiplicity, participation ratio, von Neumann, JK-fuzz bipartite MI,
fuzz tree-entropy, dH_fuzz/dlambda, distinguishability-flow, spinor-720 phase-return,
fiber-alignment, coherent information on a shell-cut, and the strength/alignment control plane) —
**none** realized the {Ne,Ni}|{Se,Si} split. The reason is exact.

Reading the repo operator table (igt-pattern-explicit-math-reference.md lines 475-478):

| Axis | split | Se | Ne | Ni | Si |
|------|-------|----|----|----|----|
| Axis-1 (dynamics) | dissipative {Se,Ni} / unitary {Ne,Si} | 0 | 1 | 0 | 1 |
| Axis-2 (frame)    | direct {Se,Ne} / conjugated {Ni,Si}     | 0 | 0 | 1 | 1 |
| Axis-0 (perceiving) | N/intuition {Ne,Ni} / S/sensing {Se,Si} | 0 | 1 | 1 | 0 |

**Axis-0 = Axis-1 XOR Axis-2**, exactly, for all four families. {Ne,Ni} (intuition) are the terrains
where the dynamics-axis and frame-axis DISAGREE; {Se,Si} (sensing) are where they AGREE.

## Why this resolves the stall

XOR is the textbook not-linearly-separable function. A single scalar functional measures one
direction in terrain space, so it can realize Axis-1 or Axis-2 but never their parity. All 14
readouts therefore HAD to collapse onto Axis-1 (or Axis-2). The target was unreachable by
construction — a theorem about what one readout can see, not a tooling failure.

## Why this matches the doctrine

The repo already states Axis-0 "cannot be evaluated on a single isolated spinor; it needs a bipartite
cut-state rho_AB" (the Xi bridge), and calls it "the single biggest open problem." A bipartite object
is a two-subsystem = two-axis construction — exactly what computing a parity requires. The discrete
Axis-0 projection {Ne,Ni}->N, {Se,Si}->S is then the GROUND-TRUTH target the Xi bridge must reduce to,
not a functional to be guessed. Axis-0 is visible only jointly in Axis-1 and Axis-2, never from either alone — the XOR identity is
the precise structural form of that statement (deterministic algebra; no statistical fit needed).

## Constructive next step

Build Xi as a genuine 2-subsystem readout whose sign equals sign(Axis-1) XOR sign(Axis-2) — e.g. a
history-window pullback (time-averaged I_c over a full 720 trajectory) that couples the dynamical and
frame characters MULTIPLICATIVELY, not additively. Use the discrete N/S lattice as the correctness
target.

## Model recommendation

Record `Axis-0 = Axis-1 XOR Axis-2` in the axis doctrine. Stop searching for Axis-0 in single-cut
dynamics; engineer the bridge to compute the parity.

## Artifacts

`axis0_xor_resolution.png`, `axis0_nature_resolution.json`, `axis0_xor_sim.py`.
Spec S7m: `constraint-core-formal-spec-2026-07-01.md`.
