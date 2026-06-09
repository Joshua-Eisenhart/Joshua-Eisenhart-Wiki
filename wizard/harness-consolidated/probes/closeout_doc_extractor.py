r"""
Phase 4 (partial): closeout-document extractor.

Reads a markdown closeout doc and extracts a boolean record matching the role
schema in `z3_closeout_completeness.py`. Output record is the same shape as the
operator-authored CLOSEOUT_RECORD blocks in dogfood probes — so the extractor
can be substituted for the operator.

Scope of this extractor (deliberately narrow):
    - Parses `##`-level headings only (not `###` or `#`). The doc title `#` and
      sub-section `###`/`####` are intentionally ignored — only top-level
      Block S/K/H/R fields live at `##`.
    - Maps each `##` heading to a normalized field name (lowercased, all
      non-alphanumerics stripped).
    - Sets each role-required field to True iff its `##` heading is present
      AND the section body is non-empty (not just the heading line followed by
      blank lines or whitespace).
    - Detects forward-plan headings via regex
      `r"^\s*##\s+forward[\s_\-]*plan\b"` (case-insensitive).
    - Records `extra_top_level_headings`: list of `##` headings that do not
      map to any role-schema field name AND are not forward-plan. Block K
      spec (24_closeout_templates.md) defines exactly seven fields; any extra
      top-level heading is a shape divergence (caught in Round D-prime audit).

What it does NOT do:
    - Natural-language fidelity check (Class III.1 in 31_admission_surface.md).
    - Field-content schema (whether "Gates cited" actually cites a gate vs
      narrative). That is Phase 4-full / out of L-proof scope.
    - Cross-role inference. Caller passes the role explicitly.

Audit trail (2026-04-18):
    Built to close the markdown↔record drift that the second Codex audit
    caught (Round D) — `audit_response_closeout_2026_04_18.md` had a literal
    `## Forward plan` heading even while the dogfood record asserted
    `forward_plan_present=False`. The third audit (Round D-prime) caught a
    second drift: extra `##`-level appendices beyond the seven Block K fields.
    `extra_top_level_headings` was added to lift that into the encoding.

Usage:
    from closeout_doc_extractor import extract_closeout_record
    record = extract_closeout_record(Path("audit_response_closeout_2026_04_18.md"), role="K")
    # record["extra_top_level_headings"] is a list of unmapped ## headings
"""

import re
from pathlib import Path

import z3_closeout_completeness as CO


# Map normalized heading text → field name in ROLE_FIELDS.
# The extractor lowercases the heading and strips non-alphanumerics; the keys
# below MUST match that normalized form. (e.g. "Gates cited" → "gatescited".)
HEADING_TO_FIELD = {
    # Role K
    "gatescited": "gates_cited",
    "admissiondecisions": "admission_decisions",
    "narrativesubstitutionsintercepted": "narrative_substitutions_intercepted",
    "workerclaimsverified": "worker_claims_verified",
    "workerclaimsnotverified": "worker_claims_not_verified",
    "statuslabelchangestoregistry": "status_label_changes_to_registry",
    "blockedactions": "blocked_actions",
    # Role S (sim-worker)
    "probefamily": "probe_family",
    "activeconstraints": "active_constraints",
    "statuslabel": "status_label",
    "resultfilepath": "result_file_path",
    "criteriatested": "criteria_tested",
    "survivingcandidates": "surviving_candidates",
    "excludedcandidates": "excluded_candidates",
    "divergencepreserved": "divergence_preserved",
    "notearnedthissession": "not_earned_this_session",
    # Role H (Hermes)
    "modeentered": "mode_entered",
    "modedeclaredby": "mode_declared_by",
    "filesstaged": "files_staged",
    "filesrun": "files_run",
    "stagegateread": "stage_gate_read",
    "actionsrefusedsetuponly": "actions_refused_setup_only",
    "handoffstate": "handoff_state",
    # Role R (batch-runner)
    "queuesource": "queue_source",
    "queuepositionworked": "queue_position_worked",
    "stagegatestatusperqueued": "stage_gate_status_per_queued",
    "simsrunfromadmittedstageonly": "sims_run_from_admitted_stage_only",
    "simsskippedbecausequeuenotpermission": "sims_skipped_because_queue_not_permission",
    "queueisnotpermissioninterceptfired": "queue_is_not_permission_intercept_fired",
    "resultfilesproduced": "result_files_produced",
}

