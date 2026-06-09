---
title: Entanglement Theory
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, research, validation, geometry]
sources:
  - raw/articles/new-docs/new content/entanglement_theory.md
  - raw/articles/new-docs/new content/schmidt_decomposition_bipartite.md
  - raw/articles/new-docs/new content/quantum_information_measures.md
  - raw/articles/system-v5-reference-docs/Older Legacy/The Dark Empress-A Practical Guide to Universal Dominion V6.1 copy.md
framing: mixed
---

# Entanglement Theory

## Overview
This page gathers separability, Schmidt decomposition, PPT tests, concurrence, entanglement of formation, negativity, and related measures.

## Main points
- Separable states are convex mixtures of product states.
- Schmidt decomposition makes pure-state bipartite structure explicit.
- PPT is necessary and sufficient in low dimensions, but not in general.
- Many entanglement measures are operationally tied to channel or state-processing tasks.

## Why it matters
This page is the core entanglement reference for the wiki’s tensor, correlation, and distinguishability layers.

## Fit for this wiki
Best fit:
- bipartite and multipartite structure on the same carrier
- correlation that is not reducible to local state summaries
- operational limits on separability, distillation, and channel use

Mismatch:
- entanglement is not the same thing as generic correlation
- PPT and concurrence are only part of the story, not the whole carrier geometry
- the page supports the stack; it does not replace the carrier/probe admissibility pages

## Cross-links to related support layers
- [[quantum-information-measures]] for entropy, coherent information, and Holevo structure
- [[quantum-fisher-information-geometry]] for entanglement witnessing via precision geometry
- [[schmidt-decomposition-bipartite]] for the pure-state structural core
- [[cptp-maps-and-channels]] for channel-processing limits
- [[current-research-overlays]] for the routing layer that explains where this page fits

## Legacy Perspective (Dark Empress)

From Chapter 12: The Dark Empress claims entanglement is foundational, not bolted on. "Instead of being something we attach on to theories we use to describe the universe, it probably should lie at the foundational root of all theories."

The book argues dimensions are born from entanglement defining directionality: "A dimension is born out of entanglement defining a direction to be opposite of another direction." Space replicates via entanglement patterns — "A certain pattern emerged that could replicate itself and grow more space" — and "Time is born with the entropy of entangled 'space'."

The claim: entanglement of space is more likely to happen at random than a stable photon appearing. Two entangled regions of space form the simplest replicating structure, and from this "space has just had the most basic reproductive system running for a long time." See [[information-geometry-reference]] for the time-as-replication view and [[entropy-sweep-protocol]] for entropy as quantum gravity.

## Concurrence and Entanglement of Formation
For 2-qubit states, concurrence C(rho) = max(0, lambda_1-lambda_2-lambda_3-lambda_4) where lambda_i are square roots of eigenvalues of rho*rho_tilde (spin-flipped). C=0 iff separable, C=1 for maximally entangled. For pure states |Psi>=a|00>+b|01>+c|10>+d|11>, C=2|ad-bc|. Wootters' formula E_F(rho) = h((1+sqrt(1-C^2))/2) gives entanglement of formation analytically for all 2-qubit states. Bell-diagonal states are entangled iff one Bell population exceeds 1/2, with C = max(0, 2p_1-1). (from entanglement_theory.md)

## Negativity and Logarithmic Negativity
N(rho) = (||rho^{T_A}||_1-1)/2 equals the sum of absolute values of negative eigenvalues of the partial transpose. For 2x2 systems, N>0 iff entangled. Logarithmic negativity E_N = log_2(1+2N) is additive and upper-bounds distillable entanglement. For 2-qubit pure states with Schmidt coefficients sqrt(lambda), sqrt(1-lambda): N = sqrt(lambda(1-lambda)) = C/2. E_N is an entanglement monotone despite non-convexity. (from entanglement_theory.md)

## Quantum Discord
Quantum discord D(A|B) = I(A:B)-J(A:B) measures non-classical correlations beyond entanglement. J(A:B) is classical correlation (optimized over POVMs on B). D=0 iff the state is classical-quantum: rho = sum p_j rho_j^A tensor |j><j|. Discord is asymmetric (D(A|B) != D(B|A)) and can be nonzero for separable states. Computing D is NP-hard (Huang 2014). For Bell-diagonal states and X-states, analytic formulas exist. (from entanglement_theory.md)

## Bell-CHSH and Horodecki Criterion
The CHSH operator B = a tensor b + a tensor b' + a' tensor b - a' tensor b' satisfies |<B>|<=2 classically (local hidden variables) and |<B>|<=2sqrt(2) quantumly (Tsirelson bound). The Horodecki criterion for 2-qubit states: max CHSH violation = 2sqrt(t_1^2+t_2^2) where t_1>=t_2 are the largest singular values of T. Violates iff t_1^2+t_2^2>1. Werner states are entangled for p>1/3 but don't violate Bell until p>1/sqrt(2) -- entanglement doesn't always imply Bell violation. (from entanglement_theory.md)

## Monogamy and Distillation
The CKW inequality C^2(A,BC)>=C^2(A,B)+C^2(A,C) quantifies monogamy: entanglement with one party constrains entanglement with others. The 3-tangle tau_3 = C^2(A,BC)-C^2(A,B)-C^2(A,C) measures genuine tripartite entanglement (1 for GHZ, 0 for W). Monogamy underpins QKD security. Distillable entanglement E_D <= E_F with equality only for pure states. PPT states have E_D=0 (bound entanglement) even when entangled. The hierarchy E_D<=E_N<=E_F and E_D<=E_R captures irreversibility of mixed-state entanglement manipulation. (from entanglement_theory.md)

## Resource Theory Framing
Entanglement is a resource under LOCC (local operations and classical communication). Free states = separable states. Monotones = concurrence, negativity, entanglement of formation. See [[resource-theories-quantum-reference]] for the general resource theory framework and how entanglement as resource maps to the system's constraint-admissibility structure.

## Related pages
- [[density-matrix-mathematics]]
- [[quantum-information-measures]]
- [[quantum-fisher-information-geometry]]
- [[stochastic-thermodynamics-reference]]
- [[schmidt-decomposition-bipartite]]
- [[spectral-decomposition-theory]]
- [[quantum-computing-applications]]
- [[information-geometry-reference]]
- [[entropy-sweep-protocol]]
- [[cptp-maps-and-channels]]
- [[distance-metrics-state-space]]
- [[current-research-overlays]]
