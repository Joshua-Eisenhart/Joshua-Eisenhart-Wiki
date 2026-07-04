---
title: Tool Capability and Integration Ledger
created: 2026-04-14
updated: 2026-05-21
type: concept
tags: [ledger, tools, integration, capability, z3, cvc5, pyg, toponetx, e3nn, geomstats, rustworkx]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/TOOL_CAPABILITY_AND_INTEGRATION_LEDGER.md
  - system_v5/docs/plans/plans/TOOL_CAPABILITY_AND_INTEGRATION_LEDGER.md
framing: derived_historical_tool_ledger
spec_mirrors:
  - specs/codex-ratchet/tool-function-receipt-status
  - specs/codex-ratchet/sim-estate-integration-status
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Tool Capability and Integration Ledger

## Overview
This dated derived ledger tracks capability probes, integration status, and load-bearing depth for core and extension tools in the Codex Ratchet research pipeline. It is useful for routing and row-level review, but it is not the definitive current authority for admission.

Current tool/function status belongs in [[specs/codex-ratchet/tool-function-receipt-status|Tool Function Receipt Status]]. Current tool-role candidate/blocked counts belong in [[specs/codex-ratchet/sim-estate-integration-status|Sim Estate Integration Status]].

## Role in the Live Wiki Cluster
*   **Strongest Use:** Verification and routing ledger for tool capability and integration. Load this page to locate candidate evidence for a specific tool API surface or tool-tool coupling before checking the current spec mirrors and exact receipts.
*   **Weak Use:** High-level narrative theory or code implementation tutorials.
*   **Authority Boundary:** Derived state view. It is built from on-disk Python capability files (`system_v4/probes/sim_capability_*.py`) and verified JSON output artifacts, but it does not promote a tool function, lego, coupling, bridge, axis, or engine claim by itself.

---

## 1. Ground Rules for Tool-Stage Admissibility

1.  **Granularity of Proof:** A ledger row is never a blanket proof of a whole library. Every capability or integration claim is strictly scoped to the exact function/API surface and test shape named by its probe.
2.  **Micro-Receipt Prerequisite:** Before a tool function can be used as load-bearing in a lego-stage claim or a tool-tool coupling, it requires a micro-receipt:
    - one specific function/API surface
    - one bounded lego target or minimal fixture
    - one positive test case
    - one negative test case
    - one boundary test case
    - one explicit demotion condition
3.  **Tool-Lego Fit Probes:** Probes exploring how a tool fits a lego are pre-lego evidence only; they do not promote the lego to a higher truth-label.

---

## 2. Core 22-Tool Ledger

