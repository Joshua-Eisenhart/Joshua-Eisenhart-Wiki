---
title: χ₂ Closed — the Open-Path Phase Readout for the Eigenvector Sector
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. χ₂ closed at FRAME level (open-path/gauge/two-sector properties exact; 99.7% frame-read empirical). Terrain-level a2 bit still open. Structural indices only.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01, taking a run at the last open item.
---

# χ₂ Closed — the Bargmann Open-Path Phase Readout

> **SYNC STATUS: not canon.** Closes the last genuinely open item at the current layer: a
> working instrument for the eigenvector-sector (phase) charge χ₂.

## The problem

§7n proved Axis-0's parity (Axis-0 = Axis-1 ⊕ Axis-2, §7m) needs BOTH charges read. χ₁ (the
entropy charge, eigenvalue sector) reads cleanly. χ₂ (the phase charge, eigenvector sector)
had NO working instrument: closed-loop holonomy was proven gauge-invariant and therefore
returns to the identity → phase 0.

## The instrument

χ₂ = Bargmann/Pancharatnam OPEN-PATH geometric phase of a state's top eigenvector against two
fixed references r₀, r₁ (states the gauge does not act on):

    χ₂(ρ) = −arg( <r₀|e><e|r₁><r₁|r₀> ),   e = top eigenvector of ρ

An OPEN path of 3 distinct states has a nonzero relational phase that is STILL gauge-invariant
under per-ket rephasing |ψ> -> e^{iφ}|ψ> — reading the eigenvector sector without the
closed-loop cancellation that killed holonomy.

## Verified (chi2_openpath_readout_sim.py)

- open-path not closed: 3 distinct states -> -1.01 (nonzero); degenerate -> 0.0
- gauge-invariant under rephasing: diff 0.0 exact
- two-sector orthogonality: varying eigenvectors at fixed spectrum moves χ₂ (0 -> 0.64) while
  S ≡ 0.5004; varying spectrum at fixed eigenvector holds χ₂ = 0.6397 while S runs 0.33->0.67
- THE Ξ PARITY: χ₂ distinguishes direct frame V from conjugate V* by 1.22; entropy blind 9e-16

## Robust and non-circular

Over 2000 random probes: entropy cannot see the direct<->conjugated frame bit at all
(max|diff| = 9e-16); χ₂ reads it on 99.7% (mean |Δχ₂| = 1.57). Misses only the measure-zero
set where the eigenvector hits a reference pole (third reference closes it). The frame bit is
read from a GENUINE operation (V vs V*, complex conjugation of the frame element), NOT off a
label — not the circular "read χ₂ off the assignment" an earlier audit flagged.

## Verdict

χ₂ is closed at the FRAME level. The two-sector theorem now has both meters: χ₁ (entropy,
eigenvalue sector) + χ₂ (Bargmann open-path phase, eigenvector sector), together instrumenting
the full Axis-0 parity of §7m. The residual gap is now specifically the TERRAIN-level a2 bit
(§7u: generator-map residuals 1.4-2.0) — a distinct, sharper question.

## Artifacts

`chi2_openpath_readout.png`, `chi2_openpath_readout_sim.py`. Spec §7v:
`constraint-core-formal-spec-2026-07-01.md`. Rosetta: `rosetta_layer.json`.
