# Wildfire Scaling Project: Rationale, Deliverables, Users, and Impact

## Overview

This document synthesizes the conceptual discussions around the wildfire scaling research program. It explains why the work matters, who will use it, what the deliverables are, and why the project merits a multi-year research investment.

The goal is to provide a clear narrative that can accompany the repository and help collaborators, reviewers, and future users understand the intellectual and practical motivations behind the project.

## Why study the geometry of wildfire growth?

Wildfire science has historically focused on two distinct levels of understanding:

1. Local fire behavior physics, including models describing rate of spread based on fuels, wind, slope, and combustion physics.
2. Fire regime statistics, including large-scale patterns such as fire size distributions, burned area trends, and return intervals.

What remains relatively unexplored is the intermediate level describing how fires grow geometrically through space and time. Satellite data now provide daily observations of fire perimeters, making it possible to reconstruct the dynamics of wildfire expansion across many events.

This project explores the hypothesis that wildfire perimeter growth may follow reproducible geometric scaling laws, potentially characterized by relationships such as:

- perimeter growth following a power-law relationship with time
- fire boundaries exhibiting fractal dimensions
- a middle expansion phase during which fires behave as rough spatial interfaces

If these patterns exist, they would connect wildfire science with broader theories of interface growth, percolation, and complex spatial systems.

## Major deliverables

### 1. Global fire growth trajectory dataset

The project will produce a standardized dataset describing how fires grow through time. Using satellite burned-area products and the `FIRED` event reconstruction system, the research team will reconstruct daily fire perimeters for many wildfire events.

Each fire will include:

- perimeter length through time
- burned area through time
- geometric complexity metrics
- environmental metadata

#### Why this matters

Most fire datasets record final burned area or ignition locations. Few datasets capture the dynamic geometry of fire growth. This dataset would provide a large-scale empirical foundation for studying wildfire expansion as a spatial process.

It also becomes reusable infrastructure for research questions beyond the scaling hypothesis.

### 2. Open-source scaling diagnostics

The project will develop analytical tools for measuring geometric scaling relationships in wildfire growth.

These tools will include methods for:

- perimeter-time scaling analysis
- fractal dimension estimation
- scaling collapse diagnostics
- geometric comparison of fire trajectories

The diagnostics will be released as modules within `CubeDynamics` so that other researchers can apply them to both observational data and model outputs.

#### Why this matters

Current wildfire models are typically evaluated using local metrics such as spread rate or burn severity. Scaling diagnostics introduce a new way to test models: whether they reproduce the large-scale geometry of real fires.

### 3. Empirical characterization of wildfire scaling

The project will analyze many fire trajectories to determine:

- whether a consistent perimeter growth exponent exists
- when scaling appears during a fire's lifetime
- how scaling varies across ecosystems and climates

This work fills a gap between detailed fire behavior experiments and statistical studies of fire regimes.

#### Why this matters

Understanding the geometry of wildfire expansion provides insight into how local spread processes scale up to landscape-scale fire behavior.

### 4. Mechanistic modeling experiments

The project will test candidate mechanisms capable of generating wildfire scaling patterns.

Minimal models will represent processes such as:

- diffusion-like spread
- connectivity-driven spread across heterogeneous fuels
- anisotropic wind-driven propagation
- long-distance spotting

Each model will generate synthetic fire trajectories that can be analyzed using the same scaling diagnostics applied to satellite observations.

#### Why this matters

This approach connects empirical observations with underlying physical processes and helps identify which mechanisms shape wildfire growth geometry.

### 5. Benchmark analysis of existing fire models

The scaling diagnostics will be applied to outputs from wildfire simulators such as:

- `FARSITE`
- `WRF-Fire`
- `FIRETEC`

This will reveal whether current fire models reproduce the geometric scaling properties observed in real fires.

#### Why this matters

This provides a new benchmark for wildfire model validation based on emergent system behavior rather than only local spread rates.

### 6. Theoretical framework for wildfire growth geometry

The final deliverable is a conceptual synthesis explaining how wildfire growth emerges from interactions among:

- fuel connectivity
- atmospheric forcing
- landscape heterogeneity
- fire spread physics

This framework links wildfire science with broader theories of spatial dynamics and complex systems.

## Who will use these results?

The immediate users of the project outputs are primarily scientific and technical communities rather than frontline firefighting personnel.

### Primary users

#### Fire model developers

Researchers developing fire simulators can use scaling diagnostics to test whether their models reproduce realistic fire growth geometry.

#### Remote sensing scientists

Satellite fire analysts can use the dataset and methods to interpret fire expansion patterns across regions and ecosystems.

#### Fire behavior researchers

Scientists studying fire spread processes gain a new empirical framework for linking local physics with landscape-scale dynamics.

#### Earth system scientists

Researchers studying disturbance regimes can integrate fire growth scaling into models of ecosystem and climate interactions.

### Secondary users

#### Agency research groups

Fire science groups within agencies such as USFS or NOAA may use the methods to evaluate forecasting tools and fire models.

#### Risk assessment and planning teams

Strategic planning teams studying fire risk across landscapes may use geometric growth indicators to classify fire regimes.

### Long-term downstream users

#### Operational fire decision systems

Incident commanders are unlikely to use fractal or scaling analysis directly. However, improvements in wildfire models and forecasting tools may indirectly benefit operational decision making.

The pathway to operational impact typically follows:

```text
scientific insight -> improved models -> improved forecasting tools -> operational use
```

## Analogies from biology and physics

The potential impact of wildfire scaling research is similar to several major developments in other fields.

### Allometric scaling in biology

Biological systems exhibit scaling relationships between body size and metabolic rate. These relationships became central organizing principles in ecology and physiology.

A similar scaling relationship for wildfire growth could provide a compact descriptor of fire dynamics.

### Turbulence scaling

Kolmogorov's turbulence theory introduced scaling laws used to evaluate atmospheric and fluid simulations.

Wildfire scaling laws could similarly serve as benchmarks for wildfire models.

### Fractal geometry in Earth sciences

Fractal analysis revealed consistent patterns in coastlines, river networks, and fault systems. These measurements became tools for understanding the processes shaping natural landscapes.

Wildfire perimeter scaling could play a similar role in disturbance ecology.

## Why this project requires major funding

Large-scale funding is justified because the project builds new scientific infrastructure rather than testing a single hypothesis.

Key investments include:

- constructing a global dataset of fire growth trajectories
- developing open analytical tools for geometric scaling analysis
- performing large-scale empirical studies across ecosystems
- building mechanistic models to explain observed patterns

These activities require sustained computational resources, algorithm development, and interdisciplinary collaboration.

## What the field gains

If successful, the project advances wildfire science in three ways.

### New data infrastructure

A global dataset describing how fires grow through time.

### New model evaluation tools

Scaling diagnostics that evaluate whether wildfire simulations reproduce realistic geometric behavior.

### New conceptual framework

A theoretical understanding of wildfire growth as a spatial interface evolving through heterogeneous landscapes.

## Summary

This research program investigates whether wildfire growth follows reproducible geometric scaling laws and what mechanisms generate those patterns.

The project will produce datasets, analytical tools, modeling experiments, and theoretical insights that help bridge the gap between local fire behavior physics and landscape-scale fire dynamics.

Rather than being a purely academic exercise, the work provides foundational science that can improve wildfire models, remote sensing interpretation, and long-term fire risk analysis.
