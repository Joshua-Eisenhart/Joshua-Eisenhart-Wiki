# Parent Route Task Card Schema v4.3

authority_status: canonical-schema
packet_version: v4.3

Required fields for every parent route worker:

- `goal`
- `wave`: `Decision Council | Failure Council | Follow-Up Council`
- `parent_route`
- `agent_spec_path`
- `scope`
- `out_of_scope`
- `acceptance`
- `child_routes`
- `key_paths`
- `read_first`
- `deliverable`
- `route_truth_fields`: `action_class`, `execution_claim_state`, `proof_depth`, `evidence_boundary`
- `stop_condition`
- `receipt_id`
- `task_card_path`

The parent route may launch child/subagent workers only after its own route, scope, and acceptance fields are concrete.
