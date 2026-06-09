---
title: Resource Theories Quantum Reference
created: 2026-04-09
updated: 2026-05-21
type: concept
tags: [reference, quantum, formal, mathematics, constraints, entropy]
sources:
  - https://arxiv.org/abs/1907.06306v2
  - https://arxiv.org/abs/1510.03695v2
  - https://arxiv.org/abs/1806.04937v3
  - https://arxiv.org/abs/2111.12646v4
  - https://doi.org/10.1103/RevModPhys.91.025001
  - https://doi.org/10.1103/PhysRevLett.115.070503
framing: reference_support_snapshot
---

# Resource Theories in Quantum Information

Resource theory is a framework for studying what transformations are possible under restricted operations. In quantum information, it provides the formal structure for entanglement theory, coherence theory, thermodynamics, and asymmetry. The constraint-admissibility framing of this system can be read through a resource-theory lens, but this page is analogy/support unless a specific repo lane defines free states, free operations, monotones, and conversion criteria.

Authority boundary: standard resource-theory facts stay as reference math. Any claim that a Codex Ratchet shell, family, or cascade is a resource theory requires an explicit local definition and repo evidence.

## Core Structure

A resource theory consists of three components:

1. **Free states** (ρ_free): States that are "free" — cost nothing to prepare. In entanglement theory: separable states. In coherence theory: diagonal states. In thermodynamics: Gibbs states.

2. **Free operations** (O_free): Transformations that cost nothing to implement. In LOCC (entanglement): local operations and classical communication. In MIO (coherence): maximally incoherent operations. In thermal operations: energy-preserving unitaries with a thermal bath.

3. **Resource states** (ρ_resource): States not preparable by free operations from free states. These are the "valuable" states.

### Monotones

A **resource monotone** is a function M(ρ) that is non-increasing under free operations:

ρ →_free σ  implies  M(ρ) ≥ M(σ)

Monotones quantify how much resource a state contains. Different monotones capture different aspects.

### Conversion Conditions

State conversion: ρ →_free σ is possible iff M(ρ) ≥ M(σ) for ALL monotones M. The set of monotones is **complete** if this "iff" holds. Entanglement convertibility generally lacks a simple finite complete monotone set. More generally, discrimination-task advantages can serve as a complete family of monotones in broad resource-theory settings, so one-monotone arguments should be treated as lower bounds or heuristics unless completeness is actually shown.

## Major Resource Theories

### Entanglement

- **Free states**: Separable states ρ = Σ_i p_i ρ_i^A ⊗ ρ_i^B
- **Free operations**: LOCC (local operations, classical communication)
- **Monotones**: Entanglement entropy (pure states), concurrence, negativity, squashed entanglement
- **Key result**: Entanglement is monogamous — if A is maximally entangled with B, it has zero entanglement with any C

### Coherence

- **Free states**: Diagonal states in a fixed reference basis
- **Free operations**: Incoherent operations (IO) or strictly incoherent operations (SIO)
- **Monotones**: l1-coherence, relative entropy of coherence, robustness of coherence
- **Key result**: Coherence is a resource for quantum speedup and is basis-dependent

### Asymmetry (frameness of reference)

- **Free states**: Symmetric under a group G (e.g., phase-invariant states for U(1))
- **Free operations**: G-covariant operations
- **Monotones**: Weighted robustness, asymmetry measures
- **Key result**: Asymmetry is dual to entanglement — a resource for breaking symmetry

### Thermodynamics

- **Free states**: Gibbs states ρ_β = e^{-βH}/Z
- **Free operations**: Thermal operations (energy-preserving unitaries with a thermal bath)
- **Monotones**: Free energy F(ρ) = Tr[Hρ] - S(ρ)/β
- **Key result**: free energy is one monotone in standard thermodynamic regimes. Single-shot, catalytic, or approximate settings require families of generalized free energies rather than one simple iff rule for work extraction.

## Relevance to This System

### Constraint Admissibility as Resource Theory

One candidate mapping reads the system's framing as a resource theory where:
- **Free states**: States admissible under all active constraints (the intersection S0 ∩ S1 ∩ ... ∩ S_k)
- **Free operations**: Operations that preserve admissibility (map admissible states to admissible states)
- **Resource states**: States admissible under fewer constraints (survive some shells but not others)
- **Candidate monotones**: entropy quantities proposed for testing; non-increase must be proven for the declared free operations and constraint additions

The constraint cascade L0-L7 is a chain of resource theories where each level adds constraints (restricts free operations, reclassifies some states from free to resource).

### Connection to Shell Nesting

If S0 ⊃ S1 ⊃ S2, then:
- S0-free ⊇ S1-free ⊇ S2-free (fewer states are free at higher shells)
- S0-ops ⊇ S1-ops ⊇ S2-ops (fewer operations are free at higher shells)
- More states become "resource" (valuable) at higher shells

