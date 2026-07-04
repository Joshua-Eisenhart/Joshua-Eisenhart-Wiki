---
title: Attractor Basins Formal Reference
created: 2026-04-07
updated: 2026-05-21
type: summary
framing: dated_reference_snapshot
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/references/ATTRACTOR_BASINS_FORMAL_REFERENCE.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Attractor Basins Formal Reference

## Overview
Reference doc covering attractor definitions, basin types, multistability, stochastic transitions, evolutionary applications, Kauffman, Waddington, and Hopfield networks. The actual mathematics and science, not the system's application.

## Formal Definitions

Dynamical system: continuous (dx/dt = f(x)) or discrete (x_{n+1} = f(x_n)). Attractor (Milnor, 1985): closed set A invariant under dynamics, with basin of attraction of positive Lebesgue measure, and no proper closed subset satisfies both conditions. Basin of attraction B(A): all initial conditions x_0 such that forward orbit converges to A as t → ∞. The state space partitions into basins (plus measure-zero boundaries).


## QIT-Aligned Translation For This Repo
This repo does not start from infinite phase space or point-particle pictures. The aligned translation is finite and operator-first: a basin is a subset of finite-dimensional density states together with admissible ordered channels or instruments such that nearby trajectories repeatedly compress back toward the same persistent regime.

The useful three-way split is:
- State attractor: a family of density matrices that trajectories approach.
- Process attractor: a stable loop of channels, instruments, or update-order patterns.
- Equivalence attractor: not one exact state, but a probe-equivalence class with stable distinguishability structure.

A compact repo-grade sketch is: choose an ordered cycle `E = Phi_n o ... o Phi_1`. A basin `B` around an attractor class `A` is present when repeated application of `E` sends states in or near `B` toward `A`, bounded perturbations stay recoverable, key observational signatures remain approximately stable, and changing the order can change the basin itself.

For current repo evidence, safer parent terms are operational equivalence class, recurrence behavior, metastable class, and stability region. Reserve full basin-of-attraction language for stronger dynamical proofs.

## Types of Attractors

Fixed point: single equilibrium where f(x*) = 0. Limit cycle: closed periodic orbit (Van der Pol oscillator). Torus attractor: quasiperiodic motion on invariant torus. Strange/chaotic attractor: fractal geometry, positive Lyapunov exponent, bounded. Examples: Lorenz attractor (fractal dimension ~2.06), Rössler, Hénon. Strange attractors have basins but fractal internal structure — nearby trajectories diverge exponentially.

## Basin Boundaries

Smooth boundaries contain unstable invariant sets. Fractal boundaries (McDonald, Grebogi, Ott, Yorke, 1985): arbitrarily small perturbations near the boundary can switch which attractor is reached. Riddled basins (Alexander et al., 1992): every open set intersecting the basin also intersects another basin — no finite-precision measurement can reliably predict which attractor. Wada basins: every boundary point is on the boundary of ALL basins simultaneously.

## Multistability

Multiple coexisting attractors. Relative basin sizes determine probability of reaching each attractor from random initial conditions. Basin volume changes with parameters (basin erosion). At bifurcation points, basins appear, disappear, or merge.

## Randomness and Attractors

Stochastic dynamical systems: dx = f(x)dt + σ·dW. Deterministic skeleton has basins; noise allows transitions. Freidlin-Wentzell theory (1984): transition probability from basin A to B scales as exp(-V_AB / σ²), where V_AB is the quasipotential barrier. Kramers' theory: residence time in each basin is exponentially distributed. Noise-induced transitions: system spends most time near attractors but hops between them. Random attractors (Arnold, 1998): compact random sets invariant under the stochastic flow.

## Attractor Basins in Evolutionary Biology

Fitness landscapes (Wright, 1932): peaks are fitness maxima, basins are genotypes driven to same peak. High-D subtlety: saddle points vastly outnumber local maxima. NK landscapes (Kauffman, 1989): K=0 → single peak; K=N-1 → exponentially many local optima. Mutation rate as noise temperature: low = trapped in nearest basin, high = error catastrophe, intermediate = explores neighboring basins. Neutral networks (Wagner): populations drift along neutral networks to arrive near different fitness basins without crossing valleys.

