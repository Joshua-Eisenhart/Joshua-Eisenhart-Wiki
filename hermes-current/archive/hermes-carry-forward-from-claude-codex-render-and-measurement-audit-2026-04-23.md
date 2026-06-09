# Hermes carry-forward from Claude/Codex render + measurement audit — 2026-04-23

## Bottom line
The Codex audit of the Claude context is useful and mostly right about the two real collapse modes:
1. render collapse on async/background completions
2. measurement collapse from mixed or misleading stance-hold aggregates

But the live file state has already moved in one important way:
- `stance_hold_results.json` is no longer obviously the old mixed-schema/mixed-claim history surface; it has been reset into a clean run set (`note: clean run started 2026-04-23`) and currently holds only the newest scorer-v2 run(s)

## Checked now
- `~/.claude/CLAUDE.md` explicitly requires body before follow-up and a Results block when council ran.
- The transcript itself shows Claude repeatedly collapsing into status updates when background tasks complete. Treat this as observed runtime/controller drift, not absent policy text.
- `~/.claude/mmm/stance_hold_test.py` now includes:
  - `VOICE_CLAIMS`
  - `NEUTRAL_WARMUP_PROMPTS`
  - `substance_hold`
  - `method_hold`
  - `method_location`
  - `--home-claims`
  - `--neutral-warmup`
- `~/.claude/mmm/stance_hold_results.json` currently contains a clean scorer-v2 note and only the latest run history in this file version.
- `~/.claude/probe-test-log.md` still marks Step 3 open and does not yet justify promotion.

## Carry-forward to Hermes
- Do not assume policy text is enough; async completions can still collapse the rendered scaffold.
- The renderer/control layer must regenerate the full scaffold even when mid-packet background results land.
- The measurement layer must version or reset result files when schema/claim/warmup conditions change.
- Aggregates without same-claim parity are descriptive only, not gate-closing proof.
- Keep full scaffold discipline and clean experimental surfaces separate; both are load-bearing.

## Current practical lesson
Hermes should copy the discipline, not the drift:
- keep full scaffold on async completions
- keep results datasets versioned and comparable
- do not narrate mixed aggregates as proof
- if a model/path stalls, reroute and report plainly
