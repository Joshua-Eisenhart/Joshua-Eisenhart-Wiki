# Old Registries, Axes, and Operators Mine

## 1. Scope and Evidence Boundary

This file mines old registry and AXES/operator source surfaces for math-object inventory only. It is not a roadmap, not an admission packet, and not a canonical promotion surface.

Inspected primary old-estate sources: 5 files.

| Source | Role in this mine |
|---|---|
| `system_v5/docs/17_actual_lego_registry.md` | broad one-row-per-lego registry; treated as candidate inventory |
| `system_v5/docs/MIGRATION_REGISTRY.md` | 28 irreducible family migration rows; treated as family inventory plus negative-battery surface |
| `system_v5/ops/AXES_TERRAINS_OPERATORS_MANIFOLD_SOURCE_LAYOUT_20260522.md` | constraint-manifold ladder, axes, terrains, operators, token grammar |
| `system_v5/ops/AXES_0_6_DEEP_MATH_DEFINITIONS_20260522.md` | axis definitions, falsifiers, runtime receipt schema, flux boundary |
| `system_v5/ops/QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md` | exact Ti/Te/Fi/Fe operator maps, signed variants, action-side/precedence rules |

V6 match scope inspected: `system_v6/sims/` names and selected build/audit cards across 82 sim directories, plus `system_v6/receipts/` names and selected receipts across 84 receipt files. A direct v6 match means the v6 packet or receipt names and scopes the same object family plainly. Incidental mentions inside large result JSONs were not counted as representation.

Counts:

| Count | Value |
|---|---:|
| Primary registry/docs inspected | 5 |
| V6 sim directories inspected for names/scope | 82 |
| V6 receipt files inspected for names/scope | 84 |
| Objects inventoried | 236 |
| Direct v6 matches | 38 |
| Row/group objects not directly represented in v6 | 198 |
| Negative/killed/control rows extracted | 22 |

Inventory count basis: 152 lego rows from `17_actual_lego_registry.md`; 28 migration-family rows from `MIGRATION_REGISTRY.md`; 56 AXES/operator grouped source objects: 20 constraint-manifold ladder rows, 4 base operator maps, 8 terrain realizations, 8 signed variants, and 16 ordered tokens.

## 2. Registry Inventory Summary

The old lego registry is broader than the current v6 packet set. It includes root/admission rows, representation rows, compression/spectral rows, geometry rows, loop/connection rows, operator/channel rows, graph/topology rows, bipartite/correlation rows, entropy rows, late bridge/Axis rows, and boundary falsifier rows.

The migration registry contributes 28 family rows. All 28 are marked `NOT_STARTED` as torch-module migrations in that old registry. That status is migration-specific: it does not mean the math object is absent everywhere, only that the standalone torch family module did not exist in that registry snapshot.

The AXES/operator docs add object groups that are not one-to-one with old lego IDs:

| Group | Objects |
|---|---|
| Constraint-manifold ladder | root constraints, `C`, `M(C)`, axis readouts, `H=C^2`, `D(C^2)`, `S^3`, Hopf projection, `S^2`, `T_eta`, Clifford torus, fiber/base loops, Weyl sheets, left/right densities, engine runtime manifold, `Xi`, cut-state family, `Phi_0` |
| Base operators | `Ti`, `Te`, `Fi`, `Fe` |
| Terrain realizations | `Se/Funnel`, `Se/Cannon`, `Ne/Vortex`, `Ne/Spiral`, `Ni/Pit`, `Ni/Source`, `Si/Hill`, `Si/Citadel` |
| Signed variants | `Ti^up`, `Ti^down`, `Te^up`, `Te^down`, `Fi^up`, `Fi^down`, `Fe^up`, `Fe^down` |
| Ordered tokens | `TiSe`, `SeTi`, `TiNe`, `NeTi`, `TeNi`, `NiTe`, `TeSi`, `SiTe`, `FiSe`, `SeFi`, `FiNe`, `NeFi`, `FeNi`, `NiFe`, `FeSi`, `SiFe` |

## 3. Standard-Math Facts Mined

These are bounded source facts, not admissions. They name finite objects or standard control relations the registries/docs expose for later packet design.

