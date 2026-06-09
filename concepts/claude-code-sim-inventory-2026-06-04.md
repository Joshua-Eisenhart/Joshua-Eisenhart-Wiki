# Claude Code Sim Inventory — 2026-06-04

Purpose: read-only inventory of what Claude Code's `work-out-layers.js` pipeline has built. Snapshot, not authority — the repo result JSONs are the actual evidence.

Status: active current inventory snapshot.

## Scale

- **60+ top-level Julia carrier result files** (system_v5/julia_carrier/)
- **157+ layer result files** (system_v5/julia_carrier/layers/)
- **7 Hopfield result files** (system_v5/julia_carrier/hopfield/)
- **166+ /tmp output files** from codex2 builds and audits
- JAX + Julia running in sealed-construction parallel

## Sim families (organized by pipeline stage)

### Stage 0 — Source Math Lock
- `/tmp/16_token_axis_projection_matrix.json` — 16 rows, locked

### Stage 1 — Geometry layers
| Sim | What it tests |
|---|---|
| `geomratchet_julia` | Geometry ratchet — constraint manifold → carrier geometry |
| `c3_chirality_constraint_candidate` | C3 chirality constraint candidate |
| `cfp_test_multi_c3` | Multi-C3 probe |
| `ratchet_f01n01_carrier_derivation` | F01+N01 carrier derivation ratchet |
| `dim2_minimality_check` | Dim-2 minimality |
| `n01_ordering_forced_carrier` | N01 ordering forces carrier |
| `nonchiral_carrier_f01n01_negative_control` | Nonchiral negative control |
| `qubit_scaling_sweep_f01n01_structure` | F01/N01 scaling sweep |
| `spinor_subsystem_independence_sweep` | Spinor subsystem independence |

### Stage 1 — G-structure exploration
| Sim | What it tests |
|---|---|
| `gs_g2_octonion_julia` | G2 octonion structure |
| `gs_spin7_cayley_julia` | Spin(7) Cayley |
| `gs_su3_calabiyau_julia` | SU(3) Calabi-Yau |
| `gs_sp2_quaternionic_julia` | Sp(2) quaternionic |

### Stage 2 — Terrains
| Sim | What it tests |
|---|---|
| `wb_axis3_terrains_julia` | Axis 3 terrains |
| `wb_axis5_spectral_gradient_julia` | Axis 5 spectral gradient |

### Stage 3 — Operators / Engines
| Sim | What it tests |
|---|---|
| `eng_axes12_julia` | Axis 1 expand/compress + Axis 2 open/closed (size ladder 8/16/32/64) |
| `eng_carnot_axiswired_julia` | Carnot engine all-6-axes wired (verdict: False — honest failure) |
| `eng_szilard_axiswired_julia` | Szilard engine 6-axis wired (verdict: True) |
| `eng_yinyang_julia` | Yin-yang 1-axis element (FLIP=chirality, ROTATE=axis4) |
| `eng_64_hexagram_julia` | 64-hexagram state space |
| `carnot_szilard_qit_engine_julia` | Carnot+Szilard+QIT engine |
| `carnot_szilard_qit_engine` | Same family, earlier version |
| `bde_julia` | Bidirectional dual-stacked engine |
| `ax4_julia` | Axis 4 variance-order split |
| `ax6_julia` | Axis 6 bounded finite-map |
| `axorth_julia` | Axis orthogonality probe |

### Stage 3 — IGT / Connection geometry
| Sim | What it tests |
|---|---|
| `igt_chirality_julia` | IGT win/lose payoff asymmetry as chirality probe (M_IGT) |
| `npc_connection_geometry_julia` | Connection geometry probe |
| `npc2_connection_geometry_julia` | Connection geometry v2 |

### Stage 4 — Nesting / Carrier
| Sim | What it tests |
|---|---|
| `crl_ratchet_julia` | Cumulative-exclusion ratchet ladder L0..L9, 6 carrier types |
| `crl2_julia` | Ratchet v2 |
| `wb_g3_basis_independence_julia` | G3 basis independence |
| `wb_engine_fix_shared_seed_julia` | Engine shared-seed fix |
| `wb_basin_proof_smt_julia` | Basin proof (SMT) |

### Stage 4 — Hopfield / Neural
| Sim | What it tests |
|---|---|
| `hopfield/neural_on_manifold` | Finite quaternionic Hopfield — nonflat changes network (audit-confirmed) |
| `hopfield/basin_probe_v2_hopfield_spinor` | Hopfield basin probe v2 |
| `hopfield/deflation_hopfield_basin` | Hopfield basin deflation (deflated) |

### Axis 0 / Entropy
| Sim | What it tests |
|---|---|
| `axis0_entropy_monotone` | Axis 0 entropy monotone |
| `basin3_julia` | Basin exploration |
| `chiral_quat_spinor_basin_explore` | Chiral quaternion spinor basin |

### Deflation family (audit-confirmed)
| Sim | Verdict |
|---|---|
| `layers/deflation_order_null` | order_null_survives ✅ |
| `layers/deflation_substrate_band` | substrate_survives ✅ |
| `layers/cocycle_third_section` | third_section_reproduces ✅ |
| `layers/cocycle_full_monopole` | full_monopole_present ✅ |
| `hopfield/neural_on_manifold` | nonflat_changes_network ✅ |
| `layers/deflation_ratchet_survivor` | ratchet_deflated 📉 |
| `hopfield/deflation_hopfield_basin` | hopfield_basin_deflated 📉 |

### Branch/prune possibility field family
| Sim | What it tests |
|---|---|
| `branch_prune_spinor_field_object` | Chirality constraint prunes branch ensemble |
| `branch_prune_dirac_gamma5_chirality_object` | Genuine gamma5 chiral charge prune |
| `branch_prune_geometry_is_information_admissibility` | Geometry IS information as admissibility constraint |
| `entropy_is_geometry_free_fermion` | Entropy IS geometry (free fermion) |

## Key observations

1. **Carnot all-6-axes FAILED honestly** (eng_carnot_axiswired_julia verdict=False). This is real evidence — the Carnot engine doesn't wire all axes cleanly.
2. **Szilard all-6-axes PASSED** (eng_szilard_axiswired_julia verdict=True). The dual-stacked engine target is closer to Szilard than Carnot.
3. **IGT chirality probe EXISTS** (igt_chirality_julia) — this directly tests the win/lose payoff asymmetry as chirality, which is the owner's key pattern.
4. **64-hexagram sim EXISTS** (eng_64_hexagram_julia) — maps to the trigram/hexagram structure.
5. **Branch/prune family is strong** — 3 PoC sims showing constraints shape which futures survive.
6. **All promotion_allowed=false** — nothing claims to be canonical.

## What's NOT here yet

- Pure QIT versions of the engines (no classical math)
- The dual-stacked engine with the specific 720° spinor loop + L/R + inner/outer flip
- Axis 4 (deduction/induction) QIT math
- Quaternion-native sims (some use quaternions, but not as the primary carrier)
- S3 layer in the ratchet chain
- Doc-by-doc IGT pattern extraction → testable predictions (codex2 running now)

## Related

- [[active-claude-code-work-2026-06-04]]
- [[deflation-map-2026-06-04]]

Write mode: controller-maintained inventory snapshot.
