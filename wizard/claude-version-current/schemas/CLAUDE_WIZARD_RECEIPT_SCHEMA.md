---
title: Claude Code Wizard Receipt Schema
type: schema
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
packet_version: v4.3
---

# Claude Code Wizard Receipt Schema

This schema is for compact route truth in Claude Code Wizard runs. It is not a proof of scientific truth, canonical sim status, or repo state. A receipt does not promote a claim; the controller synthesizes what the receipt supports and what remains open.

## Scope

Applies to all three receipt categories: parent/council receipts, child/subagent receipts, and management receipts.

## Action class vocabulary (Claude Code — required values)

```
controller_local   — controller synthesis only; no Agent, no external tool ran
tool_run           — a Claude Code tool ran (Read/Edit/Write/Bash/Skill/Monitor/CronCreate/etc.)
spawn_subagent     — an Agent call was issued and returned; use NOT spawn_worker
enqueue_runner     — CronCreate / /loop / /schedule / run_in_background was created or checked
blocked            — route could not proceed; see blocked_reason
deferred           — route is valid but not yet authorized or in budget
not_run            — route was identified but not attempted this turn
superseded         — a later route replaces this one; both are recorded
```

Do NOT use: `spawn_worker` (Hermes), `delegate_task` (Hermes).

## Runtime target vocabulary (Claude Code — required values)

Runtime targets are matched **case-insensitively** by the validator: the
capitalized tool-named forms below and the lowercase back-compat forms (e.g.
`agent`, `claude_controller`) are both accepted. Use the capitalized tool-named
form for new receipts.

Tool-named forms (preferred):

```
Agent              — Claude Code Agent tool (subagent, fan-out council member, auditor)
Skill              — Claude Code Skill tool (wizard, wizard-council, premortem, sim-*, etc.)
Bash               — Bash tool (local shell, run_in_background, background task)
Read               — Read tool
Edit               — Edit tool
Write              — Write tool
CronCreate         — CronCreate tool (durable recurring runner)
Monitor            — Monitor tool (stream events from background process)
controller_synthesis — controller acts without invoking a separate tool or agent
```

Back-compat controller-named forms (still accepted by the validator):

```
claude_controller  — controller synthesis only (equivalent to controller_synthesis)
claude_tool        — a generic Claude Code tool ran
background_process  — a run_in_background / background task
cron_or_loop        — a CronCreate / /loop / /schedule recurring runner
memory              — a memory read/write surface
none                — no runtime target (controller-only or not applicable)
```

## Required fields — parent / council receipts

```yaml
receipt_id: <stable id, e.g. cw-20260613-decision-001>
surface_id: <lane/voice/council/parent id, e.g. decision.context_strategy>
surface_kind: lane | voice | followup | council | audit | management
surface_name: <human-readable name>
action_class: controller_local | tool_run | spawn_subagent | enqueue_runner | blocked | deferred | not_run | superseded
route_status: completed | partial | blocked | deferred | not_run | superseded
runtime_target: Agent | Skill | Bash | Read | Edit | Write | CronCreate | Monitor | controller_synthesis
what_checked:
  - <file/tool/query/source checked>
conclusion: <what changed or was learned>
remains_open:
  - <unresolved issue or blocker, or explicit none>
artifacts:
  - <path/id/output handle or explicit none>
evidence_boundary: <what this receipt does and does not prove>
next_bounded_move: <next step or explicit stop>
```

## Required fields — child / subagent receipts

All parent fields above, plus:

```yaml
parent_receipt_id: <id of issuing parent receipt>
task_card_path: <path to task card that governed this child>
agent_id: <Agent call id or short handle, e.g. decision.falsifier-001>
execution_claim_state: generated_only | scout_ran_not_full_execution | audit_ran_not_full_execution | future_choice_not_executed | full_execution_ran | blocked_no_execution
proof_depth: parent_reported | controller_visible | artifact_verified | test_passed
```

A `spawn_subagent` receipt MUST have a linked Agent receipt (agent_id + artifact or block reason). A `spawn_subagent` claim with no linked Agent receipt is invalid.

## Required fields — management receipts

All parent fields above (surface_kind: management), plus:

```yaml
managed_surface: memory | wiki | skill | agent | config | cron | repo_code
patch_verified_by: readback | probe | test | result_json | explicit_skip_reason
```

