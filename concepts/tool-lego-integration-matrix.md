---
title: Tool Lego Integration Matrix
created: 2026-04-14
updated: 2026-05-21
type: concept
tags: [matrix, tools, lego, integration, ablation, z3, sympy, clifford, pytorch, pyg, rustworkx, toponetx, gudhi]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/TOOL_LEGO_INTEGRATION_MATRIX.md
  - system_v5/docs/TOOL_LEGO_INTEGRATION_MATRIX.md
framing: derived_historical_tool_lego_matrix
spec_mirrors:
  - specs/codex-ratchet/tool-function-receipt-status
  - specs/codex-ratchet/sim-estate-integration-status
  - specs/codex-ratchet/lego-sim-contract-current
---

# Tool × Lego-Family Integration Matrix

## Overview
This dated derived matrix tracks integration of specific computational tools across mathematical lego families. It is useful for seeing where load-bearing claims were argued or where gaps were identified, but it is not a current admission surface.

Current tool/function status belongs in [[specs/codex-ratchet/tool-function-receipt-status|Tool Function Receipt Status]]. Current tool-role candidate/blocked counts belong in [[specs/codex-ratchet/sim-estate-integration-status|Sim Estate Integration Status]]. Current lego/sim contract rules belong in [[specs/codex-ratchet/lego-sim-contract-current|Lego Sim Contract Current Mirror]].

## Role in the Live Wiki Cluster
*   **Strongest Use:** Derived reference. Load this page to find proposed tool x lego-family pairings, then verify against the exact receipt and current specs mirror before using the row.
*   **Weak Use:** Qualitative description or general software installation guides.
*   **Authority Boundary:** Derived state view. It does not promote a lego, coupling, bridge, axis, GStack, QIT, engine, or target-system claim by itself.

---

## 1. Definition of Lego Families
Lego families partition strictly based on their prefix, docstring, and mathematical targets:
*   `Hopf`: Hopf fibration, Hopf torus, Hopf fibers, and nested Hopf tori ($S^3 \to S^2$).
*   `Weyl`: Weyl spinors, Weyl geometry, and Weyl chiral loops.
*   `Cl3` / `Cl6`: Clifford Algebras ($Cl(3,0)$ and $Cl(6,0)$) and Spin groups ($SU(2)$ double cover).
*   `Gtower`: G-structure towers, reductions, and obstructions.
*   `Spec3`: Spectral triples (candidate name: `spectral_triple`) — *currently fully empty (high-priority backlog)*.
*   `Gerbe`: Gerbe structures — *currently empty for load-bearing tools*.
*   `Assoc`: Associated vector bundles.
*   `FEP`: Variational Free Energy Principle active inference models.
*   `SzC`: Thermodynamic cycles (Szilard and Carnot engines) under non-commutation constraints ($[O, T] \neq 0$).
*   `F01` / `N01`: The two root constraints, Finitude and Noncommutation.
*   `L0-19`: Layer coupling matrices and multi-complex state spaces.
*   `Bridge`: High-level cross-layer integration.
*   `Holo`: Projective Holodeck recall and predictive coding spaces.
*   `Axis0`: The foundational gradient $\nabla I_c$ of the constraint manifold.

---

## 2. Integration Matrix

*A cell represents the representative on-disk load-bearing simulation path; "—" indicates an empty cell (backlog).*

| Tool | Hopf | Weyl | Cl3 | Cl6 | Gtower | Spec3 | Gerbe | Assoc | FEP | SzC | F01 | N01 | L0-19 | Bridge | Holo | Axis0 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **numpy** | *baseline* | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| **pytorch** | `sim_hopf_torus_lego` | `sim_weyl_nested_shell` | — | — | — | — | — | — | — | — | `sim_axiom_f01_finite_hilbert_dim` | `sim_axiom_n01_composition_order` | `sim_layer_coupling_matrix_v3` | — | — | `sim_torch_deep_axis0_autograd` |
| **sympy** | — | — | — | — | — | — | — | — | `sim_fep_generative_model_as_shell` | — | `sim_axiom_f01_quotient_well_defined` | `sim_axiom_n01_identity_via_indist_` | — | — | — | — |
| **z3** | `sim_hopf_foliation_structure` | `sim_weyl_geometry_proof_pressure` | — | — | `sim_gtower_reduction_z3` | — | — | — | `sim_fep_pair_free_energy_coupling` | `sim_qit_szilard_landauer_cycle` | `sim_axiom_f01_finite_measurement` | `sim_axiom_n01_indiscernibility_` | `sim_L2_eight_stages` | `sim_qit_weyl_carnot_bridge` | `sim_holodeck_distinguishability` | — |
| **cvc5** | — | — | — | — | — | — | — | — | — | — | — | — | — | `sim_bridge_cvc5_crosscheck` | — | — |
| **clifford** | `sim_hopf_torus_lego` | `sim_weyl_nested_shell` | `sim_cl3_basis` | `sim_cl6_basis` | — | — | — | — | — | — | — | — | `sim_layer_coupling_matrix_v2` | — | — | — |
| **e3nn** | `sim_density_hopf_geometry` | — | — | — | — | — | — | — | — | — | — | — | — | `sim_axis6_e3nn_fe_bridge` | — | — |
| **geomstats** | `sim_foundation_hopf` | `sim_weyl_nested_shell` | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| **pyg** | `sim_pyg_deep_hopf` | — | — | — | — | — | — | — | — | — | — | — | `sim_geometric_manifold_pyg` | — | — | — |
| **rustworkx** | — | `sim_weyl_geometry_graph` | — | — | — | — | — | — | — | `sim_carnot_graph_proof_alignment` | — | — | `sim_layer_coupling_matrix` | `sim_rustworkx_bridge_dag` | — | — |
| **toponetx** | `sim_toponetx_hopf_crosscheck` | — | — | — | — | — | — | — | — | — | — | — | `sim_toponetx_constraint_shells` | `sim_toponetx_bridge_seam` | — | — |
| **gudhi** | `sim_gudhi_deep_s3_hopf_torus` | `sim_weyl_nested_shell` | — | — | — | — | — | — | — | — | — | — | — | `sim_persistence_geometry` | — | — |
| **xgi** | — | — | — | — | — | — | — | — | — | — | — | — | `sim_xgi_shell_hypergraph` | — | — | `sim_xgi_gradient_ascent` |
| **networkx** | — | — | — | — | — | — | — | — | — | — | — | — | — | — | `sim_leviathan_as_civil_shell` | — |