| Object family | Mined fact | Boundary |
|---|---|---|
| Density operators | `density_matrix`, purification, eigen-decomposition, measurement, channel, and entropy rows all presuppose finite positive semidefinite trace-one density carriers or explicit negative controls for invalid carriers. | A density carrier is a hygiene object and quotient surface, not QIT-engine admission. |
| CPTP / channel maps | Operator-channel rows distinguish base maps, signed variants, instruments, unitary rotations, dephasing/damping, and capacity/coherent-information readouts. | CPTP legality and channel taxonomy do not imply terrain/operator closure or bridge evidence. |
| Terrain/operator composition | `Ti`, `Te`, `Fi`, and `Fe` are maps applied with terrain/action-side/precedence context; `UP/DOWN` is order/precedence after a terrain is chosen, not a new independent channel formula. | Use source-locked map plus terrain context before comparing words; signed variants are not eight new maps. |
| Finite graph/scalar support | `discrete_axis0_field`, `ring_checkerboard_support`, `Xi_shell`, and `Xi_hist` expose finite graph, shell, history-window, and scalar-readout candidates. | These are local support/readout objects only; they do not close Axis0, Xi, or Phi0. |
| Entropy functionals | `path_entropy`, `branch_weight`, `history_window_entropy`, `transport_weighted_entropy`, `operator_ordered_entropy`, relative entropy, coherence, discord, and negativity rows separate readout functionals. | Entropy labels must name carrier, log base, branch weights, transport rule, and erased/shuffled controls. |
| Noncommutative/order controls | Axis 4 loop order, Axis 6 precedence, token order, operator order, and noncommuting channel order are separate degrees of freedom. | Order-correctness must be tested separately from content-correctness. |
| Geometry/gauge controls | Registry falsifiers include Hilbert-Schmidt flatness rejection, relative-entropy nonmetric boundary, real-only geometry rejection, commutative-geometry collapse, and gauge/group local-commutator constraints. | These are exclusion controls, not positive geometry/gauge admission. |

## 4. Math Objects / Legos Already Represented in v6

Direct matches only:

| Old object or source group | Direct v6 surface | Boundary |
|---|---|---|
| `density_matrix` / density matrix as quotient | `system_v6/receipts/density_matrix_as_quotient_doctrine_20260610.md` | doctrine/quotient receipt, not a full migration-module completion |
| `Ti`, `Te`, `Fi`, `Fe` base operator maps | `system_v6/sims/source_locked_operator_base_packet/` | genuine-with-caveats scratch diagnostic; source-locked operator forms, not operator-family completion |
| `Ti^up/down`, `Te^up/down`, `Fi^up/down`, `Fe^up/down` | `system_v6/sims/terrain_operator_precedence_64_matrix/` | signed variants as precedence/context rows, not eight independent base maps |
| 16 ordered topology/operator tokens | `system_v6/sims/terrain_operator_precedence_64_matrix/` | chart object and fingerprint families only; no runtime/hexagram closure |
| 8 terrain realizations | `system_v6/sims/terrain_generator_sheet_packet/` | source-locked terrain generator/sheet packet, scratch diagnostic with caveats |
| `ring_checkerboard_support` | `system_v6/sims/ring_checkerboard_support_graph_probe/` and `system_v6/receipts/ring_checkerboard_support_mine_20260610.md` | support graph candidate; no Axis-0 closure or canonical manifold admission |

Near matches not counted as direct matches:

| Old object | Related v6 surface | Why not counted direct |
|---|---|---|
| `discrete_axis0_field` | `ring_checkerboard_support_mine_20260610.md`; MCT `b0` rows | v6 has shell/readout support, not a full `phi0: V -> R` graph field with edge gradients |
| S4 operator-channel geometry | `geo_s4_operator_stage_v0` | packet was useful but rejected as claimed against the blind exactness bar |
| S5 terrain-flow fixed/basin packet | `geo_s5_terrain_flows_v0` | packet was useful but rejected as claimed against the S5 blind exactness bar |
| Axis 0/3/6 independence | `axis_independence_discriminators_036` | packet was audited decorative for carrier-independence evidence |
| full torch module migration families | v6 has many sims and receipts | old migration target was standalone torch modules; v6 packet presence is not a direct migration completion |

## 5. Unconsumed Objects Queue

Ranked future sim candidates from the unconsumed surface. These are candidate rows only; each remains blocked from promotion until a future receipt supplies the stated boundary.

