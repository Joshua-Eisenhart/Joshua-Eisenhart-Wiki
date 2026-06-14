# Child Task Card Schema v4.3

authority_status: canonical-schema
packet_version: v4.3
source_lineage: adapted from `packet-v4-1-current/taskcards/CHILD_TASK_CARDS_v4_1.md` and Hermes `TASK_CARD_TEMPLATE.md`.

Every parent-launched child receives a concrete task card with these required fields:

- `goal`
- `parent_route`
- `child_id`
- `agent_spec_path`
- `mini_mmm_or_salience_path`
- `scope`
- `out_of_scope`
- `acceptance`
- `key_paths`
- `read_first`
- `deliverable`
- `falsifier_or_check`
- `receipt_id`
- `parent_id`
- `task_card_path`
- `proof_depth`
- `execution_claim_state`
- `evidence_boundary`

Optional, when measurable:

- `verify`
- `guard`
- `closeout_check`
- `voice_method_check`

## Formal child groups

- `failure.premortem`: `premortem.likely_failure`, `premortem.dangerous_failure`, `premortem.hidden_assumption`, `premortem.early_warning`, `premortem.revised_plan`, `premortem.evidence_corruption`.
- `failure.falsifier`: `voice.popper`, `voice.pushback`, `failure.calibration`, `guard.receipt_audit`, `guard.boundary_check`.
- `follow_up.lane_builder`: `lane.direct`, `lane.alternative`, `lane.reframe`, `lane.back`, `lane.wildcard`, `lane.all_of_the_above`.

If a child lacks an exact mini-MMM file, the sparse registry slice plus definition row is the required salience source. If both are missing, the child is blocked and the parent cannot count it as accepted.
