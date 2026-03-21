# FIRE-MODEL Staffing Plan: Roles, 3-Year Timeline, Milestones, and Deliverables

## Overview

This document defines three positions for the FIRE-MODEL project: two postdoctoral scholars and the Principal Investigator. It aligns each role to Methods 1, 1B, 1C, 2, and 3, specifies a 3-year timeline, annual conference outputs, first-author paper expectations, named milestones, and concrete deliverables.

The project operates as an iterative measurement-model-validation loop: measurement defines constraints, modeling tests mechanisms against those constraints, and validation ensures that conclusions are reliable. Progress in each role depends directly on outputs from the other, creating a tightly coupled system in which discrepancies drive refinement until only mechanisms consistent with all constraints remain.

Integration cadence: the team will meet weekly to review discrepancies between measurement and model outputs and coordinate next steps. Quarterly milestone reviews will assess progress against named deliverables, including Dataset v1, Comparison Engine v1, Model Library v1, and Validation Framework v1, and will adjust priorities as needed.

Early progress targets for Month 6 are a preliminary Dataset v0 with `P(t)`, `A(t)`, `dA/dt`, and initial geometry on a subset of fires; prototype comparison metrics such as EMD, KS, DTW, and RMSE operating on Dataset v0; and an initial end-to-end pipeline run from data to metrics to comparison demonstrating feasibility.

Risk mitigation is built into the modular structure. Delays in one component do not halt progress in others, because measurement, modeling, and validation can advance in parallel while the iterative loop enables rapid identification and correction of errors or mismatches.

## Canonical milestones

- Dataset v1, end of Year 1: validated multi-fire dataset with `P(t)`, `A(t)`, `dA/dt`, `beta`, geometry, anisotropy, and initial coupling
- Comparison Engine v1, end of Year 1: working multi-objective scoring and Pareto ranking
- Model Library v1, mid-Year 2: initial set of generative mechanisms with ensemble outputs
- Validation Framework v1, end of Year 2: uncertainty, sensitivity, and identifiability implemented
- Final Mechanism Synthesis, end of Year 3: integrated results and ranked mechanisms

## Position 1: Postdoc, Computational Geospatial Scientist

This postdoc is an expert in geospatial data science who treats measurement as a scientific problem. They are fluent in Python-based geospatial stacks such as `xarray`, `rasterio`, and `geopandas`, comfortable with large spatiotemporal datasets, and experienced in remote sensing or related domains. They bring rigor in data cleaning, spatial alignment, uncertainty quantification, and reproducible pipelines, and are motivated to define how wildfire dynamics are measured in the next generation of fire science.

### Year 1: Build the measurement system

Targets: Dataset v1.

- Ingest and standardize multi-source fire perimeter datasets
- Implement CubeDynamics pipelines for `P(t)`, `A(t)`, and `dA/dt`
- Estimate scaling exponent `beta` with confidence intervals
- Compute geometry, including fractal dimension and perimeter-area scaling
- Implement anisotropy metrics
- Implement FireVase coupling by attaching meteorology to the boundary
- Produce a validated multi-fire dataset with all observables as Dataset v1

Conference output: "Measurement of Fire as a Dynamic Interface: Scaling, Geometry, and Coupling"

Completed by conference: Dataset v1 plus initial scaling and geometry results.

Lead paper: submit by end of Year 1 on the measurement framework and velocity critique.

### Year 2: Stress-test and expand measurement

Targets: uncertainty envelopes.

- Implement velocity comparison across definitions and resolutions
- Quantify scale dependence and formally reject velocity
- Build the perturbation framework for resolution, sampling, and boundary extraction
- Recompute observables under perturbations and quantify uncertainty envelopes
- Expand the dataset to additional regions and regimes and update Dataset v2

Conference output: "Uncertainty and Scale in Fire Measurement: Why Velocity Fails"

Completed by conference: uncertainty characterization and velocity results.

### Year 3: Finalize data system and integrate

Targets: production pipelines.

- Finalize the fire-environment coupled dataset, including FireVase outputs
- Optimize pipelines with Dask and HPC workflows
- Produce publication-quality diagnostics and visualizations
- Support integration with modeling, validation, and final synthesis

Conference output: "A Unified Measurement System for Wildfire Dynamics"

Completed by conference: full dataset plus coupling and uncertainty framework.

### Deliverables

- Clean, standardized fire perimeter time-series dataset, including Dataset v1 and v2
- Derived observables: `P(t)`, `A(t)`, `dA/dt`, `beta`, geometry, and anisotropy
- Fire-environment coupled dataset through FireVase
- Velocity critique across multiple definitions and scales
- Measurement uncertainty framework with perturbation analysis and envelopes
- Reproducible CubeDynamics pipelines ready for HPC use
- First-author paper in Year 1 plus co-authorship on synthesis papers

Career outcome: leader in geospatial measurement of fire dynamics and uncertainty-aware spatial analytics.

## Position 2: Postdoc, Complex Systems Modeler

