# Hermes output-format owner-boundary patch — 2026-04-23

## Bottom line
A bounded audit found that the output format was close, but a few surfaces could still fight each other: HERMES owned layout in theory, while skills/task cards still carried leftover layout, footer, tiny-mode, and worker-truth rules.

## What ran
- Read Hermes spine and current output-format carry-forward notes.
- Read current control surfaces:
  - `/Users/joshuaeisenhart/.hermes/HERMES.md`
  - `/Users/joshuaeisenhart/.hermes/SOUL.md`
  - `/Users/joshuaeisenhart/.hermes/SUBAGENT_BOOT.md`
  - `/Users/joshuaeisenhart/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
  - `/Users/joshuaeisenhart/.hermes/task-cards/FOLLOWUP_LANE_TASK_CARD.md`
  - `/Users/joshuaeisenhart/.hermes/task-cards/TASK_CARD_SCHEMA.md`
  - `hermes-follow-up-menu-style`
  - `hermes-output-surface-stress-test`
- Ran three divergent audit passes:
  - Hume/Orwell: screen-shape and owner-boundary audit
  - Zhuangzi/Popper: plurality and worker-claim honesty audit
  - Factory/Strategy: runtime adapter, route failure, and proof-packet audit

## Patches landed
### `~/.hermes/HERMES.md`
- Added worker-claim honesty: do not say a lane/voice/worker ran without a current-session receipt.
- Fixed omission conflict: Results/follow-up are preserved by default, Hygiene & Security is conditional, footer may be suppressed by screen-shape.
- Added route states: `rerouted` and `superseded`.
- Made Results preserve the strongest surviving split when plurality is the point.
- Clarified controller-local vs spawned worker truth.
- Renamed the tuning visible field from lane field to route field where Strategy/voices are included.
- Clarified Strategy as voice/lens by ownership but route-capable in tuning/stress/wizard mode when campaign fields are filled.

### `~/.hermes/SOUL.md`
- Tightened Hume so executive synthesis does not erase surviving splits.
- Added a collapse check for divergent receipts: if no split remains, say what killed the alternatives.

### `~/.hermes/SUBAGENT_BOOT.md`
- Added claim status to subagent receipts: `spawned`, `blocked`, `controller_local`, or `proposed`.

### Task cards / adapter
- `FOLLOWUP_RUNTIME_ADAPTER.md`:
  - direct worker only spawns when acceptance, guard, and artifact path are concrete
  - Strategy worker/lens only spawns when campaign-front / decisive-front / hold-retreat fields are filled
  - added route failure/reroute taxonomy
  - added worker-claim honesty gate
  - strengthened next proof packet to require Direct + Factory + Strategy + one blocked/rerouted path
- `FOLLOWUP_LANE_TASK_CARD.md`:
  - added `strategy` option_type
  - added `runtime_fallback`, `route_status`, `route_failure`
  - added claim status and route status to result contract
- `TASK_CARD_SCHEMA.md`:
  - aligned optional fields with the lane task-card fields.

### Skills
- `hermes-follow-up-menu-style`:
  - removed duplicate scaffold/footer/tiny-mode ownership
  - made it point back to HERMES for section order, footer, wizard marker, and screen-shape
  - added Strategy to the visible option family when campaign sequencing changes the move
  - made dense/rich menus subordinate to the HERMES screen-shape gate
  - changed 12-option shape into a proof target, not default render law
- `hermes-output-surface-stress-test`:
  - removed independent output scaffold / wizard-marker law
  - now routes final rendering back through HERMES.

## What remains open
- No fresh render proof packet has run after these patches.
- The next proof should use one bounded output-format task and require:
  - Direct worker receipt
  - Factory worker receipt
  - Strategy worker/lens receipt
  - one blocked/rerouted route receipt
  - final synthesis that separates Results from next-round Follow-up and preserves at least one live split when plurality is active.

## Current practical rule
Keep the visible scaffold, but let HERMES own it alone. Skills can shape menu wording. SOUL can shape body voice. Task cards can prove worker truth. None of them should quietly redefine the output format.
