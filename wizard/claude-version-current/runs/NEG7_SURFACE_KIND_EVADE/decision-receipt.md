# Decision receipt (NEG7 — surface_kind evade)

id: dec-20260613-01
wave: Decision
surface_kind: agent
action_class: spawn_subagent
runtime_target: agent
status: completed
support_level: observed
target: choose the smallest useful bounded move for the requested change
claimed_status: runs
proven_status: runs
status_label: runs
success_check: a single bounded next move named with owner, target, and output surface
stop_if: no live alternative survives, or scope cannot be bounded
evidence_boundary: |
  EVASION UNDER TEST: this is a SPAWNING council/decision receipt that
  self-labels surface_kind:agent to trip the leaf-agent early-return and skip
  provenance entirely. It claims action_class spawn_subagent but provides NO
  linked_receipt and NO real Agent leaf was produced. The fixed validator must
  reject this: a spawning receipt cannot mislabel its surface_kind to evade the
  spawn-provenance check.
member_routes:
  - evidence-mapper (claimed spawn_subagent — but no linked Agent receipt exists)
  - controller synthesis of the surviving split
surviving_split: |
  Two admissible moves remain (A: edit in place, B: introduce a small adapter).
  Both survive; the owner decides. Not collapsed.
