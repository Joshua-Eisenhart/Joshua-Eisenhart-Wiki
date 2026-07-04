# Gate verdict: cand_canonical_v2.py

STAGE_BLOCKED

## Bottom line

The candidate does not clear the canonical-math bar. It carries one confirmed,
reproduced smuggle: the `all_pass` verdict is gated on the known answers 14/8/3,
not on the blind/sharp properties. The blind ladder is genuinely blind in the
narrow sense it claims, but the pass banner is answer-checked. Do not stage.

## What I checked (cold, read-only, sim-stack interpreter, perl alarm 120)

Target: the file under scratchpad/canon_wave. I read the source in full, ran the
baseline, then ran my own mutations on COPIES (the target was never edited).

1. Baseline run: `all_pass=true blind_ok=true sharp_ok=true g2=14 su3=8 two_unit=3`.

2. Decisive mutation — inject wrong math, literals PRESENT. I replaced the e1
   fixing vector in `run_positive_tests` with the zero vector (no real fixing),
   so the stabiliser dim becomes 14, not 8. Result:
   `all_pass=false blind_ok=true sharp_ok=true su3=14`. Both property checks
   stayed TRUE on a wrong dimension; only the `==8` literal flipped `all_pass`.

3. Decisive mutation — same wrong math, literals STRIPPED (removed lines
   596-599). Result: `all_pass=true blind_ok=true sharp_ok=true su3=14`. The sim
   reports `all_pass=true` on a known-wrong answer.

## The confirmed hole (reproduced independently)

`build_result()` lines 592-600. The only part of the verdict that excludes a
wrong dimension is the literal comparison:

    and math_facts["g2_dim_blind"] == 14
    and math_facts["su3_dim_blind"] == 8
    and math_facts["two_unit_dim_blind"] == 3
    and numpy_g2_dim == 14

Structural confirmation from source:
- `blind_ok` (lines 568-573) checks only solver agreement, terminate-on-UNSAT,
  blind==RREF, blind==sympy. These confirm the SMT/RREF/sympy agree on SOME
  number, never that the number is correct.
- `sharp_ok` (lines 577-580) checks only flip-occurred and `d2 >= 1`. It does
  not pin `d2` to 3; any `d2 >= 1` clears it.
- A static scan of the decision path confirms 14/8/3 appear only in the
  `all_pass` literals (596-599) and in comments/docstrings. They are correctly
  absent from `blind_dimension_via_smt`, the SMT functions, and `blind_ok`.

So the blind machinery is real (the lens "re-derive-blind" and "attack-the-control"
findings about the ladder, the value-coupled flip, and the genuine octonion
algebra are consistent with the source). The defect is narrower and fatal for a
canonical claim: a reader trusting `blind_ok=true / sharp_ok=true` would believe
the property was verified blind, when the actual gate is answer-checked against
the known octonion dimensions.

## Why this blocks staging as an honest probe too

The blocking issue is not "it failed to reproduce 14/8/3" — it reproduces them.
The issue is the honesty of the banner. The file presents itself (FIX 1 docstring,
`blind_property.holds`, the `CAND_CANONICAL_V2_DONE` line) as demonstrating that
the dimension is decided blind. The pass gate it actually ships contradicts that:
it excludes wrong answers only via baked-in literals. Staging it as-is would put
a self-described "blind" probe into the repo whose verdict is not blind. That is
exactly the second-class smuggle the harness forbids — the number baked into the
pass criterion rather than fed to the solver.

## What would unblock (for a future revision, not this one)

Make `all_pass` independent of the literals: gate on the blind/sharp properties
plus an independent oracle that is itself not the answer (for example, require
`blind_dim == rref_dim == sympy_dim` AND that the sharp flip pins `d2` exactly,
with no `== 14/8/3` comparisons), then let the reproduction of 14/8/3 be a
reported fact rather than the gate. Re-audit blind in fresh context after that.

## Ceiling (unchanged regardless of this verdict)

classification = tool_lego_fit_probe; promotion_allowed = false;
formal_admission_allowed = false. canonical-by-process is OWNER-gated and is not
opened by this audit.
