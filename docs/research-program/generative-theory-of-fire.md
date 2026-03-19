# On Growth and Form: A Generative Theory of Fire

## Role in the FIRE-MODEL website narrative

This page captures a long-form draft for the research-program section of the proposal website. It is intended to make the project's conceptual advance, model hierarchy, technical architecture, benchmarking logic, and year-by-year execution plan legible in one place.

In terms of the repository's current working `FIRE-MODEL` framing, this document is primarily serving four proposal functions:

- clarifying the conceptual advance,
- showing the computational framework as a hierarchy rather than a monolith,
- specifying how geometry and benchmarks support validation, and
- making the work plan auditable across aims, milestones, and success criteria.

This remains draft planning prose rather than sponsor-controlled guidance. Final proposal language should still be checked against the `funder/` materials and NSF requirements before submission use.

## Overview

In natural systems, form is not an ornament added after the fact. Form is the visible record of process. The branching of a tree, the contour of a shell, the shape of a river network, and the organization of turbulent flow all arise because matter, energy, and constraint interact through time to produce lawful structure. Fire, too, is a process of growth. It advances through space, selects pathways through heterogeneous material, responds to external forcing, and produces boundaries whose geometry records the history of propagation. Yet wildfire science has rarely treated fire primarily as a problem of growth and form. Instead, most existing approaches begin from the imperative to simulate or forecast fire behavior under specified conditions. Those approaches have yielded major practical advances, but they do not directly answer a deeper scientific question: **what are the minimal governing principles that cause fire to take the shapes it does?**

This project proposes that wildfire should be understood as a **growth process on a structured substrate**, and that its observed forms can be explained, compared, and predicted through a hierarchy of minimal generative models. Our objective is not to replace operational fire models, but to provide the theoretical backbone they currently lack: a framework that identifies the smallest set of controls needed to generate realistic fire form, derives falsifiable predictions from those controls, and evaluates those predictions against observations using a unified set of metrics.

The resulting system is a **landscape-to-fire-form engine**. It takes as input a structured landscape—fuels, topography, moisture, wind, and ignition—and produces as output not only fire spread and perimeter evolution, but also a set of measurable geometric, dynamical, and threshold signatures: ignition-time fields, front organization, spanning transitions, perimeter scaling, elongation, connectivity, and the conditions under which added model complexity becomes scientifically necessary. In this way, the project links theory, computation, observation, and benchmarking into a single machine for discovering the governing rules of fire behavior.

## The Scientific Need

Existing wildfire models span a wide continuum, from empirical and quasi-empirical spread models to sophisticated coupled fire–atmosphere systems. These models can be highly effective for scenario analysis and, in some contexts, forecasting. However, they share several limitations that motivate the present work.

First, they are typically built for **forward prediction**, not for **mechanistic reduction**. They can reproduce or approximate behavior, but they do not isolate the minimal variables and interactions required to explain why specific geometries, thresholds, or regimes emerge.

Second, they often **entangle mechanisms**. Fuel effects, topographic effects, atmospheric forcing, and model structure are combined within a single simulation architecture, making it difficult to determine which factors are truly necessary for explaining the observed organization of spread.

Third, they are rarely designed around **falsifiable geometric predictions**. Fire perimeter is usually treated as an output to compare against observations, not as a primary carrier of mechanistic information. Questions of scale-dependent boundary structure, phase transitions in connectivity, and regime shifts in form are therefore underdeveloped.

Fourth, the field lacks a general framework for determining **when complexity is warranted**. Additional model detail is often assumed to improve realism, but the marginal gain of that complexity is seldom quantified systematically across regimes, scales, and observables.

This proposal addresses those gaps directly. It asks not simply whether a model can simulate fire, but whether a hierarchy of minimal models can recover the canonical behaviors, geometric regularities, and observed thresholds of wildfire growth, and can reveal the specific conditions under which richer coupling is essential.

## Central Hypothesis

We hypothesize that wildfire can be represented as an **anisotropic growth front propagating through a heterogeneous medium**, and that three classes of controls are sufficient to explain a large fraction of observed fire form:

1. **Material structure of the substrate**: fuel continuity, load, composition, and moisture determine where fire can move and with what resistance.
2. **External directional forcing**: wind, slope, and environmental gradients bias propagation and impart directionality to growth.
3. **Organization and coupling of the advancing front**: local interactions among portions of the front generate coherent large-scale structure, including elongation, front focusing, curvature effects, and threshold transitions.

From these ingredients, we expect the system to exhibit three testable properties:

