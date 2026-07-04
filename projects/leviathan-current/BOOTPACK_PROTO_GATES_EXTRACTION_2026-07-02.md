# Bootpack Proto-Gates Extraction - 2026-07-02

Requested target:
`/Users/joshuaeisenhart/wiki/projects/leviathan-current/BOOTPACK_PROTO_GATES_EXTRACTION_2026-07-02.md`

Write status: the wiki target was not writable from this workspace. This fallback artifact was written at:
`/Users/joshuaeisenhart/Desktop/Codex Ratchet/BOOTPACK_EXTRACTION_FALLBACK.md`

## Source Set

Legacy bootpacks mined:

- `system_v5/READ ONLY Reference Docs/Older Legacy/BOOTPACKS/BOOTPACK_THREAD_B_v3.9.13.md`
- `system_v5/READ ONLY Reference Docs/Older Legacy/BOOTPACKS/BOOTPACK_THREAD_S_v1.64.md`
- `system_v5/READ ONLY Reference Docs/Older Legacy/BOOTPACKS/MEGABOOT_RATCHET_SUITE_v7.4.2-PROJECTS copy.md`
- `system_v5/READ ONLY Reference Docs/Older Legacy/BOOTPACKS/MEGABOOT_RATCHET_SUITE_v7.4.7-PROJECTS_PATCHED_CONSTRAINT_MANIFOLD copy.md`

