---
name: wizard-loophole-auditor
description: Confidence and loophole audit skill for Wizard v4.1. Use when a strategy must be stress-tested until no known unresolved loophole remains under a declared evidence standard or loop cap.
---

# Wizard Loophole Auditor Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/loophole-auditor/SKILL.md`

## Driver Prompt

```text
Are you 100% confident in this strategy? If not, find all possible loopholes,
suggest proper fixes, and run this loop until you are factually 100% confident
in the new strategy.
```

## Runtime Meaning

`100% confident` means no known unresolved loophole remains under the declared
evidence standard, verification checks, child coverage, and loop cap. If
literal certainty is impossible, return the remaining uncertainty and the
evidence needed. Do not manufacture certainty.

## Return

```yaml
loophole_audit:
  strategy_under_test:
  evidence_standard:
  loopholes:
    - loophole:
      severity:
      fix:
      verification:
      status: open | fixed | blocked | out_of_scope
  confidence_status: open | sufficient | impossible | blocked
  next_loop_input:
  stop_condition:
```

## Boundary

This skill drives another Wizard loop when loopholes remain. It is not launch
approval for codex-autoresearch and not a substitute for Premortem.
