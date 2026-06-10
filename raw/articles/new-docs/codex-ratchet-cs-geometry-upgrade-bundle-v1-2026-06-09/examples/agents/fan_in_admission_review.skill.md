# fan_in_admission_review

## Purpose

Review provider evidence, GateProof refs, receipt refs, negative controls, and claim ceiling. Emit accepted/needs_evidence/needs_rework/rejected recommendation only.

## Required output

```json
{
  "skillId": "fan_in_admission_review",
  "status": "completed|blocked|evaluation_error",
  "artifactRefs": [],
  "gateProofRefs": [],
  "claimCeiling": "scratch_diagnostic_only",
  "promotionAllowed": false,
  "reason": "..."
}
```
