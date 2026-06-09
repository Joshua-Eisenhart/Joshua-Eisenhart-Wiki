# Hermes Wizard wide-council run plan

run_id: 20260504-165733
mode: REAL_ATTEMPT_PARTIAL unless raw nested child receipts become controller-visible
selected_option: prior Follow-up option 4 / All-C

Goal:
Run a wider Hermes-native v4.1 fixture:

1. Decision Council: multiple parent/member routes, run before barrier returns.
2. Failure Council: consumes Decision receipt, multiple parent/member routes.
3. Follow-Up Council: consumes Decision + Failure receipts, multiple parent/member routes and preworked next prompts.
4. Validator: fail one-parent-per-council runs that claim v4.1 coverage; pass this run only as wide parent coverage with parent-reported child/subchild visibility unless controller-visible raw child receipts are available.

Concurrency note:
Hermes delegate_task parent batches may be limited by runtime concurrency. If so, parent members run in rolling parallel batches inside the same council barrier. The council does not return until all selected parent members complete or are blocked.

Decision selected members:
- Strategy
- Systems
- Factory
- Hume
- Feynman
- Zhuangzi
- Outside evaluator

Failure selected members:
- Popper
- Pushback
- Premortem
- Black/Red Hat
- Calibration
- Receipt audit

Follow-Up selected members:
- Direct option maker
- Alternative/Reframe maker
- Wildcard maker
- All-C composition
- Compile gate
- Orwell wording
- Factory/Strategy handoff

Child/subchild target:
Each parent member should attempt two narrower child/subchild probes if orchestrator delegation is available; otherwise mark child route blocked/degraded with reason. Main controller only accepts child proof as raw if returned by tool-visible child receipts; parent self-report remains `reported_by_parent`.
