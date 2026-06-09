---
title: Hermes Wizard Receipt Schema
type: schema
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Hermes Wizard Receipt Schema

This schema is for compact route truth. It is not a public proof of scientific truth or repo status.

## Required fields

```yaml
receipt_id: <stable id>
surface_id: <lane/voice/followup/tool/council id>
surface_kind: lane | voice | followup | tool | council | memory | session | cron | process | direct
surface_name: <human-readable name>
action_class: controller_local | tool_run | spawn_worker | enqueue_runner | blocked | deferred | not_run | superseded
route_status: completed | blocked | deferred | not_run | superseded | partial
runtime_target: hermes_controller | hermes_tool | delegate_task | terminal_process | cronjob | external_cli | memory | session_search
what_checked:
  - <file/tool/query/source checked>
conclusion: <what changed or was learned>
remains_open:
  - <unresolved issue or blocker>
artifacts:
  - <path/id/output handle or explicit none>
evidence_boundary: <what this receipt does and does not prove>
next_bounded_move: <next step or stop>
```

## Optional fields

```yaml
worker_id: <delegate/process/cron/tool id>
task_card_path: <path>
source_slice: <file/query/tool surface>
model_or_provider: <if relevant>
blocked_reason: auth_missing | permission_denied | read_restricted | unsupported_model | timeout | tool_error | stale_notice | missing_input | safety_scope
parent_receipt_id: <if nested>
followup_id: <if follow-up route>
execution_claim_state: generated_only | scout_ran_not_full_execution | audit_ran_not_full_execution | future_choice_not_executed | full_execution_ran | blocked_no_execution
render_constraint: <one line the final answer must preserve>
```

## Invalid patterns

- `action_class: spawn_worker` with no worker/tool/process id and no artifact/block reason.
- `memory` receipt used as proof of current execution.
- `session_search` receipt used as proof of current filesystem state.
- `followup_id` offered as a future choice while also claimed as completed execution.
- `controller_local` described as “worker ran”.
- `tool_run` counted as child/subagent work.

## Minimal example

```yaml
receipt_id: hw-20260504-direct-001
surface_id: direct
surface_kind: lane
surface_name: Direct
action_class: tool_run
route_status: completed
runtime_target: hermes_tool
what_checked:
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/README.md
conclusion: General packet exists and is portable, not Hermes-native.
remains_open:
  - Hermes skill not yet created.
artifacts:
  - /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/README.md
evidence_boundary: Proves file content was read/written in this run; does not prove runtime adoption.
next_bounded_move: Create hermes-wizard skill if adopted.
```
