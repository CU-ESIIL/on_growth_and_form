# Evaluation and Success Criteria

## Overview

This project is evaluated on both the correctness of the system and the significance of its contributions. Evaluation therefore spans internal validation, asking whether the system works and produces reliable results, and external impact, asking whether the project advances wildfire science and changes how modeling is conducted.

Early indicators of impact, including code reuse, collaborations, workshop invitations, and community engagement, are expected within the project period, while broader conceptual adoption will be assessed in the years following completion.

This project is designed not only to produce new scientific results, but to change how wildfire modeling is conducted. Evaluation must therefore operate at multiple levels: the reliability of the system, the validity of scientific conclusions, advancement beyond existing approaches, and development of the research team.

We evaluate success across five domains: scientific discovery, technical system performance, comparative advancement relative to the field, training and workforce development, and field-level impact. Each domain includes explicit success criteria, tracking mechanisms, judgment standards, and reporting strategies.

## 1. Scientific success

### What success looks like

The project is successful if it reduces the space of plausible wildfire mechanisms and identifies at least one mechanism that is consistent with all observed constraints, including scaling, geometry, dynamics, anisotropy, and environmental coupling. Success also includes explicit rejection of alternative mechanisms.

High-level outcomes include:

- a finite, well-defined set of viable mechanisms
- explicit statements of rejected mechanisms
- a coherent explanation of wildfire growth grounded in multiple independent lines of evidence

### How we track it

- number of mechanisms evaluated versus eliminated
- consistency of surviving mechanisms across datasets
- stability of results under perturbation and uncertainty

### How we judge it

- a mechanism must pass all evaluation tests simultaneously
- failure in any critical test results in rejection
- mechanisms must remain valid across fire regimes and datasets

### How we report it

- synthesis papers explicitly listing accepted and rejected mechanisms
- clear visualizations showing constraint satisfaction across dimensions
- transparent reporting of uncertainty and ambiguity

## 2. Technical success

### What success looks like

Technical success means a fully operational end-to-end pipeline from raw data to mechanism identification, with all major components implemented and integrated:

- measurement system, including Dataset v1 and v2
- comparison engine
- model library
- validation framework

### How we track it

- completion of named milestones such as Dataset v1 and Comparison Engine v1
- successful execution of full pipeline runs on multiple datasets
- reproducibility of results across environments

### How we judge it

- pipeline runs without failure on real datasets
- outputs are consistent under repeated runs
- all components interface correctly without manual intervention

### How we report it

- publicly available code and workflows
- reproducible notebooks and pipeline documentation
- versioned releases of datasets and models

## 3. Comparative success

### What success looks like

The project demonstrates clear advancement over current fire modeling approaches in at least one of the following ways:

- it explains patterns that existing models cannot
- it rejects mechanisms currently assumed valid
- it produces more stable and consistent results across datasets
- it provides mechanism-level understanding rather than descriptive fits

### How we track it

- side-by-side comparisons with existing models
- evaluation of model performance across multiple metrics
- consistency of results across independent datasets

### How we judge it

- demonstrated improvement in explanatory power or consistency
- evidence that current approaches fail tests that the new system passes
- at least one clear case in which existing models fail to reproduce observed patterns that this framework successfully explains

### How we report it

- comparative analysis sections in manuscripts
- benchmarking studies against existing models
- clear statements of improvement and limitation

## 4. Training and workforce development success

### What success looks like

Each postdoc develops into an independent researcher capable of leading interdisciplinary projects. Indicators include:

- first-author publications in Years 1 and 2
- annual conference presentations
- ownership of major project components
- a clear research identity
- successful placement in research or academic positions

### How we track it

- publication record and authorship roles
- conference participation and presentation type
- progress in leading project components
- career progression and job placement

### How we judge it

- achievement of publication and presentation milestones
- demonstrated independence in research design and execution
- competitiveness in the job market

### How we report it

- annual progress reports including trainee outcomes
- documentation of publications and presentations
- post-project placement tracking

## 5. Field-level impact

### What success looks like

The project begins to influence how wildfire modeling is conceptualized and practiced.

Indicators include:

- adoption of measurement or comparison methods by other groups
- citations and use of datasets or code
- integration of concepts such as scaling and interface dynamics into broader literature
- invitations to speak at conferences and workshops

### How we track it

- citation counts and code repository usage
- requests for collaboration or data access
- references to project methods in other studies

### How we judge it

- evidence that methods are being reused or adapted
- uptake of concepts beyond the immediate project

### How we report it

- citation and usage metrics
- case studies of external adoption
- broader impact sections in final reports

## Final success statement

The project is considered successful if it produces a reproducible system that reduces the space of plausible wildfire mechanisms, identifies at least one mechanism consistent with all observed constraints, demonstrates explanatory power beyond existing approaches, and contributes to the development of independent researchers and broader adoption within the field. Together, these outcomes establish a new standard for mechanism-based wildfire modeling.

All evaluation results, including negative and inconclusive findings, will be reported transparently to ensure scientific integrity and to clarify the limits of current approaches.

Failure will be defined by inability to distinguish mechanisms within uncertainty, lack of stability under perturbation, or failure to generalize across datasets. These outcomes will also be reported transparently, because they provide important insight into the limits of current approaches.

This evaluation framework ensures that success is not defined by producing results alone, but by producing results that are reliable, meaningful, and influential.
