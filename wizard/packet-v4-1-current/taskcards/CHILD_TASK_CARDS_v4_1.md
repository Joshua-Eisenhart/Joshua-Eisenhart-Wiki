---
title: Wizard v4.1 Child Task Cards
type: task_cards
packet: v4.1
framing: standalone
---

# Wizard v4.1 Child Task Cards

Every parent-launched child receives this minimum card:

- parent route summary;
- exact child id;
- exact mini-MMM slice or sparse registry slice plus definition row;
- route-bound council-member skill when assigned;
- source/tool slice;
- one required output shape;
- one falsifier or check;
- receipt id and parent id.

Children do not load sibling routes or the full main MMM unless explicitly
assigned a gate or aggregator role.

## Formal Child Groups

- `failure.premortem_council`: `premortem.likely_failure`,
  `premortem.dangerous_failure`, `premortem.hidden_assumption`,
  `premortem.early_warning`, `premortem.revised_plan`,
  `premortem.sim_evidence_corruption`.
- `failure.falsifier_council`: `voice.popper`, `voice.pushback`,
  `failure.calibration`, `guard.receipt_audit`, `guard.boundary_check`.
- `follow_up.lane_council`: `lane.direct`, `lane.alternative`,
  `lane.reframe`, `lane.back`, `lane.wildcard`,
  `lane.all_of_the_above`.

If a child lacks an exact mini-MMM file, the sparse registry slice plus the
definition row is the required salience source. If both are missing, the child
is blocked and the parent cannot count it as accepted.

Compact child loading means compact member mini-MMM under
`mmm/mini/compact/...`, not the compact main MMM. Child receipts keep
`loaded_salience.full_mmm` empty unless the child was explicitly assigned a
gate or aggregator role that requires broader boot.
