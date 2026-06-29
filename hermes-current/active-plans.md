# Active Plans

Purpose: hold active implementation/planning lanes in a compact form that survives across threads.

Status: active current working-memory note.

Use this when:
- handing work between agents or threads
- deciding the next concrete move
- checking whether a planning surface already exists

Current plan stack:
1. Build and refine a small `hermes-current/` wiki spine.
2. Migrate durable facts from `hermes-memory-offload.md` into more stable current notes.
3. Keep injected memory as compact pointers into the wiki rather than as long-form doctrine storage.
4. Maintain project-specific read-first notes under `projects/` as needed; `projects/codex-ratchet/read-first.md` now exists.
5. Build or patch skills so they read the wiki spine first for substantive work.
6. Keep concept-level harness/controller doctrine as a second-layer load after `hermes-current/`, not as a competing front door.
7. Later, inspect external skill/evolution repos for patterns that help improve the wiki+skill system.
8. Stress-test the Hermes subagent/output surface so routing stays adaptive across Claude, Codex, and Gemini without collapsing plurality or looping on broken launchers.
9. Preserve the 2026-06-28 Lev/ClaimGate handoff through [[fresh-thread-continuity-2026-06-28]] and [[projects/leviathan-current/lev-claimgate-digging-status-2026-06-28]]; current verified fork: notary receipt should use the GKSL PSD flip, while legacy guard needs the owner decision on whether `@lev-os/daemon` / `@lev-os/sdlc` are deprecated. Latest Codex-pasted build moved ClaimGate source-bound evidence context into host/run options and the focused orchestration rerun passed, but Hermes reruns still find the harness session-runner slice red (`20 passed / 2 failed`) on SDLC schema path resolution despite Codex reporting `22 pass`. Do not promote the harness slice without fixing the visible worktree or preserving Codex's exact passing command/environment. Do not resume broad/mass OpenRouter calls or any `gpt-3.5-turbo` route without explicit owner authorization.
10. Keep ongoing wiki maintenance alive through [[wiki-continuous-maintenance-control-2026-06-28]] and cron job `a2e9088a081e`: every tick must be one bounded probe → patch/deepen → log → final-probe tranche, with no broad model swarm and no unverified promotion.

Open planning rules:
- Prefer one authoritative note per concern over repeated summaries.
- Only a few notes should act as integrators; most notes should stay local and simple.
- Updating a local fact should usually require only a local edit, not a wiki-wide cascade.
- Skills should enforce read order and maintenance discipline, not create unnecessary prose sprawl.

Wizard/system maintenance queue:
- Current model: Wizard is a composable controller over standalone skills, agents, model-pressure routes, and tools; components can run alone or as part of Wizard when composition changes the result.
- Breadth: `full` attempts all admitted relevant routes for the declared scope; `auto` selects only routes likely to change the answer. Decision-relevant skipped routes must be marked `not_run` or `deferred` with a reason.
- Loop: Wizard may generate next prompts/packets, pre-run scouts/audits, auto-run safe admitted generated packets, and continue until success, finite cap, no delta, repeated blocker, probe/route-truth failure, or drift from the user's goal.
- Maintenance discipline: run bounded tranches only: inventory -> patch one cluster -> verify -> log -> queue next tranche. No whole-corpus rewrite in one run.
- Routing: codex2 is preferred for heavy reading/patching; Hermes verifies and edits; Grok/Gemini/Sonnet are contrast/pressure routes where useful; conserve Opus.
- Prompt-size guard: keep global `HERMES.md` and `SOUL.md` lean; procedures and long rationale live in skills and wiki notes.
- Operational note: check Hermes CLI through the login shell path, e.g. `zsh -lc 'hermes --version'`; docs extraction may be blocked without Firecrawl config and should be recorded as a blocked route, not central doctrine.
- Closed controller-side after the codex2 tranche: the global `~/.hermes/HERMES.md` high-salience rail now carries the compact full/auto breadth rule. codex2 could not write outside `/Users/joshuaeisenhart/wiki`, so Hermes applied and verified the profile-side patch directly.
- Hermes-native controller system v0 now exists at `hermes-current/controller-system/README.md` with runnable harness `hermes_controller_harness.py`; current checked status is `passes local rerun` for built-in selftest and `pass_with_blockers` for the first scenario receipt, not canonical/default runtime. Receipts: `hermes-current/controller-system/receipts/selftest-2026-06-18.json` and `hermes-current/controller-system/receipts/hermes-native-controller-v0-build-test-2026-06-18.json`.

