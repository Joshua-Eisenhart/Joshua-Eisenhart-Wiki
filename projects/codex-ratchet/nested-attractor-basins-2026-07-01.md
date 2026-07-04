---
title: Manifold As Nested Attractor-Basin Hierarchy
created: 2026-07-01
updated: 2026-07-01
type: project-status
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false; formal_admission_allowed=false. Earned: 8 distinct terrain basins (rich fingerprint), attractor/viability kill split coinciding with Axis-0 polarity, operator sub-basins passing a commuting-control kill test. NOT earned: basin-boundary topology, sub-sub-basin depth beyond one level, state-attractor closure (most terrains are equivalence/viability class).
framing: codex-ratchet
sources:
  - concepts/basin-manifold-claim-contract.md
  - concepts/attractor-basins-formal-reference.md
  - concepts/qit-basin-engine-synthesis.md
  - concepts/falsification-sim-designs.md (viability-vs-attractor kill test)
provenance: Claude Science formalization session 2026-07-01; synced for review, NOT admitted as canon.
---

# The Manifold as a Nested Attractor-Basin Hierarchy

> **SYNC STATUS: not canon.** `scratch_diagnostic`, `promotion_allowed=false`.
> Built against the repo's basin-manifold claim contract; three attractor types
> (state / process / equivalence) kept distinct per repo guidance.

## Claim (user)

The 2 engine types, 4 topologies, flux, and 8 terrains are all part of the geometric
constraint manifold. The dual (co-)ratchet of operators + entropy couples to these
like sub attractor basins. The whole model = one attractor basin with sub-basins
and sub-sub-basins.

## What was earned (contract-compliant)

- **State space:** density matrices on the Bloch ball (extensible to 3-qubit carrier).
- **Update rule:** ordered CPTP cycle E = terrain GKSL flow then judging operators.
- **8 top-level terrain basins are distinct** under a rich fingerprint (center + dispersion
  + purity + entropy + z-bias). DOF-no-collapse holds; a coarse centroid-only readout
  collapses 6/8 to the origin (same lesson as the 64-schedule).

## Kill test: viability vs attractor

| Type | Terrains | Endpoint spread | Verdict |
|---|---|---|---|
| Ne, Ni | Vortex, Spiral, Pit, Source | ~0.000-0.001 | **attractor** (converges) |
| Se, Si | Funnel, Cannon, Hill, Citadel | ~0.03-0.09 | **viability** (bounded) |

This attractor/viability split — from an independent dynamical test — **coincides with
the Axis-0 polarity** (Ne/Ni allostatic/+, Se/Si homeostatic/-). Corroboration of that
DOF; NOT a closure of Axis-0's owner-defined dD/dλ readout.

## Sub-basins: the operator/entropy co-ratchet

The 4 judging operators refine each terrain basin into distinct sub-basins:
- Pit (attractor terrain): min sub-basin separation **0.445** (pinned point → clean split).
- Hill (viability terrain): min sub-basin separation **0.005** (bounded class → less to split).

## Killed non-basin explanation (contract req #8)

Noncommuting pair (Te,Fe) order gap = **0.268**; commuting control (Tz,Tz) order gap =
**2e-17**. Structure vanishes when noncommutation is removed → the sub-basin structure
is genuinely N01-driven, not a readout artifact.

## Artifacts (Claude Science session 2026-07-01)

- `nested_attractor_basins.png`, `nested_basin_results.json`, `nested_basin_sim.py`
- Full spec: `constraint-core-formal-spec-2026-07-01.md` §7h.

## Next (gated)

- Basin-boundary topology (smooth vs fractal vs riddled/Wada) — untested.
- Sub-sub-basin depth beyond one level.
- Lock Se/Ne/Si dissipators so terrain flows have source-locked content (Axis-0 blocker) —
  would sharpen the viability terrains' basin content.
