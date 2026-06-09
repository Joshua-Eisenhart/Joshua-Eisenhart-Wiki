# Wizard Follow-up Format v2.8

## Core

Follow-up is not a second body answer.
Follow-up is a bank of next-input prompts that the Wizard has made, lightly scouted, and audited.

Follow-up options are not proof that the route already ran for the current answer.
If the current answer claims a follow-up route already ran, it needs receipt truth before the Follow-up heading.

Compositions belong in Follow-up, not in the main answer body.
The main answer may mention what the controller synthesized, but it must not print a composition catalog such as C19-C25 before Follow-up.

## Follow-up Prework

The Follow-up bank has three internal waves:

1. Make: draft candidate next-input prompts from the voices, lanes, LLM Council, and Audit.
2. Run/Scout: lightly test which next-input prompts are useful and bounded.
3. Audit/Improve: remove weak, tangent, duplicate, sycophantic, or unsafe options.

If these waves did not run, the menu must say the options are future-choice only.

## Lean Chat Shape

```text
🪄 Follow-up
Lane follow-ups
L1. 🎯 Direct next input
   🪄 Follow-up: Make the smallest reversible repair for the current artifact, then show the validator result.
   Pre-run status/score: scouted, not executed as current work; 94/100.
   Audit: passes only if the next action has one artifact and one proof gate.

L2. 🪞 Reframe next input
   🪄 Follow-up: Restate the real unit of work, then rerun the answer through Hume, Systems, Factory, Strategy, Council, and Audit.
   Pre-run status/score: scouted, not executed as current work; 88/100.
   Audit: passes only if the new frame changes the next action.

Composition follow-ups
C5. 🧼 Hygiene composition
   🪄 Follow-up: Use Orwell, Factory, Hygiene, Council, and Audit to rewrite the output as normal chat while preserving evidence.
   Pre-run status/score: scouted, not executed as current work; 92/100.
   Audit: passes only if the answer is richer and shorter where it should be.
```

Every follow-up option needs exactly these fields:

- 🪄 Follow-up
- Pre-run status/score
- Audit

Do not use body-style fields such as Members, Integrated result, Tension handled, or Next gate in the default chat menu.

## Lane Follow-ups

Lane follow-ups are narrow next-input prompts.
They integrate the relevant voices, LLM Council, and Audit without printing each voice again.

Default lane families:

- Direct: smallest bounded action.
- Reframe: changed unit of work.
- Alternative: different route with real cost/failure mode.
- Wildcard: bounded adversarial or off-axis probe.
- Back: return to packet/runtime/source boundary.

Factory, Strategy, and Systems are voices, not lane files.
They can still shape lane follow-ups when the next input needs broader workstream, campaign, or feedback-loop context.

## Composition Follow-ups

Composition follow-ups are integrated next-input prompts.
They combine voices, lanes, LLM Council, and Audit into a single future action.

Default composition families:

- Hygiene composition: Orwell + Factory + Hygiene + Council + Audit.
- Security composition: Pushback + Popper + Feynman + Security + Council + Audit.
- Overall-context composition: Systems + Factory + Strategy + Hume + Reframe + Council + Audit.
- Behavior-proof composition: no-MMM vs main-MMM vs mini-MMM comparison with leakage audit.
- Full Wizard pass: full route-family run with quality score and final receipt audit.

## Rejection Signs

Reject the Follow-up if:

- it repeats the voice body as a voice rerun menu;
- it prints a giant route catalog;
- it has labels without real next-input prompts;
- it lacks Pre-run or Audit fields;
- it claims future options already executed without receipts;
- it makes Hygiene or Security loose tangent options instead of guarded compositions;
- it hides the current answer's open risks.
