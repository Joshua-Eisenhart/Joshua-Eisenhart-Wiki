---
title: Claude Code Wizard — Source and Lift Boundary
type: boundary
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Source and Lift Boundary

This file prevents the primary failure mode: importing the general Wizard packet or the Hermes adaptation and mistaking that import for a Claude Code native runtime.

## Definitions

- **source**: a file, tool output, memory entry, session summary, receipt, or subagent result that was read in the current run. A source is evidence of what was said or written somewhere; it is not proof of current execution.
- **lift**: the design move extracted from a source and adapted for Claude Code use. A lift must name what changed in adaptation — a copied path is not a lift.
- **execution**: a current tool action, `Agent` subagent call, `Bash` invocation, or `Skill` run that actually occurred in this session and returned a receipt.
- **proof**: a receipt (tool output, result-JSON, `Agent` final message, file read-back) plus controller re-read that supports a scoped and bounded claim. Proof has a ceiling — it supports only what the receipt says within the scope it was run.

These four terms are not synonyms and must not be conflated. Memory recall is a source, not execution. A subagent summary is pressure on a claim, not proof of the claim until the artifact is controller-visible.

---

## Rules

1. A source can inspire a Claude Code mechanism. It does not prove the mechanism runs in Claude Code.
2. A lift must name what changed when adapted to Claude Code. A copied packet path is not a Claude Code native route.
3. Hermes surfaces (`delegate_task`, `cronjob`, `HERMES.md`/`SOUL.md`, `gateway`, `spawn_worker`) are sources, not Claude Code mechanisms. The `02_TOOL_ADVANTAGE_MAP.md` records the lifted equivalents.
4. Style transfer is not runtime integration. Formatting a response to look like a Wizard run does not produce a Wizard run.
5. Memory/session recall can locate prior decisions; it cannot prove current file state or current execution.
6. A subagent summary can suggest a change. Controller verification (artifact read-back, `TaskOutput`, result-JSON) decides adoption.
7. A skill procedure loaded via the `Skill` tool is a procedure, not proof that a run happened. A run requires a receipt.

---

## Validator ceiling — forgeability accepted limit

The conformance validator (`conformance/validate_claude_wizard_run.py`) checks artifact **shape** and **internal consistency**. It does NOT verify that a Wizard actually ran.

**Why this matters:** a pure on-disk artifact validator cannot be a runtime proof. A forger who knows the schema can produce a cross-run-replay — a file set assembled from real fragments of prior runs, internally consistent, that passes all field-presence and provenance-linkage checks — without any Wizard run having occurred this session. The validator will pass it.

**Accepted limit:** cross-run-replay forgeability is a known, accepted limit of this validation tier. It is not a bug to fix now; it is a ceiling to state honestly.

**What honest shape-checking does buy:** it excludes structurally malformed artifacts, wrong action_class vocabularies, missing provenance fields, and trivially inconsistent topologies. These exclusions are real value at low cost. They are not runtime proof.

**What genuine runtime proof would require:** binding to un-forgeable execution evidence — specifically, the harness's own TaskOutput or session transcript, which the artifact-assembling parent cannot fabricate post-hoc. That design is larger and is recorded as an OPEN item in `06_ADOPTION_PLAN.md`.

**Label consequence:** the validator's output status is `shape+consistency-checked`, not `runtime-proved`. Any claim that a run is genuine must cite a separate receipt from a real tool invocation (TaskOutput, Agent final message, Bash stdout) — not just a passing validator run.

---

## Required source-and-lift fields

For each mechanism imported from the general packet or from `hermes-version-current/`:

```yaml
source_file: <path>
source_role: <what the file does in its original system>
source_mechanism: <the specific behavior being adapted>
claude_code_lift: <the Claude Code equivalent behavior>
what_changed: <concrete delta — tool name, action_class, authority surface, etc.>
what_remains_unproved: <what this lift does not yet demonstrate in a live run>
adoption_status: proposed | drafted | proved | adopted | rejected
```

---

## Label-strip test

Remove all Wizard vocabulary: Wizard, Council, Hume, Feynman, Orwell, Popper, Zhuangzi, Factory, Strategy, Systems, MMM, lane, voice, parent, management parent, Max Assembly, Full, auto.

If the remaining behavior does not have all five of:

1. a bounded target (what is being worked on, explicitly named);
2. a current evidence path (a tool ran, a file was read, a receipt exists);
3. a success check (what "done" looks like, checkable without asking the author);
4. a stop condition (when to retreat or block without completing);
5. a next move (the concrete immediate action that follows);

— then it was decorative lift, not a real Claude Code mechanism.

Apply this test to any route before claiming it ran. Apply it to any follow-up before claiming it was pre-run.

---

## Copy-rejection test

Reject an import when it depends on:

- Hermes native `delegate_task` or `spawn_worker` proof (Claude Code uses `Agent`; the receipt shape differs);
- `spawn_worker` action_class (not in Claude Code's admitted set; must be `spawn_subagent`);
- Codex Ratchet sim stage gates for non-Codex-Ratchet work;
- a fixed external model-family quorum (grok+gemini+codex as required quorum is a Hermes convention, not a Claude Code invariant);
- v4.1 or v4.2 packet paths as current authority (current binding is v4.3 via `../packet-v4-3-current/`);
- HERMES.md / SOUL.md as Claude Code authority surfaces (Claude Code authority surfaces are `~/.claude/CLAUDE.md`, project `CLAUDE.md`/`AGENTS.md`, `~/wiki/claude-memory/`, skills — named in `00_READ_FIRST.md`);
- high-fanout stress capacity as default behavior (Claude Wizard is opt-in, not always-on).

---

## Adoption status for this folder's key mechanisms

| Mechanism | Source | Lift | Status |
|---|---|---|---|
| Decision/Failure/Follow-Up barriers | `packet-v4-3-current/WIZARD_v4_3.md` | Preserved; `Agent` fan-out replaces `delegate_task` | `drafted` |
| action_class set | `packet-v4-3-current/schemas/WIZARD_V4_3_RECEIPT_SCHEMA.md` | Used as-is; `spawn_worker` excluded | `drafted` |
| MMM token-budget + COMPACT-first | panel revision 4 + COMPACT/FULL MMM files | `03_MMM_LOADING_PROCEDURE.md` | `drafted` |
| Opt-in gate | `~/.claude/CLAUDE.md` | Inherited; this folder governs only when Wizard invoked | `adopted` |
| Honest status labels | `~/.claude/CLAUDE.md` kernel + `01_RUNTIME_CONTRACT.md` | Preserved in output rule | `adopted` |
| Subagent ledger contract | `hermes-version-current/16_*` | Adapted to `Agent` + `TaskOutput` vocabulary | `drafted` |
| Compile gate | `hermes-version-current/01_*` + `packet-v4-3-current/` | Adapted; see `01_RUNTIME_CONTRACT.md` | `drafted` |
| Conformance validator | `hermes-version-current/conformance/` | Rewritten Claude-native (`conformance/validate_claude_wizard_run.py`); checks artifact shape + internal consistency, NOT runtime proof. Cross-run-replay forgeability is an accepted limit of pure on-disk validation. Genuine runtime proof requires binding to un-forgeable execution evidence (TaskOutput/transcript the parent cannot fabricate) — recorded as OPEN in `06_ADOPTION_PLAN.md`. | `drafted` |
