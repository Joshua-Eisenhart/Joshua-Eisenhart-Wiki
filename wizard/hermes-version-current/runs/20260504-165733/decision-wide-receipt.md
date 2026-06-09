# Decision Council receipt — wide fixture

run_id: 20260504-165733
mode: REAL_ATTEMPT_PARTIAL
wave: Decision
parent_route_id: decision-wide-parent-set
input_receipts: none
selected_member_obligation:
  expected: 7
  completed: 7
child_subchild_obligation:
  expected: 14
  completed_accepted: 13
  degraded_or_partial: 1
  visibility: reported_by_parent
nested_visibility: reported_by_parent
model_request: not directly controllable by delegate_task; use current runtime default
model_observed: gpt-5.5 reported by delegate_task metadata for all parent batches
verdict: validator_first_wide_fixture
artifact_surface: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733/decision-wide-receipt.md

## Council result

Decision selected the next bounded move:

Build and validate a wide-council fixture that treats Wizard v4.1 as three sequential LLM councils with wide parallel parent/member and child/subchild work inside each council. The fixture should use compact receipt envelopes and graph/dependency semantics, and it must not promote one-parent-per-council minimal topology to full v4.1 coverage.

## member_routes

### Strategy
status: completed_orchestrator_parent
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
accepted_delta: selected validator-first wide fixture as the smallest useful bounded move.
risks_for_failure_council: one parent per council mistaken as wide proof; Follow-Up accepted without Failure evidence; validator overfit to a single chain.
evidence_boundary: prompt context plus parent-reported children; no raw child transcripts.
member_utility: scope control and sequence choice.

### Systems
status: completed_orchestrator_parent
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
accepted_delta: validator must check dependency graph semantics: lineage, member routes, council order, fan-in/fan-out, dependency edges.
risks_for_failure_council: parent partial output mistaken for full council state; summaries collapse dissent/provenance; happy-path fixture misses skipped/malformed cases.
evidence_boundary: prompt context plus parent-reported children; no raw child transcripts.
member_utility: structural dependency and second-order risk map.

### Factory
status: completed_orchestrator_parent_partial
child_routes: 2 attempted, 1 completed, 1 partial due no filesystem/repo visibility, visibility reported_by_parent
accepted_delta: bottleneck is validator/reducer throughput; require compact per-member fixture envelope.
risks_for_failure_council: noisy Decision artifacts; false confidence from partial summaries; transcript-heavy validator latency.
evidence_boundary: prompt context plus parent-reported children; no raw child transcripts.
member_utility: reproducible artifact shape and validator throughput constraint.

### Hume/evidence
status: completed_evidence_bounded_partial
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
accepted_delta: prior member assertions are prompt-provided context until verified by artifacts.
risks_for_failure_council: overclaiming implementation/test passage; conflating selected strategy with proof; compact envelopes may omit adjudication fields.
evidence_boundary: no repo, validator, or fixture state verified here.
member_utility: evidence discipline and proof boundary.

### Feynman/testability
status: completed_orchestrator_parent
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
accepted_delta: dependency graph semantics must become observable pass/fail gates: unique nodes, existing deps, DAG/no cycles, no future-council deps, explicit sibling deps, partial-parent limits.
risks_for_failure_council: schema checks may miss graph semantics; compact envelopes may under-carry diagnostic evidence.
evidence_boundary: proposed testability constraints, not code proof.
member_utility: concrete validator pass/fail criteria.

### Zhuangzi/alternatives
status: completed_orchestrator_parent
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
accepted_delta: preserve alternatives and prevent selected-route collapse; validator should be a spine across councils, not a preflight only.
risks_for_failure_council: single-parent collapse; over-compressed envelope; dependency-blind selection; sequential-council flattening.
evidence_boundary: no repo/files inspected; reasoning only from supplied context and child summaries.
member_utility: anti-collapse and alternative topology constraints.

### Outside evaluator
status: completed_orchestrator_parent
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
accepted_delta: compact envelopes need provenance, uncertainty, omitted evidence, validation status, and dependency links to prevent false completeness.
risks_for_failure_council: validator bias; correlated agreement; schema compliance replacing substantive decision quality.
evidence_boundary: prompt context plus parent-reported children; no raw child transcripts.
member_utility: outside auditability constraint.

## Accepted constraints for Failure Council

- Failure must consume this receipt.
- Treat child/subchild proof as `reported_by_parent` unless controller-visible raw child artifacts become available.
- Falsify graph/dependency semantics, not just schema shape.
- Falsify one-parent-per-council overclaim explicitly.
- Test whether compact envelopes preserve enough provenance, uncertainty, alternatives, and evidence boundary.
- Decide whether wide fixture can proceed, must harden, must split smaller, or is blocked by delegate_task visibility.
