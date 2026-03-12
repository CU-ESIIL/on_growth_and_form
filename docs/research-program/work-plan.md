# Wildfire Scaling Research Program: Narrative Gantt and Work Plan

## Overview

This project investigates whether wildfire growth follows reproducible geometric scaling laws and, if so, what mechanisms generate them. Recent satellite observations suggest that wildfire perimeters may grow according to non-diffusive scaling relationships, potentially following:

```text
P(t) ~ t^(2/3)
```

with an associated fractal boundary dimension near:

```text
D ~ 4/3
```

If this pattern is real, it implies that wildfire spread may behave as a rough propagating interface moving through heterogeneous landscapes rather than as a purely diffusive or purely deterministic front. However, the existence, timing, and mechanism of this scaling regime remain open scientific questions.

This research program is designed to answer those questions through a coordinated combination of empirical analysis, mechanistic modeling, and model evaluation. The project leverages two key pieces of existing infrastructure:

- `FIRED`, a dataset and algorithm for reconstructing wildfire events and daily progression from satellite observations
- `CubeDynamics`, a computational framework that treats environmental data as spatiotemporal cubes and provides scalable analysis tools

Together, these resources allow the research team to reconstruct the geometry and dynamics of many fires and analyze them using consistent methods.

Personnel involved include:

- Principal Investigator (50% effort) providing conceptual leadership and synthesis
- Postdoctoral Researcher 1 focusing on empirical scaling measurement and satellite analysis
- Postdoctoral Researcher 2 developing generative models and theoretical interpretation
- Graduate student assisting with data processing, model experiments, and integration

## Project timeline

| Task | Year 1 | Year 2 | Year 3 | Year 4 |
| --- | --- | --- | --- | --- |
| Data integration and perimeter reconstruction | ███████ |  |  |  |
| Fire growth trajectory dataset | ███████ | ███ |  |  |
| Scaling measurement tools | ███ | ███████ |  |  |
| Scaling regime detection |  | ███████ |  |  |
| Environmental regime analysis |  | ███████ | ███ |  |
| Generative modeling experiments |  | ███ | ███████ |  |
| Mechanism comparison |  |  | ███████ |  |
| Fire model evaluation |  |  | ███ | ███████ |
| CubeDynamics scaling toolkit |  |  | ███ | ███████ |
| Synthesis and theory development |  |  |  | ███████ |

## Phase 1: Establishing the measurement system (Year 1)

The first phase focuses on establishing a robust empirical foundation for wildfire scaling analysis. Although large volumes of satellite fire data exist, they are rarely organized into consistent trajectories describing how individual fires grow through time. The primary objective of this phase is therefore to construct a standardized dataset of wildfire growth trajectories that can support large-scale geometric analysis.

The team will integrate `FIRED` fire progression data into the `CubeDynamics` framework. Using these tools, researchers will reconstruct daily perimeter evolution for many fires across multiple regions and ecosystems. Each fire will be represented as a time series describing key geometric properties including perimeter length, burned area, and shape metrics.

A significant portion of the work during this phase involves establishing reliable measurement methods. Satellite-derived fire perimeters are sensitive to spatial resolution, pixel connectivity rules, and smoothing procedures. To ensure that geometric measurements are scientifically meaningful, the team will develop standardized perimeter extraction and smoothing algorithms and evaluate how measurement resolution influences estimates of perimeter length and fractal dimension.

At the same time, the team will implement several complementary estimators of wildfire geometry, including perimeter-area scaling relationships and fractal dimension estimators such as box-counting and divider methods. These tools will allow the researchers to quantify how complex wildfire boundaries become as fires grow.

By the end of the first year, the project will produce a dataset of wildfire growth trajectories derived from satellite observations. This dataset will include perimeter and area time series for many fires and will be made available through `CubeDynamics` as a reusable research resource.

## Phase 2: Identifying the scaling regime (Year 2)

With the empirical dataset established, the second phase addresses the central question of whether wildfire perimeter growth exhibits a reproducible scaling regime.

