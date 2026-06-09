---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [systems, attractors, viability, basins, research, anti-teleology]
sources:
  - /tmp/wiki_systems_attractor_research_arxiv_20260518.json
  - /tmp/wiki_anti_teleology_research_arxiv_20260518.json
---

# Basin Stability and Viability Support

## Purpose
This page gives source-backed support for the wiki's attractor-basin and anti-teleology language.

The key bridge:

A present state can be selected by the set of viable continuations available from it, without any single future continuation becoming privileged as a final cause.

That is the research-friendly version of anti-teleology / basin teleology.

## Basin stability
Basin stability studies how likely a dynamical system is to return to or remain in an attractor basin under perturbations.

Useful role in this wiki:
- gives a non-mystical meaning to “basin pull”;
- keeps perturbation and stability central;
- matches the row-level formal-scout work in [[perturbation-depth-basin-edge-table]];
- helps prevent “attractor” from becoming just a narrative theme.

MMM sentence:
- A basin is strong when perturbations keep returning to it, not when prose names it first.

## Viability theory
Viability theory studies states and trajectories that can remain inside constraints over time.

Useful role in this wiki:
- gives a formal support lane for future-option pressure;
- treats selection as survival of admissible continuations;
- keeps many possible futures live rather than privileging one endpoint;
- links directly to [[anti-teleology-future-option-selection]].

MMM sentence:
- The present is constrained by the continuations it can still keep viable.

## Persistent topology of dynamics
Persistent homology and TDA can detect durable structure in trajectories, time series, or reconstructed attractors.

Useful role in this wiki:
- turns basin shape into a measurable question;
- links to [[topology-carrier-tool-lane]] and GUDHI;
- supports claims only where persistence/filtration results exist.

MMM sentence:
- Persistence asks which basin features survive a change of scale.

## Higher-order dynamics
Higher-order networks, hypergraphs, simplicial complexes, and cell complexes preserve multi-way relations that pairwise graphs erase.

Useful role in this wiki:
- prevents pairwise collapse of basin structure;
- connects XGI/TopoNetX to attractor-basin support;
- supports the rule that wide exploration may reveal a basin with multi-way shape.

MMM sentence:
- A basin made of multi-way constraints cannot be honestly reduced to edges.

## Research seeds

### Basin stability / complex networks
- `1612.06015v1` — Multi-node basin stability in complex dynamical networks (2016-12-19)
  - fit: Dynamical entities interacting with each other on complex networks often exhibit multistability. The stability of a desired steady regime (e.g., a synchronized state) to large perturbations is critical in the operation of many real-world networked dynamical systems such as ecosys
- `2009.03824v4` — System Size Identification from Sinusoidal Probing in Diffusive Complex Networks (2020-09-01)
  - fit: One of the most fundamental characteristic of a complex system is its size (or volume), which, in many modelling, is represented by the number of its individual components. Complex systems under investigation nowadays are typically large and/or time-varying, rendering their ident
- `2509.24554v1` — Synchronization transitions and spike dynamics in a higher-order Kuramoto model with Lévy noise (2025-09-29)
  - fit: Synchronization in various complex networks is significantly influenced by higher-order interactions combined with non-Gaussian stochastic perturbations, yet their mechanisms remain mainly unclear. In this paper, we systematically investigate the synchronization and spike dynamic
- `1612.03654v1` — Deciphering the imprint of topology on nonlinear dynamical network stability (2016-12-12)
  - fit: Coupled oscillator networks show a complex interrelations between topological characteristics of the network and the nonlinear stability of single nodes with respect to large but realistic perturbations. We extend previous results on these relations by incorporating sampling-base

### Viability / constraints
- `1809.05509v1` — Feasibility and coordination of multiple mobile vehicles with mixed equality and inequality constraints (2018-09-14)
  - fit: We consider the problem of feasible coordination control for multiple homogeneous or heterogeneous mobile vehicles subject to various constraints (nonholonomic motion constraints, holonomic coordination constraints, equality/inequality constraints etc). We develop a general frame
- `2511.19779v1` — Viability Theory in the $1$-Wasserstein Space (2025-11-24)
  - fit: In this article, we establish necessary and sufficient viability conditions for continuity inclusions over the 1-Wasserstein space. Depending on the regularity properties of the dynamics, we derive two results which are based on fairly different proof strategies. When the admissi
