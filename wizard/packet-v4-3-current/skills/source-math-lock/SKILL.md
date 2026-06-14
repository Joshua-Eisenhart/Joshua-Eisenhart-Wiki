# Source Math Lock Skill v4.3

authority_status: canonical-skill

Lock source math before downstream agents, workflows, or sims can reuse it.
This prevents later workers from relitigating or re-inventing conventions.

## When Used

Use for terrain/operator words, Axis-6 UP/DOWN, source-doc tables, atlas rows,
proof assumptions, or any stage where later workers must read one frozen finite
map rather than regenerate the math from memory.

## Method

1. Read the controlling source docs directly and cite paths.
2. Extract formulas, tables, axes, and convention rules verbatim enough to test.
3. Emit one lock artifact with source hashes, row counts, and exact fields.
4. Run an independent audit that recomputes counts from the artifact, not from
   the builder's summary.
5. Record convention drift axes: source versus lock artifact, artifact versus
   runner, wording versus executable order, scratch map versus reference.
6. Downstream stages must read the lock artifact and must not re-derive rows.

## Return Fields

```yaml
source_math_lock:
  source_paths: []
  lock_artifact: ""
  source_hashes: []
  row_counts: ""
  recomputed_checks: []
  convention_drift: []
  downstream_rule: ""
```

Also include the common child receipt fields required by `WIZARD_v4_3.md`:
child role id, compact MMM loaded, required mini-MMMs loaded, source slice,
evidence boundary, output patch, and status.

## Invalid Outputs

- A label table without explicit formulas or finite maps.
- A lock artifact that is audited by the same worker that built it.
- Re-deriving later-stage rows after a lock artifact exists.
- Treating a source lock as proof, admission, or full completion.
