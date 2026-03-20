# FIRE-MODEL Proposal Integration Document

## Status and purpose

This document is a consolidation layer for the proposal. It gathers ideas that have been developed across planning threads, draft text, and implementation discussions and places them into a single, coherent structure. It is not intended to be submission-ready prose. Instead, it is a working substrate that preserves the full richness of the thinking while making the relationships between concepts explicit.

The goal is to ensure that future drafts can draw from a consistent and complete foundation rather than re-deriving arguments in fragmented ways. Throughout, sections are labeled so they can be easily extracted, recombined, and promoted into the final proposal, website, or supporting materials. Redundancy is intentional. Clarity and completeness take priority over brevity.

## `[CORE_CLAIM]`

Wildfire behavior is governed by the geometry of its interface across scales. A model that does not reproduce this geometry, even if it reproduces outcomes such as burned area or rate of spread, is not capturing the underlying process. The central claim of this proposal is therefore that predictive wildfire models must be constrained by the structure of the evolving interface itself. Geometry is not a byproduct of fire dynamics; it is a primary expression of those dynamics and a necessary condition for predictive validity.

## `[PROBLEM_STATEMENT]`

### `[CURRENT_MODEL_LIMITATIONS]`

Contemporary wildfire models span a range of approaches, from empirical spread models to physics-based simulators and cellular automata. Across these approaches, evaluation is typically focused on quantities such as rate of spread, fireline intensity, or final burned extent. These are important outputs, but they are endpoint or local measures. They do not constrain how the fire organizes itself across space and scale.

As a result, models can match observed outcomes while failing to reproduce the structure of real fire perimeters. This creates a situation in which models may appear successful under standard validation metrics but are not actually representing the governing processes that shape fire behavior.

### `[FAILURE_MODE]`

The core failure mode is that models are underconstrained with respect to geometry. They are free to generate interfaces that are too smooth, too rough, or structurally inconsistent across scales, as long as aggregate outcomes remain plausible. This allows for correct answers produced for incorrect reasons, which limits generalization and undermines predictive reliability under novel conditions.

### `[OBSERVABLE_FAILURE]`

These limitations are not abstract. They manifest in measurable discrepancies between simulated and observed fire perimeters. In particular, models often fail to reproduce stable scaling relationships in interface length as a function of measurement scale, commonly expressed as `L(epsilon)`. They may produce incorrect fractal dimensions, inconsistent roughness, or patterns that vary unpredictably across sensors and resolutions. These discrepancies provide a concrete entry point for diagnosing model inadequacy.

## `[PROPOSED_SOLUTION]`

### `[GENERATIVE_INTERFACE_MODEL_GIM]`

#### `[GIM_DEFINITION]`

The Generative Interface Model (GIM) reframes wildfire modeling around the evolution of the fire boundary itself. Rather than treating the perimeter as a secondary outcome of spread processes, the GIM treats it as the primary object of interest. The model is designed so that the interface it generates must match the geometric properties observed in real fires across scales.

#### `[GIM_AS_MACHINE]`

It is useful to think of the GIM not as a conceptual framework but as a machine with clearly defined components. The inputs to this system include spatially explicit fuel distributions, topographic constraints, weather forcing, and ignition conditions. These inputs define the environment in which the interface evolves.

Within the model, a set of coupling rules governs how energy and probability of spread move through space. These rules may be expressed through reaction-diffusion dynamics, transport processes, or other minimal representations of local interactions. An ignition kernel determines how new regions of the interface are activated, either deterministically or stochastically, depending on the model formulation.

The output of the system is a time-evolving interface: a sequence of fire perimeters that can be analyzed geometrically. Crucially, the model is not free to produce arbitrary interfaces. It is constrained to reproduce observed scaling relationships and cross-scale geometric consistency. If the model produces an interface that diverges from empirical scaling behavior, that divergence is treated as a failure of the model, not as noise.

This framing shifts the role of modeling from reproducing outcomes to reproducing structure. It also creates a direct connection between theory and validation because the same geometric quantities that define the model also define how it is evaluated.

## `[THEORY_TO_MEASUREMENT_BRIDGE]`

### `[CHAIN]`

A central requirement of the proposal is that theoretical ideas must translate cleanly into measurable quantities. This translation proceeds through a chain that connects abstract concepts to empirical data.

At the theoretical level, the focus is on interface geometry, scaling laws, and quantities such as fractal dimension. These concepts describe how the complexity of the fire boundary changes with scale.

To make these ideas measurable, the fire perimeter is extracted from raster data at multiple resolutions. This produces a boundary representation that can be analyzed computationally. Algorithms such as box-counting are then used to compute the length of the interface as a function of measurement scale, generating `L(epsilon)` curves. The slope of these curves in log-log space provides an estimate of scaling behavior.

These computations are applied to multiple datasets, including `FIRED`, `MTBS`, `VIIRS`, and higher-resolution sources such as drone imagery and `NEON AOP` data. Cross-sensor comparisons are essential for establishing that observed patterns are not artifacts of a particular measurement system.

