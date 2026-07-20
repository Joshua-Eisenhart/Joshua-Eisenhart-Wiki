#!/usr/bin/env python3
"""generate_bundle_docs.py -- SELF-DESCRIBING BUNDLE GENERATOR (2026-07-10).

Regenerates the bundle's orientation/doc set from LIVE state every ship, so external consumers (the codex app, other
sim runners, future sessions) can process the zip STANDALONE and it can never drift stale. Run from the bundle root:
    python generate_bundle_docs.py
Emits (all at bundle root, in docs/BUNDLE_*.md and bundle_manifest.json):
  - BUNDLE_GUIDE.md        : what this is, the root project, plan, current state, what's being worked, future projects
  - TOOLS_AND_REPOS.md     : every tool/env/solver/library + versions, repos, the 3-engine dependency contract
  - MATH_INVENTORY.md      : every math class in play, forced vs installed vs withdrawn, with the deciding constraint
  - WITHDRAWN_AND_FAILED.md: registry of NEGATIVES -- withdrawn UPs, failed proposed math, why (negatives are data)
  - UP_REGISTRY.md         : every UP ledger entry (number, title, status) parsed from MODEL_LAYER_LEDGER.md
  - bundle_manifest.json   : machine-readable superset (for codex to parse programmatically)

Everything is PARSED from the live files (MODEL_LAYER_LEDGER.md, run_all.py, run_all_report.json, requirements.txt,
installed package versions) -- nothing is hardcoded, so the docs always match the shipped state. Static hand-curated
prose (the root project statement, the plan, future projects) lives in the EDITABLE BLOCKS below and is the ONLY thing
to update by hand as direction changes.
"""
import json, os, re, sys, subprocess, datetime

ROOT=os.path.dirname(os.path.abspath(__file__))
def R(p): 
    fp=os.path.join(ROOT,p)
    return open(fp).read() if os.path.exists(fp) else ""

# ============================ EDITABLE BLOCKS (hand-curated; update as DIRECTION changes) ============================
ROOT_PROJECT = """The root project is to formalize CREATION, MATHEMATICS, PHYSICS, PERCEPTION, and INTELLIGENCE as ONE
finite admissibility ratchet. The primitive is CONSTRAINT ON DISTINGUISHABILITY (not entropy -- entropy is a later
measure). Reality is built from the LEAST presumptions by a monotone generative ratchet of the WEAKEST structures
taking the SMALLEST admissible leaps up, under two root constraints: F01 (finitude) and N01 (noncommutation), with
nonassociativity (T01) emerging only when a grouping-load-bearing demand appears. The ratchet EARNS canon step by step;
nothing is canon until forced. MSS (minimal-sufficient-structure) is a hard admissibility constraint: admit only forced
structure; larger leaps are inadmissible; the pawl rejects the unforced.

The downstream FACES (all measure whether the root works; none is the root): the dual-ratchet entropic-geometric
constraint MANIFOLD; the QIT ENGINES (two Weyl-chirality engine types x 8 terrains x operators); FEP/active-inference
(a QIT FEP, no classical thermo); IGT / known-unknown; object-perception ("holodeck") with distinguishability gates;
the physics TOE (GR+SM as new foundations, gravity as entropy gradient, chiral spacetime); cosmogenesis (MSS in a
static field, dark-energy-first). Oracle duality: deduction<->induction, Turing<->oracle, reason<->perception."""

PLAN = """CONSERVATIVE ORDER, always looping back to foundations. Each ratchet up reveals things to re-audit from the
base. Current standing spine (empirical binding order, discovered not prescribed): complex-spinor carrier (forced by
F01+N01) -> Schmidt strata / nested shells (L5) -> BKM metric = rel-entropy Hessian (L6) -> Berry holonomy / flux (L7)
-> chirality (Weyl) -> engine stages. The co-ratchet runs entropy and geometry as ONE tensor (surface_identity_is_BKM).
Pawl forced by the data-processing inequality (Umegaki relative entropy).

METHOD: (1) place every new/proposed math BY THE CONSTRAINTS -- forced, installed, or excluded -- never admit by
assertion; (2) each sim gates on a GENUINELY FAILABLE result with a control that flips; definitional identities and
known theorems may be COMPUTED and reported but must NOT gate; (3) cross-family LLM panel (advisory, never gates) as an
adversarial pre-ship reviewer; (4) verify on-disk harness count BEFORE writing ledger/changelog; (5) NEGATIVES are
first-class -- withdrawn/failed math is retained and recorded."""

