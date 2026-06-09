🧙 Hermes Wizard v4.1 — REAL_ATTEMPT_PARTIAL — wide councils ran, raw child proof still bounded

What changed
Option 4 ran: Decision, Failure, and Follow-Up each used multiple parent/member routes, and the run now has a stricter validator for wide-council partial fixtures.

Best next move
✅ Keep this as the first useful Hermes wide-council fixture, then make the next fixture machine-readable enough to upgrade child/subchild proof from parent-reported to artifact-verified.

Why this is the best move
- 🧠 Decision: chose the right target — validator-first wide fixture, not another thin one-parent-per-council smoke.
- 🛡️ Failure: caught the real risk — parent-reported children and prose receipts can still fake confidence unless evidence tiers and graph checks stay explicit.
- 🧭 Follow-Up: generated the execution path — harden validator, preserve PARTIAL status, render prompt-ready next moves, and stop any FULL overclaim.

🧠 Decision
Members: Decision 7/7 — Strategy, Systems, Factory, Hume/evidence, Feynman/testability, Zhuangzi/alternatives, Outside evaluator.
Result: build a wide-council fixture with compact envelopes, dependency wiring, visible alternatives, and explicit proof boundaries.
What changed: the run no longer treats one parent per council as v4.1 coverage.
Proof: decision-wide-receipt.md.
Boundary: child/subchild work is summarized by the parent; raw child evidence was not checked.

🛡️ Failure
Members: Failure 6/6 — Popper, Pushback, Premortem, Black/Red Hat, Calibration, Receipt audit.
Result: proceed only after adding validator checks.
What changed: `completed_accepted` is demoted to parent-reported completed unless raw artifacts exist.
Proof: failure-wide-receipt.md.
Boundary: some Failure child probes were evidence-degraded, then key boundary routes were rerun with file access; raw child/subchild transcripts remain unavailable.

🧭 Follow-Up
Members: Follow-Up 7/7 — Direct, Alternative/Reframe, Wildcard, All-C, Compile gate, Orwell, Factory/Strategy handoff.
Result: prompt-ready options were generated, but Compile Gate correctly failed the pre-output state until the controller wrote this final render and the stricter validator.
What changed: Follow-Up is now doing next-prompt automation, not merely listing route names.
Proof: followup-wide-receipt.md.
Boundary: still REAL_ATTEMPT_PARTIAL, not full v4.1.

✅ Compiled move
Target: Hermes-native v4.1 wide-council fixture.
Immediate action: use `validate_hermes_wizard_wide_run.py` to validate this run as PARTIAL and reject one-parent-per-council overclaims.
Owner/lane: Hermes controller / validator-hardening lane.
Success check: validator passes this run only as a wide-council partial fixture; it requires Decision 7/7, Failure 6/6, Follow-Up 7/7, evidence-tier labels, dependency wiring checks, and negative-fixture markers.
Stop condition: stop if parent_reported is upgraded to controller_visible, artifact_verified, or test_passed without raw evidence; stop if the render implies full v4.1 coverage.
Artifact/output: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733/
Status: ready_for_validation.
Evidence boundary: this proves wide parent/member council coverage in this Hermes run, with parent-reported child/subchild summaries. It does not prove raw child/subchild transcripts, test_passed validator semantics beyond the local script, Codex Max Assembly, or full v4.1 conformance.

Validator gates added
- Evidence tiers must stay distinct: parent_reported, controller_visible, artifact_verified, test_passed.
- Dependency wiring must be visible: node IDs, edge lists, DAG/no cycle checks, no future-council dependency, existing deps only, sibling deps where claimed.
- Negative fixtures must be named: one-parent overclaim, missing child, wrong-parent child, hidden child, orphan child, malformed edge, cycle, future dependency, collapsed alternatives.
- Partial/degraded child status must not be normalized into success.
- Mock, fallback, synthetic, partial, or unavailable topology must not be rendered as actual/live/full topology.

Follow-up — pick a number
1. 🧪 Machine-readable fixture: “Turn the three wide receipts into JSON/YAML envelopes with node IDs, edge lists, evidence tiers, and per-child visibility.”
   Payoff: makes the next validator check structure instead of markdown strings.
   Use when: you want stronger machine proof.
   Stop if: raw child artifacts are still unavailable and the schema starts pretending otherwise.
2. 🔬 Child-proof upgrade: “Test whether Hermes can expose raw nested child receipt IDs or transcript artifacts from orchestrator subagents.”
   Payoff: resolves the biggest remaining proof gap.
   Use when: you want to move beyond parent-reported child summaries.
   Stop if: delegate_task backend does not expose nested artifacts.
3. ✅ Closeout: “Promote validate_hermes_wizard_wide_run.py and this run shape into the hermes-wizard skill as the default wide REAL_ATTEMPT_PARTIAL path.”
   Payoff: future Wizard runs stop falling back to thin topology.
   Use when: this fixture is acceptable as the baseline.
   Stop if: you want a JSON/YAML fixture first.
4. 🔗 All-C: “Do 1 -> 2 -> 3: make the fixture machine-readable, probe raw child proof, then promote the durable path.”
   Payoff: best route from partial working fixture to stronger runtime proof.
   Use when: you want this hardened rather than just demonstrated.
   Stop if: machine-readable validation fails.

Proof strip
Run: /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-165733
Receipts: run-plan.md, decision-wide-receipt.md, failure-wide-receipt.md, followup-wide-receipt.md, final-render.md
Validator: conformance/validate_hermes_wizard_wide_run.py
Mode: REAL_ATTEMPT_PARTIAL
Wide council coverage: Decision 7/7, Failure 6/6, Follow-Up 7/7
Nested visibility: parent-reported / reported_by_parent
Model: gpt-5.5 reported by delegate_task metadata; effort not independently verified
Limit: not full v4.1, not Codex Max Assembly, no independently checked raw child evidence
