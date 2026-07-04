---
title: Distance Metrics State Space
created: 2026-04-07
updated: 2026-04-10
type: summary
tags: [reference, research, mathematics, quantum]
sources:
  - raw/articles/new-docs/new content/distance_metrics_state_space.md
  - https://arxiv.org/abs/1810.05583v5
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Distance Metrics on Quantum State Space

## Definition
This page organizes the main distances and divergences used to compare quantum states and channels.
It is the operational side of distinguishability geometry.
The page keeps state metrics, channel metrics, and asymptotic divergences distinct rather than collapsing them into one summary number.

## Core structures
- Trace distance for single-shot state discrimination.
- Fidelity and Bures distance for overlap and geometry.
- Fubini-Study metric for pure-state projective geometry.
- Quantum Fisher information for local sensitivity.
- Relative entropy for asymptotic rates.
- Diamond norm for channel discrimination.

## Trace distance
The trace distance D(rho, sigma) = 1/2 ||rho - sigma||_1 is the most operational state metric.
It directly controls the optimal single-copy discrimination probability.
It is contractive under CPTP maps, so physical noise cannot make two states more distinguishable.
For qubits, the trace distance is half the Euclidean distance between Bloch vectors.
That makes it the simplest state-level geometry on the carrier.

## Fidelity and Bures distance
Fidelity measures overlap, not separation.
The Bures distance converts fidelity into a true metric.
This pair is useful because many quantum tasks care about closeness to a target rather than linear separability.
The Fuchs-van de Graaf inequalities connect trace distance and fidelity, so these are not unrelated views.
The Bures metric is the Riemannian continuation used in [[quantum-fisher-information-geometry]] and [[quantum-geometry-fubini-study]].

## Fubini-Study and Berry relation
For pure states, the Fubini-Study metric is the natural projective geometry.
The Berry phase is the holonomy of its connection.
That means the metric and the holonomy are two sides of the same bundle story.
The system cares about this because [[berry-phase-and-holonomy]] and [[fiber-bundles-and-spin-geometry]] keep returning to the same carrier picture.

## Relative entropy
Relative entropy is not a metric, but it is a crucial divergence.
It controls asymptotic discrimination rates and satisfies data processing.
Pinsker-type bounds show it upper-bounds trace-distance behavior.
This makes it the right object when comparing long-run distinguishability rather than one-shot separation.

## Diamond norm for channels
Channel comparison needs a stronger notion than state comparison.
The diamond norm measures distinguishability of maps with ancilla assistance.
This is why channel-level comparison appears when the target is not a state but a dynamics rule.
The metric hierarchy is therefore state, geometry, divergence, channel, not one undifferentiated class.

## System relevance
The system repeatedly asks whether two candidates are distinguishable under the active probe set.
That makes this page directly relevant to [[constraint-on-distinguishability-formal-reference]] and [[formal-constraints-and-geometry]].
It also helps interpret [[qit-engine-geometry-entropy-bridge]] because bridge candidates should be compared by an operational metric, not by a bare label.
When the live stack asks about Axis 0, it is asking for a quantity with geometric and operational meaning.

## Key results
1. Trace distance is the most direct single-shot operational metric.
2. Fidelity and Bures distance encode overlap and Riemannian structure.
3. Fubini-Study is the projective pure-state geometry.
4. Relative entropy governs asymptotic comparison.
5. Diamond norm is the correct channel-level escalation.

## Open questions
- Which metric is the right discriminator for each shell family in the live engine?
- Does Axis 0 track trace distance, Bures distance, or coherent information more faithfully in the current geometry?
- Which of the surviving families become separable only after topology change?
- Can the same metric hierarchy explain both state distinction and topology-sensitive coupling?

## 2026-04-11 arXiv source addition

### 1810.05583v5 — Thermodynamic length in open quantum systems
- Gives an explicit metric/geodesic treatment for dissipation in open quantum systems.
- Useful because it sharpens the distance/geometry side of the wiki with a direct open-system metric paper rather than pure state-space recap only.
- Best fit pages: [[distance-metrics-state-space]], [[information-geometry-reference]], [[stochastic-thermodynamics-reference]].

## Related pages
- [[quantum-fisher-information-geometry]]
- [[quantum-geometry-fubini-study]]
- [[berry-phase-and-holonomy]]
- [[constraint-on-distinguishability-formal-reference]]
- [[density-matrix-mathematics]]
- [[quantum-information-measures]]
- [[cptp-maps-and-channels]]
- [[cross-domain-equivalence-map]]
- [[qit-engine-geometry-entropy-bridge]]
- [[formal-constraints-and-geometry]]
- [[wiki-driven-arxiv-search-queue]]

## Sources
- The page synthesizes standard results from quantum distance and channel discrimination theory.
- It is written from domain knowledge rather than from an ingested raw file.
