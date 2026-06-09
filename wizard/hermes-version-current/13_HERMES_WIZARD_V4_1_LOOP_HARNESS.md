---
title: Hermes Wizard v4.1 Loop Harness
created: 2026-05-06
updated: 2026-05-06
type: runtime_design
runtime: hermes
status: current-proposed
---

# Hermes Wizard v4.1 Loop Harness

## Purpose

Define the Hermes-native v4.1 loop harness for bounded docs, skills, wiki, tools, and goal-style work.

The loop should be able to:

- infer its own next bounded move when source context is enough;
- pre-run follow-up options as candidate evidence;
- fan out through subagents and, when the runtime exposes them, subsubagents;
- preserve divergent voices and minority reports;
- force convergence through receipt-backed compile gates;
- use premortem as a mandatory Failure Council barrier;
- use autoresearch as bounded candidate discovery, not doctrine;
- emit one human-readable next move plus receipts.

This is a harness design and operating target. It is not live config adoption.

## Core invariant

Wide exploration before the gate. Strict admission at the gate.

Whole-wiki retrieval is useful as corpus search, but the whole wiki is not one authority surface. Authority/admission is per document, profile, receipt, and evidence handle.

Boundedness is per packet/profile/admission path. Independent packets can run mass-parallel when prerequisites, file/state isolation, output paths, and protected surfaces are verified.

## Loop state machine

1. `SCOPE_FENCE`
   - Classify target: `docs`, `skills`, `wiki`, `tools`, or `goals`.
   - Name allowed reads, forbidden writes, protected surfaces, owner, and claim ceiling.
   - Exclude live Hermes config, HERMES/SOUL mutation, MCP registration, credentials, cron activation, and Codex TUI-owned sim surfaces unless explicitly handed off.

2. `PACKET_BOOT`
   - Assign `loop_id`, `profile_id`, `input_hash`, `claim_ceiling`, and `write_mode`.
   - Load the relevant Wizard v4.1 packet surfaces, Hermes adapter/skill surfaces, source receipts, and profile card.
   - For MMM-backed routes, require L0 plus exact member/subcouncil MMM preload before rules/task.

3. `SOURCE_ADMISSION`
   - Treat wiki, memory, session recall, and search hits as candidate context until classified.
   - Admit source slices only with role, provenance, freshness, authority class, contradiction/drift signal, and evidence boundary.

4. `OPTION_SPACE_PRE_RUN`
   - Generate a wide candidate bank before convergence.
   - Run cheap read-only scouts where useful: stale-reference scan, link audit, skill trigger audit, tool-surface inventory, receipt-shape audit, or autoresearch candidate pass.
   - Pre-runs produce candidate evidence only. They cannot self-promote to admitted truth, queue readiness, or applied cleanup.

5. `DECISION_COUNCIL`
   - v4.1 parent topology: `decision.voices_council`, `decision.six_hats_council`, `decision.experts_council`.
   - Hermes 3x3 rendering topology: Scope/Target, Evidence/Context, Action/Route.
   - Output: selected bounded move, live alternatives, evidence boundary, risky claims for Failure, falsifier seed.

6. `FAILURE_COUNCIL`
   - v4.1 parent topology: `failure.premortem_council`, `failure.falsifier_council`, `failure.six_hats_risk_council`.
   - Hermes 3x3 rendering topology: Premortem, Falsifier/Route Truth, Regression/Safety.
   - Premortem is mandatory for substantive loops.
   - Every premortem finding maps to exactly one: `out_of_scope`, `stop_condition`, `required_hardening`, or `dismissed_by_artifact`.

7. `FOLLOW_UP_COUNCIL`
   - v4.1 parent topology: `follow_up.prompt_voice_council`, `follow_up.lane_council`, `follow_up.compile_gate_council`.
   - Hermes 3x3 rendering topology: Option Generator, Scout/Autoresearch, Audit/Selector.
   - Follow-up options are next Wizard inputs. Prework from this loop can inform the next loop, but it does not replace the next loop's Decision -> Failure -> Follow-Up barriers.

