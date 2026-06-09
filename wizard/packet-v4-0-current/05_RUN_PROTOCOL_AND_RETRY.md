---
title: Wizard v4.1 Run Protocol and Retry Rules
type: run_protocol
packet: v4.1
framing: standalone
---

# Run Protocol And Retry Rules v4.1

The basic Wizard run should not be the hard part.

The runtime loads MMMs, assigns bounded member cards, runs the workers, collects receipts, retries bad lanes, and renders a clear answer.

## Full Run Minimum

A full visible Wizard run needs:

1. Main thread loaded `mmm/FULL_MMM_v4_0.md`.
2. Decision Council ran dedicated parent members for the divergent voices, relevant Six Thinking Hats, and at least one expert lens.
3. Failure Council ran dedicated parent members for Black/Red Hats, premortem, falsifier/pushback voices, and at least one expert lens.
4. Follow-Up Council ran dedicated parent members for lanes, at least one composition, compile guard, and the wording/strategy/factory voices.
5. Each visible parent member loaded an exact mini-MMM slice.
6. Each required parent either completed, blocked with a reason, or was retried smaller.
7. At least one child/subsubagent route was attempted for each council when the runtime supports children.
8. Each accepted parent member reports `member_utility`: distinct contribution, decision use, sim relevance, theater cut, current disposition, and reboot note.
9. Follow-up options passed the universal bounded-work compile gate.
10. The final answer includes a run header, council notation, score, and follow-up prompts.

If any required item is missing, the run is not full. Mark it partial, retry, or show the blocker.

## Partial Run Minimum

A partial visible run needs:

1. Main thread loaded the full MMM.
2. At least one Decision member, one Failure member, and one Follow-Up member ran or were explicitly blocked.
3. The final option passed the universal compile gate or was marked blocked/deferred.
4. The answer does not claim full run.

v4.0 has no compact mode yet. Do not use `COMPACT` in headers or route names until a separate compact spec exists.

## Council Member Assignment

Decision Council should usually draw from:

- `voice.hume`
- `voice.zhuangzi`
- `voice.feynman`
- `voice.factory`
- `voice.strategy`
- `voice.systems`
- `six_hat.blue`
- `six_hat.white`
- `six_hat.yellow`
- `six_hat.green`
- `expert.what_experts_say`
- `expert.outside_evaluator`
- `lane.direct`
- `lane.alternative`
- `lane.reframe`

Failure Council should usually draw from:

- `six_hat.black`
- `six_hat.red`
- `voice.popper`
- `voice.feynman`
- `voice.pushback`
- `failure.premortem`
- `failure.postmortem`
- `failure.security_audit`
- `failure.calibration`
- `expert.what_experts_say`
- `expert.domain_specialist`
- `guard.receipt_audit`
- `guard.security`

Follow-Up Council should usually draw from:

- `voice.orwell`
- `voice.strategy`
- `voice.factory`
- `lane.direct`
- `lane.alternative`
- `lane.reframe`
- `lane.back`
- `lane.wildcard`
- `composition.all_a_build`
- `composition.all_b_divergence`
- `composition.all_c_closeout`
- `composition.max_assembly`
- `guard.compile_gate`
- `guard.hygiene`
- `expert.operator`

All visible full runs should use dedicated parent workers for assigned voices, hats, failure lenses, expert lenses, lanes, compositions, and guards. Controller synthesis may summarize them, but it cannot replace them.

## Child/Subsubagent Rule

Parent workers spawn children only for narrower work:

- inspect one source slice;
- test one claim;
- run one tool surface;
- compare one alternative;
- audit one receipt;
- compile one follow-up option.

Children do not synthesize the whole answer.

Children do not count unless their parent launch and child completion are both represented in receipts.

Tool or harness checks are separate from child/subsubagent routes. They may appear as `tools:{n}` or verification, but they do not satisfy the child route requirement.

If child routes are expected but not launched, the visible header must show the missed obligation. For example, a three-council run with no child receipts should use `children:0/3 not-run`, not `children:0/0 not-run`.

## Visible Output Repair Rule

The main thread must repair the visible answer before sending it. This is not optional polish; it is part of the run protocol.

