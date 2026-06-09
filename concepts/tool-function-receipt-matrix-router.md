---
title: Tool Function Receipt Matrix Router
created: 2026-05-18
updated: 2026-05-21
type: concept
tags: [simulation, tooling, proof, harness, research]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/TOOL_FUNCTION_RECEIPT_MATRIX.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/evidence/tool_function_receipt_matrix.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/scripts/tool_function_receipt_matrix.py
framing: status_router_snapshot
spec_mirror: specs/codex-ratchet/tool-function-receipt-status
---

# Tool Function Receipt Matrix Router

## Spec mirror
Current specs-side routing belongs in [[specs/codex-ratchet/tool-function-receipt-status|Tool Function Receipt Status]].

This concept page remains a row-ingestion router for tool reference pages. Do not treat it as an admission or promotion surface.

## Status boundary
This page routes the repo tool-function receipt matrix. The matrix boundary says: receipt index only. This does not admit, promote, or validate a lego, coupling, bridge, axis, GStack, QIT, or engine claim.

Role values are matrix metadata only. They are not executable sim labels and must not be used to generate sim filenames.

## Dated generated snapshot
From `system_v5/docs/TOOL_FUNCTION_RECEIPT_MATRIX.md`, generated `2026-05-17T23:28:08.506315+00:00`:

- Rows: `108`
- Passing rows: `108`
- Missing receipts: `0`
- Explicit receipt schemas missing: `108`
- Receipt contract shapes unresolved: `0`
- Candidate spec complete rows: `97`
- Candidate spec incomplete rows: `11`

The `explicit receipt schemas missing` count is a boundary fact, not by itself a failure of the matrix.

## Tool/function surfaces covered
The matrix gives exact function/API surfaces for tools including:

- z3 and cvc5 for SMT/falsifier and cross-solver checks.
- SymPy for exact symbolic witnesses.
- PyTorch/torch/autograd for tensor, density, gradient, and neural readouts.
- PyG/torch_geometric for graph data, batching, validation, MessagePassing, and pooling.
- Clifford for geometric algebra, rotor, spin, and chirality receipts.
- GUDHI for persistence and filtrations.
- TopoNetX/XGI for cell-complex, simplicial, and hypergraph surfaces.
- rustworkx/NetworkX for graph/DAG/reachability/path surfaces.
- QuTiP/Qiskit/scipy/quimb/opt_einsum/e3nn/geomstats/cotengra for bounded tool-role surfaces.

## Scope difference from the legacy tool manifest audit
[[tool-manifest-audit]] is a 2026-04-10 audit of `system_v4/probes/` and its result-template adoption. This page is a 2026-05-17 router for exact function/API receipt rows. Do not overwrite the older counts with this matrix; keep both surfaces with their different scopes.

## Canonical-by-process fence
Classification fields in the matrix (`canonical`, `classical_baseline`, `tool_lego_fit_probe`) are matrix metadata for receipt rows, not a reason to promote downstream sims. Canonical-by-process still requires the relevant sim/result contract, fresh evidence path, and claim ceiling.

## Row-level consumption pattern
The newly deepened tool reference pages should feed this matrix one row at a time. The safe pattern is:

1. Choose one tool/function row from the matrix, not an entire tool family.
2. Open the receipt named in the row and preserve these fields: `classification`, `claim_ceiling`, `promotion_allowed` if present, `tool_manifest`, `tool_integration_depth`, positive/negative controls, and boundary/out-of-scope text.
3. Link the row to the relevant tool reference page.
4. State what the row is allowed to witness and what it cannot promote.
5. Do not rewrite row roles as sim labels or new filenames.

A row is a routing witness. It is not a result-promotion event.

## Tool reference pages now ready to consume rows
These pages have been upgraded from thin references into role/receipt-boundary pages and can now absorb row-level matrix work:

