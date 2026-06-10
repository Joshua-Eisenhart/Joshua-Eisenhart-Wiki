#!/usr/bin/env python3
"""Scan for NumPy/classical contamination in canonical Lev lanes.

This scanner is intentionally conservative for Lev core/provider lanes. Use
`# lev-allow-numpy-boundary` on a line only for edge adapters, baselines,
import/export utilities, fixtures, or explicitly non-canonical projections.

Default ignores prevent the scanner from flagging its own pattern definitions.
"""
import argparse
import json
import re
from pathlib import Path

PATTERNS = [
    (re.compile(r"\.cpu\s*\(\s*\)\.detach\s*\(\s*\)\.numpy\s*\("), "block", "PyTorch CPU/detach/numpy canonical escape"),
    (re.compile(r"\.detach\s*\(\s*\)\.cpu\s*\(\s*\)\.numpy\s*\("), "block", "PyTorch detach/cpu/numpy canonical escape"),
    (re.compile(r"\.numpy\s*\("), "block", ".numpy() converts tensor state through NumPy"),
    (re.compile(r"np\.asarray\s*\("), "block", "np.asarray in canonical state path"),
    (re.compile(r"numpy\.asarray\s*\("), "block", "numpy.asarray in canonical state path"),
    (re.compile(r"np\.array\s*\("), "block", "np.array authors canonical state through NumPy"),
    (re.compile(r"numpy\.array\s*\("), "block", "numpy.array authors canonical state through NumPy"),
    (re.compile(r"np\.ndarray\b"), "block", "np.ndarray as canonical type"),
    (re.compile(r"numpy\.ndarray\b"), "block", "numpy.ndarray as canonical type"),
    (re.compile(r"jax\.device_get\s*\("), "warn", "jax.device_get may force host materialization"),
    (re.compile(r"\.tolist\s*\("), "warn", "tolist() can degrade tensor state to host lists"),
    (re.compile(r"pandas\.DataFrame\s*\("), "block", "pandas DataFrame as canonical state path"),
    (re.compile(r"pd\.DataFrame\s*\("), "block", "pd.DataFrame as canonical state path"),
    (re.compile(r"import\s+numpy\s+as\s+np"), "warn", "NumPy import requires boundary justification"),
    (re.compile(r"import\s+networkx\s+as\s+nx"), "warn", "NetworkX is projection/adapter only, not canonical Graph truth"),
    (re.compile(r"networkx\."), "warn", "NetworkX usage must stay projection/adapter only"),
    (re.compile(r"pickle\.(dump|load|dumps|loads)\s*\("), "warn", "pickle is unsafe for canonical artifacts"),
    (re.compile(r"to_csv\s*\("), "warn", "CSV should not be tensor/state authority"),
]
ALLOW = "lev-allow-numpy-boundary"
SCAN_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".mjs", ".jl"}
DEFAULT_EXCLUDE_PARTS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    "local_test_outputs",
    "local_test_outputs_v4",
    "local_test_outputs_v5",
    "source_uploads",
}
DEFAULT_EXCLUDE_FILES = {
    "numpy_contamination_scanner.py",
}
DEFAULT_EXCLUDE_SUBSTRINGS = {
    "examples/fixtures/",
}

def _is_excluded(file: Path, root: Path, extra_excludes: list[str]) -> bool:
    try:
        rel = file.relative_to(root)
    except ValueError:
        rel = file
    parts = set(rel.parts)
    if parts & DEFAULT_EXCLUDE_PARTS:
        return True
    if file.name in DEFAULT_EXCLUDE_FILES:
        return True
    rel_s = str(rel).replace("\\", "/")
    return any(ex and ex in rel_s for ex in extra_excludes) or any(ex in rel_s for ex in DEFAULT_EXCLUDE_SUBSTRINGS)

def scan(path: Path, extra_excludes: list[str] | None = None):
    extra_excludes = extra_excludes or []
    root = path if path.is_dir() else path.parent
    findings = []
    files = [path] if path.is_file() else [p for p in path.rglob("*") if p.suffix in SCAN_SUFFIXES]
    for file in files:
        if _is_excluded(file, root, extra_excludes):
            continue
        try:
            lines = file.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, start=1):
            allowed = ALLOW in line
            for rx, severity, reason in PATTERNS:
                if rx.search(line):
                    sev = "warn" if allowed else severity
                    findings.append({
                        "path": str(file),
                        "line": i,
                        "pattern": rx.pattern,
                        "severity": sev,
                        "reason": reason,
                        "allowedBoundary": allowed,
                        "text": line.strip()[:240]
                    })
    status = "block" if any(f["severity"] == "block" for f in findings) else ("warn" if findings else "pass")
    return {"status": status, "findings": findings}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail-on-block", action="store_true")
    ap.add_argument("--exclude", action="append", default=[], help="Substring path exclusion; repeatable")
    args = ap.parse_args()
    report = scan(Path(args.path), args.exclude)
    print(json.dumps(report, indent=2) if args.json else report)
    return 2 if args.fail_on_block and report["status"] == "block" else 0

if __name__ == "__main__":
    raise SystemExit(main())
