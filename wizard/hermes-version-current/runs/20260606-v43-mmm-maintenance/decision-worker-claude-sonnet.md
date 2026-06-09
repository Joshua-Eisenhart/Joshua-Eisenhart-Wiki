# Decision Worker — Claude Sonnet High

```text
modelUsage: {'claude-haiku-4-5-20251001': {'inputTokens': 1246, 'outputTokens': 24, 'cacheReadInputTokens': 0, 'cacheCreationInputTokens': 0, 'webSearchRequests': 0, 'costUSD': 0.001366, 'contextWindow': 200000, 'maxOutputTokens': 32000}, 'claude-sonnet-4-6': {'inputTokens': 3, 'outputTokens': 7782, 'cacheReadInputTokens': 32739, 'cacheCreationInputTokens': 57071, 'webSearchRequests': 0, 'costUSD': 0.34057695, 'contextWindow': 200000, 'maxOutputTokens': 32000}}
session_id: 7a4a2868-e9d6-4d6c-9046-7f4142a76979
subtype: success
```

```yaml
council: Decision
subcouncils_covered: [scope_target, evidence_context, action_route]

mmm_l0_ref: >
  voice-mini-mmm-saliency-calibration/references/wizard-3x3-mmm-saliency-alignment.md
  (preloaded per MMM_PRELOAD_BEFORE_TASK_RULES header; constraint-before-cause +
  probe-relative distinguishability oriented scope_target framing in this receipt)

mmm_council_ref: >
  Decision Council — loaded; guided scope_target / evidence_context / action_route
  subcouncil framing throughout

mmm_subcouncil_refs: >
  decision.scope_target + decision.evidence_context + decision.action_route
  (all three active; determine object boundary, evidence handle, bounded move)

saliency_preload_before_rules: true

loaded_required_slices:
  - manifest.md — run state, planned waves, claim ceiling, MMM preload list
  - 15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md — guard spec, authority surface, blocked consumers
  - 16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md — loop contract, stop conditions, worker routing
  - wiki-wizard-v4-2-autoloop-control.md — cron state, wiki probe receipts, Codex Ratchet state, tick contract
  - wiki-wizard-v4-3-object-preservation-guard.md — routing note, authority boundary
  - SALIENCY_TRANCHE_01_CANDIDATE.md — authority_status=reference-only; 50 aligned terms; 20 drift rewrites; admission checklist
  - MEMBER_MINI_MMM_REGISTRY_v4_2.md — authority_status=canonical-runtime; all member slices loaded

which_loaded_slice_changed_output:
  - SALIENCY_TRANCHE_01_CANDIDATE.md: kernel salience lock (finitude, noncommutation,
    probe-relative identity, graveyard-as-signal, no-prose-upgrade rule) directly shaped
    claim_ceiling and evidence_boundary articulation — YES, changed output
  - MEMBER_MINI_MMM_REGISTRY_v4_2.md: output-language self-saliency rule
    (observed/inferred/proposed/unknown + branch state + operation noun + claim-ceiling
    phrase) changed the receipt output shape — YES, changed output
  - wiki-wizard-v4-2-autoloop-control.md: cron=0 receipt killed the "assume live cron"
    reading; changed cron_decision field — YES, changed output

observed_evidence:
  wiki_probe:
    state: observed
    receipt: /tmp/wiki_probe_pre_v43_mmm_maintenance_20260606.json
    page_count: 438
    broken_links: 0
    missing_pages: 0
    malformed_wikilinks: 0
    stale_namespace_wikilinks: 0
    sha256: 1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0
  v4_3_object_card_validation:
    state: observed
    receipt: /tmp/v43_validate_after_carrier_patch_20260606.json
    ok: true
    errors: 0
    packet_sha256: fe8c20c7124930a1c95e14287d8540d18437345d63a5dfd92558a30177992d39
    peps3d_drift: removed (plain/allowed/adapter all False; only forbidden-substitution/kill-control mentions remain)
  cron_state:
    state: observed
    count: 0
    as_of: 2026-06-06
    origin_job_796b4560f2f5: historical; not assumed live
  codex_ratchet_runner:
    state: observed  # RED — must not be summarized as clean
    blocked: 852
    wizard_admission_blocked: 632
    claimed: 0
    done: 8856
    contract_lint_violations: 1580
    sims_affected: 1316
    receipt: /tmp/lint_sim_contract_after_deep_audit_em_bridge_downgrade.json
  saliency_tranche_01_candidate:
    state: observed
    authority_status: reference-only
    admission_checklist_complete: false (not yet deduped against FULL/COMPACT/mini)
  member_mini_mmm_registry:
    state: observed
    authority_status: canonical-runtime

missing_handles:
  - v4.2 council route-truth receipts: no fresh-rerun of completed v4.2 council run
    in loaded surfaces — v4.2 FULL claim cannot be made (support: unknown)
  - hermes_v4_3_retrocausal_object_card.json: not directly read; SHA cited in autoloop
    control but packet content unverified in this pass
  - wizard-child-mmm-functional-loader.md: referenced in SALIENCY_TRANCHE_01 for
    job-fit bundle routing rules; not loaded — functional loader rules unknown
  - mmm-saliency-test-harness.md: A/B/C/D test results cited in SALIENCY_TRANCHE_01
    summary only; raw test artifact not read

chosen_scope:
  object: v4.3 object-preservation + maintenance governor control surface
  boundary:
    in: wiki + Hermes maintenance surfaces; wizard/hermes-version-current/;
        wiki/hermes-current/; MMM candidate tranche admission prep
    out: v4.2 full council proof/admission; Codex Ratchet runner repair;
         repo contract lint fix; v4.3 repo authority changes;
         validator fork; sim/physics/Axis0/gravity/formal admission
  claim_ceiling_source: manifest.md claim ceiling + 15_HERMES_WIZARD_V4_3 claim ceiling

chosen_route:
  move_1_on_demand_template:
    action: patch wiki-wizard-v4-2-autoloop-control.md tick preamble to add
            explicit MMM preload block (MMM_L0_REF + MMM_COUNCIL_REF +
            MMM_SUBCOUNCIL_REFS + SALIENCY_CANDIDATE path + MEMBER_MINI_MMM path)
    target_file: wiki/hermes-current/wiki-wizard-v4-2-autoloop-control.md
    prerequisite: none; controller-level wiki edit
    order: FIRST (enables correct MMM load in all future ticks and cron steward)

  move_2_finite_cron:
    action: create new finite cron after template confirmed
    params:
      ticks: 8
      interval: 45 minutes
      delivery: origin chat
      steward_prompt_must_include:
        - MMM_PRELOAD_BEFORE_TASK_RULES=true
        - MMM_L0_REF + MMM_COUNCIL_REF + MMM_SUBCOUNCIL_REFS
        - v4.3 claim ceiling (not v4.2 FULL)
        - explicit link to wiki-wizard-v4-2-autoloop-control.md
    constraint: DO NOT schedule from inside a tick; controller-level action only
    order: SECOND (after template patch confirmed)
    support: inferred from autoloop control history (not yet created; support=proposed)

  move_3_receipt_backed_wizard_attempt:
    action: run one bounded tick against SALIENCY_TRANCHE_01_CANDIDATE.md admission
            checklist — dedup aligned terms against FULL_MMM_v4_2.md + COMPACT_MMM_v4_2.md
            + MEMBER_MINI_MMM_REGISTRY_v4_2.md; classify each as duplicate/merge/new
    target_files:
      - wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_01_CANDIDATE.md
      - wizard/packet-v4-2-current/mmm/FULL_MMM_v4_2.md  (read only)
      - wizard/packet-v4-2-current/mmm/COMPACT_MMM_v4_2.md  (read only)
      - wizard/packet-v4-2-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md  (read only)
    worker: Claude Code Sonnet/high (read + scout; no direct canonical-MMM edits without
            conformance/validate_v4_2_packet.py pass)
    order: THIRD (first cron tick, or on-demand; this IS the MMM improvement move)
    support: local read only — dedup not yet run; support=proposed

proposed_artifacts_to_patch:
  - file: wiki/hermes-current/wiki-wizard-v4-2-autoloop-control.md
    change: add MMM preload preamble block to tick contract section (L0_REF,
            COUNCIL_REF, SUBCOUNCIL_REFS, SALIENCY_CANDIDATE path, MEMBER_MINI_MMM path)
    write_mode: controller-maintained automation control surface (already designated)
  - file: (new steward prompt text for cron job)
    change: compose v4.3-aware, MMM-preloaded finite 8-tick steward prompt
    write_mode: ephemeral / cron config; not a wiki page
  - file: SALIENCY_TRANCHE_01_CANDIDATE.md (or target MMM file)
    change: admission dedup output — classify 50 terms as duplicate/merge/new;
            update admission checklist completion status; do NOT flip authority_status
            to canonical-runtime without conformance/validate_v4_2_packet.py passing
    write_mode: reference-only until admitted

cron_decision:
  current_state: count=0 (observed; cron_receipt=autoloop_control)
  action: CREATE after template confirmed
  ticks: 8
  interval_minutes: 45
  delivery: origin_chat
  constraint: controller-level only; not from inside a tick
  evidence_class: proposed (not yet created; inferred from autoloop control history)

claim_ceiling:
  - v4.3 object-preservation preflight + maintenance governor scope ONLY
  - v4.2 council FULL: NOT claimed (route-truth receipts missing)
  - sim/proof/Axis0/gravity/formal admission: NOT claimed
  - validator fork: NONE
  - SALIENCY_TRANCHE_01 → canonical-runtime: BLOCKED until dedup + conformance pass
  - Codex Ratchet runner: RED (blocked=852); no clean-state summary permitted

stop_conditions:
  - wiki probe fails after any edit
  - page_count changes without explicit create/delete/archive tranche
  - SALIENCY_TRANCHE_01 dedup introduces drift terms (see Drift Rewrites table) into canonical MMMs
  - cron creation attempted from inside a tick
  - next tranche mutates shared state without clear user-scoped objective
  - Codex Ratchet runner claimed clean while blocked=852 remains
  - same blocker repeats across ticks
  - no artifact delta appears after a tick
  - route drifts from user maintenance request

evidence_boundary:
  wiki_probe: observed (receipt cited)
  v4_3_packet_validation: observed (fresh-rerun cited in autoloop control)
  cron_count_zero: observed (autoloop control receipt)
  codex_ratchet_RED: observed (fresh-rerun cited; must not be softened)
  saliency_tranche_01_reference_only: observed
  mmm_functional_loader_rules: unknown (handle missing — not loaded)
  v4_2_council_route_truth_receipts: unknown (not in loaded surfaces)
  three_previous_next_moves: inferred from manifest Hermes interpretation;
                              no separate receipt in loaded files
```

