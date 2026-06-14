# Claude Code Wizard run manifest

wizard_run: true
trigger: /wizard
breadth: auto
runtime: claude_code
date: 2026-06-13
scope: NEG4_FORGED_PARENT — spawn_subagent whose linked Agent receipt parent_receipt does NOT match the spawning receipt id
note: |
  NEGATIVE fixture: the Decision receipt claims spawn_subagent and links a real
  Agent receipt with correct surface fields, but that Agent receipt's
  parent_receipt is a stale/forged id (not dec-20260613-01). The parent-linkage
  check must REJECT this — surface fields alone are not provenance.
