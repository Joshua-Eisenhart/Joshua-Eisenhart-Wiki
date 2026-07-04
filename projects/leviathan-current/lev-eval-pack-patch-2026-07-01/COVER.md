# Patch: Codex-Ratchet sim evaluator packs for core/eval

For: JP (lev-os/leviathan)
From: Josh (built by Fable/Claude + codex gpt-5.5, verified locally)
Date: 2026-07-01
Base: `origin/main` @ aa35fc457 (verified still current at package time). 3 commits.

## Apply
```
git checkout main
git am 0001-*.patch 0002-*.patch 0003-*.patch
```
(Verified the series applies clean to a fresh origin/main checkout.)

## What it is
Two Codex-Ratchet sim evaluator packs over core/eval, following the `intent_conservation` reference pack exactly (same `lev.evaluator_pack.v1` manifest, entrypoints, `lev.evaluator.gate_policy.v1`, loader-auto discovery under `core/eval/evaluators`).

A CR sim runs externally and emits per-engine result JSONs. A pack consumes them as `lev.sim_eval.provider_evidence.v1` records on `sim.julia` / `sim.jax` lanes (`non_authoritative_input`), computes cross-engine `max_abs_diff` over a declared shared observable, and a deterministic `gate-policy.yaml` decides pass/block on tolerance. Sims measure; the policy decides; no LLM in the gate path. It uses the existing sim-eval provider seam — no new proof mechanism.

- `cr_cross_engine_parity` — float fingerprint sim (`probe_quotient_fingerprint_floor_v1`), integer `quotient_class_count_full=5` agreeing across julia+jax, tol 0.
- `cr_scc_quotient_parity` — a different invariant class: integer combinatorial invariants (`scc_count`, `quotient_class_count`=41, both maps) agreeing across the sim's independent julia+jax graph algorithms, tol 0.

## Load-bearing, not decorative
- The sensor recomputes the real `@lev-os/sim-eval` FNV-1a-32 `content_address` and blocks on mismatch — as strict as the real producer's `validateProviderEvidence` (an earlier version only checked the prefix; that false-green hole is closed). Verified it reproduces the real address `sim-eval:fnv1a32:1840d25c`.
- The sensor recursively rejects any evidence carrying `verdict`/`gate_proof`/`effect_receipt` (sims can't mint truth), and blocks on missing lane / missing observable / malformed record / disagreement beyond tolerance / wrong content_address.
- Each pack has 4 cases: pass, adversarial false-green (perturb one engine → block), missing-lane (→ block), bad-address (wrong content_address → block). The bad-address gate is proven load-bearing by mutation test (neutralize the hash check → bad-address flips block→pass).

## Verification (local, fresh worktree on origin/main)
- Built the eval dep graph (logger/uri/utils/domain/config/eval) — needed because vitest resolves the `import`/dist export condition, not bun/src.
- Both pack tests pass; `pnpm typecheck` (core/eval) clean.
- Full core/eval suite: 150/151. The 1 failure (`s2-precut-certify-characterization`) is a pre-existing main test about legacy truth-vocabulary deletion, unrelated to these additive packs.
- All fixtures are built from the sims' actual on-disk engine outputs (values verified against source), and their content addresses are the real recomputed FNV hashes (a wrong one blocks).

## Honest framing of the gate
The real gate here is the vitest suite (`cr-*-parity.test.ts`), which invokes the sensor. `lev eval` run on the `.eval.js` suites is a projection/path check — `evaluateTraceCases` does path-equality on the fixture and existence-checks the sensor; it does not execute `score()`. This matches how the reference pack behaves. So: keep the vitest as CI gate; do not read a `lev eval` green here as a parity result.

## Alignment (per a fresh-context scout of live main + design docs)
On the blessed, just-hardened seam (`evaluator-pack-loader` config-resolvable roots, hardened 2026-07-01 17:38; `core/eval/evaluators` is the first default root). Sensor-measures / policy-decides matches spec-eval + spec-semantic-control. No feature branch changes the provider-evidence, loader, or pack-manifest contract. Does not emit graph patches or the spec-ahead `EvalDecision` type; stays on the measurement side of admission. The `flows/measure.flow.yaml` entrypoint is real, so a later FlowMind-IR cutover is a no-op.

## Next candidates (foundations-first, not in this patch)
- `cr_ordered_channel_parity` — float operator trace-norm noncommutation, four independent routes agree to 2.78e-16 (fence out the by-construction `lindblad_vs_te...=gamma` field).
- `cr_constraint_battery` — a new "constraint" evaluator kind for single-engine sims (constraint_core_audit C2-C7), opens the 662 formal scouts + 13 legos. Needs a ~20-line JSON-emitting wrapper on the sim first.

Claim ceiling: passes local rerun (fresh-worktree vitest + typecheck + independent replay + mutation test); not run on shared CI; not canonical.
