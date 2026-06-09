---
title: Wizard v4.1 Skills Manifest
type: skills_manifest
packet: v4.1
framing: standalone
---

# Wizard v4.1 Skills Manifest

This packet carries local skills. Skills are executable workflow dependencies,
not reference prose.

## Skill Architecture

The wiki packet is the portable source of truth for Wizard skills. Runtime
systems mirror or adapt these skills into their own local skill surfaces
(`~/.codex/skills`, Claude project skills, Gemini/OMX wrappers, or other agent
skill registries), but the canonical definitions live here so every system can
reference the same member behavior.

Skill-backed council members are allowed and encouraged when a member has a
repeatable workflow rather than just a salience role. A member skill must be:

- portable: no runtime-specific paths unless in an adapter section;
- receipt-shaped: it returns what ran, what changed, what stayed blocked, and
  what evidence supports the claim;
- MMM-compatible: it names the main/compact/mini-MMM surface it expects;
- loop-safe: it has a stop condition, iteration cap, or confidence gate;
- non-authoritative: it informs the parent council but does not replace
  Decision, Failure, Follow-Up, child-health, or compile-gate receipts.

Agent systems may maintain runtime-local versions of these skills, but a
runtime-local copy must declare its upstream wiki source path and any adapter
differences. If the runtime copy diverges without a declared adapter reason,
the packet-local wiki skill wins.

## Required Skills

- `claude-bridge`
  - Local path: `skills/claude-bridge/SKILL.md`
  - Required by: substantive Codex-adapter Wizard runs when external Claude worker capacity is available.
  - Purpose: run Claude Code as an external worker pool with bounded model routing, budgets, timeouts, and receipts.
  - Required local wrappers:
    - `skills/claude-bridge/scripts/claude_bridge.py`
    - `skills/claude-bridge/scripts/claude_child_fanout.py`
    - `skills/claude-bridge/scripts/fanout_receipt_summary.py`
  - Count rule: Claude Bridge counts only when the wrapper returns a receipt with model, status, output path, receipt path, and usable route signal. Claude final prose without receipt evidence is advisory only.

- `premortem`
  - Local path: `skills/premortem/SKILL.md`
  - Required by: `failure.premortem_council`
  - Purpose: Gary Klein-style prospective-hindsight premortem.
  - Wizard boundary: returns receipt fields only; does not create reports,
    transcripts, HTML, or open a browser.
  - Count rule: A premortem route only counts when this skill is loaded and
    its workflow is used, or when the route is explicitly marked blocked or
    degraded with the missing skill path.

## Portable Council-Member Skills

Canonical portable council-member skills live under
`skills/council-members/`. These are wiki-level skills that any agent runtime
can mirror locally:

| skill_id | owning member/route | binding | canonical path | Codex mirror path | side-effect boundary | count/block rule |
| --- | --- | --- | --- | --- | --- | --- |
| `strategy-loop` | `voice.strategy`, loop controller children | optional | `skills/council-members/strategy-loop/SKILL.md` | `~/.codex/skills/wizard-strategy-loop/SKILL.md` | no external side effects | Counts only with skill receipt and loop-control return fields. |
| `systems-strategy` | `voice.systems`, strategy audit children | optional | `skills/council-members/systems-strategy/SKILL.md` | `~/.codex/skills/wizard-systems-strategy/SKILL.md` | no external side effects | Counts only when it names system boundary, feedback loop, and local-optimization risk. |
| `loophole-auditor` | Failure/loop audit routes | optional | `skills/council-members/loophole-auditor/SKILL.md` | `~/.codex/skills/wizard-loophole-auditor/SKILL.md` | no external side effects | Counts only when it declares evidence standard, loopholes, fixes, confidence status, and stop/next-loop condition. |
| `follow-up-selector` | `follow_up.prompt_voice_council`, `follow_up.lane_council` | optional | `skills/council-members/follow-up-selector/SKILL.md` | `~/.codex/skills/wizard-follow-up-selector/SKILL.md` | no external side effects | Counts only when it makes, pre-runs, audits, improves, and selects a next prompt. |
| `factory-handoff` | `voice.factory`, queue/handoff children | optional | `skills/council-members/factory-handoff/SKILL.md` | `~/.codex/skills/wizard-factory-handoff/SKILL.md` | no external side effects | Counts only when it returns bottleneck, next station, handoff artifact, leverage, and queue movement check. |

Digest/version rule: receipts should record `source_digest` and
`mirror_digest` when the runtime can compute them. If a digest is unavailable,
the receipt must say `unknown` and name the exact file path loaded. A stale
mirror is blocked unless the adapter delta explains why it is intentionally
different.

