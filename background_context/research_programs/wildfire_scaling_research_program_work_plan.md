# Wildfire Scaling Research Program: Narrative Gantt and Work Plan

## Overview

This planning draft reframes the wildfire scaling project around a central proposal claim: wildfire perimeters are **scale-conditioned environmental interfaces** whose observed geometry depends both on how the interface is defined and on the scale at which it is measured. In this framing, perimeter geometry is not a cosmetic by-product of fire spread. It is a primary observable that encodes the coupled dynamics of fuel structure, transport, weather forcing, and landscape heterogeneity.

The project responds to three persistent weaknesses in wildfire science that are especially relevant to a competitive `FIRE-MODEL` proposal:

1. **Ambiguous geometric objects**. Fire perimeters differ across sensors and products, and cross-study comparisons often mix incompatible definitions.
2. **Fragile scaling claims**. Reported exponents may reflect measurement artifacts as much as physical mechanisms.
3. **Weak validation paradigms**. Many models are still judged by single end-state metrics rather than by whether they reproduce the observed multi-scale geometry of fire growth.

The resulting research program asks a more general question than whether wildfire perimeter growth follows one particular exponent:

> How do coupled transport and resource constraints generate scale-dependent interface geometry in environmental systems, and how can that geometry be used to infer and predict wildfire dynamics?

This framing aligns with the working `FIRE-MODEL` emphasis on conceptual innovation, computational implementation, and empirical validation. Here, the conceptual advance is a formal theory of wildfire boundaries as scale-conditioned interfaces; the computational advance is a generative modeling and analysis workflow centered on multi-scale interface geometry; and the validation advance is a geometry-based benchmarking framework for simulated and observed fires.

Two existing infrastructure elements make the program tractable:

- `FIRED`, for reconstructing wildfire events and daily progression from satellite observations
- `CubeDynamics`, for organizing spatiotemporal data cubes and supporting scalable geometry analysis

A planning assumption for this draft is that the new interface-geometry framing should be integrated into the existing multi-year project scaffold already under discussion in the repository. Team size, exact staffing mix, and project duration therefore remain provisional and should be synchronized later with budget strategy and the final solicitation interpretation.

Personnel currently assumed in the work plan are:

- Principal Investigator providing conceptual leadership, theory integration, and project synthesis
- Postdoctoral Researcher 1 focusing on data harmonization, interface extraction, and empirical geometry analysis
- Postdoctoral Researcher 2 focusing on generative modeling, mechanism mapping, and validation diagnostics
- Graduate student or equivalent research support assisting with data processing, experiments, and workflow integration

## Project timeline

| Task | Year 1 | Year 2 | Year 3 | Year 4 |
| --- | --- | --- | --- | --- |
| Multi-sensor perimeter harmonization and interface definitions | ███████ | ███ |  |  |
| Interface geometry dataset and `L_d(ε)` measurement workflows | ███████ | ███ |  |  |
| Cross-scale scaling diagnostics and equivalence tests | ███ | ███████ | ███ |  |
| WUI calibration and comparative interface analysis | ███ | ███████ |  |  |
| Generative interface modeling experiments |  | ███ | ███████ |  |
| Process-to-geometry regime mapping |  | ███ | ███████ |  |
| Fire-model geometric benchmarking |  |  | ███ | ███████ |
| `CubeDynamics` geometry toolkit and dashboards |  |  | ███ | ███████ |
| Synthesis, theory development, and proposal-ready integration |  |  |  | ███████ |

## Phase 1: Define the object and establish the measurement system (Year 1)

The first phase addresses the most basic but often under-specified issue in wildfire geometry studies: what boundary is actually being measured? Rather than assuming that a fire perimeter is a single stable object, the project will construct boundary ensembles across multiple datasets and extraction rules. Candidate sources include products derived from `MODIS`, `VIIRS`, `GOES`, and higher-resolution imagery where appropriate and feasible.

The key empirical object in this phase is the scale-conditioned boundary length function:

```text
L_d(ε)
```

where `d` denotes the boundary definition and `ε` denotes the measurement scale. This reframes boundary geometry from a single number to a function that can be compared across sensors, products, smoothing rules, and resolutions.

Work in this phase includes:

- harmonizing cross-sensor perimeter representations
- documenting how detection thresholds, temporal aggregation, and pixel connectivity alter boundary geometry
- implementing multi-scale perimeter measurement methods, including divider- and box-based approaches where appropriate
- organizing the resulting interface products inside `CubeDynamics` as reusable geometry cubes

A parallel calibration activity will use wildland-urban interface boundaries as a quasi-static comparison system. WUI boundaries provide a valuable test case because they can be generated under multiple definitions without the added complication of rapidly changing fire dynamics. This allows the team to separate issues of measurement and definition from issues of front propagation.

