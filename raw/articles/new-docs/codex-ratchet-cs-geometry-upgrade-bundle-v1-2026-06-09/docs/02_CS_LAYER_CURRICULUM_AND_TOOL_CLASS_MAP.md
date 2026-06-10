# CS Layer Curriculum and Tool-Class Map

Add this layer before physics-facing language.

## Classes

1. Graph theory
2. Algebraic / spectral graph theory
3. Hypergraphs + higher-order networks
4. Graph rewriting / rewriting logic
5. Category theory for CS
6. Automata / formal languages / computability
7. E-graphs / equality saturation
8. Combinatorial topology
9. Discrete differential geometry / DEC
10. Causal sets / event structures
11. Probabilistic graphical models + causal AI
12. Geometric deep learning / GNNs

## Immediate tool menu

- Core graph engines: `rustworkx`, `networkx`, `igraph`, `graph-tool`, `networkit`, `Graphs.jl`, `MetaGraphsNext.jl`, `petgraph`.
- Higher-order/hypergraph: `XGI`, `HyperNetX`, `hypergraphx`, `SimpleHypergraphs.jl`, `SimpleDirectedHypergraphs.jl`.
- Rewriting/category: `Catlab.jl`, `AlgebraicRewriting.jl`, `Maude`, `K Framework`, `egg`, `egglog`.
- Topology/geometry: `GUDHI`, `TopoNetX`, `Ripser.py`, `CombinatorialSpaces.jl`, `Decapodes.jl`.
- AI graph stack: `torch_geometric`, optional `GraphNeuralNetworks.jl`, JAX graph tools only after support audit.
- Proof/checking: `z3`, `cvc5`, later `Lean`, `TLA+`, `Maude`.

## Ratchet rule

No install spree. Add one micro-probe per library/function and record the receipt before any load-bearing use.
