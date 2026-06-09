---
title: Geodesic Structure on State Space
created: 2026-04-09
updated: 2026-04-16
type: concept
tags: [geometry, mathematics, quantum, reference]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_fubini_study_geometry.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_bures_geometry.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/engine_graph_driven.py
framing: current
---

# Geodesic Structure on State Space

Geodesics are the shortest paths on a curved manifold. On quantum state space with the Bures or Fubini-Study metric, geodesics encode the optimal interpolation between states — the paths that minimize distinguishability change.

## Core Structures

### Geodesic Equation

∇_γ̇ γ̇ = 0

A curve γ(t) is a geodesic if its acceleration (covariant derivative of its tangent) vanishes. On a flat manifold, geodesics are straight lines. On curved state spaces, they curve.

### Exponential Map

exp_p: T_p M → M

Maps a tangent vector at point p to the point reached by following the geodesic from p in that direction for unit time. The inverse (log map) takes a nearby point and returns the tangent vector pointing toward it.

On CP¹ (qubit pure states), the exponential map from |0⟩ in direction |1⟩ gives:
|ψ(t)⟩ = cos(t)|0⟩ + sin(t)|1⟩

This is the geodesic on the Bloch sphere (a great circle).

### Geodesic Deviation (Jacobi Fields)

Two nearby geodesics with initial separation ξ evolve according to:
D²ξ/dt² + R(γ̇, ξ)γ̇ = 0

where R is the Riemann tensor. This measures "tidal forces" — how curvature causes initially parallel paths to converge or diverge.

## Relevance to This System

### Geodesics as Constraint-Admissible Paths

A geodesic on the state space represents the path of least distinguishability change between two states. Under the constraint cascade:
- Some geodesics survive (stay within the admissible region M(C))
- Some geodesics are killed (cross constraint boundaries)
- The surviving geodesics define the "natural" transport within each shell

### Geodesic Deviation and Family Separation

If two families start near each other on the state space, geodesic deviation tells you whether they converge (same surviving family) or diverge (distinct families). The Riemann tensor's sign determines this.

Positive curvature → families converge → possible merging under cascade
Negative curvature → families diverge → cascade preserves distinction

### Connection to Shell Transport

The exponential map on the Bures manifold gives the optimal transport between density matrices. The system's `transport_allowed` function (in `engine_graph_driven.py`) may be a rough discrete analogue of this, but that mapping should currently be treated as a candidate inference rather than a verified current equivalence.

## Open Questions

- Are the geodesics on the Bures metric between admissible states themselves admissible?
- Does geodesic deviation correlate with the cascade's family-merging behavior?
- Is the exponential map surjective on the admissible region (can every admissible state be reached from a given state by a geodesic)?

## Related Pages

- [[riemannian-curvature]] — curvature that governs geodesic deviation
- [[quantum-geometry-fubini-study]] — Fubini-Study geodesics on pure states
- [[distance-metrics-state-space]] — Bures distance (geodesic distance)
- [[geometry-ingredient-map]] — geometry inventory
- [[probe-doc-result-map]] — mapping to actual sim results

## Sources

- Bengtsson, Życzkowski. "Geometry of Quantum States." Cambridge University Press, 2017.
- Nielsen. "An Introduction to Majorization and Its Applications to Quantum Mechanics." Lecture notes, 2002.
- Uhlmann. "The Transition Probability in the State Space of a *-Algebra." Rep. Math. Phys. 9, 273 (1976).
