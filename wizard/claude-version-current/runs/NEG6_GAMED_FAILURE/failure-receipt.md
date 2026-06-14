# Failure receipt (GAMED FAILURE-PATH fixture)

# NEGATIVE fixture NEG6: route_action_classes lists blocked + superseded so the
# coarse failure-path check passes, but the structured routes carry NO reason.
# Listing the action classes alone is gameable — the reason-per-route check must
# REJECT this.
id: fail-20260613-01
wave: Failure
surface_kind: council
action_class: controller_local
runtime_target: claude_controller
status: partial
support_level: observed
target: name the strongest falsifier/blocker for the Decision move and resolve it
input_receipts:
  - dec-20260613-01
claimed_status: runs
proven_status: runs
status_label: runs
success_check: each surviving move is either hardened-then-executable or honestly blocked
stop_if: the only move left is unfalsifiable hand-waving
decision: split — one move hardened, one blocked
route_action_classes:
  - blocked
  - superseded
member_routes:
  - premortem-agent (controller-local pass; no subagent needed here)
  - falsifier-agent (controller-local pass)
routes:
  - name: move-A-in-place
    action_class: superseded
  - name: move-B-adapter
    action_class: blocked
evidence_boundary: |
  Proves the falsifier ran and classified each route. Does NOT prove move-B
  works — it is blocked pending owner input.
