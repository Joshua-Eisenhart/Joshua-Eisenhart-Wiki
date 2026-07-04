# CR → Lev canonical-candidate wave receipts — 2026-06-29

Durable receipt for the recursive wave-loop run on the G2/SU(3) canonical candidate. Written because the live artifacts sit in an ephemeral session scratchpad and Hermes correctly flagged "reported by a thread, not durably receipted." Status ladder: exists < runs < passes_local_rerun < lint_pass < canonical_by_process. Nothing here reaches canonical; promotion stays owner-gated.

## Honest bottom line

The candidate `system_v5/ops/formal_scouts/foundation_foundation_r5_g2_su3_reduction_jax.py` is a useful, genuinely-controlled SCOUT. It is NOT canonical and was not promoted. The wave loop's value is that it found, by independent fresh audit, exactly why it must stay fenced — and converted that into the spec for a cleaner candidate.

## Wave chain (one wave at a time, bounded, looping)

| Wave | Task ID | Outcome | Honest status |
|---|---|---|---|
| 1. Verify scout | wr4yyyf6i | scout reaches lint_pass but is honestly only a scout; kept its scratch_diagnostic fence | passes_local_rerun; not canonical |
| 2. Author fresh v2 | w2bn44jls | blind SAT(k)→UNSAT(k+1) ladder genuine (returned 14/8/3/0/64 on 5 inputs, no dim fed to solvers); value-coupled control flips verdict; both z3+cvc5 load-bearing | passes_local_rerun at tool_lego_fit_probe; canonical_grade=FALSE held |
| 3. Fresh-context gate | wgy52momt | STAGE_BLOCKED. Confirmed+reproduced hole: `all_pass`/`blind_ok`/`sharp_ok` are answer-checked against baked-in literals (`==8/14/3`, v2 lines ~596-599). Inject wrong math (fix zero vector not e1) + strip literals → `all_pass=true` on a known-wrong answer. The banner advertises "blind" but the verdict is not blind. | not stageable; gate held |
| 4. Fix→gate wave-set loop | w049o58r0 | FAILED (not content): the check agent rate-limited and returned null; the workflow lacked a null-guard and crashed at `chk.literals_gone`. v3 fix drafted but UNVERIFIED. | inconclusive; re-run when API recovers |

## The confirmed defect (Wave 3, reproduced)

- `blind_ok` checks only solver agreement + terminate-on-UNSAT + blind==RREF==sympy — internal consistency on *some* number, never the *correct* number.
- `sharp_ok` checks only flip-occurred + d2>=1 — does not pin d2 to 3.
- The literals 14/8/3 enter the decision path only inside `all_pass`. Remove them and wrong math passes. So the proof path is answer-checked, not blind.
- Independent corroboration: Hermes read the source scout and found `expected_dim=8` still passed into `z3_structural_proof(..., expected_dim)` / `cvc5_structural_proof(...)` and the success check. Two independent paths (Hermes on source, gate on scratch v2) → same defect.

## The spec for the next candidate (extracted)

A canonical candidate must make `all_pass` derive correctness from STRUCTURE, not literals:
- the target dimension must not enter the proof path as authority (no `expected_dim`);
- the control must have an INDEPENDENTLY-predicted value (candidate route: orbit-stabiliser, dim = dim(g2) − orbit-rank, both computed), non-circular;
- removing/altering a load-bearing constraint must flip the solver verdict;
- decisive acceptance test: inject wrong math with literals stripped → `all_pass` must be false;
- result JSON exposes the claim ceiling.

## Doctrine confirmed (matches Hermes's extraction)

- Recursive serial waves > flat fanout. The earlier ~235-agent two-workflow run rate-limited; this run, one wave deep with ≤2-3 internal workers, did not (until the API itself degraded).
- Receipts > started workers. Scratch > repo mutation. Mechanical gates > narrative. Owner-gated promotion stays owner-gated.
- Builder's verdict is never evidence: the author wave's own verifier reported blind=true/sharp=true; the independent fresh gate caught that those flags weren't load-bearing for correctness.

## Artifacts (session scratchpad — ephemeral; copy on request)

- `scratchpad/canon_wave/cand_canonical_v2.py` (+ `canonical_v2_verdict.md`)
- `scratchpad/canon_wave/gate_verdict.md` (the STAGE_BLOCKED record)
- `scratchpad/canon_wave/cand_canonical_v3.py` (fix attempted, unverified)
- `scratchpad/cr_sim_readiness_report.md`, `sim_census_summary.json`, `readiness_matrix.jsonl`

## Environment note (2026-06-29)

API rate-limiting recurred and the Opus safety classifier was briefly unavailable. Per the loop discipline, no new waves are being spawned while the environment is degraded. Re-run Wave 4 (with a null-guard added to the workflow) once the API recovers.