- **Threshold behavior**: abrupt transitions from patchy, self-limiting spread to connected, spanning fires as effective connectivity or coupling exceeds critical values.
- **Scale-dependent geometry**: perimeter length, complexity, and roughness vary systematically with measurement scale, resolution, and growth regime.
- **Hierarchy-sensitive explanation**: increasingly structured models (fuel-only, anisotropic, coupled) explain progressively more of the observed morphology, but only in the regimes where their added mechanisms are required.

The scientific purpose of the project is to formalize these expectations, build the computational and analytical machinery required to test them, and determine the degree to which they organize real wildfire behavior.

## Conceptual Advance

The conceptual advance of the project is a shift from **simulation-first fire modeling** to **theory-first generative fire modeling**.

Rather than beginning with the most detailed model feasible, we begin with the most reduced model plausible. We ask what the simplest system is that can generate fire-like growth. We then add complexity only in modular, testable increments. This allows the scientific contribution of each mechanism to be identified explicitly.

The project is therefore organized as a **model hierarchy** rather than a single model:

- **M0**: isotropic, fuel-controlled growth in a passive medium
- **M1**: M0 plus directional anisotropy from wind and slope
- **M2**: M1 plus coupling terms that organize the advancing front
- **M3**: M2 plus extended dynamics, including time-varying forcing and additional surrogate processes where justified

This model ladder is not a convenience. It is the core scientific instrument of the proposal. By comparing models across the hierarchy with common data, common observables, and common evaluation metrics, we can determine:

- what mechanisms are sufficient to recover canonical fire behavior,
- what mechanisms are needed to explain observed geometry,
- what mechanisms improve predictive skill on real cases,
- and where further complexity ceases to yield proportional scientific value.

In this sense, the proposal is designed not merely to produce a model, but to **change how fire models are justified, compared, and improved**.

## Mathematical Formulation: The Growth Law

We represent wildfire as a propagating surface in time through the **ignition-time field** `T(x, y)`, where each location is assigned the time at which it ignites. This representation has several advantages. It unifies front position, spread rate, and progression history within a single object; it provides direct access to arrival-time gradients and evolving perimeter geometry; and it supports both synthetic and observation-based comparisons.

The local normal propagation speed is defined as:

```text
V(x, y, θ, t) = V₀ · g(F, M, C_f) · a(W, S, θ) · c(κ, ∇T, ∇z, N)
```

where:

- `V₀` is a baseline propagation coefficient,
- `g(F, M, C_f)` encodes substrate properties including fuel continuity `F`, moisture or dryness `M`, and optional categorical fuel-class controls `C_f`,
- `a(W, S, θ)` encodes directional anisotropy imposed by wind `W`, slope `S`, and orientation `θ`, and
- `c(κ, ∇T, ∇z, N)` is a coupling term that allows propagation to depend on front curvature `κ`, alignment of neighboring front segments, local terrain gradients, and neighborhood structure `N`.

The ignition-time field satisfies an anisotropic eikonal-type relation of the form:

```text
|∇T(x, y)| = 1 / V(x, y, θ, t)
```

or its discrete equivalent under the chosen front-propagation solver. This mathematical form is intentionally minimal. It does not attempt to resolve combustion chemistry or full atmospheric dynamics. Instead, it provides the simplest mathematically coherent description of a growth front moving through a structured landscape under directional forcing and local organization.

### Dimensionless Groups and Regime Space

A central aim of the project is to reduce the apparent complexity of fire behavior to a small number of dimensionless controls. The exact form of these quantities will be refined during Year 1, but the targeted regime-space variables are:

- `Π₁`: **Connectivity number** — a measure of fuel continuity or percolation potential across the landscape,
- `Π₂`: **Aridity/resistance number** — an effective dryness or moisture constraint on propagation,
- `Π₃`: **Forcing anisotropy number** — the strength of directional forcing due to wind and slope,
- `Π₄`: **Coupling number** — the magnitude of front organization and local interaction,
- `Π₅`: **Heterogeneity scale ratio** — the characteristic patch scale of landscape heterogeneity relative to grid scale or front width.

These variables define the **regime of growth**. The proposal’s core mathematical strategy is to map behavior in this reduced regime space, identify thresholds and transitions, and test whether observed fires occupy predictable portions of that space.

## The Machine: Technical Architecture and Its Parts

The project is built as a scientific machine whose parts are designed to work together over time. Each part has a specific function, produces a concrete output, and enables later components. The importance of each part lies not only in its standalone value, but in how it conditions the success of the entire system.

