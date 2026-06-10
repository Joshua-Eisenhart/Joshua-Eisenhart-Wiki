---
title: Octonion G2 Sedenion Carrier Geometry Audit 2026-06-08
created: 2026-06-08
type: project-audit
status: active-router
claim_ceiling: validated scratch carrier-geometry evidence only; no admitted M(C), no final manifold, no physics, no Standard Model, no bridge
framing: codex-ratchet
---

# Octonion / G2 / Sedenion Carrier-Geometry Audit 2026-06-08

## Purpose

Preserve the corrected threading after the owner flagged that the non-associative / `G2` / `Spin(7)` / `S^7` / Fano / sedenion material had been flattened into a one-line `L8 bracketing` note.

This page is an audit/router, not a proof page. It records what Hermes checked in the repo/wiki on 2026-06-08 PDT and what should change in the next sim queue.

## Bottom line

The octonion / `G2` / sedenion tower is not a late footnote. It is an early carrier-geometry frontier, behind the `M(C)` gate and canon algebra artifact, and it should be folded into Stage 4 same-carrier geometry work one bounded packet at a time.

Safe label:

```text
validated three-engine scratch carrier-geometry evidence
classification=scratch_diagnostic
all_pass=true on checked envelopes
promotion_allowed=false
formal_admission_allowed=false
```

Unsafe labels:

```text
admitted manifold
full M(C)
physics / Standard Model / GR bridge
final G2 answer
canonical by process
```

## Corrected dependency threading

The current build order should preserve this early carrier-geometry thread:

```text
M(C) gate
-> R/C/H/O/S division-algebra ladder
-> octonion carrier + associator
-> Cl(6) / >=7-imaginary-unit carrier constraint
-> G2 = Aut(O) and G2-variant family
-> Fano PG(2,2) incidence
-> Spin(7) / G2 / S^7 calibration
-> G2 -> SU(3) reduction as fenced readout pressure
-> sedenion / PG(3,2) zero-divisor graveyard control
```

This does not replace the foundation-first chain. It refines what lives early in the carrier-geometry region after the finite object/canon-artifact gate.

## Anti-collapse: G2 likely, variants open

`G2` is the leading candidate family, not the declared answer. Keep these variants separate until bounded controls exclude them:

- `G2 = Aut(O)` automorphism reading.
- `G2` as stabilizer of the associative 3-form `phi` / calibration reading.
- compact `G2` versus split `G2(2)` real-form branch.
- `G2` holonomy / 7-dimensional manifold variant.
- `G2 ⊃ SU(3)` color-like reduction pressure.
- `G2 ⊃ SU(2) x SU(2)` sub-reduction branch.
- `SU(3) -> G2 -> Spin(7)` projector / special-holonomy chain.
- `Spin(7) / G2 ~= S^7` coset / imaginary-unit shadow.

The sedenion side is not a carrier promotion. It is the early graveyard/control side: zero divisors, `PG(3,2)`, Desargues defects, and the boundary past normed division.

## Checked repo evidence

Hermes checked these result envelopes in `/Users/joshuaeisenhart/Codex-Ratchet`:

