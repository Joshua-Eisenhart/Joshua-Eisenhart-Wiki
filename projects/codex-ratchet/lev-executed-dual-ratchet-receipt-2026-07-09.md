# Lev-Executed Dual-Ratchet Receipt - 2026-07-09

Leviathan ran the Codex-Ratchet foundation lane through `lev exec` from a clean
remote Lev checkout at `6bcb9974e`. The execution used the Claude adapter after
the Codex adapter was blocked by an installed-CLI/model-version mismatch.

Lev receipt: `rcpt-be10515fab7be705`
Execution: `2979679a8b8e`
Codex receipt: [[system_v5/ops/LEV_EXECUTED_DUAL_RATCHET_FOUNDATION_RECEIPT_20260709]]

## Run

The executor ran the NumPy foundation script, the Julia 1.12.6 leg, and
`check_agreement.py`. All three exited 0. The regenerated result files remain
in the Codex-Ratchet result directory, not in this wiki.

| Metric | E_then_G | G_then_E |
|---|---:|---:|
| quotient classes | 42 | 42 |
| permanent Hell rejects | 39 | 39 |
| active Purgatory | 957 | 957 |
| Purgatory -> admitted | 5 | 5 |
| Purgatory -> Hell | 37 | 37 |
| late regions | 11 | 11 |
| narrow classes/regions | 33/5 | 33/5 |
| measured Hell re-entry | 0 | 0 |

NumPy/Julia parity passed at `1e-9`; the SMT polarity controls also passed. The
final counts agree, while binding order differs: inhomogeneity appears at step
6 in `E_then_G` and step 4 in `G_then_E`. That is evidence that ratchet order
can affect where structure appears, even when the late quotient is the same.

## Interpretation

This is a genuine bounded dual-ratchet foundation run, not a proof of the
engine. The wiki keeps it as a hypothesis-space research receipt. The ratchet
still has to earn any survivor interpretation, and the four substages must
emerge from the independent geometry/entropy survivor intersection rather than
being inserted as a count or schedule label.

## Related

- [[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[projects/codex-ratchet/wiki-cleanup-and-authority-boundary-2026-07-09]]
