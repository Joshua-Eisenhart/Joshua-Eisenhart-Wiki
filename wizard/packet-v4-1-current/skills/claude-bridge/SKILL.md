---
name: claude-bridge
description: Run Claude Code from Codex when the user asks to use Claude, Opus, Sonnet, Haiku, Claude subagents, or a mixed Claude/Codex review. Provides simple model routing, budget caps, receipt capture, and stream-json evidence for real Agent/Task use.
---

# Claude Bridge

Use this skill when Codex should call Claude Code as an external worker from the current session.

## Quick Start

Prefer the wrapper script:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model opus \
  --prompt "Review this plan and return risks plus a verdict."
```

For prompts in a file:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model sonnet \
  --prompt-file /tmp/prompt.txt \
  --budget 3
```

For Claude Agent/Task evidence, use stream mode:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model opus \
  --stream \
  --tools Task,Read,Grep,Glob,Bash,Write \
  --prompt "Use Agent/Task to launch haiku and sonnet workers, then synthesize."
```

For bounded parent-to-child fanout from a Codex subagent, prefer the fanout
wrapper. It gives every child a wall-clock timeout and returns one parent-readable
receipt:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_child_fanout.py \
  --name parent-scale-test \
  --model sonnet \
  --effort high \
  --budget 1 \
  --timeout-sec 90 \
  --max-concurrency 4 \
  --jobs-file /tmp/child_jobs.json
```

Use direct `claude_bridge.py` for one child. Use `claude_child_fanout.py` for
two or more children.

When several Codex parents may launch Claude children at the same time, add a
shared model-level limiter:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_child_fanout.py \
  --name parent-wave-limited \
  --model haiku \
  --budget 1 \
  --timeout-sec 120 \
  --max-concurrency 4 \
  --stop-after-completed 4 \
  --global-timeout-sec 120 \
  --global-max-active 8 \
  --jobs-file /tmp/child_jobs.json
```

Use `--stop-after-completed` for scouting routes where a useful subset is
enough. Use `--global-max-active` to prevent many Codex parents from starting
too many Claude CLI children at once.

Summarize completed fanout receipts with:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/fanout_receipt_summary.py \
  --route-prefix parent-wave-limited \
  --show-routes
```

Use the summary utility before reporting Wizard header counts. It counts
completed child receipts, separates abandoned/not-launched children, and avoids
turning final answers into log parsing.

## Model Routing

- `opus` -> `claude-opus-4-7`: deep audit, hard reasoning, final arbitration, large fanout controller.
- `sonnet` -> `claude-sonnet-4-6`: implementation, execution, debugging, test-running, medium-cost worker.
- `haiku` -> `claude-haiku-4-5-20251001`: inventory, counting, file summaries, cheap scout work.

Use explicit model names if the user asks for one.

## Operating Rules

1. Work through `/tmp` for experiments unless the user asks to change repo files.
2. Always set `--budget` for non-trivial calls. Default is conservative.
3. Use `--stream` when proving subagents actually ran; parse the stream for `Agent` tool calls, `task_started`, and `task_notification`.
4. Treat Claude output as an external worker receipt, not native Codex state.
5. Report the output path, receipt path, model used, cost, and whether Agent/Task evidence was observed.
6. If direct Claude fails with a socket/auth error, tell the user the Codex process lacks Claude/network access and retry only after access is restored.
7. For Codex parent -> Claude child scaling, use explicit timeouts. A child that starts but does not return a receipt is not a completed subsubagent.
8. If stream-mode Task fanout stalls, reroute through `claude_child_fanout.py` with no tools first. Let the Codex parent provide source slices in the prompt; add Claude tools only after no-tool fanout is stable.

## Verification Pattern

After a call, inspect the generated receipt JSON. For stream-mode subagent work, count:

- `Agent` tool-use events
- `task_started` events
- completed `task_notification` events
- returned worker tokens or report files
- `modelUsage` entries

Do not claim "subagents ran" from a final answer alone.

For `claude_child_fanout.py`, inspect `fanout_receipt.json` and count only
children with `"status": "completed"`. Prefer `fanout_receipt_summary.py` when
multiple parent receipts are involved. Current measured safe ladder from Codex
parent agents:

