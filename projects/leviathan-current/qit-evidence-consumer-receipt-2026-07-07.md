# QIT Evidence Consumer Receipt - 2026-07-07

> **Current read-through:** [[projects/leviathan-current/qit-evidence-boundary-refresh-2026-07-09]] records the split-worktree and current ProofBundle/idempotency gap. This receipt proves the July 7 evidence-only consumer shape and tests; it does not prove current integration into upstream main or authorize mesh mutation.

Status: Lev-side evidence-only importer implemented and smoke-tested. This is
not Lev mesh runtime admission, graph mutation, ontology writing, MMM driver
authority, or production perception.

## Live repo artifacts

Repo: `/Users/joshuaeisenhart/GitHub/lev`

Files:

- `core/orchestration/src/proof/qit-evidence-consumer.ts`
- `core/orchestration/src/handlers/qit-evidence.ts`
- `core/orchestration/src/proof/qit-evidence-consumer.test.ts`
- `core/orchestration/src/handlers/qit-evidence.test.ts`
- `core/orchestration/config.yaml`

## What it does

The consumer imports Codex-Ratchet QIT three-engine envelope results as
host-owned Lev receipts with this ceiling:

```yaml
truth_state: proposed
evidence_kind: measurement
decision_ceiling: accepted_as_evidence_only
graph_mutation_allowed: false
compositor_apply_allowed: false
mesh_projection_allowed: false
source_boundary_mutated: false
cr_object_id_is_lev_entity_id: false
```

It rejects truthy source-side promotion/runtime/graph authority fields and
requires `blocked_consumers` plus an explicit `lev_host_consumer_contract`.

## Fresh validation

```sh
pnpm --dir /Users/joshuaeisenhart/GitHub/lev/core/orchestration exec vitest run src/proof/qit-evidence-consumer.test.ts src/handlers/qit-evidence.test.ts
pnpm --dir /Users/joshuaeisenhart/GitHub/lev/core/orchestration run typecheck
pnpm --dir /Users/joshuaeisenhart/GitHub/lev/core/orchestration test
```

Result: `9` focused tests passed; TypeScript typecheck passed; the full
orchestration suite passed `850` tests across `55` files.

## Live read-only smoke

Against current Codex-Ratchet QIT envelopes:

- `qit_full_type1_type2_64_live_v1`: `host_evidence_consumed`.
- `qit_projection_battery_v0`: `host_evidence_consumed`.
- `qit_bidirectional_science_type1_type2_v0`: `host_evidence_consumed`.

Interpretation: the receipt/evidence bridge exists and has teeth, because it
now passes all three current bounded QIT envelopes after the v1 envelope was
refreshed with the host-boundary contract. It still does not create Lev objects
or mutate the mesh.

## Local quorum update

The batch handler now supports an explicit k-of-n local evidence quorum:

```sh
lev orchestration qit-evidence batch <root-dir-or-envelope> --quorum=N
```

Default behavior remains all-envelopes-required. With `--quorum=N`, the batch
result records `k_of_n_local_verifier` and a quorum object with:

- `required`
- `observed`
- `met`
- distinct accepted sim ids
- `decisionCeiling: accepted_as_evidence_only`
- graph/mesh/source mutation flags false

Fresh validation: focused tests `11/11` passed, TypeScript typecheck passed,
and the full orchestration suite passed `852` tests across `55` files.

Live smoke over the three current QIT envelopes with `--quorum=3` returned
`host_evidence_quorum_met`, `3/3` distinct evidence envelopes, `blocked=0`,
and `reviewed_failed=0`.
