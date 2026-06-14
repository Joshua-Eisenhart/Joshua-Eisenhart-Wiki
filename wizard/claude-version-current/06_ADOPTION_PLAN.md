---
title: Claude Code Wizard — Adoption Plan
type: adoption_plan
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Adoption Plan

Low-coupling path from docs to wired, conformance-proved, pointer-adopted Claude Code Wizard.

---

## Phase 0 — Docs only

**Status: completed 2026-06-13.**

Create the Claude-native folder; remove the 6 Hermes byte-identical copies; author the core Claude-native docs. Do not change any live `.claude/skills/` or `.claude/agents/` surface.

Pass conditions:
- `claude-version-current/` folder exists with at least the 5 native docs (README, 00, 01, 02, 16) plus MANIFEST, 03, 05, 06, sources/SOURCE_MAP.md authored this session.
- 6 Hermes copies deleted; MANIFEST records which were deleted and where the source lives.
- No edits to `~/.claude/CLAUDE.md`, project `CLAUDE.md`/`AGENTS.md`, `.claude/skills/`, or `.claude/agents/`.
- v4.2 split-brain risk recorded as OPEN in MANIFEST (done; see below).

Stop conditions:
- If any of the 5 native docs require rewriting to make the folder coherent, stop Phase 0 and repair first.
- If the hermes-version-current/ source is unavailable or unreadable, halt and note.

---

## Phase 1 — Retool and wire conformance surfaces

**Status: not started.**

Write the Claude-native schemas, templates, conformance validator, and a smoke topology with both POSITIVE and NEGATIVE fixtures.

Deliverables:
- `schemas/CLAUDE_WIZARD_RECEIPT_SCHEMA.md` — Claude action_class set; no `spawn_worker`.
- `templates/task-card.yaml` — `spawn_subagent` vocabulary, `runtime_target: claude_code`.
- `templates/worker-receipt.yaml` — Claude receipt fields including `linked_agent_receipt` for `spawn_subagent` claims.
- `conformance/validate_claude_wizard_run.py` — load-bearing validator (not decorative; see acceptance criteria below).
- `conformance/VALIDATION_CHECKLIST.md` — human-readable checklist in Claude vocabulary.
- `runs/SMOKE_TOPOLOGY_<date>/` — one POSITIVE fixture that PASSES, plus ≥3 NEGATIVE fixtures that FAIL:
  - (a) Hermes tools in receipts (`spawn_worker` / `delegate_task` action_class) — must REJECT.
  - (b) Opt-in gate violation: wizard structure present but no trigger declared — must REJECT.
  - (c) `spawn_subagent` claimed with no linked `Agent` receipt — must REJECT.

Validator acceptance criteria (must not be decorative):
- Checks action_class ∈ `{controller_local, tool_run, spawn_subagent, enqueue_runner, blocked, deferred, not_run, superseded}`; rejects any other value (including `spawn_worker`, `delegate_task`).
- Checks provenance: a `spawn_subagent` receipt must have a `linked_agent_receipt` field referencing a real artifact path or Agent receipt id.
- Checks topology linkage: Follow-Up receipt must reference Decision and Failure receipts by id or path (not merely sequential naming).
- Checks that at least one route went `blocked` or `deferred` (the failure path exercise).
- Checks that at least one `superseded` transition is recorded.
- Checks opt-in gate on the run artifact (was a wizard run declared + trigger present); states in the validator and checklist that a pure-Python validator cannot classify raw prompt text as "ordinary vs wizard" — it checks the RUN ARTIFACT, not the prompt.
- Checks honest status labels: rejects `verified`/`confirmed`/`all pass` without an explicit criterion citation.
- Checks bottom-line-first: the rendered output's first non-blank, non-header line is the bottom line (heuristic, documented as a soft check).

