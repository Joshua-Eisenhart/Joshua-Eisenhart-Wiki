---
title: Chat Tranche 1 Processing 2026-06-18
created: 2026-06-18
updated: 2026-06-18
type: provenance-processing-ledger
status: candidate/controller-verification-required
claim_ceiling: first bounded Packet 5 tranche; design/provenance classification only; not full chat ledger; not runtime verification
---

# Chat / Transcript Queue — Tranche 1 Processing

## Scope and method

Processed a small bounded first tranche from `/Users/joshuaeisenhart/wiki/projects/leviathan-current/chat-provenance-queue-2026-06-17.md` and `/Users/joshuaeisenhart/wiki/projects/leviathan-current/source-inventory-2026-06-17.json`.

Chosen tranche: queue rows **50-55**, the six `product/design discussion` rows listed as the first tranche in the queue. These are not raw Josh/JP chats. They are repo-resident decision/design artifacts surfaced by chat/transcript/content keywords.

All claims below start from:

```text
asserted in transcript, unverified
```

Promotion is limited to source-supported wiki wording. No runtime commands, package tests, or implementation smokes were run in this pass.

## Candidate metadata

Inventory extraction confirmed these queue rows:

| Queue # | Class | Size | Inventory reason | Exact source path |
|---:|---|---:|---|---|
| 50 | product/design discussion | 4,151 | `content-keyword` | `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md` |
| 51 | product/design discussion | 4,535 | `content-keyword` | `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/designs/agent-adapter-e2e-plan.md` |
| 52 | product/design discussion | 29,535 | `content-keyword` | `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/designs/leviathan-meta-framework.md` |
| 53 | product/design discussion | 42,817 | `content-keyword` | `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/designs/phase-3-jobtype-recognition-architecture.md` |
| 54 | product/design discussion | 32,926 | `content-keyword` | `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/designs/phase-5-agentic-compiler-architecture.md` |
| 55 | product/design discussion | 35,975 | `content-keyword` | `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/designs/phase4-weight-system-architecture.md` |

## Processed claim ledger

### queue-50 — Dogfood as preset / plugin-first decision

| Field | Value |
|---|---|
| `source_id` | `queue-50:.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md` |
| `claim_text` | The decision document says `dogfood` should be treated as a workflow preset/profile on top of graph execution, not a first-class graph primitive, and should ship plugin-first/experiment-first until stable. |
| `claim_type` | `design intent` + `repo evidence reference` |
| `initial_status` | `asserted in transcript, unverified` |
| `repo_match` | Source itself is an accepted `.lev/pm/decisions` artifact at `/Users/joshuaeisenhart/GitHub/leviathan/.lev/pm/decisions/d16-dogfood-is-preset-plugin-first.md`. Current architecture corroborates the plane/plugin boundary: `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` lines 21-27, 51-55, 181-196, and plugin topology/ownership lines 122-180. |
| `matched_authority_level` | `active decision/design provenance`; partial match at `current architecture` for plugin/plane boundary, not for a dogfood CLI implementation. |
| `wiki_allowed_claim` | `Support labels: active decision/design provenance; repo-current architecture. An accepted repo decision records dogfood as intended to be a workflow preset/profile and plugin/experiment-first surface; current architecture supports the broader rule that domain workflows attach as plugins/proposals rather than collapsing into core primitives.` |
| `blocked_overclaim` | Do not say `lev graph exec --preset dogfood` or `lev exec --workflow graph-dogfood` is implemented or current CLI truth without code/test evidence. Do not say dogfood is canonical product surface. |
| `next_action` | If a future page discusses dogfood, search active CLI/plugin code for exact commands before promoting beyond design intent. |

### queue-51 — Agent adapter E2E plan