### Part I. The Intake Layer: Preparing the Substrate for Growth

The first requirement is a robust data-intake system that converts real landscapes into a common representation usable by every model in the hierarchy. This layer harmonizes:

- fuel and land-cover rasters,
- fuel continuity and load proxies,
- digital elevation models and derivatives (slope, aspect, curvature as needed),
- moisture proxies or environmental resistance fields,
- wind fields, whether static or time-varying,
- ignition locations or ignition geometries,
- observed perimeters and progression products for evaluation.

This layer will enforce a **case object standard**, in which every fire case is stored with aligned spatial grids, explicit metadata, temporal definitions, and the observational products needed for benchmarking. The case object is essential because it prevents the project from devolving into one-off scripts and ensures that synthetic experiments and real-case analyses are evaluated in the same computational grammar.

**Primary modules:**

- `io_cases.py`: ingestion, reprojection, clipping, tiling, metadata handling
- `landscape.py`: construction of analysis-ready landscapes from raw inputs
- `environment.py`: preparation of slope/aspect, wind alignment fields, and derived forcing layers

**Why it matters:** without a common substrate representation, no higher-level comparison across models, fires, or scales is scientifically meaningful.

### Part II. The Generative Engine: Producing Fire Growth

The engine is the computational realization of the growth law. It takes a prepared landscape and computes how fire advances across it under the model hierarchy `M0–M3`. The engine produces:

- ignition-time fields `T(x, y)`,
- evolving perimeters through time,
- spatial gradients of arrival time,
- derived proxies of local spread organization.

This engine will be designed for **high-throughput experimentation**, allowing thousands of simulations across controlled parameter space. That throughput is essential for detecting thresholds, estimating exponents, and mapping regime behavior with statistical confidence.

**Primary modules:**

- `spread_core.py`: implementation of local propagation laws for `M0–M3`
- `front_tracking.py`: discrete front propagation solver (fast marching, level-set, graph-based minimum-time methods, or equivalent)
- `simulate.py`: orchestration of time stepping, outputs, and run control

**Why it matters:** this is the first place where theory becomes operational. If the engine cannot generate the expected family of forms under synthetic conditions, then the proposal’s core hypothesis fails at the most basic level.

### Part III. The Coupling and Transmission Layer: Organizing Growth

A spread engine alone can produce movement; it does not necessarily produce organized form. The transmission layer encodes the processes by which local interactions and directional bias produce coherent macroscopic structure. This includes:

- wind-aligned elongation,
- upslope acceleration,
- sensitivity to neighborhood connectivity,
- curvature modulation,
- local front focusing or diffusion,
- surrogate representations of dynamical organization that go beyond fuel-only control.

This layer enters the model explicitly in `M1–M3`. Its scientific role is to test whether geometry and threshold behavior are explained sufficiently by substrate structure and directional forcing, or whether additional front organization must be invoked.

**Primary modules:**

- `anisotropy.py`: wind and slope directional terms
- `coupling.py`: front-neighborhood interaction, curvature feedback, alignment effects

**Why it matters:** this is the part most likely to distinguish the framework from existing reduced fire models. It is where the proposal tests whether form is simply inherited from landscape structure or actively organized by the growth front itself.

### Part IV. The Measurement Layer: Quantifying Form

A model of growth is only useful if it yields measurable structure. The measurement layer extracts the observables through which theory and data will be compared. These include:

- final burned area,
- perimeter length,
- perimeter length as a function of ruler size or resolution,
- perimeter–area scaling,
- elongation and major-axis orientation,
- connected-component statistics,
- spanning probability,
- arrival-time gradients and progression structure,
- boundary roughness and curvature distributions.

This layer is also where the proposal’s WUI and fractal ideas become central. Boundary structure is not treated as a cosmetic output; it is treated as a signal of process.

**Primary modules:**

- `observables.py`: geometric and dynamical summaries
- `scaling.py`: box-counting, ruler-length estimators, scaling-law fitting
- `morphology.py`: elongation, convexity, roughness, orientation, connectivity metrics

**Why it matters:** without a systematic measurement system, the project could only claim visual resemblance. This layer makes it possible to test law-like relationships.

### Part V. The Experiment Layer: Exploring Regime Space

The experiment layer turns the machine from a simulator into a scientific instrument. It controls the knobs of the system and maps how behavior changes as those knobs vary. The controlled quantities include:

- fuel continuity,
- moisture/dryness,
- wind strength and direction,
- slope,
- heterogeneity scale,
- coupling strength,
- barrier configuration,
- WUI structural arrangement,
- ignition geometry.

