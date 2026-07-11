#!/usr/bin/env python3
"""Fail-closed lint for the bundle's claim-bearing Ratchet front doors."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# self-locate: ensure THIS script's dir is importable regardless of how we are invoked
# (the harness runs `python ratchet/bundle_ratchet_lint.py` under safe-path mode, where the
#  script's own directory is NOT auto-added to sys.path — so add it explicitly).
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ratchet_kernel import run_self_test


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SCOPE_MARKER = "RATCHET_V0_2_SCOPE_CORRECTION"

REQUIRED_TEXT = {
    "RATCHET_SPEC.md": [
        "ROOT = CONSTRAINED_DISTINGUISHABILITY",
        "MSS is an anytime frontier",
        "The evidence ratchets. The ontology does not become permanently stronger",
    ],
    "archive/RATCHET_V0_2_UPGRADE_REPORT.md": [
        "Scientific claim ceiling: process hardening / scratch diagnostic",
        "no bundle-wide scientific frontier has yet been admitted under v0.2",
    ],
    "00_START_HERE.md": [
        "ROOT = CONSTRAINED_DISTINGUISHABILITY",
        "provisional MSS frontier",
        SCOPE_MARKER,
    ],
    "CLAUDE.md": [
        "RATCHET_SPEC.md",
        SCOPE_MARKER,
    ],
    "archive/ORIENTATION.md": [SCOPE_MARKER],
    "MODEL_LAYER_LEDGER.md": [SCOPE_MARKER],
    "STATE_OF_THE_MODEL.md": [SCOPE_MARKER],
    "archive/README_UNIFIED_BUNDLE.md": [SCOPE_MARKER],
    "docs/UNIFIED_LENS_MAP.md": ["RATCHET v0.2 scope correction"],
    "archive/FOUNDATIONS_REAUDIT.md": ["RATCHET v0.2 scope correction"],
    "archive/V7_FOUNDATION_SIMS_CROSSCHECK.md": ["RATCHET v0.2 scope correction"],
    "archive/REPO_AUDIT_AND_RESOLUTIONS.md": ["RATCHET v0.2 scope correction"],
    "archive/README_FOR_THREAD.md": ["Superseded process front door"],
    "LAPTOP_README.md": ["Ratchet v0.2 integrity check"],
    "spec_and_reports/CONSTRAINT_CORE_FORMAL_SPEC.md": ["RATCHET v0.2 scope correction"],
    "spec_and_reports/PURE_MATH_CORE.md": ["RATCHET v0.2 scope correction"],
    "generate_bundle_docs.py": [
        "ROOT = CONSTRAINED_DISTINGUISHABILITY",
        "provisional MSS frontier",
    ],
    "ratchet/CA_MSS_RESEARCH_PROGRAM.md": [
        "F01 motivates finite realizations. It does not by itself imply cells",
        "The output is the set of all tested surviving candidates",
    ],
    "ratchet/CURRENT_FRONTIER.md": [
        "no bundle-wide scientific `PROVISIONAL_MSS` frontier yet under v0.2",
        "does not retroactively admit the legacy manifold tower",
    ],
    "docs/BUNDLE_GUIDE.md": [
        "ROOT = CONSTRAINED_DISTINGUISHABILITY",
        "provisional MSS frontier",
    ],
    "docs/MATH_INVENTORY.md": [
        "FORCED-WITHIN-GRAMMAR",
        "not globally forced",
    ],
}

FORBIDDEN_SCAN_FILES = {
    "RATCHET_SPEC.md",
    "archive/RATCHET_V0_2_UPGRADE_REPORT.md",
    "00_START_HERE.md",
    "CLAUDE.md",
    "archive/ORIENTATION.md",
    "STATE_OF_THE_MODEL.md",
    "archive/README_UNIFIED_BUNDLE.md",
    "docs/UNIFIED_LENS_MAP.md",
    "generate_bundle_docs.py",
    "docs/BUNDLE_GUIDE.md",
    "docs/MATH_INVENTORY.md",
    "ratchet/CA_MSS_RESEARCH_PROGRAM.md",
}

FORBIDDEN_PATTERNS = {
    r"R_t\s*=\s*\(X_t,\s*P_t,\s*Q_t,\s*G_t,\s*E_t": "separate entropy/geometry Ratchet state",
    r"complex-spinor carrier \(forced by F01(?:\+|∧)N01\)": "globally forced complex carrier",
    r"--> forces H = C\^2": "legacy global carrier-forcing arrow",
    r"THE MANIFOLD — canonical layer list": "layer inventory called canon",
    r"only primitive is \*\*constraint on distinguishability\*\*: `~_P` on a FINITE support": "equivalence/support smuggled into root",
    r"POST_RUN_RESULT": "unfinished post-run validation placeholder",
}


def main() -> int:
    errors: list[str] = []

    for relative, needles in REQUIRED_TEXT.items():
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing front-door file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{relative} missing required Ratchet marker: {needle!r}")

    scan_files = [ROOT / relative for relative in FORBIDDEN_SCAN_FILES if (ROOT / relative).exists()]
    for path in scan_files:
        text = path.read_text(encoding="utf-8")
        for pattern, label in FORBIDDEN_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"{path.relative_to(ROOT)} contains forbidden {label}")

    for relative in (
        "ratchet/weakening_grammar.json",
        "ratchet/schemas/ratchet_run.schema.json",
        "ratchet/examples/process_fixture.json",
    ):
        path = ROOT / relative
        try:
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON {relative}: {exc}")

    # anti-sprawl guard: the top level must stay small. Only these loose .md files may sit at ROOT;
    # any other doc belongs in docs/ (indexes/maps), archive/ (superseded/reports), or a topic folder.
    ALLOWED_TOPLEVEL_MD = {
        "00_START_HERE.md", "RATCHET_SPEC.md", "CLAUDE.md", "LAPTOP_README.md",
        "MODEL_LAYER_LEDGER.md", "CHANGELOG_HARDENING.md", "STATE_OF_THE_MODEL.md",
    }
    for entry in sorted(ROOT.glob("*.md")):
        if entry.name not in ALLOWED_TOPLEVEL_MD:
            errors.append(
                f"top-level sprawl: {entry.name} must live in docs/ (index/map), archive/ (superseded/report), "
                f"or a topic folder — the top level is a small fixed set (see 00_START_HERE §5e)"
            )

    for failure in run_self_test():
        errors.append(f"Ratchet kernel self-test: {failure}")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    print("PASS bundle_ratchet_lint")
    print(f"checked {len(REQUIRED_TEXT)} claim-bearing front doors; source/reference corpora remain hypothesis inputs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
