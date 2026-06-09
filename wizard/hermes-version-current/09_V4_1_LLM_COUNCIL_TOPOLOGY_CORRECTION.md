---
title: Hermes Wizard v4.1 LLM Council Topology Correction
created: 2026-05-04
updated: 2026-05-04
type: topology_correction
runtime: hermes
status: live-correction
---

# Hermes Wizard v4.1 LLM Council Topology Correction

## Correction

A v4.1 Wizard run is not merely three labels, three controller-local phases, or three parent summaries.

The v4.1 shape is:

```text
Decision Council  ->  Failure Council  ->  Follow-Up Council
     wide parallel work inside each council before the council returns
```

Each council is a distinct LLM council/wave. The councils run in sequence as write barriers, but the work inside each council is intentionally wide and parallel when the runtime can support it.

This must be treated as primary topology, not as a later enhancement.

## What the prior Hermes run proved

The run under `runs/20260504-155235/` proved only a smaller thing:

- Decision, Failure, and Follow-Up parent routes ran in sequence.
- Failure consumed Decision.
- Follow-Up consumed Decision and Failure.
- A local validator checked that minimal sequential topology and visible boundaries.

It did not prove the actual v4.1 wide LLM council topology.

Specifically, it did not prove:

- dedicated parent members across the full selected Decision member set;
- dedicated parent members across the full selected Failure member set;
- dedicated parent members across the full selected Follow-Up member set;
- 5-10 accepted child/subsubagent receipts per counted parent where the runtime supports children;
- Codex-native/Opus/Sonnet/Haiku/Gemini-style model-family matrix coverage;
- exact mini-MMM slice loading for every member;
- member utility receipts for every accepted member.

Therefore the earlier `PASS` label was too narrow. It was a pass for a minimal Hermes sequential-parent smoke harness, not for v4.1 LLM council conformance.

## Required Hermes-native adaptation

Hermes should model v4.1 as a two-level topology:

1. **Sequential council barriers**
   - Decision completes before Failure starts.
   - Failure consumes Decision.
   - Follow-Up consumes Decision and Failure.

2. **Wide intra-council fanout**
   - Each council selects multiple member routes.
   - Each selected member may spawn child/subchild variants where the runtime supports it.
   - Child variants should produce distinct deltas: source-slice scout, falsifier, receipt audit, model/reasoning variant, follow-up improver, boundary review, or mini-MMM salience check.

Hermes may scale this down only by marking the result honestly:

- `SMOKE_FORMAT`: formatting only; no council claim.
- `SMOKE_TOPOLOGY`: minimal topology proof; not v4.1 council conformance.
- `REAL_ATTEMPT_PARTIAL`: real sequential councils attempted, but wide member/child coverage incomplete.
- `REAL_ATTEMPT_FULL`: three council barriers plus selected parent/member coverage plus required child/subchild coverage plus validator/scoring.

## Output rule

User-facing Wizard output should reduce cognitive load, but route truth cannot disappear.

The body should say the decision and next move first. The proof strip or footer must still say whether the run was:

- full v4.1 wide-council coverage;
- partial sequential council coverage;
- parent-reported child coverage;
- blocked/deferred/not-run for wide child obligations.

## Source anchors checked

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`
  - Three sequential councils.
  - Parallelism happens inside a wave.
  - Councils are write barriers.

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/05_RUN_PROTOCOL_AND_RETRY.md`
  - Full run minimum requires dedicated parent members for Decision, Failure, and Follow-Up families.
  - Accepted parents satisfy child quorum when runtime supports children.
  - Useful constrained Max Assembly is usually 3-6 council parents per wave, 2-3 oversight parents per wave, and 5-10 child/subsubagent tasks per counted parent.

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/06_OUTPUT_FORMAT_AND_SCORING.md`
  - Visible answer must reduce cognitive load.
  - Header separates waves, parents, children, tools, score, and runtimes.
  - Output fails if it hides the three LLM councils or route obligations.

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/08_EXAMPLE_OUTPUT.md`
  - Example shows three LLM councils with wide parent and child receipt counts.

- `/Users/joshuaeisenhart/.codex/skills/three-council-wizard-v4-1/SKILL.md`
  - Run shape: three sequential councils.
  - Parallelize inside a council.
  - Child/subsubagent lanes are not optional theater when runtime can launch them.