Current doctrine compared:

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md`
- `system_v5/docs/LLM_CONTROLLER_CONTRACT.md`
- `system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md`
- `system_v5/docs/LEGO_SIM_CONTRACT.md`

Scope note: duplicated embedded Thread B/S/SIM/M material inside the megaboots is counted once as a rule unless the later bootpack changes the rule.

## 1. Rule-By-Rule Table

| # | Legacy gate / rule | OG formulation / sharp quote | Current-stack equivalent | Verdict | Mining note |
|---:|---|---|---|---|---|
| 1 | Report metadata | Report blocks require timestamp, boot id, and current megaboot/ruleset hashes. | LLM Controller evidence table; current docs require cited result paths and fresh verification, but not uniform report headers. | MISSING-FROM-CURRENT | Revive as receipt header schema for gates and worker reports. |
| 2 | Default flags | `NO_INFERENCE TRUE`; `NO_REPAIR TRUE`; `NO_SMOOTHING TRUE`; `NO_NICKNAMES TRUE`; `COMMIT_POLICY COMMIT_ON_PASS_ONLY`. | LLM Controller "Narrative Substitution" ban; AGENTS says current request and evidence beat summaries. | OG-BETTER-STATED | Strong, compact operating posture. Promote wording as a controller default. |
| 3 | Kernel stability | "Additions are only justified by an actual exploit, a failing regression test, or a formally defined new attack surface." | Gate Doctrine ratchet property: every failure mode becomes a permanent gate. | OG-BETTER-STATED | Better than current prose because it restricts gate growth to exploit/test/attack-surface evidence. |
| 4 | Rule id vocabulary | Rule IDs are append-only; deprecated IDs remain reserved. | Current docs have gates but no append-only rule-id registry. | MISSING-FROM-CURRENT | Gold. Prevents audit ambiguity across versions. |
| 5 | Message shape | User message must be exactly one of COMMAND_MESSAGE, ARTIFACT_MESSAGE with one container, or SIM_EVIDENCE_PACK. | Gate Doctrine shape/existence gate; LEGO_SIM required schema. | EQUIVALENT | Current schemas are more domain-specific; OG is better as a generic ingress gate. |
| 6 | Artifact comments | No `#` or `//` comments inside artifacts. | Current contracts ban narrative substitution and placeholder evidence, but not artifact comment syntax. | MISSING-FROM-CURRENT | Useful when artifact language must be machine-roundtrippable. |
| 7 | Snapshot admission | Snapshot admitted only if SURVIVOR_LEDGER has at least one real item header. | Current freshness/provenance gates; LLM Controller bans state claims without current file/result. | EQUIVALENT | Current is broader; OG is sharper for replay snapshots. |
| 8 | Canon state surfaces | Survivor ledger, park set, reject log, kill log, term registry, evidence pending, active hashes, counters. | Current wave/gate/ledger machinery exists but is more distributed. | OG-BETTER-STATED | Legacy names the minimum replayable state vector. Promote as "receipt state minimum". |
| 9 | Closed rejection tags | `TAG_FENCE`: only listed tags are allowed; any other tag is a schema failure. | Current docs have statuses and classifications, but no closed rejection-tag vocabulary. | MISSING-FROM-CURRENT | Gold. Current queue reasons drift without this. |
| 10 | Context drift | "No other context is permitted." Thread B scope is bootpack, survivor ledger, and admitted snapshot only. | Mandatory read gate plus "worker reports are not substitutes"; current uses broader repo context. | OG-BETTER-STATED | Promote for replay/import/admission lanes where ambient memory is dangerous. |
| 11 | ID namespace | F/W/K/M for axioms, P only for probes, S/R for specs. | LEGO roles and classifications; no universal namespace fence. | MISSING-FROM-CURRENT | Revive only if current artifacts need cross-run type IDs. |
| 12 | Structural name hygiene | AXIOM IDs must be structural-neutral; count/construction/domain/metaphor terms barred unless ratcheted. | ENFORCEMENT label-only ban; Gate Doctrine claim-language gate. | OG-BETTER-STATED | Better operationally: forbids semantics in identifiers before doctrine has admitted terms. |
| 13 | Foundation immutability | Accepted F* AXIOM immutable; same ID with different body is a SHADOW_ATTEMPT kill. | Current git/history plus evidence provenance; no exact ID shadow gate. | MISSING-FROM-CURRENT | Gold for canonical result IDs and gates. |
| 14 | Definition before use | Dependency defined iff in ledger or earlier in same export. | LEGO dependency receipts; ENFORCEMENT stage gate ordering. | EQUIVALENT | Current better for sims; OG better for text-artifact ingestion. |
| 15 | Forward references | Undefined REQUIRES parks instead of repair. | Current blocks if required evidence absent. | EQUIVALENT | OG "park, do not repair" wording is worth reusing. |
| 16 | Near duplicate | Same class, different ID, Jaccard above threshold parks. | Current has no formal near-duplicate admission gate. | MISSING-FROM-CURRENT | Revive for doctrine, queue, and result-entry dedup. |
| 17 | Formula containment | `=` only inside `DEF_FIELD ... FORMULA "<string>"`; unquoted equals rejects. | Current nonclassical gate bans decorative math labels but not notation containment. | MISSING-FROM-CURRENT | Gold for math text hygiene. |
| 18 | Formula carrier-only | "FORMULA strings are carriers only." | Current claim-language gate and no label-only manifold. | OG-BETTER-STATED | Promote verbatim. It blocks fake semantics from syntax. |
| 19 | Formula no hidden semantics | "No binding/precedence/quantification/implication semantics are granted by FORMULA layout." | Current finite-map/invariant requirement. | OG-BETTER-STATED | Strong ancestor of modern no-label-only doctrine. |
| 20 | Formula grammar ladder | "Only explicit ratcheted FORMULA_GRAMMAR ... may introduce structure beyond token/glyph admission." | Current LEGO finite_map and formal fields; no grammar ladder. | MISSING-FROM-CURRENT | Revive for symbolic and proof artifacts. |
| 21 | Formula token fence | Only admitted tokens/glyphs allowed in formula strings. | Current nonclassical foundation requires explicit finite objects. | MISSING-FROM-CURRENT | Current validates semantics later, but not lexical admission. |
| 22 | Derived-only scan | Equality, cartesian, time/causal, number, set/function, complex/quaternion families blocked unless explicitly allowed. | Current label-only and manifold gates; current allows these only when tied to explicit math. | EQUIVALENT | OG gives a useful lexical front-gate; current gives better semantic gate. |
| 23 | Equals-sign permit | Equals sign needs `equals_sign` CANONICAL_ALLOWED. | Current no exact equivalent. | MISSING-FROM-CURRENT | Revive selectively for formal text ingestion. |
| 24 | Digit guard | Digits are barred outside admitted grammar/permissions. | Current finite carrier/probe sets use explicit numbers but no digit lexical gate. | og-only-obsolete | Too strict for modern sim/source files; keep only for bootstrapping doctrine. |
| 25 | ASCII/glyph fence | Content and formulas must pass ASCII and admitted glyph fences. | Current developer default ASCII; no repo gate for glyph admission. | EQUIVALENT | Existing coding style covers most of it; formal artifacts could revive glyph admission. |
| 26 | Probe pressure | For each ten newly accepted specs, require one newly accepted probe. | Current ENFORCEMENT requires falsifiers/negative tests, but no numeric quota. | MISSING-FROM-CURRENT | Gold. Current has the concept but lost the pressure counter. |
| 27 | Probe utilization | A new probe must be referenced by an accepted spec within three accepted batches or it moves to park. | Current micro-first and follow-up gates, but no utilization timer. | MISSING-FROM-CURRENT | Gold for preventing decorative probes. |
| 28 | Kill-if discipline | Kills occur only when item declares KILL_IF, SIM_EVIDENCE declares matching KILL_SIGNAL, and binding passes. | Current mutation/falsifier gates; classification/promotion statuses. | OG-BETTER-STATED | Better kill semantics: declarative, idempotent, evidence-bound. |
| 29 | Kill binding scope | KILL_BIND default local; remote kills require explicit target permission. | Current shared-state/git mutation serial rules, but no semantic remote-kill scope. | MISSING-FROM-CURRENT | Revive for queue/result invalidation. |
| 30 | Ruleset hash gate | Active ruleset hash must match the reported/routed ruleset. | Current freshness/provenance gates; no universal active-ruleset hash in artifacts. | MISSING-FROM-CURRENT | Gold for doctrine version drift. |
| 31 | Thread B never simulates | "Thread B never runs simulations. Thread B consumes SIM_EVIDENCE v1 only." | Gate Doctrine LLM-as-sensor allowed, LLM-as-admission banned; current sim runner contract. | OG-BETTER-STATED | Promote verbatim with modern "admission gate never runs work it judges" variant. |
| 32 | Deterministic parking priority | Newest first, SPEC before PROBE before AXIOM, higher suffix first. | Current queue discipline exists but lacks deterministic park ordering. | MISSING-FROM-CURRENT | Revive if queue replay is a goal. |
| 33 | L0 lexeme set | Tiny bootstrap lexicon; changes are "cosmological" and require a new kernel instance. | Current no equivalent; terminology governed by claim-language and manifold gates. | MISSING-FROM-CURRENT | Gold for primitive vocabulary governance. |
| 34 | No convenience words | "Do not add convenience words. Prefer ratcheting lexemes through TERM pipeline." | Current label-only/claim-language gates. | OG-BETTER-STATED | Promote for doctrine-language changes. |
| 35 | Compound term rule | Compound components must be individually defined/admitted. | Current finite map/domain/codomain fields and source receipts. | EQUIVALENT | Useful exact phrasing for term registry. |
| 36 | Derived-only keyword smuggling | Derived words are blocked even when smuggled as substrings or compounds. | Current no-label-only doctrine; no substring gate. | MISSING-FROM-CURRENT | Revive for sensitive terms: axis, flux, manifold, terrain, parity, witness. |
| 37 | Term admission states | QUARANTINED -> MATH_DEFINED -> TERM_PERMITTED -> LABEL_PERMITTED -> CANONICAL_ALLOWED. | Current status ladder exists for code/results, not terms. | MISSING-FROM-CURRENT | Major dropped proto-gate. This is stronger than current claim-language prose. |
| 38 | MATH_DEF/TERM_DEF/LABEL_DEF/CANON_PERMIT chain | Terms need explicit math definition before term/label/canonical permissions. | Current nonclassical gate demands explicit finite map/invariant. | EQUIVALENT | Current is semantically stronger; OG is better for terminology surfaces. |
| 39 | Term drift ban | Rebinding a term to a different math definition rejects. | Current provenance gates and no overclaim wording; no explicit term rebinding ban. | MISSING-FROM-CURRENT | Revive. Prevents doctrine drift by synonym. |
| 40 | No permanent forbidden words | "No permanent forbidden words. Primitive use outside TERM pipeline is disallowed until CANONICAL_ALLOWED." | Current sensitive-language gates; label-only blocked unless math-bound. | OG-BETTER-STATED | Promote. It avoids taboo lists while keeping admission strict. |
| 41 | Accepted containers | EXPORT_BLOCK, SIM_EVIDENCE, THREAD_S_SAVE_SNAPSHOT only. | Current has sim schemas and result surfaces, less single-container generic. | EQUIVALENT | Useful for bounded import/export lanes. |
| 42 | Megaboot hash gate | Megaboot hash activates and must match for current ruleset. | Current docs are read-gated but not hash-gated. | MISSING-FROM-CURRENT | Revive as doctrine version receipt. |
| 43 | Single evidence token | One evidence token per SIM_SPEC; evidence clears pending state only if matched. | LEGO dependency receipts and result paths; no single-token discipline. | MISSING-FROM-CURRENT | Useful for avoiding many-to-one evidence ambiguity. |
| 44 | Evidence term permission | Evidence mentioning terms must respect CANONICAL_ALLOWED state. | Current claim-language gate blocks overclaim, not term-state use in evidence. | MISSING-FROM-CURRENT | Revive with modern sensitive terms. |
| 45 | Math definition hash match | Evidence must match MATH_DEF hash where applicable. | Current source/result hashes and freshness gate. | EQUIVALENT | Current should make this explicit for formal definitions. |
| 46 | Rejection forensics | Rejection echoes offender literal, rule id, and line. | Current blockers should report exact violation; claim gate reports violations. | OG-BETTER-STATED | Promote as a universal refusal/report format. |
| 47 | Deterministic stage order | Provenance, derived-only, digit, undefined term, schema, dependency, duplicate, pressure, evidence update, commit. | Current stage gate order exists for sims/tool legos. | EQUIVALENT | OG better for import/text gates; current better for sim scientific stages. |
| 48 | Policy/reporting echo | Reports echo policy state flags, export id, and header gate. | Current Results sections often cite commands, not policy state. | MISSING-FROM-CURRENT | Revive for worker/gate receipts. |
| 49 | Full introspection dumps | "FULL ITEM BODIES (no headers-only snapshots)." "FULL ENUMERATION (no placeholders)." | Current LLM Controller bans summaries as substitutes; S audit bans placeholders only legacy. | OG-BETTER-STATED | Promote. It is sharper than "cite files". |
| 50 | Thread S boundary | "Thread S never asserts canon truth and never edits Thread B." | Current controller owns synthesis/edits; external workers cannot override local verification. | OG-BETTER-STATED | Promote as compiler/admission separation. |
| 51 | Thread S no inference | If item body/input missing, emit UNKNOWN or REFUSAL. | LLM Controller: block if no cited evidence. | EQUIVALENT | OG is good exact compiler behavior. |
| 52 | S owns boot id | Emitted containers use S boot id, not copied input boot id. | Current provenance prevents stale receipts, but no compiler-owned id rule. | MISSING-FROM-CURRENT | Revive for generated receipts. |
| 53 | S single output container | S emits exactly one whitelisted container. | Current structured artifacts vary. | EQUIVALENT | Useful for replayable commands. |
| 54 | Deterministic ordering | Lexicographic by ID/term unless verbatim order required; replay/tapes preserve order. | Current no global deterministic ordering rule. | MISSING-FROM-CURRENT | Gold for save docs, ledger diffs, and generated audits. |
| 55 | Source pointers | "Every entry includes source pointers." If absent, REFUSAL listing missing structure. | LLM Controller requires evidence paths for claims. | OG-BETTER-STATED | Promote as artifact-level rule, not just prose behavior. |
| 56 | Merge priority | DUMP_TERMS overrides snapshot TERM_REGISTRY; DUMP_LEDGER_BODIES overrides snapshot ledger bodies. | Current no exact equivalent. | MISSING-FROM-CURRENT | Revive for replay/save compilers. |
| 57 | Seal refusal and placeholder ban | Full save refuses if fuel missing, placeholder substrings appear, or bodies/terms are not fully enumerated. | Current bans placeholders/fabrication risks but lacks save-level compiler refusal. | OG-BETTER-STATED | Promote for any "state snapshot" artifact. |
| 58 | Index/dictionary/replay/mega dump | INDEX_LEDGER, TERM_DICTIONARY, REPLAY_PACK, MEGA_DUMP are deterministic compiler products. | Current ledgers, audits, and result JSONs exist, but no single save compiler suite. | MISSING-FROM-CURRENT | Revive if current repo needs reproducible doctrine snapshots. |
| 59 | Export tape | Planned batches, append-order, entry index, optional branch/batch, exact export block, source pointers. | Current queues/workers have receipts; less exact raw tape format. | MISSING-FROM-CURRENT | Gold lineage for current wave/queue receipts. |
| 60 | Campaign tape | Post-run export plus Thread B report per batch, append-order; refuse if any pair missing. | Current sim/result ledgers require evidence, but not exact pair tapes. | MISSING-FROM-CURRENT | Revive for replayable queue movement. |
| 61 | Lint preflight authority | "This is a preflight; Thread B remains the sole acceptance authority." | Current lint/gate scripts are not admission unless dedicated evidence packet passes. | OG-BETTER-STATED | Promote. Direct ancestor of "generic stage_gate ok is not admission." |
| 62 | Conservative lint | Linter may over-report but must not under-report known hits. | Current gate scripts should fail closed; not worded this compactly. | OG-BETTER-STATED | Promote for all lint/scout tools. |
| 63 | Duplicate/shadow/compound lint | Lint reports duplicate IDs, potential shadow attempts, and unregistered compounds. | Current no exact linter for doctrine terms. | MISSING-FROM-CURRENT | Revive with current sensitive-term registry. |
| 64 | Tape summary | Preserve append order; parse obvious fields; report duplicate export IDs and replay cursor. | Current no exact equivalent. | MISSING-FROM-CURRENT | Useful for backlog/ledger tooling. |
| 65 | Save levels | MIN, FULL+, FULL++; only higher levels include full bodies/term registry/audit embeds. | Current statuses exist but no save-level doctrine. | MISSING-FROM-CURRENT | Major dropped gate. |
| 66 | Audit save doc | Header, required sections, placeholder bans, consistency, optional embed checks. | Current verification commands and result gates. | EQUIVALENT | Current more code-oriented; OG better for snapshot artifacts. |
| 67 | Command-card discipline | Curated cards at end; full list only on demand. | Current tools/skills expose commands ad hoc. | og-only-obsolete | UI-specific; keep only as operator ergonomics. |
| 68 | Reboot kit split | Static megaboot plus dynamic PROJECT_SAVE_DOC; snapshot restores canon; complete save compiles deterministic docs. | Current docs/process lack an explicit static/dynamic reboot split. | MISSING-FROM-CURRENT | Gold for durable recovery. |
| 69 | S-first reboot | Audit save first; only then paste snapshot into B; report state/policy after restore. | Current read-gate before claims; no restore sequence. | MISSING-FROM-CURRENT | Revive for current recovery runbooks. |
| 70 | Failsafe restore | If audit refuses for missing fuel, valid snapshot can restore canon but not deterministic docs. | Current stale receipt handling; no split between canon restore and docs completeness. | MISSING-FROM-CURRENT | Useful nuance. |
| 71 | Thread M mining boundary | Mining lab never writes canon; two lanes: kernel candidates and Rosetta overlay. | Current external research/intake skills separate advisory from canon, but less central. | OG-BETTER-STATED | Promote for JP seam/mining work. |
| 72 | Foundation roadmap | Least-assumption order; derived-only fence is a feature; branch-parallel foundations; topology-first geometry. | Current actual plan guardrail: root constraints -> carrier/probe -> legos -> manifold. | EQUIVALENT | Current is stronger for finite PEPS3D/spinor work. |
| 73 | Advanced objects as hypotheses | Advanced objects are hypotheses, not foundation. | Current no-label-only manifold, explicit finite map/invariant. | EQUIVALENT | Current better operationally; OG wording still useful. |
| 74 | Migration rule | New Thread B bootpack means new megaboot/project; do not load old snapshots; replay campaign tape. | Current docs have read gates, not immutable project lineage. | MISSING-FROM-CURRENT | Gold. Revive for doctrine/kernel changes. |
| 75 | Graveyard discipline | After every batch pass/fail, append exact export and report to campaign tape, then build graveyard reports. | Current blockers/ledgers exist, but graveyard is not this exact. | MISSING-FROM-CURRENT | Revive for failed sim/lego attempts. |
| 76 | Massive batch discipline | Single-container constraint; choose one huge export, sequential feed, or campaign tape; preflight huge blocks. | Current sim-mode says use small batches when gates red; no exact feed-mode schema. | OG-BETTER-STATED | Promote for large queue/doc migrations. |
| 77 | Failure isolation | "Record before repair." Use binary split, exact failure capture, patch, retry. | Current LLM Controller says identify exact gate violation. | OG-BETTER-STATED | Promote verbatim. |
| 78 | No memory for replay | "Never rely on memory for 'did we already feed this?'" | Current mandatory read gate and receipt paths. | OG-BETTER-STATED | Promote for queue and worker fanout. |
| 79 | Project pinning | Any bootpack change creates new megaboot and project; never patch in place. | Current no exact immutable boot lineage. | MISSING-FROM-CURRENT | Revive for current doctrine versions. |
| 80 | Boot verify smoke | After boot, report_state, optional L0 smoke probe; if primitives undefined, stop. | Current preflight/registry wave maps active stage and blockers. | EQUIVALENT | Current more comprehensive; OG smoke check is crisp. |
| 81 | Campaign loop | A/B/C/D loop: B canon advance, S graveyard, S checkpoint/seal, S/audit decision, SIM evidence. | Current wave/gate/ledger/Wizard machinery. | EQUIVALENT | Clear ancestor of current waves and receipts. |
| 82 | Save-level ratchet | "Only FULL+ can advance the ratchet. MIN is interim." | Current status ladder and canonical-by-process; no save-level advancement rule. | MISSING-FROM-CURRENT | Gold. Promote as "only audit-complete receipt can advance status." |
| 83 | Underscore/equality policy | Underscore is structural joiner only; equality has no semantics unless admitted. | Current no-label-only math, but no glyph policy. | MISSING-FROM-CURRENT | Revive for formal/doctrine artifacts. |
| 84 | Thread A noncanon drafting | A drafts only; no smoothing, no implicit memory, cites inputs, default frame, no paraphrased boot emit. | Current controller/subagent truth rules and no invented route claims. | EQUIVALENT | A-specific UI rules are obsolete; principles survive. |
| 85 | Atomic copy/paste boxes | One atomic paste unit; artifact draft prose ban; term/formula/glyph policies in generated blocks. | Current tool-based work makes copy/paste less central. | og-only-obsolete | Keep concept for prompt packets, not a core current gate. |
| 86 | Branch-parallel feed order | Route feed order is logged; branch-parallel foundations keep survivor overlap and contradiction trace. | Current multiple narratives/builders and contradiction ledgers; not feed-order exact. | MISSING-FROM-CURRENT | Revive as lineage metadata for parallel workers. |
| 87 | Thread SIM wrapper | SIM is output-only, required fields, no interpretation; hash lower64; evidence pack includes branch/batch IDs. | LEGO_SIM required fields; current runner writes canonical JSON. | EQUIVALENT | Current better for fields; OG better for "no interpretation" wrapper wording. |
| 88 | SIM manifest audit | SIM inventory and manifest audit catch duplicate SIM_ID, missing fields, chunk refusal, kernel boot hash. | Current canonical sim contract and result surfaces. | EQUIVALENT | Current should recover the duplicate-ID/kernel-hash checks. |
| 89 | Importer extractive-only | "Never invent missing export blocks, missing reports, or missing fields." | Current no self-grading/fabrication; LLM blocks if evidence absent. | OG-BETTER-STATED | Promote verbatim for all log importers and worker result ingestion. |
| 90 | Geometry scaffold | "Geometry is the constraint-manifold scaffold (topology-first; pre-axis)." | Current Nonclassical Manifold Foundation Gate: explicit finite carrier/probe/operator/path, PEPS3D/spinor/quaternion/control. | current-better | Current is stricter and more concrete. |
| 91 | Axes derived not ontology | "Treat Axes 0-6 as derived functions/slices on this manifold, not foundational ontology." | Current AGENTS: Axis0/flux/layer/manifold language label-only unless tied to explicit math. | EQUIVALENT | Current adds finite-map and carrier requirements; OG is excellent wording. |
| 92 | Topology4 checkpoint | Admit topology base-class terms after QIT carriers/grammar stabilize and pair with SIM evidence. | Current requires finite PEPS3D carrier and explicit map/invariant before manifold claims. | current-better | Legacy is proto-current; current foundation gate is the upgrade. |
| 93 | Stage8 derived/killable | Stage8 is derived and killable, useful for SIM planning, not foundation claim until branches and evidence gates survive. | Current completion claim gate and no stage label as proof. | OG-BETTER-STATED | Promote wording for all stage/substage artifacts. |
| 94 | Axis orthogonality | Axis4 != Axis6; topology-family split != graph edges; terrain derived, metric geometry not primitive. | Current terrain/operator math lock and no label-only axis claims. | EQUIVALENT | Current more detailed, but OG states common confusions sharply. |
| 95 | Candidate build order | Build order is roadmap, not commitment; graveyard can resurrect different order. | Current candidate layer order not canon; test all options. | EQUIVALENT | OG "roadmap not commitment" should be promoted. |

