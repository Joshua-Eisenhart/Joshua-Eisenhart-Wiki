# Wiki Wizard v4.2 Autoloop Control

Purpose: control surface for the finite Hermes Wizard v4.2 wiki-improvement autoloop.

Status: active bounded automation note.

Bridge note: [[wizard/hermes-version-current/14_HERMES_WIZARD_V4_2_NATIVE_LOOP_BRIDGE]]

Current v4.3 maintenance template: [[wiki-wizard-v4-3-mmm-maintenance-template]]

Job:
- Origin Hermes cron job id: `796b4560f2f5` (finite 8-tick setup job; historical, not assumed live)
- Original name: `Wizard v4.2 wiki autoloop — premortem repair`
- Original schedule: every 45 minutes for 8 ticks, delivery to origin chat
- Current continuation: any scheduled steward prompt that explicitly invokes this note; do not create, edit, remove, or recursively schedule cron jobs from inside a tick
- Delivery: scheduler-configured destination through the final response only
- Workdir: `/Users/joshuaeisenhart/wiki`
- Toolsets: file, terminal, delegation, skills

## Current operating truth

The wiki is structurally clean as of the latest local v4.3 maintenance preflight probe:
- `fresh-rerun: /tmp/wiki_probe_pre_v43_maintenance_20260606.json`
- `page_count = 438`
- `broken_links = 0`
- `missing_pages = 0`
- `malformed_wikilinks = 0`
- `stale_namespace_wikilinks = 0`
- `sha256 = 1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0`

Current scheduler truth:
- Historical v4.2 origin job `796b4560f2f5` remains historical and must not be assumed live.
- A new finite v4.3 MMM maintenance steward exists: job `497a2eaaa178`, schedule `every 45m`, repeat `8`, deliver `origin`, workdir `/Users/joshuaeisenhart/wiki`.
- This note is the v4.2 bridge/control surface; new maintenance ticks should start from [[wiki-wizard-v4-3-mmm-maintenance-template]].

Current v4.3 preflight truth:
- The Hermes v4.3 object card validated with the repo guard after the carrier-drift patch: `/tmp/v43_validate_after_carrier_patch_20260606.json`, `ok=true`, `errors=0`; packet sha256 `fe8c20c7124930a1c95e14287d8540d18437345d63a5dfd92558a30177992d39`.
- v4.3 selftest passed before the carrier patch: `/tmp/v43_selftest_20260606.json`, `ok=true`, sha256 `affafb63b2732b34c41c61c4674e07c50f7627adb542aa0dc8255676be42daa2`.
- v4.3 loop smoke passed before the carrier patch in one loop: `/tmp/v43_loop_20260606.json`, `ok=true`, `loops=1`, sha256 `67ed37c28e5b4f21cea82bf87ab081a16b9ff384fa0f3ad50fa1064e0affb2`.
- Positive primary-card PEPS3D drift was removed: `plain_contains_PEPS3D=False`, `allowed_contains_PEPS3D=False`, `adapter_contains_PEPS3D=False`; remaining PEPS3D mentions are forbidden-substitution / kill-control only.
- Claim ceiling: object-preservation preflight only. v4.2 remains the council runtime and still needs its own route-truth receipts.
- Local receipt: [[wizard-v4-3-maintenance-preflight-receipt-2026-06-06]].

Current path-routing truth for this continuation:
- active Wizard universal front door: `wizard/`
- Hermes-owned Wizard adaptation: `wizard/hermes-version-current/`
- nominalist-CS harness support copy: `wizard/harness-consolidated/`
- do not route new workers to an old `wiki/harness/` root unless a later explicit migration restores that path
- Wizard v4.3 awareness: v4.3 is an additive object-preservation guard that runs before v4.2 councils; it does not change this v4.2 autoloop runtime. Its authority is repo-held (Codex Ratchet), not wiki-held. See [[wiki-wizard-v4-3-object-preservation-guard]]. Do not create a `packet-v4-3-current` from this loop.
- Entropic monism / Axis0 owner-kernel route: when a tick concerns JK fuzz, Axis0, entropic monism, cross-field ToE genealogy, or field-wide compression geometry, load [[entropic-monism-axis0-field-compression-spine]], [[cross-field-toe-genealogy]], and [[field-wide-compression-geometry]] after the `hermes-current/` spine. Treat these as source-processing/model-spine surfaces, not proof/admission surfaces.

The Codex Ratchet repo is not runner-clean:
- recent status surface: `projects/codex-ratchet/STATUS.md`
- latest blocked-reason/queue snapshot remains red with `lane_A=0`, `lane_B=0`, `claimed=0`, `blocked=852`, `done=8856`
- dominant current blocker is `wizard_admission_blocked=632/852`; do not treat the runner as clean just because claimed is now zero
- current full repo contract lint remains red with `1,580` violations across `1,316` sims (`fresh-rerun: /tmp/lint_sim_contract_after_deep_audit_em_bridge_downgrade.json`); the active legacy C1 cleanup lane has reduced `C1_classification_missing` to `1085`, while prior C4 cleanup reduced the full C4 bucket to `231` and the blocked-queue C4 subreason bucket remains `11`
- current C4 proposal surface reports `0` simple divergence-log-only candidates and `231` classification/stage/contract-bundle review candidates; do not treat C4 rows as simple source edits unless the report explicitly marks them simple
- Git index instability remains a live hazard; do not trust plain `git status` as authority there

