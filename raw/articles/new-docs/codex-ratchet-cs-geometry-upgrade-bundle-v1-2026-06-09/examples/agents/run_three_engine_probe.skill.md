# run_three_engine_probe

## Purpose

Dispatch Julia, JAX, and PyTorch provider lanes on the same finite carrier fixture. Compare outputs and emit fan-in facts; do not self-admit.

## Required output

```json
{
  "skillId": "run_three_engine_probe",
  "status": "completed|blocked|evaluation_error",
  "artifactRefs": [],
  "gateProofRefs": [],
  "claimCeiling": "scratch_diagnostic_only",
  "promotionAllowed": false,
  "reason": "..."
}
```
