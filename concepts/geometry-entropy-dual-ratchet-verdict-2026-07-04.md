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

## 2026-07-04 update: one turn of the spiral measured live (v1_drive)

Worked out 2026-07-04 in a parallel session; build landed in the live repo (`~/Codex-Ratchet`, commits `4fb9a370d` build + `f8b3cf1fb` lock-ledger repair). Ceiling: `scratch_diagnostic`, `promotion_allowed:false`, capstone DRAFT_UNAUDITED.

`system_v7/sims/ratchet_climb_engine_v1_drive/` rewired the real climb engine from a hand-fed demand list to demands minted by a drive — a noncommutative, entangled, memory-carrying update stream running from tick one (Axis 0 as the drive, not the late readout). Results, verified against the result JSONs and a fresh codex verification lane:

- Drive variant climbed to rung 6; all three kill controls (commuting drive, static demand list, memoryless drive) died at rung 4 (v0's stall); label-shuffle robust at 6. Three-engine parity 0.0, lint 0.
- The two new rungs were forced by drive-minted demands: rung 5 by an entanglement-mixedness fact (an entropy-side fact forcing a geometry-side lift — the mechanical dual-ratchet coupling caught in the act), rung 6 by a noncommuting order fact.
- One defect found and repaired: rejected frontier attempts had been filed in the append-only lock ledger; now locks are admitted-receipts-only with refusals in their own list.

This is one measured entropy-to-geometry turn. The reverse arm (geometry re-carving what entropy can be read) remains structurally present but unearned; the two-sided update test named above is still not built.

### Demotion (same day): capstone audit verdict BY-CONSTRUCTION

The fresh-context capstone audit (commit `8c15c4c8a`, receipt `CAPSTONE_AUDIT_20260704.md` in the sim dir) demoted the section above. The drive facts are computed (Python reduced-state mixedness is real), but demands carried pre-labeled target rungs and the lift was selected by rung lookup, not by an independent admissibility search; jax/numpy share one core and the julia leg hardcodes drive values. Honest ceiling: a designed drive policy produces frontier 6 while designed controls stop at 4 — Axis-0 forcing rungs 5/6 is NOT proven, so no measured spiral turn stands yet. Repair build (fact-only events, blinded lift selector, three independent legs) launched as `ratchet_climb_engine_v2_blind`; a stall there would be a finding, not a failure.

### Second demotion (same day): v2_blind also BY-CONSTRUCTION

The blinded rebuild reached rung 5 (not 6) and its fresh audit killed that too (commit `0a9516630`): the "blinded selector" was a fixed candidate table with explicit rung labels, returning the first candidate on a threshold — a prewired receipt, not a forced lift. Two audits deep, the defect moves one layer down each time (v1: labeled demands; v2: labeled candidates). Pre-registered v3 shape: a standalone separation-witness module (measures whether the current quotient conflates fact-classes, no rung labels, audited before use), then lifts enumerated from ladder definitions and evaluated per-candidate. Standing honest state: no rung past 4 is earned; what is earned is the build-audit-demote loop catching the same smuggle twice.

### End of day: the drive question, honest standing state

Seven rounds on "does the rolling drive power the climb": three fake wins killed by audit, then three fair rounds. Fair verdict so far: the co-arm (locks license readouts; a licensed readout forces a later lift) is real and dies correctly under feedback-cut; but rolling vs dead dice TIE exactly — even with correct commuting controls, correct within-tick order instruments, and a dim-8 carrier with headroom (all live drives: 2 locks, 1 co-turn, identical timing; commits 62594c65e, b0c48fb66, dbbb27070). The identical curves point at the fact vocabulary as the bottleneck: the locks are driven by drive-independent facts and the licensing progression stalls after two locks regardless of drive. Three readings held, none collapsed: (a) the licensed readout vocabulary is still too poor to express what noncommutation mints; (b) the observable is wrong — drive-specificity may live in the CONTENT of what gets locked, not the COUNT; (c) the Axis-0-as-drive claim fails at toy scale. Next session starts at this fork.
