#!/usr/bin/env python3
"""Validate a bounded Claude Code Wizard run directory (SHAPE + BOUNDED-PROVENANCE).

Honest status label
-------------------
This validator checks the SHAPE of a run-dir artifact and a BOUNDED set of
provenance links between its receipt files. It is NOT a full runtime proof: it
does not execute the Wizard, does not verify that an Agent actually ran, and
cannot classify an ordinary prompt vs a wizard prompt from raw user text (see
LIMIT). It is stronger than field-presence (it follows id/parent linkage on
disk), but it is shape + bounded-provenance, not proof of execution.

Scope and intent
----------------
This validator is Claude-native (NOT the Hermes adaptation it replaces). It
checks that a Claude Code Wizard run produced a real, *physically linked*
Decision -> Failure -> Follow-Up topology in Claude Code action classes, with
honest status labels and a working failure path.

Field-presence alone does NOT pass: the validator checks bounded PROVENANCE on
disk.

  - A route claiming `action_class: spawn_subagent` MUST carry a `linked_receipt:`
    that resolves to an actual Agent receipt file in the run dir, and that file
    must itself be a real Agent receipt (surface_kind: agent, action_class:
    spawn_subagent, matching receipt id). A spawn_subagent claim with no linked,
    resolvable Agent receipt is REJECTED.
  - The Follow-Up receipt MUST reference the Decision and Failure receipts by
    their declared `id:` (topology physically linked, not just sequentially
    named files). Dangling references are REJECTED.

It also enforces the Claude action-class set (Hermes classes spawn_worker /
delegate_task and Hermes runtime targets like delegate_task are REJECTED), the
opt-in gate (see LIMIT below), the honest status ladder, and that the run
exercises a real failure path (a blocked/deferred route + a superseded
transition).

LIMIT (stated per panel revision 3): a pure-Python validator cannot classify an
"ordinary prompt vs a wizard prompt" from raw user text. It validates the RUN
ARTIFACT: it checks that the run dir DECLARED a wizard run with a recorded
trigger (`run.md`: wizard_run: true + a trigger token). It does not read or
judge the original prompt. The opt-in gate here means "was a wizard run
declared with a trigger", not "was the wizard correctly invoked for this prompt".

Usage:
    validate_claude_wizard_run.py <run_dir> [--json]

Exit 0 = PASS, exit 1 = FAIL (findings printed).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# --- Claude Code vocabulary (NOT Hermes) ---------------------------------
CLAUDE_ACTION_CLASSES = {
    "controller_local",
    "tool_run",
    "spawn_subagent",
    "enqueue_runner",
    "blocked",
    "deferred",
    "not_run",
    "superseded",
}
# Hermes action classes / runtime targets that must never appear in a Claude run.
HERMES_ACTION_CLASSES = {"spawn_worker", "delegate_task"}
HERMES_RUNTIME_TARGETS = {
    "delegate_task",
    "hermes_controller",
    "hermes_tool",
    "cronjob",
    "session_search",
}
# Accepted runtime targets. Matched case-insensitively (see check_action_class),
# so the schema doc's capitalized forms (Agent/Skill/Bash/...) and older
# lowercase receipts both validate. This set is the UNION of the schema-doc
# tool-named vocabulary and the older controller-named vocabulary; the schema
# (schemas/CLAUDE_WIZARD_RECEIPT_SCHEMA.md "Runtime target vocabulary") lists the
# same accepted values so doc and validator agree.
CLAUDE_RUNTIME_TARGETS = {
    # schema-doc tool-named vocabulary (capitalized in the doc; compared lower)
    "agent",
    "skill",
    "bash",
    "read",
    "edit",
    "write",
    "croncreate",
    "monitor",
    "controller_synthesis",
    # older controller-named vocabulary (kept accepted for back-compat)
    "claude_controller",
    "claude_tool",
    "background_process",
    "cron_or_loop",
    "memory",
    "none",
}

STATUS_VALUES = {"completed", "partial", "blocked", "failed", "deferred", "not_run", "superseded"}

# Honest status ladder (CLAUDE.md). A higher rung may not be claimed from a lower one.
STATUS_LADDER = ["exists", "runs", "passes local rerun", "canonical by process"]

TRIGGER_TOKENS = ["/wizard", "run the wizard", "run the council", "use the voices", "wizard this"]


def parse_fields(text: str) -> dict:
    """Parse top-level `key: value` and `key:` + `  - item` list fields from a
    receipt markdown body. Tolerant: ignores prose lines. List values become
    python lists; scalars become strings.
    """
    fields: dict[str, object] = {}
    current_list_key: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        # list item belonging to the most recent `key:` with empty value
        m_item = re.match(r"^\s*-\s+(.*)$", line)
        if m_item and current_list_key is not None:
            # A later list value must be honored even if an earlier scalar set
            # this key first: if the slot is not already a list, replace it with
            # a fresh list (scalar-then-list overwrite fix).
            if not isinstance(fields.get(current_list_key), list):
                fields[current_list_key] = []
            fields[current_list_key].append(m_item.group(1).strip())
            continue
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m_kv:
            key, val = m_kv.group(1), m_kv.group(2).strip()
            if val == "":
                # could be a list header; arm list capture. If a prior scalar
                # occupies this key, replace it with an empty list so a following
                # `- item` is honored (setdefault would wrongly keep the scalar).
                current_list_key = key
                if not isinstance(fields.get(key), list):
                    fields[key] = []
            else:
                fields[key] = val
                current_list_key = None
        else:
            # prose line breaks any pending list capture
            current_list_key = None
    return fields


def as_list(val: object) -> list[str]:
    if val is None:
        return []
    if isinstance(val, list):
        return [str(v) for v in val]
    # comma-separated scalar fallback
    return [v.strip() for v in str(val).split(",") if v.strip()]


def scalar_field(val: object) -> str:
    """Normalize a parsed field to a clean scalar string. An empty-valued `key:`
    line parses as an empty list (`[]`) under parse_fields()'s list-arming; treat
    that and None as empty so an unfilled schema field reads as MISSING, not as
    a stray literal `'[]'`."""
    if val is None:
        return ""
    if isinstance(val, list):
        return str(val[0]).strip() if len(val) == 1 else ""
    return str(val).strip()


def parse_routes(text: str) -> list[dict]:
    """Structured parse of a `routes:` block of `- name:` items, each with
    indented `action_class:` and `reason:` sub-fields (the latter possibly a
    `reason: |` folded block). The flat parse_fields() cannot see these, so a
    failure-path check that wants a reason-per-route needs this.

    Returns a list of {name, action_class, reason} dicts. A route whose reason
    is empty/whitespace yields reason="".
    """
    lines = text.splitlines()
    # find the `routes:` header line (top-level key, empty value)
    start = None
    for i, raw in enumerate(lines):
        if re.match(r"^routes:\s*$", raw):
            start = i + 1
            break
    if start is None:
        return []
    routes: list[dict] = []
    current: dict | None = None
    reason_capture = False
    reason_indent = None
    i = start
    while i < len(lines):
        raw = lines[i]
        # a new top-level key (no leading space, ends the routes block)
        if raw and not raw[0].isspace() and re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", raw):
            break
        m_item = re.match(r"^\s*-\s*name:\s*(.*)$", raw)
        if m_item:
            if current is not None:
                routes.append(current)
            current = {"name": m_item.group(1).strip(), "action_class": "", "reason": ""}
            reason_capture = False
            reason_indent = None
            i += 1
            continue
        if current is not None:
            m_ac = re.match(r"^\s+action_class:\s*(.*)$", raw)
            if m_ac:
                current["action_class"] = m_ac.group(1).strip()
                reason_capture = False
                i += 1
                continue
            m_reason = re.match(r"^(\s+)reason:\s*(.*)$", raw)
            if m_reason:
                inline = m_reason.group(2).strip()
                if inline and inline != "|":
                    current["reason"] = inline
                    reason_capture = False
                else:
                    # folded block: collect following more-indented lines
                    reason_capture = True
                    reason_indent = len(m_reason.group(1))
                i += 1
                continue
            if reason_capture:
                if raw.strip() == "":
                    i += 1
                    continue
                indent = len(raw) - len(raw.lstrip())
                if indent > reason_indent:
                    current["reason"] = (current["reason"] + " " + raw.strip()).strip()
                    i += 1
                    continue
                else:
                    reason_capture = False
        i += 1
    if current is not None:
        routes.append(current)
    return routes


def load_receipts(run_dir: Path) -> dict[str, dict]:
    """Return {filename: parsed_fields} for every *.md receipt except run.md
    and the final render."""
    receipts: dict[str, dict] = {}
    for path in sorted(run_dir.glob("*.md")):
        if path.name in {"run.md", "final-render.md"}:
            continue
        receipts[path.name] = parse_fields(path.read_text(encoding="utf-8"))
    return receipts


def check_optin_gate(run_dir: Path, findings: list[str]) -> dict:
    run_file = run_dir / "run.md"
    if not run_file.exists():
        findings.append(
            "opt-in gate: missing run.md (run artifact must declare a wizard run; "
            "validator checks the artifact, not raw prompt text)"
        )
        return {}
    fields = parse_fields(run_file.read_text(encoding="utf-8"))
    if str(fields.get("wizard_run", "")).lower() != "true":
        findings.append("opt-in gate: run.md must set `wizard_run: true` (no Wizard structure on ordinary prompts)")
    trigger = str(fields.get("trigger", "")).lower()
    if not any(tok in trigger for tok in TRIGGER_TOKENS):
        findings.append(
            f"opt-in gate: run.md `trigger` must record an explicit invocation token one of {TRIGGER_TOKENS}; got {trigger!r}"
        )
    if str(fields.get("runtime", "")) not in {"claude_code", ""} and fields.get("runtime"):
        if fields.get("runtime") != "claude_code":
            findings.append(f"runtime: run.md runtime must be claude_code, got {fields.get('runtime')!r}")
    return fields


def check_action_class(name: str, fields: dict, findings: list[str]) -> None:
    # action_class and runtime_target are matched CASE-INSENSITIVELY: the schema
    # doc writes runtime targets capitalized (Agent / Skill) while older receipts
    # and fixtures use lowercase (agent / skill). Both forms are accepted; the
    # Claude/Hermes vocabulary sets below are stored lowercased for the compare.
    ac = fields.get("action_class")
    if ac is None:
        findings.append(f"{name}: missing action_class")
        return
    ac = str(ac)
    ac_norm = ac.lower()
    if ac_norm in {h.lower() for h in HERMES_ACTION_CLASSES}:
        findings.append(f"{name}: Hermes action_class {ac!r} is not allowed in a Claude run")
    elif ac_norm not in {c.lower() for c in CLAUDE_ACTION_CLASSES}:
        findings.append(f"{name}: action_class {ac!r} not in Claude set {sorted(CLAUDE_ACTION_CLASSES)}")
    rt = fields.get("runtime_target")
    if rt is not None:
        rt = str(rt)
        rt_norm = rt.lower()
        if rt_norm in {h.lower() for h in HERMES_RUNTIME_TARGETS}:
            findings.append(f"{name}: Hermes runtime_target {rt!r} is not allowed in a Claude run")
        elif rt_norm not in {c.lower() for c in CLAUDE_RUNTIME_TARGETS}:
            findings.append(f"{name}: runtime_target {rt!r} not in Claude set {sorted(CLAUDE_RUNTIME_TARGETS)}")


def check_status_ladder(name: str, fields: dict, findings: list[str]) -> None:
    """Honest status labels: the `status_label` (if present) must be one of the
    ladder rungs, and a route may not claim a rung it did not reach. We enforce
    that `claimed_status` is never above `proven_status` when both are present.
    """
    for key in ("status_label", "claimed_status", "proven_status"):
        v = fields.get(key)
        if v is not None and str(v) not in STATUS_LADDER:
            findings.append(
                f"{name}: {key} {v!r} not an honest status-ladder rung {STATUS_LADDER}"
            )
    claimed = fields.get("claimed_status")
    proven = fields.get("proven_status")
    if claimed in STATUS_LADDER and proven in STATUS_LADDER:
        if STATUS_LADDER.index(str(claimed)) > STATUS_LADDER.index(str(proven)):
            findings.append(
                f"{name}: status overclaim — claimed_status {claimed!r} is above proven_status {proven!r}"
            )


def check_spawn_provenance(name: str, fields: dict, receipts: dict[str, dict], run_dir: Path, findings: list[str], linked_targets: set[str]) -> None:
    """A spawn_subagent claim REQUIRES a linked, resolvable Agent receipt whose
    `parent_receipt` points BACK to the spawning (claimant) receipt id.

    The Agent receipt itself (surface_kind: agent) is the terminal proof of a
    spawn; it does not need to link to a further Agent receipt. Provenance is
    required of the CLAIMANT route (council/lane/etc.), not of the agent leaf.

    Surface fields alone (surface_kind/action_class/agent_id) are NOT enough: a
    forged or stale Agent receipt that carries the right surface fields but does
    NOT name this claimant as its parent must be REJECTED. We therefore require
    that the linked Agent receipt's `parent_receipt` (or `parent_receipt_id`)
    equals the claimant receipt's declared `id` (or `receipt_id`).

    `linked_targets` is the set of receipt FILENAMES that some other receipt's
    `linked_receipt:` points at — i.e. the genuine spawn TARGETS. A real Agent
    leaf is, by construction, a spawn target (the spawner names it). The leaf
    exemption is granted ONLY to such a target; a receipt that self-labels
    surface_kind:agent + claims spawn_subagent but is NOT anyone's spawn target
    is a SPAWNER masquerading as a leaf and must run full provenance.
    """
    if str(fields.get("action_class", "")).lower() != "spawn_subagent":
        return
    # LEAF agent early-return is NARROW. A real Agent leaf is the TERMINAL proof
    # of someone else's spawn: (a) it is itself a spawn TARGET — some other
    # receipt's `linked_receipt:` names this file; (b) it was spawned (carries a
    # parent_receipt); and (c) it issues no onward spawn (no linked_receipt).
    # Only that shape skips provenance.
    #
    # PHANTOM-LEAF FIX: a receipt that itself CLAIMS a spawn (action_class
    # spawn_subagent) but is NOT a spawn target of any other receipt is a SPAWNER,
    # not a leaf — even if it self-labels surface_kind:agent, carries a
    # parent_receipt, and omits linked_receipt. Such a spawner ALWAYS requires a
    # linked_receipt and full provenance; the leaf exemption does not apply to it.
    if str(fields.get("surface_kind", "")).lower() == "agent":
        has_parent = bool(
            str(fields.get("parent_receipt") or fields.get("parent_receipt_id") or "").strip()
        )
        claims_onward_spawn = bool(fields.get("linked_receipt"))
        is_spawn_target = name in linked_targets
        if is_spawn_target and has_parent and not claims_onward_spawn:
            return
        if not is_spawn_target:
            findings.append(
                f"{name}: surface_kind:agent + action_class spawn_subagent but is NOT the spawn "
                f"target of any receipt's `linked_receipt:` — a SPAWNER cannot masquerade as a "
                f"leaf to skip provenance (a real leaf is named by its spawner's linked_receipt)"
            )
        else:
            findings.append(
                f"{name}: surface_kind:agent + action_class spawn_subagent but does not look like a "
                f"LEAF agent receipt (a leaf has a parent_receipt and issues no onward spawn) — a "
                f"spawning receipt cannot self-label surface_kind:agent to skip provenance"
            )
        # fall through: still run the full spawn-provenance check below.
    linked = fields.get("linked_receipt")
    if not linked:
        findings.append(
            f"{name}: claims action_class spawn_subagent but has no `linked_receipt:` "
            f"(spawn_subagent requires a linked Agent receipt — provenance, not field presence)"
        )
        return
    linked = str(linked)
    # PATH-ESCAPE CONTAINMENT: the linked Agent receipt MUST be a file directly
    # inside the run dir. Reject any linked_receipt that is absolute, contains
    # '..', or otherwise does not resolve to a *.md directly in run_dir. Without
    # this, a `linked_receipt: ../OTHER_RUN/agent-x.md` follows a SIBLING run's
    # receipt and borrows its provenance.
    linked_pp = Path(linked)
    contained = run_dir / linked
    run_md_set = {p.resolve() for p in run_dir.glob("*.md")}
    if (
        linked_pp.is_absolute()
        or ".." in linked_pp.parts
        or contained.resolve() not in run_md_set
    ):
        findings.append(
            f"{name}: linked_receipt {linked!r} is not contained in the run dir "
            f"(must be a *.md file directly inside {run_dir.name}/ — no absolute path, no '..', "
            f"no traversal into a sibling run; a spawn cannot borrow another run's Agent receipt)"
        )
        return
    linked_path = run_dir / linked
    if not linked_path.exists():
        findings.append(f"{name}: linked_receipt {linked!r} does not exist in run dir")
        return
    agent = receipts.get(linked)
    if agent is None:
        agent = parse_fields(linked_path.read_text(encoding="utf-8"))
    # The linked file must itself be a real Agent receipt.
    if str(agent.get("surface_kind", "")).lower() != "agent":
        findings.append(
            f"{name}: linked_receipt {linked!r} is not an Agent receipt "
            f"(surface_kind must be 'agent', got {agent.get('surface_kind')!r})"
        )
    if str(agent.get("action_class", "")).lower() != "spawn_subagent":
        findings.append(
            f"{name}: linked Agent receipt {linked!r} must record action_class spawn_subagent, "
            f"got {agent.get('action_class')!r}"
        )
    if not agent.get("agent_id") and not agent.get("worker_id"):
        findings.append(
            f"{name}: linked Agent receipt {linked!r} missing an agent_id (no real subagent identity)"
        )
    # PARENT LINKAGE: the Agent receipt must name THIS claimant as its parent.
    # Without this, a forged/stale Agent receipt with correct surface fields
    # passes. The claimant id is the spawn anchor.
    claimant_id = str(fields.get("id") or fields.get("receipt_id") or "").strip()
    agent_parent = str(agent.get("parent_receipt") or agent.get("parent_receipt_id") or "").strip()
    if not claimant_id:
        findings.append(
            f"{name}: claims spawn_subagent but has no `id:`/`receipt_id:` to anchor parent linkage "
            f"(cannot verify the linked Agent receipt points back to this spawn)"
        )
    elif not agent_parent:
        findings.append(
            f"{name}: linked Agent receipt {linked!r} has no `parent_receipt:` "
            f"(must name the spawning receipt id {claimant_id!r}; a forged/stale Agent receipt is rejected)"
        )
    elif agent_parent != claimant_id:
        findings.append(
            f"{name}: linked Agent receipt {linked!r} parent_receipt {agent_parent!r} does not match "
            f"the spawning receipt id {claimant_id!r} (stale/forged Agent receipt — parent linkage broken)"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Claude Code Wizard run dir (shape + bounded-provenance, not full runtime proof).")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    run_dir = args.run_dir
    findings: list[str] = []

    if not run_dir.is_dir():
        out = {"ok": False, "findings": [f"missing run dir: {run_dir}"], "run_dir": str(run_dir)}
        _emit(out, args.json)
        return 1

    # --- opt-in gate (run artifact, NOT raw prompt) ---
    check_optin_gate(run_dir, findings)

    # --- required topology files ---
    required = ["decision-receipt.md", "failure-receipt.md", "followup-receipt.md", "final-render.md"]
    for rf in required:
        if not (run_dir / rf).exists():
            findings.append(f"missing required topology file: {rf}")

    receipts = load_receipts(run_dir)
    decision = receipts.get("decision-receipt.md")
    failure = receipts.get("failure-receipt.md")
    followup = receipts.get("followup-receipt.md")

    # --- per-receipt wave + action class + status ladder ---
    wave_expect = {
        "decision-receipt.md": "Decision",
        "failure-receipt.md": "Failure",
        "followup-receipt.md": "Follow-Up",
    }
    for fname, expected_wave in wave_expect.items():
        f = receipts.get(fname)
        if f is None:
            continue
        if str(f.get("wave", "")) != expected_wave:
            findings.append(f"{fname}: wave must be {expected_wave!r}, got {f.get('wave')!r}")
        if not f.get("id"):
            findings.append(f"{fname}: missing `id:` (topology must be id-linkable)")
        check_action_class(fname, f, findings)
        check_status_ladder(fname, f, findings)

    # --- provenance: spawn_subagent on ANY receipt requires linked Agent receipt ---
    # Compute the set of genuine spawn TARGETS: filenames that some receipt's
    # `linked_receipt:` names. A real Agent leaf is, by construction, one of these
    # (its spawner points at it). The leaf exemption is granted ONLY to a target;
    # a self-labelled agent receipt that nobody links-to is a SPAWNER masquerade.
    linked_targets: set[str] = set()
    for f in receipts.values():
        lr = f.get("linked_receipt")
        if lr:
            linked_targets.add(str(lr).strip())
    for fname, f in receipts.items():
        check_spawn_provenance(fname, f, receipts, run_dir, findings, linked_targets)

    # --- provenance: Follow-Up must reference Decision + Failure by id ---
    # List-membership in `references:` alone is NOT provenance: the schema
    # (CLAUDE_WIZARD_RECEIPT_SCHEMA.md:102-109) requires the typed fields
    # `input_decision_receipt_id` / `input_failure_receipt_id` that RESOLVE to
    # the real Decision / Failure receipt ids. We enforce both: the typed input
    # fields must be present and match, AND the references list must include
    # them.
    if followup is not None and decision is not None and failure is not None:
        refs = set(as_list(followup.get("references")))
        decision_id = str(decision.get("id") or decision.get("receipt_id") or "").strip()
        failure_id = str(failure.get("id") or failure.get("receipt_id") or "").strip()
        input_dec = scalar_field(followup.get("input_decision_receipt_id"))
        input_fail = scalar_field(followup.get("input_failure_receipt_id"))

        if not input_dec:
            findings.append(
                "followup-receipt.md: missing `input_decision_receipt_id` "
                "(schema CLAUDE_WIZARD_RECEIPT_SCHEMA.md:104 — the consumed Decision id, "
                "not just list membership)"
            )
        elif decision_id and input_dec != decision_id:
            findings.append(
                f"followup-receipt.md: `input_decision_receipt_id` {input_dec!r} does not resolve to the "
                f"Decision receipt id {decision_id!r} (dangling/forged input reference)"
            )
        if not input_fail:
            findings.append(
                "followup-receipt.md: missing `input_failure_receipt_id` "
                "(schema CLAUDE_WIZARD_RECEIPT_SCHEMA.md:105 — the consumed Failure id, "
                "not just list membership)"
            )
        elif failure_id and input_fail != failure_id:
            findings.append(
                f"followup-receipt.md: `input_failure_receipt_id` {input_fail!r} does not resolve to the "
                f"Failure receipt id {failure_id!r} (dangling/forged input reference)"
            )

        if decision_id and decision_id not in refs:
            findings.append(
                f"followup-receipt.md: `references` must include Decision id {decision_id!r} "
                f"(physical topology link, not sequential naming); got {sorted(refs)}"
            )
        if failure_id and failure_id not in refs:
            findings.append(
                f"followup-receipt.md: `references` must include Failure id {failure_id!r}; got {sorted(refs)}"
            )

    # --- Follow-Up execution-claim discipline: render as future_choice unless authorized+completed ---
    if followup is not None:
        ecs = str(followup.get("execution_claim_state", ""))
        if ecs and ecs not in {"future_choice", "prechecked", "completed", "blocked", "not_run"}:
            findings.append(
                f"followup-receipt.md: execution_claim_state {ecs!r} invalid "
                f"(future_choice | prechecked | completed | blocked | not_run)"
            )

    # --- failure path: a blocked/deferred route AND a superseded transition somewhere ---
    all_action_classes = [str(f.get("action_class", "")) for f in receipts.values()]
    # routes may also be listed inside a receipt as `route_action_classes:`
    for f in receipts.values():
        all_action_classes.extend(as_list(f.get("route_action_classes")))
    if not ({"blocked", "deferred"} & set(all_action_classes)):
        findings.append(
            "failure path missing: no route resolved to blocked/deferred "
            "(smoke topology must exercise a real failure path, not only the clean accept)"
        )
    if "superseded" not in all_action_classes:
        findings.append(
            "failure path missing: no superseded transition recorded "
            "(a route must be shown superseded)"
        )

    # Reason-per-route discipline: listing `route_action_classes: [blocked, ...]`
    # with no per-route reason is gameable. Every blocked/deferred/superseded
    # route in a receipt's `routes:` block MUST carry a non-empty reason; and any
    # class CLAIMED in route_action_classes must be backed by at least one
    # structured, reasoned route THAT NAMES IT IN THE SAME RECEIPT.
    #
    # Cross-file evade fix: route_action_classes is aggregated across ALL
    # receipts, but a backing route must live in the SAME receipt that claims the
    # class. Parsing routes only from failure-receipt.md let a class claimed in
    # decision-receipt.md (with no backing route there) slip through. We now
    # parse routes per-receipt and require same-receipt backing.
    REASONED_CLASSES = {"blocked", "deferred", "superseded"}
    for fname, f in receipts.items():
        rpath = run_dir / fname
        parsed_routes: list[dict] = []
        if rpath.exists():
            parsed_routes = parse_routes(rpath.read_text(encoding="utf-8"))
        reasoned_classes_present: set[str] = set()
        for r in parsed_routes:
            ac = str(r.get("action_class", "")).strip().lower()
            if ac in REASONED_CLASSES:
                if not str(r.get("reason", "")).strip():
                    findings.append(
                        f"{fname}: route {r.get('name')!r} is action_class {ac!r} "
                        f"with no `reason:` (a blocked/deferred/superseded route must state why — "
                        f"listing the class alone is gameable)"
                    )
                else:
                    reasoned_classes_present.add(ac)
        claimed_classes = {
            c.lower() for c in as_list(f.get("route_action_classes")) if c.lower() in REASONED_CLASSES
        }
        for c in sorted(claimed_classes - reasoned_classes_present):
            findings.append(
                f"{fname}: `route_action_classes` claims {c!r} but no structured route "
                f"in this receipt's `routes:` resolves to {c!r} WITH a reason "
                f"(unbacked failure-path claim — a class must be backed in the SAME receipt)"
            )

    # --- final render: bottom-line-first + Claude header, no Hermes leakage ---
    fr_path = run_dir / "final-render.md"
    if fr_path.exists():
        fr = fr_path.read_text(encoding="utf-8")
        for hermes_token in ["spawn_worker", "delegate_task", "REAL_ATTEMPT_PARTIAL"]:
            if hermes_token in fr:
                findings.append(f"final-render.md: contains Hermes-era token {hermes_token!r}")
        # Bottom-line-FIRST is a position claim, not a presence claim: a buried
        # "bottom line" anywhere in the body must NOT pass. Check the first
        # non-blank CONTENT line (skipping a leading markdown heading / hr).
        first_content = ""
        for raw in fr.splitlines():
            s = raw.strip()
            if not s:
                continue
            if s.startswith("#") or set(s) <= {"-", "=", "*"}:
                continue  # markdown heading or horizontal rule — not content
            first_content = s
            break
        # Bottom-line-FIRST is a POSITION claim, but tolerate markdown emphasis on
        # the first content line: a leading blockquote `> Bottom line`, bold
        # `**Bottom line**`, or italic `_Bottom line_` must still pass. Strip
        # leading blockquote/emphasis markers before the position check while the
        # first-content-line requirement is still enforced (a buried bottom line
        # later in the body cannot reach here).
        stripped = first_content
        stripped = re.sub(r"^\s*>+\s*", "", stripped)        # blockquote marker(s)
        stripped = re.sub(r"^[*_]{1,3}\s*", "", stripped)    # leading bold/italic markers
        if not stripped.lower().startswith("bottom line"):
            findings.append(
                "final-render.md: output must be bottom-line-FIRST — the first content line must "
                f"start with 'Bottom line' (markdown emphasis tolerated) (got {first_content[:60]!r})"
            )
        for wave in ["Decision", "Failure", "Follow-Up"]:
            if wave not in fr:
                findings.append(f"final-render.md: missing {wave} section")

    out = {"ok": not findings, "findings": findings, "run_dir": str(run_dir)}
    _emit(out, args.json)
    return 0 if not findings else 1


def _emit(out: dict, as_json: bool) -> None:
    if as_json:
        print(json.dumps(out, indent=2, sort_keys=True))
        return
    if out["ok"]:
        print("PASS")
        print(f"validated: {out['run_dir']}")
    else:
        print("FAIL")
        for f in out["findings"]:
            print(f"- {f}")


if __name__ == "__main__":
    sys.exit(main())
