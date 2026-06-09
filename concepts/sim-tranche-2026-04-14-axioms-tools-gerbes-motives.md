---
title: 2026-04-14 Sim Tranche — Axioms, Tool Depth, Gerbes, G-Tower, Motives, and Clifford Micro-Sims
created: 2026-04-14
updated: 2026-05-21
type: summary
framing: historical_tranche_source_present_result_partial_snapshot
tags: [simulation, results, formal-methods, geometry, tooling, audit]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/00_manifest.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_f01_finite_measurement_set.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axiom_n01_pauli_algebra_closure.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_pyg_deep_hopf_u1_equivariant_conservation.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_sympy_deep_lindblad_dephasing_spectrum.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_gerbe_structure_b_field_cochain.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_gtower_full_chain.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_motives_1_carrier.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_motives_6_chirality_coupling.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_cl6_chirality.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/results/sim_cl6_chirality.json
missing_result_receipts:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_f01_finite_measurement_set_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_n01_pauli_algebra_closure_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_pyg_deep_hopf_u1_equivariant_conservation_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sympy_deep_lindblad_dephasing_spectrum_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gerbe_structure_b_field_cochain_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gtower_gl_to_o_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_motives_1_carrier_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_motives_6_chirality_coupling_results.json
---

# 2026-04-14 Sim Tranche — Axioms, Tool Depth, Gerbes, G-Tower, Motives, and Clifford Micro-Sims

## 1. Tranche snapshot

A large historical sim tranche landed in `system_v4/probes/` and was described as having result-artifact surfaces.

In this 2026-05-21 source-path pass, many of the old exact result JSON names cited by this page were not found in the current checkout. Treat this page as a historical tranche/source map until result paths are restored, relinked, or rerun.

Why the label stays there:
- I audited the listed source paths and exact old result receipt names.
- I did not rerun the new probes in this pass.
- Several source scripts are still present, but most old result receipt names in frontmatter are missing.
- Any internal `pass`, `all_pass`, `overall_pass`, `status`, or `classification` fields must be read from current receipts before they are reused.

The main new survivor clusters are:
1. F01/N01 axiom micro-sims
2. deep tool-native claim sims
3. gerbe-family legos
4. G-tower reduction-chain sims
5. motives-family six-step packet
6. standalone Cl(3) / Cl(6) micro-sims

One informative divergence was cited in the historical tranche:
- `system_v4/probes/a2_state/sim_results/sim_gudhi_deep_s3_hopf_torus_persistent_homology_results.json` was described as a GUDHI deep artifact with `all_pass: false`.
- That exact current JSON was not relinked in this source-path pass.
- Preserve the split as a dated claim until the exact current receipt or a nearby candidate is verified.

## 2. Math worked out in this tranche

### A. Root-axiom micro-sims
The new axiom packet makes the two root constraints more explicit as bounded executable objects.

F01-side micro-sims were recorded with old result receipt names for:
- finite state set
- finite measurement set
- finite Hilbert dimension
- quotient well-definedness

N01-side micro-sims were recorded with old result receipt names for:
- generic noncommutation
- composition-order distinction
- identity via indistinguishability
- indiscernibility implies identity
- Pauli algebra closure as a joint F01+N01 carrier instance

### B. Deep tool-native claim sims
A second packet pushes specific tools into deeper bounded claims rather than shallow capability declaration.

Representative new probe files exist for:
- PyG Hopf/U(1) equivariant conservation
- SymPy Lindblad dephasing spectrum
- rustworkx Cayley S4 admissibility
- z3 no-classical-stochastic-under-dephasing/Weyl-commute fence
- GUDHI S3/Hopf-torus persistent homology
- torch deep Axis-0 autograd/von-Neumann-entropy

### C. Gerbe family
A gerbe-side packet is present as bounded steps rather than only as scattered higher-order geometry language.

The dated tranche recorded artifacts for:
- carrier/cell-complex side
- B-field/cochain structure
- reduction/coboundary side

### D. G-tower family
A G-tower reduction lane was recorded in this tranche, but the exact current artifact layer is better described through newer ordering and reduction result files than the specific three result filenames listed here:
- GL -> O
- O -> SO
- SO -> U

The `sim_gtower_full_chain.py` file also exists as the broader composition/probe surface.

