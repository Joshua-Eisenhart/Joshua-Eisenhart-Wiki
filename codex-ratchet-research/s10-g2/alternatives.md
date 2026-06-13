# S10 G2 - Alternatives

Status: populated by corpus wave 2 child lane on 2026-06-11.

These are finite alternative labels/rows for future S10 packets. They are not
claims that a physical G2 object exists, that a canonical compact/split form is
selected, or that any row has passed formal admission.

## Registry-label candidates

| Label | Use | Required teeth | Blocked promotion |
|---|---|---|---|
| `compact_O_G2_label` | Compact division-octonion automorphism/stabilizer label. | structure constants, positive metric, `Der(O)=14`, 3-form preservation, corrupted-O control | No physics, bridge, or canonical admission. |
| `split_O_G2_2_label` | Split-octonion / split real-form label. | split table, metric signature, zero-divisor or isotropic witness, `Der=14`, compact wrong-sign control | Do not conflate with finite group `G2(2)`. |
| `real_form_signature_row` | Compact-vs-split discriminator. | signature of algebra and imaginary part, stated convention, 3-form orbit class | Label only until recomputed from table. |
| `null_stabilizer_Levi_quotient_row` | Split null-vector row. | stabilizer dimension, nilradical dimension, quotient dimension, quotient bracket evidence | Not an embedded Levi factor unless later proved. |
| `triality_D4_intertwiner_row` | D4/Spin(8) representation-permutation row. | explicit representation bases, maps, residual checks, order checks | Not all triality intertwiners; not generation physics. |
| `triality_fixed_or_folded_G2_label` | Folding/fixed-point language. | named automorphism, fixed subalgebra/group definition, real form | Do not replace octonion/3-form proof. |
| `weyl_G2_root_label` | Root-system combinatorics. | 12 roots, Weyl order 12, short/long root convention, chamber action | Does not force octonion carrier. |
| `branch_7_14_27_row` | Representation/projector branch label. | computed projector/action ranks and trace-free handling | No table-prose echo. |
| `SU3_stabilizer_pick_compact` | Compact chosen unit row. | chosen unit, stabilizer dimension 8, transported basis map, orbit/coset dimension 6 | Split rows cannot copy this automatically. |
| `split_vector_causal_stabilizer_pick` | Split positive/negative/null vector row. | vector norm class, stabilizer solve-space, causal-type label | No compact `SU(3)` import by analogy. |
| `480_orientation_enumerator_row` | Compact orientation table family. | exact enumerator, Fano triads, sign choices, table hashes, orbit keys | No 480-packet explosion before orbit classes. |
| `signature_hybrid_control` | Designed-fail compact/split mismatch. | wrong metric/form pairing and failing preservation/signature check | Control only. |

## Variants by source family

- Real form variants: `compact`, `split`, and `hybrid_control`. The source
  distinction is standard; the local packet distinction must be recomputed.
  Sources: Draper arXiv:1704.07819; Asok-Hoyois-Wendt split-octonion paper,
  https://hoyois.app.uni-regensburg.de/papers/octonionbundles.pdf.
- Parabolic/Levi variants: `standard_parabolic_label`,
  `computed_stabilizer_label`, `nilradical_plus_Levi_quotient`, and
  `embedded_Levi_factor`. Only the last requires an explicitly closed embedded
  complement. Sources: Conrad standard parabolic notes,
  https://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/stdpar.pdf;
  local audit `system_v6/sims/geo_s10_intertwiner_depth_v0/audit_verdict.md`.
- Triality variants: `D4_diagram_triality`, `explicit_intertwiner_triality`,
  `fixed_point_G2`, and `octonion_aut_G2`. These are different routes and must
  not be collapsed into a single voice. Sources: Baez arXiv:math/0105155;
  McRae arXiv:2502.14016.
- Weyl/combinatoric variants: `G2_root_system`, `Fano_incidence`,
  `Fano_oriented_table`, `signed_basis_map`, `orbit_representative`, and
  `PSL_2_7_sanity_check`. Sources: Sevennec arXiv:1106.6015; PAWS notes;
  local `system_v6/receipts/s10_g2_family_mine_20260610.md`.

## Finite row names safe for MMM/register use

- `label_only_real_form_candidate`.
- `compact_split_signature_discriminator`.
- `null_row_kills_embedded_Levi_claim_until_constructed`.
- `triality_route_requires_D4_basis_and_maps`.
- `Fano_table_orientation_candidate`.
- `480_count_requires_enumerator_receipt`.
- `SU3_stabilizer_pick_requires_unit_and_metric`.
- `split_stabilizer_pick_requires_causal_type`.
- `branch_label_requires_projector_rank`.
- `root_system_label_does_not_install_carrier`.

## Source list

- Baez, "The Octonions", arXiv:math/0105155, https://arxiv.org/abs/math/0105155.
- Draper, "Notes on G2", arXiv:1704.07819, https://arxiv.org/abs/1704.07819.
- Conrad, "Standard parabolic subgroups",
  https://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/stdpar.pdf.
- McRae, "Exploring Triality Explicitly", arXiv:2502.14016,
  https://arxiv.org/abs/2502.14016.
- Sevennec, "Octonion multiplication and Heawood's map", arXiv:1106.6015,
  https://arxiv.org/abs/1106.6015.
- Local S10 receipt and audits:
  `system_v6/receipts/s10_g2_family_mine_20260610.md`,
  `system_v6/sims/ratchet_g2_family_v0/audit_verdict.md`,
  `system_v6/sims/geo_s10_intertwiner_depth_v0/audit_verdict.md`.
