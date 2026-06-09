---
title: Hermes Skill Import Audit for Wizard Work
type: skill_audit
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Skill Import Audit

This audit lists skills that encode Codex/Codex-Ratchet/Wizard/subagent/controller patterns useful for a Hermes-owned Wizard.

Correction note: the first pass under-audited Codex's own local skill stack. The corrected detailed audit is `07_CODEX_LOCAL_SKILL_STACK_AUDIT.md`, covering `/Users/joshuaeisenhart/.codex/skills/` directly.

## Import strongly

| Skill | Useful import | Boundary |
|---|---|---|
| `autonomous-ai-agents/codex` | bounded Codex CLI worker, PTY/background monitoring, modify-verify-decide loop | Codex is worker/auditor, not truth authority |
| `autonomous-ai-agents/claude-code` | print-mode worker path, JSON/session/cost artifacts, worktree isolation | do not trust stdout summaries without artifacts |
| `autonomous-ai-agents/hermes-agent` | Hermes tools, profiles, skills, memory, gateway, cron, MCP, prompt/control split | do not turn docs into live config changes without proof |
| `autonomous-ai-agents/hermes-delegate-runtime-proof` | prove `delegate_task` with boot bundle, task cards, receipt-shaped closeout | fresh import proof is not live backend proof |
| `autonomous-ai-agents/hermes-output-surface-stress-test` | runtime registry, route truth, council/plurality validators, reroute status | avoid giant blended stress runs as default |
| `autonomous-ai-agents/lean-hermes-control-and-accounting-skills` | keep HERMES lean, procedures in skills, layer split | do not paste Wizard packet into HERMES.md |
| `software-development/subagent-driven-development` | bounded workers plus independent spec/quality reviews | implementer self-review is insufficient |
| Codex `$premortem` / `/Users/joshuaeisenhart/.codex/skills/premortem/SKILL.md` | Gary Klein-style prospective hindsight: assume future failure, generate failure reasons, deep-dive each reason, synthesize hidden assumption and revised plan | import as standalone Hermes `premortem` skill plus optional Failure barrier lens; do not bury it as a label-only risk paragraph |
| `software-development/hermes-autoresearch` | measurable improve-verify-decide loop | no ontology/dispute work without metric |
| `software-development/bounded-autoresearch-for-maintenance` | atomic maintenance loop with verify/guard/keep-discard | not for broad theory closure |
| `note-taking/capture` | read/memory/inferred/volatile accounting | capture is not proof or a mega-summary |
| `note-taking/hermes-follow-up-menu-style` | follow-ups as prepared future choices, not receipts | menus cannot imply execution |
| `software-development/hermes-stress-packet-role-receipt` | role-specific receipt shape with observed/inferred/open labels | no route redesign inside a receipt |

## Import for Codex Ratchet / sim lanes only

| Skill | Useful import | Boundary |
|---|---|---|
| `software-development/codex-ratchet-sim-planning` | micro-lego, geometry-first, truth labels, tool integration, bounded worker cap | project-specific, not general Hermes law |
| `software-development/hermes-sim-controller-orchestration` | Hermes as controller, workers bounded, runner/log/artifact verification | only for sim/controller work |
| `software-development/sim-controller-batch` | authority preflight, dirty tree checks, queue/doc/wiki lane separation | do not generalize Telegram/runtime details |
| `software-development/codex-ratchet-geometry-micro-packets` | one object/law/invariant packet discipline | not a default for ordinary Hermes tasks |
| `software-development/tool-capability-sim-planning` | tool-function micro receipts before tool claims | apply when tool proof matters |
| `software-development/truth-audit-and-tool-maintenance` | post-batch result/manifest/doc truth audit | result JSON logic is repo-specific |
| `audit/codex-ratchet-audit` | systematic audit and metric checking | source exists/result exists/fresh rerun remain separate |
| `audit/codex-ratchet-meta-drift-detector` | conservative drift detector with silence when clear | avoid noisy detectors in ordinary work |
| `software-development/llm-research-enforcement` | strict status vocabulary, worker closeout schema, validators | research-stage specific |
| `harness-guided-synthesis` | evidence-grounded synthesis with contradiction preservation | not a generic summary style |

## Import for durable wiki/controller work

| Skill | Useful import | Boundary |
|---|---|---|
| `note-taking/wiki-maintenance-and-harness` | tranche-based wiki audits, lint, provenance, raw/source distinction | avoid whole-vault salience-first edits |
| `note-taking/wiki-ingest-and-lego-maintenance` | repo-doc sync, ledger/wiki maintenance, conservative status | raw ingest is not final synthesis |
| `note-taking/codex-ratchet-wiki-steward-cron` | auditable cron tick discipline | cron evidence must be verified from live state |
| `note-taking/wiki-harness-authoring-with-claude-workers` | draft -> adversarial audit -> controller reconciliation | do not trust worker word counts/links |
| `software-development/overnight-cron-controller-runs` | repeated bounded fresh ticks | cron does not inherit current chat context |
| `software-development/tier-gate-watch-and-launch` | blocked planning vs launch gating | no chatter while gate red |
| `software-development/layered-system-stabilization-doc-stack` | layered docs, authority hierarchy, bounded read packs | no mega-summary replacing authority docs |

## Created Hermes skills

- `hermes-wizard`: created 2026-05-04 at `/Users/joshuaeisenhart/.hermes/skills/autonomous-ai-agents/hermes-wizard/SKILL.md`.
- `premortem`: created 2026-05-04 at `/Users/joshuaeisenhart/.hermes/skills/productivity/premortem/SKILL.md` after correcting the missed Codex standalone skill import.

## Proposed new skill later

None open for this audit section.

Historical candidate now completed:

`hermes-wizard`

Trigger:
- explicit Wizard/council/workerized/stress/follow-up-runtime request;
- complex work where route truth, critique, or follow-up prework can materially improve the answer;
- repeated need to use this folder's contract.

It should reference this folder and stay procedural. It should not duplicate the full folder.

## Import rule

Import process patterns, not path-specific cargo cult.

If a skill carries a repo-specific path, treat the path as an example unless the current task is that repo.
