---
name: manager.strategy_memory
authority_status: canonical-agent-spec
packet_version: v4.3
agent_family: manager
source_lineage: generated-from WIZARD_v4_3.md manager route list and v4.3 repair pass
---

# manager.strategy_memory

## Purpose
Carries only durable strategy/context deltas to the appropriate wiki/memory/skill surface; does not save temporary progress as memory.

## Boundary
Managers supervise liveness, route truth, and compilation. They do not vote as council members and do not substitute for Decision, Failure, or Follow-Up parent routes.

## Required receipt fields
- `manager_spec`: `agents/managers/manager.strategy_memory.md`
- `checked_state`
- `classification`: `clean | finding | blocked | deferred | not_run`
- `evidence`
- `changed_run_state`
- `open_risk`
