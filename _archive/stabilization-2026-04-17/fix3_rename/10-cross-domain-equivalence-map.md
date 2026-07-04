---
title: Cross Domain Equivalence Map
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: current
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/10_cross_domain_equivalence_map.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Cross-Domain Equivalence Map

## Overview
Connects the current research stack to actual domains: quantum information processing, compression/spectral math, information geometry, ML/AI, computer science, physics, and evolutionary models. Evidence-backed but still a working map.

## The Recurring Pattern

Classical distribution/feature vector to density operator/channel/reduced state. Scalar summary to spectral/information-geometric functional. Geometry on samples to geometry on state space. Evolution rule to CPTP map, unitary, Lindbladian, or constrained update.

## Domain Mappings

**Entropy families:** von Neumann, Rényi, Tsallis, min/max, relative entropy, conditional entropy, mutual information, coherent information — all become well-defined on density operators. Important boundary: some classical entropies are basis-dependent if naively ported.

**QIP math:** State preparation, unitary channels, CPTP maps, partial trace, POVMs, entanglement witnesses, coherent information, fidelity/Bures/trace distance — already native to density-matrix language.

**Compression:** SVD, PCA/QPCA, Schmidt decomposition, low-rank approximation, spectral truncation, principal subspace projection — all the same operator story in different clothing.

**Geometry:** Trace distance, fidelity/Bures, Fubini-Study, QFI, QGT, Berry phase/holonomy — part of admissible structure on state space. L0 runs showed trace distance, Bures, and Fubini-Study survive; HS-alone too flat; real-only kills Berry.

**Evolutionary models:** State = population distribution. Probe = selection pressure. Geometry = admissible transition manifold. Entropy = diversity/uncertainty. Not literally quantum biology — structural analogy under constrained state evolution.

## The Mass-Equivalence Idea

Many systems can be reframed as: state carrier + probe family + constraint manifold + admissible geometry + information functional + evolution rule. This gives a common engine for comparing physics, QIT, compression, learning dynamics, and evolutionary selection. The equivalence is structural under the right probes, not exact identity.

## Most Likely Fundamental Primitives

Density matrices/operators, admissible probes, partial trace/channel structure, noncommuting operator algebra, curved information geometry. Entropy is important but not first.

## Where Ideas Show Up
Quantum computing: state tracking, channel composition, error correction, fidelity/Bures comparisons, entanglement witnesses, QFI/QGT for parameter estimation. Physics: statistical mechanics, open quantum systems, many-body correlations, geometric phase, information geometry for phase transitions. CS/algorithms: compression, spectral methods, operational equivalence, channel capacity, distinguishability under finite probes. AI/ML: covariance/representation learning, manifold methods, entropy regularization, spectral compression. Evolutionary models: state=population, probe=selection pressure, geometry=transition manifold, entropy=diversity. (from 10_cross_domain_equivalence_map.md)

## How it connects
This map is the practical version of [[mass-equivalence-engine]]. See [[mass-equivalence-engine]] for the deeper structural classes and [[constraint-on-distinguishability]] for the foundation.

## Open questions
- Whether the structural correspondence is exact or approximate at higher layers.
- Whether evolutionary models can be lifted to genuine quantum-channel dynamics or only to classical constrained-state evolution.