| Tool page | Matrix row families to process next | Claim ceiling to preserve |
|---|---|---|
| [[geomstats-manifold-geometry-reference]] | manifold operations, S3/S2 membership, geodesic/metric witnesses, geomstats + Clifford/SymPy/Z3 scouts | tool/function or formal-scout support only unless a current gate earns more |
| [[clifford-geometric-algebra-reference]] | Cl(3)/Cl(6)/Cl(1,3), pseudoscalar/gamma5, rotor/spin/chirality, Clifford-Weyl integration | algebra/chirality witness only; no bridge/axis/engine promotion |
| [[e3nn-equivariant-geometry-reference]] | Irreps, tensor products, spherical harmonics, e3nn/PyG equivariance | symmetry witness only; no final neural architecture or manifold ontology |
| [[xgi-hypergraph-reference]] | hyperedge membership, incidence matrices, shared/unshared hyperedge controls, XGI/TopoNetX incidence | higher-arity carrier witness only; no nonclassical/bridge claim |
| [[rustworkx-graph-algorithms-reference]] | DAG reachability, cycle basis, graph reduction, path/cut/endpoint controls | pairwise graph/dependency witness only; no topology closure |
| [[toponetx-topological-complex-reference]] | cell incidence, Hodge Laplacian, rank/cell-complex fixtures, XGI/TopoNetX mapping | cell-complex witness only; no final topology |
| [[gudhi-persistent-topology-reference]] | simplex persistence, alpha/Rips complexes, Betti/barcode/lifetime rows | persistence witness only; no ontology closure |
| [[pytorch-geometric-reference]] | MessagePassing, batching, graph roundtrip, e3nn/PyG equivariance rows | graph+tensor operation only; no target-system or QIT bridge promotion |

## Near-term row queue
The next useful wiki work is not more broad tool prose. It is receipt-row ingestion. Good first rows:

1. Completed: `sim_integration_e3nn_pyg_equivariance_under_mp_micro_results.json` → [[e3nn-pyg-equivariance-message-passing-row]]; ties [[e3nn-equivariant-geometry-reference]] to [[pytorch-geometric-reference]] while preserving `tool_integration_micro_only`.
2. Completed: `sim_integration_xgi_toponetx_higher_order_incidence_micro_results.json` → [[xgi-toponetx-higher-order-incidence-row]]; ties [[xgi-hypergraph-reference]] to [[toponetx-topological-complex-reference]] while preserving `tool_integration_micro_only`.
3. Completed: `sim_gudhi_rips_point_cloud_micro_results.json` → [[gudhi-rips-point-cloud-persistence-row]]; gives [[gudhi-persistent-topology-reference]] a row-level persistence example while preserving `tool_function_micro_only`.
4. Completed: `sim_rustworkx_dag_reachability_micro_results.json` → [[rustworkx-dag-reachability-row]]; gives [[rustworkx-graph-algorithms-reference]] a clean graph-reachability row while preserving `tool_lego_fit_probe_only`.
5. `sim_toponetx_hodge_laplacian_micro_results.json` — gives [[toponetx-topological-complex-reference]] a Hodge/cell-complex row.

Each row should become either a small section on this page or a dedicated row-ledger page if the matrix starts getting too long.

## Matrix-to-wiki anti-collapse rules
- Mention count is not installation.
- Installation is not callable use.
- Callable use is not load-bearing use.
- Load-bearing use is not result promotion.
- A passing row is not a bridge.
- A tool-function receipt is not a lego coupling unless the row and its result contract explicitly say so.
- Provider/model agreement is not matrix evidence.

## Related pages
- [[repo-tool-use-router]]
- [[sim-run-catalogue-and-result-family-router]]
- [[tool-manifest-audit]]
- [[tooling-status]]
- [[z3-smt-solver-reference]]
- [[cvc5-smt-and-sygus-reference]]
- [[gudhi-persistent-topology-reference]]
- [[clifford-geometric-algebra-reference]]
- [[rustworkx-graph-algorithms-reference]]
- [[networkx-graph-structure-reference]]
- [[toponetx-topological-complex-reference]]
- [[xgi-hypergraph-reference]]
- [[pytorch-geometric-reference]]
- [[e3nn-equivariant-geometry-reference]]
- [[geomstats-manifold-geometry-reference]]
- [[sympy-symbolic-math-reference]]
