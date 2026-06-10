#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
cat = json.loads((root/'manifests'/'codex_three_engine_agent_catalog.json').read_text())
failures=[]
provider_ids={p['providerId'] for p in cat['providers']}
for required in ['lev-sim-julia','lev-sim-jax','lev-sim-torch','lev-proof-solver']:
    if required not in provider_ids:
        failures.append(f'missing provider {required}')
for p in cat['providers']:
    joined=' '.join(p.get('must_not',[])).lower()
    if 'admission' not in joined and 'proof' not in joined and 'mutate graph' not in joined:
        failures.append(f'provider {p["providerId"]} lacks authority boundary')
for a in cat['agent_roles']:
    if a.get('authority') in {'admit','accept','close'}:
        failures.append(f'agent {a["agentId"]} has forbidden authority {a["authority"]}')
if 'No agent or engine self-approves' not in cat.get('fan_in_rule',''):
    failures.append('fan_in_rule must forbid self approval')
print(json.dumps({'name':'three_engine_agent_contract_smoke','passed':not failures,'failures':failures}, indent=2))
raise SystemExit(1 if failures else 0)
