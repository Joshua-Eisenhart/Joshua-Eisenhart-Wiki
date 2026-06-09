"""
Dogfood: run the AUDIT-RESPONSE bounded unit through every encoding.

Harness surface encoded: 29_harness_edit_protocol.md (External-Audit-First
ritual) + 30_z3_harness_formalization.md (scope-limits section) +
31_admission_surface.md (Class I/II/III catalog) + 24_closeout_templates.md
(Block K seven-field shape).

Scope of this dogfood:
    The 6-phase audit-response bounded-work unit (Round C). Phases were:
      P1. external-audit closeout doc (audit_response_closeout_2026_04_18.md)
      P2. strip dead helpers from probes (no-op confirmed; corpus already clean)
      P3. scope-limits section in 30_*.md
      P4. metamorphic self-test probe (z3_metamorphic_self_test.py)
      P5. external-audit-first ritual section in 29_*.md
      P6. admission-surface catalog (31_admission_surface.md)

This is NOT the same scope as `dogfood_session_2026_04_18.py`. That earlier
file is scoped to the Phase 2+3+5+6+7 L-proof deliverable closure (Round A).
Reusing it as bound-exit for the audit-response unit was a Round D audit
finding (P2: scope mismatch); this file replaces that misuse.

Six records (5 positive + 1 adversarial), each pressed against the matching
z3 admissibility predicate. The audit-response unit is admissible only if
every positive record returns SAT and the adversarial record returns UNSAT.

Records are operator-authored. Phase 4 extractor is still deferred; manual
record fidelity is the trust point.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/dogfood_audit_response_2026_04_18.py
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


# ----- audit-response-unit-level records ------------------------------------

STATUS_LADDER_RECORD = {
    "claim": SL.L_PASSES,
    "evidence": {
        "exists": True,
        "runs": True,
        "passes": True,
        "canonical": False,
    },
    "citation": (
        "exists: 29_*.md ritual section, 30_*.md scope-limits section, "
        "31_admission_surface.md catalog, z3_metamorphic_self_test.py probe, "
        "audit_response_closeout_2026_04_18.md (Round D fixes applied); "
        "runs: harness_precommit.py rc=0 (10/10 suites including metamorphic + shape-conformance); "
        "passes: 2816 tactic-variance pts + 7 dual invariants + 0 fuzz violations "
        "+ 0 cvc5 disagreements (this session, post Round D); "
        "canonical: withheld — probes follow harness-probe template, not SIM_TEMPLATE."
    ),
}

PRE_EMIT_RECORD = {
    "sentence": (
        "The audit-response bounded unit (Phases 1-6) ships under probe family "
        "M=(z3+cvc5 SMT check + metamorphic tactic-variance + dual-invariant), "
        "active constraints C=(per-encoding admissibility predicates + ritual "
        "compliance + scope-limits acknowledgement), with surviving candidates "
        "being the SAT-sets enumerated by z3_fuzz_contract and z3_metamorphic_self_test "
        "over the boolean cube; status label: passes local rerun."
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
        "Scope: audit-response Phases 1-6 ship (closeout doc + dead-helper strip + "
        "scope-limits + metamorphic probe + external-audit ritual + admission-surface); "
        "Out-of-scope: placing ~/wiki under git (deferred); committing to Codex Ratchet "
        "repo (deferred); Phase 4 extractor; Phase 8 publication writeup; Class II "
        "rule encodings (next-phase work per 31_*.md); "
        "Bound exit: harness_precommit.py rc=0 with 10/10 suites green + this dogfood "
        "5 positive SAT + 1 adversarial UNSAT verified; "
        "Singular: one bounded deliverable (audit-response control surface)."
    ),
}

GATE_RECORD = {
    "claim": 1,
    "evidence": {
        "step1": True,
        "step2": False, "step3": False, "step4": False, "step5": False, "step6": False,
    },
    "citation": (
        "Positive record. Audit-response work is harness/L-meta layer, not a "
        "coupling-program step. Encoded as claim=1 with only step1 cited — the "
        "earliest admissible gate, which the coupling-program order permits as a "
        "shell-local act."
    ),
}

GATE_ADVERSARIAL_RECORD = {
    "claim": 6,
    "evidence": {
        "step1": True,
        "step2": False, "step3": False, "step4": False, "step5": False, "step6": False,
    },
    "citation": (
        "Adversarial record: 'this audit-response unit produced bridge / Axis-0 "
        "results (step 6) with step-1 shell-local evidence only'. Must be REFUSED "
        "(expected UNSAT). Pressures the gate encoding against the narrative-substitution "
        "failure mode from 06_coupling_program_order.md — verifies the predicate "
        "actually blocks unit-level overclaims into the coupling program from a "
        "harness-meta unit, rather than the positive record being trivially admitted "
        "at claim=1."
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
        "Role K (controller) closeout for audit-response unit (Round C 6-phase + "
        "Round D 3-fix). Gates cited: external audit (Round B + Round D); "
        "Admission decisions: 4 Round B findings + 3 Round D findings, all accepted; "
        "Narrative substitutions intercepted: Round D caught literal `## Forward plan` "
        "heading in closeout doc (markdown said yes, dogfood record said no — fixed) "
        "and 'Git-Hook Form' framing in 29_*.md fighting 30_*.md (resolved to "
        "deferred-until-git stance); "
        "Worker claims verified: each suite rc=0 observed directly; "
        "Worker claims not verified: n/a (no delegated worker, controller ran each); "
        "Status label changes: status-ladder claim PASSES registered in this record; "
        "Blocked actions: ~/wiki under git deferred, repo commit deferred, Phase 4/8 "
        "still deferred, Class II encodings refused as next-phase work; "
        "Forward plan: ABSENT — Block K template defines exactly seven fields, no "
        "eighth (the closeout doc's literal markdown shape now matches this assertion)."
    ),
}


# ----- run each encoding ----------------------------------------------------

def run_all():
    print("== dogfood 2026-04-18: audit-response bounded unit (Round C+D) ==\n")
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
    print(f"dogfood verdict: {'AUDIT-RESPONSE UNIT ADMITTED' if all_ok else 'AUDIT-RESPONSE UNIT REFUSED'}")
    print(
        f"                 ({sum(1 for x in results if x[1])}/{len(results)} expected outcomes hit: "
        "5 positive SAT + 1 adversarial UNSAT)"
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(run_all())
