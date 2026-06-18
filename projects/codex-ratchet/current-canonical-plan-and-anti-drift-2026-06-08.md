---
title: Current Canonical Plan + Anti-Drift Machinery (2026-06-08)
created: 2026-06-08
updated: 2026-06-08
type: plan
status: current-source-of-truth
claim_ceiling: plan doc. Everything built so far is scratch_diagnostic; no manifold/M(C)/bridge/Axis0/physics admission.
---

# THE PLAN (repo-gated routing aid — read this first each session)

This is the current dated routing aid for the project, subordinate to the active repo authority docs, validators, and result receipts. If older docs/registries/memory disagree with the current receipts and repo gates, the current receipts and gates win. Old docs (17_actual_lego_registry, MIGRATION_REGISTRY, docs/01-11, old lego sims) are a MINE for math objects, NOT the execution roadmap.

**OLD SIMS = FUEL, not waste (owner, 2026-06-08).** The ~389 torch formal-scouts, the 14 legos, and the system_v4 legacy corpus were "not run right" (thin tooling, single-engine, pre-canon) — but they hold REAL MATH OBJECTS (axis/operator sims, geometry/Weyl/chirality, QIT-engine, basin proofs, nonassoc/division-algebra). They are GOOD FUEL: mine the math object out, REBUILD it on the new 4-layer canon stack (Julia-canon table + JAX/PyTorch consumers + proof ladder + tool_calls receipts) through the normal execution loop + gates. They are NOT the active plan and carry NO status — a reprocessed object earns status fresh. This is a MINING LANE feeding Stages 3-6, not a stage itself.

## The object
Finite SPINOR NETWORKS with finite NONCOMMUTATION + NONASSOCIATIVITY + ATTRACTOR BASINS + Z3-style proofs. Constraint-admissibility, not state mechanics. Root: a=a iff a~b.

