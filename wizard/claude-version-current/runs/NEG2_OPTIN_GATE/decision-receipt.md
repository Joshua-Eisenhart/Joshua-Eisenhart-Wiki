# Decision receipt

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
evidence_boundary: |
  Names the bounded move and the surviving alternative. Does NOT prove the move
  succeeds — that is the Failure council's job. Subagent reading is evidence of
  scope, not of execution.
member_routes:
  - evidence-mapper (spawn_subagent, see linked Agent receipt)
  - controller synthesis of the surviving split
surviving_split: |
  Two admissible moves remain (A: edit in place, B: introduce a small adapter).
  Both survive; the owner decides. Not collapsed.
