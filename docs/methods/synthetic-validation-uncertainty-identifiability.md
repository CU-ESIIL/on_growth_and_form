# Synthetic Validation, Uncertainty, and Identifiability

## Overview

This section establishes how we verify that conclusions about wildfire mechanisms are both accurate and trustworthy. Rather than assuming that our measurement, comparison, and model-selection framework is correct, we treat the entire analytical pipeline as an object of study and subject it to a series of controlled tests. The central goal is to determine whether the system consistently produces correct answers when the truth is known, remains stable when data are imperfect, and is capable of distinguishing between competing explanations of wildfire behavior.

In practical terms, this section addresses three fundamental questions. First, if we construct a system where the correct answer is known in advance, does our framework recover that answer? Second, if we introduce realistic uncertainty into the data, do our conclusions remain stable? Third, if two mechanisms are genuinely different, does our framework correctly identify that difference? A method is considered reliable only if it succeeds across all three of these dimensions.

To ensure that all decisions are grounded in realistic conditions, we define tolerance thresholds using both empirical variability observed in real wildfire datasets and calibration experiments on synthetic data. This ensures that all judgments about agreement or disagreement reflect meaningful differences rather than arbitrary cutoffs.

## Synthetic validation: known-truth recovery

We begin by testing whether the full analytical pipeline can recover known truth. To do this, we generate synthetic fire datasets from controlled generative models in which the underlying mechanism and its expected properties are explicitly specified. These properties include the scaling relationship between perimeter and time, the geometric complexity of the boundary, and the relationship between boundary structure and growth dynamics.

For each synthetic fire, we compute the same observables used throughout the study, including perimeter as a function of time, total burned area, growth rate, scaling exponent, and geometric descriptors such as fractal dimension and perimeter-area scaling. These synthetic datasets are then processed through the full evaluation and model-selection workflow exactly as real data would be.

We quantitatively compare recovered values to the known true values using multiple measures, including absolute error, relative error, and confidence interval coverage. Confidence intervals are estimated using bootstrap resampling of time-series segments to capture variability in measurement.

We expect that a correctly functioning pipeline will recover values that are close to the true values and will correctly identify the generating mechanism as the top-ranked model. We therefore accept this step if the recovered scaling exponent falls within a predefined tolerance of the true value, geometric metrics fall within uncertainty bounds, and the correct mechanism is consistently selected. If any of these conditions are not met, the pipeline is considered unreliable and must be revised before being applied to real-world data.

## Measurement uncertainty and error propagation

We next evaluate how sensitive the framework is to realistic sources of measurement uncertainty. In real wildfire data, uncertainty arises from factors such as spatial resolution, temporal resolution, and the specific method used to extract fire boundaries.

To quantify this, we systematically perturb the data by altering spatial resolution, subsampling temporal observations, and applying alternative boundary extraction approaches. For each perturbed dataset, we recompute all observables and rerun the full evaluation pipeline.

Formally, this step compares the output of the analytical pipeline applied to the original data, denoted as `f(X)`, with the output from perturbed data, `f(X')`. Differences are quantified using absolute change, relative change, and normalized error metrics.

The expected outcome is that small perturbations in the input data lead to correspondingly small changes in derived quantities and do not alter the final model selection. We accept this step if the preferred mechanism remains unchanged and if variability in key observables is smaller than the differences between competing models. If perturbations lead to changes in model ranking, this indicates excessive sensitivity, and the measurement or comparison framework must be refined.

## Model stochasticity and ensemble consistency

Because many generative fire models include stochastic components, such as random ignition or probabilistic spread, we test whether conclusions depend on chance. Rather than evaluating a single simulation, we generate ensembles of simulations for each candidate mechanism.

For each ensemble, we compute the distribution of key observables and model scores, summarizing them in terms of their mean, variance, and selection frequency. Selection frequency is defined as the proportion of simulation runs in which a given mechanism is identified as the best-performing model.

We expect that a valid mechanism will perform consistently across realizations. We therefore accept this step if a mechanism maintains a high selection frequency and exhibits low variance in key observables relative to differences between mechanisms. If a model only occasionally matches observations, it is rejected as unreliable, as its agreement would be attributable to random variation rather than underlying process.

## Sensitivity analysis and parameter robustness

We then examine how sensitive model behavior is to parameter choices. A credible mechanism should reproduce observed patterns across a broad range of plausible parameter values, rather than requiring precise tuning.

To assess this, we perform global sensitivity analysis using two complementary approaches. Morris screening is used to identify which parameters have the greatest influence on model outputs, while Sobol variance decomposition is used to quantify how much of the variability in each observable is attributable to individual parameters and their interactions. In the Sobol framework, the total variance of an observable is decomposed into contributions from each parameter and combinations of parameters, providing a detailed understanding of model sensitivity.

We vary parameters across plausible ranges and recompute all observables and model scores. We expect that a robust mechanism will reproduce key properties, such as scaling behavior and boundary geometry, across a wide region of parameter space. We accept this step if model outputs remain within tolerance across this region. If correct behavior only occurs under narrow parameter settings, the mechanism is considered weak and is rejected.

## Regime detection and life-stage consistency

Wildfire behavior evolves through distinct phases, including early growth, expansion, and late-stage dynamics. We therefore test whether model performance is consistent across these phases.

We identify transitions between phases using change-point detection applied to time series of growth rate and scaling behavior. This method detects points where the statistical properties of the time series shift, indicating a change in regime. We then recompute all observables within each identified phase and evaluate model performance separately.

We expect that a valid mechanism will either reproduce behavior across all phases or exhibit deviations that can be explained by known physical processes. We accept this step if the preferred mechanism remains consistent across phases or if any deviations are scientifically interpretable. If a model matches only a single phase and fails in others, it is rejected as incomplete.

## Identifiability and equifinality testing

We explicitly test whether different mechanisms can be distinguished based on the available data. This addresses the problem of equifinality, in which multiple models produce similar observable patterns.

We represent each mechanism in a multi-dimensional space defined by observables such as scaling, geometry, growth dynamics, and environmental response. We compute distances between mechanisms in this space using distribution-based and trajectory-based metrics, and compare these distances to uncertainty envelopes derived from measurement error and stochastic variability.

We expect that distinct mechanisms will occupy separable regions of this space. We accept this step if the distance between mechanisms exceeds the uncertainty associated with each mechanism, indicating that they are distinguishable. If mechanisms remain indistinguishable, we report this explicitly rather than forcing a conclusion.

## Cross-validation with held-out fires

Finally, we evaluate whether conclusions generalize beyond the data used to develop the framework. We partition observed fires into development and validation subsets, using one set to establish model performance and the other to test generalization.

We apply the full evaluation pipeline to both subsets and compare model rankings. We expect that the same mechanisms will be supported in both datasets. We accept this step if model rankings are consistent across subsets. If a model performs well only on the development data but fails on the validation data, it is rejected as overfit.

## Outcome

Together, these tests provide a comprehensive validation of the analytical framework. A reliable system should consistently recover known truth, remain stable under realistic uncertainty, produce reproducible results across stochastic realizations, exhibit robustness across parameter ranges, perform consistently across fire life stages, distinguish between competing mechanisms when possible, and generalize to new data.

In plain terms, we only trust the final conclusions if the framework repeatedly produces the correct answer when the answer is known, and produces stable, consistent answers when the data are imperfect. This ensures that identified mechanisms are not only plausible, but genuinely supported by the structure of the data.
