---
title: G-Structure Variant Sim Ledger
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [concept, geometry, simulation, proof, topology, mathematics]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/g_structure_tower_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/g_structure_tower_classical_obstruction_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results/clifford_sympy_geomstats_nested_g_structure_live_state_probe_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results/g_structure_reduction_permutation_compatibility_probe_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results/root_manifold_g_structure_holonomy_chart_invariance_probe_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results/full_thirteen_layer_active_g_structure_both_chiral_source_native_composition_probe_results.json
framing: current
---

# G-Structure Variant Sim Ledger

## What this page is

This is the routing ledger for G-structure variant sims and formal scouts.

It exists because the system does not have one generic “G-structure” lane. It has multiple G-structure variants, reduction chains, branch choices, and formal-scout surfaces.

The educational wiki should teach the math, but the sim ledger should keep track of what has already been run and what its claim ceiling is.

## Safe summary

There is already sim work for several G-structure variants.

The strongest current pattern is:

- v4 has classical-baseline G-structure tower / obstruction results.
- v5 has multiple formal scouts with `promotion_allowed=false`.
- Recent scouts are useful for routing, falsifier design, and tool coverage.
- They do not yet admit a final manifold, final G-structure, final attractor basin, final engine, or physics/axis claim.

## Variant ledger

| Variant family | Main result surface | Artifact status | Load-bearing structure | What it supports | What it does not support |
|---|---|---|---|---|---|
| support-manifold tower baseline | `g_structure_tower_results.json` | `classical_baseline`, `all_pass: true` | smooth/Riemannian/oriented/Spin and even-vs-odd branch checks | baseline admissibility tower and obstruction framing | final G-structure or final manifold admission |
| tower obstruction baseline | `g_structure_tower_classical_obstruction_results.json` | `classical_baseline`, `all_pass: true` | obstruction-style tower checks | baseline obstruction witness | canonical/process-level finality |
| nested symbolic live-state chain | `clifford_sympy_geomstats_nested_g_structure_live_state_probe_results.json` | `formal_scout`, `promotion_allowed: false` | GL(2,C) -> U(2) -> SU(2) -> Spin(3) -> Weyl chirality | symbolic G-reduction chain over live EngineCore tensor state | no G-structure/manifold/engine promotion |
| reduction-permutation compatibility | `g_structure_reduction_permutation_compatibility_probe_results.json` | `formal_scout`, `promotion_allowed: false` | order-sensitive nested reductions over finite 4D metric state | N01-style order gap, reversal and adjacent-swap falsifiers | no canonical manifold/final G-structure |
| semantic nesting/order falsifier | `g_structure_nesting_semantic_order_falsifier_probe_results.json` | `formal_scout`, `promotion_allowed: false` | semantic order/falsifier pressure | routing/falsifier support | no final admission |
| semantic family permutation falsifier | `g_structure_semantic_family_permutation_falsifier_probe_results.json` | `formal_scout`, `promotion_allowed: false` | family permutation controls | routing/falsifier support | no final admission |
| semantic layer/operator coupling | `g_structure_semantic_layer_operator_coupling_probe_results.json` | `formal_scout`, `promotion_allowed: false` | layer/operator coupling pressure | coupling-design support | no final admission |
| root manifold chart/holonomy invariance | `root_manifold_g_structure_holonomy_chart_invariance_probe_results.json` | `formal_scout`, `promotion_allowed: false` | chart reparameterization, two-sheet separation, holonomy gap, varying G-structure pressure, graph/topology/proof witnesses | chart-invariance and hard-graveyard design for root manifold scouts | explicitly blocks real attractor basin, final manifold, final G-structure, final holonomy class |
| full thirteen-layer active G-structure composition | `full_thirteen_layer_active_g_structure_both_chiral_source_native_composition_probe_results.json` | `formal_scout`, `promotion_allowed: false` | 13 active manifold layers; inner SU(2); outer SU(3) -> G2 -> Spin(7); both chiral histories; tensor-network/log-negativity/Berry readouts | source-native paired-chiral composition scout with layer-disabled/random-history graveyards | no final engine, final manifold, final G-structure, physics, or matter/antimatter claim |

## Variant concepts to teach separately

The wiki should not collapse these into one page. At minimum, the learning path needs separate pages or sections for:

1. G-structure as frame-bundle reduction.
2. Classical support-manifold tower baseline.
3. Obstruction tests and branch failures.
4. Nested GL(2,C) -> U(2) -> SU(2) -> Spin(3) -> Weyl chirality chain.
5. Noncommuting reduction order and permutation falsifiers.
6. Hopf/principal-bundle and associated Weyl-section structures.
7. Chart invariance, holonomy gaps, and gauge-invariant observables.
8. SU(3) -> G2 -> Spin(7) special-holonomy projector chain.
9. Thirteen-layer active manifold composition.
10. Why `formal_scout` is not admission.

## Relation to F01 and N01

Every G-structure variant should be checked through the root pair:

- F01: what is the finite/bounded carrier or witness?
- N01: what composition, reduction order, holonomy, chirality, or operator sequence is noncommuting/order-sensitive?

For example:

- reduction-permutation compatibility directly tests N01-style order sensitivity.
- finite 4D metric state and bounded reduction list are F01 witnesses.
- chart/holonomy scout uses finite chart family and finite phase set as F01 witnesses, while holonomy/order pressure handles N01-like behavior.
- thirteen-layer scout uses bounded layer schedule, finite chiral histories, and tensor-network readouts as F01 witnesses; layer order, chiral coupling, holonomy chain, and operator composition carry N01 pressure.

## Claim ceiling discipline

Do not say:

- “the final G-structure is proven”
- “the root manifold is admitted”
- “the attractor basin is real”
- “the engine/axis/physics claim is established”

Safe wording:

- “formal scout passed under its local contract”
- “promotion remains disabled”
- “this variant supplies routing/falsifier evidence”
- “this variant suggests which educational page or next test is needed”
- “this does not yet close the manifold/basin claim contract”

## Next wiki work

Good next pages from this ledger:

1. `g-structure-as-frame-bundle-reduction`
2. `nested-g-reduction-live-state-chain`
3. `g-structure-reduction-order-falsifiers`
4. `root-manifold-holonomy-chart-invariance`
5. `thirteen-layer-active-g-structure-composition`
6. `special-holonomy-su3-g2-spin7-chain`
7. `formal-scout-vs-admission`

## Related pages

- [[g-structure-tower]]
- [[f01-n01-root-constraint-basin-pressure]]
- [[basin-manifold-claim-contract]]
- [[g-tower-hopf-weyl-integration]]
- [[hopf-fibration-mathematics]]
- [[contact-structure-s3]]

## Status fence

Current status: variant ledger / routing page.

This page records observed result surfaces and claim ceilings. It is not a fresh rerun and does not promote any result beyond its artifact status.