For each fire trajectory, researchers will analyze the relationship between perimeter and time using log-log scaling diagnostics. Instead of assuming that a single exponent applies throughout the entire lifetime of a fire, the analysis will search for intervals in which power-law relationships appear stable. These intervals may represent the expansion phase of wildfire growth, during which the fire front behaves as a statistically rough interface spanning many fuel patches.

The team will apply segmented regression and breakpoint detection techniques to identify transitions between different growth regimes. These analyses will help determine whether wildfire growth can be described by a three-phase lifecycle consisting of ignition, expansion, and termination phases.

An especially powerful diagnostic used in this phase will be scaling collapse. In this approach, individual fire trajectories are normalized by characteristic time and perimeter scales so that fires of different durations and sizes can be compared directly. If fires share a common underlying growth process, their normalized trajectories should collapse onto a common curve during the expansion phase.

In addition to identifying the scaling regime, researchers will examine how scaling behavior varies across environmental gradients. Fires will be stratified by ecosystem type, climate regime, and wind conditions to determine whether the exponent is universal or varies systematically with environmental forcing.

By the end of this phase, the project will produce a large-scale empirical characterization of wildfire perimeter growth scaling.

## Phase 3: Mechanistic modeling experiments (Year 3)

Once empirical scaling patterns are established, the next phase investigates what physical processes produce those patterns. Rather than attempting to replicate the full complexity of wildfire behavior, this phase focuses on developing simplified generative models that isolate key mechanisms of fire spread.

Researchers will construct a series of minimal models representing different classes of processes. These models will include diffusion-like spread, spread through heterogeneous fuel networks similar to percolation systems, anisotropic spread driven by wind, and models incorporating occasional long-distance ignition events representing spotting.

Each model will generate synthetic fire growth trajectories that can be analyzed using the same geometric diagnostics applied to satellite data. By comparing the scaling exponents and boundary dimensions produced by each model with those observed in real fires, the researchers can determine which mechanisms are capable of producing the observed geometric patterns.

This comparative modeling approach allows the project to move beyond empirical description toward mechanistic explanation.

## Phase 4: Evaluating fire models and synthesizing theory (Year 4)

The final phase connects the findings back to the broader wildfire modeling community. Operational wildfire simulators are widely used to predict fire spread under different weather and fuel conditions, but they are rarely evaluated based on the emergent geometric properties of the fires they produce.

In this phase, the research team will analyze fire perimeters generated by existing wildfire models and apply the same scaling diagnostics used in earlier phases. This comparison will determine whether current fire models reproduce the same perimeter growth exponents and boundary roughness observed in satellite data.

If discrepancies are found, the results will highlight which physical processes may be missing or simplified in current models. Conversely, if models reproduce the observed scaling behavior, this provides validation for their underlying spread mechanisms.

At the same time, the scaling diagnostics developed throughout the project will be integrated into `CubeDynamics` as a reusable module. This will allow researchers and fire modelers to evaluate the geometric realism of future simulations using the same analytical tools developed during the project.

The final year will also focus on synthesizing the empirical and modeling results into a coherent theoretical framework describing how local fire spread processes generate large-scale wildfire geometry.

## Expected scientific outcomes

By the end of the project, the research team will have produced several major advances in wildfire science.

First, the project will provide a systematic measurement of wildfire perimeter growth scaling across many fires using satellite observations.

Second, it will determine when during the fire lifetime scaling appears, addressing a major conceptual uncertainty about wildfire dynamics.

Third, the modeling experiments will identify which mechanisms are capable of generating the observed geometric patterns, connecting wildfire science with broader theories of interface growth and landscape connectivity.

Finally, the project will introduce a new scaling-based diagnostic framework for wildfire models, enabling researchers to evaluate whether simulations reproduce the emergent geometry of real fires.

Together, these advances help bridge a longstanding gap in wildfire science: understanding how local spread processes produce the large-scale spatial geometry of wildfire growth across landscapes.
