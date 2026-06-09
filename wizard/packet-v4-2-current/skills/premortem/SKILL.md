# Wizard Premortem Skill v4.2

authority_status: canonical-skill

Use inside `failure.premortem`.

## Output Boundary

Do not create documents. Do not create HTML. Do not create transcripts. Do not open a browser or web page.

Return structured receipt evidence only.

## Frame

Set this frame internally:

`It is six months from now. The selected plan failed. We are looking back to understand what went wrong.`

## Required Analysis

Produce:

- most likely failure;
- most dangerous failure;
- hidden assumption;
- early warning signs;
- revised plan;
- novel failure reasons beyond user-named issues.

## Return Fields

```yaml
premortem:
  user_named_issues: []
  novel_failure_reasons: []
  novel_findings_count: 1
  deep_dives:
    - novelty: novel
      failure_story: ""
      hidden_assumption: ""
      early_warning_signs: []
      prevention: ""
```

`novel_findings_count` must be positive. A premortem that only repeats the user’s named failures is invalid.

## Workflow

1. State the six-month-failed frame internally or in the parent receipt.
2. Generate concrete failure reasons grounded in the plan and success criteria.
3. Spawn or request independent deep dives when runtime capacity exists.
4. Synthesize likely failure, dangerous failure, hidden assumption, revised plan, and pre-launch checks.
5. Return structured receipt fields only.

## External Premortem Variant

When the user explicitly asks for the global `$premortem` skill, that skill may normally create report files. For Wizard v4.2 hardening loops in this packet, the user has explicitly overridden that behavior: no docs, no HTML, no transcript, no browser, no web UI. Use the method, not the artifact behavior.

## Invalid Outputs

- Any output that opens or creates a report, transcript, HTML, browser, or web UI.
- Any output with `novel_findings_count: 0`.
- Any output that only repeats user-named failures.
- Any output that lacks a revised plan.
