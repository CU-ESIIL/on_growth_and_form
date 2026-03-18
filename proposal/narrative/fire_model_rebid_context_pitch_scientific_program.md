# FIRE-MODEL Proposal Rebid: Context, Pitch, and Scientific Program

## Status and purpose

This memo captures a proposal-strategy framing for the FIRE-MODEL rebid. It is an internal planning artifact intended to guide the next Project Description, summary language, aims structure, validation narrative, and cyberinfrastructure positioning.

This document is strategy rather than sponsor guidance. Final proposal language should still be checked against the current FIRE solicitation, NSF review criteria, and PAPPG requirements summarized in `funder/`.

## Proposal function

This strategy memo is intended to strengthen the proposal against several working FIRE-MODEL expectations reflected in the repository briefing and checklist:

- make the conceptual advance explicit;
- define a computational framework rather than only a motivating idea;
- specify a validation pathway grounded in observable wildfire behavior;
- show how cross-scale dynamics and interdisciplinary integration are central rather than decorative.

In proposal terms, this memo is mainly shaping:

- the Project Description opening argument;
- the articulation of Intellectual Merit;
- the logic connecting aims, methods, and validation;
- the explanation of why this team, infrastructure stack, and timing are well matched to the call.

## Core thesis

Environmental boundaries such as wildfire perimeters and wildland–urban interface edges are **scale-conditioned interfaces**. Their geometry is not a fixed property, but a function of both how the boundary is defined and how it is measured. These interfaces encode information about the dynamics of the systems that generate them.

The central strategic claim for the rebid is therefore:

> wildfire-interface geometry should be treated as a primary observable for understanding, comparing, and predicting fire dynamics, not merely as a byproduct of simulation or mapping.

This framing supports a proposal structure that combines theory, computational implementation, and empirical validation in a way that is legible to FIRE-MODEL reviewers.

## Problem statement

The strategy is motivated by three linked weaknesses in the current wildfire-modeling landscape.

### 1) Ambiguous geometric objects

Wildfire perimeters differ across sensing systems and processing pipelines, including MODIS, VIIRS, GOES, and higher-resolution imagery. Definitions also vary with thresholding, temporal aggregation, and burn-severity conventions. As a result, perimeter comparisons across studies can be inconsistent or misleading.

### 2) Fragile scaling claims

Reported scaling exponents vary widely across studies and datasets. Without a framework that separates physical structure from observational artifacts, it is difficult to know whether a claimed law reflects dynamics, sampling, or definition choices.

### 3) Weak validation paradigms

Wildfire models are often evaluated using a small number of endpoint metrics such as final-perimeter overlap. That leaves substantial multi-scale geometric information unused and weakens the connection between model outputs and the processes those outputs are supposed to represent.

## Scientific framing

The rebid can present these three issues as consequences of a deeper gap: the field lacks a formal theory of environmental interface geometry suitable for wildfire modeling and validation.

This helps answer several implicit NSF questions at once:

- **Why this work matters now:** expanding wildfire datasets and sensing systems make cross-sensor, cross-scale geometric analysis newly feasible;
- **Why this is a conceptual advance:** the proposal elevates interface geometry from descriptive output to central observable;
- **Why this team and infrastructure are positioned to do it:** the work connects theory, satellite-derived fire products, and computational systems such as `CubeDynamics` and `OASIS`.

## Conceptual framework

### Interfaces as primary observables

An environmental interface is treated here as a boundary separating interacting fields, such as burned and unburned fuel, and as a geometric object produced by coupled processes including transport, consumption, and growth.

### Scale conditioning

The geometry of an interface depends on two independent dimensions:

- **definition (`d`)**: how the boundary is constructed;
- **measurement scale (`ε`)**: the resolution at which it is measured.

The strategic formalism is to write boundary length as:

```text
L_d(ε)
```

where the observed length depends jointly on definition and measurement scale. This reframes geometry from a single number into a function.

### Scaling behavior

Irregular interfaces may exhibit power-law scaling of the form:

```text
L(ε) ∝ ε^(1−D)
```

where `D` is an effective fractal dimension. In the proposal, this relation should be treated as a measurable signature whose stability or instability itself becomes scientifically informative.

## Why WUI and fire belong in one program

### WUI as a calibration system

The wildland–urban interface provides a comparatively stable system in which boundary geometry can be computed across multiple definitions and scales without the same level of dynamical ambiguity present in active wildfire spread. That makes WUI geometry useful as a calibration and conceptual development system.

### Fire as a dynamic interface

Wildfire perimeters are dynamic interfaces driven by fuel structure, weather forcing, and topography. They are propagating fronts shaped by transport and threshold processes rather than static mapped lines.

### Shared structure

The rebid can therefore argue that WUI boundaries and wildfire perimeters belong to a broader class of **generative interfaces**:

- irregular and multi-scale;
- emergent from coupled processes;
- sensitive to both observation and definition.

This shared framing broadens the proposal's intellectual reach while keeping wildfire behavior central.

## Core scientific question

The proposed scientific question is:

> How do coupled transport and resource constraints generate scale-dependent interface geometry in environmental systems, and how can that geometry be used to infer and predict system dynamics?

This question is useful strategically because it links mechanism, data, and validation in one sentence.

## Research aims

### Aim 1 — Define the object

**Goal:** develop a formal, data-driven framework for scale-conditioned environmental interfaces.

**Questions addressed:**

- How do different definitions alter boundary geometry?
- How does measurement scale transform observed length?
- When are two boundaries equivalent under scale transformation?

