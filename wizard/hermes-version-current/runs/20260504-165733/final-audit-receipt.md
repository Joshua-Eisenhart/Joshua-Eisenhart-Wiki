# Final audit receipt — wide-council run

run_id: 20260504-165733
mode: REAL_ATTEMPT_PARTIAL
validator_command: python3 /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/conformance/validate_hermes_wizard_wide_run.py /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733
validator_output: |
  PASS
  validated_wide_partial: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733

audit_verdict: PASS for scoped wide-partial run; final user-facing claim should be PARTIAL, not FULL.

audit_checked:
- run-plan.md
- decision-wide-receipt.md
- failure-wide-receipt.md
- followup-wide-receipt.md
- final-render.md
- conformance/validate_hermes_wizard_wide_run.py

accepted:
- final render reduces cognitive load;
- final render names Decision 7/7, Failure 6/6, Follow-Up 7/7;
- final render preserves parent-reported nested visibility;
- final render does not claim full v4.1, raw child/subchild proof, Codex Max Assembly, or independently verified child evidence;
- validator PASS is scoped to `validated_wide_partial`.

required_fixes: none

boundary:
This proves a Hermes wide-council partial fixture and local validator pass. It does not prove full v4.1 conformance or raw nested child/subchild evidence.
