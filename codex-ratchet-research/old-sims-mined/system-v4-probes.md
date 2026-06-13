# system_v4/probes Mine

## 1. Scope and Evidence Boundary

This file mines `/Users/joshuaeisenhart/Codex-Ratchet/system_v4/probes/` as an old-estate object source. It is not a roadmap, not a promotion surface, and not a canonical sim registry. Objects below are reusable only as standard-math facts, negative controls, latent test intents, or exclusion candidates until a future v6 packet supplies fresh receipts.

Counts from static inspection:

| count | value |
|---|---:|
| total files inventoried under `system_v4/probes/` | 6626 |
| readable code/doc/result files inspected statically (`.py`, `.md`, `.json`, `.html`, `.sh`, `.toml`, `.plist`) | 4673 |
| Python files in the estate | 4290 |
| JSON files in the estate | 360 |
| result JSON files detected by name/path | 349 |
| named graveyard/negative/fail/open-failure items | 68 |
| Python files exposing `run_negative_tests`, `run_graveyards`, or designed-fail style hooks | 3070 |
| static never-run probe intents detected by missing same-stem result JSON | 3825 |
| ranked unconsumed objects recorded below | 12 |

Read-first sources used:

- `AGENTS.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/README.md`
- full file inventory under `system_v4/probes/`
- targeted source/result reads for engine-lab, Carnot, Szilard, graveyard batteries, tool fences, and representative never-run probes.

Evidence boundary:

- Old `system_v4/probes/` files were read only.
- No `system_v4/` or `system_v5/` files were edited.
- The target parent directory did not exist; only `/Users/joshuaeisenhart/wiki/codex-ratchet-research/old-sims-mined/` and this file were created.
- Result JSONs are treated as old receipts, not current truth.
- Any file without a matching result JSON is a latent intent, not an executed result.
- Any graveyard row that says `survived` remains local variant evidence only. It does not close its source row.
- Any row marked `qit_or_axis_promotion_allowed: false`, `promotion_allowed: false`, or equivalent remains blocked from promotion.

## 2. Standard-Math Facts Mined

These are standard-math facts or tool-surface facts the estate already encodes. They can seed future packets only under their stated hypotheses.

| object family | mined fact | evidence slice | boundary |
|---|---|---|---|
| Carnot two-bath cycle | The reversible Carnot efficiency identity is represented as `eta = 1 - Tc/Th`; super-Carnot and single-bath positive-work violators are rejected by z3 in local fences. | `sim_carnot_constraint_admissibility_fence.py`, `bridge_carnot_admissibility_fence_results.json`, `carnot_constraint_admissibility_fence_results.json` | Classical two-bath constraint fence only; no QIT, axis, bridge, or runtime-engine admission. |
| Szilard / Landauer | One unbiased bit carries `ln2` information; erasure floor equals `kBT ln2`; no-measurement, no-feedback, random-feedback, and no-erasure variants are explicit graveyards. | `sim_szilard_measure_feedback_erasure_landauer_bounds.py`, `bridge_landauer_erasure_bit_distinguishability_results.json`, `bridge_szilard_landauer_floor_results.json` | Classical calibration only until explicit state-update and feedback-cycle receipts exist. |
| Engine loop order | Loop ordering is load-bearing in the old engine core: normal order differs from reversed, swapped, and random order; swapped loop killed entanglement in the stabilization manifest. | `MASS_SIM_MANIFEST.md`, `STABILIZATION_MANIFEST.md`, `extended_graveyard_battery.py`, `neg_scrambled_sequence_sim.py` | Old engine behavior, not a v6 canonical order claim. Future sequence claims must rerun order tests separately. |
| CPTP / density operators | Density matrices must stay Hermitian, positive semidefinite, trace-one; CPTP violations are used as designed-fail controls. | `deep_graveyard_battery.py`, `sim_channel_cptp_classical.py`, `sim_choi_matrix_classical.py`, `sim_torch_channel_taxonomy.py` | Generic QIT baseline; no nonclassical witness by itself. |
| Noncommutation / Pauli exclusion | Simultaneous eigenstate claims for incompatible Pauli surfaces are treated as UNSAT/exclusion controls. | `STABILIZATION_MANIFEST.md`, `sim_z3_pauli_joint_commute.py`, `sim_z3_deep_no_classical_stochastic_under_dephasing_weyl_commute.py` | Use as falsifier for commutative collapse, not as a positive ratchet object. |
| Hopf base/fiber reconstruction | A Hopf carrier point can be recovered from a base section plus one fiber phase; wrong basepoint or wrong phase breaks recovery. | `sim_hopf_base_section_phase_recovery.py`, `hopf_manifold.py` | Shell-local Hopf packet only; no global topology or bridge promotion. |
| Clifford Spin(3) double cover | In `Cl(3)`, unit rotors `R` and `-R` have the same vector sandwich action, while non-unit even multivectors are excluded by norm/action gates. | `sim_clifford_spinor_double_cover_micro.py` | Tier-A Clifford tool-surface evidence only; pre-lego. |
| G-structure reduction | A GL candidate is admitted to an `O(g)` reduction only when `A^T g A = g`; shears and volume-scalers are excluded for fixed metrics. | `sim_gtower_gl_to_o_reduction.py` | Classical baseline metric-preservation fixture; no nonclassical promotion. |
| Hodge/Betti cross-check | TopoNetX Hodge kernel dimensions and GUDHI Betti numbers can cross-check torus/disk/sphere topology fixtures. | `sim_toponetx_gudhi_hodge_betti_cross.py` | Tool-tool topology parity intent; static run evidence was not found by same-stem result matching. |
| Category/SMT laws | Monad-law and algebraic-law probes encode positive SAT cases and violated-law UNSAT cases through cvc5-style constraints. | `sim_cvc5_monad_laws_constraint.py`, many `sim_cvc5_*_constraint.py` files | Logical law fixtures only; do not reify as ratchet structure. |