8. `RECEIPT_ADMISSION`
   - Admit only terminal, inspectable receipts.
   - Started, streamed, stale, parent-described-only, or shape-only outputs are partial/diagnostic unless evidence handles exist.
   - Keep visibility exact: `controller_verified_raw`, `reported_by_parent`, `artifact_proxy`, or `none`.
   - Tool checks are not child/subsubagent receipts.

9. `DIVERGENCE_CONVERGENCE_GATE`
   - Build a serialized trajectory cache from receipts, not memory.
   - Compare core claim, reasoning path, evidence anchors, operation/falsifier, and conclusion direction.
   - Classify receipt spread as `PATH_IDENTICAL`, `DECORATIVE_SPLIT`, `CONVERGENT_SIGNAL`, `HEALTHY_DIVERGENCE`, or `SINGLE_ANSWER`.
   - Path-identical or decorative splits trigger one smaller rerun when it can change the result.
   - Minority reports must be preserved, promoted to a bounded test, killed by artifact, or held out of scope.

10. `COMPILE_MOVE_GATE`
    - Produce one bounded compiled move, or return `split_smaller`, `hold`, `block`, or `defer`.
    - Universal fields: target, immediate action, owner/lane, success check, stop condition, artifact/output surface, status.

11. `PRE_OUTPUT_ROUTE_TRUTH`
    - Join newest request, input hash, profile, source receipts, parent/child/tool receipts, protected-surface manifest, compiled move, and final render.
    - If header/footer counts disagree with receipts, output is blocked or rerun smaller.

12. `RENDER_AND_CARRY_FORWARD`
    - Render a scan-fast Wizard answer: answer first, council wisdom, compiled move, prompt cards, compact proof footer.
    - Carry forward only bounded reusable state: receipt paths, accepted source handles, next profile, stop conditions, and unresolved blockers.

13. `NEXT_LOOP_SCHEDULER`
    - Compile the next loop packet with profile, target cluster, allowed reads, forbidden writes, success check, stop condition, and expected receipt surfaces.
    - Mass-parallel batches are allowed only when profiles have isolated file clusters and separate output paths.

14. `APPLY_GATE`
    - Live mutation requires a separate explicit apply step.
    - Before apply, loop outputs are notes, receipts, candidate findings, draft patches, or next-loop packets only.

## BARC-RALPH autoresearch pattern

Use BARC inside RALPH:

- `Bound` — fixed objective, fixed surface, fixed profile, fixed query bank, explicit forbidden actions.
- `Audit` — evidence handles, conflict check, premortem, candidate-only boundary.
- `Route` — controller-local, native worker, external audit, artifact proxy, and tool check kept separate.
- `Compile` — exactly one next action, admitted plan, patch candidate, or stop.

Nested cadence:

- `Run` — read-only scoped search or candidate probe.
- `Audit` — verify handles, scope, conflicts, and premortem blockers.
- `Learn` — classify kept, quarantined, discarded, and admitted-plan candidates.
- `Premortem` — ask how this cleanup made the system worse.
- `Harden` — compile one bounded next action or stop.

Autoresearch default output is `candidate_findings.json`. Candidate findings are not accepted truth.

Admission ladder:

```text
candidate -> audited_candidate -> admitted_plan -> patch_candidate -> applied
```

`applied` requires an actual patch/write plus verification receipt. `admitted_plan` means audited for next action, not true globally.

## Required receipts

Minimum receipt families:

- `loop_run_receipt`: loop id, profile id, target surface, input hash, claim ceiling, write mode, protected-surface manifest, isolation status, final status.
- `source_and_lift_receipt`: source slice, role/provenance, authority class, salience loaded, reasoning move changed, contradiction/drift, evidence boundary, non-proof boundary.
- `option_pre_run_receipt`: option id, scout/probe type, artifact, falsifier/boundary found, candidate delta, status.
- `parent_receipt`: council parent, mini-MMM loaded, task card, child obligation, child impact ledger, member utility, conclusion.
- `child_subchild_receipt`: parent id, role, source/tool surface, variant signature, operation/falsifier, distinct delta, outcome delta, evidence anchor, visibility, status.
- `premortem_receipt`: future-failure story, hidden assumption, early warnings, prevention, disposition, mapped hardening/stop condition.
- `autoresearch_candidate_receipt`: baseline, focused read/proposal, verification metric, keep/discard recommendation, evidence boundary, admission status.
- `convergence_receipt`: trajectory cache, per-thinker verdict, divergence classification, minority report, all-wrong rederive, selected reason.
- `compiled_move_receipt`: target, immediate action, owner, success check, stop condition, artifact surface, evidence boundary, claim ceiling, status.

## First profile families

1. `goal_card_contract_normalize`
   - Normalize goals into objective, verify, guard, keep/discard, receipt, and next-action fields.
   - No cron or scheduler activation.

2. `wiki_duplicate_stale_merge`
   - Find duplicate/stale/contradictory wiki pages and produce candidate merge/delete/move cards.
   - No deletion without successor page, authority classification, and explicit apply gate.

3. `skill_doc_setup_claim_audit`
   - Find stale setup/install/auth/runtime claims in skills.
   - Demote or patch only after evidence handles and verification path exist.
   - No package install, auth, MCP, browser, or live config setup.

4. `tool_function_surface_ledger`
   - Map tool docs to exact function/API surfaces, inputs, outputs, and claim ceilings.
   - No execution/config changes unless separately admitted.

## Premortem hardening requirements

The loop should fail closed when:

- loop count rises without artifact delta;
- the same blocker recurs twice without a smaller artifact-level action;
- pre-run success is cited as admission or accepted evidence;
- a child/subsubagent is counted from parent prose or an artifact proxy;
- autoresearch writes outside approved receipt/scratch surfaces;
- whole-wiki search is treated as authority;
- Codex Ratchet sim surfaces would be changed while Codex TUI owns sims;
- route truth cannot compute the newest input hash and receipt-bundle digest;
- live config, HERMES/SOUL, MCP, cron, gateway, credentials, or git state would be changed without explicit apply approval.

## Observed worker boundary lesson

During the design pass for this note, one scout worker wrote a research note into the live Codex Ratchet `work/` directory even though the intended boundary was Hermes docs/skills/wiki harness work. The controller quarantined that artifact to `/tmp/hermes-wizard-autoresearch-cleanup-scout-20260506.md` and removed the live-repo copy.

This is a real Failure Council lesson: child workers must receive explicit forbidden-write surfaces, and controller verification must check for accidental live-repo writes before claiming cleanup safety.

## Output rule

A loop answer should make the human's next decision easier:

1. changed state;
2. best next move;
3. why Decision/Failure/Follow-Up selected it;
4. compiled move;
5. three to four prompt cards;
6. compact proof/footer truth.

Do not show raw worker ledgers unless diagnostics are requested.

## Non-adoptions

This note does not adopt:

- live Hermes config changes;
- HERMES/SOUL rewrites;
- MCP registration;
- cron activation;
- Ouroboros/RLM runtime enablement;
- Codex Ratchet sim cleanup while Codex TUI owns sims;
- broad whole-wiki authority.

## Option-4 repeat-loop gate

A selected `4` / `All of the Above` option may be repeated as a loop, including a 20-iteration loop, only when the gate passes before the loop starts and again after each iteration.

Required preflight:

- real premortem parent route ran;
- enough parent subagents ran for the selected scope;
- child/subsubagent receipts are controller-visible, not inferred from parent prose;
- route-truth/falsifier and regression/safety parent routes ran;
- every parent reports expected/completed child counts;
- no parent status contains `hold`, `blocked`, `needs_hardening`, or equivalent unresolved stop condition;
- protected-surface manifest excludes live Hermes config, HERMES/SOUL, MCP/cron/gateway, credentials, git mutation, and Codex TUI-owned sim surfaces;
- loop body remains read-only or draft-only until an explicit apply gate is approved.