| Tool | Capability Probe File | Capability Probe Status | Integration Sims Count | Integration Depth | Next Step / Completed Receipts |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **z3** | `sim_z3_capability.py` | passes local rerun (2026-04-19) | 3 | load_bearing confirmed for existing anchors plus the narrow QF_LIA agreement micro | Micro receipt DONE: `sim_z3_qf_lia_unsat_witness_micro.py` (SolverFor 'QF_LIA' SAT/UNSAT fixtures). Integration micro DONE: `sim_integration_cvc5_z3_unsat_agreement_micro.py` (5/5, z3: load_bearing). Next: keep additional SMT surfaces separate. |
| **cvc5** | `sim_cvc5_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed for parity/fence proofs and narrow QF_LIA agreement | Micro receipts DONE: `sim_cvc5_qf_lia_model_extraction_micro.py` (checkSat/getValue) and `sim_cvc5_sygus_synthesis_micro.py` (SyGuS LIA). Integration micro DONE: `sim_integration_cvc5_z3_unsat_agreement_micro.py`. |
| **sympy** | `sim_sympy_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (dedicated integration reran cleanly 2026-04-18) | Micro receipts DONE: `sim_sympy_matrix_identity_micro.py` (2x2 inversion) and `sim_sympy_symbolic_identity_micro.py` (calculus and simplification). Next: keep invariant-search as anchor. |
| **clifford** | `sim_clifford_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (rotor double-cover and spinor chirality probes) | Micro receipts DONE: `sim_clifford_rotor_norm_micro.py` (MultiVector product and rotor sandwich) and `sim_clifford_spinor_double_cover_micro.py` (Cl(3) same-vector sandwich). |
| **e3nn** | `sim_e3nn_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed for equivariance/SO(3) irreps and e3nn-PyG message equivariance | Micro receipts DONE: `sim_e3nn_irreps_tensor_product_micro.py` (Irreps tensor product) and `sim_e3nn_spherical_harmonics_equivariance_micro.py` (SO(3) spherical harmonics). Integration micro DONE: `sim_integration_e3nn_pyg_equivariance_under_mp_micro.py`. |
| **pyg** | `sim_pyg_capability.py` | passes local rerun (2026-04-19) | 3 | load_bearing confirmed for datasketch anchor, NetworkX handoff, e3nn equivariance, and PyG batching | Micro receipts DONE: `sim_pyg_message_passing_autograd_micro.py` (propagate with autograd) and `sim_pyg_batching_micro.py` (Batch.from_data_list). Integration micros DONE: `sim_integration_networkx_pyg_graph_roundtrip_micro.py` and `sim_integration_e3nn_pyg_equivariance_under_mp_micro.py`. |
| **toponetx** | `sim_toponetx_capability.py` | passes local rerun (2026-04-19) | 2 | load_bearing confirmed for CellComplex rank-2 incidence, Hodge-Laplacian, and XGI-TopoNetX agreement | Micro receipts DONE: `sim_toponetx_cell_incidence_micro.py` (rank-2 cell add) and `sim_toponetx_hodge_laplacian_micro.py` (Hodge-Laplacian matrix). Integration micro DONE: `sim_integration_xgi_toponetx_higher_order_incidence_micro.py`. |
| **gudhi** | `sim_gudhi_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (persistent homology, Betti exclusion; `sim_gudhi_deep_s3_hopf_torus_persistent_homology.py` passed) | Micro receipts DONE: `sim_gudhi_simplex_persistence_micro.py` (simplex tree), `sim_gudhi_rips_point_cloud_micro.py` (Rips persistent S), and `sim_gudhi_alpha_complex_micro.py` (Alpha complex). |
| **rustworkx** | `sim_rustworkx_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (DAG/SCC admissibility, Cayley graph probes) | Micro receipts DONE: `sim_rustworkx_dag_reachability_micro.py` (DAG descendants/ancestors) and `sim_rustworkx_cycle_basis_micro.py` (cycle basis over non-DAGs). |
| **geomstats** | `sim_geomstats_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (Frechet mean, SO(3) geodesic, Stiefel probes; `sim_foundation_hopf_torus_geomstats_clifford.py` passed) | Micro receipts DONE: `sim_geomstats_so3_distance_micro.py` (SO(3) intrinsic distance) and `sim_geomstats_so3_log_exp_micro.py` (SO(3) exp/log map branches). |
| **xgi** | `sim_xgi_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed for hypergraph node/edge incidence and XGI-TopoNetX two-triad agreement | Micro receipt DONE: `sim_xgi_hypergraph_incidence_micro.py` (hypergraph node/edge membership). Integration micro DONE: `sim_integration_xgi_toponetx_higher_order_incidence_micro.py`. |
| **networkx** | `sim_networkx_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed only for DiGraph node/edge extraction and incoming-neighbor message sums | Integration micro DONE: `sim_integration_networkx_pyg_graph_roundtrip_micro.py` (verifies exact node/edge mapping and isolated nodes). Next: keep graph algorithms separate. |
| **numpy** | `sim_numpy_capability.py` | passes local rerun (2026-04-19) | 0 | superficial (baseline numeric substrate; torch is load-bearing by doctrine) | Classical baseline only; no dedicated integration sim required. |
| **pytorch / autograd** | `sim_pytorch_capability.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (gradient I_c via autograd; Axis 0 gradient probes) | Micro receipts DONE: `sim_pytorch_autograd_gradient_micro.py` (second-order gradients) and `sim_pytorch_density_entropy_gradient_micro.py` (autograd over eigvalsh density entropy). |
| **ribs** | `sim_capability_ribs_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (CMAME/QD grid archive) | Run isolated capability fresh; keep z3 archive integration (`sim_integration_ribs_z3_constraint_archive.py`) as the current anchor. |
| **deap** | `sim_capability_deap_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed for DEAP evolutionary genome and DEAP×Clifford rotor evolution | Ledger-only reconciliation `manifest_repair_deap` completed 2026-05-02. Evidence: `sim_deap_evolve_sim_genome_results.json` and `sim_integration_deap_clifford_rotor_evolution_results.json`. |
| **evotorch** | `sim_capability_evotorch_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed for EvoTorch SNES and EvoTorch×PyTorch autograd search | Ledger-only reconciliation `manifest_repair_evotorch` completed 2026-05-02. Evidence: `sim_evotorch_es_constraint_search_results.json` and `sim_integration_evotorch_autograd_constraint_search_results.json`. |
| **datasketch** | `sim_capability_datasketch_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (LSH / MinHash graph extraction) | Run isolated capability fresh; keep PyG LSH graph integration (`sim_integration_datasketch_pyg_lsh_graph.py`) as anchor. |
| **pymoo** | `sim_capability_pymoo_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed for Pymoo NSGA-II and Pymoo×GUDHI Pareto-persistence | Ledger-only reconciliation `manifest_repair_pymoo` completed 2026-05-02. Evidence: `sim_capability_pymoo_isolated_results.json` and `sim_integration_pymoo_gudhi_pareto_persistence_results.json`. |
| **hypothesis** | `sim_capability_hypothesis_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (metamorphic fuzzing) | Run isolated capability fresh; keep z3 property guard integration (`sim_integration_hypothesis_z3_property_guard.py`) as anchor. |
| **optuna** | `sim_capability_optuna_isolated.py` | passes local rerun (2026-04-19) | 1 | load_bearing confirmed (hyperparameter search) | Run isolated capability fresh; keep sympy invariant search integration (`sim_integration_optuna_sympy_invariant_search.py`) as anchor. |
| **hdbscan** | `sim_capability_hdbscan_isolated.py` | passes local rerun (2026-04-19) | 2 | load_bearing confirmed for named density clustering | Ledger-only reconciliation `truth_reconcile_hdbscan` completed 2026-05-02. Evidence: `sim_capability_hdbscan_isolated_results.json`, `sim_integration_hdbscan_constraint_clustering_results.json`, and `sim_hdbscan_umap_verdict_clustering_results.json`. |
| **umap** | `sim_capability_umap_isolated.py` | passes local rerun (2026-04-19) | 2 | load_bearing confirmed for named low-dimensional projections | Ledger-only reconciliation `truth_reconcile_umap` completed 2026-05-02. Evidence: `sim_capability_umap_isolated_results.json`, `sim_integration_umap_gtower_projection_results.json`, and `sim_hdbscan_umap_verdict_clustering_results.json`. |