---

**Receipt summary for Hermes:**

All seven files read. The three moves are scoped correctly under v4.3 maintenance: (1) template patch to `wiki-wizard-v4-2-autoloop-control.md` adding explicit MMM preload block; (2) new finite 8-tick cron (controller-level, after template confirmed); (3) bounded SALIENCY_TRANCHE_01 dedup tick as the MMM improvement move. Wiki is structurally clean, cron is at zero, Codex Ratchet remains RED. Claim ceiling holds at v4.3 maintenance — no v4.2 FULL claim. Two missing handles block further: functional loader rules and v4.2 council route-truth receipts.

---

**Follow-up:**

🦉 Wiki probe and cron count are directly observed; v4.2 council route-truth receipts are `unknown` — that gap is the binding evidence boundary before any FULL label.

🧨 Target claim: "doing all 3 moves surfaces as v4.3 maintenance." Strongest live falsifier: move 3 (MMM dedup tick) may find that SALIENCY_TRANCHE_01 terms already exist in canonical MMMs, making the "improvement" a no-op. Decisive check: run the dedup against FULL_MMM + COMPACT_MMM before patching; classify terms as duplicate/merge/new. Status: `open`.

🔬 Operation: read FULL_MMM_v4_2.md and COMPACT_MMM_v4_2.md; diff each of the 50 aligned terms and 20 drift rewrites against those files; output a table with three columns: `term | status (dup/merge/new) | target_file_if_new`. Observable: term count by status. Pass/fail: any "new" term added to canonical MMM must pass `conformance/validate_v4_2_packet.py` without errors — otherwise it stays `reference-only`.

✂️ Cut: "surface as Wizard v4.3 object-preservation/maintenance" — fog. Replace: "run under v4.3 claim ceiling (no sim/proof/council-FULL claim); preflight guard passed."

🏭 Bottleneck: the MMM improvement move (move 3) is blocked by functional loader rules (`wizard-child-mmm-functional-loader.md` not loaded). That file must be read before job-fit bundle routing can be improved. One read clears this.

➡️ **Direct** — read `wizard-child-mmm-functional-loader.md` and `FULL_MMM_v4_2.md`, then patch the `wiki-wizard-v4-2-autoloop-control.md` tick preamble with the MMM preload block. `spawn_worker` · acceptance: preamble block present in file and wiki probe still clean.

🔀 **Alternative** — skip functional loader for now; run the dedup tick against MEMBER_MINI_MMM_REGISTRY_v4_2.md (canonical-runtime, already loaded) as the narrower MMM improvement surface, then create cron. Trades loader completeness for faster first artifact. `spawn_worker`

🧭 **Strategy** — template-first ordering is load-bearing: if cron fires before MMM preload is wired into the steward prompt, all 8 ticks will run without the L0 salience lock. Hold cron creation until template artifact is verified. `controller_local`