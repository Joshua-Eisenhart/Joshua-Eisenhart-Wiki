---
title: Quantum Information Measures
created: 2026-04-07
updated: 2026-05-21
type: concept
tags: [reference, geometry, research, validation]
sources:
  - raw/articles/new-docs/new content/quantum_information_measures.md
  - raw/articles/new-docs/references/INFORMATION_GEOMETRY_REFERENCE.md
  - raw/articles/new-docs/references/STOCHASTIC_THERMODYNAMICS_REFERENCE.md
  - raw/articles/legacy-books/the-dark-empress-a-practical-guide-to-universal-dominion-v6-1-2.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Quantum Information Measures

## Overview
This page collects von Neumann entropy, Rényi entropies, mutual information, coherent information, the Holevo bound, and their operational meanings.

Authority boundary: this is a reference/support page. Standard quantum-information facts are background; legacy black-hole/spacetime interpretations are source genealogy; neither upgrades a repo sim, entropy lane, or bridge claim without current receipts.

## Main points
- Entropy measures state uncertainty and correlation structure.
- Strong subadditivity is the central structural inequality.
- Holevo information bounds accessible classical information from quantum ensembles.
- Coherent information is the quantum quantity most closely tied to channel capacity.

## Why it matters
This is the information-theoretic layer connecting density matrices, channels, and thermodynamic accounting.

## Fit for this wiki
Best fit:
- entropy and information on density operators, not on naked state labels
- the distinction between local uncertainty and relational information
- channel capacity, compression, and thermodynamic accounting on the same carrier

Mismatch:
- entropy is not the master variable for the wiki
- mutual information does not collapse the geometry or algebra layers
- a high entropy value is not a proof of admissibility or canonicality

## Cross-links to related support layers
- [[distinguishability-formal-reference]] for data-processing and probe-relative identity
- [[information-geometry-reference]] and [[quantum-fisher-information-geometry]] for geometric refinements of distinguishability
- [[entanglement-theory]] for the correlation side of the same state space
- [[cptp-maps-and-channels]] for the processing layer
- [[current-research-overlays]] for where this page sits in the research routing graph

## Legacy Perspective (Dark Empress)

From Chapter 12: The Dark Empress claims black hole information is embedded in space-time itself. "All the information in a black-hole is embedded in space-time. That information can cross the event horizon of a black hole, with enough time, because space-time can be 'emitted' from a black-hole."

The interior of a black hole: "The interior of the black-hole and its singularity will contain the structure of space-time at the smallest and most discrete levels on massive scales. A singularity from the inside is massive walls and not a singular point." The Dark Empress presents this as resolving the information paradox; that is a legacy source claim, not standard QIT and not repo proof.

The mechanism: space-time itself carries information via micro-gravitational waves. "Space-time itself then has to imbed information about the universe in its own structure. At the tiniest levels, space-time can be micro-curved, and those curves can contain information that can influence the universe around it." See [[entanglement-theory]] for the entanglement-space connection and [[information-geometry-reference]] for time as replication.

## Von Neumann Entropy Properties
S(rho) = -Tr(rho log rho) is non-negative (zero iff pure), bounded by log d (maximal iff maximally mixed), and concave in rho. It is unitarily invariant and additive on tensor products. The Fannes-Audenaert inequality |S(rho)-S(sigma)| <= T log(d-1) + h(T) gives tight continuity bounds where T = (1/2)||rho-sigma||_1. Strong subadditivity S(ABC)+S(B) <= S(AB)+S(BC) is the deepest inequality, equivalent to non-negativity of conditional mutual information I(A:C|B) >= 0. Its equality condition (Hayden-Jozsa-Petz-Winter 2004) characterizes quantum Markov chain structure. (from quantum_information_measures.md)

## Renyi Entropies and Operational Meanings
S_alpha(rho) = (1/(1-alpha)) log Tr(rho^alpha) interpolates between key quantities: S_0 = log(rank) (Hartley), S_1 = S (von Neumann via L'Hopital), S_2 = -log(purity) (collision), S_inf = -log(lambda_max) (min-entropy). Renyi entropies are non-increasing in alpha and all agree on pure states. Operationally: S_0 counts nonzero-probability outcomes, S_1 gives optimal compression rate (Schumacher), S_2 relates to collision probability for randomness extraction, and S_inf bounds guessing probability for cryptography. The sandwiched Renyi relative entropy D_alpha(rho||sigma) converges to quantum relative entropy as alpha->1. (from quantum_information_measures.md)

## Conditional Entropy Can Be Negative
S(A|B) = S(AB)-S(B) is negative for entangled pure states: S(AB)=0 but S(B)>0, giving S(A|B) = -S(B) < 0. Maximum negativity S(A|B) >= -log d_A is achieved by maximally entangled states. This negativity has operational meaning: -S(A|B) equals the coherent information, the rate of quantum state merging. Classically conditioned quantum entropy S(B|X) = sum p_x S(rho_B^x) is always non-negative -- negativity arises specifically from quantum correlations. (from quantum_information_measures.md)

## Holevo Bound and Data Processing
The Holevo quantity chi = S(rho) - sum p_x S(rho_x) bounds accessible classical information: I(X:Y) <= chi. The proof uses the classical-quantum state rho_{XB} = sum p_x |x><x| tensor rho_x and data processing. The Holevo-Schumacher-Westmoreland theorem achieves chi as the classical capacity for i.i.d. channels. The data processing inequality S(rho||sigma) >= S(N(rho)||N(sigma)) for CPTP maps N is tied to Petz recovery in equality cases; modern rotated/approximate recovery results provide near-optimal recovery bounds. (from quantum_information_measures.md, cptp_maps_and_channels.md)

## Entropy Cone and Quantum-Classical Differences
For n=2 parties, the entropy region is characterized by subadditivity and Araki-Lieb. For n=3, strong subadditivity adds S(ABC)+S(B) <= S(AB)+S(BC). Quantum entropy vectors differ from classical ones because monotonicity/conditional nonnegativity can fail; negative conditional entropy is a key witness, not the whole cone story. For mutual information, the quantum bound I(A:B) <= 2 min(S(A),S(B)) is twice the classical bound -- a genuinely quantum feature. The additivity conjectures for minimum output entropy and entanglement of formation were both disproved by Hastings (2009). (from quantum_information_measures.md)

## Related pages
- [[density-matrix-mathematics]]
- [[information-geometry-reference]]
- [[stochastic-thermodynamics-reference]]
- [[distinguishability-formal-reference]]
- [[spectral-decomposition-theory]]
- [[cptp-maps-and-channels]]
- [[quantum-computing-applications]]
- [[distance-metrics-state-space]]
- [[entanglement-theory]]
- [[compression-math-density-matrix]]
- [[current-research-overlays]]
