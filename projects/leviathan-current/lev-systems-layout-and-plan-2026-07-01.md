---
title: Lev + patch + CR integration — systems layout and plan (line-itemed)
created: 2026-07-01
branch: patch/waverun-engine-gates-20260630
type: systems-map-and-plan
status: current
claim_ceiling: passes local rerun for all committed items; live-verified where stated; nothing canonical-by-process
---

# Lev + patch + CR integration — systems layout and plan

Grounded in live runs this session (recursive loop, daemon fleet, engine census) plus the SYSTEM_INVENTORY receipt. Status labels are exact. Nothing here is canonical.

## Live proof this session (2026-07-01)
- `lev orchestration lev-wizard-ratchet loop --waves 1 --real-engines --real-skills --real-source-evidence` → status completed, 1/1 waves, 0 findings, steeringStatus host_consumed, graphMutationApplied true (graphEventId ge-1782940481911-l54yjh), nextRunSeed emitted + graph-applied, threeEngineValidation ok (envelope sha256:945fc834…). claimCeiling still fixture_or_dry_run_until_live_model_and_engine_receipts; modelLaneRuntime.ran=false (flag not passed).
- Daemon fleet brought up: postgresql:5432, redis:6379, patterns:8082, leann-grpc:50052, nextjs:3000 all running. `daemon start --all` only starts brew services; stale pmdaemon regs need `restart` (ops bug).
- Engine census: python sim-stack 20/20 import clean (jax 0.10.1, torch 2.11.0, sympy 1.14.0, z3, cvc5 1.3.3, quimb 1.14.0, geomstats 2.8.0, clifford 1.5.1, opt_einsum, toponetx, torch_geometric 2.7.0, numba, scipy, networkx, e3nn, pennylane, cirq, qutip). Julia carrier 24 pkgs, heavy loads pass (Z3, Yao, ITensors, QuantumClifford, Grassmann, Symbolics). Runtime doctor ok=True stable_observed.

## Commits landed this session (branch patch/waverun-engine-gates-20260630, local only — no push access for Joshua-Eisenhart on lev-os/leviathan)
- ad4edbafb feat(claim-gate): CR sims as host-owned engine obligations (pilots A/B + requiredLanes default-from-engineMode fix)
- 1bf548879 test(claim-gate): host-witness consume semantics + A22 redteam ledger isolation
- 533ce1e00 fix(graph): honor declared execution_profile frontmatter in skill source pack runner
- c8b8984a1 ci: opt-in real-engines workflow + preflight
- b5b62df55 ci: mandatory cheap ClaimGate proof-suite backstop (orchestration=vitest, graph=bun test)

