---
title: Quantum Fisher Information Geometry
created: 2026-04-07
updated: 2026-04-10
type: concept
tags: [reference, geometry, validation, research]
sources:
  - raw/articles/new-docs/new content/quantum_fisher_information_geometry.md
  - raw/articles/new-docs/references/INFORMATION_GEOMETRY_REFERENCE.md
  - raw/articles/new-docs/new content/quantum_geometry_fubini_study.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Quantum Fisher Information Geometry

## Definition
Quantum Fisher information geometry studies how sensitively a density operator changes with respect to a parameter and how that sensitivity induces a metric on state space.
It is the precision-theoretic side of the same geometry that appears as Fubini-Study and Bures structure.
In this wiki, QFI is a distinguishability object, not a generic entropy summary.

## Core structures
- Classical Fisher information on probability manifolds.
- Quantum Fisher information on density-operator families.
- Symmetric logarithmic derivative as the local generator of the metric.
- Bures distance as the Riemannian continuation of the same structure.
- Wigner-Yanase skew information as a related monotone quantity.
- Multi-parameter quantum Cramer-Rao bounds and commutation obstructions.

## Classical baseline
The Fisher-Rao metric is the statistical precursor.
The Cramer-Rao inequality says covariance cannot beat the inverse information matrix.
Chentsov uniqueness is important because it says monotone metrics are not arbitrary.
That same logic is reused later when the system asks which geometry on density matrices is admissible under physical maps.

## Quantum Fisher information
The symmetric logarithmic derivative L_theta is defined by d rho/d theta = (rho L_theta + L_theta rho)/2.
The QFI is F_Q = Tr(rho L_theta^2).
For a pure-state family, QFI collapses to four times the variance of the generating Hamiltonian.
For maximally mixed states, QFI vanishes because the family is locally uninformative.
That vanishing is not a failure; it is the geometry saying no local parameter can be extracted.

## Geometry relation to Bures and Fubini-Study
QFI is tied to the Bures metric by ds_B^2 = (1/4) F_Q d theta^2.
On pure states, the same object reduces to the Fubini-Study geometry described in [[quantum-geometry-fubini-study]].
This is why the pure/mixed boundary is not a separate universe.
It is one geometry with different admissibility regions.

## Entanglement and metrology
QFI is a witness of metrological usefulness.
If F_Q exceeds the shot-noise scale, the family is more useful than classical separable noise.
If the scaling reaches the Heisenberg regime, the family is strongly entangled.
This is the right page to read alongside [[entanglement-theory]] and [[resource-theories-quantum-reference]].

## Wigner-Yanase and monotone metrics
The Wigner-Yanase skew information is another way to quantify noncommutativity relative to a generator.
It sits inside the Petz family of monotone metrics.
That family matters because it shows there is a constrained family of admissible geometries rather than a single magic formula.
[[distance-metrics-state-space]] is the broader metric catalog; this page is the precision-theory slice.

## Relevance to this system
The system’s distinguishability and shell questions are geometric, so QFI belongs here.
It helps locate where a family is locally separated, where it is locally flat, and where a perturbation is load-bearing.
That makes it relevant to [[constraint-on-distinguishability-formal-reference]], [[formal-constraints-and-geometry]], and [[axis-and-entropy-reference]].
It also gives a natural language for why some candidates survive only under sufficiently rich probes.

## Key results
1. QFI is the local sensitivity metric for parametric quantum families.
2. QFI reduces to four times the pure-state variance under unitary encoding.
3. QFI and Bures geometry are the same local structure up to scaling.
4. QFI can witness entanglement and metrological enhancement.
5. Multi-parameter estimation is obstructed by noncommuting generators.

## Open questions
- Which shell parameters are genuinely QFI-sensitive in the live engine?
- Is the system’s Axis 0 more naturally read as a QFI gradient or a coherent-information gradient, or are those only partial views?
- Which monotone metric is actually load-bearing for the surviving families?
- Does the geometry remain stable when the topology class changes?

## Related pages
- [[information-geometry-reference]]
- [[quantum-geometry-fubini-study]]
- [[distance-metrics-state-space]]
- [[entanglement-theory]]
- [[resource-theories-quantum-reference]]
- [[cptp-maps-and-channels]]
- [[density-matrix-mathematics]]
- [[constraint-on-distinguishability-formal-reference]]
- [[formal-constraints-and-geometry]]
- [[axis-and-entropy-reference]]

## Sources
- The page synthesizes standard QFI, Bures, and monotone-metric results from quantum information geometry.
- It is written from domain knowledge rather than from an ingested raw file.
