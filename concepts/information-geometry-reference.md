---
title: Information Geometry Reference
created: 2026-04-07
updated: 2026-05-21
type: concept
tags: [reference, geometry, validation, research]
sources:
  - raw/articles/new-docs/references/INFORMATION_GEOMETRY_REFERENCE.md
  - raw/articles/new-docs/10_cross_domain_equivalence_map.md
  - raw/articles/new-docs/05_research_index.md
  - raw/articles/legacy-books/the-dark-empress-a-practical-guide-to-universal-dominion-v6-1-2.md
  - https://arxiv.org/abs/1810.05583v5
  - https://arxiv.org/abs/1210.5071v1
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Information Geometry Reference

## Overview
This reference covers the mathematics of statistical manifolds, Fisher-Rao geometry, alpha-connections, divergence functions, and their quantum extensions.

Authority boundary: this page supplies standard information-geometry background and source analogies. It does not by itself admit a repo carrier, metric, or geometry lane; current repo admission still requires explicit result receipts and validator/status surfaces.

## Main points
- A statistical manifold is a triple (M, g, C): manifold M with Riemannian metric tensor g and totally symmetric cubic tensor C (Amari-Chentsov tensor). "Nearness" is NOT Euclidean in parameter space — geometry tracks distinguishability, not parameter distance.
- The Fisher-Rao metric measures LOCAL DISTINGUISHABILITY of nearby distributions — how much information one observation carries about which distribution generated it. It is the Hessian of KL divergence at zero separation.
- Čencov's Uniqueness Theorem (1982): the Fisher-Rao metric is, up to a positive scalar, the UNIQUE Riemannian metric on statistical models invariant under sufficient statistics. The geometry of distinguishability is categorically forced, not arbitrary.
- Amari's alpha-connections: one-parameter family of torsion-free affine connections, with α=0 giving Levi-Civita, α=1 giving e-connection (flat for exponential families), α=-1 giving m-connection (flat for mixture families). Duality: ∇^(α) and ∇^(-α) are conjugate.
- Projection theorems: inference as geometric projection. Maximum likelihood = m-projection of empirical distribution onto model. Maximum entropy = e-projection onto moment constraint submanifold. Variational inference = m-projection onto tractable family. EM algorithm = alternating e- and m-projections.
- In dually flat manifolds with Bregman divergence, the Pythagorean theorem holds as EXACT equality, not just inequality.
- Quantum information geometry: unlike classical (Čencov: unique metric up to scale), quantum admits INFINITELY MANY monotone metrics (Petz 1996). Bures/SLD is minimal in the usual monotone-metric ordering; Kubo-Mori/BKM is an important relative-entropy and thermal metric, not a generic largest metric unless a specific convention is being cited. The non-uniqueness is a fundamental structural difference between classical and quantum.
- Natural gradient (Amari, 1998): steepest descent on the Riemannian manifold, not Euclidean parameter space. Reparameterization-invariant.
- Thermodynamic length: optimal protocols are GEODESICS of the thermodynamic metric. Many thermodynamic uncertainty relation derivations can be framed through Cramér-Rao/Fisher-information bounds, with entropy production supplying a constraint; do not read this as a global identity between Fisher information and total entropy production.

## Why it matters
This reference grounds the wiki's geometry layer in formal information geometry rather than decorative metric language. The Fisher-Rao metric is the clean classical reference model for distinguishability geometry; whether it is the system's operative geometry in a given lane depends on the carrier and receipts. See [[quantum-fisher-information-geometry]] for the quantum extension.

## Fit for this wiki
Best fit:
- geometry on the same carrier rather than a separate abstract space
- metric language that tracks distinguishability, not just parameter distance
- a clean bridge from classical statistical manifolds to the quantum state-space pages

Mismatch:
- classical uniqueness results do not automatically transfer to the quantum case
- information geometry is about admissible parameterization and distinguishability, not the whole operator algebra
- the page is a reference support, not a replacement for the system's own carrier-specific math

## Legacy Perspective (Dark Empress)

From Chapter 12: The Dark Empress treats time as a physical entity — "Time could be an emergent property of entropy, that itself is the growth of nothingness into something, where one event influences the next event." Time = replication of space-time growing: "Time could be just the replication of space-time growing, from an actual definable structure."

Time = expansion of entangled space: "Time itself is a kind of 'particle' that is not matter. It is better described as a pattern, a replicating system, operating on the tiniest scales of reality." Time can't stop: "Nothing can block time itself." The expansion of the universe "is a product of time, and time itself is this very expansion of space in the direction it moves."

This is a source-genealogy connection, not a proof transfer: the Fisher-Rao metric tracks how distinguishability changes, while the Dark Empress claims that change is time itself. See [[entanglement-theory]] for the entanglement foundation and [[entropy-sweep-protocol]] for entropy as quantum gravity.


- Amari (2016) *Information Geometry and Its Applications*, Springer.
- Sivak & Crooks (2012) *Thermodynamic Metrics and Optimal Paths*, Phys. Rev. Lett. 108.
- Amari (1998) *Natural gradient works efficiently in learning*, Neural Computation 10.

## 2026-04-11 arXiv source additions

### 1810.05583v5 — Thermodynamic length in open quantum systems
- Gives a metric on open-system Gibbs-state space where minimally dissipative protocols follow geodesics.
- Best fit when the wiki needs a direct bridge from information geometry to open-system thermodynamic control rather than a purely classical Fisher-Rao story.
- Best fit pages: [[information-geometry-reference]], [[distance-metrics-state-space]], [[stochastic-thermodynamics-reference]].

### 1210.5071v1 — Stochastic Thermodynamics, Reversible Dynamical Systems and Information Theory
- Connects stochastic thermodynamics to reversible dynamical systems and information-theoretic quantities.
- Useful because it keeps the geometry lane tied to trajectory-level bookkeeping rather than abstract manifold language only.
- Best fit pages: [[information-geometry-reference]], [[stochastic-thermodynamics-reference]], [[research-support-bibliography]].

## Related pages
- [[constraint-on-distinguishability]]
- [[geometry-families-on-same-carrier]]
- [[mass-equivalence-engine]]
- [[system-architecture-reference]]
- [[research-inventory-and-foundations]]
- [[distinguishability-formal-reference]]
- [[stochastic-thermodynamics-reference]]
- [[quantum-fisher-information-geometry]]
- [[quantum-information-measures]]
- [[entanglement-theory]]
- [[entropy-sweep-protocol]]
- [[current-research-overlays]]
- [[wiki-driven-arxiv-search-queue]]