These skills can be assigned to council parents or children through task cards.
They still require receipts and child/parent linkage. A skill call is not a
council member unless a real worker or tool invoked it and returned a receipt.

## External Loop Skill

- `codex-autoresearch`
  - Canonical runtime skill: `~/.agents/skills/codex-autoresearch/SKILL.md`.
  - Wizard role: long-running improve/verify loop for measurable goals after
    the Wizard has produced a bounded goal, metric, scope, verification command,
    guard, iteration cap, and stop condition.
  - Boundary: interactive launches keep the codex-autoresearch ask-before-act
    rule. The Wizard may prepare an autoresearch launch packet and ask for the
    required run-mode approval; it must not silently start a background
    autoresearch loop unless the user explicitly approved that launch mode.
  - Count rule: autoresearch receipts are loop-runtime evidence, not
    Decision/Failure/Follow-Up council replacements.

## Runtime-Callable Codex Skill Registry

The Wizard may route council parents or children through existing Codex skills
when the task matches the skill and the worker returns a receipt-shaped result.
Do not load every skill into every worker. Select the narrowest useful skill for
the route, record the loaded path, and keep the skill inside the parent/child
receipt boundary.

| skill_id | default Wizard use | route fit | count/block rule |
| --- | --- | --- | --- |
| `codex-autoresearch` | bounded improve/verify loop after a compiled move has a metric, guard, cap, and approval | Follow-Up loop runtime, not a council replacement | Counts only as loop evidence with launch approval/run mode and verification command. |
| `prior-art` | check whether the repo/history already contains the same strategy, failure, or pattern | Decision experts, Failure falsifiers, Follow-Up scout | Counts only when it cites inspected local sources and says what is reused, contradicted, or absent. |
| `prompt-guard` | adversarial prompt/security boundary scan | Failure falsifier or loophole child | Counts only with explicit attack/failure class, affected surface, and fix/stop condition. |
| `arch` | architecture and trade-off review | Decision experts, Strategy/System voices | Counts only with quality attributes, trade-off, and boundary/rollback condition. |
| `testing-golden-artifacts` | make output regressions testable | Follow-Up compile gate, Failure prevention child | Counts only with a concrete golden artifact/check and update policy. |
| `safe-run-maintenance` | archive-first cleanup and repo hygiene | Factory/handoff, Follow-Up lane | Counts only when it avoids destructive cleanup and names archive/keep/delete classes. |
| `thread-run-monitor` | detect stalled/blocked workers | management.child_health, management.rerouter | Counts only with worker ids/statuses, deadlines, and reroute action. |
| `thread-dispatch-controller` | bounded worker launch planning | management.resource_pressure, management.rerouter | Counts only with launch plan, pool split, deadline, and receipt requirement. |
| `pro-return-instant-audit` | audit returned external/deep-research packets | Failure falsifier, Follow-Up audit | Counts only with accepted/rejected findings and evidence refs. |
| `a2-brain-refresh` | refresh Ratchet A2 context before memory-sensitive work | Decision context parent | Counts only with exact read/write boundary and no hidden memory promotion. |
| `ratchet-a2-a1` | inspect Ratchet brain/memory surfaces without flattening contradictions | Decision experts, Systems voice | Counts only with contradiction-preserving summary and source refs. |
| `brain-delta-consolidation` | consolidate accepted loop findings into small memory deltas | Follow-Up compile gate after acceptance | Counts only after the compile gate accepts the underlying finding. |
| `tribunal` | independent multi-model comparison | Decision or Failure child, never as controller synthesis | Counts only with distinct model receipts and disagreement summary. |
| `cdo` | multi-agent deliberation pattern when a route needs broader framing | Decision experts or Failure audit child | Counts only when route-specific receipts remain separate from synthesis. |

Skills with broad side effects, external accounts, publishing, UI/browser
automation, commits, pushes, reminders, or long-running background behavior are
not default Wizard council members. They may be prepared as Follow-Up options
only when the option includes approval boundary, run mode, stop condition, and
verification surface.

## Load Rule

Main Wizard docs name which routes require skills. The active route loads the
local skill before running. Global runtime copies, such as Codex skills under
`~/.codex/skills`, may mirror these skills, but packet-local skills are the
portable source for standalone Wizard.

For substantive Codex-adapter Wizard work, both required skills load:

1. `skills/claude-bridge/SKILL.md`
2. `skills/premortem/SKILL.md`

Premortem provides the future-failure method. Claude Bridge provides external
worker execution and receipt evidence. They are separate obligations.
