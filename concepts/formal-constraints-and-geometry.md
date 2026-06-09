---
title: Formal Constraints and Geometry
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [reference, validation, system, architecture]
sources:
  - raw/articles/system-v5-reference-docs/Formal constraints and geometry.md
  - raw/articles/new-docs/CONSTRAINT_SURFACE_AND_PROCESS.md
  - raw/articles/new-docs/CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md
framing: mixed
---

# Formal Constraints and Geometry

## Overview
Strict tabular extraction of the constraint-to-geometry chain: root constraints, extended axioms, base admissibility fences, topology/relation fences, carrier and state layer, Pauli/operator basis, spinor/Hopf geometry, loop geometry, chiral working layer, and Weyl spinor layer. This preserves the source/model build-order language from constraints to axes; use current spec mirrors and repo receipts for live admission status.

## Root Constraints and Constraint Manifold

| Object | Math | Role |
|---|---|---|
| Root constraint 1 (F01) | dim(H_S) < infinity, |P| < infinity, |O| < infinity, |Gamma| < infinity | Bounded distinguishability |
| Root constraint 2 (N01) | AB != BA in general | Order-sensitive composition |
| Constraint manifold M(C) | {x : x admissible under C} | Pre-geometry state space |
| Build order | constraints to M(C) to geometry on M(C) to A_i: M(C) to V_i | Root-to-axis chain |

## Extended Axioms (No Primitive X)

Seven extended axioms ban primitive identity, primitive equality, primitive time/causality, primitive geometry/coordinates, free algebraic closure, and proofless claims. Every admissible claim requires a finite witness.

## Base Admissibility Fences (BC04-BC12)

Nine fences: identity ban, equality ban, order ban, closure ban, probe-relative identification, probability ban, metric/coordinate ban, optimization ban, anti-smuggling rule. These are the root-level prohibitions that force everything downstream to be earned.

## Topology/Relation Fences (T1-T8)

Thirteen fences prevent importing analytic, metric, or semantic structure at the topology layer. Adjacency does not imply direction, metric, reachability, or identity. Topology is relational only.

## Carrier and State Layer

Hilbert carrier = C^2. Density state space D(C^2). Bloch decomposition rho = 1/2(I + r dot sigma). Base Hamiltonian H_0 = n_x sigma_x + n_y sigma_y + n_z sigma_z. Pauli basis: I, sigma_x, sigma_y, sigma_z, sigma_minus, sigma_plus.

## Spinor and Hopf Geometry

Spinor carrier S^3 = {psi in C^2 : |psi| = 1}. Hopf projection pi(psi) to S^2. Hopf chart psi_s(phi, chi; eta) with nested torus strata T_eta. Clifford torus at eta = pi/4. Hopf connection A = -i psi^dagger d psi = d phi + cos(2 eta) d chi.

## Loop Geometry

Fiber loop gamma_f^s(u) = psi_s(phi_0 + u, chi_0; eta_0): density-stationary path (rho constant). Base loop gamma_b^s(u) = psi_s(phi_0 - cos(2 eta_0)u, chi_0 + u; eta_0): density-traversing path (rho varies). Horizontal condition A(gamma-dot_b^s) = 0.

## Weyl Spinor Layer

Left sheet: H_L = +H_0, psi_L in S^3, rho_L = psi_L psi_L^dagger, precession r-dot_L = 2 n cross r_L. Right sheet: H_R = -H_0, mirror. The left/right split is load-bearing: Hamiltonian sign differs, loop ownership differs, engine type assignment differs, bridge into chiral cut-state depends on it.

Engine placement: Type 1 inner = (rho_L, gamma_f^L), Type 1 outer = (rho_L, gamma_b^L), Type 2 inner = (rho_R, gamma_f^R), Type 2 outer = (rho_R, gamma_b^R).

## Full Chain

constraints -> M(C) -> S^3 -> T_eta -> (psi_L, psi_R) -> (rho_L, rho_R, gamma_f, gamma_b) -> Xi -> rho_AB -> entropy

## How it connects
This page is the explicit version of the build order implicit in [[constraint-surface-and-process]] and [[constraint-on-distinguishability]]. See [[axis-and-entropy-reference]] for the downstream axis layer and [[system-architecture-reference]] for the CS axiom translations.

## Extended Axioms — detail
The seven extended axioms define what the system forbids at root level. Identity is not primitive; it requires contrast under admissible probes. Equality is replaced by probe-relative indistinguishability: a~b iff every probe in a finite admissible family gives matching results. No primitive time parameter exists; ordered composition is structural. No primitive coordinates, metric, or geometry are admitted. No closure or completeness is given by default — composition must be explicitly admitted.

## Base Admissibility Fences — detail
BC04 through BC12 form the admission firewall. BC04 bans primitive identity predicates on state-tokens. BC05 bans unrestricted substitution (no primitive equality). BC06 forbids global total orders — only explicit finite sequencing is allowed. BC07 denies closure by fiat. BC08 requires that any identification go through a finite probe family, not labels. BC09 bars probabilistic primitives at base. BC10 blocks metric, distance, norm, or coordinate charts from being fundamental. BC11 forbids optimization or utility primitives. BC12 is the anti-smuggling rule: every new term needs an explicit admissible definition.

## Topology/Relation Fences — detail
T1-T8 fences ensure the topology layer imports nothing extra. T1_01 makes compatibility scoped, not global. T2_01-T2_03 separate adjacency from direction, distance, and reachability. T3_01-T3_02 require explicit neighborhoods and forbid analytic semantics. T4_03 prevents path equivalence by fiat. T6_01 prevents identity from relation alone. T6_03 blocks scalarization. T8_01-T8_03 forbid geometry, smoothness, and semantic inflation at the topology layer.

## Why the source treats the Weyl spinor layer as load-bearing
In the source/model build order, the left/right Weyl split is not optional decoration. Removing it collapses the model into generic qubit geometry with no chirality, no engine type assignment, and no bridge into the chiral cut-state. The Hamiltonian sign differs (H_L = +H_0 vs H_R = -H_0), loop ownership differs, and the bridge into Axis 0 depends on it. See [[terrain-laws-and-loop-geometry]] for the eight terrain laws that live on these sheets and [[qit-engine-geometry-entropy-bridge]] for the master-table separation.

## Source
Extracted from `raw/articles/system-v5-reference-docs/Formal constraints and geometry.md`. This page covers the constraint-to-geometry build chain; see [[axis-0-1-2-qit-packet]] for the downstream Axis 0-2 math and [[system-tools-and-plan]] for the enforcement layer.
