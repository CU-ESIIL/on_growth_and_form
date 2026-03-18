# Scale-Conditioned Geometry of the Wildland-Urban Interface (WUI)

## Status and use in this repository

This note is a scientific framing document for proposal development. It is not a funder requirement document. Its purpose is to sharpen how the proposal talks about wildfire perimeters, WUI structure, and multi-scale validation in ways that are consistent with the FIRE-MODEL emphasis on conceptual advance, computational implementation, and empirical validation.

## Overview

The wildland-urban interface (WUI) is a critical spatial configuration where human settlements and flammable vegetation intersect. It is often characterized using derived quantities such as boundary length to assess wildfire exposure, planning risk, and policy outcomes. However, treating WUI boundary length as a single, intrinsic scalar obscures a fundamental geometric reality: **boundary length is inherently scale-dependent**.

This framework recasts WUI boundary length from a fixed quantity into a **scale-conditioned estimand**, making explicit how both analytical assumptions and measurement resolution shape the observed value. In doing so, it connects wildfire science with established ideas from fractal geometry, landscape ecology, and complex systems.

## The core problem

A seemingly simple question—*How long is the WUI boundary?*—does not have a unique answer. The length of an irregular boundary depends on two distinct choices:

1. **How the boundary is defined**: the analytical rules used to construct the object.
2. **How the boundary is measured**: the observation scale or geometric resolution used to estimate its length.

Recognizing this changes the scientific task. Instead of reporting one number, the analysis should characterize **how boundary length changes with scale**.

## Two independent sources of scale dependence

### 1. Definition scale: object construction

Definition scale refers to the assumptions used to construct the WUI boundary. Relevant choices can include:

- housing density thresholds
- vegetation classification rules
- adjacency criteria
- neighborhood radius
- representation of settlements, such as building points versus aggregated units

Different choices produce different boundary geometries. These are not necessarily errors. They are often **alternative, defensible model specifications**, and each specification defines a different boundary object.

### 2. Measurement scale: geometric resolution

Measurement scale refers to the resolution at which a fixed boundary is measured. As the ruler or sampling scale becomes finer, more local detail is resolved and the estimated boundary length typically increases.

This is the same basic logic as the coastline paradox and is what one should expect for irregular, fractal-like boundaries.

## From scalars to functions

To keep both kinds of scale dependence explicit, boundary length should be written as a function:

```text
L_d(ε)
```

where:

- `d` denotes the delineation or definition bundle that produced the boundary object
- `ε` denotes the measurement scale used to estimate its length

This reframing has several consequences:

- reported differences between studies may be expected outcomes of different delineation bundles or resolutions
- boundary length becomes an **estimand**, not a fixed geographic constant
- interpretation should focus on scaling curves and diagnostics rather than single summary values

## Scaling behavior and fractal geometry

Irregular boundaries often follow power-law relationships of the form:

```text
L(ε) ∝ ε^(1−D)
```

where `D` is an effective roughness or fractal dimension. In this view, boundary complexity persists across scales rather than disappearing at finer resolution.

This matters because geometry can carry information about process. Similar scaling behavior has been studied for:

- coastlines
- river networks
- vegetation patch boundaries
- wildfire perimeters

The WUI boundary can therefore be interpreted not only as a mapped line, but also as a spatial trace of coupled human and ecological dynamics.

## WUI as a generative anthropogenic-ecological interface

Rather than treating WUI boundaries as static cartographic artifacts, this framework interprets them as **emergent interfaces produced by interacting processes**. At minimum, those processes include:

1. **Settlement expansion**, often mediated by infrastructure networks and clustered development
2. **Vegetation mosaics**, shaped by ecological gradients, disturbance, and land management
3. **Wildfire dynamics**, which both respond to and reshape landscape structure over time

The resulting boundary is therefore a process signature, not merely a line on a map.

## Minimal dynamical interpretation

A compact way to formalize this idea is to work with coupled spatial fields such as:

- settlement density `S(x,t)`
- vegetation biomass or cover `V(x,t)`
- fire activity `F(x,t)`

The WUI boundary then emerges as the contour or interface where settlement and vegetation intersect under chosen thresholds. This provides a conceptual bridge to reaction-diffusion systems, percolation theory, and spatial ecology.

## Why this matters for analysis and decision support

Treating WUI boundary length as `L_d(ε)` resolves several recurring problems.

### Comparability

Differences in reported WUI boundary lengths often reflect different delineation assumptions or measurement scales rather than contradictory substantive findings.

### Transparency

Rigorous reporting requires the delineation bundle and the measurement protocol to be stated explicitly.

### Interpretation

Boundary geometry should be analyzed through scale-dependent curves, log-log diagnostics, and sensitivity analysis, not only through a single scalar.

### Dynamics

WUI boundaries change through time as settlement, vegetation, and disturbance co-evolve.

## Minimum reporting standard suggested by this framework

A scale-aware WUI analysis should, at minimum, report:

- the delineation specification `d`
- the measurement protocol and scale interval `ε`
- perimeter-by-scale curves
- log-log scaling diagnostics
- sensitivity analyses across alternative definitions

## Extension to the fire modeling proposal

This WUI framing is useful in the repository because it sharpens how wildfire perimeter scaling should be described in the proposal.