## Tick contract

Each tick must:
1. reread `hermes-current/` spine notes and relevant project front doors;
2. read Wizard v4.2 runtime and skills manifest enough to apply the topology;
3. run `wiki_probe.py` before edits;
4. choose exactly one bounded tranche;
5. run premortem + loophole audit before edits;
6. use external model-family pressure when available, read-only only;
7. apply at most one small repair/improvement tranche;
8. inspect touched files directly;
9. rerun `wiki_probe.py` after edits;
10. append exactly one log entry with changed files, model routes, premortem dispositions, verification, and next tranche.

## External model-family pressure

Advisory/read-only routes, not authority by themselves:
- Claude Opus
- Claude Sonnet
- Claude Haiku
- Gemini
- Grok / xAI when an executable or configured provider route is actually available
- Codex
- Hermes/controller synthesis

Model outputs are premortem/audit receipts. They do not directly authorize edits, truth-label promotion, repo claims, or wiki page creation.

## Premortem consensus from setup preflight

Independent model routes converged on the same danger pattern:
- structural green can hide semantic overclaim;
- one-tranche discipline can decay into blob pages;
- Codex Ratchet red runner/index state can be laundered into wiki prose;
- log entries can become success theater unless they include before/after probe evidence;
- repo-backed claims need explicit snapshot/fresh-rerun labels;
- `hermes-current/` should not become a project-detail dump.

## Outer vs inner loop

- Outer loop: the scheduled steward invocation, finite by its prompt or scheduler contract, one bounded wiki tranche per tick.
- Inner loop: optional Wizard `auto loop auto` reasoning inside a tick, capped by the tick prompt and stopped before apply if route truth or premortem dispositions are incomplete.
- A tick may report `PARTIAL` or `BLOCKED` with no wiki edit; that is success when the honest move is to stop.

## Required tick receipt bundle

Each tick should leave or report:
- tick id or input hash;
- declared target cluster;
- allowed files;
- forbidden surfaces;
- preflight `wiki_probe.py` path/result;
- Decision, Failure, and Follow-Up summaries or explicit blocked/not-run status;
- premortem + loophole findings mapped to `out_of_scope`, `stop_condition`, `required_hardening`, or `dismissed_by_artifact`;
- external model route states for Claude, Gemini, Grok, Codex, and Hermes/controller: `completed`, `blocked`, `deferred`, or `not_run`;
- changed files;
- direct inspection note for touched files;
- final post-log `wiki_probe.py` path/result;
- next bounded tranche or stop reason.

## Wiki alignment receipt fields

For any page touched or audited for LLM-alignment work, classify: file, role, authority class, freshness, source support, drift signal, allowed write status, claim ceiling, and next action.

## Mandatory stop conditions

Stop the tick, repair, or report blocked if:
- pre- or post-edit `wiki_probe.py` fails;
- page count changes without an explicit create/delete/archive tranche;
- a tranche touches files outside its declared scope;
- a repo-backed claim lacks `snapshot:` or `fresh-rerun:` support;
- Codex Ratchet runner health is summarized as clean while the current blocked backlog remains red (`blocked=852`, dominant `wizard_admission_blocked=632/852`) or full contract lint remains red (`1,580` violations);
- plain `git status` is used as authority for the unstable Codex Ratchet repo;
- `hermes-current/` is touched without a declared Hermes-spine/control-surface reason;
- new content starts becoming a salience-first blob instead of a routed page or bounded support note.

## Preferred tranche order

1. Structural integrity repair if probe is dirty.
2. Routing coherence if pages exist but are weakly routed.
3. Role clarification for overlapping clusters.
4. One bounded owner-kernel/source-spine or repo-to-wiki/result-family content cluster.
5. Support-layer routing/handoff polish.
6. Tooling/verification improvement only if it removes a real blocker.

## Best first tranche

Use an alignment-first tranche unless the preflight is dirty:
- name the concrete wiki/Hermes alignment surface being improved before selecting work: front door, Hermes spine, bridge/control note, skill pointer, research/evidence router, or bounded support note;
- prefer the smallest research-index reconciliation that helps future LLMs load Josh's goal, language, research spine, evidence discipline, and next bounded wiki move;
- treat route truth, receipt checks, Codex Ratchet RED status, queue safety-window limits, and Git-index instability as guardrails/falsifiers around that alignment target, not as the content target;
- if the only payoff is `prove routes ran`, `audit receipts`, or `generic safety/freshness`, mark the tranche `diagnostic-only/PARTIAL` and select a smaller alignment surface instead;
- patch only the missing control/router guardrail needed to preserve that objective;
- run wiki probe before/after;
- log the result.

## Do not

- do not schedule more cron jobs from inside a tick;
- do not edit raw/source corpora unless the tranche is explicit raw ingest with provenance wrapper;
- do not create broad synthesis pages from multiple unrelated clusters;
- do not mutate Codex Ratchet repo state from the wiki loop;
- do not report success if verification fails.

Related notes:
- [[read-first]]
- [[active-plans]]
- [[wiki-ingest-queue-and-priorities]]
- [[projects/codex-ratchet/STATUS]]
- [[wizard/hermes-version-current/14_HERMES_WIZARD_V4_2_NATIVE_LOOP_BRIDGE]]

Write mode: controller-maintained automation control surface.
