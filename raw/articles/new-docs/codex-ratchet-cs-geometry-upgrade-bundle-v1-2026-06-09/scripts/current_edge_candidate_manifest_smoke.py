#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root/'manifests/current_edge_candidate_library_set.json').read_text())
assert manifest['status'] == 'candidate_menu_not_install_order'
libs = manifest['libraries']
assert len(libs) >= 15
names = {x['name'] for x in libs}
for required in ['Catlab.jl','AlgebraicRewriting.jl','CombinatorialSpaces.jl','XGI','TopoNetX','GUDHI','egglog','PGMax','Orbax']:
    assert required in names, required
for item in libs:
    assert item['support_grade'] in {'A','B','C','D'}
    assert item['first_probe']
print(json.dumps({'ok': True, 'library_count': len(libs), 'required_present': True}, indent=2))
