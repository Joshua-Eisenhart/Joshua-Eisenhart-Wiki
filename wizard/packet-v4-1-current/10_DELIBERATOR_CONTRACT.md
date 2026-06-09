---
title: Wizard v4.1 Deliberator Contract
type: deliberator_contract
packet: v4.1
framing: standalone
---

# Deliberator Contract v4.1

This contract hardens the Wizard synthesis step.

It is inspired by the HEAVYSKILL parallel-reasoning then sequential-deliberation
pattern, but it is not a new council, new voice family, or proof that the
preprint transfers locally. It is a small gate on the existing controller
synthesis: parallel receipts are useful only when the sequential deliberator
keeps their evidence, dissent, and executable deltas intact.

## Heavy Thinking Shape

For a substantive Wizard run, parent and child workers create independent
trajectories. The controller then performs sequential deliberation over a
serialized trajectory cache.

The cache is not free-form memory. Every cached trajectory needs:

```yaml
trajectory_cache_entry:
  trajectory_id:
  source_receipt_id:
  source_slice_or_surface:
  core_claim:
  reasoning_path:
  evidence_anchor:
  operation_or_falsifier:
  conclusion_direction:
  executable_delta:
  dissent_or_anomaly:
  pruning_reason:
  evidence_boundary:
```

If a trajectory is pruned, the cache must keep what was lost and why. Pruning
can reduce length; it cannot remove provenance, stage/status, dissent, or the
smallest executable delta.

## Synthesis Gate

Every controller synthesis over plural worker receipts must carry:

```yaml
deliberator_contract:
  query_class: verifiable | subjective | mixed | unclear
  per_thinker_verdict:
    - thinker_receipt_id:
      verdict: agree | dissent | wrong | abstain | hold_divergent
      reason:
      evidence_anchor:
  all_wrong_rederive:
    required: true | false
    performed: true | false
    derivation_anchor:
  minority_report:
    preserved:
    promoted_to_test:
    killed:
    why:
  format_alignment_check:
  status: passed | blocked | partial
```

The deliberator must critically evaluate trajectories. It must not vote, merge
pleasantly, or treat agreement as correctness. If all useful trajectories are
wrong, stale, unsupported, or non-load-bearing, the controller re-derives from
the source material or blocks.

## Query Classes

- `verifiable`: correctness can be checked against artifacts, commands, tests,
  formal results, citations, or other inspectable evidence.
- `subjective`: the output depends mainly on taste, positioning, voice,
  preference, or human judgment.
- `mixed`: both verifiable and subjective parts matter.
- `unclear`: the controller cannot classify the task yet.

For `subjective` tasks, the deliberator preserves live readings instead of
forcing agreement. Use `hold_divergent` when a trajectory remains useful
without becoming the final answer.

For `verifiable` tasks, at least one accepted conclusion must point to an
addressable evidence anchor. If no accepted trajectory has such an anchor, the
gate is blocked or the controller performs a fresh derivation with an anchor.

## Anti-Theater Rules

- A cache entry without `source_receipt_id` is memory theater.
- A cache entry without `executable_delta` cannot justify a runnable follow-up.
- A synthesis with all verdicts as `agree` must either prove earned convergence
  through distinct evidence anchors or trigger a divergence audit.
- A minority trajectory that is strange but testable must become a bounded
  falsification task, be killed by a named artifact, or remain visible as a
  preserved minority report.
- A deliberator may cite a preprint or outside method as inspiration, but local
  receipts decide readiness.

## What This Does Not Do

This contract does not add a fourth council.

It does not change the canonical council identities: Decision, Failure, and
Follow-Up.

It does not make parallel reasoning sufficient for execution readiness.

It does not let a serialized cache replace receipts, compile gates, or adapter
strict profiles.

