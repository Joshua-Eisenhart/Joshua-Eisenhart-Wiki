---
title: QFI Kill-Point Behavior
created: 2026-04-09
updated: 2026-04-16
type: concept
tags: [geometry, quantum, simulation, constraints]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_pure_lego_qfi_killpoint_divergence.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_pure_lego_qfi_wy_qgt.py
framing: current
---

# QFI Kill-Point Behavior

Quantum Fisher Information (QFI) may diverge or vanish at the same parameter values where the constraint cascade kills families. In the current wiki this is still a support hypothesis tied to existing result artifacts, not a settled present-tense mapping.

## Core Idea

The QFI F_Q(η) measures how distinguishable nearby states are along parameter direction η. The Cramér-Rao bound gives: Var(η̂) ≥ 1/F_Q.

Two extreme behaviors signal structural transitions:
- **F_Q → ∞**: infinitesimally small parameter changes produce maximally distinguishable states (the system is maximally sensitive)
- **F_Q → 0**: nearby states are indistinguishable along η (the system is maximally insensitive)

At constraint cascade kill points (L4, L6), one candidate reading is that one of these extremes may occur — the family either becomes very sensitive or very insensitive under the tested probe family. That still needs rerun-backed tightening before it should be treated as live truth.

## QFI Definition

For a parametric family ρ(η) and symmetric logarithmic derivative L satisfying dρ/dη = (Lρ + ρL)/2:

F_Q(η) = Tr[ρ L²]

For pure states |ψ(η)⟩: F_Q = 4(⟨∂_ηψ|∂_ηψ⟩ - |⟨∂_ηψ|ψ⟩|²)

For mixed states, the QFI is the Bures metric component: F_Q = 4 ∂²D_B / ∂(dη)².

## Connection to Axis 0

Axis 0 is ∇_η I_c — the gradient of coherent information. QFI can be compared against how metrologically meaningful that gradient is:

- Where F_Q is large and ∇I_c is large: the shell parameter controls a distinguishable degree of freedom with quantum content
- Where F_Q is small and ∇I_c is large: the gradient exists but is metrologically invisible
- Where F_Q diverges and ∇I_c is finite: one candidate reading is that the system is near a structural boundary

## Result Evidence

`qfi_killpoint_divergence_results.json` exists in sim_results/. `pure_lego_qfi_wy_qgt_results.json` also relevant. See [[probe-doc-result-map]] for status.

## Open Questions

- Does F_Q diverge at L4 (composition kill) or L6 (irreversibility kill)?
- Is QFI divergence correlated with Bures metric degeneracy?
- Does the QFI/gradient alignment change across the cascade (early shells: aligned, late shells: misaligned)?

## Related Pages

- [[quantum-fisher-information-geometry]] — QFI, Bures metric, entanglement witnessing
- [[distance-metrics-state-space]] — Bures distance, fidelity
- [[pytorch-ratchet-build-plan]] — Axis 0 formal math, ∇I_c
- [[geometry-ingredient-map]] — geometry ingredient inventory
- [[probe-doc-result-map]] — mapping to actual sim results
- [[riemannian-curvature]] — curvature of the Bures manifold

## Sources

- Braunstein, Caves. "Statistical Distance and the Geometry of Quantum States." Phys. Rev. Lett. 72, 3439 (1994).
- Paris. "Quantum Estimation for Quantum Technology." Int. J. Quantum Inf. 7, 125 (2009).
- Tóth, Apellaniz. "Quantum Metrology from a Quantum Information Science Perspective." J. Phys. A 47, 424006 (2014).
