# Canonical-readiness verdict: G2/SU(3) reduction scout

## Bottom line

The scratch copy is mechanically clean: py_compile exit 0, run exit 0, no open mechanical gaps. No formal linter (pyflakes/ruff/flake8) is installed in the repo env, so there is no flake-level lint pass — only a compile/parse check. It is not canonical, and it should not be promoted. The sim is honestly a scout. Its real load-bearing signal (the SMT erase-flip control) is genuine, but the headline `dim 8 = SU(3)` claim is checked against a basis the same script computes, not re-derived independently. Keep the `scratch_diagnostic` fence. Promoting it would be greenwash. The next move is to author a fresh canonical sim, not to flip this one.

Honest ladder reached: `exists < runs < passes_local_rerun < py_compile_pass` — reached `py_compile_pass` (compile/parse only; no flake linter installed). Not `lint_pass`, not `canonical`.

## 1. Is the scratch copy now canonical-clean?

Yes on the mechanical axis, verified this session with the Makefile interpreter (`/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3`):

- `py_compile`: exit 0.
- run: exit 0, `all_pass=true`, computed dims `der_O=14, fix_e1=8, two_unit=3, forced_comm=15`, z3 and cvc5 both `unsat`.
- Result JSON writes into the scratch dir only. The real repo path `system_v5/ops/formal_scouts/results/foundation_foundation_r5_g2_su3_reduction_jax_results.json` shows no change in `git status`.
- The two earlier mechanical gaps (G3 template skeleton, G4 result path) are closed and stay closed.

So "canonical-clean" in the mechanical sense (py_compile 0, run 0, no mechanical gaps) is true; note this is a compile check, not a flake-linter pass (none is installed). "Canonical" in the process sense is false — see section 3.

## 2. Is it genuinely canonical-worthy, or honestly only a scout?

Honestly only a scout. Reasons, separated by what survives and what does not.

What is genuinely load-bearing:
- The erase-flip control is real. Dropping the `D(e1)=0` rows flips both z3 and cvc5 from `unsat` to `sat` (`erase_flip_unsat_to_sat=True` for both). That is a true ablation: the SMT verdict depends on a constraint that is actually removed, not on a flag.
- The controls compute distinct dimensions (14 / 8 / 3 / 15), not by-construction echoes of a target. The forced-commutative control changes the table and yields a different dim (15), so it is a real perturbation, not a relabel.
- The mathematics is sound: `Der(O) = g2` has dim 14; the stabilizer of one imaginary unit is `su(3)`, dim 8. The code recovers both from exact-rational RREF, not from a literal.

What blocks "canonical-worthy":
- The SMT "no extra kernel" proof is bound to the RREF nullspace the same script computes. z3/cvc5 verify that no vector outside the script's own 8-vector free-coordinate basis satisfies the constraints. That is internal consistency of the computed nullspace, not an independent re-derivation of dim 8. The `expected_dim=8` value is passed in; the solvers are not asked to find the dimension blind.
- The negative assertion for the forced-commutative control is only `dim != 8` (`forced_commutative_dim_differs`). A `!=` guard is a weak control: many wrong tables would also differ from 8. It does not pin a specific predicted dimension, so it is a sanity perturbation rather than a sharp falsifier.
- The `density_guard` (`trace=1, psd=True, rho=I/dim`) is a constant stub, not computed from the carrier. It is harmless because the result explicitly says the stabilizer dim is not inferred from rho, but it is decorative, not load-bearing, and a canonical sim should not carry a hard-coded density block.

Net: one genuine load-bearing control (erase-flip) plus correct math, sitting next to a self-referential main proof and a weak `!=` control. That profile is a scout, not a canonical anchor.

## 3. Owner-gated decisions remaining

These were not touched and must not be auto-flipped. They are the promotion-ceiling decisions the task fences.

- G1 — classification value. `classification = "scratch_diagnostic"` (line 35) is not a SIM_TEMPLATE canonical value (`"classical_baseline"` or `"canonical"`). Moving it is the promotion-ceiling decision. Owner-gated. My honest recommendation: do not move it; the sim has not earned `canonical`.
- G2 — promotion ceiling. `promotion_allowed=False` and `formal_admission_allowed=False` (lines 37-40), and the `all_pass` guard in `build_result` (lines 611-614) hard-requires the scratch ceiling (`classification == "scratch_diagnostic"`, both flags `False`, `reads_peer_result False`). The candidate is internally consistent: `all_pass` is conditioned on staying at the scratch ceiling. Any promotion needs the owner to change the classification value AND relax this guard together. Owner-gated. The internal assertion path at the all_pass guard was left intact.

There is no third hidden ceiling: the file does not promote itself anywhere.

## 4. Diff summary: scratch vs original

`diff /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/foundation_foundation_r5_g2_su3_reduction_jax.py <scratch>` shows three honest changes, all mechanical, none touching a verdict:

1. Result path repointed (lines 29, 32-33). `ROOT` and `SOURCE_PATH`/`RESULT_PATH` moved from the hard-coded `/Users/joshuaeisenhart/Codex-Ratchet` tree to `Path(__file__).resolve().parent`, so the run writes into the scratch dir. This is what keeps the real repo untouched.
2. Three SIM_TEMPLATE section wrappers added (lines 465-557): `run_positive_tests`, `run_negative_tests`, `run_boundary_tests`. They delegate to the already-computed `summarize_system` / `z3_structural_proof` / `cvc5_structural_proof` and return the same dicts that already populate the result. No new computation, no changed verdict.
3. Canonical result keys added to `build_result` (lines 703-753): `probe_family`, `constraint_set`, `positive`, `negative`, `boundary`, `criteria_checked`. Values are copied from locals already computed in the function. No new verdict.

The wrappers and the result keys are duplicative of substance that already existed. They satisfy SIM_TEMPLATE structural literalism honestly (real key names over real computed values), but they add no new evidence. That is the correct reading: the fix closed a template-shape gap, it did not raise the evidentiary tier.

## 5. Next move

Author a fresh canonical sim. Do not apply-to-repo as a promotion.

- Apply-to-repo (owner-gated): the only repo-applicable changes here are the three mechanical edits (path, wrappers, keys). Applying them to the real scout is fine as a tidy-up if the owner wants the scout to carry SIM_TEMPLATE section names, but it must keep `classification = scratch_diagnostic` and both flags `False`. It does not make the scout canonical and must not be described that way.
- Recommended: write a new canonical sim that fixes the two evidentiary weaknesses. (a) Make the SMT proof derive the stabilizer dimension without passing `expected_dim` — assert the constraint system and have the solver establish the kernel dimension, so the 8 is not an input. (b) Replace the `!= 8` forced-commutative control with a sharp predicted dimension, or with a value-coupled control whose predicted dim is computed independently. Start from `system_v4/probes/SIM_TEMPLATE.py`, set `classification` honestly only once those hold, and run a fresh-context audit before any promotion.

Promoting the current file would be greenwash: it would label a scout `canonical` on the strength of a self-referential main proof and one weak control. The erase-flip is good evidence, but one good control does not clear the canonical bar. Keep the fence; build the real one.
