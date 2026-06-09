# Format correction receipt — 2026-05-04

User correction: prior Wizard render still looked like a log file. The purpose of Wizard formatting is to reduce human cognitive load and automate the making of next possible prompts.

Correction applied:

- Rewrote `final-render.md` into a human-load surface:
  - one-sentence changed state;
  - best next move first;
  - Decision/Failure/Follow-Up cards as reasons, not log entries;
  - compiled move;
  - copy-pasteable follow-up prompts with payoff and stop condition;
  - proof strip at the bottom.
- Patched `08_HERMES_WIZARD_RUN_HARNESS.md` so future Wizard renders prefer the human-load template over log-shaped route tables.
- Patched `hermes-wizard` skill pitfall 11 to require human-load rendering and automated next-prompt generation.

Validator rerun:

```text
PASS
validated: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-155235
```

Boundary:

This correction changes the user-facing render and future harness guidance. It does not change the underlying route proof: nested member routes remain `reported_by_parent`, and low-effort model routing remains unverified.
