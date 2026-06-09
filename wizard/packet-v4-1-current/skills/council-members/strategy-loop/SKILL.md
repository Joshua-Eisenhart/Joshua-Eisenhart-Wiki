---
name: wizard-strategy-loop
description: Strategy council-member skill for Wizard v4.1. Use when a parent or child must sequence work, decide priority, set hold/retreat conditions, or choose whether the Wizard should loop, execute, split, or stop.
---

# Wizard Strategy Loop Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/strategy-loop/SKILL.md`

## Load

Load the assigned Strategy mini-MMM or sparse registry slice, the task card,
the current loop state, and the source/receipt slice. Do not load sibling
voices unless assigned a cross-voice composition.

## Return

```yaml
strategy_loop:
  priority:
  sequence:
  hold_condition:
  retreat_condition:
  next_loop_input:
  stop_condition:
  reason:
```

## Boundary

This skill recommends sequence and loop control. It does not replace Decision,
Failure, Follow-Up, child-health, or the compile gate.
