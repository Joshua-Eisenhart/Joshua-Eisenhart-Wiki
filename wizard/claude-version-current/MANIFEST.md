---
title: Claude Code Wizard Version — Manifest
type: manifest
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Manifest

## Status labels used in this folder

| Label | Meaning |
|---|---|
| `exists` | File is present and has coherent content |
| `drafted` | Written this session; has not been pressure-tested in a live run |
| `reviewed` | Controller re-read and corrected against sources |
| `proved` | A bounded runtime proof used it successfully and the receipt is on disk |
| `adopted` | The matching skill or pointer was intentionally promoted to the live `.claude/skills/` surface |
| `source-only` | Retained as provenance/reference; does not govern current Claude Code behavior |

Current folder status: `drafted`.

---

## Files

### Claude-native docs (KEEP, may extend)

| File | Status | Notes |
|---|---|---|
| `README.md` | `exists` | Front door; read order; provenance; open adoption items |
| `00_READ_FIRST.md` | `exists` | Authority boundary, opt-in rule, working rule, read-on-entry contract |
| `01_RUNTIME_CONTRACT.md` | `exists` | Decision/Failure/Follow-Up topology, action classes, compile gate, output rule |
| `02_TOOL_ADVANTAGE_MAP.md` | `exists` | Claude Code tools mapped to Wizard jobs; anti-theater rule |
| `16_CLAUDE_WIZARD_MAINTENANCE_GOVERNOR.md` | `exists` | Maintenance loop, subagent ledger contract, worker routing |

### Authored this session

| File | Status | Notes |
|---|---|---|
| `MANIFEST.md` (this file) | `drafted` | Inventory with status labels; open questions recorded |
| `03_MMM_LOADING_PROCEDURE.md` | `drafted` | Token-budget + eviction protocol, COMPACT-first default, child-Agent prompt template |
| `05_SOURCE_AND_LIFT_BOUNDARY.md` | `drafted` | Source / lift / execution / proof definitions + label-strip test |
| `06_ADOPTION_PLAN.md` | `drafted` | Phase-gated Phase0→4, pass/stop conditions, v4.2 split-brain risk as named gate item |
| `sources/SOURCE_MAP.md` | `drafted` | Origin of every imported concept |

### Schemas, conformance, templates

| File | Status | Notes |
|---|---|---|
| `schemas/CLAUDE_WIZARD_RECEIPT_SCHEMA.md` | `drafted` | Claude action_class + runtime_target set; parent/child/management receipt fields; invalid pattern catalogue; written 2026-06-13 |
| `templates/task-card.yaml` | `drafted` | Claude-native task-card (spawn_subagent, Agent, Skill, Bash, etc.); written 2026-06-13 |
| `templates/worker-receipt.yaml` | `drafted` | Claude-native worker receipt; written 2026-06-13 |
| `conformance/validate_claude_wizard_run.py` | `drafted` | Shape + internal-consistency validator (NOT runtime proof). Checks action-class vocabulary, spawn_subagent parent-linkage provenance, Follow-Up input-id provenance, reason-per-route failure path, bottom-line-first position, opt-in gate. Passes the positive smoke fixture and rejects NEG1–NEG6. **Ceiling: the validator checks artifact shape and internal consistency only. It cannot verify that a Wizard actually ran. A forged but internally-consistent file set (cross-run-replay) passes this validator. Genuine runtime proof would require binding to un-forgeable execution evidence — see OPEN item in `06_ADOPTION_PLAN.md`.** Not yet exercised by a live council run; still `drafted`. |
| `conformance/VALIDATION_CHECKLIST.md` | `drafted` | Human-readable conformance checklist, Claude vocabulary; written 2026-06-13 |

### Deleted (Hermes byte-identical copies removed 2026-06-13)

Per PANEL REVISION 1: the 6 Hermes copies were plain-`rm`-deleted (not `git rm`; no git commands run). Git history retains them; `hermes-version-current/` is the live source. The adaptation dir must be strictly Claude-native.

| Deleted file | Source location |
|---|---|
| `conformance/validate_hermes_wizard_run.py` | `../hermes-version-current/conformance/validate_hermes_wizard_run.py` |
| `conformance/validate_hermes_wizard_wide_run.py` | `../hermes-version-current/conformance/validate_hermes_wizard_wide_run.py` |
| `conformance/VALIDATION_CHECKLIST.md` | `../hermes-version-current/conformance/VALIDATION_CHECKLIST.md` |
| `schemas/HERMES_WIZARD_RECEIPT_SCHEMA.md` | `../hermes-version-current/schemas/HERMES_WIZARD_RECEIPT_SCHEMA.md` |
| `templates/task-card.yaml` | `../hermes-version-current/templates/task-card.yaml` |
| `templates/worker-receipt.yaml` | `../hermes-version-current/templates/worker-receipt.yaml` |

---

## Shared packet reference (do not duplicate)

`../packet-v4-3-current/` is the authoritative v4.3 core. Files here REFERENCE it; they do not copy it.

Key packet files:
- `../packet-v4-3-current/WIZARD_v4_3.md` — council topology, MMM contract, output contracts
- `../packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` — compact MMM (COMPACT-first default)
- `../packet-v4-3-current/mmm/FULL_MMM_v4_3.md` — full MMM (~36k lines; load only when budget allows)
- `../packet-v4-3-current/mmm/mini/` — per-role mini-MMMs
- `../packet-v4-3-current/schemas/WIZARD_V4_3_RECEIPT_SCHEMA.md` — portable receipt schema (runtime: claude_code already supported)
- `../packet-v4-3-current/conformance/validate_v4_3_packet.py` — packet-level validator

---

## OPEN QUESTION — v4.2 / v4.3 split-brain risk

The `wizard-council` skill and the 9 `voice-*.md` agents at `~/.claude/agents/wizard/` currently load `packet-v4-2-current` MMM paths. The v4.3 files exist byte-ready in `packet-v4-3-current`. The maintenance governor (`16_CLAUDE_WIZARD_MAINTENANCE_GOVERNOR.md`) flags the v4.2 council shape as POSSIBLY intentional.

**Status: OPEN. Do not resolve without owner decision.**

Consequence: a conformance run that validates against the v4.3 schema (this folder) will PASS while a real council run invoked through the skills would load v4.2 MMM paths — shape mismatch is possible. This risk is named in `06_ADOPTION_PLAN.md` as a Phase 3 gate item.

---

## Non-goals

- No full universal packet copy
- No default high-fanout behavior (Wizard is opt-in, not always-on)
- No global `~/.claude/CLAUDE.md` or project `CLAUDE.md` rewrite
- No pretending memory/session recall is current execution evidence
- No git commands