Using designed sweeps and ensembles, this layer will identify:

- critical thresholds in spanning behavior,
- geometry transitions across regime space,
- sensitivity of exponents to forcing and heterogeneity,
- regions where coupled models outperform simpler alternatives.

**Primary modules:**

- `experiments.py`: parameter sweeps, Latin hypercube or factorial designs
- `ensemble.py`: distributed or batched simulation management
- `phase_diagrams.py`: visualization and estimation of regime boundaries

**Why it matters:** this layer is where falsifiable predictions are born. It translates a model into a map of what the theory expects under specified conditions.

### Part VI. The Calibration and Inference Layer: Bringing Theory into Contact with Observation

Once synthetic behavior is established, the framework must confront real data. The calibration layer estimates parameter values, compares nested models, and determines whether coupling or anisotropy provides measurable explanatory gain. This layer will support:

- parameter sweeps for pilot fitting,
- likelihood-free or simulation-based inference where appropriate,
- uncertainty quantification for thresholds and exponents,
- ablation studies across `M0–M3`,
- cross-case validation across distinct fire events and landscape classes.

**Primary modules:**

- `calibration.py`: parameter estimation workflows
- `model_compare.py`: nested model comparison and information metrics
- `uncertainty.py`: bootstrap, ensemble, and sensitivity analysis tools

**Why it matters:** this is the honesty layer of the machine. It prevents elegant theory from escaping empirical test and determines whether added complexity is scientifically justified.

### Part VII. The Benchmark Layer: Determining Success

The project will be judged through a three-tier benchmark system, each tier tied to concrete outputs and reviewable milestones.

#### Benchmark Tier 1. Mechanism Recovery

The minimal engine must reproduce canonical behaviors under synthetic conditions:

- approximately isotropic expansion in homogeneous no-wind flat terrain,
- monotonic elongation with increasing directional forcing,
- upslope acceleration relative to downslope spread,
- suppression, deflection, or fragmentation under barriers and heterogeneity,
- increasing spanning probability as connectivity rises.

This benchmark determines whether the machine has the correct dynamical vocabulary.

#### Benchmark Tier 2. Pattern Recovery

The framework must reproduce realistic families of observed geometric and statistical patterns:

- perimeter–area scaling,
- regime-dependent complexity across ruler sizes,
- elongation and orientation distributions,
- cluster and spanning statistics,
- progression-map organization where available.

This benchmark determines whether the machine captures the observed forms of fire.

#### Benchmark Tier 3. Predictive Skill

The more structured models in the hierarchy must deliver measurable improvement over simpler baselines on real cases using shared metrics such as:

- overlap / IoU of final burn extent,
- boundary distance (Hausdorff, mean nearest-boundary distance, or related metrics),
- orientation and centroid error,
- arrival-time RMSE where progression products exist,
- spread-direction error,
- mismatch in exponent or regime-space statistics.

This benchmark determines whether the machine is not only explanatory but useful.

**Primary modules:**

- `benchmarks.py`: benchmark definitions and reporting
- `metrics.py`: shared metric calculations for synthetic and observed cases
- `reports.py`: standardized outputs, tables, figures, and comparison summaries

**Why it matters:** reviewers need to see exactly how success will be judged. This layer makes the proposal legible as a disciplined scientific program rather than an open-ended modeling effort.

## Specific Aims and Their Interactions Over Time

### Aim 1. Formalize the growth law and build the minimal engine

We will define the mathematical structure of the ignition-time formulation, implement `M0` and `M1`, and establish the case-object and landscape-intake standard. This aim produces the substrate and engine on which every later task depends.

**Outputs:**

- formal notation and mathematical specification,
- initial dimensionless groups,
- intake/case architecture,
- `M0–M1` solver,
- regression and mechanism-recovery tests.

**Why it matters:** this aim establishes that the project has a coherent mathematical core and a working minimal machine.

### Aim 2. Build the scaling and measurement apparatus

We will implement observables for perimeter, area, complexity, spanning, elongation, and progression; develop scaling estimators; and use synthetic experiments to map threshold and geometry regimes in reduced parameter space.

**Outputs:**

- robust measurement library,
- synthetic experiment suite,
- initial phase diagrams,
- preliminary estimates of critical thresholds and geometric exponents.

**Why it matters:** this aim turns simulation output into testable structure, making it possible to claim more than visual resemblance.

### Aim 3. Add coupling and quantify its contribution

