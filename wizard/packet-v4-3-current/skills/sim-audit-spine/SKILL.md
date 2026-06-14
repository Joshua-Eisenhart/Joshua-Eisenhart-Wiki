# Sim Audit Spine Skill v4.3

authority_status: canonical-skill

Keep Codex Ratchet sim/proof/workflow claims from collapsing builder output,
mechanical gates, fabrication audit, and final claim ceiling into one self-
grading lane.

## When Used

Use for sim, proof, workflow, result, terrain/operator, queue, or claim-confirming
Wizard work, especially when JAX/Julia parity, SMT proof, or Claude/Gemini/worker
reports look clean enough to tempt promotion.

## Method

1. Classify the exact claim, required gate, allowed status label, and blocked
   consumers before building.
2. Separate roles: state archaeologist, builder, mechanical gatekeeper,
   fabrication auditor, SMT/proof engineer, and controller synthesis.
3. Builders may author or run artifacts, but never admit or audit their own work.
4. Mechanical gates report exact command, verdict, and artifact path; green gates
   are necessary but not sufficient.
5. Fabrication audit re-derives from source/result artifacts and checks hardcoded
   deltas, decorative tools, name-overclaim, planted oracles, and parity-as-proof.
6. SMT proof requires a real/erased verdict flip on z3 and cvc5 with polarity
   named; UNSAT alone is not enough.
7. Final synthesis states the weakest honest ceiling and blocked consumers.

## Return Fields

```yaml
sim_audit_spine:
  claim: ""
  state_paths_read: []
  builder_lane: ""
  mechanical_gates: []
  fabrication_audit: ""
  smt_flip: ""
  accepted_status_label: ""
  blocked_consumers: []
  next_unblocked_step: ""
```

Also include the common child receipt fields required by `WIZARD_v4_3.md`:
child role id, compact MMM loaded, required mini-MMMs loaded, source slice,
evidence boundary, output patch, and status.

## Invalid Outputs

- Builder report treated as verification.
- JAX/Julia parity treated as proof or admission.
- Mechanical green gate treated as canonical by itself.
- Stale torch/PyTorch gate drift patched with decorative torch.
- Layer, manifold, basin, flux, Axis0, bridge, physics, or completion wording
  without the dedicated repo claim gate and evidence packet.
