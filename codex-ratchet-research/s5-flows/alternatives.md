# S5 Flows - Alternatives

Source registry: `system_v6/receipts/round3_discriminator_registry_20260611.md`.
Evidence ceiling: finite alternative-space research, not result evidence.

## Canonicalizer

The registry canonicalizes the family as the sorted eight-row tuple:

`(terrain_id, A_exact, b_exact, validity_class, fixed_point_exact, mirror_class, N01_signature)`.

Exact row equality after the documented L/R mirror/convention map is alias.
Matching only quotient survival or a fixed point is co-survival, not alias.

## Candidate Families

- `S5.R3.0_committed_8`: source-locked eight terrain generators. Control row.
- `S5.R3.1_alpha_mix_rotation_contraction`: finite convex generator mixtures
  `alpha*H + (1-alpha)*D` for `alpha in {1/4,1/2,3/4}` on L/R pairs. Tests the
  combined load of contraction and rotation.
- `S5.R3.2_committed_coeff_epsilon`: exact `epsilon in {1/20,-1/20}`
  perturbations on one load-bearing off-diagonal slot per family. This is the
  nearest coefficient-neighbor row.
- `S5.R3.3_nonunital_weak_shift`: committed `A` plus weak `b_z` shifts when
  validity survives. Tests non-unital fixed-point and quotient behavior.
- `S5.R3.4_pairwise_LR_mirror_preserver`: finite rows preserving part of the
  mirror continuum while perturbing other frames. Tests whether mirror evidence
  is local or full-family.
- `S5.R3.5_basin_preserving_null`: same fixed point for `Se_Funnel_L` with
  altered transient rotation. Designed to survive a basin row and fail a
  time-flow/N01 row if the discriminator has teeth.

## Classification Bounds

Affine-flow classification separates generator equality, finite-time map
equality, fixed-point equality, mirror class, and basin behavior. GKSL validity,
when required, is a generator-level constraint. A quotient-level co-survivor is
not an alias unless the full eight-row tuple agrees.
