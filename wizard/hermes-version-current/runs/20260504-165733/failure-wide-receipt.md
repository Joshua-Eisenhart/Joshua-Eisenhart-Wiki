# Failure Council receipt — wide fixture

run_id: 20260504-165733
mode: REAL_ATTEMPT_PARTIAL
wave: Failure
parent_route_id: failure-wide-parent-set
input_receipts: decision-wide-receipt.md
selected_member_obligation:
  expected: 6
  completed: 6
child_subchild_obligation:
  expected_core: 12
  attempted_core: 12
  reroute_attempted: 3
  useful_or_accepted: mixed
  visibility: reported_by_parent plus rerouted file-visible parent checks
nested_visibility: reported_by_parent
model_request: not directly controllable by delegate_task; use current runtime default
model_observed: gpt-5.5 reported by delegate_task metadata for parent batches
verdict: harden_then_execute
artifact_surface: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733/failure-wide-receipt.md

## Council result

Failure Council consumed `decision-wide-receipt.md` and returned `harden_then_execute`.

The Decision receipt is acceptable only as a partial, parent-reported wide Decision fixture. It does not prove raw child/subchild execution or full v4.1 conformance. The next step may proceed only if the validator and final render preserve those boundaries and add checks that reject one-parent-per-council overclaims.

## member_routes

### Popper/falsifier
status: completed_orchestrator
child_routes: 2 attempted, 2 completed, visibility reported_by_parent
decisive_falsifier: parent-reported children cannot validate graph semantics or child-result truth if expected child edges/results come from the same parent envelope being validated.
decisive_check: require independent child graph records and bidirectional equality between parent-reported and child-recorded edges.
outcome: harden
required_hardening: child_id, child_route, child_receipt_path/hash, visibility, verification_status, result_claim_scope; negative cases for nonexistent/omitted/wrong-parent/hidden/orphan child.
evidence_boundary: consumed Decision receipt path via prompt context; no files created.
member_utility: high; isolates self-certified parent graph risk.

### Pushback/boundary
status: completed after reroute
child_routes: original 2 evidence-blocked; reroute launched 1 child with file access; visibility parent summary + file-visible reroute
challenge: `completed_accepted: 13` overclaims controller-level acceptance when child visibility is only `reported_by_parent`.
smallest_viable_correction: rename to `parent_reported_completed` or `parent_reported/provisionally accepted`; rename `accepted_delta` to `proposed_delta` unless artifact-backed.
outcome: proceed_only_with_hardening
required_hardening: distinguish parent_reported, controller_visible, artifact_verified, test_passed; preserve not-full-v4.1 boundary.
evidence_boundary: reroute verified Decision receipt content; no raw child transcripts or validator/test outputs.
member_utility: high; blocks overclaim language.

### Premortem
status: degraded_complete
child_routes: 2 attempted, 2 route returns, but receipt-read evidence blocked in child probes; visibility reported_by_parent
failure_story: six months later, users see topology language that looks authoritative but is fixture/synthetic/fallback/partial, so they conclude Hermes lost v4.1 topology again.
hidden_assumption: users infer fixture/live/partial state correctly from context.
outcome: provisional hardening guidance
required_hardening: label every topology display live/fixture/synthetic/fallback/partial/unavailable; fail if mock/fallback/partial topology is presented as actual topology.
evidence_boundary: based on task frame plus child summaries; not receipt-content verified by those children.
member_utility: high for trust failure prevention, evidence-degraded for receipt specificity.

### Black/Red Hat
status: completed_degraded
child_routes: 2 attempted, 2 completed, both evidence-degraded for receipt content; visibility reported_by_parent
black_hat_risks: false confidence from route completion without receipt access; nominal diversity; validator checking member presence rather than adversarial substance; evidence-boundary leakage.
red_hat_signal: trust signal negative/degraded until receipt-read verification and snippets are visible.
outcome: degraded_pass_for_route_execution_only; blocked_for_receipt-grounded_member_judgment
required_hardening: require explicit readable receipt verification; mark unread receipts degraded/failed; require non-empty Black Hat and Red Hat content.
evidence_boundary: meta-fixture risks and child visibility failures, not receipt-specific audit.
member_utility: fail-closed trust signal.

### Calibration
status: completed after reroute
child_routes: original 2 evidence-blocked; reroute launched 1 child with file access; visibility parent summary + file-visible reroute
calibrated_status: PARTIAL
confidence: high
basis: Decision receipt says REAL_ATTEMPT_PARTIAL, selected members 7/7, child_subchild expected 14, completed_accepted 13, degraded_or_partial 1, visibility reported_by_parent.
model_effort_truth: gpt-5.5 reported by delegate_task metadata; effort not evidenced; child/subchild model identity not raw-verified.
outcome: partial, not full, not blocked
required_hardening: require raw child transcripts or router metadata before stronger model/effort or nested visibility claims.
evidence_boundary: Decision receipt file + narrow child summary; no raw child/subchild transcripts.
member_utility: high status calibration.

### Receipt audit
status: completed after reroute
child_routes: original 2 evidence-blocked; reroute launched 1 child with file access; visibility parent summary + file-visible reroute
receipt_findings: Decision receipt is valid as a partial, parent-reported Decision Council receipt; not valid as raw proof of child/subchild execution.
validator_must_checks: require all 7 selected member routes; child_subchild block; visibility=reported_by_parent unless raw artifacts; graph/dependency semantics; compact envelope sufficiency; negative fixtures for one-parent overclaim, missing child evidence, malformed edge, cycle, future dependency, collapsed alternatives.
outcome: proceed_with_validator_hardening
required_hardening: machine-checkable node IDs, raw child receipts or unavailable labels, per-child validation status, separate dependency edge list, explicit PASS/PARTIAL/FAIL fields.
evidence_boundary: Decision receipt read from disk; child/subchild evidence remains parent-reported only.
member_utility: high validator-hardening route.

## Required hardening before Follow-Up

- Follow-Up must consume this receipt and keep final mode `REAL_ATTEMPT_PARTIAL`, not FULL.
- Validator must reject one-parent-per-council runs that claim v4.1 coverage.
- Validator must require selected member counts for Decision, Failure, and Follow-Up.
- Validator must distinguish parent-reported child summaries from raw child/subchild evidence.
- Validator must preserve partial/degraded child status instead of normalizing it into success.
- Follow-Up options must be prompt-ready and prechecked, not route labels.
