# Agent receipt — evidence-mapper (FORGED PARENT fixture)

# NEGATIVE fixture NEG4: this Agent receipt carries all the correct surface
# fields (surface_kind: agent, action_class: spawn_subagent, agent_id) but its
# parent_receipt points at a STALE id that does NOT match the spawning Decision
# receipt id (dec-20260613-01). A forged/stale Agent receipt that does not name
# the actual spawn as its parent must be REJECTED.
id: agent-20260613-evmap
surface_kind: agent
action_class: spawn_subagent
runtime_target: agent
agent_id: evidence-mapper
status: completed
support_level: observed
parent_receipt: dec-20260601-STALE-NOT-THIS-SPAWN
task_card: |
  goal: map which files/claims bound the requested change
  scope: read-only scan of the 3 candidate paths
  out_of_scope: edits, commits, promotion
what_checked:
  - candidate path A (in-place edit target)
  - candidate path B (adapter seam)
conclusion: both seams are valid in isolation; neither excludes the other yet
remains_open:
  - which seam the owner prefers
artifacts:
  - none (read-only scan)
evidence_boundary: read-only; proves scope/surface, not execution success
