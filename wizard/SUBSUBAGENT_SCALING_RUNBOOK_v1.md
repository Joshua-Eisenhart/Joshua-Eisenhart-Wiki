# Subsubagent Scaling Runbook v1

Purpose: make Codex parent -> Claude child scaling reproducible without
letting one slow child hold the whole run.

This runbook is for orchestration testing. Use real, bounded repo facts, but do
not launch sims or mutate Git while testing the fanout system.

## Current Finding

Codex native parent agents are healthy. Direct Claude Bridge calls are healthy.

The unstable path is:

```text
Codex parent -> Claude Bridge stream mode -> Claude Task/Agent fanout
```

That path stalled in this session.

The stable path is:

```text
Codex parent -> claude_child_fanout.py -> bounded Claude child calls -> fanout_receipt.json
```

The fix is hard timeout control plus one parent-readable receipt.

For overlapping waves, the second fix is cross-parent child throttling. Parent
agents may run laterally, but Claude child starts must pass through a shared
model-level slot limiter. Without the limiter, 7-8 parents can stampede the
Claude CLI with 28-32 simultaneous starts and produce false failures.

Gemini is also available through a bounded wrapper:

```text
Codex parent -> gemini_child_fanout.py -> bounded Gemini child calls -> fanout_receipt.json
```

Use Gemini for narrow, well-defined fallback lanes until more high-width tests
are measured.

## Active Tools

Single child:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model sonnet \
  --effort high \
  --budget 1 \
  --timeout-sec 60 \
  --prompt "Return one bounded verdict."
```

Multiple children:

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

Overlapping parent waves:

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

Use `--global-max-active` whenever multiple Codex parents may launch Claude
children at the same time. Use `--stop-after-completed` when the route only
needs a useful subset and slow tails should be abandoned rather than allowed to
hold the parent open.

Receipt summaries:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/fanout_receipt_summary.py \
  --route-prefix opt8-limit-H8s4 \
  --show-routes
```

Use this before writing Wizard headers or comparing parent waves. It reports
accepted completed children, timed-out children, abandoned tails, and
not-launched jobs from `fanout_receipt.json` files, so the visible answer can
stay compact.

Gemini children:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/gemini_child_fanout.py \
  --name parent-gemini-test \
  --timeout-sec 60 \
  --max-concurrency 2 \
  --jobs-file /tmp/gemini_child_jobs.json
