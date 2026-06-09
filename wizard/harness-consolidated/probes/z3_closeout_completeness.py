"""
z3 encoding of the closeout-block completeness predicate.

Harness surface encoded: 24_closeout_templates.md.

Four role blocks (S / K / H / R), each with a required field set. A closeout is admissible
iff every required field for its role is present AND no "forward-plan" field is present
(closeouts have no forward-plan field by construction — appending one is skip-ahead).

Role S (sim-worker) required fields:
    probe_family, active_constraints, status_label, result_file_path,
    criteria_tested, surviving_candidates, excluded_candidates,
    divergence_preserved, not_earned_this_session

Role K (controller) required fields:
    gates_cited, admission_decisions, narrative_substitutions_intercepted,
    worker_claims_verified, worker_claims_not_verified,
    status_label_changes_to_registry, blocked_actions

Role H (Hermes) required fields:
    mode_entered, mode_declared_by, files_staged, files_run,
    stage_gate_read, actions_refused_setup_only, handoff_state

Role R (batch-runner) required fields:
    queue_source, queue_position_worked, stage_gate_status_per_queued,
    sims_run_from_admitted_stage_only, sims_skipped_because_queue_not_permission,
    queue_is_not_permission_intercept_fired, result_files_produced

Forward-plan field present → UNSAT (closeouts are bound-exit records, not forward plans).
"""

from z3 import Bool, Solver, And, Not, sat, unsat


ROLE_FIELDS = {
    "S": [
        "probe_family", "active_constraints", "status_label", "result_file_path",
        "criteria_tested", "surviving_candidates", "excluded_candidates",
        "divergence_preserved", "not_earned_this_session",
    ],
    "K": [
        "gates_cited", "admission_decisions", "narrative_substitutions_intercepted",
        "worker_claims_verified", "worker_claims_not_verified",
        "status_label_changes_to_registry", "blocked_actions",
    ],
    "H": [
        "mode_entered", "mode_declared_by", "files_staged", "files_run",
        "stage_gate_read", "actions_refused_setup_only", "handoff_state",
    ],
    "R": [
        "queue_source", "queue_position_worked", "stage_gate_status_per_queued",
        "sims_run_from_admitted_stage_only", "sims_skipped_because_queue_not_permission",
        "queue_is_not_permission_intercept_fired", "result_files_produced",
    ],
}


def closeout_predicate(role, fields_present, forward_plan_present):
    """
    Admissible iff every required field for role is present AND forward_plan is absent.
    """
    required = ROLE_FIELDS[role]
    all_required = And(*[fields_present[f] for f in required])
    return And(all_required, Not(forward_plan_present))


def check(role, record):
    s = Solver()
    fields_present = {f: Bool(f) for f in ROLE_FIELDS[role]}
    forward_plan_present = Bool("forward_plan_present")

    for f in ROLE_FIELDS[role]:
        s.add(fields_present[f] == record.get(f, False))
    s.add(forward_plan_present == record.get("forward_plan_present", False))

    s.add(closeout_predicate(role, fields_present, forward_plan_present))
    return s.check()


def main():
    all_fields_S = {f: True for f in ROLE_FIELDS["S"]}
    all_fields_K = {f: True for f in ROLE_FIELDS["K"]}

    tests = [
        {
            "label": "positive (S): all required fields present, no forward_plan",
            "role": "S",
            "record": {**all_fields_S, "forward_plan_present": False},
            "expected": sat,
        },
        {
            "label": "positive (K): all required fields present, no forward_plan",
            "role": "K",
            "record": {**all_fields_K, "forward_plan_present": False},
            "expected": sat,
        },
        {
            "label": "negative (S): missing 'surviving_candidates'",
            "role": "S",
            "record": {**all_fields_S, "surviving_candidates": False, "forward_plan_present": False},
            "expected": unsat,
        },
        {
            "label": "negative (K): forward_plan_present (skip-ahead)",
            "role": "K",
            "record": {**all_fields_K, "forward_plan_present": True},
            "expected": unsat,
        },
        {
            "label": "negative (K): missing 'blocked_actions'",
            "role": "K",
            "record": {**all_fields_K, "blocked_actions": False, "forward_plan_present": False},
            "expected": unsat,
        },
        {
            "label": "boundary (H): minimal complete Hermes closeout",
            "role": "H",
            "record": {f: True for f in ROLE_FIELDS["H"]} | {"forward_plan_present": False},
            "expected": sat,
        },
    ]

    all_ok = True
    for t in tests:
        result = check(t["role"], t["record"])
        ok = result == t["expected"]
        all_ok = all_ok and ok
        print(f"[{'OK' if ok else 'FAIL'}] {t['label']}\n        expected={t['expected']}, got={result}")

    print()
    print("all tests passed" if all_ok else "one or more tests failed")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
