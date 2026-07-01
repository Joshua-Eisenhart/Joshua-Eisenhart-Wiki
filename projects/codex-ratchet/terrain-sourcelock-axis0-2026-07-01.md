---
title: Terrain Source-Locking And The Axis-0 Orthogonality Diagnosis
created: 2026-07-01
updated: 2026-07-01
type: project-status
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false; formal_admission_allowed=false. Earned: source-locked GKSL content for all 8 terrains (fixed points matched to scratch maps); first-principles proof that Axis-0's Ne/Ni|Se/Si grouping is orthogonal to 5 dynamical functionals. NOT earned: a working Axis-0 readout (now open for a principled reason -- needs the Omega_r/JK spine, not terrain-local dynamics).
framing: codex-ratchet
sources:
  - concepts/igt-pattern-explicit-math-reference.md (section 12: scratch Bloch maps)
  - projects/codex-ratchet/qit-axes-terrain-operator-fold-2026-06-09.md (D_-/D_+/D_P admitted needs)
  - concepts/axis0-physics-source-teeth-map.md (Axis-0 late-object spine)
provenance: Claude Science formalization session 2026-07-01; synced for review, NOT admitted as canon.
---

# Terrain Source-Locking and the Axis-0 Orthogonality Diagnosis

> **SYNC STATUS: not canon.** `scratch_diagnostic`, `promotion_allowed=false`.

## The blocker (now closed)

Across prior work, only Ni's dissipator (σ∓) was source-locked; Se/Ne/Si used symbolic
families (D[L_k], D[M_k], P_j) an agent had to choose -- which manufactures canon.

## Source-locking (achieved)

Using the repo's scratch Bloch maps (igt-pattern-explicit-math-reference.md §12), each
terrain's fixed point pins its GKSL content without invention:

- **Se (Funnel/Cannon)**: scratch `(√.78x,√.78y,.78z+.22·.86)` = generalized amplitude
  damping toward z*≈+.86 / −.86, realized as `γ₊D[σ₊]+γ₋D[σ₋]` with z*=(γ₊−γ₋)/(γ₊+γ₋).
  NOT the pure D[σ_z] dephasing used earlier.
- **Ni (Pit/Source)**: D[σ₋]→z*=−1 (Pit), D[σ₊]→z*=+1 (Source). (Already locked.)
- **Ne (Vortex/Spiral)**: Hamiltonian-dominant + weak isotropic depolarizing → center.
- **Si (Hill/Citadel)**: projective invariant-subspace preservation.

Settled fixed points (GKSL, CPTP by construction) track the scratch targets:
Funnel +0.78 (target +.86), Pit −0.90 (−.92), Cannon −0.77 (−.86), Source +0.91 (+.92).
Offsets = competing −iε[H,ρ] tilt (physical).

## Axis-0 is orthogonal to every single-trajectory functional

Five principled Axis-0 readouts tested vs target split Ne/Ni(+) | Se/Si(−):

| Functional | Grouping | Tracks |
|---|---|---|
| entropy production ΔS | {Se,Ni}− {Ne,Si}+ | **Axis-1** |
| response derivative dD/dλ | {Se,Ni} high {Ne,Si} low | **Axis-1** |
| trajectory activity (arc length) | Ne,Ni,Se + / Si − (3/4) | mixed |
| future-option multiplicity | {Se,Ni} many {Ne,Si} few | **Axis-1** |
| participation ratio | all + | none |

**None realizes Ne/Ni | Se/Si.** The three DOF partitions are mutually orthogonal:
- Axis-0 (perceiving): active {Ne,Ni} | conservative {Se,Si}
- Axis-1 (dynamics): dissipative {Se,Ni} | unitary {Ne,Si}
- Axis-2 (frame): direct {Se,Ne} | conjugated {Ni,Si}

Any single-trajectory scalar tracks the dynamical contrast (Axis-1), which cuts across
Axis-0 -> collapse is forced. This is why models stall on Axis-0. Per the teeth map,
Axis-0 is a LATE object on the spine Ω_r/JK → branch-kill → C_G → Ξ → ρ_AB → Φ0,
NOT terrain-local. Realizing it needs that spine (ring-checkerboard / many-futures layer),
not a better one-shot functional.

## Artifacts (Claude Science session 2026-07-01)

- `axis0_sourcelock_diagnosis.png`, `axis0_sourcelock_diagnosis.json`, `terrain_sourcelock_axis0_sim.py`
- Full spec: `constraint-core-formal-spec-2026-07-01.md` §7i.

## Next (gated)

- Build the Ω_r/JK many-futures layer (ring-checkerboard model) as the actual Axis-0 seat.
- This is the principled path now that terrain-local readouts are ruled out from first principles.