- `2005.07691v1` — Safe Motion Planning for Autonomous Driving using an Adversarial Road Model (2020-05-15)
  - fit: This paper presents a game-theoretic path-following formulation where the opponent is an adversary road model. This formulation allows us to compute safe sets using tools from viability theory, that can be used as terminal constraints in an optimization-based motion planner. Base
- `2201.06399v1` — Cooperative constrained motion coordination of networked heterogeneous vehicles (2022-01-17)
  - fit: We consider the problem of cooperative motion coordination for multiple heterogeneous mobile vehicles subject to various constraints. These include nonholonomic motion constraints, constant speed constraints, holonomic coordination constraints, and equality/inequality geometric c
- `2510.03367v2` — Viability-Preserving Passive Torque Control (2025-10-03)
  - fit: Conventional passivity-based torque controllers for manipulators are typically unconstrained, which can lead to safety violations under external perturbations. In this paper, we employ viability theory to pre-compute safe sets in the state-space of joint positions and velocities.

### Persistent homology / dynamics
- `2601.10900v2` — A Stable Measure of Chaos in Dynamical Systems using Persistent Homology (2026-01-15)
  - fit: Many real-world dynamics exhibit chaos, a phenomenon in which neighboring trajectories in the state space of a dynamical system diverge exponentially over time. A common measure used for quantifying the degree of this divergence is the maximal Lyapunov exponent, which relies on p
- `2009.08972v1` — Using Zigzag Persistent Homology to Detect Hopf Bifurcations in Dynamical Systems (2020-09-18)
  - fit: Bifurcations in dynamical systems characterize qualitative changes in the system behavior. Therefore, their detection is important because they can signal the transition from normal system operation to imminent failure. While standard persistent homology has been used in this set
- `2305.08999v3` — Wavelet-Based Density Estimation for Persistent Homology (2023-05-15)
  - fit: Persistent homology is a central methodology in topological data analysis that has been successfully implemented in many fields and is becoming increasingly popular and relevant. The output of persistent homology is a persistence diagram -- a multiset of points supported on the u
- `2408.15834v1` — Characterization of dynamical systems with scanty data using Persistent Homology and Machine Learning (2024-08-28)
  - fit: Determination of the nature of the dynamical state of a system as a function of its parameters is an important problem in the study of dynamical systems. This problem becomes harder in experimental systems where the obtained data is inadequate (low-res) or has missing values. Rec
- `1907.11182v2` — Fractal Dimension Estimation with Persistent Homology: A Comparative Study (2019-07-25)
  - fit: We propose that the recently defined persistent homology dimensions are a practical tool for fractal dimension estimation of point samples. We implement an algorithm to estimate the persistent homology dimension, and compare its performance to classical methods to compute the cor

### Higher-order / cell-complex dynamics
- `2510.05253v2` — Collective dynamics on higher-order networks (2025-10-06)
  - fit: Higher-order interactions that nonlinearly couple more than two nodes are important in many networked systems, and their effects on collective dynamics are increasingly being studied. Here we provide an overview of this rapidly growing field, and of the techni
- `2203.06601v1` — Dynamics on higher-order networks: A review (2022-03-13)
  - fit: Network science has evolved into an indispensable platform for studying complex systems. But recent research has identified limits of classical networks, where links connect pairs of nodes, to comprehensively describe group interactions. Higher-order networks,
- `2402.14938v1` — Contagion dynamics on higher-order networks (2024-02-22)
  - fit: Understanding the dissemination of diseases, information, and behavior stands as a paramount research challenge in contemporary network and complex systems science. The COVID-19 pandemic and the proliferation of misinformation are relevant examples of the impo
- `2303.18169v2` — Dynamical fluctuations of random walks in higher-order networks (2023-03-31)
  - fit: Although higher-order interactions are known to affect the typical state of dynamical processes giving rise to new collective behavior, how they drive the emergence of rare events and fluctuations is still an open problem. We investigate how fluctuations of a 
- `9307078v1` — The Langevin equation on a cell complex (1993-07-11)
  - fit: We consider a cell-complex in an arbitrary Hausdorff space as a dynamical object that can be coupled to a field defined on the complex. The Langevin equation is then derived for this field. In other words, a noise-field is created resulting from the field/geom
