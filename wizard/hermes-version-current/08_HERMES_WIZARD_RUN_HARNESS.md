---
title: Hermes Wizard Run Harness
created: 2026-05-04
updated: 2026-06-05
type: run_harness
runtime: hermes
status: draft-live
---

# Hermes Wizard Run Harness

## Purpose

This harness fixes the failure mode where Hermes produces Wizard-shaped prose without a real Wizard-shaped run.

It defines the minimum live contract for a Hermes-native Wizard run before execution begins.

## Run modes

- `SMOKE_FORMAT` — render the attractive Wizard surface from sample or partial receipts. Must not claim real council execution.
- `SMOKE_TOPOLOGY` — test parent/child/subchild route proof. Formatting may be secondary.
- `REAL_ATTEMPT_PARTIAL` — run Decision -> Failure -> Follow-Up as sequential LLM councils, but selected parent/member or child/subchild coverage is incomplete or parent-reported only.
- `REAL_ATTEMPT_FULL` — run Decision -> Failure -> Follow-Up as three LLM councils with selected parent/member coverage, wide intra-council child/subchild fanout where supported, exact visibility labels, and final validation.

## Breadth selectors

`full` and `auto` are orthogonal to the run mode:

- `full` attempts every admitted relevant council, lane, skill, worker, model, and tool route in the declared scope. It still reports `REAL_ATTEMPT_PARTIAL` or `BLOCKED` when receipts, visibility, or validation are incomplete.
- `auto` picks the smallest set of routes likely to change the answer or compiled move. Any skipped decision-relevant route is shown as `not_run` or `deferred` with the reason.

Neither selector authorizes hidden routes, fake worker proof, fixed child quorum, or Max Assembly default behavior.

## What counts

### Wave
A wave is a sequential council barrier that consumes the prior wave's output artifact or receipt.

- Decision can run first.
- Failure must consume the Decision receipt.
- Follow-Up must consume Decision and Failure receipts.

Three sibling delegate calls are not three waves unless the dependency chain is real.

### Council
A council is a named LLM wave with selected members whose work is run before that council returns.

For v4.1, the primary council identities are fixed:

1. Decision Council.
2. Failure Council.
3. Follow-Up Council.

Parallelism belongs inside each council. A council may be partial if Hermes can only launch a narrow member set, but that partial state must be visible. A single parent summary for a council is not full v4.1 council coverage unless it carries accepted member and child/subchild receipts for the selected council work.

### Wide intra-council fanout
When the runtime supports it, each council should launch multiple parent/member routes and each counted parent should launch useful child/subchild variants.

Useful child/subchild variants include:

- source-slice scout;
- falsifier or boundary check;
- mini-MMM salience check;
- receipt audit;
- same invariant under a different model/reasoning level;
- follow-up prompt improver;
- outside-frame critique.

A child route is blocked only by a concrete runtime/access/safety/timeout reason, not by "nothing useful for a child to do."

### Parent route
A parent route is one controller-launched `delegate_task` for a council wave.

### Child/subchild route
A child or subchild route counts only when the returned parent receipt names:

- child route id or label;
- child role/member;
- status;
- conclusion;
- evidence boundary;
- whether raw child transcript is controller-visible.

If raw nested transcripts are not exposed, mark nested proof as `reported_by_parent`, not `controller_verified_raw`.

## Required receipt fields

```yaml
run_id: <id>
mode: SMOKE_FORMAT | SMOKE_TOPOLOGY | REAL_ATTEMPT_PARTIAL | REAL_ATTEMPT_FULL
wave: Decision | Failure | Follow-Up | Final Audit
parent_route_id: <id>
input_receipts:
  - <prior receipt id or none>
selected_member_obligation:
  expected: <n>
  completed: <n>
child_subchild_obligation:
  expected: <n or unknown>
  completed_accepted: <n>
  visibility: controller_verified_raw | reported_by_parent | none
member_routes:
  - id: <member id>
    role: <member role>
    status: completed | blocked | degraded | not_run
    conclusion: <one-line result>
    evidence_boundary: <what is and is not proven>
nested_visibility: controller_verified_raw | reported_by_parent | none
model_request: <requested model/effort>
model_observed: <observed model/effort or unknown>
verdict: pass | harden | split | block | kill | generated
artifact_surface: <path or terminal-only>
```

