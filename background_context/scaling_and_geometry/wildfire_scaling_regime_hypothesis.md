# Wildfire Scaling Regime Hypothesis

## Overview

A central question for a wildfire scaling framework is when during the fire lifetime scaling should apply. A plausible hypothesis is that wildfire growth does not follow one scaling law from ignition to extinction. Instead, scaling likely emerges only during a middle expansion phase when the fire front behaves as a rough propagating interface moving across heterogeneous fuels.

Under this view, wildfire lifetime is divided into three dynamical regimes:

1. Ignition / nucleation phase
2. Expansion / scaling phase
3. Constraint / termination phase

The key proposal hypothesis is that the observed perimeter growth relationship

```text
P(t) ~ t^(2/3)
```

and the implied fractal boundary dimension near

```text
D ~ 4/3
```

apply primarily during the expansion phase, not across the full fire lifetime.

## 1. Three-phase wildfire lifetime model

### Phase 1: Ignition / nucleation

In the earliest stage of fire growth:

- fire size is small
- geometry is dominated by local fuel arrangement
- stochastic ignition effects are large
- perimeter estimates are noisy
- suppression or short-term weather may dominate dynamics

At this stage the fire is too small to exhibit robust emergent geometry.

#### Predictions

- perimeter and area growth are noisy
- apparent exponents vary widely
- no stable scaling law should be expected

### Phase 2: Expansion / scaling regime

Once the fire becomes established:

- the front spans many fuel patches
- local heterogeneities begin to average into statistical structure
- the perimeter behaves like a rough propagating interface
- landscape connectivity, anisotropy, and long-range spread begin to determine growth geometry

This is the regime where a scaling law is most likely to emerge.

Core hypothesis:

```text
P(t) ~ t^(2/3)
```

with a corresponding boundary fractal dimension near

```text
D ~ 4/3
```

This phase is the main target of the proposal.

### Phase 3: Constraint / termination

As the fire matures and begins to slow:

- fuel exhaustion increases
- suppression and containment become important
- weather changes may reduce spread
- topographic and landscape boundaries limit expansion
- the front may fragment or smooth

In this late stage, finite-size effects and external constraints should break the scaling regime.

#### Predictions

- perimeter growth slows
- scaling exponents shift or collapse
- the fire exits the fractal growth regime

## 2. The core hypothesis

The most important conceptual statement is:

Wildfire perimeter growth exhibits reproducible non-diffusive scaling during the expansion phase of fire development, with fractal geometry emerging from local spread processes interacting with landscape connectivity, anisotropy, and long-range transport.

This hypothesis does not claim that all fires obey a single exponent over their entire lifetimes.

Instead it predicts:

- a middle scaling regime exists
- this regime is measurable
- the exponent is likely stable enough to detect statistically
- departures from the regime occur at early and late stages

## 3. Why this hypothesis makes sense

This phase-structured view is consistent with many classes of growing systems.

Examples from other fields:

- Percolation and critical growth: scale invariance emerges after nucleation, not at the first occupied sites.
- Interface growth: roughening laws apply after the interface develops, not at the moment of formation.
- Power-law event statistics: scaling often appears only above lower size thresholds and below upper finite-size limits.

Wildfire growth likely behaves similarly.

## 4. The key test: detecting a scaling regime

The main empirical challenge is to identify whether a real fire contains a distinct scaling interval.

For each fire, the proposal would reconstruct:

- perimeter through time: `P(t)`
- area through time: `A(t)`
- perimeter-area relationship: `P(A)`

Then it would test whether the fire contains:

- an early non-scaling phase
- a middle power-law phase
- a late constrained phase

This can be done using segmented fits, breakpoint detection, and scaling collapse.

## 5. Scaling collapse as the cleanest test

A particularly elegant test comes from statistical physics: scaling collapse.

The idea is to ask whether fires of different sizes and durations can be rescaled so that their growth curves fall on a common universal shape.

### General idea

If different fires are realizations of the same underlying process, then after appropriate normalization their trajectories should align.

For example, define:

- `t* = t / T_fire` (time normalized by fire duration)
- `P* = P / P_max` (perimeter normalized by final or characteristic perimeter)

If the expansion phase follows a common scaling law, then plots of `P*` versus `t*` should collapse onto a shared curve during the scaling interval.

### Why this matters

Scaling collapse provides evidence that:

- the exponent is not just an artifact of averaging
- the same generative process may operate across many fires
- the scaling regime occupies a reproducible fraction of the fire lifetime

### What success would look like

A successful collapse would show:

- strong scatter during ignition
- overlap during a middle interval
- divergence again during termination

That pattern would directly support the three-phase wildfire lifetime model.

## 6. Proposal-ready testable predictions

### Prediction 1

Small fires and the earliest time steps will not show stable scaling.

### Prediction 2

A middle expansion regime will exhibit approximately power-law perimeter growth.

### Prediction 3

The perimeter growth exponent during this regime will cluster near `2/3`.

### Prediction 4

Independent perimeter measurements will indicate a non-Euclidean boundary dimension near `4/3`.

### Prediction 5

Late-stage fires will deviate from the scaling regime due to finite-size, suppression, weather, and fuel limitations.

### Prediction 6

Fires stratified by regime and rescaled by characteristic time and size will show partial or strong scaling collapse.

## 7. Why this matters for fire modeling

Most wildfire models focus on local spread rates or local front motion.

This proposal asks a different question:

At what stage of the fire lifetime does large-scale geometric regularity emerge?

Answering that question would:

- identify the relevant growth regime for scaling theory
- prevent overclaiming a universal law across all fire stages
- provide a new diagnostic benchmark for wildfire models

A model should not merely spread fire; it should also reproduce the timing and geometry of the scaling regime.

## 8. Working proposal framing

A strong proposal framing is:

We hypothesize that wildfire perimeter scaling is a regime-specific property of the fire expansion phase. Using time-resolved fire perimeters, we will identify when scaling emerges, how long it persists, when it breaks down, and whether normalized fire trajectories collapse onto a common scaling form.

This framing is both ambitious and defensible because it turns the reviewer concern into a measurable research objective.

## Conclusion

The most plausible current hypothesis is not that wildfire growth obeys one power law from ignition to extinction. Rather, wildfire growth likely enters a middle expansion regime in which the perimeter behaves as a rough fractal interface and follows reproducible non-diffusive scaling.

The proposal should therefore focus on:

1. identifying the scaling regime
2. measuring its exponent and geometry
3. testing its universality across fires
4. determining what mechanisms produce it

This makes the project both scientifically rigorous and responsive to reviewer concerns.
