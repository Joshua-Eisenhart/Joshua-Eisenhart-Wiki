# Wizard (smoke) — compiled move

Bottom line: one move is hardened-but-blocked on an owner seam decision; a
second move was superseded. No move executed; nothing promoted. Two seams stay
live until the owner picks.

## Decision
Smallest useful move chosen; a read-only `Agent` (evidence-mapper) mapped the
two candidate seams. Both seams survive — split preserved (status: runs).

## Failure
Falsifier ran controller-local. Move-A (in-place) was **superseded** after it
was shown to silently widen scope. Move-B (adapter) is **blocked** pending a
private owner seam preference. Honest block, not a fake completion.

## Follow-Up
Two future choices, both rendered as `future_choice` (not pre-worked):
unblock-move-B (when owner confirms seam) and audit-move-A-supersession (before
any revival). Each carries payoff + use_when + stop_if.

## Status (honest ladder)
- evidence-mapper subagent: `runs` (read-only scan completed; not a promotion).
- compiled move: `runs` — bounded and id-linked; not `passes local rerun`, not
  `canonical by process`.

Evidence boundary: subagent reading proves scope, not execution. Move-B is
blocked, not done.