## 3. Graveyard / Negative Controls

Named graveyard/negative inventory:

- 68 named graveyard/negative/fail/open-failure items were found by path/name.
- 60 of those are Python source files.
- 8 are old result JSONs under `system_v4/probes/a2_state/sim_results/`.
- 3070 Python files expose negative-test or graveyard hooks; those are ambient designed-fail coverage, not all first-class graveyards.

Representative graveyard result totals:

| receipt | variants | killed | survived | source-row closure |
|---|---:|---:|---:|---|
| `carnot_asymmetric_direction_graveyard_results.json` | 10 | 7 | 3 | false |
| `szilard_open_failure_graveyard_results.json` | 9 | 4 | 5 | false |
| `engine_lab_sidecar_graveyard_results.json` | 6 | 2 | 4 | false |
| combined representative graveyard receipts above | 25 | 13 | 12 | false |

Best 5 designed-fail controls from this region:

| candidate | why killed | decisive condition | reusable designed-fail control |
|---|---|---|---|
| Super-Carnot efficiency / single-bath work | Violates the classical heat/work and second-law fence. | z3 returns UNSAT for super-Carnot or equal-temperature positive work while exact bound attainment remains SAT. | Use as a thermodynamic admission guard before any Carnot-adjacent packet is allowed to claim cycle gain. |
| Below-Landauer or free-erasure Szilard row | Treats information erasure as cheaper than `kBT I` or free at nonzero information. | z3 rejects `E_erase < kBT I`; no-erasure repeated cycles flag unpaid surplus. | Use as measurement-feedback-erasure floor control. |
| Scrambled / swapped engine loop order | Removes the order-sensitive loop grammar and kills or collapses the measured old-engine signal. | Reversed, swapped, or random order fails the same observable that normal order preserved in old stabilization runs. | Use as a mandatory order-falsifier; content-correctness is not order-correctness. |
| CPTP violation / non-positive trace map | Breaks density-operator admissibility by trace increase or non-positive evolution. | Density validity gate fails or negative battery classifies the row as KILL. | Use as the first QIT hygiene control before interpreting any channel result. |
| Wrong Hopf basepoint or wrong fiber phase | Reconstructs a different carrier while pretending to preserve base/fiber identity. | Rebuild gap exceeds tolerance under wrong base or wrong phase while correct section+phase reconstructs. | Use as a quotient/convention control for Hopf-fiber packets. |

Other first-class negatives:

| candidate | why killed or bounded | decisive condition | reusable control |
|---|---|---|---|
| Carnot forward hot-heavy closure dominance | Cold-heavy closure mismatch mean is lower than hot-heavy mean in the old asymmetric sweep. | `forward_hot_heavy_closure_dominance` verdict is `killed`. | Excludes a naive forward leg-order prior. |
| Carnot reverse asymmetric closure advantage | Best reverse closure setting is balanced, not asymmetric. | `reverse_asymmetric_closure_advantage` verdict is `killed`. | Separates return closure from COP or leg-dominance narratives. |
| Szilard low-noise monotonicity | High-noise mean margin exceeded low-noise mean margin in the old ordering sweep. | `ordering_sensitivity_low_noise_monotonicity` verdict is `killed`. | Blocks monotone-noise assumptions; preserves nonmonotone tuning as variant evidence. |
| Szilard record reset swing | Stronger reset grid did not reach strict QIT reset swing. | `record_reset_repair_reset_swing` verdict is `killed`. | Forces exact-threshold reset rechecks instead of broad repair claims. |
| Engine-lab performance/closure split | Exact rows were best for both performance and closure, killing the claimed split. | `carnot_performance_closure_split` verdict is `killed`. | Blocks a readout-family split claim while leaving source rows open. |
| Weak Szilard topology claim | Worst topology margin remained positive, killing the weak-topology negative claim. | `szilard_weak_topology_exists` verdict is `killed`. | Prevents removing wide topology from a single weak-topology prior. |
| Non-unit Clifford rotor candidate | Non-unit even multivector fails norm/action gates. | Unit reverse-product norm or vector norm drift gate rejects it. | Excludes spinor representative misuse. |
| GL candidate outside `O(g)` | Invertible shear or scaler does not preserve the metric. | `A^T g A != g`, and z3 det-volume obstruction is UNSAT. | Excludes metric-preservation shortcuts. |
| Disk-as-torus topology | Disk has Betti/Hodge kernel `(1,0,0)`, not torus `(1,2,1)`. | TopoNetX and GUDHI agree it is not torus. | Topology mislabel control. |

## 4. Never-Run Probe Intents

Never-run here means: Python probe-like files with no same-stem result JSON found by static matching. This is conservative and may overcount when result names are transformed, but it is useful for mining latent intent. Count found: 3825.

| file/probe | intended test | observable | v6 packet candidate or exclusion |
|---|---|---|---|
| `sim_engine_lab_next_work_queue.py` | Build a bounded queue from open-row audits, repair priorities, and graveyard coverage. | Queue rows, active uncovered rows, recommended lane, `qit_or_axis_promotion_allowed=false`. | Candidate controller-index packet only; excluded from science evidence. Result JSON was not present. |
| `sim_szilard_torch_measure_feedback_erasure_landauer_cycle.py` | PyTorch-native measurement-feedback-erasure cycle with z3 Landauer exclusions. | Density validity, mutual information, feedback/erasure costs, forbidden-region UNSAT. | Strong candidate micro packet for Szilard/Landauer calibration; promotion remains false. |
| `sim_toponetx_gudhi_hodge_betti_cross.py` | Cross-check Hodge kernel dimensions against GUDHI Betti numbers on torus, disk, sphere. | `(1,2,1)` torus, disk negative, sphere boundary. | Candidate topology parity micro; no same-stem result found. |
| `sim_cvc5_monad_laws_constraint.py` | Prove monad identity/associativity fixtures and violated-law negatives with cvc5. | SAT for law instances, UNSAT for law violations. | Candidate SMT law fixture; not a ratchet object. |
| `sim_gtower_gl_to_o_reduction.py` | Exclude GL candidates that do not preserve a metric under `O(g)` reduction. | `A^T g A = g`, determinant obstruction, shear obstruction. | Candidate G-structure exclusion packet; classical baseline only. |
| `sim_clifford_spinor_double_cover_micro.py` | Isolate Clifford Spin(3) sign equivalence: `R` and `-R` same vector action. | Sandwich action equality, non-unit exclusion, 2pi/4pi boundary. | Candidate pre-lego Clifford tool-surface packet. |
| `sim_hopf_base_section_phase_recovery.py` | Recover Hopf carrier from base section plus fiber phase. | Rebuild gap under correct phase; wrong base/phase failure. | Candidate Hopf convention packet; shell-local only. |
| `sim_weyl_a2_su3_noncommutativity.py` | Test Weyl A2/SU3 noncommutativity and negative controls. | Order-sensitive commutators and negative cases. | Candidate noncommutation fixture; must not promote without fresh run. |
| `sim_lego_engine_protocol_dag.py` | Encode old engine protocol as a DAG-like receipt dependency. | Protocol edges, reachability/order, negative dependency breaks. | Candidate source for future protocol-order falsifier, not a science result. |
| `sim_hopf_higher_fibration_winding_index.py` | Probe higher Hopf fibration winding-index candidates. | Positive/negative/boundary winding checks. | Candidate only; high risk of topology overreach. |
| `sim_cvc5_algebraic_effect_handler_constraint.py` | SMT constraints for effect-handler identity/composition/associativity violations. | Law SAT/UNSAT checks. | Candidate algebraic law negative fixture. |
| `sim_integration_quantum_open_entangle_correlator_mega_stack.py` | Integrate entangled prep, open-system amplitude damping, reduced correlator geometry, and tool checks. | Open-system density error, fit metrics, negative wrong-reference controls. | Exclude from near-term v6 unless decomposed; too wide for a micro packet. |

