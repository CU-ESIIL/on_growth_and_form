# FIRE-MODEL Resubmission Strategy Document

This page is the sendable strategy document for the FIRE-MODEL resubmission. It translates reviewer feedback into a falsifiable research program with explicit benchmarks, deliverables, and decision points.

> Status note: this is an internal strategy synthesis, not sponsor-issued guidance. Use it alongside the solicitation and checklist materials under [Funder Materials](funder-materials.md).

!!! note "Why this page is elevated"
    This document now has a privileged position in the site because it is the main revision-planning memo for the resubmission. It is meant to be shareable with collaborators as the current strategy statement.

## Overview

The central revision is a shift away from presenting wildfire growth as a single settled scaling law. The resubmission instead proposes a testable multi-regime framework in which fire behavior changes as growth proceeds and as transport constraints are relaxed or enforced.

The goal is to make the proposal legible as a discovery program with explicit benchmarks:

- what is observed;
- what is derived from those observations;
- what the models are expected to reproduce; and
- what evidence would support or challenge the framework.

## I. Narrative restructuring

We replace a scaling-centric narrative with a regime-based description: wildfire does not necessarily obey a single governing law across all stages of growth. Instead, it may transition between regimes that differ in effective dimensionality and in the balance between combustion demand and atmospheric transport.

We organize the science around three observable stages:

- **Pre-emergent:** patchy, ignition-limited, spatially sparse spread.
- **Transition / emergence:** increasing connectivity and ventilation, with the onset of a coherent front.
- **Post-emergent:** boundary-governed growth in which geometry dominates and scaling relations stabilize.

This restructuring also clarifies model roles:

- **Wave model:** local spread, coupling, and conditions for achieving a coherent front in the pre-emergent and transition regimes.
- **Manifold / geometric model:** reduced description once a coherent front exists in the post-emergent regime.

Meteorology is treated as a primary control through transport, mixing, and ventilation rather than as an auxiliary add-on.

## II. Physical foundation

We introduce a feasibility condition that can be operationalized with observations and models: a continuous fire front requires oxygen supply and atmospheric transport capacity to meet or exceed combustion demand at the leading edge.

We therefore define:

- **Ventilation capacity (`V`)** as a proxy family for transport support.
- **Combustion demand (`D`)** as a proxy family for energetic and fuel constraints at the advancing front.

### Ventilation capacity proxy family

Candidate ingredients for `V` include:

- near-surface wind speed `U` from reanalysis or stations;
- boundary-layer height `H` from reanalysis-derived products;
- stability or turbulence proxy `S`, such as Richardson-number class or gustiness index; and
- coupling factor `C`, terrain- and canopy-adjusted through empirical calibration.

Working example:

`V ∝ U × H × f(S) × C`

### Combustion demand proxy family

Candidate ingredients for `D` include:

- fuel load and fuel type from LANDFIRE-class products or equivalent sources;
- effective burn-layer thickness at the head, conditioned on fuel class; and
- heat of combustion or effective heat-release assumptions by fuel class.

Working example:

`D ∝ fuel_load × burn_depth × heat_release_rate`

### Working hypothesis

Regime transitions should cluster near `V ≈ D`.

Predictions:

- `V < D`: intermittent spread, larger variance, fragmented fronts.
- `V ≈ D`: rapid changes in continuity and acceleration, indicating onset of coherence.
- `V > D`: continuous fronts, smoother perimeters, and more stable perimeter-area relations.

Because `V` and `D` are constructed from proxies, the resubmission should explicitly commit to evaluating multiple formulations and conducting sensitivity analyses.

## III. From narrative to tests

### A. Decisive hypothesis test (Benchmark 0)

The resubmission should explicitly discriminate between:

- **H1, single-law framing:** a single scaling relation such as `P ~ A^α` holds across conditions.
- **H2, multi-regime framing:** scaling and geometry change across regimes, with transitions governed by transport constraints.

Test design:

- compare single-law against piecewise or regime-based models using information criteria such as AIC and BIC;
- use cross-validation to test predictive robustness; and
- evaluate whether change points in geometry or continuity align with transitions in `V / D`.

Deliverable:

- a model-selection report and decisive figure showing whether observed fire behavior is better represented by a single regime or multiple regimes.

### B. Observable quantities

From FIRED and auxiliary datasets, estimate:

- perimeter `P(t)` and area `A(t)`;
- scaling relation `P ~ A^α`;
- time-varying exponent `α(t)`;
- local spread rates along the head and flanks;
- continuity metrics such as connected-front fraction, gap frequency, and filamentation;
- boundary curvature and roughness; and
- meteorological drivers such as `U`, `H`, and stability proxies.

Derived quantities include:

- variance and intermittency metrics; and
- `V`, `D`, and their ratio `V / D`.

### C. Regime classification as a product

Develop a reproducible, uncertainty-aware regime classifier that labels fire states as pre-emergent, transition, or post-emergent using:

- continuity metrics such as connected-front fraction;
- stability and change in `α(t)`; and
- thresholds or transition behavior in `V / D` proxies.