```

`child_jobs.json` shape:

```json
[
  {
    "id": "runner",
    "prompt": "Given facts: sim runner is stopped and cleanup guard blocks new sim execution. Return one concise verdict."
  }
]
```

## Count Law

Count only completed receipts.

Do not count:

- started child processes;
- prompt files;
- pending children;
- timed-out children;
- stream starts;
- orphaned Claude calls;
- direct Claude calls from the main thread as subsubagents.

A child counts as a completed subsubagent only when:

```text
Codex parent returned a receipt
fanout_receipt.json exists
child status is completed
child bridge receipt path exists
child output is usable
```

## Measured Ladder

All rows below were run from Codex parent agents unless marked local.

```text
local 1 x 4, timeout 25, concurrency 4: 3 completed, 1 timed out
parent 1 x 4, timeout 25, concurrency 4: 0 completed, 4 timed out
parent 1 x 1 Sonnet high, timeout 60: 1 completed, 0 timed out, 8.529s
parent 1 x 1 Haiku, timeout 30: 1 completed, 0 timed out, 7.255s
parent 1 x 2 Sonnet high, timeout 60, concurrency 2: 2 completed, 0 timed out, 23.973s
parent 1 x 3 Sonnet high, timeout 60, concurrency 3: 3 completed, 0 timed out, 27.529s
parent 1 x 4 Sonnet high, timeout 60, concurrency 4: 4 completed, 0 timed out, 52.474s
parent 1 x 6 Sonnet high, timeout 90, concurrency 4: 6 completed, 0 timed out, 54.431s
parent 1 x 8 Sonnet high, timeout 90, concurrency 4: 7 completed, 1 timed out, 90.097s
parent 2 x 4 Sonnet high, timeout 120, concurrency 4: 7 completed, 1 timed out, plus 1 reroute completed in 8.192s
parent 2 x 4 Haiku, timeout 60, concurrency 4: 8 completed, 0 timed out, 12.634s and 16.324s parent durations
local 1 x 2 Gemini, timeout 40, concurrency 2: 2 completed, 0 timed out, 10.164s
parent 1 x 2 Gemini, timeout 45, concurrency 2: 1 completed, 1 timed out, 45.013s
parent 1 x 1 Gemini reroute, timeout 60: 1 completed, 0 timed out, 7.238s
parent 1 x 6 Sonnet high, timeout 120, concurrency 4: 6 completed, 0 timed out, 119.233s
parent 1 x 8 Sonnet high, timeout 150, concurrency 4: 8 completed, 0 timed out, 113.615s
parent 1 x 8 Haiku, timeout 90, concurrency 4: 8 completed, 0 timed out, 65.179s
parent 1 x 12 Haiku, timeout 90, concurrency 6: 12 completed, 0 timed out, 73.749s; 2 outputs were clarification-style
parent 1 x 4 Gemini, timeout 90, concurrency 2: 3 completed, 1 timed out, 135.557s
parent 1 x 2 Gemini, timeout 90, concurrency 2: 2 completed, 0 timed out, 17.642s
parent 1 x 3 Haiku queue reroute, timeout 45, concurrency 3: 3 completed, 0 timed out, 9.271s
parent 4 x 4 Haiku, timeout 75, concurrency 4 each: 16 completed, 0 timed out, parent durations 18.309s-21.532s
parent 2 x 6 Sonnet high, timeout 150, concurrency 4 each: 12 completed, 0 timed out, parent durations 25.793s and 29.157s
parent 1 x 1 Opus high, timeout 180: 1 completed, 0 timed out, 23.495s; output acted as arbitration/conflict check
parent 4 x 6 Sonnet high, timeout 180, concurrency 4 each: 24 completed, 0 timed out, parent durations 31.110s-36.600s; some children added footer/receipt text
parent 4 x 8 Haiku, timeout 100, concurrency 4 each: 32 completed, 0 timed out, parent durations 34.291s-50.034s; quality drift increased
parent 4 x 2 Gemini, timeout 120, concurrency 2 each: 8 completed, 0 timed out, parent durations 12.574s-17.919s; CLI warnings/noise remain
mixed parent wave, timeout by model: Sonnet 6 completed, Haiku 8 completed, Gemini 2 completed, Opus 1 completed; 17 completed, 0 timed out
parent 8 x 8 Sonnet high, timeout 210, concurrency 4 each: 64 completed, 0 timed out, parent durations 34.300s-131.287s
parent 8 x 12 Haiku, timeout 130, concurrency 6 each: 96 completed, 0 timed out after 3 parent-return reroutes; parent durations 80.034s-138.907s
parent 4 x 4 Gemini, timeout 180, concurrency 2 each: 16 completed, 0 timed out, parent durations 99.019s-115.564s
parent 8 x 12 Sonnet high, timeout 260, concurrency 4 each: 96 completed, 0 timed out, parent durations 57.278s-143.121s
parent 8 x 16 Haiku, timeout 180, concurrency 8 each: 118 completed, 14 timed out across the first 8-parent edge wave; unstable because it stampedes Claude child starts and drains timeout tails
parent 8 x 8 Haiku, stop-after-completed 4, global-max-active 8: 32 completed, 0 timed out, 18 abandoned, 14 not launched; stable rolling 8-parent operating shape with early-success receipts
```

Current safe default:

```text
8 parents x 12 Sonnet-high children, timeout 260s, max concurrency 4 per parent
```

Current aggressive default:

```text
8 parents x 8 Sonnet-high children, timeout 210s, max concurrency 4 per parent
```

Fast scout default:

```text
8 parents x 8 Haiku children, stop-after-completed 4, timeout 120s, max concurrency 4 per parent, global-max-active 8
```

Fast scout edge:

```text
4 parents x 8 Haiku children, timeout 100s, max concurrency 4 per parent. Watch output quality.
```

Current edge:

```text
8 parents x 16 Haiku at concurrency 8 is beyond the stable child-start envelope. It can finish many children, but timeout tails and parent drain behavior make it a poor default.
```

Current limiter rule:

```text
Use more Codex parents before raising per-parent child concurrency. For Claude
children, keep per-parent concurrency at 4 and set global-max-active near 8
until a higher global CLI start limit is proven. For useful-subset scouting,
use stop-after-completed so slow tails are abandoned with receipts.
```

Current Gemini rule:

```text
Use Gemini as a two-child fallback lane. Four parents x two Gemini children is stable with a 120s cap, but output includes CLI warning noise.
```

Current Opus rule:

```text
Use Opus as rare arbitration or doctrine-conflict review, not as a wide scout pool.
```

## Reroute Rule

If a child times out:

1. Keep the parent receipt.
2. Do not count the timed-out child.
3. Spawn a smaller replacement child with a narrower prompt.
4. If the replacement also times out, switch model or mark blocked.
5. Continue synthesis with completed receipts only.

If Codex reports an agent thread limit:

1. Close completed parent agents.
2. Retry the blocked parent spawn.
3. Do not treat the model/runtime as failed until closed handles have been freed.

If a parent does not return:

1. Close the parent.
2. Do not count its children unless a parent-readable fanout receipt exists.
3. Retry with fewer children or a larger timeout.

If many parents are running and multiple children time out together:

1. Treat it as a global child-start bottleneck, not a model-quality failure.
2. Add `--global-max-active` and keep per-parent concurrency at 4 or lower.
3. Prefer rolling parent waves over raising per-parent concurrency.
4. Use `--stop-after-completed` when a useful subset is enough.
5. Mark killed tails as abandoned, not failed route content.

If header counts are needed:

1. Run `fanout_receipt_summary.py` for the relevant route prefix.
2. Count only `completed` children as subsubagents.
3. Put the compact totals in the Wizard header.
4. Keep receipt paths in Results only when useful.

## Source Rule

Start no-tool first.

Preferred child input:

```text
parent reads source slice -> parent passes facts/source excerpt to child prompt
```

Avoid file-tool child calls until no-tool fanout is stable. In this session,
tool-enabled child calls were slower and sometimes orphaned.

## Next Scaling Tests

Run these in order:

```text
8 parents x 12 Sonnet-high children each, repeat once with global-max-active 12 to see whether Sonnet benefits from a limiter
8 parents x 8 Haiku children each, stop-after-completed 4, global-max-active 10, compare against the stable global-max-active 8 run
8 parents x 4 Gemini children each, timeout 180s, concurrency 2 per parent, only if Gemini quota is clean
mixed overlapping wave: Sonnet parents use no limiter or global-max-active 12; Haiku parents use global-max-active 8; Gemini stays narrow
```

Stop increasing width when:

- more than one child times out per parent;
- parent receipts stop returning;
- Claude child process cleanup leaves orphans;
- child outputs become generic or useless.

## Sim Runner Test Payload

Use these facts for safe real-work testing without launching sims:

```text
sim runner: stopped
cleanup_first_guard: blocks new sim execution
repair_queue_count: 5
active_actionable_lane: probe_source__sim_family_axis0
active_stage: lego
allow_tier_d_launch: false
primary sim result JSON count: 4420
secondary sim result root JSON count: 0
manifest fixer dry-run: would fix 3417, already clean 1002, skipped non-object JSON 1
focused bot guard tests: 22 passed
```

These facts are enough for child agents to do real route work without touching
the repo or launching a runner.
