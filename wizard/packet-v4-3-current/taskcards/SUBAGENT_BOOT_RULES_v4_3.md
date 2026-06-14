# Subagent Boot Rules v4.3

authority_status: canonical-schema
packet_version: v4.3
source_lineage: adapted from `packet-v2-8-expanded-current/boot_rules/md/SUBAGENT_BOOT_RULES_v2_8.md` plus current v4.3 MMM/route-truth rules.

Read before task card:

1. shared L0 / current context pack when provided by the parent;
2. exact v4.3 mini-MMM or route/member salience set for the assigned agent;
3. `WIZARD_v4_3.md` route-truth field contract;
4. this boot rule;
5. concrete task card;
6. task-specific source files/tools.

Receipt:

- `status`: `spawned | blocked | deferred | not_run | superseded`
- `agent_spec_path`
- `task_card_path`
- `positive_mini_mmm_loaded_before_task`: yes/no/path
- `boot_scope`: `v4_3_mini_mmm_then_task`
- `checked`
- `concluded`
- `open`
- `evidence`
- `artifact_or_output`
- `proof_depth`
- `execution_claim_state`

If the agent did not load the assigned salience before the task card, its output is `receipt-candidate` only and cannot count as MMM-backed topology.
