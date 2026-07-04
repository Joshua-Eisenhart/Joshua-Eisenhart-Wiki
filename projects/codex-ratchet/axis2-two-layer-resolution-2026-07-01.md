---
title: Axis-2 is a Two-Layer Object — the W-vs-V Fork Resolved
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. Axis-2 = continuous frame V (connection K=H0) x discrete Z2 involution W (operator map). No spec repair. Structural indices only.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01, running the consistency check the §7t fork demanded.
---

# Axis-2 is a Two-Layer Object

> **SYNC STATUS: not canon.** Resolves the §7t fork (native-operator law = W-covariance, but
> spec's Axis-2 = V=exp(-iH0 u)). Answer: neither is wrong; Axis-2 has two composable layers.

## The fork (from §7t)

The native-operator law is exact covariance under the Hadamard involution W=(sx+sz)/sqrt2, but
the spec's Axis-2 element is the co-rotating frame V=exp(-iH0 u) with connection K=iV†V̇ (§7n).
Either V is wrong, or W is a separate symmetry.

## Four-property test

| property Axis-2 must satisfy | V=exp(-iH0 u) | W=(sx+sz)/sqrt2 |
|---|:---:|:---:|
| gauge-invariant (preserves state invariants) | yes 9e-16 | yes 8e-16 |
| implements direct<->conjugated operator map | NO (Ti->Te 0.67, Fi->Fe 2.15) | yes (Ti->Te 3e-33, Fi->Fe 4e-17) |
| phase-sector (moves eigenvectors not spectrum) | yes | yes 9e-16 |
| carries connection K=iV†V̇ (changes dynamics) | yes K=H0 | NO K=0 |

## Resolution: two layers, composing

- CONTINUOUS layer V=exp(-iH0 u): u-dependent co-rotating frame; connection K=H0 (nonzero);
  changes effective dynamics (§7n role). Cannot implement the x<->z operator swap.
- DISCRETE layer W=(sx+sz)/sqrt2: fixed Z2 involution; V̇=0 so K=0; carries the exact
  operator map Ti<->Te, Fi<->Fe (§7t role). Not a continuous frame.

They compose: W acts on the continuous frame by conjugating its connection,
K -> W K W = H0 - 2σy/√3 (the y-component flips since WσyW=-σy). This IS the §7n clause
"K=iV†V̇ changes the effective dynamics", now realized as the discrete direct/conjugated bit
acting on the continuous frame's connection.

## Verdict

NO spec repair. Axis-2 is refined, not corrected: record it as a two-layer object
(V continuous frame) x (W discrete direct/conjugated bit). The native-operator law is earned
as covariance under the discrete layer; the continuous frame keeps its §7n role intact.

## Artifacts

`axis2_two_layer.png`, `axis2_two_layer_sim.py`. Spec §7u: `constraint-core-formal-spec-2026-07-01.md`.
Rosetta: `rosetta_layer.json`.