| Rank | Candidate | Source | Boundary / first honest probe |
|---:|---|---|---|
| 1 | `discrete_axis0_field`: graph scalar `phi0: V -> R` and directed gradients | `17_actual_lego_registry.md`; ring-checkerboard mine | Build finite support graph `G=(V,E,kappa,V_inner,V_outer,phi0)`; test directed gradients under adjacency/color/nesting/orientation controls. No Axis-0 closure. |
| 2 | `Xi_shell` bridge family | `17_actual_lego_registry.md`; AXES ladder | Shell bridge only; construct shell-aggregated bridge on one bounded shell family. Do not identify with `Phi_0` closure. |
| 3 | `Xi_hist` bridge family | `17_actual_lego_registry.md`; AXES ladder | History-window bridge only; test bounded history window behavior with erased-history control. |
| 4 | `axis0_field_candidate` | `17_actual_lego_registry.md`; AXES deep definitions | Local candidate scalar field only; must separate controls before bridge/axis promotion. |
| 5 | `torus_seat_entropy` | `17_actual_lego_registry.md`; AXES ladder | Geometry-seat entropy over one torus family; no global entropy-field claim. |
| 6 | `path_entropy` and `branch_weight` | `17_actual_lego_registry.md`; AXES deep definitions | Branch/path entropy over bounded CPTP branching; branch weights must be computed, not label-assigned. |
| 7 | `history_window_entropy` | `17_actual_lego_registry.md` | Entropy over declared finite history windows; compare against erased-history and shuffled-order controls. |
| 8 | `transport_weighted_entropy` | `17_actual_lego_registry.md` | Weight entropy by declared transport structure; control must erase transport without changing state labels. |
| 9 | `operator_ordered_entropy` | `17_actual_lego_registry.md`; QIT signed-operator doc | Compare entropy under operator/terrain order on one fixed family; must reuse source-locked operator and terrain forms. |
| 10 | `shell_indexed_tensor_network` | `17_actual_lego_registry.md` | Shell-indexed tensor-network support only; no PEPS/MPS closure unless a separate tensor receipt proves it. |
| 11 | `shell_fuzz_jk` | `17_actual_lego_registry.md` | Support-window fuzz variables only; test j/k window perturbations with erased-window control. |
| 12 | `chiral_overlap` | `MIGRATION_REGISTRY.md` row 26 | Old registry says no baseline implementation. Minimal baseline: left/right Weyl handedness overlap under fixed spinor/Hopf carrier. |
| 13 | `z_measurement` | `MIGRATION_REGISTRY.md` row 12 | Old registry says no dedicated z-measurement baseline. Build one finite measurement/instrument row, separate from generic POVM. |
| 14 | standalone `purify(rho)` | `MIGRATION_REGISTRY.md` row 2 | Extract purification as its own function/object; compare density and purification views without widening to distillation. |
| 15 | standalone `unitary_rotation()` as channel | `MIGRATION_REGISTRY.md` row 11 | Dedicated rotation-as-channel baseline; do not rely on incidental mega-protocol usage. |
| 16 | `relative_entropy_coherence` | `MIGRATION_REGISTRY.md` row 23 | Coherence functional, not generic relative entropy; include incoherent-state control. |
| 17 | `wigner_negativity` | `MIGRATION_REGISTRY.md` row 24 | Phase-space negativity row; keep separate from Wigner representation. |
| 18 | `quantum_discord` | `MIGRATION_REGISTRY.md` row 28 | Local two-party discord candidate; require classical-correlation control and no bridge promotion. |
| 19 | `mutual_information_measure` | `17_actual_lego_registry.md`; migration row 27 | Local MI row; old registry says useful-if-rejected is no, but it remains a named object. |
| 20 | `coherent_information_measure` | `17_actual_lego_registry.md` | Keep separate from conditional entropy and Axis-0 `Phi_0` candidate. |
| 21 | `logarithmic_negativity` | `17_actual_lego_registry.md` | Distinct from raw negativity; compare on fixed bipartite state family. |
| 22 | `channel_capacity` | `17_actual_lego_registry.md` | Later than CPTP legality; local channel-capacity probe only. |
| 23 | `measurement_instrument` | `17_actual_lego_registry.md` | State-update instrument row; not just POVM effects. |
| 24 | `blackwell_style_comparison` | `17_actual_lego_registry.md` | Operational comparison under finite probe families; preserve probe-relative language. |
| 25 | `operator_semigroup_closure` over `{Ti,Te,Fi,Fe}` | QIT operator doc; terrain operator map | Bounded word-depth closure/invertibility test; likely kills finite-group overclaim unless parameters/quotients are fixed. |

## 6. Negative / Killed Candidates and Designed-Fail Controls

Extracted negatives/kills/control rows: 22.

Old registry falsifier rows:

| Negative/control | Source | Use |
|---|---|---|
| `hilbert_schmidt_flatness_rejection` | `17_actual_lego_registry.md` | reject Hilbert-Schmidt as sole geometry |
| `relative_entropy_nonmetric_boundary` | `17_actual_lego_registry.md` | relative entropy is not a metric |
| `real_only_geometry_rejection` | `17_actual_lego_registry.md` | real-only restriction kills Berry/curvature structure |
| `commutative_geometry_collapse` | `17_actual_lego_registry.md` | commuting reduction collapses nontrivial geometry |
| `gauge_group_correspondence` | `17_actual_lego_registry.md` | gauge/group claims must be generated by local commutators |
| `viability_vs_attractor` | `17_actual_lego_registry.md` | distinguish constraint viability from attractor pull |
| `quantum_metric_nonuniqueness` | `17_actual_lego_registry.md` | Bures/Wigner-Yanase/Kubo-Mori disagreement is a boundary surface |