## The architecture (canon — GPT Pro spec, owner-endorsed)
- **Julia = CANON.** Owns algebra tables (structure constants C[k,i,j]), bracket order, topology, basin labels, proof obligations, result arbitration. Least numpy-corrupted -> closest to truth.
- **JAX = batched differentiable dynamics** (diffrax/dynamiqs/netket/quimb) — consumes the canon table.
- **PyTorch = first-class compute + THE graph/network engine** + much of the existing machinery (389 scouts + 10/14 legos are torch). The spinor NETWORK is a graph -> PyG (torch_geometric) MessagePassing does the noncommutative/nonassociative octonion edge updates. Richly tooled: PyG + torchdiffeq/torchode + xitorch + geomstats + clifford/torch_ga + e3nn + z3/cvc5. "Weighted least" applies ONLY to arbitration (most numpy-corrupted -> doesn't arbitrate; Julia arbitrates), NOT to importance/workload.
- **Layer 4 = WORLD ENGINE.** Where the validated constraint-admissibility geometry becomes a RUNNING, learned/generative world (end goal: "one world engine where classical runs inside nonclassical"). Repos in /Users/joshuaeisenhart/GitHub: le-wm (JEPA), lpwm, flowm, AnyFlow (world models) + Sana/stylegan3 (generative). INTEGRATION TARGET — fenced like bridge/physics; foundation Stages 1-6 gate it. (Sim-engine LIBRARIES live in depots ~/.julia + codex python env, NOT cloned/in-repo.)
- **Proof tiered by type:** Z3/cvc5 = finite/discrete/logical; interval/Taylor/reachability + auto_LiRPA (Verified-Intelligence, in /Users/joshuaeisenhart/GitHub) = continuous certified bounds; SOS/JuMP = Lyapunov/region-of-attraction; final acceptance = Julia manifest. Optimizers (Optax/xitorch/cvxpylayers) = candidate/counterexample search ONLY, never proof.
- **Exchange:** DLPack zero-copy, NO numpy/.numpy()/np.asarray/CSV/pickle on the claim path. Intra-process DLPack; multi-process MPI/mpi4jax/torch.distributed.

## Stages (ordered; do not skip; each gated before the next)
0. **Tool foundation** — full stack installed + verified; poorly-supported pkgs replaced; repo-pinned Julia project. STATUS: DONE (verified-tool-stack memory; canon project repo-pinned).
1. **Canon algebra artifact** — Julia owns octonion/quaternion structure constants, Z3-proven (nonassoc SAT / assoc UNSAT / alternative+flexible UNSAT). STATUS: DONE + verified (mine + codex app).
2. **Cross-framework consumer gate** — JAX+PyTorch consume the same table, compute the same associator (max_div 0.0), re-association control flips, proofs on all 3 legs, function-level tool_calls receipts. STATUS: DONE + verified.
3. **M(C) scratch foundation** — `M(C) v0` exists as a valid three-engine `scratch_diagnostic` envelope, and separate scratch envelopes exist for the nonassoc root-vs-carrier discriminator and spinor holonomy. Full/admitted `M(C)` remains open until composition/bracketing/readout/receipt fields are explicitly wired into one admitted finite object and pass the relevant gates. Do not rebuild the landed packets by default; verify/adjudicate named gaps.
4. **Same-carrier geometry micro-legos** — spinor-lift / Hopf / Weyl / Clifford / holonomy on the canon carrier, bounded by one object/claim and function-level tool receipts. The octonion / `Cl(6)` / `G2` / Fano / `Spin(7)` / sedenion tower is part of this early carrier-geometry frontier, not a late bracketing footnote: `G2` is likely, but its variants remain open until bounded controls exclude them. Some scratch versions already exist; next work should harden a named gap or build a genuinely new same-carrier micro-lego.
5. **Attractor-basin layer** — Attractors.jl (Julia) + diffrax-vmap (JAX) basin maps of constraint dynamics. Target: test `C=>Basin` under the basin-manifold contract; no basin admission until finite state space, update rule, boundary, invariant, escape cases, killed simpler explanation, and receipts pass. Continuous claims require interval/reachability certificates, not just Z3.
6. **Cross-model readout matrix** — one carrier read by QIT/IGT/Holodeck/physics lenses. `v1` exists as `scratch_diagnostic`; harden/adjudicate named gaps rather than rebuilding `v0` from nothing.
7. **Couplings / coexistence / emergence** — BLOCKED until 3-6 done for the families involved.
8. **Bridge / Axis0 / physics / cosmology** — BLOCKED until 1-7. Gödel/horizon metric = math-only donor, fenced.

CURRENT FRONTIER = harden/adjudicate the already-built scratch foundation envelopes without promotion, then choose the next bounded Stage-4 same-carrier geometry micro-lego or harden the cross-model readout matrix. Everything remains gated and no full/admitted `M(C)`, bridge, Axis0, physics, or manifold claim is admitted.

New source-intake note: [[projects/codex-ratchet/cs-geometry-upgrade-bundle-intake-2026-06-09]] adds a useful discrete-math / CS-layer scaffold between finite carrier and downstream readouts: graph/hypergraph/rewrite representation -> event/multiway graph -> topology/quotient/basin readouts -> GNN/AI only after the graph object is explicit. Treat it as source/design pressure and a micro-probe queue, not repo authority. Before adoption, translate leftover Lev identifiers and repair/replace its Julia support probe.

## How each step gets done (the execution loop)
1. Claude writes a BOUNDED build card (one object / one claim / one set of controls / the tool->role map / the ceiling). NOT a giant fullstack build.
2. **codex1** (gpt-5.5 xhigh, ~/.codex) BUILDS via STDIN-redirect — run MASS-PARALLEL across effort levels; Claude never builds science. **codex2 (~/.codex-second) is HISTORICAL / memory-only (auth revoked 2026-06-17) — do NOT dispatch builds to it; treat it as a memory-ingest source.** [2026-06-17: this UN-INVERTS the prior off-limits rule; the codex1-vs-codex2 split was quota-era routing, not doctrine.]
3. Claude VERIFIES on disk (validator --require-pytorch, values, tool_calls real, no-numpy-path, controls flip) — builder's verdict is NOT evidence.
4. **Fresh-context audit** on any LOAD-BEARING receipt — a SEPARATE fresh read-only codex1 invocation (CODEX_HOME=~/.codex, did NOT build that artifact) + Claude fresh-audit-runner + multi-model fleet alt-views (grok/gemini/deepseek/qwen/kimi via OpenRouter). [2026-06-17: codex2 is no longer a live audit worker.]
5. Gate. If it passes -> next stage. If not -> re-harden THAT piece (not a rebuild of everything).
6. Save the receipt to the wiki. Update memory.

## ANTI-DRIFT MACHINERY (the part that matters)
Drift happened from: no repo-gated routing aid, two checkout memories, old docs treated as plan, giant relaunched builds, thin tooling, over-narration. Counters:
1. **One read-first routing aid = THIS doc, subordinate to repo gates.** Start every session here after repo authority, not from old registries or one-checkout memory. Linked from read-first.md.
2. **Stage gate, hard.** Current frontier is named by current receipts and gates. No work past the frontier without the prior gate shown PASS. No "some strong locals" exception.
3. **Canon-rule gates on every receipt** (mechanical, not vibes): function-level tool_calls present; no numpy on claim path; bracket order preserved + no hidden re-association; proof tiered (no optimizer-as-proof); repo-pinned; cross-framework algebra test passes; classification honest. A receipt that fails any is not promoted.
4. **The three gate skills are now wired** (Codex app shakedown, 2026-06-08): `codex-ratchet-env-agent-coordination` (runtime/install truth), `codex-ratchet-tool-status-auditor` (function-level tool receipts), and `lego-sim-classifier` (real status and claim ceiling). Treat these as mandatory in-loop guards before package work, tool-integration claims, or sim classification. Current Codex audit receipt: `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/tooling/codex_runtime_capability_shakedown_results.json` (`classification=audit`, `all_pass=true`, `promotion_allowed=false`).
5. **Fresh-context audit for load-bearing claims.** A builder's verdict on its own work is never evidence.
6. **Status ladder, never collapsed:** exists < runs < passes-local-rerun < canonical-by-process. Everything now is scratch_diagnostic. Don't imply higher.
7. **Bounded builds only.** One object per build card. If a build needs >1 object, split it. The "giant fullstack" pattern is banned — it produces thin or decorative work.
8. **Don't relaunch the same thing.** If a receipt has a named gap, harden THAT; finish + verify one before starting the next.

Source tags: `reference_gpt_pro_canonical_tristack_architecture`, `reference_verified_tool_stack_and_poorly_supported_alts`, `feedback_new_stack_is_plan_old_docs_are_mine`, `reference_tri_engine_parallel_share_julia_canon_numpy_corruption`.

---

## 2026-06-17 UPDATE (tooling + method + state — supersedes any conflicting line above)

**Tooling / routing (the "how"):**
- **codex1 (`~/.codex`, gpt-5.5 xhigh) is the LIVE build worker.** codex2 (`~/.codex-second`) is HISTORICAL / memory-only (token revoked). This un-inverts the old "codex1 off-limits / codex2 builds" rule — that split was quota-era routing, not doctrine.
- **cocoindex** is the semantic retrieval layer (a map, NOT authority): wiki via MCP `mcp__cocoindex_wiki__search` with `refresh_index=false` (the default `true` collides with the background indexer and drops the connection); repo via `ccc search` run from `~/Codex-Ratchet`.
- **Full multi-model fleet** live via OpenRouter (`$OPENROUTER_API_KEY` in-shell; direct `XAI`/`GROK`/`GEMINI` keys in `~/.zshrc`): deepseek, qwen, kimi, grok, gemini. Use it for **divergence** (raise the chance something useful survives), not only adversarial close.
- Repo authority is **Wizard v4.3**.

**Method (the deeper "how"):**
- The gate splits in two: (a) a **narrow deterministic SEAT-CERTIFIER** — did the artifact actually run / real evidence vs. stub (python/validator/binary; strict); (b) a **soft multi-model JUDGMENT** — what to explore / rescue ordering / interpretation choice (NOT strict, NOT perfect; many models, statistical). Do NOT make the soft part a strict policy.
- Dominant failure mode (owner): LLMs lock onto ONE often-unstated interpretation, harden it into rules, and burn huge effort. Counter = keep readings **plural**; fleet for divergence.
- The **engine-run-authenticity re-executor** (re-run the `.jl`/`.py`, recompute the claimed values, sign a run receipt) is the missing seat-certifier slice — designed (`project_deterministic_harness_design`), NOT built. Current validators check declared shape + source tokens, not execution.

**State (where we are, 2026-06-17):**
- `entropy_geometry_coratchet_floor_v0` fleet-gated (Claude+DeepSeek+Grok) → defects fixed → re-gated clean: **geometry/distinguishability is the spine; entropy is a TYPED downstream readout recomputed per carve — NOT a co-equal dual ratchet.** Still scratch_diagnostic.
- **system_v3** (the original deterministic system + rescue/graveyard/lawyer machinery) is RECOVERABLE from commit `ecee5ea8a` (untracked+gitignored 2026-06-09, not lost). Do NOT wholesale-restore; extract + ledger first.
- Agent memory → wiki is **SCAFFOLDED, not done**: router + research tranche exist, the provenance ledger does not; `wiki/codex-memory/` is empty; codex1/codex2/.claude memory largely unprocessed (coverage audit 2026-06-17).
- "Purgatory" rename is NOT propagated into code (still `graveyard` + `graveyard-lawyer` + `op_graveyard_rescue` in `system_v4`).

Claude-memory cross-refs: `feedback_codex2_is_the_build_workhorse` (codex1-live correction), `feedback_gate_narrow_seatcertifier_judgment_soft_multimodel`, `project_geometry_entropy_coratchet_not_dual`, `project_deterministic_harness_design`, `reference_cocoindex_wiki_semantic_search`.
