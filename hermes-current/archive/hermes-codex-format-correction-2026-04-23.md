# Hermes Codex-format correction — 2026-04-23

## Main point
The Codex example restored the target surface that Hermes had drifted away from. The intended tuning / workerized-audit render is not a generic bottom-line summary. It uses literal sections:

1. `Main answer`
2. `Results`
3. `Follow-up`
4. `Hygiene & Security`
5. `Footer`

## What the Codex example added back
- Main answer uses short voice/lane-labelled method blocks, not one blended paragraph.
- Results reports actual worker use and the remaining falsifier.
- Follow-up preserves the full voice + lane route field and two concrete all-bundles.
- Hygiene & Security is a visible section even when security is clear.
- Footer is a labelled section, not just an unlabeled rail.

## Worker truth rule
For tuning / stress / workerized-audit turns, a visible route is one of:
- `spawned`
- `blocked`
- `deferred`

Do not silently collapse visible plurality routes into `controller_local`.

## Six-receipt proof spine
A spawned visible route is not proved by worker count alone. It needs:
1. controller assignment receipt
2. spawn receipt
3. live scope receipt
4. worker artifact receipt
5. controller reread receipt
6. promotion / defer / blocked receipt

Missing receipt means `partial`, `deferred`, or `blocked`, not proven independent work.

## Files patched from this correction
- `/Users/joshuaeisenhart/.hermes/HERMES.md`
  - added literal scaffold label rule
  - added workerized-audit voice-body rule
  - added `deferred` route/action status
  - added six-receipt proof spine
- `/Users/joshuaeisenhart/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
  - added workerized-audit handling
  - added `deferred`
  - added six-receipt proof requirement
- `/Users/joshuaeisenhart/.hermes/task-cards/FOLLOWUP_LANE_TASK_CARD.md`
  - added `deferred` action/status support
- `/Users/joshuaeisenhart/.hermes/task-cards/TASK_CARD_SCHEMA.md`
  - added `deferred` action/status support
- `/Users/joshuaeisenhart/.hermes/SUBAGENT_BOOT.md`
  - added `deferred` to claim status
- `hermes-correction-turns` skill
  - patched exact-scaffold correction exception so a quoted desired format preserves literal sections

## Practical render model
When the user is auditing/tuning Hermes output, answer in the exact section frame above. Keep sections short and single-spaced, but do not rename or omit them unless the user explicitly requests raw/minimal output.
