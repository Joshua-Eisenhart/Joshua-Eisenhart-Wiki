#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
cat=json.loads((root/'manifests'/'codex_library_sets_full_catalog.json').read_text())
failures=[]
sets=cat.get('sets',{})
for s in ['julia_core_canon','jax_workers','pytorch_workers','typescript_lev_world']:
    if s not in sets:
        failures.append(f'missing set {s}')
checks=[('julia_core_canon','adopt','DLPack.jl'),('julia_core_canon','dynamics_basin','Attractors.jl'),('jax_workers','adopt','diffrax'),('pytorch_workers','adopt','torch_geometric'),('typescript_lev_world','adopt','graphology')]
for group, section, item in checks:
    if item not in sets.get(group,{}).get(section,[]):
        failures.append(f'missing {item} in {group}.{section}')
print(json.dumps({'name':'library_sets_catalog_smoke','passed':not failures,'failures':failures}, indent=2))
raise SystemExit(1 if failures else 0)
