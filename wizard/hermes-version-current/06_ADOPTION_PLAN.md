---
title: Hermes Wizard Adoption Plan
type: adoption_plan
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Adoption Plan

## Phase 0 — Docs only

Status: completed 2026-05-04.

Create this folder and do not change global runtime behavior.

Pass condition:

- folder exists;
- sources and import decisions are explicit;
- no HERMES.md/SOUL.md edits are required to understand it.

## Phase 1 — Create a skill

Candidate skill:

`hermes-wizard`

Status: completed 2026-05-04 at `/Users/joshuaeisenhart/.hermes/skills/autonomous-ai-agents/hermes-wizard/SKILL.md`.

Purpose:

- load this folder when Wizard behavior is requested;
- run the lightweight Decision -> Failure -> Follow-up barriers;
- use Hermes tools/workers only where useful;
- render through Hermes's existing scaffold;
- keep receipts compact in Results.

Do not paste these docs into the skill. The skill should be a short procedure with links to this folder.

## Phase 2 — Dry-run proof packet and sandbox loops

Status: initial manual and sandbox proof packets completed 2026-05-05/06.

Completed evidence includes:

- Hermes Wizard minimal/wide fixtures under this folder's `runs/` tree;
- validators for minimal and wide-partial run directories;
- RLM/OpenKB/PageIndex/premortem sandbox scout under `/tmp/hermes-loop-integration-20260505-135517/`;
- reusable profile-driven sandbox runner at `/tmp/hermes-loop-integration-20260505-135517/bin/hermes_wizard_loop_cli.py`;
- latest profile-driven receipt at `/tmp/hermes-loop-integration-20260505-135517/loop-runs/loop-smoke-0012/receipt.json`;
- summary note `11_HERMES_WIZARD_LOOP_SANDBOX_RESULTS.md`.

Pass condition now:

- every visible route has a receipt or block/defer reason;
- Follow-up entries remain future choices;
- Results does not become a raw worker log;
- per-profile admission stays local and evidence-gated;
- no live Hermes config/wiki/queue mutation is implied by sandbox proof.


## Phase 3 — Conformance fixtures

Add fixture examples for:

- ordinary direct answer;
- fake worker claim;
- memory-as-proof failure;
- unscouted follow-up failure;
- blocked route answer;
- conflicting worker receipts;
- stale handoff;
- successful workerized packet.

Pass condition:

- the checklist rejects the failures and accepts the successful packet.

## Phase 4 — Tiny HERMES pointer only if needed

Candidate pointer:

`Wizard-mode Hermes routing lives in ~/wiki/wizard/hermes-version-current/ and should be loaded through the hermes-wizard skill when explicitly requested or when route-truth/follow-up-runtime work is admitted.`

Do not add packet details to HERMES.md.

## Phase 5 — Optional runtime/tooling

Status: sandbox tooling exists; live runtime adoption is not done.

Current sandbox tooling:

- profile-driven sim loop CLI under `/tmp/hermes-loop-integration-20260505-135517/bin/`;
- target profile and receipts under the same sandbox;
- no live Hermes config or MCP registration.

Next tooling target:

- create a separate non-sim docs/skills/MMM cleanup loop runner in `/tmp/` first;
- use mass parallel bounded profiles with one batch receipt, one summary, and raw worker evidence;
- keep live writes behind a separate explicit apply step.

Only after repeated sandbox/manual success:

- add a helper script or validator to a durable location;
- add a skill support file/template;
- consider a skill command or slash route;
- integrate with cron/gateway only with explicit scope.

## Stop conditions

Stop or retreat if:

- the folder starts duplicating HERMES.md or SOUL.md;
- every answer starts running fake Wizard ceremony;
- the skill grows into a packet dump;
- memory/session summaries are treated as execution proof;
- follow-up prework is claimed without scout/audit receipts;
- user-facing output becomes harder to read.
