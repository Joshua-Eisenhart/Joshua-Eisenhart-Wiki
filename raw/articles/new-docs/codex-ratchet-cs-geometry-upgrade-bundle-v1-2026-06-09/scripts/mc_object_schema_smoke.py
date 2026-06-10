#!/usr/bin/env python3
import json
from pathlib import Path
try:
    import jsonschema
except Exception as e:
    print(json.dumps({'name':'mc_object_schema_smoke','passed':False,'failures':[f'jsonschema missing: {e}']}, indent=2)); raise SystemExit(1)
root=Path(__file__).resolve().parents[1]
schema=json.loads((root/'schemas'/'codex.mc-object.v0.schema.json').read_text())
valid={
 'objectId':'mc://example-v0','finiteCarrier':{'stateSetRef':'artifact://state','operatorSetRef':'artifact://ops','probeSetRef':'artifact://probes','pathSetRef':'artifact://paths'},
 'constraints':['F01','N01'],'readoutMap':{'quotientRef':'artifact://quot','readoutRefs':['artifact://readout']},
 'admissibilityPredicate':{'predicateRef':'gate://predicate','gateProofRequired':True},
 'composition':{'bracketPolicy':'explicit_tree','noncommuting':True,'nonassociativePolicy':'fenced_carrier_pressure'},
 'controls':['carrier-erasure'],'receiptRefs':[],'promotion':{'allowed':False,'status':'scratch'}
}
bad=dict(valid); bad['objectId']='bad-id'
failures=[]
try: jsonschema.validate(valid, schema)
except Exception as e: failures.append(f'valid rejected: {e}')
try:
    jsonschema.validate(bad, schema); failures.append('bad objectId accepted')
except Exception: pass
print(json.dumps({'name':'mc_object_schema_smoke','passed':not failures,'failures':failures}, indent=2))
raise SystemExit(1 if failures else 0)