We will implement `M2` and optional `M3` components, focusing on explicit front-organization terms and the conditions under which they improve explanatory power. This aim is where the proposal’s central distinction from reduced fuel-only models is tested directly.

**Outputs:**

- coupling module,
- ablation comparisons across `M0–M2`,
- regime maps showing when coupling matters,
- uncertainty estimates on coupling-related gains.

**Why it matters:** this aim determines whether organized front dynamics are required to explain fire form.

### Aim 4. Benchmark against real landscapes and observed fires

We will package pilot fire cases into the common case-object standard, calibrate models, and compare performance across the hierarchy using the shared benchmark suite.

**Outputs:**

- real-case dataset package,
- calibrated model runs,
- benchmark reports across mechanism, pattern, and predictive tiers,
- cross-case synthesis of where the hierarchy succeeds or fails.

**Why it matters:** this aim determines whether the framework changes fire modeling in practice, not just in concept.

These aims are intentionally interlocking. Aim 1 creates the engine. Aim 2 creates the measurement tools. Aim 3 tests the necessity of richer organization. Aim 4 evaluates the machine against the world. The full system emerges by building these pieces in sequence, each one increasing the interpretability, testability, and practical value of the framework.

## Year-by-Year Work Plan

### Year 1: Build the frame, intake, and minimal engine

Year 1 is devoted to mathematical formalization, data architecture, and the first operational version of the machine.

**Tasks:**

- finalize notation and mathematical specification of the ignition-time formulation,
- derive initial non-dimensionalization and regime variables,
- implement aligned case-object and landscape-preparation pipeline,
- implement `M0` and `M1` in the spread engine,
- establish scientific regression tests for canonical behaviors,
- run first synthetic experiments across connectivity and anisotropy gradients.

**Milestones:**

- working `M0–M1` engine,
- successful mechanism-recovery benchmark,
- reproducible synthetic experiment suite,
- first regime-space diagrams.

**Benchmark gate:** `SC1` is achieved if the engine reproduces canonical behaviors and exhibits an identifiable connectivity transition under controlled sweeps.

### Year 2: Build the scaling engine and add coupling

Year 2 is devoted to turning the machine into a true theory-testing system.

**Tasks:**

- implement measurement library for perimeter scaling, elongation, connectivity, and progression structure,
- estimate threshold locations and scaling exponents from ensembles,
- implement `M2` coupling terms and optional pilot `M3` extensions,
- perform ablation studies across `M0–M2`,
- ingest pilot real-world fire cases into the case-object standard,
- begin calibration and uncertainty analysis on selected cases.

**Milestones:**

- stable scaling-analysis workflow,
- estimated exponents and critical thresholds with uncertainty,
- initial evidence for or against coupling-related gains,
- first pattern-recovery benchmark reports.

**Benchmark gate:** `SC2` is achieved if the framework produces stable regime-dependent geometric statistics and demonstrates measurable shifts in form across reduced parameter space.

### Year 3: Full benchmarking, synthesis, and demonstration of value

Year 3 is devoted to comprehensive testing, real-case comparison, and synthesis into a new modeling paradigm.

**Tasks:**

- complete cross-case benchmarking across the model hierarchy,
- evaluate predictive skill relative to simple baselines,
- generate scenario experiments relevant to landscape structure and management,
- synthesize where complexity improves explanation and where it does not,
- package software, benchmark datasets, and reporting tools for re-use.

**Milestones:**

- benchmark suite complete,
- comparative model-hierarchy evaluation complete,
- scenario analyses demonstrating practical relevance,
- final synthesis manuscript and methodological framework.

**Benchmark gate:** `SC3` is achieved if `M2` or higher models show statistically credible gains over `M0/M1` on real-case benchmarks and if the hierarchy identifies where that added complexity is necessary.

## Concrete Success Criteria

The proposal will be considered successful if it meets the following explicit criteria:

### SC1. Functional success of the minimal machine

- `M0–M1` reproduce canonical spread behaviors under synthetic control conditions.
- The intake system and case-object standard allow reproducible synthetic and real-case runs.
- Threshold-like behavior emerges in connectivity sweeps.

### SC2. Scientific success of the scaling program

- Perimeter and morphology metrics are stable across repeated estimation.
- Threshold locations and scaling exponents can be estimated with uncertainty.
- Distinct form regimes can be mapped in reduced parameter space.

### SC3. Explanatory success of the coupling program

- Coupling terms improve at least one of geometry, threshold explanation, or predictive metrics in a regime-specific way.
- The hierarchy identifies where anisotropy alone is sufficient and where richer organization is needed.