---

## 3. Ablation Audit of 8 Deep-Integration Sims
The "Ablation Audit" tests whether replacing the named library with a simple numpy stub collapses the simulation's *admissibility claim* (not just the numerical calculation). This separates truly load-bearing tools from those used decoratively as wrappers:

*   **z3** (`sim_z3_deep_no_classical_stochastic_under_dephasing_weyl_commute.py`):
    - *Ablation Verdict:* **TRUE load-bearing**.
    - *Reason:* The claim is an UNSAT structural impossibility over a 4×4 row-stochastic circulant surrogate. The z3 `prove/unsat` is the admissibility statement; a numpy stub can only sample, completely evaporating the exclusion claim.
*   **sympy** (`sim_sympy_deep_lindblad_dephasing_spectrum.py`):
    - *Ablation Verdict:* **TRUE load-bearing**.
    - *Reason:* The admissibility boundary is defined as the exact locus $\gamma_\phi = -\gamma_1 / 2$ derived in closed symbolic form. A numerical solver only approximates the boundary, failing to prove exactness or identify degeneracy.
*   **clifford** (`sim_clifford_deep_cl3_rotor_double_cover.py`):
    - *Ablation Verdict:* **TRUE load-bearing**.
    - *Reason:* The double-cover identity $R v \tilde{R} = (-R) v (-\tilde{R})$ while $R \neq -R$ is meaningful only inside the geometric algebra where $R$ and $-R$ are distinct Spin(3) elements. A numpy matrix representation erases the sign, collapsing the 2-to-1 claim.
*   **pytorch** (`sim_torch_deep_axis0_autograd_vn_entropy.py`):
    - *Ablation Verdict:* **TRUE load-bearing (but narrow)**.
    - *Reason:* The claim is that autograd reproduces $dS/d\theta = 0$ through complex matrix exponentiation and eigenvalues. A numpy finite-difference stub would yield numerical approximations, but the doctrinal claim requires a backward-pass through the complex exponential.
*   **pyg** (`sim_pyg_deep_hopf_u1_equivariant_conservation.py`):
    - *Ablation Verdict:* **FALSE (decorative)**.
    - *Reason:* The update rule is a linear symmetric aggregation; charge conservation and $U(1)$ equivariance follow from arithmetic, not PyG's `MessagePassing.propagate()`. A 10-line numpy edge-loop reproduces the same conservation and equivariance.
*   **rustworkx** (`sim_rustworkx_deep_cayley_s4_admissibility.py`):
    - *Ablation Verdict:* **TRUE load-bearing**.
    - *Reason:* Uses `cycle_basis`, `is_isomorphic` (VF2), `max_flow`, and `node_connectivity`. These non-trivial graph algorithms cannot be reproduced by a simple numpy stub without completely rewriting the library.
*   **toponetx** (`sim_toponetx_deep_hodge_boundary.py`):
    - *Ablation Verdict:* **PARTIALLY TRUE (weak load-bearing)**.
    - *Reason:* Boundary-of-boundary $B_{k-1} B_k = 0$ and the Hodge Laplacian are mathematical properties of any correctly-constructed incidence matrix. TopoNetX is load-bearing for the *construction* of the CellComplex, but decorative for the *proof*.
*   **gudhi** (`sim_gudhi_deep_s3_hopf_torus_persistent_homology.py`):
    - *Ablation Verdict:* **TRUE load-bearing**.
    - *Reason:* Rips filtration and SimplexTree persistent Betti calculations are non-trivial algebraic topology algorithms. A numpy stub cannot calculate persistent Betti numbers without reimplementing GUDHI.

---

## 4. Key Backlogs and Gaps

1.  **SpectralTriple Column is Fully Empty:** No tool-stage or lego-stage carrier simulation has been written for spectral triples (no `spectral_triple` file matches in the probes directory). This is the highest-value single backlog.
2.  **Gerbe Column Gaps:** While five gerbe simulations exist, none declare a load-bearing tool. They remain classical numpy-only cochain arithmetic.
3.  **AssocBundle Column Gaps:** Six associated bundle simulations exist, but none utilize a load-bearing tool.
4.  **Decorative PyG & Weak TopoNetX:** The PyG and TopoNetX deep simulations must be upgraded to target non-trivial, non-linear, or complex boundary calculations that numpy stubs cannot hand-encode, satisfying the strict load-bearing tool requirement.

---

## Related Pages
*   [[tool-capability-and-integration-ledger]] ── lists all 22 core tools and their capabilities.
*   [[repo-tool-use-router]] ── acceptable and unacceptable uses of tools in the wiki.
*   [[anomalous-computer-science-translation]] ── computer-science translation of local terms.
