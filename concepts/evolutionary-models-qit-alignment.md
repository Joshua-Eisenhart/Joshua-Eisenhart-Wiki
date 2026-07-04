---
title: Evolutionary Models QIT Alignment
created: 2026-04-07
updated: 2026-04-07
type: comparison
tags: [comparison, research, architecture, simulation]
sources:
  - raw/articles/new-docs/new content/evolutionary_models_qit_alignment.md
  - raw/articles/new-docs/references/EVOLUTIONARY_EPISTEMOLOGY_REFERENCE.md
  - raw/articles/new-docs/references/FEP_AND_ACTIVE_INFERENCE_REFERENCE.md
framing: mixed
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Evolutionary Models QIT Alignment

## What is being compared
How replicator dynamics, mutation-selection balance, and evolutionary game theory line up with quantum-information language.

## Comparison
| Evolution | QIT | Mapping |
|---|---|---|
| Population frequencies | diagonal density matrices | exact embedding |
| Fitness | Hamiltonian / measurement operator | exact in diagonal case |
| Mutation | CPTP / classical channel | exact for stochastic mutation |
| Selection | post-selection / purification | structural, nonlinear in general |
| Drift | noise / depolarization | exact for finite-population analogs |

## Verdict
The strongest bridge is the diagonal-state embedding; nonlinear selection is the main mismatch.

## Replicator Equation as Continuous Measurement
For frequency-independent fitness F=diag(f_1,...,f_n), the replicator equation d rho/dt = F rho + rho F - 2 Tr(F rho) rho is the nonlinear von Neumann equation with normalization. Linearization: define sigma = exp(Ft) rho_0 exp(Ft), then rho(t)=sigma/Tr(sigma). This is Lueders rule for non-selective measurement with operator exp(Ft/2). Nature continuously "measures" the population: fittest types have highest detection probability. The anti-commutator {F,rho} (not commutator [H,rho]) reflects dissipative rather than conservative dynamics. (from evolutionary_models_qit_alignment.md)

## Shahshahani Metric and Fisher-Rao
The natural metric on the probability simplex ds^2 = sum (dx_i)^2/x_i is the Fisher-Rao metric = Fubini-Study restricted to diagonal density matrices. Under this metric, replicator dynamics is a gradient flow dx/dt = grad V(x). KL divergence D_KL(x*||x) to the ESS is a Lyapunov function: d/dt D_KL = -(sum x*_i f_i - f_bar) <= 0. Free energy F(sigma) = Tr(sigma H) - T S(sigma) = F(rho_beta) + T S(sigma||rho_beta) gives the same Lyapunov structure. (from evolutionary_models_qit_alignment.md)

## Frequency-Dependent Fitness and Nonlinearity
With payoff matrix A: f_i = (Ax)_i, the replicator becomes quadratic in rho -- genuinely nonlinear. No linear quantum channel reproduces this exactly. Mean-field approximation rho^2 -> rho * Tr(A rho) recovers a Lindblad form: d rho/dt ~ [A,rho] + {A-Tr(A rho)I, rho}. Recombination is analogous to entangling operations on multi-locus systems. Genetic drift corresponds to depolarizing noise. The fundamental tension: evolutionary dynamics is nonlinear, quantum channels are linear. (from evolutionary_models_qit_alignment.md)

## Related pages
- [[evolutionary-epistemology-reference]]
- [[fep-and-active-inference-reference]]
- [[quantum-information-measures]]
- [[density-matrix-mathematics]]
- [[quantum-geometry-fubini-study]]
- [[density-matrices-across-fields]]
