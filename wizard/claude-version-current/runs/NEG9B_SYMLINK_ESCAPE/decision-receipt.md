# Decision receipt (NEG9B — SYMLINK path-escape bypass)

# BYPASS fixture NEG9B: this SPAWNING Decision receipt claims action_class
# spawn_subagent and provides NO Agent receipt of its own. Its linked_receipt is
# the BARE in-dir name `agent-evidence-mapper.md` — which is a SYMLINK directly
# inside this run dir pointing OUT to a SIBLING run's Agent receipt
# (../SMOKE_TOPOLOGY_20260613/agent-evidence-mapper.md). The current containment
# gate checks `linked_pp.is_absolute()` (false — bare name), `'..' in
# linked_pp.parts` (false — bare name), and `contained.resolve() not in
# run_md_set`. But run_md_set is built by glob('*.md') which MATCHES the symlink,
# and BOTH sides .resolve() FOLLOW the symlink to the same sibling target, so the
# membership test PASSES. The spawn then borrows the sibling run's Agent receipt
# via a symlink — escape still resolves + validates.
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
  - evidence-mapper (spawn_subagent; linked receipt is a symlink escaping the run dir)
  - controller synthesis of the surviving split
surviving_split: |
  Two admissible moves remain (A: edit in place, B: introduce a small adapter).
  Both survive; the owner decides. Not collapsed.
