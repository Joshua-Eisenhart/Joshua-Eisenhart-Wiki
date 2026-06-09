---
title: Hermes Wizard Maintenance Governor
type: runtime_contract
runtime: hermes
created: 2026-06-05
updated: 2026-06-05
status: current-proposed
---

# Hermes Wizard Maintenance Governor

This note aligns the Hermes Wizard with Hermes maintenance without turning Wizard into a second global prompt or a separate operating system.

## Role

Hermes Wizard may supervise maintenance of:

- Hermes itself: config, runtime docs, gateway/cron/delegation surfaces, and profile-scoped control files when explicitly in scope.
- Durable memory: preserve first, normalize into wiki/skills, then compress injected memory to compact pointers.
- Skills: patch procedures when a real run exposes stale, missing, or wrong guidance.
- Wiki: keep `hermes-current/` as the low-entropy frame-loader and route deeper doctrine/project pages from it. Owner-kernel/source-spine tranches are valid maintenance targets when the user is preserving or clarifying model language; current example route: [[entropic-monism-axis0-field-compression-spine]], [[cross-field-toe-genealogy]], and [[field-wide-compression-geometry]].
- Subagents: track task cards, launch receipts, completion/block status, outputs, and promotion/defer decisions.

This is a maintenance governor role, not a new authority layer.

## Authority boundary

For live Hermes behavior, authority remains:

1. current user request
2. `~/.hermes/HERMES.md` — control law, routing, output scaffold
3. `~/.hermes/SOUL.md` — body voice and anti-collapse method
4. `~/wiki/hermes-current/` — long-form Hermes frame and memory-offload spine
5. skills — executable maintenance procedures
6. Wizard docs — controller design, run receipts, and proof/maintenance contracts

Wizard coordinates these surfaces. It does not replace them.

## Maintenance loop

Use a bounded loop:

1. **Inventory** — name the maintenance surface and read only the needed current files/receipts.
2. **Classify** — decide whether the issue belongs in memory, wiki, skill, config, cron, gateway, or runtime code.
3. **Patch one cluster** — keep shared-state writes serial through the controller.
4. **Verify** — run file/readback/probe/checks that prove the patch landed; provider/worker output is pressure, not proof.
5. **Log or queue** — record durable state in the wiki or skill only when it will matter later.
6. **Stop or continue** — continue only while a finite cap remains, the next tranche is obvious and safe, and the objective has not drifted.

For memory pressure specifically, preserve the live memory/profile snapshot into `hermes-current/memory-maintenance-YYYY-MM-DD.md` before compression. Then update `hermes-memory-offload.md` or the target spine note, patch skills if the procedure failed, and only then shrink injected memory.

## Subagent ledger contract

Every spawned or queued subagent route needs a compact ledger entry with:

- task card / objective
- owner or route (`delegate_task`, codex2, Claude Code, Grok/Gemini pressure, cron/background)
- launch receipt or block reason
- input surfaces allowed
- output artifact or summary receipt
- status: `running`, `completed`, `blocked`, `deferred`, `killed`, `superseded`
- promotion decision: `admit`, `repair_then_admit`, `defer`, `reject`, or `needs_controller_verification`

Do not let the parent summary become proof of child/subchild work. Parent-reported nested work stays `parent_reported` unless raw artifacts are controller-visible and verified.

## Worker routing

For heavy maintenance reading/patching, codex2 is the preferred heavy worker. Hermes stays controller/verifier/editor.

Use external lanes by function:

- codex2 — heavy source/wiki/skill reading and draft patches
- Claude Code Sonnet/high — strong source review and repair pressure
- Grok/Gemini — contrast, gap finding, premortem, and research pressure when live credentials/routes are verified
- Opus — occasional high-stakes review only

All worker outputs remain advisory until Hermes verifies the changed files or durable artifacts.

## Shared-state safety

Keep these serial through Hermes controller unless a separate explicit profile/worktree/surface split exists:

- profile config changes
- durable memory edits
- skill edits
- front-door wiki edits
- cron creation/removal
- gateway or platform delivery
- subagent ledger promotion

Parallel subagents can read, scout, audit, and propose; they should not race-write the same control or memory surfaces.

## Output requirement

A maintenance Wizard answer should say, compactly:

- what changed
- what was verified
- what remains open
- which subagents/routes ran, blocked, or were deliberately not run
- where the durable receipt lives, if any

Do not dump raw subagent logs unless asked.

## Stop conditions

Stop the maintenance loop when:

- the finite cap is reached
- the same blocker repeats
- no artifact delta appears
- route truth fails
- a needed permission or current-source read is missing
- the next tranche would mutate shared state without a clear user-scoped objective
- the task drifts from the user's maintenance request

## Non-goals

- Do not paste this note into `HERMES.md`.
- Do not make Wizard a replacement memory provider.
- Do not make every ordinary Hermes answer a maintenance run.
- Do not split the main Hermes profile/wiki surfaces into per-agent surfaces until independent profiles or explicit agent boundaries exist.
