# Decision receipt (NEG9 — path-escape containment)

# NEGATIVE fixture NEG9: this SPAWNING Decision receipt claims action_class
# spawn_subagent but provides NO Agent receipt of its own. Instead its
# linked_receipt traverses OUT of this run dir via '..' to borrow a SIBLING
# run's Agent receipt (SMOKE_TOPOLOGY_20260613/agent-evidence-mapper.md). The
# fixed validator must reject this: the linked Agent receipt MUST be a *.md file
# directly inside THIS run dir — an absolute path or a '..' traversal into
# another run cannot satisfy provenance (a spawn cannot borrow another run's
# Agent receipt). NOTE: this run dir intentionally contains NO local
# agent-evidence-mapper.md.
id: dec-20260613-01
wave: Decision
surface_kind: council
action_class: spawn_subagent
runtime_target: agent
status: completed
support_level: observed
target: choose the smallest useful bounded move for the requested change
linked_receipt: ../SMOKE_TOPOLOGY_20260613/agent-evidence-mapper.md
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
  - evidence-mapper (spawn_subagent, but linked receipt escapes the run dir)
  - controller synthesis of the surviving split
surviving_split: |
  Two admissible moves remain (A: edit in place, B: introduce a small adapter).
  Both survive; the owner decides. Not collapsed.
