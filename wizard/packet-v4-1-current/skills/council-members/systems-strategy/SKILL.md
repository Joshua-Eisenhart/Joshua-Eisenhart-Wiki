---
name: wizard-systems-strategy
description: Systems council-member skill for Wizard v4.1. Use when the Wizard must step back from local optimization and inspect whole-system context, feedback loops, second-order effects, or strategy drift.
---

# Wizard Systems Strategy Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/systems-strategy/SKILL.md`

## Load

Load the assigned Systems mini-MMM or systems family slice, task/source
context, loop state, and relevant receipts. Do not optimize the local prompt
until the system boundary is named.

## Return

```yaml
systems_strategy:
  system_boundary:
  active_feedback_loop:
  second_order_effect:
  local_optimization_risk:
  step_back_recommendation:
  intervention:
  evidence_needed:
```

## Boundary

This skill can tell the Wizard to step back, split, or change target. It cannot
declare the compiled move ready without the normal compile gate.