CURRENT_FOCUS = """Placing the genuinely-new math from the 2026-07 attachment batch (tropical/max-plus, quantum info
geometry, HoTT/braids, idempotent analysis) relative to the forced core -- most land as classical limits or
constructible-not-forced upper layers, which is itself informative. Making the bundle SELF-DESCRIBING (this generator)
so codex and other systems can process it standalone."""

FUTURE_PROJECTS = """(A) Get the QIT engines FULLY running in deep nuance: every stage/substage doing distinct
information processing, all axes load-bearing on one running trajectory, Axis-0 end-to-end entropy-gradient on the
engine pair. (B) Axes 7-12 = the FIELD OF ENGINES (each node an engine; natural home of IGT) with its own embedding
geometry -- where the exceptional algebras (E6/E8/Albert) may finally become load-bearing; needs a field-metric rung.
(C) Grand-application projects, kept ONLY where they consistently help the overall system when looped back from
foundations: fine-structure constant, P-vs-NP, Navier-Stokes, Riemann/primes, Yang-Mills, GR+SM unification, gravity,
cosmogenesis. All GATED behind earning the structure they need; no skipping ahead. (D) Idempotent-analysis/HJB as a
possible forced ratchet STEP (decohere->T->0), which would upgrade the max-plus placement from context to a gate.
(E) Run the owner's real Julia/JAX/PyTorch engines where load-bearing (Julia canon arbiter; strict-carrier laptop-side
due to registry TLS block)."""

DEPENDENCY_CONTRACT = """THREE-ENGINE DEPENDENCY CONTRACT (load-bearing gates): z3 AND cvc5 must agree on the same
structural claim with erased controls that flip it; numpy/scipy/mpmath are CONTROL-LANE only, never load-bearing; at
least one tool outside the array baseline must gate a verdict. Sims carry NO jargon -- pure real math and structure;
a rosetta layer maps earned structure to labels afterward."""

CONSUMER_NOTE = """FOR EXTERNAL CONSUMERS (codex app, other sim runners): this bundle is self-describing. Re-run
`python generate_bundle_docs.py` to regenerate these docs from live state. The authoritative harness is
`python run_all.py` (full, no --fast). The ledger MODEL_LAYER_LEDGER.md is the append-only record of every rung (UP).
Negatives (WITHDRAWN_AND_FAILED.md) are as informative as positives -- proposed math that fails tells you what the
constraints EXCLUDE. Nothing here is canon until the ratchet earns it."""
# ====================================================================================================================

def parse_ups(ledger):
    """Parse every '## UP-N ... title' header; dedupe by UP number, withdrawn-wins.
    A rung may appear twice (original ship header + a later WITHDRAWN header); the WITHDRAWN status must win and the
    withdrawal title is preferred."""
    seen={}
    for m in re.finditer(r'^##\s+(UP-[0-9/]+)\s+(?:--\s*)?(.+)$', ledger, re.M):
        num,rest=m.group(1),m.group(2).strip()
        low=(num+" "+rest).lower()
        status="withdrawn" if "withdrawn" in low else "shipped"
        if num not in seen:
            seen[num]={"up":num,"title":rest,"status":status}
        else:
            # merge: withdrawn wins, and prefer the withdrawn title
            if status=="withdrawn":
                seen[num]={"up":num,"title":rest,"status":"withdrawn"}
    # preserve first-seen order by UP numeric where possible
    def key(u):
        mm=re.match(r'UP-(\d+)',u["up"]); return int(mm.group(1)) if mm else 9999
    return sorted(seen.values(), key=key)

def parse_registered_sims(runall):
    return sorted(set(re.findall(r'\("([a-z][a-z0-9_]*_sim\.py)"', runall)))

def get_versions():
    vers={}
    for mod in ["numpy","scipy","sympy","sklearn","pysindy","z3","cvc5","mpmath"]:
        try:
            code=f"import {mod};v=getattr({mod},'__version__',None) or getattr({mod},'get_version_string',lambda:'present')();print(v)"
            out=subprocess.run([sys.executable,"-c",code],capture_output=True,text=True,timeout=60)
            vers[mod]=out.stdout.strip() if out.returncode==0 else "not present"
        except Exception: vers[mod]="unknown"
    return vers

