# Claude Code Wizard run manifest

wizard_run: true
trigger: /wizard
breadth: auto
runtime: claude_code
date: 2026-06-13
scope: NEG7 negative fixture — surface_kind evade (spawning Decision self-labels surface_kind:agent to skip provenance)
note: |
  NEGATIVE fixture. The Decision receipt claims action_class spawn_subagent but
  self-labels surface_kind:agent (and provides no linked_receipt, no Agent leaf)
  so that the old leaf-agent early-return skipped provenance entirely. The fixed
  validator MUST reject this run. All other receipts are the clean SMOKE shape;
  only the surface_kind evasion is introduced.
