---
name: premortem
description: Wizard-embedded premortem method for Failure Council. Assumes the selected move failed six months later, works backward to expose failure causes, hidden assumptions, early warnings, and revised-plan pressure. This packet-local version returns receipt fields only; it does not create documents or open a browser.
---

# Premortem

Use this skill inside `failure.premortem_council`.

This is Gary Klein-style prospective hindsight: imagine the selected move has
already failed six months from now, then work backward to identify why. The goal
is not generic risk analysis. The goal is specific failure pressure that changes
the compiled move, stop condition, or follow-up options.

## Wizard Boundary

This packet-local skill is embedded in Wizard. It does not:

- create an HTML report;
- create a markdown transcript;
- open a browser or web page;
- write files unless a separate route explicitly asks for an artifact.

It returns structured premortem evidence to the Wizard receipt.

## Context Minimum

Before running, establish:

1. What move is being premortemed.
2. Who or what it affects.
3. What success would have looked like.

Infer this from Wizard Decision Council receipts and task context when possible.
Ask only if the premortem would otherwise be meaningless.

## Workflow

### 1. Set The Frame

Use this frame:

```text
It is six months from now. The selected move failed. We are looking back to understand exactly what went wrong.
```

### 2. Generate Raw Failure Reasons

List the genuine ways this move could have failed. Each reason must be:

- specific to the selected move;
- plausible and consequential;
- grounded in the task/source context;
- not padded.

### 3. Deep Dive

For each load-bearing failure reason, produce:

- failure story;
- underlying assumption;
- early warning signs;
- prevention or hardening move.

Use child workers when the runtime supports them. If child workers cannot run,
mark the route `degraded_local` and do the deep dives locally. Do not pretend
children ran.

### 4. Synthesize

Return:

- most likely failure;
- most dangerous failure;
- hidden assumption;
- revised plan pressure;
- pre-execution checklist;
- open findings that must join Follow-Up as stop conditions, required
  hardening, or blockers.

## Receipt Output

Populate the Wizard receipt `premortem` field with:

```yaml
skill_loaded: true
skill_path: skills/premortem/SKILL.md
skill_load_status: loaded | blocked | degraded_local
frame_set: true
context_minimum:
  what:
  who_affected:
  success_criteria:
raw_failure_reasons:
  - id:
    reason:
    novelty: user_named | derived_extension | novel
user_named_issues:
  - id:
    issue:
novel_failure_reasons:
  - id:
    reason:
novel_findings_count:
deep_dives:
  - failure_reason_id:
    novelty: user_named | derived_extension | novel
    failure_story:
    hidden_assumption:
    early_warning_signs:
    prevention:
synthesis:
  most_likely_failure:
  most_dangerous_failure:
  hidden_assumption:
  revised_plan:
  pre_execution_checklist:
open_findings:
  - id:
    finding:
```

## Quality Bar

- Set the failed-six-months frame every time.
- Ground failure modes in the actual move and evidence boundary.
- Find failure modes beyond the issues already named by the user or current
  controller. Repeating only named complaints is not a valid premortem.
- `novel_findings_count` must be greater than zero for an accepted premortem.
  If no novel failure mode is found, mark the route partial and say that the
  premortem failed usefulness rather than padding the receipt.
- Every deep dive must include `failure_story`, `hidden_assumption`,
  `early_warning_signs`, and `prevention`. A receipt missing these fields is
  partial even if it sounds critical.
- Make hardening concrete.
- Feed unresolved findings into the Follow-Up join gate.
- Do not output generic risk lists.
- Do not create files or open a web page.
