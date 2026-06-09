# Hermes format-only owner + screen-shape patch — 2026-04-23

Bottom line
The Codex audit was directionally right: formatting authority was fragmented and tuning-mode visibility rules were helping produce ugly terminal output. I made a bounded format-only patch in the owner surfaces.

What changed
- `~/.hermes/HERMES.md`
  - made `HERMES.md` the sole owner of visible output formatting law
  - added a hard screen-shape gate for narrow/monospaced interfaces
  - made footer suppression explicit when it wraps or crowds the answer
  - made tuning-mode visibility subordinate to screen-shape budgets
- `~/.hermes/SOUL.md`
  - cut presentation pressure back
  - made emoji sparse on narrow/monospaced screens
  - stated plainly that SOUL does not own section count, follow-up count, wrap budgets, or footer behavior
- `~/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
  - made the runtime adapter obey screen-shape budgets before forcing the full visible route field
  - let omitted route truth stay in Results or appear only on explicit request when the screen would turn into wall-text

What remains open
- no fresh render proof packet has run after this format-only patch
- the current live answer still needs to demonstrate the cleaner shape, not just describe it
- tuning-mode richness vs narrow-screen readability is now better owned, but still needs live proving