## Optional fields (any receipt type)

```yaml
source_slice: <file/query/tool surface that was the input>
model_or_provider: <if a specific model was routed to>
blocked_reason: auth_missing | permission_denied | read_restricted | unsupported_model | timeout | tool_error | stale_notice | missing_input | safety_scope | budget_exceeded
followup_id: <if this is a follow-up route receipt>
render_constraint: <one line the final output must preserve>
parent_id: <parent receipt id, for nested management receipts>
```

## Follow-Up receipts — additional required fields

```yaml
input_decision_receipt_id: <receipt_id of the Decision receipt consumed>
input_failure_receipt_id: <receipt_id of the Failure receipt consumed>
```

Follow-Up receipts must reference Decision and Failure receipts by id or path. Sequential naming alone is not provenance. A follow-up item is `future_choice_not_executed` unless a separately-authorized branch receipt proves otherwise.

## Invalid patterns

- `action_class: spawn_subagent` with no `agent_id` and no `artifacts` or `blocked_reason`.
- `action_class: spawn_worker` — this is Hermes vocabulary; use `spawn_subagent`.
- `runtime_target: hermes_tool` / `delegate_task` / `terminal_process` / `cronjob` / `session_search` — Hermes vocabulary; use Claude Code equivalents above.
- A `controller_local` receipt described as "Agent ran" or "worker returned".
- A `tool_run` receipt counted as a child subagent receipt.
- A memory read used as proof of current execution state.
- A Follow-Up receipt that does not reference Decision and Failure receipts by id/path.
- `proof_depth: artifact_verified` or `test_passed` without naming the artifact or test.
- `route_status: completed` when `execution_claim_state: future_choice_not_executed`.

## Minimal example — parent / council receipt

```yaml
receipt_id: cw-20260613-decision-ctx-001
surface_id: decision.context_strategy
surface_kind: council
surface_name: Decision — Context & Strategy
action_class: spawn_subagent
route_status: completed
runtime_target: Agent
agent_id: decision-ctx-agent-001
what_checked:
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-3-current/agents/parents/decision.context_strategy.md
  - /Users/joshuaeisenhart/wiki/wizard/claude-version-current/01_RUNTIME_CONTRACT.md
conclusion: Context framed; two live candidate strategies remain, both admitted under current constraints.
remains_open:
  - Which strategy survives Failure council falsification.
artifacts:
  - runs/SMOKE_TOPOLOGY_20260613/decision-receipt.md
evidence_boundary: Proves context was read and two candidates named; does not prove either strategy is the correct move.
next_bounded_move: Pass decision-receipt.md to Failure council.
parent_receipt_id: none
task_card_path: runs/SMOKE_TOPOLOGY_20260613/task-cards/decision-ctx.yaml
execution_claim_state: full_execution_ran
proof_depth: artifact_verified
```

## Minimal example — child / subagent receipt (Failure council child)

```yaml
receipt_id: cw-20260613-failure-falsifier-001
surface_id: failure.falsifier
surface_kind: council
surface_name: Failure — Falsifier (voice-popper)
action_class: spawn_subagent
route_status: completed
runtime_target: Agent
agent_id: failure-falsifier-agent-001
parent_receipt_id: cw-20260613-failure-001
task_card_path: runs/SMOKE_TOPOLOGY_20260613/task-cards/failure-falsifier.yaml
what_checked:
  - runs/SMOKE_TOPOLOGY_20260613/decision-receipt.md
  - /Users/joshuaeisenhart/wiki/wizard/packet-v4-3-current/agents/parents/failure.falsifier.md
conclusion: Strongest falsifier identified; one candidate strategy killed; one survives.
remains_open:
  - Survival requires loophole-auditor check before promotion.
artifacts:
  - runs/SMOKE_TOPOLOGY_20260613/failure-falsifier-receipt.md
evidence_boundary: Proves one falsifier was applied; does not prove all failure modes surveyed.
next_bounded_move: Pass to loophole-auditor child, then compile Failure receipt.
execution_claim_state: full_execution_ran
proof_depth: artifact_verified
```

## Status labels (apply to all receipts)

`exists < runs < passes local rerun < canonical by process`

Never write "verified," "confirmed," or "all pass" without naming which criterion was checked and citing the result artifact path from this session.
