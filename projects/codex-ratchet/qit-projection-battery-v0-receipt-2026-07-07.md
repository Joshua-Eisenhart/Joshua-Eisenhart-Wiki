# QIT projection battery v0 receipt — 2026-07-07

Status: repo-grounded scratch diagnostic. This is not canon, not Axis0, not FEP,
not production perception, not an ontology writer, and not Lev mesh runtime
admission.

## Live repo artifact

Repo: `/Users/joshuaeisenhart/Codex-Ratchet`

Packet:
`system_v7/sims/qit_projection_battery_v0/`

Primary envelope:
`system_v7/sims/qit_projection_battery_v0/results/qit_projection_battery_v0_envelope_results.json`

Parent packet:
`system_v7/sims/qit_full_type1_type2_64_live_v1/`

## What ran

This packet consumes the finite v1 object-card carrier and tests whether five
partial MMM-style projection views converge to the same four underlying loop
objects.

The nominal views are:

- `maintenance_mmm`
- `finance_mmm`
- `safety_mmm`
- `planning_mmm`
- `ontology_mmm`

The nominal masks intentionally exclude direct `loop` and `engine_type` fields.
Those fields exist in the parent carrier and would trivially identify the four
objects, so the packet records them only as an overclaim hazard.

## Fresh metrics

- Controller result: `all_pass=true`
- Nominal mean held-out projection accuracy: `0.9`
- Bag-erased control mean: `0.25`
- View-erased control mean: `0.25`
- Julia/JAX/PyTorch survivor object-count divergence: `0.0`
- Julia/JAX/PyTorch projection view-count divergence: `0.0`
- z3/cvc5 full-gate negation: `unsat`
- erased controls: `sat` / chance
- PyTorch role: tiny learned prototype readout plus `torch.func` jacrev/vmap sensitivity

## Verification

Passed in the live repo:

```bash
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 system_v7/sims/qit_projection_battery_v0/validate_qit_projection_battery_v0.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/validate_three_engine_sim_result.py system_v7/sims/qit_projection_battery_v0/results/qit_projection_battery_v0_envelope_results.json --require-pytorch --strict-source-backed --require-tool-intent
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/lint_sim_contract.py system_v7/sims/qit_projection_battery_v0/qit_projection_battery_v0.py system_v7/sims/qit_projection_battery_v0/qit_projection_battery_v0_envelope.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 -m pytest system_v7/sims/qit_projection_battery_v0/tests
```

Runtime doctor also reported `ok=true`, `install_state=stable_observed` during
the same work session.

## Honest interpretation

This is a stronger object-factory scout than the v1 ordered-stream packet:
multiple partial projections can point back to one finite object family, while
erased controls fail at chance.

It is still bounded. It has no real-world sensor loop, no production object
factory, no Axis0/FEP closure, no ontology writer authority, no MMM driver
admission, and no production Lev OS integration.

## Lev boundary

The envelope carries a Lev host-consumer contract:

- `truth_state: proposed`
- `evidence_kind: measurement`
- `decision_ceiling: accepted_as_evidence_only`
- `graph_mutation_allowed: false`
- `compositor_apply_allowed: false`
- `mesh_projection_allowed: false`
- `source_boundary_mutated: false`

CR object ids and survivor hashes are evidence keys only. They are not Lev
entity ids.
