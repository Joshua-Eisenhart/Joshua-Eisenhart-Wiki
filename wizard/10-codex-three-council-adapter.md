---
title: Codex Adapter For The Three-Council Wizard
created: 2026-05-02
updated: 2026-05-02
packet: v3.5
type: concept
tags: [wizard, codex, adapter, subagents, rerouter]
framing: current
---

# Codex Adapter For The Three-Council Wizard

This is the Codex-specific adapter for the universal Wizard model.

Do not put Codex-only mechanics into the universal model. Claude Bridge, Opus, Codex native subagents, `spawn_agent`, parent/child receipts, and Playwright restrictions are runtime details.

## Codex Mapping

Universal member -> Codex parent subagent.

Member child probe -> Codex child subagent when capacity allows.

External semantic worker -> Claude Bridge / Opus / Sonnet / Gemini only when the run explicitly assigns that runtime.

Controller -> main Codex thread.

Manager/rerouter -> controller-owned scheduling function or explicit manager subagent. It tracks liveness but does not vote, synthesize, or count as a council member.

## Required Proof

A visible council member counts as run only when there is:

- Codex `spawn_agent` id;
- assigned member name and family;
- loaded source/salience slice;
- terminal completion;
- usable output;
- parent-side launch proof for children;
- final receipt state: completed, blocked, deferred, rerouted, superseded, or simulated.

Child/subsubagent work counts only when the parent launch/fanout and child completion both exist. A child id, stream, started task, or self-report is not enough.

Claude Bridge output is external worker evidence, not Codex-native subagent evidence. It needs runtime facts, model/cost/command metadata where available, completion status, and durable output/receipt path.

## Council Run Shape

For judgment runs where the user needs to see the system:

1. Wave 1 Decision Council: run each selected Decision member as its own parent subagent.
2. Wave 2 Failure Council: run each selected Failure member as its own parent subagent.
3. Wave 3 Follow-Up Council: run each selected Follow-up member as its own parent subagent.
4. Each parent should launch narrower children when useful and capacity allows.
5. The manager/rerouter watches liveness and reroutes stuck work smaller.
6. Controller synthesis only combines accepted receipts. It is not a council member.

## Resource Manager

The Codex manager tracks:

- route id;
- member family;
- runtime pool;
- deadline;
- heartbeat/progress;
- receipt validity;
- child fanout status;
- accepted/superseded/blocked state.

Suggested deadlines:

- `ack_deadline`: 30-60 seconds.
- `first_progress_deadline`: first useful signal by 15-25% of wave budget.
- `soft_deadline`: shrink or reroute at 60-70%.
- `hard_deadline`: close, reroute, or supersede at 85-90%.
- `wave_close_deadline`: stop waiting and classify unresolved routes at 100%.

Receipt states:

- `completed`
- `pending`
- `slow`
- `stalled`
- `timed_out`
- `rerouted`
- `superseded`
- `blocked`
- `abandoned`
- `supplemental`

Only `completed` usable receipts count in `subagents:total` or `subsubagents:total`.

## Codex Follow-Up Names

Do not use `Full Wizard` as a composition option name.

Use `Max Assembly` for the maximum useful route-family composition.

`FULL` remains a header/runtime mode, not a composition label.

## Playwright Boundary

For this workspace, do not call Playwright/browser helpers unless the user explicitly asks. If helpers respawn, kill or report them as environment noise; do not open browser surfaces for Wizard runs by default.

## Output

Default visible output should show:

- main answer;
- what changed the answer;
- accepted results and blockers;
- useful follow-up prompts;
- compact route truth only when it matters.

Do not show worker logs, raw receipt ledgers, bridge internals, or timeout chatter unless diagnostics are requested.
