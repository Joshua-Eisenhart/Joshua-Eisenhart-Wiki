---
title: Audit Response — §7o Downgrade, §7q/§7r Corrections, and the Earned W-Covariance Law
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. Ratchet kill-test: one claim withdrawn, two reframed, one new earned theorem. Structural indices only.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01, responding to an external thread's audit of constraint_core_selfcontained.zip. Independently verified here.
---

# Audit Response — Kill-Test of the Bundle

> **SYNC STATUS: not canon.** An external thread audited the self-contained bundle and found
> one downgrade, one inference inversion, and one new positive result. All three were
> reproduced independently here. This is the ratchet working: exploration + kill-tests, with
> corrections logged openly rather than hidden.

## 1. §7o "gauge-breaking law" — WITHDRAWN (downgrade)

The claim was `a2-physicality = k*delta, k=0.0787, R^2=0.999997` (a linear law). It does not
survive. The dissipation entered the sim as a SINGLE KRAUS STEP `K0=sqrt(1-delta/2)I,
K1=sqrt(delta/2)Z`, which maps coherence `rho01 -> (1-delta)rho01` — affine in delta BY
CONSTRUCTION. Verified: `split/delta` is constant to `5e-17` all the way to `delta=2.0`, and
the fitted `k` equals the closed form exactly. R^2=1 was an algebraic identity of the
parametrization, not a discovered law.

Rebuilt with a GENUINE GKSL semigroup: `split/delta` falls from `0.15` (delta=0.05) to
`0.039` (delta=2.0) — an ordinary saturating first-order response, no linear law.

WHAT SURVIVES (both exact): (1) the gauge degeneracy at delta=0 — the two unitary objects are
provably the IDENTICAL channel (~3e-16), so the parity is not a single-channel observable
there; (2) the qualitative co-ratchet link — the frame bit is readable only once dissipation
(the entropy sector) is switched on. Sim: `axis0_gauge_breaking_sim.py` v3.

## 2. §7q "the null failure is the point" — REFRAMED (inference inversion)

The four lab-frame metrics that fail to prefer the native operator pair are an HONEST NULL.
It was reported as evidence FOR fusion; the null is equally consistent with "the native
pairing is arbitrary at terrain level". A null cannot adjudicate. The fusion claim is instead
settled by the containment-residual split and — decisively — by the W-covariance theorem (§7t).

Also: the "8/8 coincidence across §7o/§7p/§7q" is three probes reading the SAME bit (Axis-1,
dissipative/unitary), so it is internal consistency, not threefold convergence. Reframed in
§7r/§7s.

## 3. NEW EARNED THEOREM — the native-operator law is exact W-covariance (§7t)

The Hadamard involution `W=(sx+sz)/sqrt2` maps the direct operator pair to the conjugated
pair EXACTLY as channels: `W.Ti.W = Te` (3.4e-33), `W.Fi.W = Fe` (4.5e-17), because
`W sz W = sx` and `W sx W = sz`. So the operator table's "conjugated = x<->z image of direct"
IS frame covariance under W. The native-operator law is promoted from a rosetta LABELLING to
an earned THEOREM.

THE FORK, SETTLED — and a spec correction. The spec's Axis-2 element `V=exp(-iH0 u)` does NOT
implement the swap: a rotation about the H0 axis (1,1,1)/sqrt3 can send sz->sx (120-deg cyclic
x->y->z->x) but then sends sx->sy, mapping Fi to a Y-rotation, NOT Fe. Only the involution W
(rotation by pi about the x-z diagonal) swaps z<->x for BOTH pairs at once. => the Axis-2 frame
element that realizes direct<->conjugated is the Hadamard involution W, not the H0-axis
rotation currently written as V_s(u). Flagged for repair. Sim: `audit_response_w_covariance_sim.py`.

## Artifacts

`audit_response_w_covariance.png`, `audit_response_w_covariance_sim.py`,
`axis0_gauge_breaking_sim.py` (v3, corrected). Spec §7o/§7q/§7r/§7t: `constraint-core-formal-spec-2026-07-01.md`.
Rosetta (with audit log): `rosetta_layer.json`.