## 2. Promotion List

Ranked OG formulations worth adopting verbatim or near-verbatim into current doctrine:

1. "Thread B never runs simulations. Thread B consumes SIM_EVIDENCE v1 only."
   - Modern placement: gate/admission authority separation. Variant: admission gates never run the work they judge.

2. "FORMULA strings are carriers only."
   - Modern placement: claim-language, symbolic, topology, and manifold gates.

3. "No binding/precedence/quantification/implication semantics are granted by FORMULA layout."
   - Modern placement: nonclassical finite-map and proof-artifact requirements.

4. "Thread S never asserts canon truth and never edits Thread B."
   - Modern placement: compiler/importer/output-generator boundaries.

5. "This is a preflight; Thread B remains the sole acceptance authority."
   - Modern placement: lint, scout, and generic stage-gate output disclaimers.

6. "No permanent forbidden words. Primitive use outside TERM pipeline is disallowed until CANONICAL_ALLOWED."
   - Modern placement: sensitive words including manifold, flux, Axis0, witness, parity, terrain, shell, layer.

7. "Do not add convenience words. Prefer ratcheting lexemes through TERM pipeline."
   - Modern placement: doctrine edits and glossary intake.

8. "FULL ITEM BODIES (no headers-only snapshots)." / "FULL ENUMERATION (no placeholders)."
   - Modern placement: state snapshots, evidence packets, worker receipts.