## 5. Unconsumed Objects Queue

Ranked for mining value, not execution order.

| rank | object | why it matters | boundary |
|---:|---|---|---|
| 1 | Carnot/Szilard/Landauer fence family | It contains clean standard thermodynamic floors, exact violators, and calibrated graveyards. | Classical calibration and exclusion only. |
| 2 | Engine-lab open-row audit and graveyard trio | It already separates open failures, repair gaps, readout splits, and topology sidecars without promotion. | Controller audit only; no source-row closure. |
| 3 | Stage-matrix negative batteries | They encode order, dissipation, chirality, CPTP, decoherence, and commutativity kill switches. | Old-engine falsifier library; future order claims need fresh rerun. |
| 4 | Szilard PyTorch + z3 measurement-feedback cycle | It is a compact candidate for load-bearing density evolution plus forbidden-region proof. | Bridge/control row; `promotion_allowed=false`. |
| 5 | Hopf base-section phase recovery | It gives a tight base/fiber convention test and wrong-phase negative. | Shell-local only. |
| 6 | Clifford Spin(3) double-cover micro | It isolates a small, reusable representative/sign gate. | Pre-lego Clifford tool surface only. |
| 7 | TopoNetX/GUDHI Hodge-Betti cross-check | It offers independent topology parity for torus/disk/sphere fixtures. | Needs fresh execution; not found as same-stem result. |
| 8 | G-tower GL-to-O metric reduction | It provides a standard metric-preservation exclusion. | Classical G-structure fixture only. |
| 9 | SMT/cvc5 law fixtures | Many are useful as compact algebraic designed-fail rows. | Law fixtures are not ratchet mechanism evidence. |
| 10 | QIT density/channel baselines | They encode CPTP, Choi, entropy, trace-distance, Werner, Bell/CHSH, and channel controls. | Baselines before any nonclassical readout. |
| 11 | Hopf/Weyl/Clifford transport family | The estate has many convention-sensitive carrier/readout probes. | Must be decomposed to one carrier, one observable, one kill condition. |
| 12 | Large integration / mega-stack probes | They preserve latent test vocabulary and tool couplings. | Mostly exclude from first pass; too wide until micro receipts exist. |

Top unconsumed objects:

1. Carnot/Szilard/Landauer exact fence controls.
2. Engine-lab open-row audit plus Carnot/Szilard/sidecar graveyards.
3. Stage-matrix negative batteries.
4. Szilard PyTorch measurement-feedback-erasure cycle.
5. Hopf base/fiber phase recovery and Clifford Spin(3) sign micro.

## 6. Convention Divergences

| divergence | source evidence | exclusion rule |
|---|---|---|
| Result existence vs source existence | 4290 Python files but only 349 detected result JSONs. | Source presence does not imply executed evidence. |
| Old engine runtime vs current stage gates | `STABILIZATION_MANIFEST.md` marks old engine core and bridges as robust in that session. | Treat as historical old-estate signal, not current v6 canonical proof. |
| Controller index vs science result | Engine-lab audit files write controller classifications and queues. | Controller indexes can organize work but cannot admit QIT, axis, GStack, runtime-engine, or nonclassical claims. |
| Survived graveyard variant vs promoted row | Carnot/Szilard graveyards include survived variants while keeping source rows open. | A survived local variant is not row closure. |
| Open rows vs closed rows | `engine_lab_open_row_audit_results.json` reports `matrix_status=complete_with_open_rows`, 11 audited nonpassing rows, promotion blocked. | Completion of coverage is not completion of scientific admission. |
| Same object under different tool representation | Clifford rotor vs NumPy Fe divergence is called structural in stabilization notes. | Representation mismatch is a convention issue until a shared observable closes it. |
| Topology sidecar vs strict carrier evidence | Sidecar graveyard says topology/readout signals are not strict QIT carrier evidence. | Keep topology variants as sidecars until re-expressed on strict carriers. |
| Boundary/fence result vs mechanism claim | Carnot and Landauer fences reject violators but do not implement full cycle mechanics. | A fence can block impossible claims; it cannot supply mechanism. |
| Standard theorem fixture vs ratchet object | cvc5 category/law files encode theorem-like constraints. | Use as law controls only unless a future packet names a ratchet observable and gate. |
| Broad mega-stack vs micro tool/function packet | Many integration files combine tools, carriers, and couplings. | Decompose before reuse; no packet should debug tool, lego, and coupling together. |

