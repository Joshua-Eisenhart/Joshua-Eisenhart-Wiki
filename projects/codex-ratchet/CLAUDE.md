# CLAUDE.md — agent contract for the constraint-core bundle

You are working inside a formal research bundle with strict claim discipline.
Read this whole file before editing anything. It is short on purpose.

## What this is
A machine-checked formalization of a constraint-based theory (single-qubit GKSL
dynamics + a layered spec). Everything is `scratch_diagnostic`,
`promotion_allowed=false`. The ratchet earns canon; you do not.

## The one command that matters
```
python3 run_all.py
```
Must exit 0 (GREEN) **before and after** any change you make. It runs all 20
sims and asserts their headline invariants with tolerances. JAX sims are
skipped automatically if jax is absent; that is still GREEN.

## Hard rules (violating any of these is the failure mode this file exists to prevent)

1. **Never edit an expected value in `run_all.py` to make a check pass.** A
   mismatch between a sim and its expected value is a FINDING — report it, do
   not resolve it. Same for mismatches between the spec and a sim: divergence
   is data, not a bug to silently harmonize.
2. **Some expected results are honest failures. They must stay failed.**
   - `manifold_build_ladder.py`: `doctrine realized ... : False` — the Axis-0
     entropy doctrine does NOT hold at density level. Making it True is a
     regression, not a fix.
   - `engine_64_schedule_sim.py`: order-blind collapse `11/64` — the collapse
     is the point.
3. **Withdrawn claims — never restore these, even if older text in the corpus
   still asserts them:**
   - the "linear gauge-breaking law, R² = 1.0" (§7o — withdrawn; it was an
     affine identity of a one-step Kraus parametrization);
   - the "threefold convergence" of §7o/§7p/§7q (it is ONE bit — non-unitality
     `L(I) ≠ 0` — read three ways);
   - the flat "16/16 access theorem" of §7s (the earned form is two-tier:
     exact on the 8 dephasing stages, 14/16 under a chirality-neutral probe,
     16/16 only with the sheet Hamiltonian adopted into the loop definition);
   - "the §7q null supports fusion" (a null cannot; fusion is settled by the
     containment split + W-covariance §7t, not by the metric null).
4. **Sims are pure math. No labels in code.** Structural indices only
   (`eps, a1, a2, t0..t7, Ti/Te/Fi/Fe`). All naming — terrain names, Jungian
   labels, physics vocabulary ("gauge", "Weyl", "geometric phase") — lives in
   `data_json/rosetta_layer.json` with earned/witness/candidate tiers. Never
   move a label from the rosetta into a sim, and never change a label's tier.
5. **Do not conflate V and W (§7u).** `V = exp(−iH₀s)` is the continuous state
   gauge (commutes with the engine flow; carries the δ=0 degeneracy and
   K = H₀). `W = (σx+σz)/√2` is the discrete pair-duality (swaps Ti↔Te, Fi↔Fe
   exactly; does NOT commute with the flow). They are provably distinct; code
   or text that substitutes one for the other is wrong.
6. **Owner-level open decisions — do not resolve them yourself:**
   - the two-64s tension: §7g's `64 = 2×8×4` (all combos runnable) vs
     §7r's `16 = 8×2` native stages (which makes 64 = 16 stages × 4
     sub-stages, with 48 combos inadmissible). Incompatible counts; flagged
     in the spec; the owner decides.
   - the terrain-level direct/conjugated bit (a2 on terrains): realized by
     NEITHER V nor W at generator level (§7u); currently rests on the source
     table. Finding its generator-level invariant is open work, not a lookup.
   - χ₂ (the open-path eigenvector-sector readout): CLOSED at the frame level
     (§7v, chi2_openpath_readout_sim.py) — the Bargmann open-path phase reads
     the direct↔conjugated frame bit on 99.7% of probes; entropy blind. Closed
     loops provably fail (that part stands). The remaining open item is now the
     terrain-level a2 bit above, not χ₂.
7. **Comparisons are tolerance-based, never `==`** on floats. Claim grades per
   spec §8: promotable rows need `symbolic_identity` / `closed_form` /
   `finite_exhaustive` routes; float tolerance is `diagnostic_float_nonclaim`.
8. **Do not regenerate figures** unless explicitly asked; `figures/` is
   pre-rendered and matplotlib is deliberately not a requirement.
9. **Determinism:** all stochastic sims are seeded. If you add a sim, seed it
   (`np.random.default_rng(0)`), make it standalone, CWD-independent, print
   its headline invariants to stdout, and add a `run_all.py` entry.
10. **When editing the spec**, corrections are logged visibly (see §7o's
    correction note for the required style) — never silently rewritten. New
    claims get an explicit claim ceiling.

## Map
```
ORIENTATION.md                  canonical orientation (root; the copy in
                                spec_and_reports/ is a pointer stub)
CLAUDE.md                       this file
run_all.py                      verification harness (exit 0 = green)
requirements.txt                numpy/scipy/sympy required; jax optional
spec_and_reports/
  CONSTRAINT_CORE_FORMAL_SPEC.md  the spec (§0–§10; manifold arc §7–§7u)
  PURE_MATH_CORE.md               de-jargoned proposition ledger P1–P11
  constraint_core_methods_report.md, geometric_manifold_consolidated.md
sims_and_scripts/               20 standalone sims (pure math, no labels)
  out/                          scratch output of manifold_build_ladder.py
data_json/                      per-sim result data + rosetta_layer.json
figures/                        pre-rendered PNGs (do not regenerate)
inputs/                         owner's original source spreadsheet
```

## Orientation for the math itself
Read, in order: `ORIENTATION.md` → `spec_and_reports/PURE_MATH_CORE.md`
(compact, label-free, P1–P11) → the spec sections you need. The pure core is
the fastest way to load the actual mathematics without absorbing overlay
vocabulary as if it were structure.
