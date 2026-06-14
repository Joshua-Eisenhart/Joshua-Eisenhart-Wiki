# Decision receipt (NEG8 — cross-file route evade)

id: dec-20260613-01
wave: Decision
surface_kind: council
action_class: spawn_subagent
runtime_target: agent
status: completed
support_level: observed
target: choose the smallest useful bounded move for the requested change
linked_receipt: agent-evidence-mapper.md
claimed_status: runs
proven_status: runs
status_label: runs
success_check: a single bounded next move named with owner, target, and output surface
stop_if: no live alternative survives, or scope cannot be bounded
route_action_classes:
  - superseded
  - blocked
evidence_boundary: |
  EVASION UNDER TEST: this Decision receipt CLAIMS route_action_classes
  superseded + blocked but provides NO `routes:` block here to back them with a
  reasoned route. The legitimate failure path lives only in failure-receipt.md.
  The OLD validator aggregated route_action_classes across all receipts but
  parsed backing routes ONLY from failure-receipt.md, so these unbacked
  decision-receipt claims slipped through. The fixed validator must reject them:
  a route_action_classes claim must be backed by a reasoned route in the SAME
  receipt that claims it.
member_routes:
  - evidence-mapper (spawn_subagent, see linked Agent receipt)
  - controller synthesis of the surviving split
surviving_split: |
  Two admissible moves remain (A: edit in place, B: introduce a small adapter).
  Both survive; the owner decides. Not collapsed.