Deliverable:

- versioned regime-classification datasets and code applicable to both observations and model outputs.

### D. Tests of the ventilation boundary

Test whether observed regime transitions align with `V ≈ D` by:

- computing `V` and `D` proxies through time for each fire;
- detecting change points in geometry and continuity, including Bayesian change-point detection where useful; and
- evaluating temporal alignment between observed transitions and crossings of `V / D ≈ 1`.

Evaluation metrics:

- precision and recall of transition detection;
- temporal offset between `V / D` crossing and observed transition; and
- sensitivity to proxy definitions.

### E. Model experiments as falsifiable contrasts

#### 1. Wave-model experiments

- Sweep parameters over `U`, `H`, `C`, and fuel parameters.
- Output continuity, `α(t)`, and transition timing.
- Test whether the model reproduces observed regime transitions and their dependence on `V / D`.

#### 2. Geometric / manifold model experiments

- Initialize coherent fronts and evolve boundary-driven growth.
- Test whether the reduced model reproduces post-emergent scaling and geometry without detailed local ignition physics.

Falsifiable claim:

- If post-emergent behavior is geometry-dominated, a reduced geometric model should reproduce observed scaling independently of local ignition detail within stated uncertainty.

#### 3. Cross-model comparison

- Identify conditions under which both models agree in the post-emergent regime.
- Identify conditions under which local spread physics remains necessary in the pre-emergent and transition regimes.

### F. Benchmarking against existing models

Apply the same diagnostics to existing model outputs to ask:

- do current models reproduce regime transitions;
- do they predict continuous fronts when `V < D`, producing false positives; and
- do they miss transitions when `V > D`, producing false negatives.

Deliverable:

- a reusable benchmark suite for evaluating any fire model against regime transitions and geometry diagnostics.

## IV. Reviewer critiques mapped to actions

| Reviewer concern | Action in resubmission |
| --- | --- |
| Scaling and data limitations | Estimate `α(t)`, compare piecewise and single-law fits, and quantify sensitivity to temporal resolution, suppression, and detection limits. |
| Meteorology underdeveloped | Incorporate `U`, `H`, and stability proxies directly into `V` and test predictive power for regime transitions. |
| Validation unclear | Define success in terms of correct regime labels, transition timing, and post-emergent geometry rather than final area alone. |
| Technical implementation too conceptual | Implement a modular pipeline: data ingestion → feature extraction → regime classification → model experiments → benchmarking. |
| Differentiation from existing models weak | Provide diagnostics that evaluate existing models rather than claiming to replace them outright. |
| Feasibility concerns | Organize Years 1-2 as parallel workstreams with independently evaluable deliverables. |
| Broader impacts underspecified | Release datasets, code, dashboards, and tutorials through ESIIL / OASIS-aligned channels. |

## V. Resulting position

The resubmission should present a testable framework for when and why wildfire transitions between growth regimes, grounded in transport constraints and evaluated with explicit benchmarks.

Key product-oriented outputs:

- regime classification system with uncertainty for observations and model outputs;
- `V / D` proxy datasets linking meteorology and fuels to fire behavior; and
- benchmark suite for evaluating model ability to reproduce regime transitions and extreme behavior.

Conceptual anchor:

- a phase diagram of fire behavior in `(V / D, connectivity)` space that maps fragmented, transitional, and continuous spread.

## VI. Benchmarks, milestones, and deliverables

### Core benchmarks

#### 0. Single-law vs multi-regime discrimination

- **Metric:** AIC / BIC comparison of single-law and regime-based models.
- **Test:** cross-validated fits plus alignment of change points with `V / D`.
- **Deliverable:** decisive figure and report demonstrating whether regime structure is supported.

#### 1. Regime detection accuracy

- **Metric:** precision, recall, and F1 score against independently derived continuity transitions.
- **Test:** cross-validation plus uncertainty quantification.
- **Deliverable:** versioned regime labels and evaluation report.

#### 2. Ventilation-demand boundary validity

- **Metric:** hit rate and time offset for alignment between `V / D ≈ 1` and observed transitions.
- **Test:** bootstrap and sensitivity analyses across proxy definitions.
- **Deliverable:** `V / D` datasets, code, and validation figures.

#### 3. Geometry and scaling in post-emergent fires

- **Metric:** stability of `α(t)`, cross-fire distributions, and boundary roughness statistics.
- **Test:** piecewise vs single-law fits plus robustness to sampling resolution.
- **Deliverable:** `α(t)` time series, summary tables, and methods notebook.

#### 4. Model fidelity to regimes

- **Metric:** accuracy of transition timing, continuity metrics, and post-emergent geometry.
- **Test:** side-by-side diagnostics comparing observations with wave and geometric models.
- **Deliverable:** standardized benchmark suite.

#### 5. Discrimination versus existing models

- **Metric:** false positive and false negative rates for continuity under `V < D` and `V > D`.
- **Test:** apply the diagnostics to available model outputs.
- **Deliverable:** comparative evaluation report and reusable toolkit.

### Milestones and work plan