Minimum repair checklist:

- real section headers: `## ✨ Answer`, `## 🏛️ Council Results`, `## ✅ Compiled Move`, `## 🧭 Follow-Up Options`, and final `## 🧙 Footer`;
- no bold pseudo-headings as substitutes for sections;
- header/footer route truth agrees across waves, parents, children, and tools;
- required child/subsubagent obligations are visible even when not run;
- compiled move has target, immediate action, owner/lane, success check, stop/failure condition, artifact/output surface, and status;
- each visible follow-up option has a copy-pasteable prompt, payoff, use condition, and stop/block condition;
- verification counts are tied to exact commands.

If this checklist fails, rewrite the visible answer. Do not report the failed draft.

## Oversight Parent Set

For Max Assembly, run a small oversight set alongside the council parents or immediately after each council:

- `manager.rerouter`: liveness, deadline, retry, and resource pressure;
- `guard.receipt_audit`: route truth, completed counts, blocked/deferred lanes;
- `guard.receipt_divergence`: structural plurality before synthesis;
- `guard.compile_gate`: readiness of the compiled move or visible follow-up option;
- `guard.hygiene`: user-facing readability and cognitive-load budget.

Oversight parents have no vote. They can block, reroute, shrink, or require a sharper child task. They cannot replace council members or synthesize the answer.

Useful constrained Max Assembly is usually:

- 3-6 council parents per wave;
- 2-3 oversight parents per wave or one oversight pass after each wave;
- 2-4 child/subsubagent tasks per parent, split by source slice, claim, falsifier, fixture, or follow-up option.

Stress-test fanout may go wider, but useful runs should throttle down when added children produce shape-identical receipts.

For ordinary hardening work, prefer one controller plus three bounded lanes:

- an explore/map lane for current source truth;
- an execute/patch lane for one isolated target;
- a verify/audit lane for contracts, tests, and output shape.

Add an external scout only when it answers a specific uncertainty. Do not fan out for ceremony.

## Rerouter Rule

The rerouter watches liveness. It does not vote.

Default liveness thresholds:

- soft: 90 seconds without a useful receipt, file target, or clear progress;
- stall: 3 minutes without new evidence or narrower replacement;
- hard: 7 minutes per lane before close/reroute smaller.

The run is not worth more time when one obvious local edit and one verification command would prove the point, and extra lanes would only restate context instead of reducing risk or time.

Retry when:

- a required parent does not load its mini-MMM;
- a required parent returns generic synthesis instead of its member output shape;
- a child starts but does not return a usable receipt;
- a member drifts outside its task card;
- the compile gate fails but a smaller replacement is available.

Retry smaller, not broader.

## Retry States

Use these internal states:

- `planned`
- `launched`
- `active`
- `completed`
- `slow`
- `stalled`
- `timed_out`
- `rerouted`
- `superseded`
- `blocked`
- `deferred`
- `abandoned`
- `supplemental`

Only `completed` usable receipts count as ran.

## Retry Budget

For a normal full run:

- retry each required failed parent once with a smaller card;
- retry child fanout once per council with a smaller child task;
- after retry, mark blocked/deferred rather than hiding failure;
- if more than one required council remains under minimum, rerun the missing councils with smaller cards or report blocked.

## Member Reboot Rule

A member that became theater in one run is not automatically useless.

Before suppressing or retiring a member, classify the failure:

- bad task card;
- wrong source slice;
- prompt too broad;
- wrong model/runtime;
- role collapsed into another member;
- context not suited to that member;
- repeated cross-context uselessness.

Use `manager.member_rebooter` only when a reboot could change the decision, falsifier, evidence boundary, or compiled next move. It should produce one or two sharper initialization variants, not a large prompt bank.

Do not reboot for ceremony. If the rerouter says the member cannot change the answer, mark `cut_this_run` or `suppress_this_context` and continue.

## Automatic Rerun Rule

If the run header would say full but the receipts prove partial, do not output a fake full run.

First try one repair pass:

1. identify missing council/member/child;
2. rerun only the smallest missing part;
3. re-score;
4. if still below full threshold, report partial with blockers and a ready next prompt.