9. "Every entry includes source pointers."
   - Modern placement: generated docs, importers, result summaries, queue movement.

10. "Record before repair."
    - Modern placement: failing sim, broken queue, import/lint regression, and gate debugging workflows.

11. "Never rely on memory for 'did we already feed this?'"
    - Modern placement: worker fanout, queue replay, import tapes, result ingestion.

12. "Only FULL+ can advance the ratchet. MIN is interim."
    - Modern placement: status promotion doctrine: only audit-complete evidence advances status.

13. "Never invent missing export blocks, missing reports, or missing fields."
    - Modern placement: all log importers, closeout ingestion, worker receipt normalization.

14. "Treat Axes 0-6 as derived functions/slices on this manifold, not foundational ontology."
    - Modern placement: axis/terrain/operator doctrine. Keep as a readable parent rule above the finite-map gate.

15. "Stage8 ... not a foundation claim until it survives multiple branches + evidence gates."
    - Modern placement: all stage/substage, layer, and manifold planning docs.

16. "Roadmap, not commitment."
    - Modern placement: candidate build order and queue roadmap language.

## 3. Dropped-Gates List

These proto-gates have no strong modern descendant, or the modern descendant is weaker. Revive calls are intentionally short.

| Dropped proto-gate | Current gap | Revive? |
|---|---|---|
| Closed rejection tag vocabulary | Current blockers/reasons can drift. | Yes; create append-only rejection/status reason registry. |
| Append-only RULE_ID_VOCAB | Current docs lack stable gate IDs across versions. | Yes; required for long-lived audit history. |
| Rule growth only from exploit/test/attack surface | Current ratchet property says failures become gates, but does not restrict new gates enough. | Yes; prevents doctrine bloat. |
| Formula carrier-only grammar ladder | Current bans label-only claims but not syntax-level semantic smuggling. | Yes; especially for math/proof artifacts. |
| Equals/digit/glyph admission fences | Current has general ASCII and semantic gates, not symbolic lexical gates. | Partial; revive for doctrine/formal artifacts, not source code. |
| Term admission ladder | Current has code/result status ladder, not term status ladder. | Yes; major gold. |
| Term drift ban | Current does not block redefinition by soft synonym drift. | Yes. |
| Probe pressure quota | Current wants falsifiers but has no counter pressure. | Yes; tune ratio to current workflow. |
| Probe utilization timer | Current can accumulate decorative probes. | Yes. |
| Deterministic parking priority | Current queues are less replay-deterministic. | Yes, for queue compilers. |
| Active ruleset/megaboot hash in receipts | Current reads docs but does not stamp artifacts with active doctrine hash. | Yes. |
| One evidence token per SIM_SPEC | Current evidence can be many-to-one and ambiguous. | Partial; use where exact binding matters. |
| Thread S boot-id ownership | Generated artifacts can inherit stale source identity. | Yes for importers/compilers. |
| Source-pointer refusal | Current says cite evidence, but generated artifacts may still summarize without hard refusal. | Yes. |
| Save levels MIN/FULL+/FULL++ | Current status ladder does not encode snapshot completeness. | Yes. |
| "Only FULL+ advances ratchet" | Current canonical-by-process is close but not save-level explicit. | Yes. |
| Campaign tape exact export/report pairing | Current receipts are distributed; replay can be harder. | Yes for queue movement. |
| Graveyard pass/fail tape | Current blockers exist, but failed attempts are less first-class. | Yes. |
| New bootpack -> new project, replay not snapshot | Current lacks immutable boot lineage. | Yes for doctrine/kernel revisions. |
| Importer extractive-only command | Current anti-fabrication is broad but not importer-schema exact. | Yes. |
| Branch feed-order logging | Current parallel worker truth lacks feed-order replay metadata. | Partial; useful for Max Assembly receipts. |
| L0 lexeme cosmological change rule | Current has no primitive vocabulary kernel. | Partial; revive for sensitive doctrine terms only. |
| Near-duplicate admission gate | Current duplicate handling is ad hoc. | Yes; use for docs, terms, result IDs. |
| Shadow-attempt kill for same ID/different body | Current git can show changes, but artifact IDs lack semantic immutability. | Yes. |

