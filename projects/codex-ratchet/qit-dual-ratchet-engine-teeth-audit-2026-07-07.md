---
title: QIT Dual Ratchet Engine Teeth Audit 2026-07-07
created: 2026-07-07
type: project-note
tags: [codex-ratchet, qit, engine, lev, mmm, object-formation]
---

# QIT Dual Ratchet Engine Teeth Audit 2026-07-07

> **Historical baseline:** this page records the July 7 state. [[projects/codex-ratchet/current-research-frontier-2026-07-09]] and [[projects/codex-ratchet/external-86-v84-92-foundations-engine-audit-receipt-2026-07-09]] control the current reading. The fresh 16-stage affine re-identification passes, while the stranger-seed Type-2 same-content-after-permutation gate fails. Keep those results separate.

Source receipt in the live repo:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/QIT_DUAL_RATCHET_ENGINE_TEETH_AUDIT_20260707.md`

## Current State As Of 2026-07-07

The current QIT / dual-ratchet stack has real bounded machinery:

- 16 oracle-contract macro-stages are numerically distinct and order-sensitive under the current 1q and 3q JAX/Torch/Julia validators.
- Each macro-stage has 4 operator/substage moves in the Engine 64 schedule atlas.
- Two engine sheets produce 64 ordered microsteps.
- Fresh local runs showed order-sensitive 64-state behavior, while order-blind controls collapsed to 11 buckets.
- `qit_dual_engine_live_v0` reran across NumPy, JAX, Torch, and Julia with exact action parity and measurable D/C sheet divergence; its live-loop ceiling remains `classification: scratch_diagnostic` and `promotion_allowed: false`.
- Candidate formal scouts exist for classifier/readout signal, dynamics-required discrimination, placement discrimination, holodeck replay, and spinor-memory adapter seeds. The later Weyl/terrain alignment audit found only 9 source-native candidates and 245 downstream-geometry rows without the declared source operating space, so no blanket `source-aligned engines` claim survives.

The current stack does not yet admit:

- full Type-1 / Type-2 64-stage QIT engine closure;
- a production object-perception engine;
- ontology/MMM writer authority;
- Axis0/FEP/physics bridge;
- Lev mesh state mutation.

## Correct Shape

The clean current interpretation is:

```text
2 engine sheets x 8 macro-stage visits per sheet x 4 operator/substage moves = 64 ordered microsteps
```

The 16 macro-stages are real enough to be load-bearing under the current oracle/validator contract. The 64 are ordered microsteps, not 64 independent macro-stage identities.

## Object Formation Bridge

The safe Leviathan / MMM bridge is:

```text
candidate object
-> measurement packet
-> gate policy
-> decision
-> receipt
-> Lev imports as claim/evidence
-> local verifier quorum
-> mesh-visible object projection
```

This matches the object-factory idea without pretending the object factory has already been proved. MMMs and ontologies can be treated as scoped projection surfaces over candidate root objects. Failed projections should produce anti-hashes / graveyard receipts.

## What Landed After This Baseline

`qit_full_type1_type2_64_live_v1`, the five-view projection battery, the bidirectional-science packet, and a Lev evidence-only consumer shape subsequently landed as working-tree artifacts and receipts. They add:

- one shared finite object family over both engine sheets;
- a 64-row atlas schedule-runtime scout with a separate four-phase science wrapper;
- JAX, Julia, and PyTorch result lanes;
- held-out reconstruction/classification and erasure controls;
- five partial projection views over four object cards;
- Type-1-only, Type-2-only, shared-win, and shared-failure receipts;
- object cards with survivor hashes and anti-hashes;
- a Lev consumer packet that imports evidence, not state mutation.

They remain scratch/pre-admission work. The current parent-receipt chain is not hash-current end to end, the stronger Type-2 stranger-seed criterion failed, and the Lev path is not a current proof-bound idempotent mesh mutation route.

## Claim Ceiling

Safe baseline phrase:

> bounded real QIT engine machinery with strong 16-stage oracle-contract and 64-schedule evidence, not full QIT engine admission.

Live-loop status label: `scratch_diagnostic`, `promotion_allowed=false`.

Avoid:

- "AI perception is solved";
- "Axis0 is unlocked";
- "Lev mesh object engine is live";
- "the object factory is proved";
- "64 independent macro-stages are complete."
