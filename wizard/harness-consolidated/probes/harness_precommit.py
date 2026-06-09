"""
Consolidated L-proof aggregator — harness-edit gate (not a git hook).

Harness surface encoded: 29_harness_edit_protocol.md (L-meta) +
30_z3_harness_formalization.md (Phase 5 deliverable).

Runs, in order:
    1. All 5 individual z3 encoding test suites (unit-level admissibility tests)
    2. Contract fuzzer over the boolean cube of each encoding (C1–C4 guarantees)
    3. cvc5 cube cross-check against every input cube point (dual-solver ratchet)
    4. MD monotone conjecture probe (regenerating invariant on the composite metric)

Non-zero exit iff any suite reports a failure. This is the structural refusal point:
if any encoding drifts, or if z3/cvc5 disagree on any cube point, or if the MD
monotone conjecture probe changes outcome, the harness has lost a decidability
guarantee and the harness-edit gate refuses.

Scope note (audit 2026-04-18): the wiki harness tree at ~/wiki/wizard/harness-consolidated/ is NOT under
git version control. A git pre-commit hook is therefore not the right gate here —
there is no pre-commit event to attach to. Instead, this script is run manually at
two points:

    - before declaring any harness-edit closeout (per 29_harness_edit_protocol.md)
    - before submitting any session claim that cites harness admissibility predicates

If the wiki harness tree is later placed under git, an installable git-hook shim
can be added; it is deliberately not documented here until that prerequisite exists.

What this aggregator does NOT run:
    - dogfood_session_2026_04_18.py (a point-in-time session claim, not a
      regenerating invariant — cited separately in closeouts)
    - any session-specific bounded-work-unit check (session records live elsewhere)

Run directly:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/harness_precommit.py
"""

import subprocess
import sys
import time
from pathlib import Path

PY = "/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3"
PROBES = Path(__file__).parent

SUITES = [
    ("status-ladder unit", "z3_status_ladder_admissibility.py"),
    ("pre-emit unit", "z3_pre_emit_six_axis.py"),
    ("bounded-work unit", "z3_bounded_work_unit.py"),
    ("gate-ordering unit", "z3_coupling_gate_ordering.py"),
    ("closeout unit", "z3_closeout_completeness.py"),
    ("sim tool-manifest unit", "z3_sim_tool_manifest_completeness.py"),
    ("contract fuzzer", "z3_fuzz_contract.py"),
    ("cvc5 cube cross-check", "cvc5_cross_check.py"),
    ("MD monotone probe", "z3_md_monotone.py"),
    ("metamorphic self-test", "z3_metamorphic_self_test.py"),
    ("closeout shape conformance", "z3_closeout_shape_conformance.py"),
]


def run_suite(label, script):
    path = PROBES / script
    t0 = time.time()
    r = subprocess.run([PY, str(path)], capture_output=True, text=True)
    dt = time.time() - t0
    ok = r.returncode == 0
    return {
        "label": label,
        "script": script,
        "ok": ok,
        "rc": r.returncode,
        "elapsed_s": dt,
        "stdout_tail": r.stdout.strip().splitlines()[-3:],
        "stderr": r.stderr.strip(),
    }


def main():
    print("== L-proof harness pre-commit gate ==")
    results = []
    any_fail = False
    t0 = time.time()
    for label, script in SUITES:
        res = run_suite(label, script)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] {label:<25} rc={res['rc']} {res['elapsed_s']:.2f}s  ({script})")
        if not res["ok"]:
            any_fail = True
            for line in res["stdout_tail"]:
                print(f"        stdout: {line}")
            if res["stderr"]:
                print(f"        stderr: {res['stderr'][:400]}")
    total = time.time() - t0
    print()
    print(f"total: {len(SUITES)} suites, {total:.2f}s")
    if any_fail:
        print("REFUSED: one or more suites failed. Commit blocked.")
        return 1
    print("ADMITTED: every L-proof suite holds. Commit gate open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
