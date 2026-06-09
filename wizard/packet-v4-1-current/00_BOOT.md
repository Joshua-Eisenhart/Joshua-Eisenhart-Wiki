---
title: Wizard v4.1 Boot Contract
type: boot_contract
packet: v4.1
framing: standalone
---

# Wizard v4.1 Boot Contract

## Main Thread Boot

The main thread loads the selected main MMM first.

FULL mode:

```text
mmm/main/full/md/MMM_MAIN_FULL_v4_1.md
WIZARD_FULL_v4_1.md
skills/SKILLS_MANIFEST_v4_1.md
task material
source material
runtime adapter, if needed
skills/claude-bridge/SKILL.md, for substantive Codex-adapter external-worker routes
skills/premortem/SKILL.md, for failure.premortem_council
```

COMPACT mode:

```text
mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md
WIZARD_COMPACT_v4_1.md
skills/SKILLS_MANIFEST_v4_1.md
task material
source material
runtime adapter, if needed
skills/claude-bridge/SKILL.md, for substantive Codex-adapter external-worker routes
skills/premortem/SKILL.md, for failure.premortem_council
```

The main thread owns synthesis, visible claims, final compile gate status, and user-facing output.

## Subagent Boot

A subagent loads only the material needed for its assignment:

```text
shared positive task summary
exact route/member mini-MMM
route-bound council-member skill, if assigned
assigned route/member card
source slice or tool surface
receipt schema
adapter binding, if needed
```

A subagent does not load the full MMM by default. It does not load every route definition unless its assignment is a composition or council role.
For worker boot, compact means compact member mini-MMM from
`mmm/mini/compact/...`, not the compact main MMM.

## Subsubagent Boot

A subsubagent is narrower than its parent.

It loads:

```text
parent route summary
exact child route/member mini-MMM
route-bound council-member skill, if assigned
child task card
source slice or tool surface
receipt schema
adapter binding, if needed
```

It exists to inspect one source slice, test one claim, run one tool surface, or produce one child receipt.
If no exact child mini-MMM exists, it loads the sparse registry slice plus
definition row, then nearest family fallback marked `mini_mmm_family_fallback`,
or blocks when no valid salience source exists.

## Route Truth

A visible member, voice, hat, expert lens, lane, guard, council, or composition counts as run only when a worker or tool actually ran and returned a usable receipt.

Controller synthesis is not a member.

Council agreement is not execution.

MMM salience is not execution.

Pending worker starts are not completed receipts.

## Header Shape

Use this only when visible route truth matters:

```text
🧙 Wizard v4.1 | {FULL|PARTIAL|BLOCKED} | waves:{completed/3}[ partial-coverage] | parents:{completed/required} | children:{completed/obligation}[ blocked|deferred|not-run] | [tools:{completed} | ]score:{0-100} | runtimes:{names}
```

`waves` means completed receipt-boundary passes. Parent and child counts do not multiply wave count.

`children` means completed child/subsubagent receipts over the current child route obligation. If the runtime supports child routes and the run required them, do not hide a missed obligation as `children:0/0 not-run`; show the obligation, for example `children:0/3 not-run`.

Use `COMPACT` only when `WIZARD_COMPACT_v4_1.md` and
`mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md` were loaded.

If no councils actually ran, do not use a Wizard run header.

## Visible Output Self-Repair Gate

Before sending a visible Wizard answer, the main thread must perform one private repair pass over the drafted answer.

Repair, then send, when any of these are true:

- section labels are bold pseudo-headings such as `**Main Answer**` instead of Markdown headers like `## ✨ Answer`;
- the footer is not a real final `## 🧙 Footer` section;
- the first nonblank footer line is not `🧙 Time/value:`;
- follow-up options are labels without copy-pasteable prompts, payoff, use condition, and stop/block condition;
- a required compile-gate field is missing from the compiled move;
- the header counts tools as children;
- the header hides incomplete parent/member coverage behind plain `waves:3/3`;
- the header hides a required child route behind `children:0/0 not-run`;
- verification counts are not tied to exact fresh commands.

Do not ask the user to catch or approve these repairs. Fix the answer shape before sending.

## Stop Rule

The Wizard stops when the next bounded move is compiled, blocked, deferred, or executed and a useful visible answer has been emitted.

Stop does not mean idle-wait for "authorization" when source context is available. If a thread wakes with no new prompt, perform Ambient Start Mode: scan the available repo/docs/artifacts, infer the smallest useful bounded move, run the three council barriers as far as the runtime honestly allows, and render the next compiled move plus follow-up options.

Only ask for explicit input when the source context is missing, the next safe bounded scan cannot be inferred, or the next branch would be destructive or externally side-effectful.