| Row | Result path | Checked status |
|---|---|---|
| `G2` automorphism xhigh | `system_v5/ops/formal_scouts/results/foundation_foundation_r3_g2_automorphism_xhigh_envelope_results.json` | `validate_three_engine_sim_result.py --require-pytorch` ok; `--strict-source-backed` ok |
| `G2` automorphism high | `system_v5/ops/formal_scouts/results/foundation_r3_g2_automorphism_high_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| octonion / `Cl(6)` link | `system_v5/ops/formal_scouts/results/foundation_r3_octonion_cl6_link_xhigh_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| nonassoc root-vs-carrier discriminator | `system_v5/ops/formal_scouts/results/foundation_foundation_r4_nonassoc_root_vs_carrier_discriminator_xhigh_envelope_xhigh_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| `G2 -> SU(3)` reduction | `system_v5/ops/formal_scouts/results/foundation_foundation_r5_g2_su3_reduction_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| Fano `PG(2,2)` incidence | `system_v5/ops/formal_scouts/results/foundation_foundation_r6_fano_pg22_incidence_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| `Spin(7)/G2` calibration forms | `system_v5/ops/formal_scouts/results/foundation_foundation_r6_spin7_g2_calibration_forms_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| sedenion `PG(3,2)` / Desargues | `system_v5/ops/formal_scouts/results/foundation_foundation_r6_sedenion_pg32_desargues_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| sedenion zero-divisor | `system_v5/ops/formal_scouts/results/foundation_foundation_r3_sedenion_zerodivisor_envelope_results.json` | `--require-pytorch` ok; `--strict-source-backed` ok |
| `J3(O)` Jordan | `system_v5/ops/formal_scouts/results/foundation_foundation_r3_j3o_jordan_envelope_results.json` | `--require-pytorch` ok; source-backed ok in batch check |
| alternativity | `system_v5/ops/formal_scouts/results/foundation_foundation_r3_alternativity_envelope_results.json` | `--require-pytorch` ok; source-backed ok in batch check |

The key discriminator remains:

```text
Non-associativity is installed by stronger carrier constraints such as Cl(0,6) / >=7 imaginary units / 3-qubit-Weyl pressure.
It is not forced by the bare root alone.
```

So the build queue should not promote non-associativity directly into R1/R2 unless a future bounded discriminator earns that. Current placement remains early carrier/bracketing geometry.

## Tool / runtime audit status

Observed checks on 2026-06-08 PDT:

- Runtime doctor: `scripts/codex_runtime_env_doctor.py` returned `ok=True`, `install_state=stable_observed`, canonical Python `/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3`, Julia `/opt/homebrew/bin/julia`, strict carrier project `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier`, and no active installers observed.
- Engine shakedown: `scripts/codex_engine_stack_shakedown.py` returned `ok:true`, result path `system_v5/ops/tooling/codex_runtime_capability_shakedown_results.json`; summary `31` pass, `0` fail, `0` warn, `1` skip (`julia_python_dlpack_bridge`).
- Three-engine source audit: `scripts/audit_three_engine_source_claims.py` wrote `/tmp/cr_three_engine_source_audit_current.json` and `/tmp/cr_three_engine_source_audit_current.md`; `42` envelopes audited, `38` source-backed all lanes, `4` source-backed but review-needed. The review-needed rows were `foundation_qit_operator_composition_mcp_envelope`, `foundation_r3_associator_low`, `foundation_r3_associator_medium_envelope`, and `foundation_r1_f01_finite_admissibility_unsat_v1`.
- Tool-library coverage: `scripts/sim_tool_library_coverage.py` succeeded when output was repo-local at `system_v5/evidence/hermes_audit/sim_tool_library_coverage_current.json` and `.md`. It fails for `/tmp` output because the script tries to render a repo-relative link to an out-of-repo JSON path.
- Formal-scout readiness: `scripts/formal_scout_readiness_index.py` wrote `system_v5/evidence/hermes_audit/formal_scout_readiness_index_current.json` and `.md`; it reported `208` results, `15` schema-ready formal-scout rows, `4` validator-failed rows, `189` non-formal-boundary rows, and `203` README-index-missing rows. Treat this as readiness/index hygiene, not result rejection.

Important runtime distinction:

- `codex_runtime_env_doctor.py` and `codex_engine_stack_shakedown.py` verify the strict carrier route.
- `sim_tool_library_coverage.py` also reports a global/default Julia inventory. Do not use that global inventory as strict carrier evidence.

## Skill / agent audit status

Hermes ran `scripts/codex_skill_agent_inventory.py` against:

```text
repo: /Users/joshuaeisenhart/Codex-Ratchet
codex primary: /Users/joshuaeisenhart/.codex
codex2: /Users/joshuaeisenhart/.codex-second
Hermes: /Users/joshuaeisenhart/.hermes
wiki: /Users/joshuaeisenhart/wiki
```

Observed and repaired:

- Inventory initially ran, but the narrow test suite failed because `system_v5/codex_skills/three-engine-sim/references/sim_agent_role_cards.md` had renamed the JAX/PyTorch role ids while `system_v5/tests/test_sim_agent_role_cards.py` still required the legacy ids.
- Hermes patched the repo role-card file with compatibility aliases:
  - `jax_rich_mirror_sim_builder` -> alias of `jax_batched_workhorse_sim_builder`;
  - `pytorch_support_sim_builder` -> alias of `pytorch_graph_network_sim_builder`.
- Hermes synced that same role-card file to both installed Codex homes:
  - `/Users/joshuaeisenhart/.codex/skills/three-engine-sim/references/sim_agent_role_cards.md`
  - `/Users/joshuaeisenhart/.codex-second/skills/three-engine-sim/references/sim_agent_role_cards.md`
- After sync, `repo_active_skill_parity` and `repo_secondary_skill_parity` had zero mismatches.
- Narrow tests passed: `pytest -q system_v5/tests/test_codex_skill_agent_inventory.py system_v5/tests/test_sim_agent_role_cards.py system_v5/tests/test_three_engine_sim_result_validator.py` -> `8 passed`.

This means the sim-engine skill/agent surface is runnable for the checked route. It does not prove that a future worker actually ran; worker receipt truth still requires runtime receipts.

## Current blockers / hardening gaps

1. Most of the checked carrier-geometry envelopes pass validator/source-backed gates but do not include the newer `canon_runtime` and `foreign_runtime_manifest` fields from `system_v5/docs/JULIA_CANON_RUNTIME_CONTRACT.md`. They remain valid scratch evidence, not full Canon-runtime receipts.
2. The readiness index shows many result/source indexing gaps. That is hygiene debt, not a reason to rebuild the checked G2/octonion/sedenion envelopes.
3. `sim_tool_library_coverage.py` has a path assumption: `/tmp` outputs crash during Markdown rendering. Use repo-local outputs until the script is patched.
4. `Basins.jl` remains absent; use `Attractors.jl` / JuliaDynamics routes for basin work unless a separate install/admission lane is opened.
5. Four source-audit review-needed envelopes should not be used as clean rich-tool fuel until reviewed: QIT operator composition MCP, low/medium associator, and R1 F01 finite-admissibility UNSAT.

## Queue correction

Do not rebuild the checked G2/octonion/sedenion envelopes by default. The next bounded packet should be one of:

1. **M(C) gap table hardening** — identify exactly which full `M(C)` fields are not yet present in the scratch v0 and which are delegated to separate envelopes.
2. **Same-carrier geometry micro-lego** — best candidates remain Hopf fiber/base loop law or Weyl-on-Hopf chirality, but the packet should explicitly thread the octonion/G2/sedenion tower as early carrier-geometry context, not late readout.
3. **Canon-runtime receipt hardening** — add `canon_runtime` / `foreign_runtime_manifest` to a selected consumer packet without widening the math claim.
4. **G2-variant split packet** — compare one concrete variant pair, such as `G2=Aut(O)` versus associative-3-form/calibration reading, with explicit controls and no promotion.

## One-line handoff

The corrected plan is: root discipline and `M(C)` gate remain first, but the octonion / `Cl(6)` / `G2` / Fano / `Spin(7)` / sedenion tower is an early carrier-geometry frontier, with `G2` likely but variant-family open, and with all checked evidence held at validator-clean `scratch_diagnostic` / no-promotion status.
