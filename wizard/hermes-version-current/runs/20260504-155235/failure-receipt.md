# Failure Receipt

run_id: 20260504-155235
mode: REAL_ATTEMPT
wave: Failure
parent_route_id: failure-parent
input_receipts: decision-receipt.md
model_request: gpt-5.5 low requested if runtime supports it
model_observed: parent=session gpt-5.5 per runtime metadata; child routes reported model=gpt-5.5 by delegate_task
artifact_surface: terminal summary written by controller
nested_visibility: reported_by_parent; child summaries and delegate metadata visible; raw child transcripts not visible

## Member routes

| route_id | label | role | status | failure / hardening finding | evidence_boundary |
|---|---|---|---|---|---|
| popper-falsifier | 🧨 Popper/falsifier | child member | completed | Harden before proceed: “Hermes-native Wizard harness exists” is not enough; controller must name an executable validation path plus live receipt source before any smoke-run claim. | Child-reported finding from Decision context; parent saw summary/tool metadata only, not raw nested transcript. |
| pushback-boundary | 🛑 Pushback/boundary | child member | completed | Harden scope: acceptable only if constrained to read-only verification until a concrete failure is reproduced; minimum fix plus one bounded smoke run must not broaden into general v4.1 cleanup or infer nested transcript contents. | Child-reported finding from context; parent saw summary/tool metadata only, not raw nested transcript. |
| premortem-future-failure | 🪦 Premortem/future failure | child member | completed | Harden future artifact risk: require unique bounded run dir and explicit fixture/receipt-only vs live-Hermes visibility labels before route/status summary. | Child-reported finding from Decision context; parent saw summary/tool metadata only, not raw nested transcript. |

## Verdict

harden

## Required hardening

1. Verify the Hermes-native Wizard harness exists before repair.
2. Name an executable validation path.
3. Start read-only, then write only scoped harness/run artifacts.
4. Use one unique run directory.
5. Distinguish live-Hermes execution, fixture/receipt replay, and parent-reported summaries.
6. Do not claim raw nested transcript visibility.

## Evidence boundary

This Failure parent consumed the Decision receipt at:
/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260504-155235/decision-receipt.md

This route spawned three child member routes through delegate_task. The parent received child summaries, model metadata, and tool-call metadata only. Raw child transcripts and raw nested tool outputs were not visible.