### E. Motives family
A six-step motives lane was recorded in this tranche, but this page should treat the exact result-artifact census as dated until the current motives result files are re-linked:
1. carrier
2. structure
3. reduction
4. admissibility
5. distinguishability
6. chirality coupling

### F. Standalone Clifford micro-sims
Separate Cl(3) and Cl(6) micro-sims were recorded as separated result surfaces for:
- basis
- rotor product
- bivector exponential / reflection / composition / invariants on Cl(3)
- basis / rotor product / spin-group embedding / chirality on Cl(6)

## 3. Tranche translation

In controller terms, this tranche is not one big "theory advance."
It is a widening of the bounded object inventory.

The main translation is:
- axioms became executable micro-legos
- tool pressure became deeper claim-local packets
- higher-order geometry families (gerbes, G-tower, motives) moved from broad naming toward stepwise packets
- standalone Clifford surfaces were separated into tiny basis/product/chirality probes instead of staying implicit inside larger pages

That is aligned with the repo's lower-first discipline:
- tiny local objects first
- bounded family steps second
- larger bridge language only later

## 4. What is already earned

| Claim | Evidence path(s) | Artifact-side classification/field | Safe public label in this maintenance pass |
|---|---|---|---|
| The tranche recorded an F01/N01 axiom micro-sim packet | exact current result-artifact paths should be refreshed before this row is read as a live artifact census | dated tranche claim rather than a re-linked live artifact row | source-present / result-link-partial |
| The tranche recorded a deep tool-native packet across PyG/SymPy/rustworkx/z3/GUDHI/torch | exact current result-artifact links for that row need refreshing | dated tranche claim rather than a re-linked live artifact row | source-present / result-link-missing until relinked |
| Gerbe family was recorded as a bounded packet | old gerbe result filenames are currently missing from the exact cited result surface | source-present / result-link-missing until relinked | source-present |
| The tranche recorded a G-tower reduction packet | the live artifact layer should now be referenced through the currently visible G-tower result files rather than the three filenames listed in this row | dated tranche claim rather than a re-linked live artifact row | source-present / current candidate unresolved |
| The tranche recorded a motives six-step packet from carrier through chirality coupling | the exact current result-artifact links for that family need refreshing before this row is read as live artifact truth | dated tranche claim rather than a re-linked live artifact row | source-present / result-link-missing |
| Standalone Cl(3)/Cl(6) micro-sims were recorded as separated result surfaces | `system_v4/probes/results/sim_cl3_*.json`, `system_v4/probes/results/sim_cl6_*.json`; only the cited `sim_cl6_chirality.json` path is directly listed in current sources | sampled fields must be reread from current receipts before reuse | result-link-partial |

## 5. What is still open

1. Repo ledgers have not yet been reconciled to this tranche in the same pass.
   - `system_v5/docs/16_lego_build_catalog.md`
   - `system_v5/docs/17_actual_lego_registry.md`

2. The public wiki still lacks dedicated current pages for these new families:
   - gerbes
   - G-tower reduction chain
   - motives packet
   - executable root-axiom micro-sims as a cluster

3. The controller has not freshly rerun these probes in this pass, so the new artifacts stay below `runs` or `passes local rerun` here.

4. Most exact old result names cited by this page are missing in the current checkout. The next repair is receipt relinking or bounded rerun, not summary-level smoothing.

5. The deep-tool packet's cited GUDHI split needs a later bounded rerun/audit lane or exact receipt relink before it is treated as current evidence.

## 6. One next bounded rerun lane

One plausible next bounded controller rerun/audit lane:
- `system_v4/probes/sim_gudhi_deep_s3_hopf_torus_persistent_homology.py`
- artifact: `system_v4/probes/a2_state/sim_results/sim_gudhi_deep_s3_hopf_torus_persistent_homology_results.json`

Why this one:
- it sits inside the new deep-tool packet
- the historical tranche described it as the most explicit internal divergence (`all_pass: false`)
- it connects directly to the active geometry/Hopf lane rather than opening a totally separate doctrine surface

## 7. Optional dependencies

Optional follow-on surfaces after the bounded rerun/audit lane:
- `[[tooling-status]]` if the rerun changes how the GUDHI deep lane should be described
- `[[actual-lego-registry]]` and `[[lego-build-catalog]]` if the new families are promoted into the public inventory
- dedicated public concept pages for gerbes, G-tower reduction, and motives only after a bounded routing decision is made
