# Claude Code Wizard run manifest

wizard_run: true
trigger: /wizard
breadth: auto
runtime: claude_code
date: 2026-06-13
scope: NEG5_FIELD_ONLY — field-only run, schema field NAMES present but no real receipt content
note: |
  NEGATIVE fixture: every receipt lists the schema field names but with empty /
  placeholder values and no real linked content (no resolvable Agent receipt, no
  matching ids, no reasons, no bottom-line-first render). Field presence is not
  provenance; the validator must REJECT this.