---

## 3. Extension Tool Normalization: Qiskit / QuTiP / SciPy

These tools were surfaced or integrated after the main 22-tool ledger structure was finalized. They are normalized here to ensure visibility to tool-lego planning, scoped strictly to the named receipt paths below:

*   **qiskit:**
    - *Evidence:* `tool_capability_qiskit_results.json` (`classification: canonical`, `summary.all_pass: true`).
    - *Scope:* Circuit construction, statevector evaluation, density matrices, partial trace, and Pauli expectation checks.
    - *Role:* Nonclassical/QIT tool-stage capability. Load-bearing only for the named functions; does not prove broad axis or engine claims.
*   **qutip:**
    - *Evidence:* `tool_capability_qutip_results.json` (`classification: canonical`, `summary.all_pass: true`).
    - *Scope:* Qobj construction, operator application, expectation evaluation, and capability-gated input validation.
    - *Role:* Nonclassical/QIT and open-system support capability. Load-bearing only for the named functions.
*   **qiskit x qutip x clifford Bell surface:**
    - *Evidence:* `sim_integration_qiskit_qutip_clifford_bell_bridge_results.json` (`classification: canonical`, `summary.all_pass: true`, with qiskit, qutip, and clifford load-bearing).
    - *Scope:* Bounded integration micro over one Bell-state density/correlation surface.
    - *Role:* Nonclassical tool-integration micro; does not prove broad axis, engine, or coupling claims.
*   **qiskit x qutip x pytorch x z3 channel variants:**
    - *Evidence:* `sim_tier2_qiskit_qutip_channel_variant_probe_results.json` (`classification: canonical`, `summary.all_pass: true`, with all four tools load-bearing).
    - *Scope:* Below-axis tier-2 channel/tool evidence on 3q density witnesses and valid GStack order variants.
*   **qutip open-system baseline:**
    - *Evidence:* `qutip_open_system_bridge_results.json` (`classification: classical_baseline`, `qutip: load_bearing`).
    - *Scope:* Classical/bridge baseline for single-qubit amplitude-damping Lindblad evolution.
*   **scipy spectral baseline:**
    - *Evidence:* `sim_integration_scipy_spectral_eigenvalues_results.json` (`classification: classical_baseline`).
    - *Scope:* Classical/spectral bridge support for Dirac eigenvalue baseline. SciPy is load-bearing for `scipy.linalg.eigvalsh`.

---

## 4. Key Gaps Summary

1.  **As of the 2026-04-19 ledger snapshot, all 22 tools were reported to have a capability probe** that passed the local rerun used for that ledger. Standalone capability probes for `hdbscan` and `umap` were reported active and passing in that snapshot.
2.  **Unresolved or Zero Dedicated Integration Sims:** `numpy` remains baseline-only. All other 21 tools have dated canonical/load-bearing micro-integration receipts for their specific function surfaces. These receipts represent narrow agreement (such as cvc5-z3 QF_LIA, XGI-TopoNetX, or e3nn-PyG message-passing), not current maturity, broad solver equivalence, or generalized library couplings.
3.  **Manifest Debt Repaired:** Ledger-only reconciliation completed on 2026-05-02 for `deap`, `evotorch`, and `pymoo` to align their status with existing bounded results. Stale, failing standalone evidence remains quarantined.

---

## Related Pages
*   [[repo-tool-use-router]] ── maps tool surfaces to acceptable, bounded wiki roles.
*   [[tool-function-receipt-matrix-router]] ── lists raw receipt paths on disk.
*   [[anomalous-computer-science-translation]] ── computer-science ontology translation.
*   [[queries/five-framework-cluster|five-framework-cluster]] ── QIT engine and scientific-method connections.
