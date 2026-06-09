# Wizard Follow-up System v3.4

Follow-up is where lanes and compositions normally appear. It is not a worker log and not a raw route catalog. It is a short bank of useful next prompts produced from prior waves.

## Three waves

### Follow-up Make / Assembly

Input:

- voices;
- voice audit;
- LLM Council;
- checks/guards;
- general output;
- route registry;
- acceptance gates;
- blockers.

Process:

1. extract useful next actions;
2. map actions to lanes;
3. merge related actions into compositions;
4. mark blocked/deferred candidates;
5. build the full candidate bank.

### Follow-up Run / Scout

Run/scout every candidate that will be claimed as preworked. Use temporary files or disposable worker space when prework/full Wizard is active. If not run/scouted, do not call it preworked; mark the route blocked, deferred, or simulated and keep `Scout: not_scouted` separate from route truth.

### Follow-up Audit / Improve

Remove weak options, merge duplicates, improve wording, add payoff, add blocker/defer condition, suppress failed routes, order useful next prompts, and produce the final visible follow-up menu.

## Default visible Follow-up

The visible menu is a short audited useful subset. It is mostly lanes and compositions. It is not raw candidate bank, not a worker log, and not a voice-rerun menu.

The full visible-family bank is five lanes plus four compositions:

- L1 🎯 Direct
- L2 🔀 Alternative
- L3 🪞 Reframe
- L4 🃏 Wildcard
- L5 ⬅️ Back
- C1 🔗 All-A
- C2 🧬 All-B
- C3 🧹 All-C
- C4 🧙🏽‍♂️ Full Wizard

The example below is an audited subset, not a requirement to print exactly these four entries. Prefer concise lane/composition lines. Add route/scout truth inline only when it affects selection or when an option could be mistaken for preworked.

```text
🪄 Follow-up
L1. 🎯 Direct — "<next prompt that makes the clearest bounded move." `Scout: scouted`
L2. 🪞 Reframe — "<next prompt that changes the frame when the current frame is causing failure." `Scout: not_scouted`
C1. 🔗 All-A — "<next prompt that combines the bounded move, falsifier, check, and alternative." `Scout: scouted`
C4. 🧙🏽‍♂️ Full Wizard — "<next prompt for maximum integrated route with receipt truth." `Route: deferred; Scout: not_scouted`
```

In tuning/debugging or full-bank mode, the visible family bank may show all five lanes and all four compositions, but it should still use concise prompt lines rather than expanding into a worker log.

## Full candidate bank

The full candidate bank may include:

- voices;
- lanes;
- checks/guards;
- system routes;
- compositions.

Show the full bank only when the user asks, tuning/debugging is active, or full diagnostic mode is active.

## Suppression rules

Suppress follow-up options when they are duplicate, decorative, unsafe, too broad, not actionable, unscouted but worded as preworked, or weaker than a merged composition. Voice reruns appear only when requested, tuning/debugging, full-bank mode, or audit says a voice collapsed.


## v3.4 Runtime and elastic scout note

Follow-up candidates are not obligations. Build the full candidate bank, then scout only the candidates with plausible payoff under the current runtime. If a candidate was not actually scouted by a worker/tool/file/model surface, mark its route `blocked`, `deferred`, or `simulated` and its scout state `not_scouted`; do not call it preworked.

Use test-and-learn sizing: scout the smallest useful set, read receipts, then expand only when a candidate remains promising and untested. Hard counts are not doctrine.