### A. Linking WUI scaling to fire perimeter scaling

WUI boundaries and wildfire perimeters are both irregular interfaces generated by interacting processes. The WUI is relatively slow-moving and shaped by settlement plus vegetation patterns, while fire perimeters are dynamic interfaces shaped by combustion, transport, weather, and fuels. Even so, both systems show:

- multi-scale geometric roughness
- sensitivity to observation resolution
- emergent structure from coupled processes

For proposal framing, this means observed fire scaling should be treated as a **scale-conditioned phenomenon** rather than as a single universal exponent to be asserted without qualification.

### B. Observational constraints as measurement scale

Satellite products such as MODIS, VIIRS, and GOES impose implicit measurement scales through:

- spatial resolution
- temporal resolution
- detection thresholds and masking rules

In this framework, these are not just nuisances; they are formal parts of `ε`, the measurement scale.

Operationally, that suggests:

- treating each dataset as a different sampling of `L(ε)`
- constructing perimeter-by-scale curves for each sensing regime
- testing whether inferred scaling exponents vary systematically with sampling structure

A defensible claim for the proposal is therefore:

> observed fire scaling relationships are functions of both physical dynamics and observational structure

### C. Definition scale in fire modeling

Fire perimeters also depend on definition choices, such as:

- burn severity thresholds
- active-fire detection criteria
- temporal aggregation windows
- interpolation or smoothing procedures

These choices define the boundary object itself. In proposal terms, model-data comparison should therefore align not only on physics, but also on boundary definition.

### D. Validation as curve matching rather than point matching

A key implication for FIRE-MODEL framing is that validation should move beyond single end-state metrics. The more informative comparison is functional and multi-scale:

1. compute `L_d(ε)` curves for observed fires
2. compute `L_d(ε)` curves for simulated fires
3. compare slope, intercept, and stability across scale ranges

Additional diagnostics can include:

- curvature distributions
- roughness statistics
- fractal-dimension estimates across scales
- sensitivity to temporal thinning or spatial subsampling

This turns validation into comparison of **functions across scales**, not only overlap at one chosen resolution.

### E. Generative interpretation of fire as interface dynamics

The same perspective also strengthens the proposal's theoretical positioning. Fire perimeter geometry can be interpreted as an emergent trace of:

- fuel structure and continuity
- weather forcing
- topographic constraints
- local spread and long-range spotting

That keeps the argument grounded in process while still using geometric observables as diagnostics.

### F. Minimal coupled-system interpretation for the proposal

The proposal can specialize the coupled-field idea toward fire-focused variables such as:

- `V(x,t)`: fuel availability and structure
- `F(x,t)`: fire state or intensity
- `W(x,t)`: weather forcing

A minimal system then takes the form of coupled growth, transport, ignition, consumption, and extinction terms. The value of this abstraction is not that it replaces operational fire models, but that it clarifies how measurable geometry can emerge from interacting physical and ecological processes.

### G. Testable hypotheses enabled by the framework

This scale-conditioned perspective supports hypotheses that are suitable for the proposal's validation agenda:

1. **Scale invariance hypothesis**: inferred exponents remain stable across sensors and resolutions over identifiable scale ranges.
2. **Sampling artifact hypothesis**: exponents vary systematically with temporal or spatial aggregation.
3. **Regime dependence hypothesis**: wind-driven and fuel-limited fires produce different scaling signatures.
4. **Process signature hypothesis**: changes in fuel continuity or meteorology alter curvature and roughness statistics.

These hypotheses translate an abstract geometric idea into a structured empirical program.

### H. Cyberinfrastructure implications

The framework also aligns with the repository's FIRED and CubeDynamics direction:

- represent perimeters as time-indexed geometries
- compute `L_d(ε)` over data cubes and trajectories
- expose scaling diagnostics as first-class analytical products

Potential outputs include multi-scale perimeter datasets, scaling dashboards, and cross-fire comparative libraries.

### I. Positioning relative to existing fire models

Traditional frameworks such as FARSITE- or WRF-Fire-style modeling emphasize forward simulation under prescribed conditions. The scale-conditioned interface perspective does not replace those approaches. Instead, it adds:

- scale-aware diagnostics
- geometry-based validation
- process inference from boundary structure

That additional layer is well aligned with the FIRE-MODEL expectation that projects articulate a conceptual advance, a computational implementation path, and an empirical validation strategy.

## Proposal takeaways

For proposal framing, the main takeaways are:

- fire and WUI boundaries can be treated as members of a shared class of scale-dependent interfaces
- observed scaling should be interpreted through `L_d(ε)`, not only through one reported exponent
- remote-sensing products and preprocessing pipelines define measurement and definition scales
- validation should compare scale-conditioned functions, not only single outputs
- boundary geometry provides a tractable window into coupled underlying dynamics

## Open issues to keep explicit

Several pieces still need explicit empirical support before they should be elevated from framing to proposal claim:

- which WUI or fire interfaces actually exhibit stable power-law scaling over meaningful scale ranges
- how sensitive estimated roughness dimensions are to preprocessing choices
- whether the same scaling language is equally informative across different fire regimes and sensor products

Those uncertainties should remain visible in proposal drafting so the narrative stays evidence-based and reviewable.
