# Claude Code Wizard run manifest

wizard_run: true
trigger: /wizard
breadth: auto
runtime: claude_code
date: 2026-06-13
scope: NEG6_GAMED_FAILURE — failure path lists action classes with no per-route reasons
note: |
  NEGATIVE fixture: the failure receipt lists route_action_classes blocked +
  superseded but the structured routes carry NO reason. The reason-per-route
  check must REJECT this — a class list alone is gameable.
