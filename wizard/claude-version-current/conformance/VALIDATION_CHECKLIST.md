---
title: Claude Code Wizard Validation Checklist
type: conformance_checklist
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# Validation Checklist

A Claude Code Wizard run passes `validate_claude_wizard_run.py` only if these
checks pass. This is the Claude-native checklist; the Hermes original
(`spawn_worker`/`delegate_task`/HERMES.md authority) is replaced, not adapted
in place.

## What the validator operates on (and its limit)

- It validates the **run artifact** (the `runs/<RUN>/` directory of receipts +
  `run.md` + `final-render.md`), NOT raw prompt text.
- **Opt-in limit (stated):** a pure-Python validator cannot
  classify "ordinary prompt vs wizard prompt" from user text. The opt-in gate
  is checked against the artifact: `run.md` must declare `wizard_run: true` and
  record a `trigger` token (`/wizard`, `run the wizard`, `run the council`,
  `use the voices`, `wizard this`). "Opt-in satisfied" here means *a wizard run
  was declared with a trigger*, not *the wizard was correctly invoked for this
  prompt*. A human/runtime check still owns the prompt-classification question.

## Opt-in gate check (run.md)

- [ ] `run.md` exists.
- [ ] `run.md` sets `wizard_run: true` (no Wizard structure on ordinary prompts).
- [ ] `run.md` records a `trigger` containing an explicit invocation token.
- [ ] `runtime` is `claude_code`.

## Vocabulary check (Claude, not Hermes)

- [ ] Every receipt `action_class` is in the Claude set: `controller_local`,
      `tool_run`, `spawn_subagent`, `enqueue_runner`, `blocked`, `deferred`,
      `not_run`, `superseded`.
- [ ] No receipt uses Hermes action classes `spawn_worker` / `delegate_task`.
- [ ] No receipt uses Hermes runtime targets (`delegate_task`,
      `hermes_controller`, `hermes_tool`, `cronjob`, `session_search`).
- [ ] `final-render.md` contains no Hermes-era tokens (`spawn_worker`,
      `delegate_task`, `REAL_ATTEMPT_PARTIAL`).

## Topology + id check

- [ ] `decision-receipt.md` (`wave: Decision`), `failure-receipt.md`
      (`wave: Failure`), `followup-receipt.md` (`wave: Follow-Up`), and
      `final-render.md` all exist.
- [ ] Each topology receipt declares an `id:` (so the topology is id-linkable).

## Provenance check (BOUNDED-PROVENANCE — field presence alone fails)

This is shape + bounded-provenance on disk, NOT a runtime proof that an Agent
actually ran.

- [ ] Any route claiming `action_class: spawn_subagent` carries a
      `linked_receipt:` that resolves to an actual file in the run dir.
- [ ] The `linked_receipt:` is **contained** in the run dir: a `*.md` file
      directly inside it — never absolute, never containing `..`, never a
      traversal into a sibling run. A spawn cannot borrow another run's Agent
      receipt (fixture: `runs/NEG9_PATH_ESCAPE/`).
- [ ] A receipt that itself claims `action_class: spawn_subagent` and is NOT
      the spawn target of any other receipt's `linked_receipt:` (i.e. a SPAWNER,
      not a leaf) always requires a `linked_receipt:` + full provenance — even if
      it self-labels `surface_kind: agent` with a `parent_receipt` and no
      `linked_receipt`. The leaf exemption is granted ONLY to a genuine spawn
      target (fixture: `runs/NEG10_PHANTOM_LEAF/`).
- [ ] That linked file is itself a real Agent receipt: `surface_kind: agent`,
      `action_class: spawn_subagent`, and carries an `agent_id` (real subagent
      identity).
- [ ] **Parent linkage**: the linked Agent receipt's `parent_receipt`
      (or `parent_receipt_id`) equals the spawning receipt's declared `id`. A
      forged/stale Agent receipt with correct surface fields but a mismatched
      (or missing) parent is REJECTED (fixture: `runs/NEG4_FORGED_PARENT/`).
- [ ] The Follow-Up receipt carries `input_decision_receipt_id` and
      `input_failure_receipt_id` (schema `CLAUDE_WIZARD_RECEIPT_SCHEMA.md:102-109`)
      that RESOLVE to the real Decision / Failure ids — not just list membership
      in `references`. Empty/dangling input ids are REJECTED
      (fixture: `runs/NEG5_FIELD_ONLY/`).
- [ ] The Follow-Up `references` list also includes the Decision id AND the
      Failure id (physical topology link, not sequential naming).

A run that names the waves but does not *link* them (no Agent receipt behind a
spawn claim, a stale/forged parent, or a Follow-Up whose input ids do not
resolve) is REJECTED even though every field name is present.

