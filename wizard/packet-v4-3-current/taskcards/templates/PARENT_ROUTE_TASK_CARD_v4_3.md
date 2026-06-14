# Parent Route Task Card Template v4.3

authority_status: canonical-schema
packet_version: v4.3

```yaml
goal: "<one sentence outcome>"
wave: "<Decision Council | Failure Council | Follow-Up Council>"
parent_route: "<route id>"
agent_spec_path: "agents/parents/<route id>.md"
scope: "<bounded council/wave unit>"
out_of_scope: "<what this parent must not solve>"
acceptance: "<what must be true for this parent route to count>"
child_routes:
  - "<child id or agent spec>"
key_paths:
  - "WIZARD_v4_3.md"
read_first:
  - "taskcards/PARENT_ROUTE_TASK_CARD_SCHEMA_v4_3.md"
  - "agents/parents/<route id>.md"
deliverable: "<parent receipt>"
route_truth_fields:
  action_class: spawn_worker
  execution_claim_state: not_run
  proof_depth: controller_local
  evidence_boundary: "<what this parent receipt would prove>"
stop_condition: "<when to stop/reroute/block>"
receipt_id: "<run-id>/<parent-route>"
```
