#!/usr/bin/env python3
import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

STATE_PATH = Path('/Users/joshuaeisenhart/wiki/projects/codex-ratchet/_steward_state.json')
OUT_PATH = Path('/Users/joshuaeisenhart/wiki/projects/codex-ratchet/_steward_scan_latest.json')
MEMORY_DIR = Path('/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory')
REPO_DIR = Path('/Users/joshuaeisenhart/Desktop/Codex Ratchet')
WIKI_PROJECT_DIR = Path('/Users/joshuaeisenhart/wiki/projects/codex-ratchet')
WIKI_CONCEPTS_DIR = Path('/Users/joshuaeisenhart/wiki/concepts')
HARNESS_DIR = Path('/Users/joshuaeisenhart/wiki/wizard/harness-consolidated')
INDEX_PATH = HARNESS_DIR / '10_owner_doctrine_index.md'

BANNED = re.compile(r'\b(causes|creates|drives|produces|generates|forces|determines|makes)\b', re.I)
MD_LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
ABS_PATH = re.compile(r'`(/[^`]+)`')
WORD_RE = re.compile(r'\b\S+\b')


def run(cmd, cwd=None):
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"last_tick": None, "last_digest_date": None, "last_repo_commit": None}


def iso_to_dt(s):
    if not s:
        return None
    return datetime.fromisoformat(s)


def mtime_iso(path):
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat()


def changed_files_since(directory: Path, last_dt, exclude_names=None):
    out = []
    exclude_names = set(exclude_names or [])
    if not directory.exists():
        return out
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '_archive']
        for name in files:
            if name in exclude_names:
                continue
            p = Path(root) / name
            try:
                mt = datetime.fromtimestamp(p.stat().st_mtime).astimezone()
            except FileNotFoundError:
                continue
            if last_dt is None or mt > last_dt:
                out.append({
                    'path': str(p),
                    'mtime': mt.isoformat(),
                })
    out.sort(key=lambda x: x['mtime'])
    return out


def git_commits_since(repo: Path, last_dt):
    if not repo.exists():
        return []
    since = '' if last_dt is None else f"--since={last_dt.isoformat()}"
    cmd = f"git log --pretty=format:%H%x09%ad%x09%s --date=iso-strict {since}".strip()
    code, out, err = run(cmd, cwd=str(repo))
    if code != 0:
        return [{'error': err or out or 'git log failed'}]
    commits = []
    for line in out.splitlines():
        parts = line.split('\t', 2)
        if len(parts) == 3:
            commits.append({'hash': parts[0], 'date': parts[1], 'subject': parts[2]})
    return commits


def grep_banned(base: Path):
    hits = []
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d != '_archive']
        for name in files:
            if not name.endswith('.md'):
                continue
            if name == '03_language_discipline.md' or name == '_steward_log.md':
                continue
            p = Path(root) / name
            text = p.read_text(errors='ignore')
            for i, line in enumerate(text.splitlines(), start=1):
                if BANNED.search(line):
                    hits.append({'path': str(p), 'line': i, 'content': line.strip()})
    return hits


def unresolved_links(base: Path):
    issues = []
    for name in sorted(os.listdir(base)):
        if not name.endswith('.md'):
            continue
        p = base / name
        text = p.read_text(errors='ignore')
        for _, target in MD_LINK.findall(text):
            if target.startswith('http'):
                continue
            candidate = (p.parent / target).resolve()
            if not candidate.exists():
                issues.append({'path': str(p), 'target': target})
    return issues


def doctrine_paths_missing(index_path: Path):
    if not index_path.exists():
        return [{'path': str(index_path), 'missing': 'index file missing'}]
    text = index_path.read_text(errors='ignore')
    missing = []
    for path in ABS_PATH.findall(text):
        if not Path(path).exists():
            missing.append(path)
    return missing


def word_counts(base: Path):
    out = []
    for name in sorted(os.listdir(base)):
        if not name.endswith('.md'):
            continue
        p = base / name
        words = len(WORD_RE.findall(p.read_text(errors='ignore')))
        out.append({'file': name, 'words': words})
    return out


def primer_flags(counts):
    flags = []
    for row in counts:
        name, words = row['file'], row['words']
        if name == '00_READ_FIRST.md' and words > 300:
            flags.append({'file': name, 'words': words, 'limit': 300})
        elif name != 'README.md' and words > 500:
            flags.append({'file': name, 'words': words, 'limit': 500})
    return flags


def main():
    state = load_state()
    last_dt = iso_to_dt(state.get('last_tick'))
    now = datetime.now().astimezone()
    summary = {
        'now': now.isoformat(),
        'last_tick': state.get('last_tick'),
        'memory_changes': changed_files_since(MEMORY_DIR, last_dt),
        'repo_commits': git_commits_since(REPO_DIR, last_dt),
        'wiki_project_changes': changed_files_since(WIKI_PROJECT_DIR, last_dt, exclude_names={'_steward_log.md', '_steward_state.json', '_steward_scan_latest.json'}),
        'wiki_concept_changes': changed_files_since(WIKI_CONCEPTS_DIR, last_dt),
    }
    counts = word_counts(HARNESS_DIR)
    summary['audit'] = {
        'banned_hits_harness': grep_banned(HARNESS_DIR),
        'banned_hits_project': grep_banned(WIKI_PROJECT_DIR),
        'unresolved_harness_links': unresolved_links(HARNESS_DIR),
        'missing_doctrine_paths': doctrine_paths_missing(INDEX_PATH),
        'word_counts': counts,
        'primer_limit_flags': primer_flags(counts),
    }
    OUT_PATH.write_text(json.dumps(summary, indent=2))
    print(str(OUT_PATH))

if __name__ == '__main__':
    main()