## Kauffman: Self-Organization and Order for Free

Random Boolean networks spontaneously exhibit ordered behavior at low connectivity. K=2: number of attractors ∝ √N. Cell types as attractors: genome defines network, cell types are different attractor basins in gene expression space. "Edge of chaos" hypothesis: biological systems sit near critical K ≈ 2. "Order for free": selection does not create all biological order — some emerges spontaneously from network topology.

## Waddington's Epigenetic Landscape (1957)

Ball rolling down branching valleys represents cell differentiation. Each valley = developmental trajectory. Modern work (Huang, 2009) connected this to gene regulatory network dynamics, showing cell types genuinely correspond to attractor states. The metaphor was vindicated by the mathematics.

## Hopfield Networks (1982)

Recurrent neural networks with symmetric weights have energy function decreasing along trajectories. Stored memories = local energy minima. Basin of each minimum = input patterns "corrected" to that memory. Storage capacity ≈ 0.14N. Spurious attractors (mixture states) reduce capacity.

## Critiques and Limitations

Non-autonomous systems: if f(x,t) depends on time, no fixed basins. High dimensionality: almost all critical points are saddle points, not local minima. Deterministic attractors vs stochastic accumulation: conflating these is a common error — deterministic attractors return after perturbation, stochastic accumulation might not. Metastability: local minima have finite lifetimes; whether to call them "attractors" depends on timescale.


## Dated Repo Examples And Limits
These April/system_v4 examples support three different basin-adjacent claims in the dated support snapshot. Use current `system_v5` receipts and spec mirrors for live repo truth.

- `sim_viability_vs_attractor.py` gives an artifact-side classified canonical separation between viability-preserving evolution and attractor-style collapse on one bounded carrier.
- `sim_axis0_attractor_basin_boundary.py` gives process-specific basin-boundary evidence and shows that boundary behavior depends on trajectory structure rather than generic random-state averaging.
- `sim_qit_attractor_basin_recovery.py` is the clean QIT-native row in this dated April/system_v4 support snapshot: bounded perturbations of nearby density states return under one ordered noncommuting schedule to the same operational equivalence class, the swapped order is weaker, and a commuting control loses the order effect.

The limit is just as important: live repo evidence does not justify a universal attractor ontology. Viability remains the broader survival primitive, and basin talk has to stay finite, probe-bounded, and fail-closed.

## 2026-04-10 arXiv source additions

### 1907.08101v2 — What attracts to attractors?
- Asks what kinds of dynamical structure actually make attraction robust.
- Useful for tightening the difference between attractor language and generic decay-to-something language.
- Best fit pages: [[attractor-basins-formal-reference]], [[viability-theory-reference]], [[distance-metrics-state-space]].

### 2409.01079v1 — Attractor Basins in Concurrent Systems
- Brings basin language into concurrent-system long-run behavior.
- Useful as a bridge from dynamical basins to concurrency / trace-theory routing.
- Best fit pages: [[attractor-basins-formal-reference]], [[concurrency-and-trace-theory-reference]], [[formal-methods-and-witness-discipline]].

## How it connects
See [[qit-vocabulary-discipline-reference]] for term discipline, [[distinguishability-formal-reference]] for the equivalence-class backbone, [[distance-metrics-state-space]] for the recovery metrics, [[cptp-maps-and-channels]] for the channel dynamics, [[viability-theory-reference]] for the complementary "can it stay?" framing, and [[evolutionary-epistemology-reference]] for neutral networks and basin-hopping.


- Strogatz (2015) *Nonlinear Dynamics and Chaos*, Westview Press.
## Related pages
- [[constraint-surface-and-process]]
- [[viability-theory-reference]]
- [[evolutionary-epistemology-reference]]
- [[falsification-sim-designs]]
