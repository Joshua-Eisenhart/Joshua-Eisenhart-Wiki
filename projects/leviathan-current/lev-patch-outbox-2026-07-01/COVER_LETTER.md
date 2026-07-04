# Patch series: WaveRun engine gates + CR sim integration

To: lev dev (lev-os/leviathan maintainer)
From: Josh (branch work by Codex gpt-5.5 + Claude, verified locally)
Date: 2026-07-01
Branch: `patch/waverun-engine-gates-20260630` (31 commits on top of `origin/main` at `02e520e3d927`)

## How to apply

Preferred — fetch the bundle (preserves exact hashes):

```
git fetch /path/to/waverun-engine-gates-20260630.bundle patch/waverun-engine-gates-20260630:patch/waverun-engine-gates-20260630
```

Alternative — apply the mailbox series in `patches/` (01…31) with `git am`.

Prerequisite commit `02e520e3d927` must exist in your clone (it is on `origin/main`).

## What the branch contains (31 commits, three arcs)

1. **Trust spine closure.** Blocker A (forged obligation sourceHashes) closed; Blocker A-prime (wizard runner accepted forged self-consistent engine digests) closed, plus residuals: fixture engine authority is symbol-keyed test-only, and every real engine substrate digest now carries runId/nonce/issuedAt with single-use host-built authority. Persisted host-scoped trust secret for the two chain-crossing ledgers (host-trust incl wave-run-consume; host-graph-event-trust) with persisted anti-replay. Host-witness and graph-apply authority intentionally stay per-process (in-process attestations).
2. **Recursive WaveRun loop + real engines.** `lev orchestration lev-wizard-ratchet loop --waves N --real-engines --real-skills --real-source-evidence` runs a bounded multi-wave loop: real Julia/JAX/PyTorch subprocess spawns through the mechanical probe runner, ClaimGate gates, graph-applies survivors via the explicit host apply chain, emits and chains the next-run seed. Live-verified 2026-07-01: 1/1 waves, steering `host_consumed`, `graphMutationApplied: true`, seed graph-applied.
3. **Codex Ratchet sims as Lev workloads.** Two pilot obligation kinds (`cr_fingerprint_floor_v1`, `cr_coratchet_floor_v0`) run CR sims from host-owned, source-hash-pinned carriers with executed negative controls under a new `julia_jax_required` engine mode; both pass live with accepted claims and fenced graph proposals. Plus: skill loader honors declared `execution_profile` frontmatter; suspect-evidence warnings on failed steering projections; A22 red-team test isolation.

CI added: `.github/workflows/claimgate-proof-suite.yml` — mandatory cheap backstop on every push touching core/orchestration or core/graph. Note it runs core/graph with `bun test` (its declared runner, 393 tests); running graph under vitest finds only ~83 and would report a misleading green. `.github/workflows/real-engines.yml` — opt-in (workflow_dispatch + weekly cron) heavy job that spawns the real engines; locally dry-run verified, never yet run on a GitHub runner.

## Verification status (honest labels)

- `core/orchestration`: 821/821 (vitest), typecheck clean — local rerun 2026-07-01.
- `core/graph`: 393/393 (`bun test`, 44 files) — local rerun 2026-07-01.
- Live end-to-end loop and both CR pilots: verified by direct receipt reads, this session.
- Everything is **passes local rerun**, not canonical: none of it has run on shared CI. First push of this branch should trigger the claimgate-proof-suite workflow; please also `workflow_dispatch` real-engines once merged to main and expect the Julia `Pkg.instantiate` of a heavy manifest (ITensors/Yao/Z3) to be the risky step.

## Known open items (not blockers to applying)

- `host_blocked` on pass/pass steering projections is correct but carries no per-run discrimination beyond gate names (accepted design: external evidence enters only via host-executed engine obligations).
- Wizard council/model-lane content remains fixture-typed by construction until live model-lane receipts exist (`--run-model-lanes` is the partial step).
- A generic manifest-driven CR-sim obligation kind (replacing per-sim TS carrier builders) is in progress on our side and will come as a follow-up series.

## Contact

Receipts and the full systems layout live in `~/wiki/projects/leviathan-current/` (`lev-systems-layout-and-plan-2026-07-01.md`, `lev-waverun-work-plan-and-status-2026-07-01.md`) on Josh's machine; ask and we'll export them.
