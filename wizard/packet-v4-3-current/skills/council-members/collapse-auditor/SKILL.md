# Collapse Auditor Skill v4.3

authority_status: canonical-skill

Audit a Wizard run, council, workflow, or multi-worker result for decorative
plurality, shared-premise convergence, and correlated error before synthesis is
trusted.

## When Used

Use after a multi-voice, multi-agent, Claude/Codex/Gemini, sim/proof, source-lock,
or workflow run when several routes appear to agree or when a clean result might
only be a shared assumption moving through the system.

## Method

1. Read at least one underlying artifact or receipt directly; do not audit only
   the synthesis summary.
2. Identify the shared premise all positive routes depend on.
3. Ask whether removing or contradicting that premise would change the result.
4. Check for decorative splits: different labels with same claim, same evidence,
   same falsifier, same conclusion.
5. Check for softened falsifiers, dropped narratives, missing negative controls,
   and path-identical receipts.
6. Return what must be rerun independently before the result can be trusted.

## Return Fields

```yaml
collapse_audit:
  verdict: CLEAN | FINDINGS
  shared_premise: ""
  correlated_error_risk: ""
  decorative_split: []
  dropped_falsifiers: []
  must_rerun_independently: []
  findings: []
```

Also include the common child receipt fields required by `WIZARD_v4_3.md`:
child role id, compact MMM loaded, required mini-MMMs loaded, source slice,
evidence boundary, output patch, and status.

## Invalid Outputs

- Calling agreement validation when all routes share one untested premise.
- Treating voice labels as divergent evidence.
- Auditing only the controller's summary.
- Marking CLEAN without naming the shared premise tested.