Dropped gates to revive: 24 yes/partial out of 24 listed.

## 4. Structural Finds

### Replay and Save-Level Discipline

The old stack distinguishes recovery from deterministic reconstruction:

- A snapshot can restore Thread B canon.
- A complete save doc needs full ledger bodies, term registry, indexes, evidence pending, policy state, and audit output.
- MIN is interim. FULL+ is ratchet-moving. FULL++ is a richer audited/replay package.

This anticipates the modern freshness/provenance/canonical-by-process ladder, but current doctrine is mostly result/gate oriented. It does not have a first-class "save completeness controls whether state may advance" rule. The old wording is better for durable recovery: "Only FULL+ can advance the ratchet. MIN is interim."

Lineage mapping:

- Legacy snapshot -> current result/evidence receipt.
- Legacy FULL+ save -> current admitted-by-gate/canonical-by-process status.
- Legacy FULL++ -> current audit bundle plus replayable source/result/index evidence.
- Legacy placeholder/header-only refusal -> current stale-receipt/fabrication risk, but with a sharper compiler failure rule.

### Thread A/B/S/SIM Workflow

Legacy roles:

- Thread A drafts and routes; it does not canonize.
- Thread B admits/rejects canon; it never runs simulations.
- Thread S compiles indexes, saves, tapes, lints, and reports; it never asserts canon truth or edits B.
- Thread SIM emits evidence packs; it does not interpret or canonize them.
- Thread M mines candidates and overlays, never canon.

