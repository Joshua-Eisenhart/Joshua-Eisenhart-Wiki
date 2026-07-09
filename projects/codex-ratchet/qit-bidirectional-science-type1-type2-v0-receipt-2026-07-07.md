# QIT bidirectional science Type-1/Type-2 v0 receipt - 2026-07-07

Status: repo-grounded scratch diagnostic. This is not canon, not Axis0, not
FEP, not production perception, not an ontology writer, and not Lev mesh
runtime admission.

## Live repo artifact

Repo: `/Users/joshuaeisenhart/Codex-Ratchet`

Packet:
`system_v7/sims/qit_bidirectional_science_type1_type2_v0/`

Primary envelope:
`system_v7/sims/qit_bidirectional_science_type1_type2_v0/results/qit_bidirectional_science_type1_type2_v0_envelope_results.json`

Parent packets:

- `system_v7/sims/qit_projection_battery_v0/`
- `system_v7/sims/qit_full_type1_type2_64_live_v1/`

## What ran

This packet runs paired finite science-method loops over the same four
projection object cards:

- Type-1: candidate -> measurement -> counter-projection -> update -> falsifier -> receipt.
- Type-2: measurement -> candidate -> counter-projection -> update -> falsifier -> receipt.

The object family and view masks are shared. The difference is the method
order. Type-1 starts with a declared candidate object card; Type-2 starts with
a partial measurement and forms the candidate from that view.

## Fresh metrics

- Controller result: `all_pass=true`
- Paired method trials: `40`
- Type-1 nominal accuracy: `1.0`
- Type-1 wrong-candidate accepted rate: `0.1`
- Type-2 nominal accuracy: `0.9`
- Type-2 bag-erased accuracy: `0.25`
- Type-2 view-erased accuracy: `0.25`
- Unique-win table: `18` shared wins, `2` Type-1-only wins, `0` Type-2-only wins, `0` shared failures
- Julia/JAX/PyTorch survivor object-count divergence: `0.0`
- Julia/JAX/PyTorch trial-count divergence: `0.0`
- z3/cvc5/Julia Z3 method-gate negation: `unsat`
- PyTorch role: `torch.func` jacrev/vmap sensitivity of the Type-1 minus Type-2 method margin

## Verification

Passed in the live repo:

```bash
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 system_v7/sims/qit_bidirectional_science_type1_type2_v0/validate_qit_bidirectional_science_type1_type2_v0.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/validate_three_engine_sim_result.py system_v7/sims/qit_bidirectional_science_type1_type2_v0/results/qit_bidirectional_science_type1_type2_v0_envelope_results.json --require-pytorch --strict-source-backed --require-tool-intent
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/lint_sim_contract.py system_v7/sims/qit_bidirectional_science_type1_type2_v0/qit_bidirectional_science_type1_type2_v0.py system_v7/sims/qit_bidirectional_science_type1_type2_v0/qit_bidirectional_science_type1_type2_v0_envelope.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 -m pytest system_v7/sims/qit_bidirectional_science_type1_type2_v0/tests
```

Runtime doctor also reported `ok=true`, `install_state=stable_observed` during
the same work session.

## Honest interpretation

This is the first bounded bidirectional science-method tooth on top of the
projection battery. It shows that Type-1 and Type-2 are not just two labels:
they have different useful failure modes over the same finite object family.

Type-1 confirms and falsifies declared candidates more sharply. Type-2 can form
a candidate from a measurement, but single-view reconstruction remains
ambiguous in two planning-view cases.

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

## Lev import smoke

Lev now has a host-side evidence-only consumer:
`/Users/joshuaeisenhart/GitHub/lev/core/orchestration/src/proof/qit-evidence-consumer.ts`.

Read-only smoke from Lev consumed this envelope as `host_evidence_consumed`.
After refreshing the older `qit_full_type1_type2_64_live_v1` envelope with
the same evidence-only host contract and explicit tool intent, read-only smoke
from Lev consumed all three current QIT envelopes as `host_evidence_consumed`.
The Lev batch consumer now also supports an explicit evidence-only local
quorum; `--quorum=3` over the three current QIT envelopes returned
`host_evidence_quorum_met`.

This confirms only the CR -> Lev evidence receipt boundary. It is not graph
mutation, mesh projection, ontology writing, or runtime object creation. The
local quorum is evidence-only.
