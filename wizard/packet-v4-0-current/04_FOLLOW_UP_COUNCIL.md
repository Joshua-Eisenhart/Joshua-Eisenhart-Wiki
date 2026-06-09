---
title: Wizard v4.0 Follow-Up Council
type: followup_contract
packet: v4.0
framing: standalone
---

# Follow-Up Council v4.0

Follow-Up Council makes divergent good next prompts.

It should generate a broad internal bank, then show only the useful few.

The visible options should reduce human cognitive load. They should feel like good choices, not internal route names.

## Follow-Up Option Shape

Each visible option needs:

```yaml
label:
prompt:
payoff:
use_when:
blocked_if:
pre_run_check:
audit_fix:
first_action:
target:
immediate_action:
owner_lane:
success_check:
stop_condition:
artifact_output_surface:
status:
```

## Follow-Up Deepening Loop

Visible follow-ups should be preworked before the user sees them.

Run this loop internally:

1. **Make**: generate divergent candidate prompts.
2. **Pre-run**: mentally or read-only walk each option through the first action, likely artifact, and first blocker.
3. **Audit**: check for ambiguity, scope creep, missing success check, missing stop condition, and hidden dependency.
4. **Improve**: rewrite the prompt so it is clearer, smaller, and easier to execute.
5. **Select**: show only the useful few.

The visible option can summarize this as one short `Pre-checked` line. Do not expose the whole internal audit unless diagnostics are requested.

Visible wording should use:

- short labels that describe the human choice;
- a little visual character, such as a relevant emoji;
- plain-language payoff;
- the first action;
- the pre-check result;
- clear "use this when" and "do not use if";
- no raw route bookkeeping unless diagnostics are requested.

Show three to four options. If more than one option is genuinely useful, include an `All of the Above` option that sequences them safely.

## Useful Lanes

- Direct: do the smallest useful next move.
- Alternative: try a different route to the same goal.
- Reframe: change the object, unit, or premise.
- Back: retreat to the last stable smaller move.
- Wildcard: run one off-axis probe with a concrete payoff.

## Useful Compositions

- All-A Build: build plus mechanism, falsifier, alternative, audit.
- All-B Divergence: preserve alternatives and test collapse.
- All-C Closeout: clarity, safety, handoff, receipt audit.
- Max Assembly: integrate all useful candidates into one non-contradictory maximum plan.

## Combined Prompt Option

When several follow-ups are all useful, include one combined option.

The combined option should:

- sequence the moves;
- remove contradictions;
- pre-run the sequence;
- audit the handoffs between options;
- keep the first action small;
- include a stop condition;
- include an artifact/output surface.

Do not give the combined option a generic all-routes name. Use "Max Assembly" only when it means maximum useful integration.

Use `All of the Above` when the user-facing meaning is "do these useful options in sequence." Use `Max Assembly` when the system-facing meaning is maximum useful route integration.
