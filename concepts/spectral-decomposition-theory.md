---
title: Spectral Decomposition Theory
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [reference, geometry, research, architecture]
sources:
  - raw/articles/new-docs/new content/spectral_decomposition_theory.md
  - raw/articles/new-docs/new content/density_matrix_mathematics.md
  - raw/articles/new-docs/new content/svd_and_low_rank_approximation.md
framing: mixed
---

# Spectral Decomposition Theory

## Overview
This page collects the spectral theorem, density-matrix diagonalization, interlacing inequalities, majorization, Nielsen’s theorem, and Schur-Horn structure.

## Main points
- Normal operators admit orthonormal eigenbases.
- Density matrices are spectral objects with probability-simplex eigenvalues.
- Majorization orders spectra and underlies LOCC convertibility.
- Spectral data control entropy and many downstream quantum quantities.

## Why it matters
This is the eigenspectrum backbone beneath density matrices, entanglement, and low-rank approximations.

## Eigenvalue Interlacing and Araki-Lieb
For rho_AB on C^m tensor C^n with eigenvalues mu_1>=...>=mu_{mn}, Thompson's inequalities constrain eigenvalues lambda_i of rho_A=Tr_B(rho_AB): sum_{i=1}^k lambda_i <= sum_{i=1}^{kn} mu_i. For pure states rho_AB=|psi><psi|, rho_A and rho_B share the same nonzero eigenvalues (Schmidt coefficients squared). The entropy consequence: |S(rho_A)-S(rho_B)|<=S(rho_AB)<=S(rho_A)+S(rho_B) -- the Araki-Lieb triangle inequality. (from spectral_decomposition_theory.md)

## Weyl's Inequalities and Perturbation Theory
For Hermitian A,B with C=A+B: gamma_k <= alpha_i+beta_j for appropriate index ranges. The perturbation corollary ||B||_op=epsilon implies |lambda_i(C)-lambda_i(A)|<=epsilon. Lidskii's theorem refines this: (gamma-alpha) is majorized by eigenvalues(B). The Hoffman-Wielandt inequality sum(gamma_i-alpha_i)^2<=||B||_F^2 gives Frobenius-norm bounds. Non-degenerate perturbation theory lambda_i(rho+eps V) = lambda_i + eps<i|V|i> + eps^2 sum_{j!=i}|<j|V|i>|^2/(lambda_i-lambda_j) + O(eps^3) fails at degeneracies. (from spectral_decomposition_theory.md)

## Majorization and Birkhoff's Theorem
x is majorized by y (x<|y) iff sum_{i=1}^k x_i^down <= sum_{i=1}^k y_i^down for all k with equality at k=n. Equivalently: x=Dy for some doubly stochastic D (Hardy-Littlewood-Polya). Birkhoff's theorem: doubly stochastic matrices = convex hull of permutations. The Lorenz curve of x lies nowhere above that of y iff x<|y. Extreme: most majorized = (1/n,...,1/n), least majorized = (1,0,...,0). (from spectral_decomposition_theory.md)

## Nielsen's Theorem and LOCC Convertibility
|psi> -> |phi> by LOCC iff lambda(rho_A^psi)<|lambda(rho_A^phi) (Nielsen 1999). Proof uses that LOCC transforms Schmidt coefficients by doubly stochastic matrices. The maximally entangled state (1/d,...,1/d) is majorized by all others, so it converts to ANY state by LOCC. GHZ and W are LOCC-incomparable. Catalytic LOCC (Jonathan-Plenio): sometimes |psi> tensor |chi> -> |phi> tensor |chi> even when |psi>-/->|phi>, using "trumping" (refined majorization). (from spectral_decomposition_theory.md)

## Schur-Horn Theorem
Diagonal entries d of a Hermitian matrix satisfy d<|lambda (eigenvalues). Conversely, any d<|lambda is achievable. For density matrices: measurement probabilities in any basis are majorized by eigenvalues. The eigenvalue distribution is the "most informative" -- it has the least entropy. Schur-Horn extends to arbitrary compact Lie groups via coadjoint orbits (Kostant). Knowing diagonals in an informationally complete set of bases determines rho uniquely. (from spectral_decomposition_theory.md)

## Entropy as Schur-Concave
S(rho) = -sum eta(lambda_i) with eta concave is Schur-concave: x<|y implies S(x)>=S(y). This means LOCC cannot increase entanglement entropy (by Nielsen + Schur-concavity). All Renyi entropies S_alpha are Schur-concave. Purity sum lambda_i^2 and lambda_max are Schur-convex. For unital channels, lambda(E(rho))<|lambda(rho) (Schur's theorem for channels), so unital channels always increase mixedness. (from spectral_decomposition_theory.md, quantum_information_measures.md)

## Related pages
- [[density-matrix-mathematics]]
- [[entanglement-theory]]
- [[svd-and-low-rank-approximation]]
- [[quantum-information-measures]]
- [[cptp-maps-and-channels]]
- [[distance-metrics-state-space]]
