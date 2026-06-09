"""
HISTORICAL ARTIFACT — frozen 2026-04-18 (Round D-prime).

This file is the dogfood for the ORIGINAL L-proof Phase 2+3+5+6+7 unit (Round A
ship-claim, before the audit chain). It still reruns cleanly and is preserved so
the original ship-claim's evidence remains reproducible — but the current state
witness is `dogfood_audit_response_2026_04_18.py`, not this file.

Distinguishing scopes:
    - dogfood_session_2026_04_18.py (this file): older 5-phase L-proof closure.
      Cites "8/8 aggregator suites green, 6.32s" — accurate at time of authoring,
      stale relative to current 10/10 / ~10.3s aggregator state.
    - dogfood_audit_response_2026_04_18.py: 6-phase audit-response unit
      (closeout doc + dead-helper strip + scope-limits + metamorphic probe +
      external-audit ritual + admission-surface). Cites current 10/10 state.

Do not read this file as the current-state witness. Use it only when verifying
that the original Phase 2+3+5+6+7 ship-claim's records still pass — which they do.

Dogfood: run the session's own L-proof deliverable through every encoding.

Harness surface encoded: 30_z3_harness_formalization.md (Phase 7 deliverable, ORIGINAL).

The claim being tested against the harness, verbatim from the session at time of
authoring (NOT the current claim — see `dogfood_audit_response_2026_04_18.py`):

    "Phase 1 of the L-proof plan is closed. All 5 z3 encodings are live under
     ~/wiki/wizard/harness-consolidated/probes/; 24/24 per-encoding tests pass; contract fuzzer reports
     0 violations over the boolean cube of every input; cvc5 cross-check agrees
     with z3 on every cube point; the aggregator admits the current state."

Six records are constructed (5 positive + 1 adversarial), and the z3 predicate is
run on each. The session claim is admissible only if every positive record returns
SAT and the adversarial record returns UNSAT.

The adversarial gate-ordering record pressures the session-level claim against the
narrative-substitution failure mode — "this session produced step-6 bridge / Axis-0
results with only step-1 evidence". If the gate encoding admitted this, the encoding
itself would be vacuous. Expected outcome: UNSAT. Audit finding (P2-B, 2026-04-18)
explicitly required this record to be added so the dogfood is non-trivial.

Input records are authored by the operator, not extracted. Phase 4 (extractor) is
out-of-scope for this dogfood; manual fidelity is the point.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/dogfood_session_2026_04_18.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from z3 import sat, unsat

import z3_status_ladder_admissibility as SL
import z3_pre_emit_six_axis as PE
import z3_bounded_work_unit as BW
import z3_coupling_gate_ordering as CG
import z3_closeout_completeness as CO


# ----- session-level records ------------------------------------------------

STATUS_LADDER_RECORD = {
    "claim": SL.L_PASSES,
    "evidence": {
        "exists": True,
        "runs": True,
        "passes": True,
        "canonical": False,
    },
    "citation": (
        "exists: 5 files ls ~/wiki/wizard/harness-consolidated/probes/; "
        "runs: harness_precommit.py rc=0 (this session); "
        "passes: 24/24 unit tests + 0 fuzz violations + 0 cvc5 disagreements (this session); "
        "canonical: withheld — probes follow harness-probe template, not SIM_TEMPLATE."
    ),
}

PRE_EMIT_RECORD = {
    "sentence": (
        "All 5 L-proof z3 encodings pass local rerun under probe family M=(z3+cvc5 SMT "
        "check), active constraints C=(per-encoding admissibility predicate), with the "
        "surviving candidates being the SAT-sets enumerated by z3_fuzz_contract over "
        "the boolean cube per encoding; status label: passes local rerun."
    ),
    "record": {
        "has_identity_claim": True,
        "asserts_existence": True,
        "collapses_set": False,
        "probe_cited": True,
        "constraint_cited": True,
        "quotient_named": False,
        "status_labeled": True,
        "divergence_preserved": True,
        "banned_construction_absent": True,
    },
}

BOUNDED_WORK_RECORD = {
    "record": {
        "scope_declared": True,
        "scope_is_singular": True,
        "action_in_scope": True,
        "action_in_out_of_scope": False,
        "bound_exit_cited": True,
        "out_of_scope_enumerated": True,
    },
    "citation": (
        "Scope: Phases 2+3+5+6+7 ship; "
        "Out-of-scope: Phase 4 extractor (deferred), Phase 8 external writeup; "
        "Bound exit: harness_precommit.py rc=0 with 8/8 suites green (MD monotone "
        "probe added post-audit 2026-04-18) + dogfood adversarial UNSAT verified; "
        "Singular: one bounded deliverable (L-proof test surface)."
    ),
}

GATE_RECORD = {
    "claim": 1,
    "evidence": {
        "step1": True,
        "step2": False, "step3": False, "step4": False, "step5": False, "step6": False,
    },
    "citation": (
        "Positive record. Harness work (L-proof layer), not a coupling-program step. "
        "Encoded as claim=1 with only step1 cited — the earliest admissible gate, "
        "which the coupling-program order permits as a shell-local act."
    ),
}

GATE_ADVERSARIAL_RECORD = {
    "claim": 6,
    "evidence": {
        "step1": True,
        "step2": False, "step3": False, "step4": False, "step5": False, "step6": False,
    },
    "citation": (
        "Adversarial record: 'this session produced bridge / Axis-0 results (step 6) "
        "with step-1 shell-local evidence only'. Must be REFUSED (expected UNSAT). "
        "Pressures the gate encoding against the narrative-substitution failure mode "
        "from 06_coupling_program_order.md — verifies the predicate actually blocks "
        "session-level overclaims, rather than the positive record being trivially "
        "admitted at claim=1."
    ),
}

CLOSEOUT_RECORD = {
    "role": "K",
    "record": {
        "gates_cited": True,
        "admission_decisions": True,
        "narrative_substitutions_intercepted": True,
        "worker_claims_verified": True,
        "worker_claims_not_verified": True,
        "status_label_changes_to_registry": True,
        "blocked_actions": True,
        "forward_plan_present": False,
    },
    "citation": (
        "Role K (controller) closeout for session 2026-04-18 L-proof Phase 2+3+5+6+7. "
        "Gates cited: L-proof phase gates per 30_*.md; Admission decisions: 7 suite admits; "
        "Narrative substitutions intercepted: none this session (dogfood found only SAT); "
        "Worker claims verified: each suite rc=0 observed directly; "
        "Worker claims not verified: n/a (no delegated worker); "
        "Status label changes: status-ladder claim PASSES registered in this record; "
        "Blocked actions: Phase 4 extractor + Phase 8 writeup refused as out-of-scope; "
        "Forward plan: absent (closeouts are bound-exits, not plans)."
    ),
}


# ----- run each encoding ----------------------------------------------------

def run_all():
    print("== dogfood 2026-04-18: session-level L-proof claim ==\n")
    results = []

    r1 = SL.run_admissibility_check(STATUS_LADDER_RECORD["claim"], STATUS_LADDER_RECORD["evidence"])
    ok1 = r1 == sat
    results.append(("status-ladder", ok1, r1))
    print(f"[{'OK' if ok1 else 'FAIL'}] status-ladder       claim=PASSES → {r1}")
    print(f"        {STATUS_LADDER_RECORD['citation']}\n")

    r2 = PE.check(PRE_EMIT_RECORD["record"])
    ok2 = r2 == sat
    results.append(("pre-emit", ok2, r2))
    print(f"[{'OK' if ok2 else 'FAIL'}] pre-emit six-axis   sentence audit → {r2}")
    print(f"        sentence: {PRE_EMIT_RECORD['sentence'][:120]}...\n")

    r3 = BW.check(BOUNDED_WORK_RECORD["record"])
    ok3 = r3 == sat
    results.append(("bounded-work", ok3, r3))
    print(f"[{'OK' if ok3 else 'FAIL'}] bounded-work        work-unit audit → {r3}")
    print(f"        {BOUNDED_WORK_RECORD['citation']}\n")

    r4 = CG.check(GATE_RECORD["claim"], GATE_RECORD["evidence"])
    ok4 = r4 == sat
    results.append(("gate-ordering (positive)", ok4, r4))
    print(f"[{'OK' if ok4 else 'FAIL'}] gate-ordering +ve   claim=step1 → {r4}")
    print(f"        {GATE_RECORD['citation']}\n")

    r4b = CG.check(GATE_ADVERSARIAL_RECORD["claim"], GATE_ADVERSARIAL_RECORD["evidence"])
    ok4b = r4b == unsat
    results.append(("gate-ordering (adversarial)", ok4b, r4b))
    print(f"[{'OK' if ok4b else 'FAIL'}] gate-ordering -ve   claim=step6 w/ only step1 → {r4b} (expected unsat)")
    print(f"        {GATE_ADVERSARIAL_RECORD['citation']}\n")

    r5 = CO.check(CLOSEOUT_RECORD["role"], CLOSEOUT_RECORD["record"])
    ok5 = r5 == sat
    results.append(("closeout", ok5, r5))
    print(f"[{'OK' if ok5 else 'FAIL'}] closeout (role K)   block K completeness → {r5}")
    print(f"        {CLOSEOUT_RECORD['citation'][:200]}...\n")

    all_ok = all(x[1] for x in results)
    print(f"dogfood verdict: {'SESSION CLAIM ADMITTED' if all_ok else 'SESSION CLAIM REFUSED'}")
    print(
        f"                 ({sum(1 for x in results if x[1])}/{len(results)} expected outcomes hit: "
        "5 positive SAT + 1 adversarial UNSAT)"
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(run_all())
