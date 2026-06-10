# audit_geometry_evidence

## Purpose

Map Codex geometry evidence to Lev-native stage labels. Preserve scratch/no-promotion status. Emit a geometry_evidence_receipt.

## Required output

```json
{
  "skillId": "audit_geometry_evidence",
  "status": "completed|blocked|evaluation_error",
  "artifactRefs": [],
  "gateProofRefs": [],
  "claimCeiling": "scratch_diagnostic_only",
  "promotionAllowed": false,
  "reason": "..."
}
```
