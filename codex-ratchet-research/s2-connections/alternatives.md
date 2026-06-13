# S2 Connections - Alternatives

Source registry: `system_v6/receipts/round3_discriminator_registry_20260611.md`.
Evidence ceiling: finite alternative-space research, not a sim result.

## Registry Space

The round-3 S2 space is finite and committed-adjacent. Every candidate is
reduced before testing to:

`(F=dA, c1, lifted_holonomy_vector[pi/12,pi/6,pi/4,pi/3,5pi/12], annular_flux_vector, cover_period_pin)`.

Exact tuple equality under the documented S2 convention map is `alias`.
Equality of `c1` alone is `co_survivor`.

## Candidate Families

- `S2.R3.0_committed`: `f=cos(2eta)`, no extra `g_phi` or `g_chi`. This is the
  anchor, not an alternative to kill.
- `S2.R3.1_large_gauge_chi_shift`: same `f`, `g_chi in {1/2,-1/2}`. Classification
  turns on whether the large-gauge/convention shift preserves the pinned lifted
  holonomy tuple, not only `F`.
- `S2.R3.2_same_curvature_shifted_holonomy`: `f=cos(2eta)+c`,
  `c in {1/4,-1/4}`. The derivative and therefore curvature match the committed
  density, but leaf holonomy shifts; this is the canonical same-curvature,
  different-lift stressor.
- `S2.R3.3_endpoint_chern_preserving_bump`:
  `f=cos(2eta)+epsilon*sin(2eta)^2`, `epsilon in {1/10,-1/10}`. Endpoint
  topology is preserved while interior curvature density changes.
- `S2.R3.4_two_leaf_holonomy_match`:
  `f=cos(2eta)+epsilon*cos(2eta)*(cos(2eta)-1/2)`,
  `epsilon in {1/5,-1/5}`. It matches selected leaves but must be compared
  against an expanded holonomy vector and annular flux.
- `S2.R3.5_boundary_conditioning_variant`: finite unions of leaves with a
  canonical disintegration rule. This is heavy because conditioning validity is
  upstream of flux comparison.

## Classification Bounds

The standard classification result bounds only the bundle topology by `c1`.
The registry's alias class is stricter: it requires the canonical tuple. Same
curvature with shifted lifted holonomy is at most a convention neighbor until
the pinned holonomy convention says otherwise. Same endpoint Chern class with
different annular density is a co-survivor candidate, not an alias.