By the end of Phase 1, the project should deliver a formal definition workflow for wildfire boundary objects, a harmonized multi-scale perimeter dataset, and a documented analysis pipeline for computing `L_d(ε)` curves reproducibly.

## Phase 2: Identify scaling regimes and explain the form (Year 2)

Once the measurement framework is established, the second phase asks what kinds of scaling behavior the observed interfaces actually exhibit and what those behaviors imply about process.

The project will evaluate whether and when observed interfaces show approximate power-law behavior of the form:

```text
L(ε) ∝ ε^(1−D)
```

where `D` is an effective fractal dimension or roughness indicator. Rather than treating `D` as a universal constant, the analysis will test whether scaling behavior changes with sensor definition, fire regime, ecosystem setting, or stage of fire growth.

Empirical tasks in this phase include:

- estimating slopes, curvature, and stability ranges for `L_d(ε)` curves
- identifying regimes in which interfaces behave as smooth fronts versus rough or fractal boundaries
- testing whether different definitions become equivalent under scale transformation
- comparing geometry across environmental gradients and observation systems

This phase also develops the project's mechanistic interpretation. The team will build minimal coupled models that link interface form to candidate generative processes, including:

- diffusion-like spread
- heterogeneous fuel connectivity and percolation-like behavior
- anisotropic transport under wind or topographic forcing
- threshold-based ignition and resource-limited propagation
- occasional nonlocal spread processes such as spotting, where justified

The goal is not to recreate all wildfire complexity immediately. It is to determine which process combinations produce distinct geometric signatures and which conditions generate transitions between smoother and rougher interface regimes.

By the end of Phase 2, the project should have a defensible empirical characterization of scale dependence, a first map from process parameters to geometric signatures, and a clearer statement of which scaling claims are robust versus measurement-induced.

## Phase 3: Develop the Generative Interface Model and compare regimes (Year 3)

The third phase formalizes the central modeling contribution: a **Generative Interface Model (GIM)** for wildfire boundaries.

In this model class, the primary output is not only burned area or final perimeter overlap. The principal target is the evolving geometry of the interface itself. A generic state description includes:

- `V(x,t)`: fuel availability or resource field
- `F(x,t)`: fire state or combustion field
- `W(x,t)`: environmental forcing field

These fields interact through transport, energy transfer, threshold dynamics, and landscape heterogeneity to generate evolving interfaces whose geometric properties can be measured with the same `L_d(ε)` diagnostics used for observations.

Core tasks in this phase include:

- implementing and comparing minimal GIM variants
- calibrating synthetic interfaces against observed geometry curves rather than only final states
- mapping parameter changes to shifts in roughness, curvature, and effective fractal dimension
- evaluating whether distinct fire regimes produce distinct geometric signatures

This phase is where the proposal's theory and computation components become tightly coupled. The model experiments provide a way to test competing explanations for observed interface forms and to identify which mechanisms appear necessary to reproduce the empirical geometry.

## Phase 4: Validate wildfire models using geometry and synthesize the framework (Year 4)

The final phase shifts model evaluation from single-metric comparison toward functional geometric validation.

Observed and simulated fires will be compared using full multi-scale geometry curves and related diagnostics, including:

- `L_d(ε)` curve shape
- slope and intercept comparisons across scale ranges
- curvature and regime-break diagnostics
- sensitivity to subsampling and observational degradation
- stability of inferred exponents across datasets and model outputs

This framework can then be applied both to the project's own GIM variants and to external wildfire models where simulation outputs are available. The resulting benchmark asks a stronger question than whether a model reaches the correct final footprint: does it reproduce the observed geometry of wildfire interfaces across scales?

At the same time, the geometry diagnostics will be packaged into `CubeDynamics` and related workflows as reusable tools for:

- time-indexed geometry cubes
- streaming perimeter analysis
- model-observation comparison dashboards
- reproducible cross-sensor interface studies

The final synthesis will articulate a broader theory of wildfire and related environmental boundaries as members of a more general class of generative interfaces. This provides a conceptual bridge between wildfire perimeters, WUI edges, and other environmental boundaries shaped by coupled transport, growth, and resource constraints.

## Expected scientific outcomes

By the end of the project, the research team should have produced several proposal-relevant advances.

First, the project will provide a formal framework for defining and measuring wildfire perimeters as scale-conditioned interfaces rather than assuming a single invariant boundary object.

Second, it will generate harmonized multi-scale perimeter datasets and documented geometry workflows that support more defensible comparisons across sensors and studies.

Third, it will establish a mechanism-oriented interpretation of interface roughness and scaling behavior, clarifying when apparent scaling reflects process and when it reflects observation.

Fourth, it will introduce a validation framework in which wildfire models are evaluated against observed multi-scale geometry rather than only endpoint overlap or coarse summary statistics.

Finally, it will position wildfire science within a broader theory of generative environmental interfaces, giving the proposal a stronger conceptual identity that answers the `FIRE-MODEL` call for an explicit scientific and computational advance.
