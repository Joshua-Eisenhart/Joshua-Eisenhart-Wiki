#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
data = json.loads((root/'manifests/codex_cs_layer_curriculum.json').read_text())
assert 'graph_theory' in data['classes']
assert 'e_graphs_equality_saturation' in data['classes']
assert data['build_order'][0] == 'finite_carrier'
assert data['build_order'][-1] == 'gnn_ai_after_explicit_graph_object'
assert len(data['immediate_probe_queue']) >= 8
print(json.dumps({'ok': True, 'classes': len(data['classes']), 'queue': len(data['immediate_probe_queue'])}, indent=2))
