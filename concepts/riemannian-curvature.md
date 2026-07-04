---
title: Riemannian Curvature
created: 2026-04-09
updated: 2026-04-16
type: concept
tags: [geometry, mathematics, quantum, reference]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_pure_lego_riemannian_curvature.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_cvc5_riemannian_curvature_constraint.py
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Riemannian Curvature on State Space

Riemannian curvature measures how a manifold deviates from being flat. On the quantum state space, it captures the intrinsic geometry that distinguishes different families of states and constrains admissible transport.

## Core Structures

### Riemann Tensor

R(X,Y)Z = ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_[X,Y] Z

Measures the failure of covariant derivatives to commute. On a flat manifold, R = 0 everywhere. On curved state spaces, R ≠ 0 encodes the topology of the carrier.

### Sectional Curvature

K(X,Y) = ⟨R(X,Y)Y, X⟩ / (|X|²|Y|² - ⟨X,Y⟩²)

The Gaussian curvature of the 2-plane spanned by X and Y. For quantum state spaces:
- **Positive K**: states converge under parallel transport (sphere-like)
- **Negative K**: states diverge (hyperbolic-like)
- **Zero K**: flat directions exist (torus-like)

### Ricci Curvature

Ric(X,Y) = trace of R(·, X)Y

Averaged curvature in all directions. For the Bures metric on density matrices, Ric gives a scalar measure of how distinguishability changes under transport.

### Scalar Curvature

R = trace of Ric

Single number summarizing overall curvature. On CP¹ (qubit pure states), R = 2 (constant positive curvature matching the sphere S²).

## Relevance to This System

### Curvature as Constraint Indicator

Where curvature is high, small parameter changes produce large state changes — the system is "sensitive" to that direction. Where curvature is low, the system is "flat" and transport is cheap.

The constraint cascade may correlate with curvature: regions of high curvature could be where constraints kill families (small parameter windows that admit few states).

### Bures Curvature

The Bures metric induces a Riemannian structure on the space of density matrices. The sectional curvature of this metric has been computed:
- For single-qubit states (Bloch ball), sectional curvature is positive everywhere on the boundary (pure states) and varies in the interior (mixed states)
- A common textbook reading is that the boundary becomes singular in a way that can be described as curvature blow-up relative to nearby mixed states

That is a useful support analogy for the system's result packet, but the page should treat the repo-side curvature match as snapshot-based until a fresh rerun is cited directly.

### Result Evidence

`riemannian_curvature_results.json` exists in sim_results/. See [[probe-doc-result-map]] for status.

## Open Questions

- Does the Riemann tensor on the Bures manifold have nonzero components that correlate with L4/L6 kill points?
- Is scalar curvature a monotone under the constraint cascade (decreasing as constraints add)?
- Does geodesic deviation (Jacobi fields) predict which families survive coupling?

## Related Pages

- [[quantum-geometry-fubini-study]] — Fubini-Study metric on pure states
- [[distance-metrics-state-space]] — Bures distance and fidelity
- [[quantum-fisher-information-geometry]] — QFI as curvature component
- [[berry-phase-and-holonomy]] — connection and holonomy on curved bundles
- [[geometry-ingredient-map]] — full geometry ingredient inventory
- [[probe-doc-result-map]] — mapping to actual sim results
- [[hopf-fibration-mathematics]] — the carrier geometry

## Sources

- Petz. "Monotone Metrics on Matrix Spaces." Linear Algebra and Its Applications 244 (1996).
- Braunstein, Caves. "Statistical Distance and the Geometry of Quantum States." Phys. Rev. Lett. 72, 3439 (1994).
- Bengtsson, Życzkowski. "Geometry of Quantum States." Cambridge University Press, 2nd ed., 2017.