Near-term concrete targets:
- keep `hermes-current/read-first.md` as the Hermes front door
- keep `hermes-current/about-me-and-how-to-work-with-me.md` as the identity surface
- keep `hermes-current/active-intentions.md` and this note as the cross-thread continuity surface
- use `hermes-current/fresh-thread-continuity-2026-06-28.md` as the restart/capture note for the overwhelmed Hermes thread `20260628_004303_aa3f2b`: Lev blockers are preserved there as recovered context, while wiki maintenance continues under bounded probe -> patch -> probe tranches
- keep `hermes-current/hermes-memory-offload.md` as a migration ledger rather than a permanent dump note; use `[[memory-maintenance-2026-06-06-wizard-maintenance-correction]]` as the latest live memory snapshot/compression receipt and `[[memory-maintenance-2026-06-05]]` as the prior baseline receipt
- use `hermes-current/wiki-ingest-queue-and-priorities.md` as the bounded ingest router so repo/wiki deepening stays organized and non-blob-like
- use `hermes-current/wiki-wizard-v4-3-mmm-maintenance-template.md` as the active v4.3 MMM maintenance/on-demand/cron template; it must preload MMM salience before task rules and keep v4.3 object-preservation/maintenance wording while naming the legacy v4.2 provenance bridge explicitly. Historical finite steward job `497a2eaaa178` was created on 2026-06-06, but a 2026-06-13 Hermes `cronjob list` returned `count=0`; do not call it live without a new scheduler creation receipt.
- use `hermes-current/wiki-wizard-v4-2-autoloop-control.md` as the historical/bridge Wizard v4.2 wiki-autoloop control surface under the current v4.3 binding; original job `796b4560f2f5` and finite steward job `497a2eaaa178` are historical, no old schedule should be assumed, and each tick must be one bounded tranche with pre/post `wiki_probe.py`, v4.3 object-preservation preflight when object/proxy drift is in scope, model-family premortems when available, repair gate, and one log entry
- current owner-kernel/Axis0 route: `concepts/entropic-monism-axis0-field-compression-spine.md`, `concepts/cross-field-toe-genealogy.md`, `concepts/field-wide-compression-geometry.md`, and `concepts/entropic-spacetime-monism-readout-map.md`; use this route for entropic monism, JK fuzz, cross-field ToE genealogy, field-wide compression, and spacetime/mass-energy/matter/force readout monism before compressing into physics-first summaries
- current cross-model convergence route: `concepts/model-convergence-qit-engine-full-stack.md`; use it when the user says all models are different perspectives on the same thing, or when `QIT engines` means the proposed geometric constraint manifold plus spinor/Weyl/Hopf/Clifford/division-algebra/branch math and engine grammar, not one narrow runtime slice
- current sim/tool rebuild gate: `projects/codex-ratchet/tri-engine-rich-tool-sim-contract-failure-and-rebuild-2026-06-07.md`; load it and the `codex-ratchet-tri-engine-rich-tool-contract` skill before accepting Julia/JAX/PyTorch sim claims. Bare `jax.numpy` plus Julia `LinearAlgebra`/serialization parity is scratch only until rebuilt with package-native, load-bearing rich tools. Current rebuild intake: `projects/codex-ratchet/foundation-root-distinguishability-and-associator-rebuild-2026-06-07.md` records R0 v2 and R3 associator scratch receipts under no-promotion ceilings; current full R3 carrier-layer status is `projects/codex-ratchet/nonassociativity-carrier-layer-status-2026-06-07.md`.
- current overall execution plan: `projects/codex-ratchet/overall-aligned-execution-plan-2026-06-07.md`; use it to keep wide exploration and strong gates aligned across Holodeck, physics, IGT, QIT-engine, external-theory, and carrier/bracketing lanes. The state-reconciled route is: six current `three_engine_sim_result_v1` envelopes are built `scratch_diagnostic` under no-promotion ceilings and validate with `--require-pytorch` — R4 `M(C) v0`, `nonassoc_root_vs_carrier_discriminator_xhigh`, `spinor_holonomy_path_integral_variant`, plus R5 Hopf, Weyl, and Clifford spinor carrier. `su2_unit_quaternion_hopf_holonomy_order_probe` is separate `FORMAL_SCOUT_RESULT_v1` / `formal_scout`. Full/admitted `M(C)` remains open. Next frontier is cross-model readout matrix v0 or a genuinely new same-carrier geometry micro-lego; do not rebuild the six by default. Use `projects/codex-ratchet/manifold-layers-and-sim-queue-capture-2026-06-08.md` for the current layer/queue capture and stale-map guard.
- treat ingest and promotion questions mainly as entropy/refinement questions rather than hard canon/non-canon splits
- only promote material toward `hermes-current/` or other front-door surfaces after repo-backed evidence, rerun-backed results, or explicit review makes that refinement level honest