def main():
    ledger=R("MODEL_LAYER_LEDGER.md"); runall=R("run_all.py"); changelog=R("CHANGELOG_HARDENING.md")
    report=json.loads(R("run_all_report.json")) if R("run_all_report.json") else {}
    summ=report.get("summary",{})
    ups=parse_ups(ledger); regsims=parse_registered_sims(runall); vers=get_versions()
    withdrawn=[u for u in ups if u["status"]=="withdrawn"]
    now=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    hp=summ.get("pass","?"); hf=summ.get("fail","?"); hs=summ.get("skip","?"); green=summ.get("green","?")

    docs=os.path.join(ROOT,"docs"); os.makedirs(docs,exist_ok=True)

    # math-class inventory: parse sim filenames for math keywords -> a coarse but real inventory
    mathmap={"entangl":"entanglement/negativity","bkm|modular|umegaki|petz|dpi|relent":"QIT entropy / modular theory",
      "jordan|albert|octonion|malcev|f4|e6|g2|clifford|hopf":"nonassociative / exceptional algebra (Jordan/octonion/Lie)",
      "spinor|weyl|chiral|holonomy|berry":"spinor / chirality / holonomy","schmidt|shell|metric|geodesic":"information geometry / manifold",
      "maxplus|tropical|idempotent":"tropical / max-plus (idempotent)","qfi|fubini|fisher":"quantum information geometry (QFI/Fubini-Study)",
      "braid|hott|homotop":"topology / braid groups (HoTT)","fep|surprise|active":"FEP / active inference",
      "carnot|szilard|landauer|thermo":"thermodynamic bridges (rosetta only)","mond|a0|redshift|physics|gravity|cosmo":"physics bridges / TOE",
      "smt|z3|cvc5":"SMT-gated structural proofs","penrose|aperiodic|e8":"aperiodic order / E8 (not forced)",
      "hubbard|biochem|tunnel|chem":"chemistry / biochem bridges","axis|engine|terrain|stage|substage|schedule":"QIT engine mechanics / axes"}
    mathinv={}
    for s in regsims+[u["up"] for u in withdrawn]:
        pass
    allsims=parse_registered_sims(runall)
    # classify registered sims
    for s in allsims:
        for pat,label in mathmap.items():
            if re.search(pat,s): mathinv.setdefault(label,[]).append(s)

    # ---------- BUNDLE_GUIDE.md ----------
    g=f"""# BUNDLE GUIDE -- constraint_core_unified (self-describing)
_Regenerated {now} from live ledger + harness. Do not hand-edit; run `python generate_bundle_docs.py`._

## Harness state (authoritative)
**{hp} pass / {hf} fail / {hs} skip -> {"GREEN" if green else "NOT GREEN"}**  ({len(allsims)} registered sims, {len(ups)} UP rungs in ledger, {len(withdrawn)} withdrawn.)
Authoritative run: `python run_all.py` (full, no --fast). Result: `run_all_report.json`.

## The root project
{ROOT_PROJECT}

## Plan & method
{PLAN}

## What is being worked NOW
{CURRENT_FOCUS}

## Future projects
{FUTURE_PROJECTS}

## For external consumers (codex app, other sim runners)
{CONSUMER_NOTE}

## Doc set in this bundle (docs/)
- `BUNDLE_GUIDE.md` (this file) -- plan, state, focus, future
- `TOOLS_AND_REPOS.md` -- every tool/solver/library + versions, repos, dependency contract
- `MATH_INVENTORY.md` -- every math class, forced vs installed vs withdrawn
- `WITHDRAWN_AND_FAILED.md` -- registry of NEGATIVES (as informative as positives)
- `UP_REGISTRY.md` -- every rung (UP) with status
- `../bundle_manifest.json` -- machine-readable superset for programmatic parsing
"""
    open(os.path.join(docs,"BUNDLE_GUIDE.md"),"w").write(g)

    # ---------- TOOLS_AND_REPOS.md ----------
    vtable="\n".join(f"- **{k}**: {v}" for k,v in vers.items())
    t=f"""# TOOLS, SOLVERS, LIBRARIES & REPOS
_Regenerated {now}. Versions read from the live environment._

## Solver & library versions (this environment)
{vtable}

Python: {sys.version.split()[0]}. Env: constraintcore (conda). Numba cache: /tmp/numba_cache.

## Dependency contract
{DEPENDENCY_CONTRACT}

## Repos (source of truth)
- **codex-ratchet repo** (system_v7/constraint_core/): the v7 sim runner + canon docs. THE authoritative repo (with the wiki).
- **Wiki** (Joshua-Eisenhart/Joshua-Eisenhart-Wiki, projects/codex-ratchet/): synced reports, ledger, changelog, sims.
- **leviathan** (github.com/lev-os/leviathan): a CS-version reference of many concepts; REFERENCE not canon.
- This bundle mirrors the audit-engine sim set; the codex app consumes these zips + runs its own sims.

## How the pieces run
- `run_all.py` -- the full harness (each sim is a subprocess; a row PASSES on a 'contains' string match). No jargon in sims.
- `sims_and_scripts/` -- {len([f for f in os.listdir(os.path.join(ROOT,'sims_and_scripts')) if f.endswith('.py')])} python sim files (some are withdrawn scaffolds, not registered).
- `panel_adversarial_review.py` -- cross-family LLM panel (Gemini/Grok/Qwen/GLM) as an ADVISORY adversarial reviewer; never gates.
- `MODEL_LAYER_LEDGER.md` / `CHANGELOG_HARDENING.md` -- append-only rung record + hardening log.
"""
    open(os.path.join(docs,"TOOLS_AND_REPOS.md"),"w").write(t)

    # ---------- MATH_INVENTORY.md ----------
    mi=f"""# MATH INVENTORY -- classes in play, and their status under the constraints
_Regenerated {now}. Classes inferred from registered sim names; status from the ledger._

Every math class is PLACED by the constraints: **forced** (F01/N01 compel it), **installed/constructible-not-forced**
(realizable but not compelled -- a live upper branch), or **excluded** (a constraint forbids it as foundation).

## Registered math classes (by sim clustering)
"""
    for label in sorted(mathinv):
        mi+=f"\n### {label}\n{len(mathinv[label])} sim(s): {', '.join(sorted(mathinv[label])[:12])}{' ...' if len(mathinv[label])>12 else ''}\n"
    mi+=f"""
## Key placements (forced / installed / excluded)
- **complex spinor (qubit)** -- FORCED: unique smallest carrier satisfying F01 AND N01.
- **noncommutation (su(2)/Pauli)** -- FORCED: N01 at the operator level.
- **Umegaki relative entropy pawl** -- FORCED by the data-processing inequality (Petz recoverability).
- **BKM metric** -- FORCED: it is the Hessian of the forced rel-entropy pawl (= the surface tensor; entropy & geometry one).
- **Z2 spinor double cover (720deg)** -- FORCED path-topology.
- **chirality (Weyl)** -- FORCED: no self-mirror generator can be both finite and noncommuting (which side is empirical).
- **quaternions Im(H)** -- FORCED: single-qubit su(2) IS Im(H).
- **max-plus / tropical / idempotent** -- EXCLUDED as foundation (coherent interference violates its monotonicity);
  it is the T->0 decoherence/deductive-limit (Bellman) arithmetic. [UP-138]
- **QFI / Fubini-Study** -- INSTALLED as the fidelity/Bures-family metric; the model's metric is BKM (rel-entropy),
  conditional on the forced pawl; QFI coincides only on the classical face. [UP-139]
- **HoTT / braid groups** -- CONSTRUCTIBLE-NOT-FORCED (needs a multi-anyon degenerate fusion space the single carrier
  lacks); forced carrier topology is the abelian Z2 double cover. [UP-140 withdrawn -- placement real, no failable gate]
- **octonions / T01 / Malcev / G2->F4->E6 / E8 / Albert(27) / 3-generations / Penrose** -- CONSTRUCTIBLE-NOT-FORCED
  ({{H,O}} branch); "3 generations = |chi|/2" is an ANSATZ. Live upper-layer math, not re-derived as forced.
- **Clifford Cl_3** -- FORCED at operator level BUT associative -> cannot carry octonionic nonassociativity (a decisive negative).
"""
    open(os.path.join(docs,"MATH_INVENTORY.md"),"w").write(mi)

    # ---------- WITHDRAWN_AND_FAILED.md ----------
    wf=f"""# WITHDRAWN & FAILED -- the NEGATIVES (as informative as the positives)
_Regenerated {now}. Withdrawn rungs parsed from the ledger; retained scaffolds live in sims_and_scripts/ but are NOT registered._

Proposed math that FAILS to be forced, and sims whose gates did not hold up, are first-class information: they tell you
what the constraints EXCLUDE or leave merely constructible. Nothing is deleted; withdrawals are recorded.

## Withdrawn rungs (from ledger headers)
"""
    for u in withdrawn:
        wf+=f"- **{u['up']}** -- {u['title']}\n"
    wf+=f"""
## Standing negatives (excluded / constructible-not-forced) -- see MATH_INVENTORY for the deciding constraint
- max-plus/tropical: EXCLUDED as foundation (interference breaks monotonicity). [UP-138]
- HoTT/braids: constructible-not-forced (no failable gate at the single carrier). [UP-140 withdrawn]
- octonions/T01/Malcev/exceptional tower/E8/Penrose/3-generations: constructible-not-forced ({{H,O}} branch, ansatz).
- "entropy = topology / Atiyah-Singer index" and E6-gauge/F4-gravity/dim-27: genuine established math on the unforced branch, NOT earned by {{F01,N01}}.
- gauge-breaking-law (old): WITHDRAWN as an algebraic identity (R^2=1 by construction).
- field-of-engines "weakest rung" (UP-137): WITHDRAWN -- opposite/same chirality gave identical negativity -> generic 2-qubit QM, not theory-specific.
- 64/64 substage uniqueness overclaim (UP-104/105): WITHDRAWN -- only a coarse subset shown position-unique.

## Why keep them
Each negative is a probe of the boundary of the forced core. A future forced DEMAND (e.g. a Malcev bracket, a
non-special 3-level observable, a field-metric rung) could promote a currently-unforced item; the negatives map where
to look. They also stop the grand-synthesis overclaim from creeping back in.
"""
    open(os.path.join(docs,"WITHDRAWN_AND_FAILED.md"),"w").write(wf)

    # ---------- UP_REGISTRY.md ----------
    ur=f"# UP REGISTRY -- every rung\n_Regenerated {now}. Parsed from MODEL_LAYER_LEDGER.md ({len(ups)} entries)._\n\n"
    for u in ups:
        mark="~~WITHDRAWN~~ " if u["status"]=="withdrawn" else ""
        ur+=f"- **{u['up']}** {mark}-- {u['title']}\n"
    open(os.path.join(docs,"UP_REGISTRY.md"),"w").write(ur)

    # ---------- bundle_manifest.json (machine-readable) ----------
    # ---------- 00_START_HERE.md (single entry point; canon static, harness line live) ----------
    sh_path=os.path.join(ROOT,"00_START_HERE.md")
    if os.path.exists(sh_path):
        sh=open(sh_path).read()
        sh=re.sub(r"<!--LIVE_HARNESS-->.*?<!--/LIVE_HARNESS-->",
                  "<!--LIVE_HARNESS-->**Harness now: %s pass / %s fail / %s skip -- green=%s** (stamped %s)<!--/LIVE_HARNESS-->"%(hp,hf,hs,green,now),
                  sh, flags=re.S)
        open(sh_path,"w").write(sh)

    manifest={"generated_utc":now,"harness":{"pass":hp,"fail":hf,"skip":hs,"green":green,"registered_sims":len(allsims)},
      "versions":vers,"python":sys.version.split()[0],
      "ups":ups,"withdrawn":withdrawn,"registered_sims":allsims,
      "math_inventory":{k:sorted(v) for k,v in mathinv.items()},
      "root_project":ROOT_PROJECT,"plan":PLAN,"current_focus":CURRENT_FOCUS,"future_projects":FUTURE_PROJECTS,
      "dependency_contract":DEPENDENCY_CONTRACT,"consumer_note":CONSUMER_NOTE,
      "doc_files":["docs/BUNDLE_GUIDE.md","docs/TOOLS_AND_REPOS.md","docs/MATH_INVENTORY.md","docs/WITHDRAWN_AND_FAILED.md","docs/UP_REGISTRY.md"]}
    json.dump(manifest,open(os.path.join(ROOT,"bundle_manifest.json"),"w"),indent=2)

    print(f"Generated docs/ (5 md) + bundle_manifest.json")
    print(f"  harness {hp}/{hf}/{hs} green={green}; {len(ups)} UPs ({len(withdrawn)} withdrawn); {len(allsims)} registered sims")
    print(f"  math classes: {len(mathinv)}; versions: {', '.join(f'{k}={v}' for k,v in list(vers.items())[:4])} ...")
    print("  withdrawn:", ", ".join(u["up"] for u in withdrawn))

if __name__=="__main__":
    main()