FORWARD_PLAN_HEADING_RE = re.compile(
    r"^\s*##\s+forward[\s_\-]*plan\b", re.IGNORECASE | re.MULTILINE
)
H2_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def _normalize(heading_text):
    """Lowercase + strip non-alphanumerics. 'Gates cited' → 'gatescited'."""
    return re.sub(r"[^a-z0-9]+", "", heading_text.lower())


def _section_body_nonempty(text, heading_start, next_heading_start):
    """Return True iff the body between heading_start and next_heading_start
    contains non-whitespace characters beyond the heading line itself."""
    section = text[heading_start:next_heading_start]
    lines = section.split("\n")
    if not lines:
        return False
    body = "\n".join(lines[1:]).strip()
    return bool(body)


def extract_closeout_record(doc_path, role):
    """Parse a markdown closeout doc and return a boolean record matching the
    role schema in z3_closeout_completeness.ROLE_FIELDS[role] plus
    'forward_plan_present' plus 'extra_top_level_headings'.

    A field is True iff its `##` heading is present AND the section body has
    non-whitespace content. forward_plan_present is True iff any `##` heading
    matches the forward-plan regex. extra_top_level_headings is the list of
    `##` heading texts that do not map to a role-schema field and are not
    forward-plan headings.
    """
    if role not in CO.ROLE_FIELDS:
        raise ValueError(f"unknown role: {role!r}; expected one of {list(CO.ROLE_FIELDS)}")

    text = Path(doc_path).read_text()
    record = {f: False for f in CO.ROLE_FIELDS[role]}
    extras = []

    matches = list(H2_HEADING_RE.finditer(text))
    boundaries = [m.start() for m in matches] + [len(text)]

    for idx, m in enumerate(matches):
        heading = m.group(1).strip()
        normalized = _normalize(heading)
        field = HEADING_TO_FIELD.get(normalized)

        is_forward_plan = bool(re.match(r"forward[\s_\-]*plan", heading, re.IGNORECASE))

        if field is not None and field in CO.ROLE_FIELDS[role]:
            body_present = _section_body_nonempty(text, m.start(), boundaries[idx + 1])
            record[field] = body_present
        elif is_forward_plan:
            pass  # counted via FORWARD_PLAN_HEADING_RE below
        else:
            extras.append(heading)

    record["forward_plan_present"] = bool(FORWARD_PLAN_HEADING_RE.search(text))
    record["extra_top_level_headings"] = extras
    return record


def main():
    """Self-test: extract from the audit-response closeout (role K) and
    cross-check against z3 closeout-completeness predicate."""
    doc_path = Path(__file__).parent.parent / "audit_response_closeout_2026_04_18.md"
    if not doc_path.exists():
        print(f"FAIL: {doc_path} not found")
        return 1

    record = extract_closeout_record(doc_path, role="K")
    print(f"== extracted closeout record (role K) from {doc_path.name} ==")
    for f in CO.ROLE_FIELDS["K"]:
        print(f"  {f}: {record[f]}")
    print(f"  forward_plan_present: {record['forward_plan_present']}")
    print(f"  extra_top_level_headings: {record['extra_top_level_headings']}")
    print()

    verdict = CO.check("K", record)
    print(f"z3 closeout-completeness verdict: {verdict}")
    expected_co = "sat"
    co_ok = str(verdict) == expected_co
    print(f"[{'OK' if co_ok else 'FAIL'}] closeout-completeness expected {expected_co}, got {verdict}")

    extras_ok = len(record["extra_top_level_headings"]) == 0
    print(f"[{'OK' if extras_ok else 'FAIL'}] no extra ## headings beyond Block K spec "
          f"(got {len(record['extra_top_level_headings'])} extras)")

    return 0 if (co_ok and extras_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