Modern equivalents:

- Main Codex controller owns synthesis and edits, but must respect gate/evidence boundaries.
- Gate scripts and docs judge claims, but generic lint is not admission.
- Runner/result surfaces emit evidence under canonical sim contracts.
- External workers/subagents are advisory unless verified locally.
- Wizard waves replace A/S/M-style orchestration but currently lack the old hard role grammar.

Best structural extraction: reintroduce the "role cannot do the thing it judges" sentence form. It is clearer than current distributed language.

### Batch Discipline

The bootpacks are obsessed with batch shape:

- one container per message;
- preflight huge blocks;
- exact export tape before replay;
- campaign tape with export/report pairs;
- binary split on failure;
- record before repair;
- never rely on memory for replay status.

This directly anticipates modern sim-mode Max Assembly, queue gates, and receipt validation. Current doctrine says small batches when contract lint or queue safety is red, but the old stack is better at replay logistics. The modern machinery should inherit:

- feed mode declared before large batch work;
- append-only feed tape;
- exact pass/fail report paired to each batch;
- deterministic replay cursor;
- graveyard for failed batches, not just blockers.

### Constraint-Manifold Lineage

The v7.4.7 manifold patch is recognizably proto-current:

- geometry before axes;
- axes derived as functions/slices, not ontology;
- topology before metric/terrain;
- Stage8 as derived/killable planning surface;
- build order as roadmap, not canon.

