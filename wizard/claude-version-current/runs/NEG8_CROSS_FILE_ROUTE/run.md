# Claude Code Wizard run manifest

wizard_run: true
trigger: /wizard
breadth: auto
runtime: claude_code
date: 2026-06-13
scope: NEG8 negative fixture — cross-file route evade (route_action_classes claimed in decision-receipt with no backing route there)
note: |
  NEGATIVE fixture. decision-receipt.md claims route_action_classes
  superseded + blocked but provides no `routes:` block to back them; the only
  reasoned routes live in failure-receipt.md. The OLD validator parsed backing
  routes only from failure-receipt.md, so the unbacked decision-receipt claim
  passed. The fixed validator MUST reject this run. Everything else is the clean
  SMOKE shape.