Observed preflight:

`/tmp/hermes-v41-option4-20-preflight/audit/preflight_aggregate_receipt.json`

Result: `HOLD_20_LOOP`.

The preflight produced 3 parent receipts and 6 child receipts, but one parent returned `needs_hardening_hold_before_20_loop`. That is enough to prove the gate is working; it is not enough to launch the 20-loop run.

## Autoloop round 0001

Chosen follow-up: clear the safety hold by building an enforcement-first read-only loop runner preflight.

Artifacts:

- root: `/tmp/hermes-v41-autoloop-rounds/round-0001/`
- runner: `/tmp/hermes-v41-autoloop-rounds/bin/read_only_loop_runner.py`
- receipt: `/tmp/hermes-v41-autoloop-rounds/round-0001/runner/receipt.json`
- audit: `/tmp/hermes-v41-autoloop-rounds/round-0001/runner/audit.json`

Route truth:

- parent receipts: 3/3;
- child receipts: 6/6;
- premortem parent: completed;
- enforcement/audit parent: complete;
- follow-up selector parent: complete conditional proceed/hold;
- tools: local Python runner only, not counted as children;
- model-family boundary: no Sonnet/Haiku/Opus proof in the current Hermes delegate route.

Runner status: `admitted_plan`.

The runner found candidate-only cleanup findings and selected `patch source map note13 entry` as the next safe action. That action was applied to `sources/SOURCE_MAP.md` after the runner audit passed. Candidate findings remain candidate/admitted-plan material, not global truth.

## Autoloop round 0002

Chosen follow-up: run a read-only MMM calibration battery after round 0001 cleared the enforcement preflight.

Artifacts:

- root: `/tmp/hermes-v41-autoloop-rounds/round-0002/`
- audit: `/tmp/hermes-v41-autoloop-rounds/round-0002/audit/calibration_audit.json`
- summary: `/tmp/hermes-v41-autoloop-rounds/round-0002/summary.md`
- calibration receipts: `/tmp/hermes-v41-autoloop-rounds/round-0002/calibration/*.json`

Route truth:

- premortem parent: 1/1 with 2/2 children;
- audit/enforcement parent: 1/1 with 2/2 children;
- calibration condition workers: 4/4;
- overclaims: 0;
- high-similarity collapse pairs: 0;
- MMM salience score improved over no-MMM in the bounded same-session audit.

Runner status: `pass` as calibration candidate.

Boundary: this supports a small same-session behavior signal only. It does not prove durable fresh-session adoption and does not prove Sonnet/Haiku/Opus feedback because the current Hermes route did not expose those model-family receipts.

## Opus subagent route proof

A separate Claude Code custom-agent proof established a working Opus route for future external feedback pressure:

- root: `/tmp/hermes-claude-opus-proof-20260506T062943Z/`
- file-agent probe: `/tmp/hermes-claude-opus-proof-20260506T062943Z/outputs/file_probe.json`
- nested manager/leaf probe: `/tmp/hermes-claude-opus-proof-20260506T062943Z/outputs/nested_probe.json`
- summary: `/tmp/hermes-claude-opus-proof-20260506T062943Z/outputs/summary.json`

Results:

- `OPUS_AGENT_OK` returned with `modelUsage` containing `claude-opus-4-7`.
- `NESTED_OK` returned with `modelUsage` containing `claude-opus-4-7`.

Interpretation: use Claude Code custom agents in print mode as the current working path for Opus subagents/subsubagents. Do not treat this as proof of Hermes-native `delegate_task` ACP Opus routing. `modelUsage` also includes Haiku overhead, so do not claim pure-Opus-only execution.

## Next safe proof

Run autoloop round 0003 as stricter fresh-session/external-feedback audit when an external model route is actually available, then validate:

- protected-surface manifest;
- candidate-only autoresearch output;
- premortem mapped findings;
- route-truth receipt join;
- one `receipt.json`, one `summary.md`, and `raw/` evidence;
- no live config/git/Codex sim mutation.

Write mode: controller-maintained.