This is a possible reading of the cascade: geometry may be enriched at lower levels and dynamics selected later. Treat it as a mapping to test, not a result promoted by this reference page.

### Connection to the 28 Families

If a future receipt defines a full resource ordering over the 28 irreducible families, they could be read as candidate resource objects in that ordering. This page does not prove minimality or that the full constraint set has a completed resource theory.

### Connection to Monogamy

Entanglement monogamy says a state cannot be maximally entangled with two independent systems simultaneously. The system's constraint structure may enforce a generalized monogamy: a family that is "maximally admissible" under one constraint shell may be "minimally admissible" under another.

## Key Results

1. **Resource theory completeness**: For entanglement, the set of monotones is not finite — infinitely many are needed to characterize convertibility (Vidal 1999). For coherence, a finite set suffices (Winter, Yang 2016).
2. **Second laws of resource theories**: Each resource theory has a family of second laws (one per monotone). The system's entropy sweep protocol is essentially a search for the right monotones.
3. **Resource destroyers**: Some operations destroy all resource. Dephasing destroys coherence. Decoherence destroys entanglement. These correspond to the "kill" operations in the constraint cascade.
4. **Discrimination-task completeness**: Takagi and Regula (2019) show that, across general resource theories, discrimination-task advantages provide a complete operational characterization of resource ordering.
5. **Resource interconversion**: Entanglement can be converted to coherence and vice versa in some regimes with overhead. This suggests an analogy for the system's cross-domain equivalence claims; it does not prove those couplings.

## 2026-04-10 open-access source additions

These papers were pulled from the current wiki-driven arXiv queue and are now the cleanest open-access support for the resource-theory lane.

### 1907.06306v2 — Resource theory of asymmetric distinguishability for quantum channels
- Extends the resource-theory frame from states to channel boxes.
- Makes distinguishability an operational resource under superchannels.
- Gives one-shot and asymptotic conversion statements, including distillation and dilution.
- Best use here: support for channel-level resource ordering and asymmetric comparison.

### 1510.03695v2 — Relative submajorization and its use in quantum resource theories
- Generalizes majorization to approximate resource conversion.
- Gives a geometric and linear-programming-duality formulation via Lorenz curves.
- Best use here: support for comparison geometry, convertibility, and reversibility bounds.

### 1806.04937v3 — The first law of general quantum resource theories
- Extends resource-theory language to multiple resources at once.
- Treats the interplay of constraints as a generalized first law.
- Emphasizes relative entropy distances from invariant sets.
- Best use here: multi-resource ordering and thermodynamic-style exchange under constraints.

### 2111.12646v4 — Stochastic approximate state conversion for entanglement and general quantum resource theories
- Studies the intermediate regime between deterministic and probabilistic conversion.
- Gives bounds on maximal fidelity for a given success probability.
- Applies across general resource theories and to channel manipulation.
- Best use here: approximate conversion, stochastic conversion, and rate bounds.

### Fit to the wiki
- These papers strengthen [[distinguishability-formal-reference]] by moving from generic comparison language to explicit resource-order language.
- They also support [[constraint-on-distinguishability-full-math]] as the operational backbone behind convertibility.
- They are support pages, not proof that the current shell order is canonical.

## Open Questions

- Can the 28 families be organized as a Hasse diagram of resource convertibility under the full constraint set?
- Does the system's constraint cascade define a unique resource theory, or are there multiple consistent choices?
- Is there a "resource theory of resource theories" that classifies the different constraint combinations?

## Related Pages

- [[entanglement-theory]] — entanglement as a resource
- [[quantum-shannon-theory-reference]] — capacity and resource convertibility
- [[constraint-surface-and-process]] — the constraint manifold
- [[entropy-sweep-protocol]] — searching for admissible entropy families
- [[viability-theory-reference]] — constraint-survival framing (parallel to resource framing)
- [[nominalism-in-this-system]] — identity as admissibility class
- [[distinguishability-formal-reference]] — operational compare/convert backbone
- [[wiki-driven-arxiv-search-queue]] — source queue that surfaced these papers

## Sources

- Chitambar, Gour. "Quantum Resource Theories." Rev. Mod. Phys. 91, 025001 (2019).
- Brandão, Gour. "Reversible Framework for Quantum Resource Theories." Phys. Rev. Lett. 115, 070503 (2015).
- Streltsov, Adesso, Plenio. "Quantum Coherence as a Resource." Rev. Mod. Phys. 89, 041003 (2017).
- Goold, Huber, Riera, del Rio, Skrzypczyk. "The Role of Quantum Information in Thermodynamics." J. Phys. A 49, 143001 (2016).
