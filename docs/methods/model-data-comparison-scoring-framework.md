# Method 1C: Model-Data Comparison and Scoring Framework

## Overview

This section defines how we determine whether a candidate mechanism is correct.

To determine which generative mechanisms correctly explain wildfire growth, we do not rely on a single measure of model performance. Instead, we treat model evaluation as a structured experiment in which each model is subjected to a sequence of tests. In each test, we take a specific action, observe the resulting agreement or disagreement with empirical data, and use that outcome to either retain or reject the model. A model is only considered viable if it consistently reproduces multiple independent patterns observed in real fires, using the same measurement system applied to both observed and simulated data.

This approach follows principles of pattern-oriented modeling, in which models are evaluated against multiple independent patterns observed in the system rather than a single outcome. It ensures that we are not asking whether a model merely looks similar, but whether it reproduces the same patterns, relationships, and behaviors for the same underlying reasons.

Taken together, these steps define a formal elimination framework in which candidate mechanisms are progressively rejected unless they satisfy all independent constraints.

## Establishing a common basis for comparison

We begin by placing observed fires from FIRED and simulated fires into a common measurement framework using CubeDynamics. For each fire, we extract a consistent set of observables, including perimeter through time, burned area, growth rates, boundary geometry, directional spread, and environmental conditions along the fire boundary. This ensures that any comparison between models and data is made using identical definitions and measurement operators.

The result of this step is a set of matched datasets describing observed and simulated fires in the same terms. This allows us to directly compare patterns without introducing bias from inconsistent measurement.

The decision logic at this stage is simple: a model must be capable of reproducing all categories of observed behavior. If it fails to reproduce any major class of observable pattern, it is rejected before further analysis.

## Comparing distributions of behavior

Because wildfire behavior is highly variable, we do not compare only average values. Instead, we examine the full distribution of behaviors across fires and time. For each observable, such as growth rate or boundary roughness, we compare the distribution produced by the model to the distribution observed in real fires.

We quantify this comparison using metrics such as Earth Mover's Distance, which measures how much one distribution must be reshaped to match another, and the Kolmogorov-Smirnov statistic, which measures the maximum difference between distributions.

If the model reproduces the overall shape and spread of the observed distribution, it is retained. If it produces distributions that are systematically too narrow, too broad, or shifted, it is rejected. This step ensures that models capture variability, not just central tendencies.

## Comparing growth trajectories through time

Next, we evaluate how fires evolve through time. We compare trajectories of perimeter, area, and growth rate between observed and simulated fires. Because fires may evolve at different speeds while still following similar patterns, we use dynamic time warping to align trajectories based on shape rather than exact timing.

If a model reproduces the overall form of growth, meaning that its trajectories follow the same patterns as observed fires even if shifted in time, it is retained. If the shape of growth differs fundamentally, the model is rejected. This ensures that models capture the dynamic behavior of fire spread, not just static outcomes.

## Enforcing the scaling constraint

We then test whether the model reproduces the observed scaling relationship between perimeter and time. For each fire, we estimate the scaling exponent and evaluate its stability through time.

Because this scaling relationship is a central empirical result, it is treated as a strict constraint. If a model fails to reproduce the correct scaling exponent, or produces unstable scaling behavior, it is rejected regardless of its performance on other metrics.

This step ensures that all retained models are consistent with the fundamental growth law observed in real fires.

## Evaluating boundary geometry across scales

We next examine the structure of the fire boundary. Real fire perimeters exhibit complex, multiscale geometry, meaning their structure changes depending on the scale at which they are measured.

We quantify this using measures such as fractal dimension and perimeter-area relationships, and we compare these metrics between observed and simulated fires across multiple spatial scales.

If a model reproduces boundary structure consistently across scales, it is retained. If it matches geometry at one scale but not others, it is rejected. This step ensures that models capture the underlying structure of the fire boundary, not just its overall shape.

## Testing mechanism-specific relationships

A key goal of this project is not only to reproduce observed patterns, but to reproduce the relationships that generate those patterns. We therefore test whether models reproduce relationships such as the coupling between boundary length and growth rate, or the interaction between geometry and environmental conditions.

If a model produces the correct patterns but fails to reproduce these relationships, it is rejected. This prevents models from being accepted based on superficial similarity and ensures that retained mechanisms reflect the correct underlying processes.

## Evaluating directional behavior

Wildfires do not spread uniformly in all directions. Instead, they exhibit directional behavior driven by environmental factors such as wind and terrain. We therefore evaluate whether models reproduce directional growth patterns and their alignment with environmental forcing.

Models that capture this anisotropic behavior are retained, while those that produce uniform or incorrect directional patterns are rejected. This step ensures that models account for the directional nature of real fire spread.

## Testing performance under extreme conditions

We then evaluate model performance during extreme fire behavior, such as periods of rapid growth or strong directional forcing. These conditions are known to be challenging for many existing models.

If a model continues to reproduce observed patterns under extreme conditions, it is retained. If it fails under these conditions, it is rejected. This ensures that accepted models are robust and capable of explaining both typical and extreme fire behavior.

## Integrating results across all tests

Because no single metric determines correctness, we evaluate model performance across all tests simultaneously. We use a multi-objective framework in which models must satisfy all primary criteria and are compared using Pareto dominance, meaning that a model is only considered optimal if no other model performs better across all criteria simultaneously.

Models that satisfy all constraints and are not outperformed across the full set of metrics are retained. Models that fail any critical test or are consistently outperformed are rejected.

## Guarding against false agreement

Finally, we address the possibility that different mechanisms could produce similar outputs. To reduce this risk, we require that models match observations across multiple independent dimensions, including scaling, geometry, dynamics, environmental response, and extreme behavior.

Only models that match all of these dimensions simultaneously are considered valid. This reduces the likelihood that incorrect mechanisms are accepted due to coincidental agreement in a subset of metrics.

## Outcome

This framework provides a formal, reproducible system for identifying the mechanisms that govern wildfire growth. By systematically testing models against multiple independent criteria and rejecting those that fail any critical test, we isolate the minimal set of processes required to reproduce observed fire behavior.

Because each test captures a different, independent aspect of wildfire behavior, including scaling, geometry, dynamics, environmental response, and extreme conditions, agreement across all tests provides strong evidence that the underlying mechanism is correct rather than coincidentally similar.

In plain terms, we are not asking whether a model fits the data. We are asking whether it reproduces the system itself, across all observable dimensions, and for the correct underlying reasons.

The robustness and reliability of this framework are evaluated in the following section.