### SC4. Practical success of the benchmark program

- A shared benchmark suite exists for synthetic and observed fires.
- Model comparison is performed using common metrics rather than ad hoc case studies.
- The framework yields reusable software and benchmark protocols that others can adopt.

These criteria ensure that the proposal is judged not by aspiration, but by concrete scientific and technical accomplishment.

## Why Each Piece Matters to the Whole

A proposal of this kind succeeds only if reviewers can see why the individual parts are necessary and how they accumulate into something transformative.

- The **intake layer** matters because a theory of fire cannot be tested without a consistent representation of the landscapes on which fire grows.
- The **engine** matters because theory must be made operational before it can be falsified.
- The **coupling layer** matters because it is the decisive test of whether fire form is merely inherited from substrate structure or actively organized by front dynamics.
- The **measurement layer** matters because without explicit observables, there is no way to distinguish scientific law from visual analogy.
- The **experiment layer** matters because thresholds and scaling laws are properties of ensembles and regime space, not of individual simulations alone.
- The **calibration layer** matters because elegant minimal models must still answer to real fires.
- The **benchmark layer** matters because the field needs not only new models, but new standards for showing what those models explain.

The machine is therefore cumulative. Each part builds the next. Each aim depends on outputs from the previous one. By the end of the project, what began as a reduced mathematical description becomes a complete scientific system for relating landscape structure to fire form.

## How This Will Change Fire Modeling for the Better

The long-term value of the project is not only the specific software produced, but the modeling logic it introduces.

First, it provides a **mechanistic reduction framework** for fire science. Instead of treating model complexity as self-justifying, it asks what complexity is necessary and demonstrates the answer empirically.

Second, it makes **geometry central** to wildfire theory. Fire perimeters, roughness, elongation, and scale-dependent boundary structure become first-class observables rather than incidental outputs.

Third, it establishes a **shared benchmark architecture** in which synthetic mechanism tests, pattern-recovery tests, and predictive tests are linked. This creates a more disciplined path for future fire-model development.

Fourth, it creates a bridge between **fundamental science and practical application**. By identifying the conditions under which substrate structure, anisotropy, and coupling govern spread, the framework can inform scenario analysis for fuel treatment, landscape connectivity, and WUI structure while remaining grounded in theory.

Finally, it changes the scientific question itself. Rather than asking only, “Can we simulate this fire?” it asks, “What governs the form of wildfire, what is the simplest system that explains it, and when does additional complexity become necessary?” That is a deeper and more general question. It is also one that can reorganize how wildfire modeling is done.

## Expected Outcomes

By the end of the project, we expect to deliver:

1. A mathematically explicit minimal theory of fire growth based on ignition-time surfaces and anisotropic propagation.
2. A modular open-source software system implementing the model hierarchy `M0–M3`.
3. A common case-object architecture for synthetic and real wildfire analyses.
4. A robust library of geometry, scaling, and progression observables.
5. Estimated threshold conditions and scaling laws with quantified uncertainty.
6. A shared benchmark suite for mechanism recovery, pattern recovery, and predictive skill.
7. A synthesis identifying where coupling and added complexity are necessary for explaining real wildfire form.

Together, these outputs constitute both a new scientific framework and a reusable research infrastructure.

## Broader Significance

By returning fire to the domain of growth and form, this project places wildfire alongside other natural systems whose complexity is made intelligible through minimal laws, dimensionless controls, and emergent structure. The resulting ideas and methods will be relevant not only to wildfire science, but to broader questions of spread, boundary formation, threshold behavior, and pattern emergence across ecology, geophysics, and complex systems science.

At the same time, the project addresses an urgent applied problem. As wildfire becomes an increasingly dominant force across many landscapes, the need is not only for better prediction, but for deeper explanation. Management, planning, and risk assessment all benefit from understanding what features of a landscape make fire more connected, more elongated, more spanning, or more controllable. A theory-grounded generative framework offers a principled route to that understanding.

## Summary

This project asks a classical question with modern tools: **how does fire grow, and what determines the form it takes?** It answers that question by building a scientific machine in stages: first a substrate, then an engine, then instruments of measurement, then tests against the world. The result is a framework that does more than simulate fire. It reveals the conditions under which wildfire acquires form, quantifies the thresholds and scaling laws that organize that form, and establishes when added complexity is truly needed. In doing so, it offers a path toward a more explanatory, more comparable, and ultimately more useful science of fire modeling.
