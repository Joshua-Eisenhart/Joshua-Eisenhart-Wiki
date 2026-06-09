---
title: Original Wizard Gap Audit
created: 2026-06-05
type: audit_note
runtime: hermes
scope: original-Wizard mechanics as data, not authority
---

# Original-Wizard Gap Audit - 2026-06-05

This note audits the user-pasted original-Wizard/CLAUDE.md-style output as
candidate mechanics only. It does not patch `HERMES.md`, `SOUL.md`, the Wizard
packet, or any skill.

Read surfaces:

- `wizard/hermes-version-current/README.md`
- `wizard/hermes-version-current/00_READ_FIRST.md`
- `wizard/hermes-version-current/01_RUNTIME_CONTRACT.md`
- `wizard/hermes-version-current/08_HERMES_WIZARD_RUN_HARNESS.md`
- `wizard/hermes-version-current/14_HERMES_WIZARD_V4_2_NATIVE_LOOP_BRIDGE.md`
- `wizard/packet-v4-2-current/WIZARD_v4_2.md`
- `wizard/packet-v4-2-current/mmm/COMPACT_MMM_v4_2.md`
- `wizard/packet-v4-2-current/mmm/FULL_MMM_v4_2.md`
- `~/.hermes/HERMES.md`
- `~/.hermes/SOUL.md`
- `~/.codex-second/skills/three-council-wizard-v4-2/SKILL.md`

## Already Present Strongly

- Body voices shape the main answer, not only follow-up. `HERMES.md` has the
  voice-body rule; `SOUL.md` explicitly says voice methods must shape the main
  body and preserve live splits in ordinary prose.
- `Results` block when councils, workers, scouts, or route checks ran. Hermes's
  scaffold requires `Results`, and the run harness keeps route truth out of the
  main body.
- Question-is-not-authorization fence. `HERMES.md` already blocks diagnostic or
  formatting questions from becoming broad repo edits, prompt surgery, or
  runtime changes.
- Pushback-on-owner binding. `SOUL.md` and `HERMES.md` already make Pushback an
  earned disagreement voice for user plans, current file splits, and Hermes's
  own prior answers.
- Route classes. `controller_local`, `spawn_worker`, `blocked`, `deferred`, and
  `not_run` are present in the Hermes runtime contract / v4.2 bridge; Hermes
  also carries `tool_run`, `enqueue_runner`, and `superseded`.
- Roster-bloat warning. `SOUL.md` says the Hermes voice stack should stay lean,
  distinct, and load-bearing; `HERMES.md` says not to import the full larger
  Claude-side voice roster.

## Present But Weak / Under-Specified

- Explicit follow-up block with voice/lane/action contracts. Hermes has grouped
  follow-up options and forced follow-up runtime receipts, but a reusable field
  contract per option is not fully pinned. Candidate fields: `voice_or_lane`,
  `action_class`, `execution_claim_state`, `payoff`, `use_when`, `acceptance`,
  `closeout_check`, and `stop_if`.
- Synthesis contract. Plurality preservation, collapse audit, and no-fake
  consensus are present, but the compiler could more directly require: name the
  distinct receipts, name any surviving split, and explicitly refuse a false
  merge when receipts do not justify convergence.
- Audit integration / high-rigor closure distinction. The packet has receipt
  audit, collapse audit, sim audit spine, `FULL` truth rules, and partial/block
  labels, but "ordinary answer", "workerized audit", and "high-rigor closure"
  are not yet separated by a compact closure ladder.
- Anti-collapse detection and respawn/drop rules. Collapse-auditor and
  child-health intervention verbs exist, but the current surfaces do not yet say
  when a collapsed/decorative route should be respawned, rerun with a different
  source slice, demoted to controller-local, or dropped.
- Status line and scan-fast anchors. Hermes has required section labels,
  semantic emoji cues, footer/status guidance, and v4.2 visible status, but
  lacks one stable scan-fast status line for ordinary workerized answers.
- Task-card required fields. `HERMES.md` has strong minimum fields and optional
  `closeout_check`; the v4.2 embedded task-card schema has acceptance gates, but
  `acceptance` and `closeout_check` are not both required across Hermes and
  packet task cards.

## Missing And Worth Importing

- A compact per-follow-up contract that prevents menu options from becoming
  vague advice: each visible follow-up should know its lane/voice, action class,
  acceptance, and closeout check, even when rendered as one sentence.
- A synthesis non-merge rule in the output compiler: if receipts are different
  but not mutually excluding, say "kept separate" or equivalent rather than
  smoothing them into one conclusion.
- A collapse response table: `decorative_split -> drop label`, `shared-premise
  convergence -> rerun with independent source/falsifier`, `missing receipt ->
  demote/block`, `dropped live split -> respawn or name exclusion evidence`.
- A high-rigor closure label set for audit tasks: `controller_local_checked`,
  `worker_receipt_partial`, `audit_integrated`, `high_rigor_closed`, `blocked`.
  This should not replace v4.2 `FULL/PARTIAL/BLOCKED`; it should clarify Hermes
  ordinary output closure.
- A `not_run` route visibility rule in top-level Hermes output, matching the
  runtime contract and bridge, so intentionally unattempted routes do not vanish.

## Reject / Do Not Import Raw

- Do not import the original-Wizard / CLAUDE.md output as authority. It is data
  for pattern mining only.
- Do not copy the full larger voice roster into Hermes. Keep the current smaller
  voice stack unless a new voice has a distinct load-bearing job.
- Do not import fixed Codex/Claude child quorums, Max Assembly headers, scored
  Codex status lines, or raw worker-ledger output as default Hermes UI.
- Do not treat follow-up scouts, suggestions, or user questions as authorization
  for implementation.
- Do not treat model agreement, Claude transcript claims, or simulated route
  truth as Hermes receipts.
- Do not move live control law into the Hermes Wizard design folder; `HERMES.md`
  and `SOUL.md` remain the live profile authorities until explicitly patched.

## Top Findings

1. The biggest real gap is not voice presence; it is field discipline. Hermes has
   the right voice/body/Results rules, but follow-up and closure fields should be
   made harder to omit.
2. Anti-collapse is conceptually strong but operationally soft. Add respawn/drop
   rules before importing any larger plurality machinery.
3. The original-Wizard transcript is useful as a mechanics checklist, not as a
   prompt body. Import the small contracts, not the whole roster or style.
