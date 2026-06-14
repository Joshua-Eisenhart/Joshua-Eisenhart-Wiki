# Taskcards Manifest v4.3

authority_status: canonical-schema
packet_version: v4.3

Task-card files define how v4.3 parent routes, agents, subagents, and subsubagents are instantiated. They are required packet surfaces, not optional notes.

## Active taskcard files

- `SUBAGENT_BOOT_RULES_v4_3.md`: subagent boot order and receipt spine.
- `SUBSUBAGENT_BOOT_RULES_v4_3.md`: narrow child/subchild boot order.
- `PARENT_ROUTE_TASK_CARD_SCHEMA_v4_3.md`: fields for parent route workers.
- `CHILD_TASK_CARD_SCHEMA_v4_3.md`: fields for child/subagent workers.
- `templates/SUBAGENT_TASK_CARD_v4_3.md`: fill-in template for a concrete child/subagent dispatch.
- `templates/PARENT_ROUTE_TASK_CARD_v4_3.md`: fill-in template for a concrete parent route dispatch.

## Rule

A v4.3 agent file is not enough to claim an agent ran. A run receipt must name the agent spec, the task card, the MMM/slice preload, the runtime target, and the observed output or block/defer reason.
