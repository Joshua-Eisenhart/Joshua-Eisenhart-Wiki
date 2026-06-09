---
title: Exceptional Lie Group Series (G2, F4, E6, E7, E8)
created: 2026-04-15
updated: 2026-05-21
type: concept
tags: [g-tower, lie-groups, exceptional, e8, g2, f4, e6, e7, cartan, weyl, xgi, simulation, constraint-geometry]
sources:
  - sim_gtower_g2_exceptional_geometry
  - sim_gtower_f4_exceptional_geometry
  - sim_gtower_e6_exceptional_geometry
  - sim_gtower_e7_exceptional_geometry
  - sim_gtower_e8_exceptional_geometry
  - sim_gtower_e8_lattice_unimodular
  - sim_gtower_e8_root_system_240
  - sim_e8_weyl_rotor_length_preservation
framing: historical_candidate_geometry
---

# Exceptional Lie Group Series (G2, F4, E6, E7, E8)

## Core claim

The five exceptional compact simple Lie groups — G2, F4, E6, E7, E8 — are
source-reported candidate geometries in the G-tower hypergraph. They are NOT in
the main reduction chain. G2 and F4 are pendant nodes (degree-1 in XGI) attached
via group containment; the E-series forms a standalone exceptional family. E8 is
the terminal exceptional group: no larger exceptional group exists.

**Status**: reported candidate geometry, not current live receipt authority and
not a bridge proof. Check current repo/spec mirrors before citing as validated
status. Do not collapse to theorem.

---

## G-tower placement

The G-tower main reduction chain runs:

```
GL(3) → O(3) → SO(3) → SU(3) → Sp(6) → ...
```

The exceptional groups attach as follows:

| Group | Attachment point | XGI node degree | Role |
|---|---|---|---|
| G2 | SU(3) containment | 1 (pendant) | Off-chain; G2 ⊃ SU(3) |
| F4 | Sp(6)/B4=SO(9) containment | 1 (pendant) | Off-chain; F4 ⊃ B4 ⊃ Sp(6) |
| E6 | Standalone exceptional family | — | Not in main chain |
| E7 | Standalone exceptional family | — | Not in main chain |
| E8 | Terminal exceptional group | — | No larger exceptional group |

Pendant node (degree-1) means G2 and F4 do not lie on any reduction path between two other nodes — they are leaves. The XGI G-tower hypergraph encodes this structurally: removing a pendant node does not disconnect the chain.

---

## Reported Packet Instances

| Group | Rank | Dim | Cartan det | Root structure | Sim |
|---|---|---|---|---|---|
| G2 | 2 | 14 | 1 | Non-simply-laced; off-diagonal ∉ {0,−1} | `sim_gtower_g2_exceptional_geometry` |
| F4 | 4 | 52 | 1 | Non-simply-laced | `sim_gtower_f4_exceptional_geometry` |
| E6 | 6 | 78 | 3 (or 6 Bourbaki) | Simply-laced; all off-diagonal ∈ {0,−1} | `sim_gtower_e6_exceptional_geometry` |
| E7 | 7 | 133 | 2 | Simply-laced | `sim_gtower_e7_exceptional_geometry` |
| E8 | 8 | 248 | 1 | Simply-laced; unimodular; 240 roots, all length²=2 | `sim_gtower_e8_exceptional_geometry`, `sim_gtower_e8_lattice_unimodular`, `sim_gtower_e8_root_system_240` |

**E8 special properties (reported in the packet):**
- Unimodular lattice (Cartan det=1): unique in the E-series. E6 has det=3 (or 6), E7 has det=2.
- All 240 roots have equal length² = 2: the root system is uniform.
- Weyl rotor (SO(8)) action preserves root length² = 2 in the reported sim `sim_e8_weyl_rotor_length_preservation`; treat G-tower × Weyl compatibility as a candidate compatibility result until current receipts are checked.
- Terminal: the classification of simple Lie groups yields no larger exceptional group beyond E8.

---

## Structural dividing lines

### Simply-laced vs non-simply-laced

This is the primary structural division in the exceptional series:

| Category | Groups | Property |
|---|---|---|
| Simply-laced (ADE) | E6, E7, E8 | All roots same length; all off-diagonal Cartan entries ∈ {0,−1} |
| Non-simply-laced | G2, F4 | Roots of two different lengths; Cartan matrix asymmetric |

**Consequence for G-tower**: non-simply-laced groups (G2, F4) have asymmetric Cartan matrices — the reduction structure is directional. Simply-laced groups (E6/E7/E8) have symmetric Cartan matrices, meaning the root geometry is more uniform and admits different coupling behavior.

The non-commutative ordering test applies here: G2 and F4 containments must be tested in both directions (G2∘SU(3) vs SU(3)∘G2) before treating them as ratchet steps. Symmetric Cartan ≠ commutative containment.

### Cartan determinant gradient in E-series

Along E6 → E7 → E8, the Cartan determinant decreases: 3 (or 6) → 2 → 1. E8 is the unique unimodular endpoint. This gradient is a candidate structural signal, not yet a proven invariant.

---

## Anti-smoothing caveat

- **Do not** treat pendant node placement as a theorem about all possible G-tower topologies. Pendant = degree-1 in the current XGI hypergraph; different hyperedge definitions could change degree.
- **Do not** treat E8 unimodularity as implying E8 is the "correct" or "final" object in the G-tower. E8 is the terminal exceptional group by classification; whether it is relevant to the Codex Ratchet constraint program is an open question.
- **Do not** infer from E8's 240 roots being all length²=2 that the root system is "simple" in any physics sense — it is maximally complex.
- **Open**: E-series coupling behavior with the main reduction chain is not yet simmed. Placement as "standalone exceptional family" is structural, not coupling-tested.
- **Open**: Whether G2/F4 pendant attachment introduces log(2) or other entropy cost at the attachment node is not yet determined.

---

## Connection to Weyl geometry

The Weyl rotor (SO(8) action) preserves E8 root length²=2 in the reported `sim_e8_weyl_rotor_length_preservation` packet. Candidate reading:

> The G-tower and the Weyl geometry stack are **compatible** at the E8 level under the SO(8) rotor action.

This is a candidate compatibility result, not a proof that Weyl geometry and E8 are the same object. The ratchet doctrine requires testing both orderings (Weyl∘E8 vs E8∘Weyl) and checking for non-commutativity before treating any stacking as a constraint ratchet step.

---

## Related pages

- [[log2-z2-structural-constant]] — Cartan det=1 (G2, F4, E8) vs det>1 (E6, E7): does the unimodular/non-unimodular split carry a log entropy cost?
- [[axis0-current-doctrine-state-card]] — G-tower entropy reduction chain; SU(3) is the attachment point for G2
- [[g-tower-hopf-weyl-integration]] — Main reduction chain and Weyl geometry stack
- [[shell-local-to-coupled-program]] — Coupling program order; pendant nodes require shell-local sims before coupling