| Field | Value |
|---|---|
| `source_id` | `queue-51:.lev/pm/designs/agent-adapter-e2e-plan.md` |
| `claim_text` | The plan describes E2E tests for lifecycle hooks, conversation parsing triggers, and an AgentAdapterEventBridge, originally targeting `~/lev/core/agent-adapter`. |
| `claim_type` | `design intent` + `implementation status` |
| `initial_status` | `asserted in transcript, unverified` |
| `repo_match` | Current docs place analogous adapter/hook ownership under `/Users/joshuaeisenhart/GitHub/leviathan/docs/plugins/core-platforms.md`: current features include `IAbstractHooks`, Claude Code hooks, `event-bridge.ts`, `conversation-parser.ts`, and sync pipeline (lines 31-49, 94-143, 176-197). Bounded file search found no active `*agent-adapter*` path outside archive/prior-art files. |
| `matched_authority_level` | `current docs/design` for core-platforms adapter/hook surface; `none found` for active `core/agent-adapter` module. |
| `wiki_allowed_claim` | `Support labels: repo-current docs/design; no current match found. The older agent-adapter plan resembles capabilities now documented under the active core-platforms plugin: platform lifecycle hooks, hook/event bridge, conversation parser, and conversation sync. The specific core/agent-adapter path appears not to be active in the bounded search.` |
| `blocked_overclaim` | Do not claim the planned E2E tests exist under `core/agent-adapter`, or that `AgentAdapterEventBridge` was implemented at that legacy path. Do not claim full test coverage from this plan. |
| `next_action` | For implementation claims, inspect active `plugins/core-platforms/src/platform-hooks/**` and its tests before promotion to code/test-supported. |

### queue-52 — Leviathan meta framework / three pillars

| Field | Value |
|---|---|
| `source_id` | `queue-52:.lev/pm/designs/leviathan-meta-framework.md` |
| `claim_text` | The design frames Leviathan as a three-pillar AI operations stack: CC-Mirror/LLM proxy, Clawdbot gateway, and FlowMind middleware/inference layer. |
| `claim_type` | `product speculation` + `design intent` |
| `initial_status` | `asserted in transcript, unverified` |
| `repo_match` | Current architecture supports Lev as a universal agent runtime using FlowMind, Orchestration, Event Bus, Poly, and plugins: `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` lines 19-27, 41-56, 151-196. Current core-platforms docs list a Clawdbot gateway SDK as live: `/Users/joshuaeisenhart/GitHub/leviathan/docs/plugins/core-platforms.md` lines 31-49 and 133-137. Current roadmap says `lev-gwpy (Gateway)` is done and FlowMind/compiler tracks exist: `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md` lines 67-90. Search found CC-MIRROR/three-pillar matches primarily in `_archive/docs/**`, not current authority docs. |
| `matched_authority_level` | `current architecture` and `current roadmap` for runtime/gateway/FlowMind pieces; `archive/prior art` or `none found` for CC-MIRROR as current pillar. |
| `wiki_allowed_claim` | `Support labels: repo-current architecture; repo-current roadmap/status; archive/prior art. The three-pillar artifact is useful as product/design framing. Current sources support FlowMind as a central control/policy plane and document a Clawdbot gateway SDK/Gateway track. Current authority did not establish CC-MIRROR/LLM proxy as a current implemented pillar in this bounded pass.` |
| `blocked_overclaim` | Do not say Leviathan currently ships one key vault, one memory system, one gateway, CC-MIRROR production routing, or full three-pillar stack implementation based on this design doc. |
| `next_action` | Route to Packet 3/product-surface work if Clawdbot/gateway positioning is needed; search active package/code before any CC-MIRROR claim. |

### queue-53 — Phase 3 JobType recognition design

| Field | Value |
|---|---|
| `source_id` | `queue-53:.lev/pm/designs/phase-3-jobtype-recognition-architecture.md` |
| `claim_text` | The design proposes a JobType recognition system using filesystem signatures, tool usage profiling, clustering, classification, and shard routing. |
| `claim_type` | `design intent` + `implementation status` |
| `initial_status` | `asserted in transcript, unverified` |
| `repo_match` | The active roadmap has unrelated `job_type` references in Poly/job architecture, but bounded search found no active `*jobtype*` files and no `core/jobtype-recognition/**` package. The self-learning spec mentions Weight System Phase 4 as needing numeric signals but does not establish JobType implementation: `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/proposal-memory-self-learning-pipeline.md` lines 56-70. Archive/prior-art roadmap contains Atomic ID/Weight System/JobType references: `/Users/joshuaeisenhart/GitHub/leviathan/_archive/docs/roadmaps/self-learning-os.md`. |
| `matched_authority_level` | `active decision/design provenance`; `archive/prior art`; `none found` for active implementation. |
| `wiki_allowed_claim` | `Support labels: active decision/design provenance; no current match found. The artifact is a detailed design proposal for future JobType recognition and skill shard routing. The bounded pass found no active core/jobtype-recognition package or current code support.` |
| `blocked_overclaim` | Do not claim JobType recognition, clustering, shard router, `lev jobtype` CLI, or `core/jobtype-recognition` exists as current implementation. Do not import the >80% accuracy target as an achieved metric. |
| `next_action` | Keep as design intent. If Packet 6 needs self-learning roadmap context, cite with design/provenance label and verify against current roadmap first. |

