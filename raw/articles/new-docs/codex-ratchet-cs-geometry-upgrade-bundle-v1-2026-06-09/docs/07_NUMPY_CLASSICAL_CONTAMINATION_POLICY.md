# NumPy / Classical Contamination Policy for Codex

NumPy can remain in baselines and legacy diagnostics. It must not become canonical for nonclassical claims.

Block from claim-bearing nonclassical lanes:

- `.numpy()` tensor conversion;
- `np.asarray`, `np.array`, `np.ndarray` as semantic state exchange;
- `pandas.DataFrame` as canonical state;
- `networkx` or adjacency matrices as canonical graph truth;
- flattened operator chains that assume associativity;
- embedding similarity as identity.

Allowed:

- Lane B classical baselines with explicit classification;
- adapter/import/export surfaces that state claim ceiling;
- DLPack/tensor exchange in provider lanes;
- JSON/Arrow artifacts with typed schema;
- proof/witness artifacts with receipts.
