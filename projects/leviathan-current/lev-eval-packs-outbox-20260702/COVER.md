# Lev Eval Packs Outbox 2026-07-02

Base: current origin/main `35d11965f`.

Patches:
1. `feat(eval): cr_ordered_channel_parity evaluator pack` - adds the ordered-channel witness pack under `plugins/sim-eval/evals` and its plugin test.
2. `feat(eval): first sim->eval->world-model->graph seam receipt` - adds the replay test and receipt artifacts beside upstream `cr_cross_engine_parity`.
3. `feat(eval): cr_qit_bridge_stream_v0 QIT bridge witness pack` - adds the core QIT stream adapter/export plus plugin-owned QIT witness pack.
4. `fix(eval): make seam receipts replay on current checkout` - refreshes receipts and makes QIT fixture refs project-relative for checkout-root-stable replay.

Verified on fresh current-main throwaway clone after hydrating workspace deps and building minimal package entries:
- `pnpm --dir plugins/sim-eval test` -> 8 files, 71 tests passed.
- `pnpm --dir core/eval exec vitest run src/cr-qit-bridge-stream-v0.test.ts src/world-engine-seam-receipt.test.ts` -> 2 files, 8 tests passed.
- `pnpm --dir core/eval typecheck` -> passed.
- `pnpm --dir plugins/sim-eval typecheck` -> passed.

Ceilings:
- Passes local rerun and fresh-main throwaway apply/test.
- Not CI.
- `cr_constraint_battery` branch delta is intentionally omitted: current `origin/main` already owns that pack, and replaying the branch delta breaks upstream `cr-scout-lego-adapter.test.ts` pass expectation.

Deterministic code changes:
- New core QIT parser/address helper and exported lane typing for `sim.qit`.
- New/updated Vitest replay tests and deterministic sensors/fixtures under plugin-owned packs.

DNA/FlowMind/YAML/.lev changes:
- Evaluator pack manifests, measure flows, gate policies, and routing policies live under `plugins/sim-eval/evals/*`.
- No `.lev` task state changes.

Code vs LLM boundary:
- Code handles parsing, content addressing, score decisions, discharge checks, world-model projection, graph write/readback, and regression assertions.
- LLM only handled patch selection/cover summarization; no runtime truth is delegated to LLM output.