### queue-54 — Phase 5 agentic compiler / process mining design

| Field | Value |
|---|---|
| `source_id` | `queue-54:.lev/pm/designs/phase-5-agentic-compiler-architecture.md` |
| `claim_text` | The design proposes transforming execution traces into reusable FlowMind workflows using a process-mining engine, conformance checker, hotspot detector, lesson generator, router rule compiler, and provenance linking. |
| `claim_type` | `design intent` + `implementation status` |
| `initial_status` | `asserted in transcript, unverified` |
| `repo_match` | Current roadmap supports that FlowMind session engine and Graph Blueprint IR have shipped, while FlowMind program-driven loop and topology enforcement remain in progress/partial: `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md` lines 91-106 and 112-127. Bounded search found no active `*process*mining*` files and PM4Py/process-mining matches only in archive/prior-art. Current architecture supports FlowMind/Orchestration/Graph/Event Bus boundaries: `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md` lines 181-196. |
| `matched_authority_level` | `current roadmap` for adjacent FlowMind status; `current architecture` for plane boundaries; `none found` for process-mining implementation. |
| `wiki_allowed_claim` | `Support labels: repo-current roadmap/status; repo-current architecture; no current match found. The artifact is a future-looking design for agentic compiler/process-mining capabilities layered on FlowMind traces. Current roadmap supports adjacent FlowMind progress but not PM4Py/process-mining implementation.` |
| `blocked_overclaim` | Do not claim PM4Py, Inductive Miner, conformance checking, hotspot detection, lesson generation, or router rule compilation exists in current code. Do not preserve the January bug/test-coverage assertions as current truth without fresh source verification. |
| `next_action` | If compiler status is needed, cite current ROADMAP and active FlowMind code/tests instead of this design. Treat this file as design pressure only. |

### queue-55 — Phase 4 weight system design

| Field | Value |
|---|---|
| `source_id` | `queue-55:.lev/pm/designs/phase4-weight-system-architecture.md` |
| `claim_text` | The design proposes stable Atomic IDs, JobType × AtomicID weight tables, outcome recording, weight policies, CLI commands, and skill-selection ranking. |
| `claim_type` | `design intent` + `implementation status` |
| `initial_status` | `asserted in transcript, unverified` |
| `repo_match` | Current self-learning spec says Weight System Phase 4 needs numeric signals and rejects deferring those signals: `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/proposal-memory-self-learning-pipeline.md` lines 56-70. It also defines transcript-to-triplet/reward/proposal architecture and requirements in lines 73-118, 123-170, 218-307. Bounded file search found no active `core/weights/**`, no weight CLI files, and only one unrelated `*weight*` stress test under `plugins/evolve-memory/tests/stress/LH-02-cached-token-weight.ts`. Archive roadmap includes Atomic ID and Weight System tasks. |
| `matched_authority_level` | `current spec` for self-learning numeric-signal need; `archive/prior art` for older roadmap; `none found` for weight-system implementation. |
| `wiki_allowed_claim` | `Support labels: repo-current contract; no current match found. Current self-learning spec recognizes the need for numeric signals related to a Weight System, while the phase4 design is a detailed proposed architecture. The bounded pass found no active implementation of the proposed weight table/CLI package.` |
| `blocked_overclaim` | Do not claim `lev weights show/update`, SQLite weight tables, Atomic ID registry, outcome-to-weight aggregation, or skill-selection ranker is implemented. Do not state retry-rate reduction or latency targets as achieved. |
| `next_action` | Preserve as self-learning/weight-system design intent. For current status, cite `docs/specs/proposal-memory-self-learning-pipeline.md` and search active memory/telemetry code before promotion. |

## Tranche outcome

- Candidates processed: 6.
- Promoted to current implementation truth: 0.
- Promoted to current doc-supported architecture/status only: limited pieces of queue-50, queue-51, queue-52, queue-54, queue-55.
- Kept as design/provenance intent: all 6.
- Explicitly blocked overclaims: dogfood CLI implementation; legacy `core/agent-adapter` implementation; three-pillar/CC-MIRROR production claims; JobType recognition implementation; PM4Py/process-mining implementation; Weight System/CLI implementation.

## Controller verification needs

- Verify whether `.lev/pm/decisions/**` should be treated as stronger than `active decision/design provenance` for accepted ADRs.
- If future synthesis needs any of these claims, rerun targeted code/test checks in active paths before using implementation language.
- Confirm that no sensitive transcript/log/config content was imported; this tranche used design/decision docs only.