## 7. Source Index

Inventory commands and static scans:

- `rg --files system_v4/probes | sort`
- `find system_v4/probes -type f`
- static Python scan for file/result counts, negative hooks, and missing same-stem result JSONs
- targeted JSON reads under `system_v4/probes/a2_state/sim_results/`

High-signal source files:

- `system_v4/probes/MASS_SIM_MANIFEST.md`
- `system_v4/probes/STABILIZATION_MANIFEST.md`
- `system_v4/probes/sim_engine_lab_open_row_audit.py`
- `system_v4/probes/sim_engine_lab_next_work_queue.py`
- `system_v4/probes/sim_carnot_asymmetric_direction_graveyard.py`
- `system_v4/probes/sim_szilard_open_failure_graveyard.py`
- `system_v4/probes/sim_engine_lab_sidecar_graveyard.py`
- `system_v4/probes/sim_carnot_constraint_admissibility_fence.py`
- `system_v4/probes/sim_szilard_measure_feedback_erasure_landauer_bounds.py`
- `system_v4/probes/deep_graveyard_battery.py`
- `system_v4/probes/extended_graveyard_battery.py`
- `system_v4/probes/thermodynamic_graveyard_battery.py`
- `system_v4/probes/stage_matrix_neg_lib.py`
- `system_v4/probes/sim_szilard_torch_measure_feedback_erasure_landauer_cycle.py`
- `system_v4/probes/sim_toponetx_gudhi_hodge_betti_cross.py`
- `system_v4/probes/sim_cvc5_monad_laws_constraint.py`
- `system_v4/probes/sim_gtower_gl_to_o_reduction.py`
- `system_v4/probes/sim_clifford_spinor_double_cover_micro.py`
- `system_v4/probes/sim_hopf_base_section_phase_recovery.py`

High-signal result files:

- `system_v4/probes/a2_state/sim_results/cycle_protocol_receipt_status_matrix_results.json`
- `system_v4/probes/a2_state/sim_results/engine_lab_open_row_audit_results.json`
- `system_v4/probes/a2_state/sim_results/carnot_asymmetric_direction_graveyard_results.json`
- `system_v4/probes/a2_state/sim_results/szilard_open_failure_graveyard_results.json`
- `system_v4/probes/a2_state/sim_results/engine_lab_sidecar_graveyard_results.json`
- `system_v4/probes/a2_state/sim_results/carnot_constraint_admissibility_fence_results.json`
- `system_v4/probes/a2_state/sim_results/bridge_carnot_admissibility_fence_results.json`
- `system_v4/probes/a2_state/sim_results/szilard_measure_feedback_erasure_landauer_bounds_results.json`
- `system_v4/probes/a2_state/sim_results/bridge_landauer_erasure_bit_distinguishability_results.json`
- `system_v4/probes/a2_state/sim_results/bridge_szilard_landauer_floor_results.json`

Family counts by static filename/path scan:

| family key | count |
|---|---:|
| `szilard` | 64 |
| `engine_` | 62 |
| `carnot` | 43 |
| `qit_szilard` | 18 |
| `landauer` | 14 |
| `engine_lab` | 12 |
| `stoch` | 9 |
| `qit_carnot` | 9 |
| `maxwell` | 5 |
| `jarzynski` | 4 |

Math/tool cluster counts by Python filename/path scan:

| cluster | count |
|---|---:|
| SMT/symbolic exclusion (`z3`, `cvc5`, `sympy`, `unsat`, `smt`) | 472 |
| Clifford/Weyl/spinor/chirality | 458 |
| Hopf/fiber/torus/connection/holonomy | 356 |
| QIT density/entropy/channel | 302 |
| topology/graph/homology | 277 |
| category/homotopy/algebraic geometry | 251 |
| autograd/geometry/optimization | 196 |
| thermodynamic Carnot/Szilard/Landauer/Jarzynski/Maxwell | 108 |
