# Subsubagent Boot Rules v4.3

authority_status: canonical-schema
packet_version: v4.3
source_lineage: adapted from `packet-v2-8-expanded-current/boot_rules/md/SUBSUBAGENT_BOOT_RULES_v2_8.md` plus current v4.3 proof-depth rules.

Use only for narrow child checks launched by a parent/subagent.

Read before child task card:

1. inherited positive parent summary;
2. exact v4.3 child mini-MMM or route/member salience set;
3. child task card;
4. one source/check.

Receipt:

- `status`: `spawned | blocked | deferred | not_run | superseded`
- `parent_unit_id`
- `child_unit_id`
- `agent_spec_path`
- `task_card_path`
- `positive_mini_mmm_loaded_before_task`
- `boot_scope`: `inherited_positive_summary_then_child_task`
- `checked`
- `concluded`
- `open`
- `evidence`
- `parent_effect`
- `proof_depth`

Subsubagent proof remains parent-reported unless the controller can read the raw child artifact.