This postdoc is trained in applied mathematics, physics, or complex systems and focuses on mechanisms that generate patterns. They are comfortable with stochastic processes, scaling laws, and dynamical systems, and can translate theory into simulation and testable predictions. They bring expertise in model design, multi-objective comparison, and rigorous validation including sensitivity, identifiability, and cross-validation, and are motivated to build systems that can eliminate incorrect theories of wildfire spread.

### Year 1: Build the decision and modeling core

Targets: Comparison Engine v1.

- Implement comparison metrics including EMD, KS, DTW, and RMSE
- Formalize scaling, geometry, and mechanistic constraints
- Build multi-objective scoring and Pareto ranking as Comparison Engine v1
- Implement initial generative models for interface, network, and stochastic processes
- Ensure simulation outputs align with measurement pipeline inputs

Conference output: "A Multi-Objective Framework for Evaluating Fire Mechanisms"

Completed by conference: Comparison Engine v1 and prototype models.

Lead paper: submit by end of Year 1 on the comparison framework and decision logic.

### Year 2: Expand models and run experiments

Targets: Model Library v1 and Validation Framework v1.

- Develop the full library of generative models as Model Library v1
- Run ensemble simulations for each mechanism
- Execute parameter sweeps across plausible ranges
- Compute model-data comparisons across all metrics
- Begin sensitivity analysis with Morris screening and assemble Validation Framework v1

Conference output: "Testing Competing Mechanisms of Wildfire Spread"

Completed by conference: ensemble results, parameter sweeps, and initial sensitivity analyses.

### Year 3: Validation, identifiability, and synthesis

Targets: Final Mechanism Synthesis.

- Perform Sobol variance decomposition
- Implement identifiability analysis comparing model separation to uncertainty
- Conduct life-stage or regime consistency analysis
- Run cross-validation on held-out fires
- Integrate results into final mechanism ranking as Final Mechanism Synthesis

Conference output: "Identifying Mechanisms of Wildfire Growth Under Multiple Constraints"

Completed by conference: full validation and final rankings.

### Deliverables

- Fully implemented comparison framework corresponding to Method 1C and Comparison Engine v1
- Multi-objective scoring and Pareto ranking system
- Library of generative fire models as Model Library v1
- Simulation engine and ensemble outputs
- Sensitivity analysis through Morris and Sobol methods
- Identifiability and uncertainty analysis as Validation Framework v1
- Cross-validation results and final mechanism selection
- First-author paper in Year 1 plus co-authorship on synthesis papers

Career outcome: leader in mechanism-based modeling and inference for complex environmental systems.

## Position 3: Principal Investigator

The Principal Investigator leads the scientific vision and integrates measurement and modeling into a coherent discovery system. The PI is uniquely responsible for translating between empirical measurement, theoretical modeling, and system-level interpretation, including scaling, interface dynamics, and coupling. The PI also manages hiring, budget, reporting, collaborations, and ensures alignment with proposal goals.

### Year 1: Setup and alignment

Targets: Dataset v1 and Comparison Engine v1.

- Recruit and hire postdocs through ads, interviews, and onboarding
- Establish repository structure, coding standards, and CI workflows
- Define milestones, success metrics, and communication cadence
- Guide early measurement and comparison development
- Frame the synthesis of fire as an interface and scaling system

Conference output: "Fire as a Scaling Interface: A New Framework for Modeling"

Completed by conference: conceptual framing plus early outputs, especially Dataset v1 and Comparison Engine v1.

### Year 2: Integration and iteration

Targets: Model Library v1 and Validation Framework v1.

- Coordinate the measurement-model-validation loop
- Resolve mismatches among data, models, and metrics
- Guide the expansion of models and datasets
- Lead cross-cutting analyses of scaling, coupling, and dimensionality
- Initiate synthesis manuscripts

Conference output: "Integrating Measurement and Mechanism in Wildfire Science"

Completed by conference: integrated results across methods.

### Year 3: Synthesis and dissemination

Targets: Final Mechanism Synthesis.

- Lead final synthesis across all components
- Write high-impact manuscripts on mechanism identification and theory
- Connect results to applications in prediction, management, and digital twins
- Coordinate final reporting and deliverables

Conference output: "Mechanisms of Wildfire Growth: A Constraint-Based Discovery Framework"

Completed by conference: full synthesis and final results.

### Deliverables

- Hiring and team formation with budget and reporting compliance
- Integrated methods system spanning measurement, modeling, and validation
- Cross-cutting synthesis papers on theory and mechanism
- Stakeholder engagement and dissemination
- Final framework for mechanism-based wildfire modeling

## Summary

Together, these roles form a tightly coupled system:

- Postdoc 1 defines reality through measurement and data
- Postdoc 2 tests explanations through models and inference
- The PI integrates both into discovery and synthesis

The named milestones, annual conference outputs, and first-author paper expectations ensure early productivity, sustained progress, and a clear path to Final Mechanism Synthesis.
