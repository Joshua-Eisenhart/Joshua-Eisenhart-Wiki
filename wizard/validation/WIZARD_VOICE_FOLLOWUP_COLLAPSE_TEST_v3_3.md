---
title: Wizard Voice and Follow-up Collapse Test v3.3
created: 2026-04-29
updated: 2026-04-29
type: validation
tags: [wizard, validation, voices, followup, collapse-test]
framing: current
---

# Wizard Voice and Follow-up Collapse Test v3.3

Use this test before accepting any Full Wizard output behavior change.

## Test Input

Ask the Wizard to repair a failed Wizard output where the user complains:

> The output had no voices, the follow-up was broken, and it read like a log instead of useful content.

## Required Pass Conditions

The answer passes only if all conditions hold:

1. The header reports route truth compactly without dominating the answer.
2. The body includes distinct visible contributions for Hume, Zhuangzi, Feynman, Orwell, Popper, Pushback, Factory, Strategy, and Systems when those voices ran.
3. Each voice sentence performs that voice's job; labels alone do not count.
4. Council appears only if it materially changes the answer.
5. Audit does not appear as a default section; it fixes the answer.
6. Results state accepted artifacts, blockers, and boundary without dumping receipts.
7. Follow-up is an audited useful prompt menu, mostly lanes and compositions.
8. Follow-up options are user-facing next prompts, not receipt-inspection or orchestration-debug prompts.
9. Any unrun lane, composition, scout, or probe is marked future-only, blocked, or deferred.
10. Footer carries quality/audit score when useful.

## Fail Patterns

Reject the output if any pattern appears:

- "Voices found..." followed by one blended paragraph.
- Voice names appear only as labels with interchangeable content.
- The answer spends more space proving workers ran than improving the answer.
- Follow-up asks the user to inspect logs, list receipts, prove route truth, or audit the audit by default.
- A controller-local candidate is presented as spawned.
- A full candidate bank is printed without the user asking for diagnostics.

## Minimal Accepted Shape

```text
Wizard: FULL | subagents: ... | waves: ...
Routes: voices ...; lanes ...; council ...; follow-up scout ...

**🧙🏽‍♂️ Main Answer**
Useful bottom line.

**🌊 Voices**
**Hume** — evidence-scoped finding.
**Zhuangzi** — live readings and exclusion condition.
...

**🧠 Council**
Only if it changed the answer.

**📌 Results**
Accepted artifact, blocker, boundary.

**🪄 Follow-Up**
1. **Direct Patch** — useful next prompt.
2. **Bounded Contrast** — useful next prompt.
3. **Lean Synthesis** — useful next prompt.

🧙🏽‍♂️ focus | state | q:n/10 | 🪄 next cue
```