- `2605.15955v1` — Kalman Filtering on Cell Complexes (2026-05-15)
  - fit: Inferring latent dynamics from multivariate time-series defined over topological cell complexes is crucial for capturing the complex, higher-order interactions inherent in real-world systems such as in water, sensor, and transportation networks. However, recon
- `2305.16174v2` — From Latent Graph to Latent Topology Inference: Differentiable Cell Complex Module (2023-05-25)
  - fit: Latent Graph Inference (LGI) relaxed the reliance of Graph Neural Networks (GNNs) on a given graph topology by dynamically learning it. However, most of LGI methods assume to have a (noisy, incomplete, improvable, ...) input graph to rewire and can solely lear
- `2510.05831v3` — Phase locking and multistability in the topological Kuramoto model on cell complexes (2025-10-07)
  - fit: Higher-order interactions fundamentally shape collective dynamics in oscillator networks. The topological Kuramoto model captures these effects by extending synchronization models to include interactions between cells of arbitrary dimension within simplicial a

### Policy selection / future-option pressure
- `1904.08149v2` — Bayesian policy selection using active inference (2019-04-17)
  - fit: Learning to take actions based on observations is a core requirement for artificial agents to be able to be successful and robust at their task. Reinforcement Learning (RL) is a well-known technique for learning such policies. However, curr
- `2209.02550v3` — Efficient search of active inference policy spaces using k-means (2022-09-06)
  - fit: We develop an approach to policy selection in active inference that allows us to efficiently search large policy spaces by mapping each policy to its embedding in a vector space. We sample the expected free energy of representative points i
- `2311.06417v1` — Resolving uncertainty on the fly: Modeling adaptive driving behavior as active inference (2023-11-10)
  - fit: Understanding adaptive human driving behavior, in particular how drivers manage uncertainty, is of key importance for developing simulated human driver models that can be used in the evaluation and development of autonomous vehicles. Howeve
- `1807.02128v4` — Adaptive Path-Integral Autoencoder: Representation Learning and Planning for Dynamical Systems (2018-07-05)
  - fit: We present a representation learning algorithm that learns a low-dimensional latent dynamical system from high-dimensional \textit{sequential} raw data, e.g., video. The framework builds upon recent advances in amortized inference methods t
- `2411.09198v1` — Risk-aware MPPI for Stochastic Hybrid Systems (2024-11-14)
  - fit: Path Planning for stochastic hybrid systems presents a unique challenge of predicting distributions of future states subject to a state-dependent dynamics switching function. In this work, we propose a variant of Model Predictive Path Integ
- `2405.04498v1` — Generative Planning with Fast Collision Checks for High Speed Navigation (2024-05-07)
  - fit: Reasoning about large numbers of diverse plans to achieve high speed navigation in cluttered environments remains a challenge for robotic systems even in the case of perfect perceptual information. Often, this is tackled by methods that ite
- `1312.4185v1` — Comment: Causal entropic forces (2013-12-15)
  - fit: In this comment I argue that the causal entropy proposed in [1] is state-independent and the entropic force is zero for state-independent noise in a discrete time formulation and that the causal entropy description is incomplete in the cont
- `1308.4375v1` — Comment on Phys. Rev. Lett. 110, 168702 (2013): Causal Entropic Forces (2013-08-20)
  - fit: The recent Letter by Wissner-Gross and Freer [1] proposes a relationship between intelligence and entropy maximization based on a causal generalization of entropic forces over configuration space paths, which may beautifully induce sophisti
- `1604.05393v1` — An Adaptive Learning Mechanism for Selection of Increasingly More Complex Systems (2016-04-19)
  - fit: Recently it has been demonstrated that causal entropic forces can lead to the emergence of complex phenomena associated with human cognitive niche such as tool use and social cooperation. Here I show that even more fundamental traits associ

## How to use this page
Use it to support language in:
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[attractor-basin-row-level-evidence-ledger]]
- [[topology-carrier-tool-lane]]

Do not use it to promote a current result. It is research support, not repo evidence.

## Stop conditions
- Do not treat active inference or causal-entropic-force papers as root ontology.
- Do not collapse viability into destiny.
- Do not call a basin stable without perturbation evidence.
- Do not call topology persistent without filtration/persistence evidence.

## Related pages
- [[systems-attractor-basin-research-queue-2026-05-18]]
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[perturbation-depth-basin-edge-table]]
- [[topology-carrier-tool-lane]]
- [[mmm-formal-noun-and-great-sentence-reservoir]]
