# Hardening changelog — 2026-07-01 (external audit pass, claude.ai session)
All changes below are audit-inserted; sync knowingly. Sims' mathematical
content untouched except H-3 (path containment only).

H-1  ADDED    CLAUDE.md — agent contract (hard rules, withdrawn-claims list,
              honest-failure guards, V/W anti-conflation, open-decision fence).
H-2  FIXED    spec_and_reports/ORIENTATION.md had diverged from root
              ORIENTATION.md (two different orientations = agent trap).
              Replaced with a pointer stub; root is canonical.
H-3  FIXED    manifold_build_ladder.py wrote 4 JSONs into the caller's CWD.
              Now writes to sims_and_scripts/out/ (path containment only; no
              math change; verified identical stdout).
H-4  ADDED    run_all.py — deterministic harness: 20 sims, per-sim headline
              invariants with explicit tolerances, honest-failure guards
              (Axis-0 doctrine must stay False; 11/64 collapse must stay 11),
              withdrawn-claim guards ("no linear law" string asserted), JAX
              graceful skip, exit 0/1, writes run_all_report.json.
H-5  ADDED    requirements.txt (numpy/scipy/sympy required, jax optional,
              matplotlib deliberately excluded).
H-6  EDITED   spec §7g: inline AUDIT FLAG on the two-64s tension marked
              PENDING OWNER DECISION (guards against silent harmonization).
H-7  ADDED    spec_and_reports/PURE_MATH_CORE.md — the de-jargoned P1–P11
              proposition ledger from the audit session (referenced by
              CLAUDE.md as the fast label-free entry point).


# Merge pass — 2026-07-01 (later session, χ₂ closure + staleness fix)
Fable's hardening (H-1..H-7 above) is preserved in full. This pass merged it
onto the CURRENT spec state (v29) and fixed the parts that had gone stale,
because fable's zip predated the χ₂ closure done later the same day.

M-1  REFRESHED  spec (v28->v29), rosetta (v11->v12), root ORIENTATION.md to
                current state. Added §7v (χ₂ closed) to the spec.
M-2  ADDED      sims_and_scripts/chi2_openpath_readout_sim.py + its figure —
                the Bargmann open-path phase readout for the eigenvector-sector
                charge. Absent from the hardened zip (built after it).
M-3  UPDATED    the χ₂="open" claims fable correctly flagged, now that it is
                closed at the frame level: spec §7n bridge-status para,
                PURE_MATH_CORE P10 (open->earned) + rosetta row + open queue,
                CLAUDE.md open-decision fence. The terrain-level a2 bit (P9)
                is now the sole remaining open item at this layer.
M-4  PORTED     fable's §7g two-64s AUDIT FLAG (H-6) into v29 (it was authored
                against the zip's spec copy; v29 lacked it).
M-5  WIRED      run_all.py: added a chi2_openpath_readout_sim.py guard
                (closed-loop=0, gauge-invariance, >=99.5% frame-read). Harness
                re-verified: 19 pass / 0 fail / 2 skip (jax) -> GREEN.
Nothing fable added was removed; the withdrawn-claim and honest-failure guards
all still hold.