**Validator ceiling (must be stated in the validator's own output and in `conformance/VALIDATION_CHECKLIST.md`):** the validator checks artifact shape and internal consistency only. It cannot verify that a Wizard actually ran. Cross-run-replay forgeability — assembling an internally-consistent file set from real fragments of prior runs — is a known, accepted limit of pure on-disk validation. A passing validator run is `shape+consistency-checked`, not `runtime-proved`. See OPEN item below.

Pass conditions:
- POSITIVE fixture: `validate_claude_wizard_run.py` exits 0.
- All ≥3 NEGATIVE fixtures: `validate_claude_wizard_run.py` exits nonzero and names the violation.
- Validator is run in this session and the output is recorded in `runs/SMOKE_TOPOLOGY_<date>/validator_receipt.txt`.

Stop conditions:
- If the validator can only do field-presence checks (no provenance, no topology linkage), it is decorative. Halt and rebuild.
- If the smoke topology only exercises the clean-accept path (no blocked/deferred, no superseded), it does not satisfy the panel revision requirement. Halt and add the failure path.
- If the validator's output or checklist does not state the forgery-ceiling explicitly, halt and add it before declaring Phase 1 done.

Named OPEN item — validator forgery ceiling / runtime proof:
- The Phase 1 validator checks artifact shape and internal consistency. It cannot verify that a Wizard actually ran.
- Cross-run-replay forgeability (internally-consistent file sets assembled from prior-run fragments, passing the validator without any live Wizard run) is an **accepted limit** of this tier. It is not a Phase 1 bug; it is a ceiling to state honestly.
- Genuine runtime proof would require binding to un-forgeable execution evidence: the harness's own `TaskOutput` or session transcript, which the artifact-assembling parent cannot fabricate post-hoc.
- **Status: OPEN. This is a larger design, deferred past Phase 4.** Do not claim runtime proof from a passing validator run; the honest label is `shape+consistency-checked`.

---

## Phase 2 — Dry-run

**Status: not started. Depends on Phase 1 completion.**

Run a real (not smoke-fixture) bounded Wizard turn using Claude Code tools: one Decision council `Agent` fan-out, one Failure council check, one Follow-Up rendering. At least one route `blocked` or `deferred` with a reason.

Pass conditions:
- Every visible route has a receipt, or explicit `blocked`/`deferred`/`not_run` with reason.
- Follow-up entries rendered as `future_choice`, not preworked branches.
- Builder agent did not audit its own output (fresh-context auditor ran or the audit was explicitly `not_run` with reason).
- No Hermes action_class appears in any receipt.
- Honest status labels throughout.

Stop conditions:
- If any follow-up is rendered as completed without a separate authorized execution, retreat and re-render as `future_choice`.
- If the council collapsed two live surviving candidates into one without evidence, name the surviving split and halt.

---

## Phase 3 — Conformance

**Status: not started. Depends on Phase 2 completion.**

Run the validator against the dry-run receipts. Add edge-case negative fixtures if any new failure mode surfaced in Phase 2.

Named gate item — v4.2 / v4.3 split-brain risk:
- The `wizard-council` skill and `~/.claude/agents/wizard/*.md` agents currently load `packet-v4-2-current` MMM paths.
- A Phase 3 conformance run validates the v4.3 schema in THIS folder.
- These two things are independent: the conformance validator can PASS while a real council invoked through the live skills loads v4.2 MMM paths and may produce v4.2-shaped receipts.
- **This gate item is OPEN.** Before Phase 3 is declared complete, the owner must either: (a) confirm v4.2 is intentional for the live skills (document as accepted divergence), or (b) update the live skills to v4.3 MMM paths and re-run.
- Do not assert this gate is resolved; it requires an owner decision.

Pass conditions:
- `validate_claude_wizard_run.py` passes against the Phase 2 dry-run receipts.
- v4.2/v4.3 split-brain gate is either acknowledged as accepted divergence or resolved.
- No new field-presence-only checks were added to make the validator pass (decorative expansion = stop).
- Validator forgery ceiling is stated in the validator output and checklist (see OPEN item in Phase 1); passing the validator is NOT claimed as runtime proof.
- Any Phase 3 summary report uses the label `shape+consistency-checked`, not `runtime-proved` or `verified`.

Stop conditions:
- Any regression in validator behavior from Phase 1 fixtures.
- v4.2 gate still unresolved and owner has not been consulted.

---

## Phase 4 — Pointer adopted

**Status: not started. Depends on Phase 3 completion.**

Wire this folder as the reference for the relevant `.claude/skills/`: `wizard`, `wizard-council`, `wizard-v43`, `sim-wizard`, `claude-wizard-loop-engineering`. Add a pointer to this folder from the skills, not a content dump.

Pointer form (do not add packet details to the skill body):
```
Claude Wizard v4.3 native adaptation lives in ~/wiki/wizard/claude-version-current/.
Load through the wizard skill when explicitly requested or when route-truth/follow-up-runtime work is admitted.
```

Pass conditions:
- Skills updated to reference this folder.
- Version binding (v4.3) explicit in each skill's header or pointer.
- `wizard-council` v4.2 question resolved at Phase 3 (see above).
- `16_CLAUDE_WIZARD_MAINTENANCE_GOVERNOR.md` is reachable from the skill chain.
- No skill body contains a full packet dump.

Stop conditions:
- If the folder is still `drafted` (not `reviewed` or `proved`), do not promote the pointer.
- If the v4.2 split-brain gate is unresolved, do not wire `wizard-council` to this pointer.
- If wiring requires rewriting `~/.claude/CLAUDE.md` kernel rules, halt and consult the owner.

---

## Global stop conditions (apply to any phase)

- Folder starts duplicating `~/.claude/CLAUDE.md` or project `CLAUDE.md`.
- Every answer starts running Wizard ceremony without being invoked (opt-in violated).
- Memory/session summaries are treated as current execution proof.
- Follow-up prework is claimed without scout/audit receipts.
- User-facing output becomes harder to read than plain answers.
