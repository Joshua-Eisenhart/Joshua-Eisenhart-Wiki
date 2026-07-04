---
title: Quantum Geometry Fubini Study
created: 2026-04-07
updated: 2026-04-10
type: concept
tags: [reference, geometry, research, architecture]
sources:
  - raw/articles/new-docs/new content/quantum_geometry_fubini_study.md
  - raw/articles/new-docs/new content/hopf_fibration_mathematics.md
  - raw/articles/new-docs/references/FIBER_BUNDLES_AND_SPIN_GEOMETRY_REFERENCE.md
  - raw/articles/system-v5-reference-docs/Older Legacy/The Dark Empress-A Practical Guide to Universal Dominion V6.1 copy.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Quantum Geometry Fubini Study

## Definition
This page tracks the pure-state geometry of projective Hilbert space and the way that geometry extends to mixed states through the Bures metric.
It is the bridge page for seeing quantum states as points on a curved manifold rather than as opaque vectors.
The page is not about entropy first; it is about distinguishability geometry first.

## Core structures
- Projective Hilbert space CP^{d-1} is the natural arena for pure-state geometry.
- The Fubini-Study metric is the canonical geodesic metric on that arena.
- The quantum geometric tensor splits into metric and curvature pieces.
- The Berry connection and Berry curvature are gauge data on the same bundle.
- The Bures metric extends the geometry to density operators.
- The Petz family classifies monotone metrics compatible with CPTP maps.

## Pure-state geometry
For normalized states |psi> and |phi>, the Fubini-Study distance is d_FS(|psi>,|phi>) = arccos(|<psi|phi>|).
On a qubit, the coordinate expression reduces to one quarter of the round S^2 metric.
That factor of 1/4 is not decoration; it marks the projective quotient from vectors to rays.
Geodesics are great circles in the induced Bloch-sphere picture.
The pure-state boundary is therefore curved, finite, and operationally structured.

## Quantum geometric tensor
The tensor Q_{mu nu} = <d_mu psi|(1-|psi><psi|)|d_nu psi> is the cleanest local object in the story.
Its symmetric real part is the metric.
Its antisymmetric imaginary part is the Berry curvature.
This split matters for the system because metric data and holonomy data are not interchangeable.
[[berry-phase-and-holonomy]] uses the same bundle language to isolate the gauge piece.

## Bures extension to mixed states
The Bures metric extends pure-state geometry to density matrices.
It is the mixed-state analogue that stays contractive under physical evolution.
For qubits, the radial coordinate and angular coordinates separate cleanly.
Pure states sit at the boundary; mixed states occupy the interior.
That boundary behavior is why this page matters for [[distance-metrics-state-space]] and [[quantum-fisher-information-geometry]].

## Relevance to this system
The system uses curved distinguishability geometry when a flat summary would hide the structure.
That makes this page relevant to [[constraint-on-distinguishability-formal-reference]] and [[formal-constraints-and-geometry]].
In this wiki, the geometry is not generic background; it is the carrier on which probe-relative distinctions live.
The Fubini-Study boundary also links to the state-space pictures in [[density-matrix-mathematics]].
The Hopf quotient viewpoint is useful because the system repeatedly uses S^3-to-S^2 collapse as a carrier story.

## Key results
1. Pure-state distance is geometric, not merely algebraic.
2. Berry curvature is the antisymmetric companion to the metric part of the QGT.
3. Bures geometry is the mixed-state continuation of the same state-space story.
4. The Petz family shows monotone metrics are not unique, but they are still constrained.
5. Speed limits are geometric statements about how fast state-space distance can be traversed.

## Speed limits and operational meaning
The Mandelstam-Tamm and Margolus-Levitin bounds are geometric inequalities on evolution time.
They say the metric structure constrains how fast a state can move.
That makes the geometry operational, not decorative.
The same logic is reused in [[quantum-fisher-information-geometry]] where local distinguishability becomes a resource.

## Why the Berry piece matters
The curvature term carries holonomy.
Holonomy is what survives when the system returns to a loop but not to a trivial phase.
That is why [[fiber-bundles-and-spin-geometry]] and [[hopf-fibration-mathematics]] are linked here.
If the metric is the path length, the curvature is the loop memory.

## Open questions
- Which geometric quantities are load-bearing for Axis 0, and which are only supportive?
- Does the system need the full Petz family, or only the Bures/FS corner?
- How much of the live engine behavior is explained by projective geometry before any entropy talk begins?
- Can the same carrier geometry support both bridge candidates and topological reruns without collapsing distinctions?

## Related pages
- [[quantum-fisher-information-geometry]]
- [[distance-metrics-state-space]]
- [[berry-phase-and-holonomy]]
- [[fiber-bundles-and-spin-geometry]]
- [[hopf-fibration-mathematics]]
- [[density-matrix-mathematics]]
- [[distinguishability-formal-reference]]
- [[constraint-on-distinguishability-formal-reference]]
- [[formal-constraints-and-geometry]]
- [[current-research-overlays]]

## Sources
- The page synthesizes the standard Fubini-Study, Berry, Bures, and Petz results from the quantum geometry literature.
- It is written from domain knowledge rather than from an ingested raw file.
