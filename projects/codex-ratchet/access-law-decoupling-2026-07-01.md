---
title: Access-Law Decoupling — §7s Sharpened Under a Hostile Probe
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. §7s sharpened not demoted: exact symbolic theorem on 8 pinching stages, dynamical 14/16 on 8 rotation stages. Structural indices only.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01, responding to a second external audit probing §7s. Independently verified here.
---

# Access-Law Decoupling — §7s Under a Hostile Probe

> **SYNC STATUS: not canon.** A second external audit probed the eight-of-sixteen access law
> (§7s) for circularity. §7s mostly survives, with a precise crack. Reproduced independently.

## The circularity concern (legitimate)

In the §7s sim, `eps` sits in BOTH the terrain Hamiltonian AND the measurement drive. So the
"global geometric-phase sign" could have been the meter's chirality, not the stage's.

## Decoupled result: the chirality lives in the terrain

Splitting eps into eps_terr (terrain Hamiltonian) and eps_drive (meter), across 16 stages:
the geometric-phase sign follows the TERRAIN 14/16 and the DRIVE only 2/16. The chirality
genuinely lives in the stage -- the law earning itself against its own hostile probe.

## The crack (a familiar place)

The non-clean stages are all Fe stages (Fe = fixed-sign z-rotation, competes with the
terrain's signed one). Under a fully chirality-neutral meter the law holds 14/16, and the two
failures are t3:Fe and t7:Fe -- the SAME sheet-symmetric projective Si pair that was the
bottleneck in §7p and §7r. The manifold's weakest chirality fails first, exactly where the
fingerprint predicted. The published 16/16 is real only because the loop carries the sheet's
own H0; defensible (the engine's Hamiltonian arguably IS part of the stage) but must be
adopted as the loop's definition explicitly, or the theorem is 14/16.

## The upgrade: two-tier, mirroring §7q's fusion split

The dephasing stages (Ti,Te) negate IDENTICALLY under eps-flip -- |a(+)+a(-)|=0 to machine
precision for all 8 -- an exact conjugation symmetry (dissipators are conjugation-invariant,
the coherent term flips, y->-y negates the swept area). The rotation stages (Fi,Fe) are
dynamical/approximate (deviation up to 0.18). So the access law is:
  - exact symbolic-identity theorem on the 8 pinching stages
  - dynamical-and-approximate on the 8 rotation stages
"structural theorem" is true for half of it in the strongest possible sense.

## Housekeeping (the audit's stale flag)

The second audit flagged that "v2 didn't incorporate the previous audit's edits". That flag
is now superseded: spec v24 already withdrew §7o's linear law, reframed §7q's null and the
8/8 coincidence, and added §7t (the W-vs-V fork earning the native-operator law). This §7s
sharpening is v25.

## Artifacts

`access_law_decoupling.png`, `access_law_decoupling_sim.py`. Spec §7s: `constraint-core-formal-spec-2026-07-01.md`.
Rosetta: `rosetta_layer.json`.
