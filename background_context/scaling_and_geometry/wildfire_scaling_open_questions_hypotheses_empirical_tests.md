# Wildfire Scaling: Open Questions, Hypotheses, and Empirical Tests

## Overview

Recent observations suggest that wildfire perimeter growth may exhibit non-diffusive scaling behavior, potentially following relationships such as:

```text
P(t) ~ t^(2/3)
```

with an implied fractal boundary dimension near:

```text
D ~ 4/3
```

If robust, this pattern would imply that wildfire spread may be governed by emergent geometric rules, not only by local spread physics. However, substantial uncertainty remains about whether such scaling exists, when it occurs, what mechanisms generate it, and whether current fire models reproduce it.

This note surveys major open questions surrounding wildfire perimeter scaling and outlines empirical and modeling tests that could address them using datasets such as `FIRED` and analytical frameworks such as `CubeDynamics`.

The goal is to articulate a research agenda that bridges wildfire behavior, statistical physics, landscape ecology, and satellite observation.

## 1. Does a reproducible scaling regime exist?

### The question

The most fundamental empirical question is whether wildfire perimeter growth follows a reproducible power-law relationship through time.

Candidate scaling relationship:

```text
P(t) ~ t^(2/3)
```

If true, this would indicate that wildfire spread is not governed by classical diffusion processes, which would instead produce scaling of the form:

```text
R(t) ~ t^(1/2)
```

Instead, wildfire spread would behave more like a rough propagating interface in a heterogeneous medium.

### Why this question is open

Although satellite datasets now provide time-resolved fire perimeters, few studies have systematically examined perimeter growth scaling across large fire populations.

Possible complications include:

- measurement resolution effects
- perimeter smoothing artifacts
- temporal sampling intervals
- heterogeneity in fire regimes

### Empirical test

Using `FIRED` fire progression data:

1. reconstruct `P(t)` and `A(t)` for many fires
2. estimate growth exponents using log-log regression
3. evaluate robustness across spatial resolution

### Expected outcomes

Possible results include:

- a consistent exponent near `2/3`
- a distribution of exponents clustered around a central value
- no clear scaling relationship

Each outcome would significantly inform wildfire spread theory.

## 2. When during the fire lifetime does scaling apply?

### The question

Even if scaling exists, it may not apply uniformly across the entire fire lifetime.

Many natural growth processes exhibit scaling only during a middle expansion phase, after ignition but before termination constraints dominate.

This suggests a possible three-phase wildfire growth model:

1. ignition / nucleation phase
2. expansion / scaling phase
3. termination / constraint phase

### Why this question is important

Failure to account for growth phases could produce misleading scaling estimates.

For example:

- early ignition dynamics may be dominated by stochastic local effects
- late-stage fires may be limited by fuel exhaustion or suppression

### Empirical test

For each fire:

1. reconstruct perimeter trajectories `P(t)`
2. detect breakpoints in growth behavior
3. identify intervals where power-law fits are stable

Scaling collapse techniques can then test whether normalized trajectories align across fires during the expansion phase.

### Expected outcomes

Evidence may show that:

- scaling emerges after fires exceed a minimum size
- scaling persists for a substantial fraction of fire duration
- scaling breaks down near termination

## 3. What physical mechanism produces the observed exponent?

### The question

If a consistent scaling exponent exists, the next challenge is identifying the physical processes responsible for it.

Several candidate mechanisms exist:

- diffusive spread
- ballistic spread
- fractal interface growth
- percolation and connectivity
- spotting and long-range transport

### Empirical and modeling tests

Develop minimal generative models representing each mechanism and compare simulated growth curves to observed fire trajectories.

### Expected outcomes

The dominant mechanism may involve a combination of:

- fuel connectivity
- wind-driven anisotropy
- occasional long-range ignition events

## 4. Is the fractal dimension of fire perimeters universal?

### The question

If wildfire perimeters exhibit fractal geometry, an important question is whether the boundary dimension is universal or varies across environments.

A value near `4/3` appears in several theoretical systems including percolation cluster hulls.

However, real wildfire boundaries may be influenced by:

- vegetation patterns
- topography
- wind fields
- suppression activity

### Empirical test

Measure boundary fractal dimension using multiple methods:

- box-counting
- perimeter-area scaling
- divider methods

Apply these measurements across diverse ecosystems.

### Expected outcomes

Possible outcomes include:

- clustering of dimensions near a universal value
- systematic variation across fire regimes
- resolution-dependent measurements

## 5. What role does landscape connectivity play?

### The question

Landscape ecology emphasizes that disturbance spread depends on spatial connectivity among fuel patches.

Percolation theory predicts that near a connectivity threshold, disturbance clusters become fractal and exhibit scale-invariant geometry.

### Empirical test

Combine fire progression data with vegetation and fuel maps to estimate connectivity metrics.

Test whether fires occurring in landscapes near connectivity thresholds exhibit stronger fractal scaling.

### Expected outcomes

Evidence may reveal that fractal wildfire perimeters emerge primarily in landscapes with high fuel connectivity.

## 6. How does anisotropy affect fire geometry?

### The question

Wildfire spread is strongly influenced by directional forces such as wind and slope.

These forces introduce anisotropy that may stretch or distort fire perimeters.

### Empirical test

Quantify anisotropy using perimeter shape metrics and compare scaling exponents under different wind regimes.

### Expected outcomes

Directional forcing may alter perimeter shape while preserving underlying scaling relationships.

## 7. What role does spotting play?

### The question

Spotting allows fire to spread discontinuously through ember transport.

These long-distance ignition events may significantly alter growth geometry.

### Empirical test

Identify fires with strong spotting signatures and compare scaling exponents to fires dominated by continuous spread.

### Expected outcomes

Spotting may produce superdiffusive growth patterns that modify perimeter scaling.

## 8. Do existing fire models reproduce observed scaling?

### The question

Operational wildfire simulators focus primarily on predicting local spread rates rather than emergent geometric properties.

It remains unclear whether these models reproduce real wildfire scaling behavior.

### Empirical test

Run existing fire models under controlled scenarios and compute simulated perimeter growth trajectories.

Compare model outputs to satellite-derived scaling relationships.

### Expected outcomes

Models may reproduce some scaling properties but fail to capture fractal boundary roughness.

## 9. Are fire size distributions related to perimeter scaling?

### The question

Wildfire size distributions often follow power-law relationships.

It is not yet clear whether these distributions arise from the same processes that generate perimeter scaling.

### Empirical test

Compare scaling relationships between:

- fire size distributions
- perimeter growth trajectories

### Expected outcomes

A shared mechanism such as landscape connectivity or critical dynamics may produce both patterns.

## 10. Toward a unified theory of wildfire geometry

The broader intellectual challenge is to understand how local fire spread processes produce large-scale geometric patterns.

Wildfire science has traditionally focused on:

- combustion physics
- spread rate models
- fire behavior prediction

However, satellite observations now allow researchers to examine wildfire growth as a geometric and dynamical system.

This creates an opportunity to develop a unified framework that integrates:

- local spread physics
- landscape structure
- atmospheric forcing
- emergent spatial geometry

## Conclusion

Wildfire perimeter scaling represents a promising avenue for advancing wildfire science.

Answering the questions outlined here would help determine whether wildfire growth obeys reproducible geometric laws, what mechanisms generate those laws, and how current fire models should evolve to capture emergent fire dynamics.

The combination of event-based datasets such as `FIRED` and cube-based analytical frameworks such as `CubeDynamics` provides the tools needed to address these questions at unprecedented scale.