Migration negative batteries:

| Battery | Covered families |
|---|---|
| `sim_negative_density_matrices.py` | density, purification, eigen decomposition, Husimi, Wigner negativity |
| `sim_negative_channels.py` | dephasing, damping, flips, z-measurement, Hadamard, T gate |
| `sim_negative_entanglement.py` | CNOT, CZ, SWAP, iSWAP, Cartan/KAK |
| `sim_negative_entropy_boundaries.py` | coherence, mutual information, discord |
| `sim_negative_geometry.py` | Hopf connection, chiral overlap |

AXES/operator kills and fences:

| Candidate or failure mode | Status from sources |
|---|---|
| A3-A6 generate 16 tokens as stated | falsified as stated; A3 x A4 x A5 x A6 gives 8 paired signatures, not 16 token identities |
| flux as pre-axial root | not admitted; derived candidate family only |
| engine type equals A3 x A4 | not proven; underdetermined |
| eight signed variants as eight new channel maps | killed; they are four maps plus precedence/action-side context |
| `UP/DOWN` as plus/minus sign on operator formula | killed; it is order/precedence after a terrain map is chosen |
| Axis 0 chart seat equals bridge `Phi_0` closure | not admitted; chart and bridge Axis 0 must not be silently identified |
| Axis 4 loop order collapsed into Axis 6 precedence | killed by source separation; must vary independently |
| win/lose as executable payoff | fenced; no payoff/utility/selection claim until a named functional is attached |
| Te as intrinsically descent | killed; descent/ascent depends on functional, target, terrain, and stage word |
| Fe/Fi as entropy-changing by themselves | killed; bare unitary maps preserve spectrum |

## 7. Convention Divergences

| Divergence | Source exposure | Current boundary |
|---|---|---|
| `sigma_+` / `sigma_-` for Ni/Pit and Ni/Source | migration and terrain/operator receipts preserve convention pressure | v6 terrain packet source-locks Pit to `sigma_-` and Source to `sigma_+`, but future rows should keep the convention explicit |
| Pure Ne Hamiltonian vs weak-dissipator Ne | AXES/terrain docs and v6 terrain audit | Pure Ne is the source-forced purity-preservation object; weak dissipator is a pinned/exploratory variant unless separately scoped |
| Si projector frames | terrain/operator sources and v6 terrain packet | Hill/Citadel use pinned z/x frames in v6; source requires projector structure but does not force every axis choice |
| Bloch `sigma_y` sign / pinned-y convention | v6 S4 audit and estate convention ledger | Standard source-locked basis and pinned-y crosswalk must be separated; sign-correctness and content-correctness are different tests |
| Axis 4 order vs Axis 6 precedence | AXES deep definitions; matrix64 and axis-independence receipts | Two different order degrees of freedom; do not use one as evidence for the other |
| Axis 0 polarity vs Axis 3 placement vs Axis 6 precedence | terrain operator map addendum and axis-independence mine | Three distinct polarities; do not collapse shared `+/-` vocabulary |
| Terrain family vs operator map | AXES source layout and QIT operator packet | `Se/Ne/Ni/Si` are terrain/topology laws; `Ti/Te/Fi/Fe` are maps on density matrices |
| 64 chart matrix vs runtime hexagram 64 | matrix64 mine and terrain-operator precedence audit | Four parallel 64 constructions remain distinct; chart distinctness does not imply runtime closure |
| `covered` in old registry vs represented in v6 | old lego registry | Old `covered` is not a v6 direct match unless a v6 packet or receipt names and scopes the object |

## 8. Source Index

Primary old sources:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/17_actual_lego_registry.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/MIGRATION_REGISTRY.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/AXES_TERRAINS_OPERATORS_MANIFOLD_SOURCE_LAYOUT_20260522.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/AXES_0_6_DEEP_MATH_DEFINITIONS_20260522.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md`

V6 match/adjudication surfaces used:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/source_locked_operator_base_packet/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/terrain_generator_sheet_packet/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/terrain_operator_precedence_64_matrix/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/geo_s4_operator_stage_v0/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/geo_s5_terrain_flows_v0/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/axis_independence_discriminators_036/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/ring_checkerboard_support_graph_probe/`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/terrain_operator_map_20260609.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/doc_router_axes_terrains_operators_20260609.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/estate_convention_ledger_20260610.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/matrix64_mine_20260610.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/axis_independence_mine_20260610.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/ring_checkerboard_support_mine_20260610.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/s4_build_spec_20260610.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/s5_build_spec_20260610.md`