Uncertainty enters at each stage, including sensor resolution, classification accuracy, and temporal sampling. The framework explicitly acknowledges and quantifies these uncertainties so that observed scaling behavior can be interpreted robustly.

## `[SCALING_CONVERGENCE]`

### `[MULTIPLE_LINES_OF_EVIDENCE]`

The proposal does not rely on a single line of reasoning for scaling behavior. Instead, it draws on multiple domains that independently point toward similar geometric structure.

In percolation theory, cluster boundaries exhibit fractal properties with well-characterized dimensions, often near `4/3` in two-dimensional systems. Fire perimeters share qualitative similarities with these boundaries, suggesting a connection between spread processes and critical phenomena.

In turbulence, energy cascades across scales produce structured patterns that follow scaling laws described by Kolmogorov theory. While the mechanisms differ, the presence of scale-invariant structure provides an important parallel.

In biological systems, metabolic scaling laws, such as the `3/4` power law, emerge from the geometry of resource distribution networks. These networks are constrained by transport efficiency, which imposes geometric regularities on the system.

### `[CONVERGENCE_ARGUMENT]`

Taken together, these domains suggest that scaling behavior is not incidental but arises from fundamental constraints on transport, interaction, and structure. The convergence of percolation, turbulence, and metabolic scaling on similar geometric signatures supports the hypothesis that wildfire interfaces are governed by a general class of scaling laws. This proposal treats that convergence not as speculation, but as a testable organizing principle.

## `[BENCHMARK_SYSTEM]`

### `[CORE_IDEA]`

The benchmark system is built on the premise that models should be evaluated based on their ability to reproduce geometric observables across scales. Instead of asking whether a model gets the right answer in aggregate, the benchmark asks whether it produces the right structure at every scale.

### `[METRICS]`

The primary metrics include scaling curves of interface length as a function of measurement scale, estimates of fractal dimension, measures of roughness, and distributions of curvature. These quantities provide a multi-dimensional description of interface geometry.

### `[EVALUATION_CRITERIA]`

Model performance is assessed based on the stability of these metrics across datasets, agreement with empirically observed ranges, and consistency across sensors and resolutions. The goal is to establish whether a model captures the invariant structure of fire, not just specific instances.

### `[BASELINES]`

Existing models, including operational tools such as `FARSITE` and research models such as `QUIC-Fire` and cellular automata approaches, provide baselines for comparison. These models are expected to reproduce some aspects of fire behavior but may fail under geometric evaluation.

### `[SUCCESS_DEFINITION]`

A successful model is one that reproduces observed scaling behavior within defined tolerances and maintains that performance across ecosystems and data sources. Partial success is possible if a model captures some but not all geometric features, providing insight into which mechanisms are missing.

## `[DELIVERABLES]`

The project is designed to produce a small number of concrete, reusable outputs. These include a curated dataset of wildfire interfaces across scales, a library of tools for computing geometric observables, a reference implementation of the Generative Interface Model, a standardized benchmark suite for evaluating fire models, and an integrated module within `CubeDynamics` for applying these tools to spatiotemporal data. Each of these deliverables is intended to stand on its own while also contributing to a unified framework.

## `[WORK_PLAN_STRUCTURE]`

### `[YEAR_1_DETECT]`

The first year focuses on establishing whether robust scaling relationships exist in real wildfire data. This involves building the data pipeline, computing geometric metrics across multiple datasets, and testing for consistency. The key decision point at the end of this phase is whether stable scaling laws can be identified across sensors and ecosystems.

### `[YEAR_2_EXPLAIN]`

The second year shifts to explanation. Minimal models are developed and tested to determine whether they can reproduce the observed geometric structure. This phase explores which mechanisms are necessary and sufficient to generate the scaling behavior identified in Year 1. The central question is whether simple, interpretable models can produce the same patterns seen in real fires.

### `[YEAR_3_APPLY]`

The third year focuses on application. The benchmark system is formalized, and the tools are packaged for use by the broader community. Models are evaluated systematically, and the framework is integrated into `CubeDynamics`. The final decision point is whether geometric metrics can reliably distinguish between models and provide actionable insight.

## `[USER_WORKFLOW]`

### `[PERSONA_MODEL_DEVELOPER]`

A model developer interacts with the system by running a fire simulation and extracting the resulting interface geometry. Using the provided tools, they compute scaling metrics and compare them against the benchmark dataset. Discrepancies between simulated and observed geometry reveal where the model is failing, guiding further development. This workflow turns abstract evaluation into a concrete diagnostic process.

## `[REMAINING_GAPS]`

Several elements require further development before the proposal is fully mature. These include defining explicit error thresholds for benchmark metrics, formalizing acceptable ranges for scaling behavior, expanding comparisons with existing models, and developing more detailed user impact narratives. These gaps are known and can be addressed within the existing framework.

## `[NOTES]`

This document should be treated as a living integration layer. Its purpose is to hold the full structure of the proposal in one place, making it easier to produce consistent, high-quality narrative text. Future work should focus on refining individual sections into submission-ready prose while maintaining alignment with this underlying structure.
