# Subagent Task Card Template v4.3

authority_status: canonical-schema
packet_version: v4.3

```yaml
goal: "<one sentence outcome>"
parent_route: "<decision.context_strategy | failure.falsifier | follow_up.lane_builder | ...>"
child_id: "<stable child id>"
agent_spec_path: "agents/<family>/<agent>.md"
mini_mmm_or_salience_path: "mmm/mini/<...>.md or registry slice id"
scope: "<bounded unit>"
out_of_scope: "<explicit stop list>"
acceptance: "<what must be true for done>"
key_paths:
  - "<absolute or packet-relative path>"
read_first:
  - "taskcards/SUBAGENT_BOOT_RULES_v4_3.md"
  - "<source doc>"
deliverable: "<receipt, patch, report, or artifact>"
falsifier_or_check: "<one concrete check>"
receipt_id: "<run-id>/<child-id>"
parent_id: "<parent route receipt id>"
verify: "<optional verifier>"
closeout_check:
  acceptance: "<acceptance repeated>"
  verifier: "<command or check>"
  result: NOT_RUN
```
