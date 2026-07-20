# Ratchet v0.2 upgrade report

Date: 2026-07-10  
Output: `123_claude_science_ratchet_v0_2.zip`  
Scientific claim ceiling: process hardening / scratch diagnostic; no model rung promoted

## Source and preservation

- Source archive: `122.zip`
- Source SHA-256: `f23d4309d53c7362dd45c76af1caca8ae77f16e6cef716cb5ed2c84f9331a320`
- Source entries: 501; `unzip -t` passed.
- The repeated attachment set was byte-identical.
- The source archive was not overwritten. Binary figures, PDFs, spreadsheets, owner sources, and reference corpora are
  preserved. Their inclusion remains provenance/hypothesis input, not admission.
- Simulation runs generated temporary result updates in this environment; all pre-existing science-result JSON and engine
  target files were restored byte-for-byte from `122.zip`. Only the new environment-level `run_all_report.json` is added.

## Central correction

The prior Claude Science state had absorbed part of the owner's correction but still encoded four incompatible process
assumptions:

1. it represented the root as an equivalence relation `~_P` over a pre-given finite support `X`;
2. it stored geometry and entropy as independent Ratchet state fields;
3. it called one object “the weakest” without a finite search-relative frontier certificate;
4. it moved from F01 toward a bottomed-out CA grain too quickly.

v0.2 replaces these with:

- constrained distinguishability before objects, equivalence, support, quotient, carrier, entropy, geometry, or CA;
- one later organized distinction surface with entropy/geometry/operator co-views;
- an anytime provisional MSS frontier of all minimal tested survivors;
- witnessed weakening maps, finite local weakening coverage, open attacks, and automatic reopening;
- append-only evidence history with defeasible model frontiers;
- rung dependency DAGs rather than a required linear ladder;
- finite realized refinement with indefinitely extendible finite resolution, not a completed infinity or asserted global
  smallest grain;
- a CA/ring-checkerboard candidate bakeoff against weaker transition, rewrite, and evolving-graph families.

## Executable additions

- `RATCHET_SPEC.md`: complete v0.2 process specification.
- `ratchet/ratchet_kernel.py`: validates receipts, computes the tested minimal-survivor frontier, and validates linked
  receipt DAGs.
- `ratchet/schemas/ratchet_run.schema.json`: interchange schema.
- `ratchet/weakening_grammar.json`: explicitly installed and globally incomplete weakening grammar.
- `ratchet/examples/process_fixture.json`: synthetic, non-scientific fixture.
- `ratchet/bundle_ratchet_lint.py`: fail-closed guard over 20 claim-bearing front doors.
- `ratchet/CURRENT_FRONTIER.md`: explicitly says no bundle-wide scientific frontier has yet been admitted under v0.2.
- `ratchet/CA_MSS_RESEARCH_PROGRAM.md`: bounded CA/ring-checkerboard research packet.

The kernel self-test accepts the valid fixture and rejects eleven mutations: object smuggling, a global-minimum claim,
wrong frontier, independent entropy state, missing controls, cyclic weakness, missing lineage, open registered lowering,
unaudited admission, missing predecessor, and cyclic receipt dependencies.

## GitHub grounding

The read-only audit used `Joshua-Eisenhart/Codex-Ratchet` at
`87446663072c9c102609fe5f9abe9dee09056e31`. Important anchors:

- the MSS draft already has plural `Min(Surv(C))`, installed weakness order, and supplied dynamics;
- the constraint-process document already says finite exploration cannot cover the whole surface;
- the v7 distinguishability quotient is a real finite density/Pauli fixture but therefore belongs after the root;
- the ring-checkerboard/QCA audit chain supplies concrete negative species: label leakage, definitionally forced periods,
  calibration relabeling, single-token/full-field conflation, frozen support, open-chain/ring boundary confusion, and
  finite-ring index ceilings.

The GitHub estate informed candidates, controls, and ceilings. It was not treated as canon.

## Legacy-state migration

Scope-correction banners and anti-drift language were propagated through the start file, agent contract, orientation,
model ledger, state summary, unified-lens map, historical foundation audits, formal-spec/pure-math front doors, laptop
runner, generated guide, inventory, and manifest. Existing numerical results remain fixture-local evidence. The previous
global wording “complex qubit forced by F01/N01” is withdrawn; the current qubit route is an installed/minimal-within-
tested-grammar result awaiting the real v0.2 carrier bakeoff.

## Validation

### Untouched source baseline in this workspace

`python3 run_all.py` returned **106 pass / 6 fail / 33 skip**. This contradicts the source front page's historical
145-green stamp only because this workspace lacks required/optional packages and two jobs exceeded stale time budgets:

- missing `sympy`: one failure;
- missing `pysindy`: two failures;
- missing `z3`: one failure;
- pre-existing 60-second and 40-second timeouts: two failures;
- missing optional JAX/Torch/solver/QIT lanes: 33 explicit skips.

Both timeout jobs passed unchanged when run to completion. Their harness budgets were raised to 180 and 120 seconds.
`requirements.txt` and `LAPTOP_RUN.sh` now declare/install `sympy`, `pysindy`, `z3-solver`, and `cvc5`, which registered
jobs already required. No expected scientific value or gate was relaxed.

### Post-upgrade validation

`python3 run_all.py` returned **109 pass / 4 fail / 33 skip**. Relative to the untouched-source baseline, both timeout
failures became unchanged passes and the new Ratchet process-integrity lane passed. The four remaining failures are
exactly the undeclared-environment cases corrected in `requirements.txt`: one missing `sympy`, two missing `pysindy`,
and one missing `z3`. The 33 skips are optional-tool lanes in this workspace. Thus the process upgrade introduced no
observed simulation regression, but this environment cannot honestly certify a fully green numerical suite until the
required packages are installed. `run_all_report.json` preserves the exact per-job result.

Independent targeted checks passed:

- Ratchet receipt + ledger self-test;
- synthetic receipt validation;
- 20-front-door anti-drift lint;
- Python syntax for generator, harness, kernel, and lint;
- JSON syntax for manifest, receipt schema, weakening grammar, and fixture;
- `bash -n LAPTOP_RUN.sh`;
- both corrected-time-budget jobs, without code or expected-value changes.

## Honest remaining work

- Install `requirements.txt` plus optional full-mode dependencies and obtain a completely green fresh laptop run.
- Build actual v0.2 scientific receipt packets; the supplied tower is not retroactively admitted.
- Migrate old rung claims into a dependency DAG, preserving every death/demotion.
- Run the root/object/carrier/order/surface packets before granting CA or ring-checkerboard privilege.
- Add future weakening operators and rival mathematical families whenever discovered; every affected rung must reopen.
