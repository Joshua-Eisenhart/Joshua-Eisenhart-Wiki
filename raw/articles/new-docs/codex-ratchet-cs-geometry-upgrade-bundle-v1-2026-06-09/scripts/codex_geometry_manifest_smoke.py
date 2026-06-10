#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root/'manifests'/'codex_geometry_stack_manifest.json').read_text())
failures=[]
if manifest.get('promotion_allowed') is not False:
    failures.append('manifest promotion_allowed must be false')
ids=[x['id'] for x in manifest['build_order']]
for required in ['root_constraints','M_C_finite_admissibility_object','attractor_basin','physics_facing_metrics']:
    if required not in ids:
        failures.append(f'missing build stage {required}')
stage_index={x['id']:i for i,x in enumerate(manifest['build_order'])}
if stage_index['M_C_finite_admissibility_object'] > stage_index['attractor_basin']:
    failures.append('M(C) must precede attractor_basin')
if any(x.get('status') == 'admitted' for x in manifest.get('carrier_geometry_tower', [])):
    failures.append('carrier geometry tower must not contain admitted entries')
print(json.dumps({'name':'codex_geometry_manifest_smoke','passed':not failures,'failures':failures}, indent=2))
raise SystemExit(1 if failures else 0)