#### Year 1 — Measurement and labeling

- Build feature extraction for `P(t)`, `A(t)`, `α(t)`, continuity, and curvature.
- Implement initial `V` and `D` proxies plus a sensitivity-analysis plan.
- Develop regime classifier and change-point detection.

Outputs:

- v1 features dataset;
- v1 regime labels; and
- preliminary `V / D` time series.

#### Year 2 — Testing and model experiments

- Validate regime labels and refine `V / D` definitions.
- Conduct wave-model parameter sweeps and compute diagnostics.
- Quantify alignment of observed transitions with the `V / D` boundary.

Outputs:

- validated regime dataset v2;
- experiment library; and
- transition-alignment report.

#### Year 3 — Geometry, benchmarking, and release

- Validate the geometric model in the post-emergent regime.
- Assemble and apply the cross-model benchmark suite.
- Package datasets, code, and dashboards for public use through ESIIL / OASIS pathways.

Outputs:

- benchmark suite;
- comparative evaluation report; and
- public releases for data, code, and documentation.

### Deliverables as artifacts

- reproducible pipeline from raw data to features, regimes, and benchmarks;
- versioned datasets for features, `α(t)`, regime labels, and `V / D` proxies;
- model experiment library with standardized diagnostics;
- benchmark suite for evaluating any fire model; and
- public documentation and example notebooks.

Each project year should yield independently evaluable artifacts so progress remains cumulative and auditable.

## VII. Data, methods, and reproducibility

### Data sources

- **FIRED event time series:** reconstructed wildfire perimeters through time derived from satellite observations, supporting all geometry and scaling analyses.
- **Meteorology from reanalysis and stations:** wind speed, boundary-layer height, and stability-related diagnostics for transport proxies, with station data used where available for local validation.
- **Fuels from LANDFIRE or equivalent products:** amount and type of burnable material used to estimate combustion demand.

### Quality control and uncertainty

- **Perimeter uncertainty:** quantify uncertainty in boundary location and propagate it into perimeter, area, and exponent estimates.
- **Temporal sampling limits:** test how observation frequency affects inferred growth rates and scaling relationships.
- **Regime classification uncertainty:** assign probabilities rather than hard labels near regime transitions.
- **Sensitivity analyses:** test multiple `V` and `D` formulations and report how conclusions depend on those choices.

### Reproducibility commitments

- fully scripted pipeline from raw data to figures;
- versioned processed datasets;
- controlled computational environments; and
- public notebooks for key figures and statistics.

## VIII. Risks and mitigations

### Risk: `V` and `D` proxies are too noisy to align with transitions

- Possible cause: atmospheric or fuel data are too coarse to capture the relevant processes.
- Mitigation: test multiple proxy families, aggregate over time windows, and use ensemble estimates rather than relying on a single formulation.

### Risk: regime boundaries are not sharp

- Possible cause: fire behavior changes continuously rather than through clear change points.
- Mitigation: use probabilistic classification and continuous metrics instead of forcing binary categories.

### Risk: geometric model fails in the post-emergent regime

- Possible cause: local physics still matters even after coherence emerges.
- Mitigation: refine boundary dynamics with anisotropy or curvature-dependent terms and treat failure as a scientific result that narrows the model's valid scope.

### Risk: limited access to external model outputs

- Possible cause: comparison models are difficult to obtain or standardize.
- Mitigation: design benchmarks that require minimal inputs such as perimeter time series and pursue targeted collaborations where needed.

## IX. Governance and roles

- **Empirical lead (Postdoc 1):** data ingestion, feature extraction, regime labeling, and uncertainty quantification.
- **Modeling lead (Postdoc 2):** wave simulations, geometric model development, parameter sweeps, and comparable diagnostics.
- **PI / Co-PIs:** integration across empirical and modeling results, benchmark design, meteorology-fuels interpretation, and external model comparisons.

Parallel workstreams are meant to ensure that delays in one component do not halt overall progress.

## X. Figures and outputs

### Planned core figures

1. Decisive test: single-law versus multi-regime behavior.
2. Phase diagram in `(V / D, connectivity)` space with observed fire trajectories.
3. Regime-classification example time series with uncertainty.
4. Transition-alignment figure comparing `V / D` crossings with detected change points.
5. Model-comparison panel contrasting observations, wave-model outputs, and geometric-model outputs across regimes.

### Public outputs

- versioned datasets for features, `α(t)`, regimes, and `V / D`;
- benchmark suite with scripts and expected outputs; and
- documentation and tutorials integrated with the project website and OASIS-facing materials.

## XI. Acceptance criteria

The framework is supported if:

- evidence favors multi-regime over single-law models in a majority of tested fires;
- regime transitions align with `V / D` within a defined temporal tolerance across datasets;
- post-emergent geometry is reproducible by a reduced geometric model within uncertainty bounds; and
- the benchmark suite meaningfully differentiates model performance on regime transitions and extreme behavior.

If any of these criteria are not met, the result is still informative and should be reported as evidence about which assumptions fail and how the framework should be revised.