Current runtime handoff:
- handoff note: `[[handoffs/hermes-runtime-subagent-handoff-2026-04-20]]`
- fresh-terminal prompt: `[[handoffs/hermes-next-terminal-prompt-2026-04-20]]`
- stress/adaptive-routing plan: `[[hermes-subagent-stress-and-adaptive-routing-plan-2026-04-21]]`
- answer-surface stress rubric: `[[hermes-answer-surface-stress-rubric-2026-04-21]]`
- follow-up collapse hardening note: `[[hermes-follow-up-collapse-hardening-2026-04-21]]`
- default-controller proof plan: `[[hermes-default-controller-proof-plan-2026-04-22]]`
- mass voice/lane tuning plan: `[[hermes-mass-voice-lane-tuning-plan-2026-04-22]]`
- mass spin results: `[[hermes-mass-spin-results-2026-04-22]]`
- Claude transcript transfer + mini-MMM note: `[[hermes-claude-transcript-transfer-and-mini-mmm-2026-04-22]]`
- Hume + 14-role + contradiction bundle: `[[hermes-hume-14role-contradiction-bundle-2026-04-22]]`
- matrix14 compare (Opus/Codex/Sonnet/Gemini): `[[hermes-matrix14-opus-codex-sonnet-gemini-compare-2026-04-22]]`
- Opus-heavy window + hybrid microfix packet: `[[hermes-opus-heavy-window-and-hybrid-microfix-2026-04-22]]`
- validator gate packet: `[[hermes-validator-gate-packet-2026-04-22]]`
- carry-forward from current Claude context: `[[hermes-carry-forward-from-current-claude-context-2026-04-22]]`
- carry-forward from Claude/Codex render+measurement audit: `[[hermes-carry-forward-from-claude-codex-render-and-measurement-audit-2026-04-23]]`
- output voice-audit + format patch packet: `[[hermes-output-voice-audit-and-format-patch-packet-2026-04-23]]`
- format-only owner + screen-shape patch: `[[hermes-format-only-owner-and-screen-shape-patch-2026-04-23]]`
- format-correction process failure and reset: `[[hermes-format-correction-process-failure-and-reset-2026-04-23]]`
- current multi-family compare packet: `[[hermes-current-multi-family-compare-packet-2026-04-23]]`
- Claude Code Opus subagents proof: `[[claude-code-opus-subagents-proof-2026-04-23]]`
- lane + council carry-forward from pasted thread: `[[hermes-lane-council-carry-forward-from-pasted-thread-2026-04-23]]`
- output-format owner-boundary patch: `[[hermes-output-format-owner-boundary-patch-2026-04-23]]`
- Codex-format correction: `[[hermes-codex-format-correction-2026-04-23]]`
- MMM orientation + prompt plan: `[[hermes-mmm-orientation-and-prompt-plan-2026-04-23]]`
- wizard-mode fresh-terminal prompt: `[[handoffs/hermes-next-terminal-prompt-wizard-mode-2026-04-21]]`
- Hermes-native Wizard folder: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/` — current adaptation/proof surface for binding the general Wizard packet to Hermes strengths without copying Codex Max Assembly or dumping packet doctrine into HERMES/SOUL.
- Hermes Wizard v4.3 native loop bridge: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/14_HERMES_WIZARD_V4_2_NATIVE_LOOP_BRIDGE.md` — current bridge for v4.3 loop/autoloop work in Hermes; v4.3 preflight where scoped, v4.2 topology for runtime, with external model pressure, premortem dispositions, wiki alignment receipts, and stop conditions.
- Corrected Codex-local skill stack audit: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/07_CODEX_LOCAL_SKILL_STACK_AUDIT.md` — direct audit of `/Users/joshuaeisenhart/.codex/skills/` after the first pass missed the local Codex skill stack.
- Hermes Wizard run harness: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/08_HERMES_WIZARD_RUN_HARNESS.md` — modes, wave topology, wide intra-council fanout obligations, receipt fields, human-load visual template, and validator for real Hermes-native Wizard attempts.
- Hermes Wizard v4.1 topology correction: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/09_V4_1_LLM_COUNCIL_TOPOLOGY_CORRECTION.md` — records that proper v4.1 means three different LLM councils in sequence with wide parallel work inside each; `runs/20260504-155235` is only `REAL_ATTEMPT_PARTIAL`, not full/proper wide-council conformance.
- Hermes Wizard wide-council fixture: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733/` — option-4 All-C run with Decision 7/7, Failure 6/6, Follow-Up 7/7 parent/member coverage, parent-reported child/subchild visibility, and `validate_hermes_wizard_wide_run.py` passing as `validated_wide_partial`.
- Hermes-native Wizard skill: `/Users/joshuaeisenhart/.hermes/skills/autonomous-ai-agents/hermes-wizard/SKILL.md` — procedure skill for loading the Hermes Wizard folder and running lightweight Decision -> Failure -> Follow-up barriers with compact route truth.
- Hermes premortem skill: `/Users/joshuaeisenhart/.hermes/skills/productivity/premortem/SKILL.md` — standalone Gary Klein-style prospective-hindsight skill; now strengthened as essential Failure Council member/join gate for consequential Wizard runs.
- Hermes Wizard repo integration scout: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/10_HERMES_NEEDS_RECURSION_KB_PREMORTEM_INTEGRATION.md` — maps RLM-FORGE/Ouroboros to evidence-gated recursion, PageIndex/OpenKB to structure-first compiled wiki/KB ingestion, and premortem to essential Failure Council join gate.
- Hermes Wizard loop sandbox results: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/11_HERMES_WIZARD_LOOP_SANDBOX_RESULTS.md` — durable summary of loop-smoke 0003-0012, including role/provenance wiki classifier, TraceGuard direct gate, profile-driven runner, blocked Ouroboros/RLM runtime, and corrected mass-parallel bounded-profile next loop.
- Sandbox aggregate report: `/tmp/hermes-loop-integration-20260505-135517/artifacts/aggregate_loop_report.md` — temp evidence report, not live runtime authority. (NOTE: the loop-integration sandbox is the only `/tmp/hermes-*` sandbox that still exists on disk; the docs-cleanup, 3x3-MMM, and autoresearch-cleanup sandboxes have been garbage-collected.)
- Profile-driven sandbox runner: `/tmp/hermes-loop-integration-20260505-135517/bin/hermes_wizard_loop_cli.py`; latest admitted receipt `/tmp/hermes-loop-integration-20260505-135517/loop-runs/loop-smoke-0012/receipt.json`; first profile `/tmp/hermes-loop-integration-20260505-135517/profiles/dr_refinement_micro_01.json`.
- Read-only Hermes docs/skills/MMM cleanup loop: GONE — `/tmp/hermes-docs-cleanup-loop-20260506/` was garbage-collected. Evidence summary preserved in `wiki/wizard/hermes-version-current/` harness docs.
- Hermes 3x3 MMM pilot results: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/12_HERMES_3X3_MMM_PILOT_RESULTS.md` — historical sandbox evidence of 9/9 subcouncil receipt-backed workers over one bounded cleanup task; aggregate receipt was at `/tmp/hermes-3x3-mmm-pilot-20260506/receipt.json` (now garbage-collected). Boundary: historical sandbox pilot only, not current preload proof; fresh-session calibration still needed before full MMM-backed Wizard claim.
- Hermes Wizard v4.1 loop harness: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/13_HERMES_WIZARD_V4_1_LOOP_HARNESS.md` — legacy/provenance loop-harness design; current loop work should route through the v4.2 native bridge: self-generated next steps, option pre-runs, premortem/autoresearch, mass subagents/subsubagents, divergence-to-convergence gate, route truth, and explicit apply gate. Includes worker-boundary lesson from quarantined accidental Codex Ratchet scout artifact (now garbage-collected from /tmp).
- Hermes Wizard v4.3 object-preservation guard: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md` — Hermes-native v4.3 preflight guard; runs the repo validator directly. Hermes-authored packet at `wizard/hermes-version-current/packets/hermes_v4_3_retrocausal_object_card.json`. Skill: `hermes-wizard-v4-3-object-preservation`. Routing note: [[wiki-wizard-v4-3-object-preservation-guard]].
- Active Claude Code work: [[active-claude-code-work-2026-06-04]] — read-only snapshot of the live `work-out-layers.js` pipeline (6-stage gated proof program), the owner's actual goals (QIT engines from IGT patterns, dual stacked engine, constraint ratchet), and the current carrier story (nested PEPS2D / Hopfield connection geometry, not PEPS3D). 43 Julia carrier sims, 158 layer sims, JAX+Julia parallel. Nothing has canon yet. Sim inventory: [[claude-code-sim-inventory-2026-06-04]].

Do not:
- treat speculative ideas as already-active plans
- scatter current plans across many unrelated notes if a compact update here would suffice

Related notes:
- [[read-first]]
- [[active-intentions]]
- [[hermes-memory-offload]]
- [[skills-and-agent-rules]]

Write mode: controller-maintained.