## Failure-path check (not only the clean accept; reason per route)

- [ ] At least one route resolves to `blocked` or `deferred`.
- [ ] At least one `superseded` transition is recorded.
- [ ] **Reason per route**: every `blocked` / `deferred` / `superseded` route in
      the failure receipt's `routes:` block carries a non-empty `reason:`, and any
      class CLAIMED in `route_action_classes` is backed by a structured route that
      names it WITH a reason. Listing the action classes with no reasons is
      REJECTED (fixture: `runs/NEG6_GAMED_FAILURE/`).

A run that only shows the happy accept path, or that lists failure classes with
no reasons, is rejected.

## Honest status ladder check

- [ ] Any `status_label` / `claimed_status` / `proven_status` is one of
      `exists < runs < passes local rerun < canonical by process`.
- [ ] `claimed_status` is never above `proven_status` (no rung claimed from a
      lower rung).

## Follow-Up discipline check

- [ ] Follow-Up `execution_claim_state` is one of `future_choice`, `prechecked`,
      `completed`, `blocked`, `not_run` (future choices unless a branch was
      separately authorized and completed).

## Output check (final-render.md)

- [ ] Output is bottom-line-**first**: the first non-blank CONTENT line (after
      any leading heading / horizontal rule) starts with `Bottom line`. A buried
      `bottom line` later in the body is REJECTED (position, not mere presence).
- [ ] Decision / Failure / Follow-Up sections are present.

## Failure examples this checklist must reject

- A run using Hermes `spawn_worker` / `delegate_task` action classes
  (fixture: `runs/NEG1_HERMES_TOOLS/`).
- A full Decision/Failure/Follow-Up topology emitted with `wizard_run: false`
  and no trigger — Wizard structure on an ordinary prompt
  (fixture: `runs/NEG2_OPTIN_GATE/`).
- A route claiming `spawn_subagent` with no linked Agent receipt
  (fixture: `runs/NEG3_SPAWN_NO_RECEIPT/`).
- A `spawn_subagent` whose linked Agent receipt's `parent_receipt` does NOT match
  the spawning receipt id (forged/stale parent)
  (fixture: `runs/NEG4_FORGED_PARENT/`).
- A field-only run: schema field names present but empty/placeholder values —
  no id to anchor the spawn, unresolved Follow-Up input ids, unbacked failure
  classes, and a buried bottom line (fixture: `runs/NEG5_FIELD_ONLY/`).
- A gamed failure path: `route_action_classes` lists blocked/superseded but the
  structured routes carry no reasons (fixture: `runs/NEG6_GAMED_FAILURE/`).
- A spawning receipt that self-labels `surface_kind: agent` (with a fake
  `parent_receipt` and no `linked_receipt`) to masquerade as a leaf and skip
  provenance (fixture: `runs/NEG7_SURFACE_KIND_EVADE/`).
- A failure class claimed in `route_action_classes` in one receipt with no
  reasoned route backing it in the SAME receipt — cross-file route evade
  (fixture: `runs/NEG8_CROSS_FILE_ROUTE/`).
- A `spawn_subagent` whose `linked_receipt` escapes the run dir (absolute, `..`,
  or otherwise not a `*.md` directly inside the run dir) to borrow a sibling
  run's Agent receipt (fixture: `runs/NEG9_PATH_ESCAPE/`).
- A spawning Decision/council receipt that self-labels `surface_kind: agent`
  with a `parent_receipt` and NO `linked_receipt` to masquerade as a leaf — a
  receipt that itself claims `spawn_subagent` and is not anyone's spawn target
  always requires a linked Agent receipt + full provenance
  (fixture: `runs/NEG10_PHANTOM_LEAF/`).
- A status overclaim (`claimed_status` above `proven_status`).
- A run with only the clean accept path (no blocked/deferred + no superseded).

## Fixtures + how to run

```
python3 conformance/validate_claude_wizard_run.py runs/SMOKE_TOPOLOGY_20260613   # PASS (exit 0)
python3 conformance/validate_claude_wizard_run.py runs/NEG1_HERMES_TOOLS         # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG2_OPTIN_GATE           # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG3_SPAWN_NO_RECEIPT     # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG4_FORGED_PARENT        # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG5_FIELD_ONLY           # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG6_GAMED_FAILURE        # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG7_SURFACE_KIND_EVADE   # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG8_CROSS_FILE_ROUTE     # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG9_PATH_ESCAPE          # FAIL (exit 1)
python3 conformance/validate_claude_wizard_run.py runs/NEG10_PHANTOM_LEAF        # FAIL (exit 1)
```

The validator checks shape + bounded-provenance, not full runtime proof. The
positive fixture is a SELFTEST / smoke fixture, not a real task run.
