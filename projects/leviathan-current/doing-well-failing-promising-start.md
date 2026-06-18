---
title: Leviathan Doing Well Failing Promising Start
created: 2026-06-17
type: assessment
status: starter assessment / needs deeper packet verification
claim_ceiling: first-pass assessment from current docs, inventory, and starter scans; not final verdict
---

# Leviathan — Doing Well, Failing, Promising — Start

> Supersession note, 2026-06-18: the row saying the current repo has unresolved conflict markers is now historical damaged-checkout evidence. The clean snapshot `c90ec8499c83db3d17f6132ec734698a8de2dbce` had no `<<<<<<<`/`>>>>>>>` scan hits. Keep the broader assessment, but route current-health claims through [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].

## Claim ceiling

This is a first-pass assessment for wiki routing. It is grounded in current repo docs already read, package/module starter scans, source inventory, and conflict-marker scans. It is not a final model review and it has not run the full test/build suite.

## Doing well now

| area | support | why it matters |
|---|---|---|
| Clear architecture planes | observed docs: `docs/ARCHITECTURE.md`, specs | FlowMind / Orchestration / Graph / Event Bus separation gives the project a real runtime shape instead of one giant agent blob. |
| Strong north-star framing | observed docs: `docs/NORTH_STAR.md` | The project knows it wants governed agent-human execution, not mere chat. |
| Broad package/module surface | observed manifests and module scan | The repo has concrete package boundaries for `flowmind`, `orchestration`, `graph`, `event-bus`, `exec`, `poly`, `daemon`, and `domain`. |
| Constraint vocabulary is explicit | observed docs/search signals | Finitude, non-commutation, ratchet, locality, nominalized artifacts, leases, and scope appear as first-class concepts. |
| Human-loop/governance instincts are strong | observed docs/specs | AgentPing/AgentLease/policy/event traces point at the right failure mode: agents need bounded authority and receipts. |

## Failing or weak now

| issue | support | why it matters |
|---|---|---|
| Architecture is ahead of implementation | roadmap/design intent + worker reads | Docs themselves preserve gaps around universal graph, enterprise readiness, protocol coverage, security, and release hardening. |
| Current repo has unresolved conflict markers | observed file scan | Conflict markers block trust in build/runtime health. Found: `.lev/pm/handoffs/20260307-marketplace-gtm-bundle-sprint.md`, `crates/lev-tui-theme/src/lib.rs`, `crates/lev-tui-widgets/src/attention_kanban.rs`, `core/event-bus/src/index.ts`, `core/event-bus/src/context/pr.ts`, `core/event-bus/src/bridge/index.ts`, `core/event-bus/src/events/scm.ts`. |
| High entropy / legacy bulk | observed inventory | `_archive`, `workshop`, `.lev`, reports, and chats/handoffs are large; without provenance fencing, a reader will confuse prior art, logs, design intent, and current code. |
| Contribution provenance is not yet separated | observed need + signal scan | Josh doctrine, JP implementation, assistant elaboration, and repo-current enforcement must be split before attribution or explanation is honest. |
| Specs are contract-heavy but not all verified | observed authority-doc worker | Specs help, but docs/spec labels and implementation status need file/test matching before stronger claims. |

## Promising

| promise | support | condition for promotion |
|---|---|---|
| Governed agent runtime | observed/inferred docs | Promote only when event traces, policies, approvals/leases, and execution paths are verified end-to-end. |
| Constraint runtime translation of Josh's roots | signal scan + existing bridge | Promote only after source quote/provenance rows and current-code enforcement rows exist. |
| Graph memory/context engineering | observed module/docs | Promote after graph APIs, persistence, projection, and retrieval behaviors are tested or code-read deeply. |
| Event-sourced agent audit | observed event-bus docs/module | Promote after conflict markers are resolved and event emission/replay tests pass. |
| Human-loop surfaces | observed AgentPing/AgentLease docs/specs | Promote after implemented surfaces are separated from roadmap/product language. |

## Dangerous overclaims to block

- `Leviathan fully implements Josh's model` — open, not proven.
- `Leviathan is enterprise-ready` — contradicted by roadmap/hardening gaps.
- `All chat-processed ideas are current repo truth` — false evidence class.
- `Codex Ratchet and Leviathan are the same object` — category collapse.
- `Architecture docs prove runtime behavior` — not enough; code/tests required.

## Decisive next checks

1. Run a safe build/test inventory: package manager, scripts, which tests exist, and whether a no-mutation test pass is feasible.
2. Create `josh-root-constraints-in-leviathan.md` with quote/provenance rows, not just keyword hits.
3. Deep-read `core/event-bus` after resolving or at least isolating conflict-marker files.
4. Deep-read FlowMind compiler/kernel surfaces and match constraint declarations to runtime enforcement.
5. Process the top chat/provenance tranche with speaker/source classification.

## Current verdict

Leviathan is most promising where it treats agents as bounded actors inside a governed runtime: policy, graph context, event receipts, leases/approvals, and surfaces. It is weakest where the repo's huge archive/chat/design mass can make the project sound more complete than current code/tests support. The right wiki has to be both explanatory and adversarial: explain the vision, but keep every claim on its earned evidence rung.
