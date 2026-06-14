---
title: Claude Code Wizard — Source Map
type: source_map
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Source Map

Records where every imported concept in `claude-version-current/` came from. Proves that sources were consulted; does not prove runtime adoption.

---

## Claude Code authority surfaces (primary — not imported, inherited)

| Surface | Role |
|---|---|
| `~/.claude/CLAUDE.md` | Global control law: bottom-line-first output, honest status labels, kernel anti-collapse rules, opt-in Wizard gate, human-offload rules |
| `<repo>/CLAUDE.md` (Codex-Ratchet) | Project law: stage gates, status ladder, sim requirements, coupling program order |
| `<repo>/AGENTS.md` | Codex authority (Claude reads as reference) |
| `~/wiki/claude-memory/` | Claude-owned cross-thread working memory and handoff |
| `.claude/skills/` | Executable procedures (wizard, wizard-council, wizard-v43, sim-wizard, three-engine-sim, premortem, etc.) |

These surfaces are not imported into `claude-version-current/`. They are the authority above this folder. This folder is subordinate to them until `adopted` status (Phase 4 of the adoption plan).

---

## Shared v4.3 packet (reference — not duplicated)

| File | Concepts imported |
|---|---|
| `../packet-v4-3-current/WIZARD_v4_3.md` | Decision/Failure/Follow-Up council topology; 9 parents; management parents; MMM contract; sim/proof overlay; visible-output contract |
| `../packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` | Compact MMM positive reservoir; COMPACT-first default; saliency patch on output language |
| `../packet-v4-3-current/mmm/FULL_MMM_v4_3.md` | Full MMM reservoir; size reference (~36k lines) for token-budget calculations; FULL-only-if-budget rule |
| `../packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` | Mini-MMM registry structure; per-role assignment convention |
| `../packet-v4-3-current/mmm/mini/compact/` + `full/` | Per-role mini-MMM files (voices, lanes, checks, compositions, system_routes, controller_acts) |
| `../packet-v4-3-current/schemas/WIZARD_V4_3_RECEIPT_SCHEMA.md` | Portable receipt schema; `action_class` set; `runtime: claude_code` field; evidence_boundary and success_check fields |
| `../packet-v4-3-current/conformance/validate_v4_3_packet.py` | Packet-level validator reference; conformance bar for receipt fields |
| `../packet-v4-3-current/templates/LLM_ADAPTATION_TEMPLATE.md` | Completeness template for LLM-specific adaptation (used as a check, not copied verbatim) |

---

## Hermes adaptation (reference adapter — not Claude authority)

`../hermes-version-current/` is the completeness reference, not Claude authority. Hermes concepts were lifted (not copied) into Claude-native equivalents.

| Hermes source file | Concept lifted | Claude Code equivalent | What changed |
|---|---|---|---|
| `hermes-version-current/README.md` | Folder front door; read order; provenance | `README.md` | Hermes tools/authority surfaces replaced with Claude Code equivalents; opt-in gate added |
| `hermes-version-current/00_READ_FIRST.md` | Authority boundary; boot contract; read-on-entry/write-on-exit loop | `00_READ_FIRST.md` | `HERMES.md`/`SOUL.md` → `~/.claude/CLAUDE.md`; always-on → opt-in |
| `hermes-version-current/01_RUNTIME_CONTRACT.md` | Runtime contract; compile gate; synthesis non-merge rule; output rule | `01_RUNTIME_CONTRACT.md` | `delegate_task` → `Agent`; `spawn_worker` → `spawn_subagent`; Hermes gateway → `CronCreate`/`/loop` |
| `hermes-version-current/02_TOOL_ADVANTAGE_MAP.md` | Tool-to-job mapping; tool-first rule; anti-theater rule | `02_TOOL_ADVANTAGE_MAP.md` | All Hermes tools replaced with Claude Code tool set; authority surfaces updated |
| `hermes-version-current/16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md` | Maintenance loop; subagent ledger contract; worker routing | `16_CLAUDE_WIZARD_MAINTENANCE_GOVERNOR.md` | Hermes-specific workers → Claude-specific (codex2, Claude Agent, Sonnet mass-use authorization) |
| `hermes-version-current/05_SOURCE_AND_LIFT_BOUNDARY.md` | Source/lift/execution/proof definitions; label-strip test; copy-rejection test | `05_SOURCE_AND_LIFT_BOUNDARY.md` | Hermes surfaces in copy-rejection test replaced with Claude Code; adoption status table added |
| `hermes-version-current/06_ADOPTION_PLAN.md` | Phase-gated adoption plan structure; pass/stop conditions | `06_ADOPTION_PLAN.md` | All Hermes phase outcomes replaced; v4.2 split-brain risk gate added; Phase 1 load-bearing validator requirement added per panel revision |
| `hermes-version-current/MANIFEST.md` | File inventory structure; status labels | `MANIFEST.md` | Hermes-specific files replaced; deleted-files section added; v4.2 open question section added |

### Hermes concepts explicitly NOT lifted

| Hermes concept | Reason not lifted |
|---|---|
| `delegate_task` action class | Claude Code uses `Agent` tool; the action_class is `spawn_subagent` |
| `spawn_worker` action class | Not in Claude Code admitted action_class set |
| `cronjob` surface | Claude Code uses `CronCreate` / `/loop` / `/schedule` skill |
| `gateway` | No Claude Code equivalent; routing is via `Skill` tool + `~/.claude/agents/` |
| `HERMES.md` / `SOUL.md` as authority | Claude Code authority surfaces: `~/.claude/CLAUDE.md`, project `CLAUDE.md`/`AGENTS.md` |
| Always-on Wizard | Claude Wizard is opt-in; fires only on explicit invocation |
| Fixed external model quorum | grok+gemini+codex quorum is a Hermes convention; Claude uses Sonnet fleet + codex2 + advisory-only grok/gemini per project memory |

---

## Build brief sources

| Source | Concepts |
|---|---|
| `/tmp/wizard_brief.md` | Task scope; PANEL REVISIONS 1–7; file list; delete vs keep decisions; v4.2 open question |
| PANEL REVISION 1 | Delete 6 Hermes copies, not keep-and-deprecate |
| PANEL REVISION 2 | Load-bearing validator requirement; ≥3 negative fixtures; provenance check for spawn_subagent; Follow-Up topology linkage |
| PANEL REVISION 3 | Opt-in gate caveat: pure-Python validator checks run artifacts, not prompt text |
| PANEL REVISION 4 | Token-budget + eviction protocol for MMM; COMPACT-first; FULL only if budget allows; which slices drop first; child-Agent prompt template |
| PANEL REVISION 5 | Smoke topology must exercise failure path (blocked/deferred, superseded transition, honest status ladder) |
| PANEL REVISION 6 | v4.2/v4.3 split-brain risk as named OPEN gate item in MANIFEST and 06_ADOPTION_PLAN |
| PANEL REVISION 7 | No git commands; no files outside claude-version-current/ |

---

## Source status

This source map proves only that these surfaces were consulted or identified during this design pass (2026-06-13). It does not prove runtime adoption. Adoption status is tracked per file in `MANIFEST.md`.
