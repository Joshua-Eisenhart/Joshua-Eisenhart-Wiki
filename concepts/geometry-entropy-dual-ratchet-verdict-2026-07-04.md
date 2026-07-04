# Geometry/entropy: not a dual ratchet, but a mechanical dual-ratchet claim survives narrower

Worked out 2026-07-01..04 in Desktop-clone sessions; salvaged from Claude memory 2026-07-04. Source: `project_geometry_entropy_coratchet_not_dual.md`.

## Bottom line

Geometry (distinguishability) is prior. Entropy is a typed, downstream readout — not a second, co-equal ratchet running in parallel with geometry. This was settled 2026-06-17 and is not reopened.

A narrower, later claim from 2026-07-03 is live and distinct: a **mechanical** dual-ratchet, where geometry constrains which flows exist and those flows re-carve which geometry survives the next admissibility pass. This is explicitly not the same claim as the rejected symmetric duality, and does not reopen it.

## The settled 2026-06-17 position

Owner asked: "do we need a dual ratchet with geometry and entropy?"

Answer, grounded in the repo and wiki doctrine:

- **Not two co-equal independent ratchets.** Doctrine forbids it. `concepts/qit-engine-dev-framing.md` states "entropy is not the master variable; distinguishability comes first" and "engine cycles are downstream of the geometry/admissibility spine, not a replacement." This matches the project's `CLAUDE.md` rule: do not use entropy as the master organizing variable.
- **Yes to a single geometry/admissibility ratchet carrying a typed entropy readout** that recomputes per carve — the owner's own reframe: "geometry vs entropy-running-on-geometry, coupled processes."
- **A live divergence held, not collapsed:** the project's anti-collapse rule allows backward admissibility — later-compatible organization can feed back on earlier candidates. So there is a surviving reading where entropy/readout admissibility feeds back as a constraint on geometry candidates. This is still a coupled feedback, not a co-equal peer ratchet. This reading is held open, not resolved away.

## The sim: entropy_geometry_coratchet_floor_v0

Built to owner spec (`Levos packet sim_targets/entropy_geometry_coratchet_floor_v0.md`).

**Verification note (2026-07-04):** this memory originated in a Desktop-clone context and named the path `system_v7/sims/entropy_geometry_coratchet_floor_v0`. Checked against the live `~/Codex-Ratchet` repo on 2026-07-04: the directory exists at `system_v7/sims/entropy_geometry_coratchet_floor_v0/`, containing `entropy_geometry_coratchet_floor_v0_exact.py` and a `results/entropy_geometry_coratchet_floor_v0_exact_results.json`. File presence confirmed only — contents were not re-verified against the memory's claims in this pass. Re-check contents before citing specific numbers from it.

Honest scope, as recorded: capacity/quotient/block/SCC-basin entropy is available and changes under carve, probe, and order. Von Neumann entropy is blocked until density is earned. Fiber/cut entropy is absent until the structure exists. No probability or density or time is meant to be smuggled in.

Status at build time: `scratch_diagnostic`, `draft_unaudited`, `promotion_allowed:false`, not fleet-gated (`all_9_tests_pass=true` was an unaudited self-report at that point).

### Fleet gate result (2026-06-17)

Fleet gate run, reproduced (`passes local rerun`, source SHA-256 matched). Fleet: Claude fabrication-auditor (exhaustive falsifiers) plus DeepSeek-v3.1 plus Grok-4.3, convergent.

**Verdict: partial — earns core, headline oversells.** Still `scratch_diagnostic` / `promotion_allowed:false` — correctly fenced.

**Survives (load-bearing, 3-method convergent, found_fabrication:false):**

- **T5** — static ring constraints commute (exhaustive 66/66); state-dependent running-mean window constraints noncommute (11/15); the noncommutativity is located specifically in the state-dependence (a fixed-threshold control gives 0/15). A real, reproducible N01 result. Empirically supports "geometry/distinguishability drives, entropy is a monotone downstream readout."

**Defects found, correctable, not fatal (3-method convergent):**

1. `honest_scope.earns` claimed "no probability smuggled" — this was false. `scc_basin_entropy` built a normalized `c/total` (summing to 1.0) and fed it into Shannon entropy, the smuggled-equivalence pattern.
2. `all_9_tests_pass:true` overstated the result roughly ninefold — only T5 was strong. T3/T4 were weak. T1/T2 were near-tautological (monotone shrinkage). T7/T8/T9 were guards that pass by construction (capability flags off). T6 was mixed.
3. Two of five controls were decorative (`label_shuffle`, `probe_erasure` cannot fail); `same_cardinality` was real but mislabeled "random" — it is actually the `x0==0` slice.

**Fixed and re-gated clean (2026-06-17, 3-method convergent — fresh fabrication-auditor re-derived T5 independently, plus DeepSeek and Grok):**

- Basin readout changed to count-based: `basin_count_entropy_bits = log2(num_basins) = 4.3923`.
- Shannon-over-probability version fenced explicitly as `shannon_over_basin_distribution_DIAGNOSTIC_uses_probability`.
- `honest_scope` reworded to drop the bare no-smuggle claim.
- Added `discriminator_class` (T5 = discriminator, T7/8/9 = guard, T1/2 = near_tautology) and `load_bearing_result`.
- T5 preserved exactly under the falsifier check: reweighting basins moved the count metric not at all, and moved Shannon from 3.523 to 1.93 — showing the fix isolates the right quantity.
- Still `scratch_diagnostic` / `promotion_allowed:false` — single-engine, stdlib, not promoted.
- These edits are uncommitted working-tree changes (+17/-3) on top of build commit `574d29b6f`. The intended builder, codex2, no-showed (auth revoked); Claude made the surgical edits as a named fallback. The verdict still came from fresh, multi-model context — no self-grading was introduced by this substitution.

## The 2026-07-03 owner sharpening — a narrower, distinct claim

The owner reopened the phrase "dual ratchet," but as a **mechanism** claim, not the rejected symmetric-math duality:

> Operators and entropy must dual-ratchet with the geometry: geometry admits which operator/entropy flows exist; those flows re-carve which geometry survives the next admissibility pass; one-directional progress exists only from the interlock (wheel-and-pawl).

This does **not** reopen the 2026-06-17 verdict. That verdict rejected symmetric duality — the idea that one side is derivable from the other, as co-equal peers. The mechanical duality being reopened here is a claim about mutual constraint on the *next admissible step*, which is a different and narrower claim.

The entropic-monism draft's open question about E-versus-G recompute order is this dual-ratchet mechanism question — not a mere sequencing technicality.

**Test implication named by the owner:** `entropy_surface_terrain_v0` must test the two-sided update — geometry constrains flow, and flow re-carves geometry — not just surface identity at a fixed point.

## What is still open

- Committing the T5 fix (currently uncommitted working-tree changes).
- Then, owner's call: either advance the typed-readout layer, or move toward the geometry-to-ρ_AB bridge — which is gated behind lego and coupling steps in the project's hard stage gate, and is not yet reached.
- The two-sided update test for the narrower mechanical dual-ratchet claim has not yet been built or run.