**Approach:**

- construct boundary ensembles across MODIS, VIIRS, GOES, and higher-resolution products;
- compute `L_d(ε)` curves;
- harmonize cross-sensor representations.

**Proposal role:** this aim provides the empirical and mathematical foundation for later validation claims.

### Aim 2 — Explain the form

**Goal:** connect interface geometry to generative processes.

**Questions addressed:**

- What process combinations produce distinct scaling regimes?
- How do fuel, weather, and transport coupling appear in geometry?
- Under what conditions do interfaces become smooth, rough, or fractal?

**Approach:**

- develop minimal coupled models linking fuel, fire, and environment;
- explore reaction–diffusion and percolation analogs;
- simulate synthetic interfaces across parameter regimes.

**Proposal role:** this aim carries the conceptual and mechanistic Intellectual Merit.

### Aim 3 — Validate using geometry

**Goal:** establish multi-scale validation for wildfire models using interface geometry.

**Questions addressed:**

- Can models reproduce observed `L_d(ε)` curves?
- Are inferred scaling exponents stable across datasets and definitions?
- Do different model classes leave distinct geometric signatures?

**Approach:**

- compute geometry curves for observed and simulated fires;
- compare slopes, intercepts, curvature, and stability;
- develop diagnostics for roughness, fractal dimension, and sensitivity.

**Proposal role:** this aim responds directly to the need for a legible validation pathway in FIRE-MODEL proposals and to prior reviewer concerns about unclear evaluation.

## Generative Interface Model (GIM)

### Strategic role

The modeling centerpiece can be introduced as the **Generative Interface Model (GIM)**. The key pitch is not simply that it is another spread model, but that it is a model class explicitly constrained by multi-scale interface geometry.

### Core components

- state fields for fuel, fire state, and environmental forcing;
- transport processes such as advection and diffusion;
- energy release and transfer;
- threshold-based ignition and propagation;
- evolving interface geometry as a central model output.

### Why it is distinctive

In proposal framing, GIM is innovative because it:

- is constrained by geometry across scales rather than only endpoint fit;
- is calibrated against `L_d(ε)` curves and related diagnostics;
- provides an interpretable link between process parameters and geometric form.

## Working hypotheses

The strategy memo supports a hypothesis-driven structure built around four candidate hypotheses:

1. **Scale invariance hypothesis:** scaling exponents remain stable across datasets when definitions are harmonized.
2. **Sampling artifact hypothesis:** some apparent exponents are products of observation structure rather than intrinsic dynamics.
3. **Regime dependence hypothesis:** different fire regimes produce distinct scaling signatures.
4. **Process signature hypothesis:** interface geometry reflects underlying coupling mechanisms.

These hypotheses help keep the proposal falsifiable rather than declarative.

## Validation strategy

The proposal should explicitly state that validation shifts from pointwise or endpoint metrics to functional comparison of geometric observables. Core validation elements include:

- comparison of `L_d(ε)` curves;
- evaluation of exponent stability;
- curvature and roughness diagnostics;
- sensitivity to subsampling and sensor definition;
- comparison of observed and simulated geometric signatures.

This framing should be connected directly to reviewer concerns about weak validation paradigms and to FIRE-MODEL expectations for empirical grounding.

## Cyberinfrastructure integration

The strategic cyberinfrastructure narrative is that the geometry framework is not a standalone theory note. It is intended to integrate with the repository's data-systems vision through:

- time-indexed geometry cubes;
- streaming perimeter analysis;
- scaling dashboards;
- open and reproducible workflows using `CubeDynamics` and `OASIS`.

This supports the call's apparent interest in computational systems, data integration, and scalable analytical infrastructure.

## Broader impacts positioning

Broader impacts can be framed around:

- improved wildfire risk assessment through more informative geometric diagnostics;
- better model-evaluation tools for the research and management communities;
- a transferable framework for environmental boundaries beyond wildfire alone;
- open-source data products and analytical tooling.

These broader impacts will still need a concrete implementation and evaluation plan in the actual proposal package.

## Team and timeline framing

The document supports a three-person scientific structure centered on:

- PI leadership for theory, integration, and modeling;
- Postdoctoral Researcher 1 for data and geometry systems;
- Postdoctoral Researcher 2 for modeling and validation.

A simple timeline logic is:

- **Year 1:** interface definition and dataset construction;
- **Year 2:** generative modeling and process experiments;
- **Year 3:** validation, synthesis, and integration.

If this staffing model is retained, the final proposal should still include contingency language so the work does not appear to hinge unrealistically on immediate hiring success.

## Strategic takeaways for the rebid

The proposal pitch should make the following points legible and repetitive:

- fire perimeters are scale-conditioned interfaces;
- geometry is a diagnostic of dynamics rather than just a descriptive outcome;
- scaling should be treated as a function of definition and measurement, not a single constant;
- model validation should occur across scales;
- the proposal advances wildfire modeling by linking generative theory, computational implementation, and empirical validation.

## Assumptions and follow-up needs

- This memo is a strategy synthesis based on the user-provided framing and the repository's existing FIRE-MODEL context documents; it is not derived from newly verified NSF wording.
- Before this language is moved into sponsor-facing proposal prose, the framing should be checked against the official FIRE solicitation and any page or section constraints that apply to the next submission.
- If the rebid adopts the `Generative Interface Model` name, the proposal should define how that name relates to existing repository terms such as wildfire scaling, generative models, and `CubeDynamics` so the narrative remains internally consistent.
