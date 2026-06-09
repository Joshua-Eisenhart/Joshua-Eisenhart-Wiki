---
name: wizard-follow-up-selector
description: Follow-Up council-member skill for Wizard v4.1. Use to generate, pre-run, audit, improve, and select the next Wizard prompt.
---

# Wizard Follow-Up Selector Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/follow-up-selector/SKILL.md`

## Loop

1. Make divergent candidate prompts.
2. Pre-run the first action and first blocker.
3. Audit ambiguity, scope creep, missing check, missing stop, and hidden dependency.
4. Improve the prompt.
5. Select the next Wizard input or mark blocked.

## Return

```yaml
follow_up_selector:
  candidate_count:
  selected_prompt:
  payoff:
  use_when:
  stop_if:
  artifact_output_surface:
  verification_or_receipt_check:
  alternates:
```

## Boundary

The selected prompt re-enters the Wizard loop with prior receipts and context.
It does not bypass Decision, Failure, and Follow-Up.
