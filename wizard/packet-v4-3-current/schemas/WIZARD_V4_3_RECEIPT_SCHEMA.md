---
title: Wizard v4.3 Receipt Schema
packet: v4.3
type: schema
---

# Wizard v4.3 Receipt Schema

Minimal portable receipt fields:

```yaml
wizard_version: v4.3
runtime: hermes | claude_code | codex | other
route_name: <name>
action_class: controller_local | tool_run | spawn_worker | spawn_subagent | enqueue_runner | blocked | deferred | not_run | superseded
status: completed | partial | blocked | failed | not_run
support_level: observed | inferred | remembered | proposed | unknown
target: <what route worked on>
receipt: <tool output path / worker id / file path / explicit block reason>
evidence_boundary: <what this does and does not prove>
success_check: <criterion>
stop_if: <failure/retreat condition>
```

A receipt does not promote a claim by itself. The controller must still synthesize what the receipt supports and what remains open.
```