- 1 parent x 1 Sonnet-high child: stable.
- 1 parent x 2 Sonnet-high children: stable.
- 1 parent x 3 Sonnet-high children: stable.
- 1 parent x 4 Sonnet-high children: stable with a 60s+ timeout.
- 1 parent x 6 Sonnet-high children: stable with `--timeout-sec 90 --max-concurrency 4`.
- 1 parent x 8 Sonnet-high children: partial in the observed run, 7 completed and 1 timed out.
- 2 parents x 4 Sonnet-high children: usable, but one long-tail child timed out at 120s and rerouted cleanly.
- 2 parents x 4 Haiku children: stable and fast; 8/8 completed in the observed run.
- 1 parent x 2 Gemini children: partial under 45s, then a 1-child reroute completed under 60s.
- 2 parents x 6 Sonnet-high children: stable in the observed run with 12/12 completed under a 150s child cap.
- 4 parents x 4 Haiku children: stable in the observed run with 16/16 completed under a 75s child cap.
- 1 parent x 12 Haiku children: completed under a 90s child cap, but output quality started to drift.
- 1 parent x 4 Gemini children: partial in the observed run; keep Gemini narrow until more evidence exists.
- 1 parent x 1 Opus child: completed, but behaved as arbitration/conflict review rather than scout work.
- 4 parents x 6 Sonnet-high children: stable in the observed run with 24/24 completed under a 180s child cap.
- 4 parents x 8 Haiku children: stable in completion with 32/32 completed under a 100s child cap, but output quality drift increased.
- 4 parents x 2 Gemini children: stable in the observed run with 8/8 completed under a 120s cap, but CLI warning noise is present.
- Mixed four-parent wave with Sonnet 6 + Haiku 8 + Gemini 2 + Opus 1: 17/17 completed.
- 8 parents x 8 Sonnet-high children: stable in the observed run with 64/64 completed under a 210s child cap.
- 8 parents x 12 Sonnet-high children: stable in the observed run with 96/96 completed under a 260s child cap.
- 7 parents x 12 Sonnet-high children plus 1 parent x 4 Opus-high children: stable in the observed run with 88/88 completed, zero failures/timeouts, max observed parent duration about 70s.
- 7 parents x 16 Sonnet-high children at concurrency 8 plus 1 parent x 4 Opus-high children: stable in completion with 116/116 completed, zero failures/timeouts, max observed parent duration about 107s. Opus arbitration rated this a partial pass because quality drift and receipt homogeneity become the soft limit before raw spawn failure.
- 8 parents x 12 Haiku children: stable in completion with 96/96 completed after parent-return reroutes; use smaller per-parent concurrency or the limiter for normal use.
- 8 parents x 16 Haiku children at concurrency 8: unstable; completed 118 but timed out 14 because the run stampedes Claude child starts and drains slow tails.
- 8 parents x 8 Haiku with `--stop-after-completed 4 --global-max-active 8`: stable operating shape; 32 useful completions, 0 timeouts, tails abandoned or not launched by design.

Default starting point for future Codex parent tests:

```text
8 parents x 12 Sonnet-high children, timeout 260s, max concurrency 4 per parent
```

Default Wizard v4 throttle after the 116-child limit probe:

```text
Use 8 Codex parents when a real Max Assembly run needs broad plurality.
Use Sonnet-high as the main child pool at 6-8 children per parent per council wave.
Use 10 Sonnet-high children per parent only as the upper normal setting when the task genuinely decomposes that far.
Use 11+ children per parent only as a stress setting, with max concurrency 8 and a receipt-shape/divergence audit before synthesis.
Reserve Opus-high for arbitration, usually 1 parent x 4 children.
Throttle down when the last quartile of child receipts stops adding distinct throttle signals, Opus reports shape-identical receipts, or parent p95 latency approaches the timeout.
```

For wide cheap scout lanes, Haiku is currently the fastest stable Claude child
model, but it needs global child-start throttling when many parents overlap.
A proven scout shape is 8 parents x 8 Haiku children with
`--stop-after-completed 4 --global-max-active 8`. Use Gemini as a bounded
fallback for narrow, well-defined lanes rather than as the first high-width
child pool. Use Opus for rare arbitration, not wide fanout.