Current doctrine is better because it names the actual admission record: finite carrier/probe/operator/path set, noncommuting/order-sensitive operation, domain/codomain, finite PEPS3D carrier, JAX/Julia spinor state or tensor, quaternionic map/invariant if used, negative/control condition, receipt path, and blocked downstream consumers. The legacy patch should not override current nonclassical gates, but its plain-language warnings should be promoted above them as readable "why" clauses.

## 5. JP Seam Notes

Relevant proto-witness/proto-parity ideas:

- Thread SIM evidence packs are proto-witnesses: they are output-only, hash-stamped, branch/batch-bound, and non-interpretive.
- Thread B consuming SIM_EVIDENCE but never running SIM is proto-parity by separation: generator and judge are distinct roles.
- Campaign tape export/report pairs are proto-parity ledgers: raw proposal plus independent acceptance/rejection report are stored together.
- The term pipeline is a proto-witness discipline for language: a word is not admissible because it sounds right; it needs a math definition, permission state, and drift protection.
- Probe pressure and probe utilization are proto-adversarial parity: every growth in specs must drag falsifiers behind it, and unused probes are demoted.
- Branch-parallel foundation work plus survivor-overlap logging anticipates current multi-builder/basin convergence gates.
- The Rosetta/kernal split is a JP seam guard: interpretive overlays can help humans navigate, but they do not overwrite canon or count as proof.

Most relevant modern adoption for JP seam work:

1. Treat "witness" and "parity" as TERM-pipeline candidates until explicitly admitted.
2. Require source-pointer refusal for any JP seam extraction.
3. Keep mining/overlay artifacts separate from kernel/admission artifacts.
4. Pair every seam claim with raw extracted quote plus current descendant gate or explicit missing-gate verdict.

## Compact JSON

{"rules_extracted":95,"og_better_stated":24,"missing_from_current":42,"promotion_list_top3":["Thread B never runs simulations. Thread B consumes SIM_EVIDENCE v1 only.","FORMULA strings are carriers only.","Record before repair"],"dropped_gates_revive":24,"output":"BOOTPACK_EXTRACTION_FALLBACK.md"}
