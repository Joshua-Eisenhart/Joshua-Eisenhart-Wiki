---
title: Two-Thread Convergence — Non-Unitality Theorem, Symbolic-Identity Grades, and the Terrain-Level Axis-2 Gap
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. §7q upgraded to non-unitality theorem; §7n regraded symbolic_identity; caveats discharged. Structural indices only.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01, incorporating two converging external-thread audits.
---

# Two-Thread Convergence and the Non-Unitality Upgrade

> **SYNC STATUS: not canon.** Two external threads independently reproduced this session's
> results and converged on the same conclusions. This closes their combined queue.

## Cross-instance confirmation of §7u

The second thread independently ran the W-vs-V consistency check and reached the SAME
conclusion as §7u: "two exact theorems carried by two provably distinct group elements — V
carries the degeneracy and the connection, W carries the pair swap — no single element can
carry both. The fork was a false dichotomy: de-conflation, not substitution." That is exactly
the two-layer Axis-2 of §7u, reached from a different starting point. Its key numeric —
||[W, e^{-iH0 t}]|| ~ 1.1-1.3 and conjugated-channel difference 0.6 (vs 3e-16 for V) — is why
W cannot be the frame element without killing §7o's delta=0 degeneracy. Recorded.

## Upgrade 1: §7q surplus is exactly NON-UNITALITY (theorem)

The numerical containment split (0.00-0.12 fused vs 0.67-0.71 source-locked) is now an exact
algebraic statement. All 4 operators are UNITAL: Ti(I)=Te(I)=Fi(I)=Fe(I)=0, so any span is
unital. Source-locked terrains carry D[σ±] with ||L(I)||=√2 != 0 exactly (t0,t2,t4,t6); fused
terrains ||L(I)||=0 (t1,t3,t5,t7). So the source-locked generators provably cannot lie in the
operator algebra, in ANY frame (unitality is basis-independent). The 8/8 fusion bit is exactly
1[||L(I)|| != 0]. This replaces the falsified co-moving-frame test with a one-line identity.

## Upgrade 2: §7n sector-blindness is a SYMBOLIC IDENTITY

Frame conjugation rho -> V†rho V is a unitary similarity, which preserves the spectrum of any
Hermitian operator EXACTLY (spec(V†rho V)=spec(rho) for any unitary V). Entropy functionals
depend only on eigenvalues, so their frame-invariance is algebraic, not the 2e-15 numerical
result previously reported. Regraded symbolic_identity.

## Caveats discharged

- Residual norm convention: all §7t/§7u residuals are FROBENIUS NORMS ||.||_F, not squared;
  Ti->Te=3.4e-33 is an exact Pauli-basis permutation floor. Tagged in-spec.
- GKSL convention pinned in axis0_gauge_breaking_sim.py v3 (L=σz⊗I, evolution time T=1, unitary
  phase t=0.7); a different thread's T/rate gave 0.30->0.06 vs this run's 0.15->0.039 — same
  qualitative saturating decay, reconcilable by convention.

## The sharper open item (replaces the fork)

W-covariance is exact at the OPERATOR level but does NOT extend to the TERRAIN level: neither
W nor V conjugates the direct terrain generators into their conjugated partners (||U L_dir U† -
L_conj|| = 1.4-2.0 for both, all four pairings). So the direct/conjugated a2 bit ON TERRAINS
still rests on the source table alone. That is the actual remaining Axis-2 gap — better-posed
than "which element is the frame." Plus the unchanged χ₂ open-path eigenvector-sector readout.

## Artifacts

`nonunitality_theorem.png`, `nonunitality_theorem_sim.py`. Spec §7q/§7n/§7t/§7u/§7o:
`constraint-core-formal-spec-2026-07-01.md`. Rosetta (audit log): `rosetta_layer.json`.
