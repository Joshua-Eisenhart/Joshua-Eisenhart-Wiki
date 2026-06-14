# Decision receipt (NEG10B — DONATED leaf-exemption bypass)

# BYPASS fixture NEG10B (re-attack of the phantom-leaf fix). Identical to NEG10
# (a SPAWNING receipt that self-labels surface_kind:agent + claims
# action_class spawn_subagent + carries a parent_receipt + omits linked_receipt,
# so it produces NO real Agent leaf) EXCEPT the controller_local Follow-Up
# receipt carries one stray `linked_receipt: decision-receipt.md` line. That line
# puts this filename into `linked_targets` (validate_claude_wizard_run.py:499-503
# collects linked_receipt from EVERY receipt with no guard on the pointer's
# action_class/validity), so `is_spawn_target` is True and the leaf exemption at
# :364 fires (is_spawn_target AND has_parent AND not claims_onward_spawn). The
# phantom spawner is exempted from provenance and the run PASSES with no Agent
# receipt anywhere. The fix is circumvented: leaf-exemption can be DONATED by any
# receipt — even one never itself subjected to provenance — that merely names the
# spawner.
id: dec-20260613-01
wave: Decision
surface_kind: agent
action_class: spawn_subagent
runtime_target: agent
status: completed
support_level: observed
parent_receipt: dec-20260613-00
target: choose the smallest useful bounded move for the requested change
claimed_status: runs
proven_status: runs
status_label: runs
success_check: a single bounded next move named with owner, target, and output surface
stop_if: no live alternative survives, or scope cannot be bounded
evidence_boundary: |
  EVASION UNDER TEST: a spawning council/decision receipt masquerading as a leaf
  agent. It has a parent_receipt and no linked_receipt, so the OLD leaf
  early-return ('has parent AND no linked -> skip provenance') let it pass with
  NO real Agent leaf produced. A genuine leaf is named by its spawner's
  linked_receipt; this receipt is named by no one, so it is a SPAWNER and must
  carry a linked Agent receipt + full provenance.
member_routes:
  - evidence-mapper (claimed spawn_subagent — but no linked Agent receipt exists)
  - controller synthesis of the surviving split
surviving_split: |
  Two admissible moves remain (A: edit in place, B: introduce a small adapter).
  Both survive; the owner decides. Not collapsed.