## Human-load visual template

Wizard formatting is not a receipt dump. Its job is to reduce the reader's cognitive load by doing the sorting work for them.

Render in this order:

1. State the changed state in one sentence.
2. Name the best next move before showing proof.
3. Compress Decision, Failure, and Follow-Up into cards that explain why the move was selected.
4. Put receipt paths and route truth in a proof strip, not the main body.
5. Generate copy-pasteable next prompts, with payoff and stop condition.
6. Keep explicit boundaries visible: nested visibility, model/effort truth, validator status.

```text
🧙 Hermes Wizard v4.1 — <MODE> — <PASS|PARTIAL|BLOCKED>

What changed
<one-sentence state change>

Best next move
✅ <the move the councils compiled>

Why this is the best move
- 🧠 Decision: <choice and reason>
- 🛡️ Failure: <risk caught and hardening>
- 🧭 Follow-Up: <prepared continuation>

✅ Compiled move
Target: ...
Action: ...
Owner: ...
Success check: ...
Stop condition: ...
Artifact: ...
Evidence boundary: ...

Follow-up — pick a number
1. <copy-pasteable prompt>
   Payoff: ...
   Stop if: ...
2. <copy-pasteable prompt>
   Payoff: ...
   Stop if: ...

Proof strip
Validator: ...
Nested visibility: controller_verified_raw | reported_by_parent | none
Model: requested <...> · observed <...>
Receipts: <paths or compact list>
```

The log-shaped route table belongs in diagnostics or receipts, not the default user-facing Wizard surface.

Follow-up options use the compiler contract in `01_RUNTIME_CONTRACT.md`: lane/voice, action class, execution claim state, payoff/use condition, acceptance, closeout check, and stop condition may stay internal, but the visible line must be traceable to those fields.

## Collapse response table

Use this table when route plurality, agreement, or synthesis looks collapsed:

| Finding | Required response |
|---|---|
| `decorative_split` | drop the label or rerun with a sharper task |
| `shared-premise convergence` | rerun with an independent source or falsifier |
| `missing receipt` | demote to partial, block, or mark `not_run` |
| `dropped live split` | respawn the split or cite bounded exclusion evidence |

Then render through the normal Hermes scaffold:

- Main answer
- Results
- Follow-up
- Hygiene & Security
- Footer

## Validator

Fail closed if any of these are true:

- Mode is missing.
- `REAL_ATTEMPT_FULL` lacks wide member/child obligations.
- A run claims v4.1 council conformance from only one parent route per council.
- Selected member obligations are absent or hidden.
- Child/subchild obligations are absent, hidden as `0/0`, or marked blocked without a concrete runtime/access/safety/timeout reason.
- Failure did not consume Decision.
- Follow-Up did not consume Decision and Failure.
- A council is claimed without a parent receipt.
- A child/subchild is claimed without a named member route in the returned receipt.
- Raw nested transcript is implied but only a parent summary exists.
- Model/effort is stated as fact when only requested.
- Output lacks the visual Wizard surface.
- Follow-up options are worded as executed when they are future choices.
- Meaningful skipped routes are hidden instead of marked `not_run`.
- Distinct receipts are falsely merged without bounded exclusion evidence.
- A collapse finding has no drop, rerun, demote, block, respawn, or exclusion response.

## Boundary

This harness is Hermes-native. It does not copy Codex Max Assembly, Codex scored headers, or Codex fixed child quorums. It imports only the useful structure: sequential barriers, route truth, receipts, follow-up prework, and visible formatting discipline.
