---
title: Classical Baseline vs Canonical Tool Boundary
created: 2026-04-13
updated: 2026-05-21
type: concept
tags: [concept, research, tooling, simulation, validation, qit, constraints]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_sasakian_structure_s3.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_contact_structure_s3.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_hopf_foliation_structure.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_g_structure_tower.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_weyl_chirality_bipartite.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_weyl_relay_gradient_sweep.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_weyl_bipartite_to_3q_coupling.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_su2_killing_form_exhaustion.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_gstructure_compatibility_coupling.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_axis0_pyg_proxy.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_four_topology_pauli_map.py
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/enforcement-process-rules-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/tool-function-receipt-status.md
framing: concept_policy_snapshot
---

# Classical Baseline vs Canonical Tool Boundary

## Overview
A key architectural clarification from this session is that numpy-first sims are not failures by default. They are often the right classical baseline layer.

The real problem is not using numpy. The real problem is misclassifying a numpy-primary sim as if it were already a canonical tool-native sim.

Current contract/status mirrors:
- [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]]
- [[specs/codex-ratchet/enforcement-process-rules-current|enforcement-process-rules-current]]
- [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]]
- [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]]

## The rule
- `classification: classical_baseline`
  - numpy or other classical substrate computes the primary objects
  - richer tools may check, cross-validate, or pressure the result
- `classification: canonical`
  - the nonclassical / tool-native stack computes the primary objects or primary structural claims
  - proof, symbolic, geometric-algebra, graph, or tensor tools are genuinely load-bearing

This makes the boundary explicit:
- baseline = classical reference realization
- canonical = tool-native constraint-enforced realization

Hard caveat: a nonclassical/source-native sim cannot use NumPy as the load-bearing substrate or hide a NumPy conversion behind `.numpy()` and still count as nonclassical. NumPy belongs in the classical baseline lane unless the current repo contracts and receipts say otherwise.

## Why this helps
This lets the project do both things honestly:
1. build a numpy version of everything
2. then build the correct nonclassical counterpart

The difference between the two becomes a real documented boundary rather than a vague aspiration.

## Dated examples from the 2026-04-13 session
These examples were verified in the April session from probe files and result JSONs. Treat them as dated examples of the boundary, not as the current complete repo status.

### Classical baseline examples
- `sim_sasakian_structure_s3.py` -> `classical_baseline`
- `sim_contact_structure_s3.py` -> `classical_baseline`
- `sim_hopf_foliation_structure.py` -> `classical_baseline`
- `sim_g_structure_tower.py` -> `classical_baseline`
- `sim_weyl_chirality_bipartite.py` -> `classical_baseline`
- `sim_weyl_relay_gradient_sweep.py` -> `classical_baseline`
- `sim_weyl_bipartite_to_3q_coupling.py` -> `classical_baseline`

### Canonical examples
- `sim_su2_killing_form_exhaustion.py` -> `canonical`
- `sim_gstructure_compatibility_coupling.py` -> `canonical`
- `sim_axis0_pyg_proxy.py` -> `canonical`
- `sim_four_topology_pauli_map.py` -> `canonical`

## How to read the boundary
The operational question is not “does this sim import a fancy tool?”
It is:
- what computes the object that carries the claim?
- what tool is actually load-bearing in the claim path?

If numpy computes the geometry and the formal tools only check properties of that output, the sim belongs on the baseline side.
If sympy/z3/torch/clifford/PyG/etc. actually compute the primary structure, the sim can belong on the canonical side.

## Why this is good for the plan
This supports the current planning direction:
- build numpy baselines broadly
- then build canonical tool-native counterparts
- document the difference between them
- use that difference to teach the system what the tools actually add

That makes the tool-capability-sim lane much more concrete.

## How it connects
- [[tool-capability-sim-program]]
- [[tooling-status]]
- [[specs/codex-ratchet/lego-sim-contract-current]]
- [[specs/codex-ratchet/sim-estate-integration-status]]
- [[support-first-constraint-manifold-dependency-chain]]
- [[research-inventory-and-foundations]]
- [[pytorch-ratchet-build-plan]]
