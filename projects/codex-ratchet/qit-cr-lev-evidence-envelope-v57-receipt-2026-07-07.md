# CR->Lev QIT evidence envelope (audit_engines lane, bundle v57) — 2026-07-07

Status: repo-grounded scratch diagnostic. Not canon, not Axis-0, not FEP, not
Lev mesh runtime admission, graph mutation, ontology writing, or production
perception. Evidence-only.

## What this is

Lev implemented a host evidence boundary (`qit-evidence-consumer.ts`) that
consumes Codex-Ratchet QIT envelopes as host-owned **evidence-only** receipts
and blocks any envelope that overclaims promotion / graph mutation / runtime
object creation, or that omits `blocked_consumers` + an explicit
`lev_host_consumer_contract`.

This receipt records the CR-side emitter in the `audit_engines` bundle lane
(`constraint_core_unified` v57) that produces a conformant envelope from the
CURRENT engine results — the corrected non-circular polarity readouts and the
source-fidelity linter, refreshing what codex's Phase-3 envelope carried from
bundle v55.

## Emitter

`sims_and_scripts/lev_qit_evidence_envelope_emitter.py` reads this bundle's
engine result JSONs and emits `lev.qit_engine_perception_evidence.v1` with:

- `lev_host_consumer_contract`: truth_state=proposed, evidence_kind=measurement,
  decision_ceiling=accepted_as_evidence_only, graph/compositor/mesh/source-boundary/
  entity-id all false.
- `blocked_consumers`: graph admission, mesh projection, ontology writer, MMM
  driver authority, local-verifier quorum, Axis0/FEP closure, runtime object factory.
- deep-audit-55 claim-language fields: mechanical_run_status, source_fidelity_status,
  dynamic_claim_status, promotion_status=scratch_diagnostic.

## Real tooth (not prose)

The emitter self-validates the envelope conforms to the host boundary, and a
**falsifiable control** builds a promoting twin (`truth_state=canon`,
`graph_mutation_allowed=true`, `promotion_status=earned`) which the SAME
validator rejects (4 problems). A validator that cannot reject the promoting
twin would be a rubber stamp.

## Payload (current bundle numbers)

- stage re-identification rate: 0.6875 (separation 0.6203 over shuffled)
- object binding accuracy: 0.7917 (1.0 on non-degenerate; all misses genuine degeneracies)
- Type-1 polarity −0.019 vs Type-2 +0.011 (opposite, not a Bloch relabeling of each other)
- schedule source-fidelity linter: PASS (running sims consume source-faithful slots)
- formation-loss sum (defined components): 1.706

## Verification

Harness: `101 pass / 0 fail / 0 skip GREEN` (constraintcore full harness).
Emitter gate: `LEV EVIDENCE ENVELOPE CONFORMS: True`; promoting-twin control rejected.

## Honest interpretation

This closes the CR→Lev evidence loop from the audit_engines lane: my
scratch-diagnostic measurements are now packaged so Lev can consume them as
host receipts only. It does not create Lev objects, mutate the mesh, or make
any truth/promotion claim.
