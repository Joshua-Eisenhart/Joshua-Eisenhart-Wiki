# Decision receipt (NEG10 — phantom-leaf spawner)

# NEGATIVE fixture NEG10: this is a SPAWNING Decision/council receipt that
# self-labels surface_kind:agent AND claims action_class spawn_subagent AND
# carries a parent_receipt AND omits linked_receipt — exactly the phantom-leaf
# shape that the cycle-2 leaf early-return wrongly exempted. It is NOT the spawn
# target of any other receipt's linked_receipt; it IS the spawner. The fixed
# validator must reject this: a receipt that itself claims spawn_subagent and is
# not anyone's spawn target ALWAYS requires a linked_receipt and full
# provenance — no leaf exemption for spawners.
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
