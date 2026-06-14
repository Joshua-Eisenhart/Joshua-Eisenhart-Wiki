# Run manifest (opt-in gate VIOLATION fixture)

wizard_run: false
trigger: (none — ordinary prompt, user did not ask for the Wizard)
breadth: auto
runtime: claude_code
date: 2026-06-13
note: |
  NEGATIVE fixture: full Decision/Failure/Follow-Up topology emitted on an
  ordinary prompt with no Wizard invocation. The opt-in gate must REJECT this.
  (Validator checks the run artifact's declared wizard_run + trigger, not raw
  prompt text — stated limit.)