## A. Lev runtime spine
- core/orchestration — proof/gate machinery; 820/820, typecheck 0. Status: passes local rerun. TODO: none blocking.
- core/graph — entity graph + append-only JSONL events + probe runner + projection-binding; bun test 393/44. Status: passes local rerun. TODO: none blocking (CI now runs it).
- core/event-bus / core/exec / core/domain / core/event-machines / core/event-providers — suites pass. Status: passes local rerun. TODO: none.
- core/daemon — 235 tests pass, 12 skipped. TODO: examine skips; commit cli-lifecycle.ts.
- core/poly (lev CLI) — live; ~29 gates.test.ts fails reference missing plugins/sdlc/*. TODO: restore or retire stale gate tests.
- core/harness — repair dispatch + providers; 4 cdo-triple50 fails at last inventory. TODO: re-verify on current branch.
- core/flowmind — YAML→exec compiler; 6 fails from one missing dna-gitagent-parity fixture. TODO: restore fixture.
- core/lifecycle, core/memory session-state-projection — pass but zero live consumers. TODO: wire or mark scaffolding.

## B. Trust spine (hardened)
- Host-trust + wave-run-consume ledger — cross-process persisted XDG secret, persisted anti-replay. DONE (bfc36727a upstream + wiring).
- Host-graph-event-trust ledger — same fix, persisted spent-ledger. DONE.
- Host-witness ledger — per-process BY DESIGN (cross-process witness = replay). DONE, do not change.
- Graph-apply authority — per-process single-spend not_transferable BY DESIGN. DONE, do not harden cross-process.
- Blocker A closed 50d2e64f3; A-prime closed 408267f51 + residuals 92f6535eb / e83974175. All live-repro verified.
- TODO: durable red-team suite for the closed legs (forged digest, stale source hash, external injection, serialized digest replay).

## C. Engine substrate (CR sim engines inside Lev)
- Three-engine envelope (Julia canon / JAX workhorse / PyTorch graph) — real spawns proven repeatedly; sealed receipts, executed negative controls. Status: passes local rerun / live-verified.
- Carriers: r0-quotient, graph-substrate, cr-fingerprint-floor-v1, cr-coratchet-floor-v0 — present, source-hash-pinned; CR two committed. Status: passes local rerun.
- TODO: real-engine CI committed but UNVERIFIED on a GitHub runner (julia manifest instantiate + linux wheels). Mandatory cheap job now exists (b5b62df55).

## D. WaveRun / Wizard ratchet loop
- Recursive loop live-verified (gates → graph apply → next seed, all fenced promotionAllowed:false at runtime).
- Ceiling: council/model-lane CONTENT still fixture-typed by construction; model lanes did not run in the verified wave.
- TODO: fixed-point/progress law (halt when a wave adds no new admitted state); live model-lane receipts to lift the fixture ceiling; council member profiles as executable schemas.

## E. Steering produce/consume boundary (shallow wrap)
- Fail-closed for all external evidence — verified across 10 sims + forged/stale attacks. host_consumed unreachable via shallow wrap; deep host-executed obligations are the ingestion route.
- Two verified seams (non-blocking, fail-closed): (1) fail lane accepts fabricated evidence refs silently; (2) host_blocked indiscriminate (identical findings honest vs forged). PATCH IN FLIGHT (codex1, message/finding-signal only, no status change).

## F. Skills / memory / model lanes
- Skill loader — declared execution_profile frontmatter now wins (533ce1e00). Remaining: ~249 skills mostly don't declare it. TODO: declare frontmatter across estate or build real derivation.
- Spinor memory cell — proposal-only, promotion structurally impossible by design.
- Autoresearch LLM provider — hardcodes Anthropic defaults. TODO: env-configurable (fix exists uncommitted).

## G. Daemon fleet / services
- Running: postgresql, redis, patterns, leann-grpc, nextjs.
- Missing binaries (verified absent at registry paths AND on PATH, 2026-07-01): ast-grep (`~/.cargo/bin/sg`, structural AST search — installable via `cargo install ast-grep` or brew + symlink), bd (`~/.local/bin/bd`, Beads issue tracker), ck (`~/.cargo/bin/ck`, semantic code search), frankensearch (`~/.cargo/bin/frankensearch`, experimental hybrid retrieval), leann (`~/.local/bin/leann`, vector doc search CLI — its gRPC daemon IS running), qmd (`~/.bun/bin/qmd`, local-embeddings search). All are retrieval sidecars, none gate the sim/engine/ClaimGate pipeline. TODO: owner names install sources (or disables in core/poly/registry.yaml) — installing same-named lookalikes blind is the wrong risk.
- Legacy/unknown: deer-flow, old-dash, presence, sofia-api, sofia-web. TODO: owner decision retire/revive.
- Graph persistence: JSONL append-only + in-memory; neo4j configured-unused (deliberate).
- TODO: `daemon start --all` stale-pmdaemon fallback (should restart, not error).

## H. CR integration
- Deep path: cr_fingerprint_floor_v1 + cr_coratchet_floor_v0 pass as host-executed obligations (committed, receipts verified). THE ingestion route.
- 10 pilot sims all at passes local rerun (correct lego validator 8/8; ceiling promotion_allowed=false).
- CR runner path fix — in flight in a separate owner session (task chip task_cb286c41).
- Correct validators: legos→validate_lego_results.py; formal scouts→validate_formal_scout_results.py; v7 three-engine→validate_three_engine_sim_result.py. lint_sim_contract.py is v4-probes-scoped (do NOT use on legos).

## I. Sim tools & libraries — all usable (verified this session)
- See §Live proof / engine census above. Everything imports and loads; no missing/broken libs in the sim-stack env or julia carrier project.

## Plan (order — trust before features)
1. (in flight, owner session) CR runner path fix — codex_sim_runner.py:981 results/ subdir.
2. CI backstop: local half DONE (b5b62df55). REMAINING: push access + verify claimgate-proof-suite + real-engines.yml on an actual GitHub runner. BLOCKED on push perms (Joshua-Eisenhart lacks write on lev-os/leviathan; no SSH key). Owner action.
3. Durable red-team suite for the closed forgery legs.
4. (in flight, codex1) Two consume-lane seam patches — message/finding signal only.
5. Pilot C — DECIDED 2026-07-01 (foundations-first, owner: "just decide yourself, system prefers foundations first"): **Rung 0.5 = finite_ring_checkerboard_support_three_presentation_consistency_v0** (the literal next row per system_v6/foundations/mss_and_rung_climb_foundations_DRAFT_20260615.md:88-93). Rung 1-2 (survivor_set_running_mean_threshold_noncommutation_v0) is the successor after 0.5. Onboard onto the generic cr_sim_packet_v0 path once committed. GAP: the sim has exact.py (python-stdlib oracle) + jax.py but NO julia leg — Pilot C build must add a Julia leg reproducing the finite INTEGER agreement tables (exact equality, not 1e-10 — observables are support counts/adjacency components/quotient classes, floats are readout-only). Negative control: reuse one of its 5 existing breaking controls (fiber_coordinate_erasure_merges_classes or shell_nesting_erasure_merges_classes). Carrier = new host-owned dir under core/orchestration/src/probes/lev-sim-engine-carrier/, packet.json per the generic schema.
6. Corpus runner — batch the lego registry through the pilot pattern once runner fix lands (codex1 fleet, bounded).
7. Fixed-point/progress law → council profiles + live model lanes (lifts fixture ceiling) → new obligation kinds one at a time with negative controls.
8. Ops cleanup — daemon stale-reg fallback, missing tool binaries, legacy services, skill-frontmatter declarations.

## Owner-blocked items (cannot resolve with tools)
- Push access to lev-os/leviathan (item 2 GitHub verification).
- Pilot C science: the next rung above the co-ratchet floor.
- Retire/revive decision on legacy daemons (deer-flow, sofia-*, presence, old-dash).
