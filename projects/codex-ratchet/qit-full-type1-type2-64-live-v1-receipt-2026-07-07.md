# QIT full Type1/Type2 64 live v1 receipt — 2026-07-07

Status: repo-grounded scratch diagnostic. This is not canon, not Axis0, not FEP,
not production perception, and not Lev mesh runtime admission.

## Live repo artifact

Repo: `/Users/joshuaeisenhart/Codex-Ratchet`

Packet:
`system_v7/sims/qit_full_type1_type2_64_live_v1/`

Primary envelope:
`system_v7/sims/qit_full_type1_type2_64_live_v1/results/qit_full_type1_type2_64_live_v1_envelope_results.json`

## What ran

The packet builds a finite 64-slot carrier from `ENGINE_64_SCHEDULE_ATLAS.md`:

- 4 loop objects
- 16 macro rows
- 4 substages per macro row
- 64 slots total
- 32 Type-1 slots
- 32 Type-2 slots
- 16 chart-locked macro cells
- 48 bounded runtime probe cells

The finite object test is order-sensitive. Ordered observations recover the
hidden loop object. Static/bag-erased projections collapse identity.

## Fresh metrics

- Controller result: `all_pass=true`
- Ordered object recovery: `1.0`
- Mean entropy drop: `2.0` bits
- Bag-topology control unique signatures: `1`
- First-static control unique signatures: `1`
- PyTorch ordered readout accuracy: `1.0`
- PyTorch bag-control accuracy: `0.25`
- Julia/JAX/PyTorch survivor object-count divergence: `0.0`
- z3/cvc5 full-gate negation: `unsat`
- erased control: `sat` / collapsed

## Verification

Passed in the live repo:

```bash
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 system_v7/sims/qit_full_type1_type2_64_live_v1/qit_full_type1_type2_64_live_v1_envelope.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 system_v7/sims/qit_full_type1_type2_64_live_v1/validate_qit_full_type1_type2_64_live_v1.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/validate_three_engine_sim_result.py system_v7/sims/qit_full_type1_type2_64_live_v1/results/qit_full_type1_type2_64_live_v1_envelope_results.json --require-pytorch --strict-source-backed --require-tool-intent
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/lint_sim_contract.py system_v7/sims/qit_full_type1_type2_64_live_v1/qit_full_type1_type2_64_live_v1.py system_v7/sims/qit_full_type1_type2_64_live_v1/qit_full_type1_type2_64_live_v1_envelope.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 -m pytest system_v7/sims/qit_full_type1_type2_64_live_v1/tests/test_qit_full_type1_type2_64_live_v1.py
```

Runtime doctor also reported `ok=true`, `install_state=stable_observed`.

## Honest interpretation

This is a real narrow tooth: the model can create finite object cards from an
ordered stream and reject weaker projections as insufficient. PyTorch is useful
as the learnable readout layer in this packet.

This is still not live perception. It has no real-world sensor loop, no mesh
object factory, no Axis0 bridge, no FEP closure, and no production Lev OS
integration.

## Lev boundary refresh

The envelope now carries the same evidence-only Lev host-consumer contract as
the newer QIT projection and bidirectional packets:

- `truth_state: proposed`
- `evidence_kind: measurement`
- `decision_ceiling: accepted_as_evidence_only`
- `graph_mutation_allowed: false`
- `compositor_apply_allowed: false`
- `mesh_projection_allowed: false`
- `source_boundary_mutated: false`
- `cr_object_id_is_lev_entity_id: false`

It also carries explicit `tool_intent` for Julia Graphs/Z3, JAX z3/cvc5, and
PyTorch `torch.func`. Read-only Lev smoke consumed this envelope as
`host_evidence_consumed`; graph mutation and source boundary mutation remained
false.
