#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    'codex_cs_curriculum_smoke.py',
    'current_edge_candidate_manifest_smoke.py',
    'codex_geometry_manifest_smoke.py',
    'library_sets_catalog_smoke.py',
    'mc_object_schema_smoke.py',
    'three_engine_agent_contract_smoke.py',
]
results=[]
for script in SCRIPTS:
    proc = subprocess.run([sys.executable, str(ROOT/script)], capture_output=True, text=True)
    try: out=json.loads(proc.stdout)
    except Exception: out={'stdout':proc.stdout,'stderr':proc.stderr}
    results.append({'script':script,'returncode':proc.returncode,'output':out})
passed=all(r['returncode']==0 for r in results)
print(json.dumps({'name':'run_codex_local_smokes','passed':passed,'results':results}, indent=2))
sys.exit(0 if passed else 1)
