# FIRE-MODEL Resubmission Strategy from First-Submission Reviews

## Status and purpose

This memo captures reviewer and panel feedback from the previous FIRE-MODEL submission and translates that feedback into proposal-development strategy for the next submission. It belongs in `proposal/narrative/` because it is guiding rewrite priorities, framing choices, work-package design, validation language, and staffing-risk mitigation for the resubmission.

This is an internal strategy document, not sponsor-issued guidance. Final proposal decisions should still be checked against the current solicitation, NSF review criteria, and any submission instructions in `funder/`.

## Core interpretation of the reviews

The reviews indicate that the conceptual core of the proposal was well received, but that reviewers lacked confidence in how the research program would be operationalized and validated.

Working interpretation:

- reviewers responded positively to the conceptual novelty;
- reviewers wanted substantially more confidence in execution detail;
- the resubmission should convert enthusiasm about the idea into confidence in feasibility, rigor, and validation.

## Executive summary of panel outcome

### Strengths noted by reviewers

- Highly novel conceptual framework.
- Potentially transformative perspective on wildfire dynamics.
- Strong empirical motivation from the global satellite fire record.
- Compelling integration of geometric and dynamical modeling.

### Primary concerns raised by reviewers

- Insufficient technical detail about implementation.
- Limited discussion of satellite sampling limitations.
- Lack of explicit meteorological inputs.
- Validation strategy was unclear.
- Scope of work was unclear relative to the proposed budget.

Bottom-line interpretation: reviewers liked the idea but lacked confidence in execution clarity.

## Reviewer feedback summary table

| Reviewer concern | What reviewers meant | Strategy for resubmission |
| --- | --- | --- |
| Satellite-derived 2/3 scaling may be biased by sampling | MODIS and VIIRS revisit intervals can miss rapid fire spread dynamics and may create artifacts in scaling estimates | Explicitly discuss temporal sampling limitations. Add a research objective to test scaling robustness using higher-frequency or complementary data sources such as GOES, VIIRS active fire detections, and reconstructed perimeter products. Frame the scaling relationship as a hypothesis to be tested rather than an assumed truth. |
| Meteorological drivers missing | Wind, humidity, and atmospheric conditions strongly affect fire spread, so excluding them suggested an incomplete process model | Introduce meteorology as external forcing variables rather than internal drivers. Integrate wind fields, humidity, and VPD as boundary conditions or forcing terms within the wave model. Emphasize the interaction between internal fire dynamics and external forcing. |
| Insufficient technical detail | The conceptual framework was clearer than the algorithmic and computational plan | Add explicit algorithm descriptions, pseudo-code blocks, and clearer model architecture diagrams. Specify how the wave model updates nodes, how ignition probabilities are calculated, and how manifolds are reconstructed. |
| Validation plan unclear | Reviewers could not see how a first-principles model would be quantitatively validated against real fires | Introduce explicit validation metrics such as perimeter error, Hausdorff distance, curvature similarity, spread-rate error, and ignition-density comparison. Include cross-validation across case-study fires. |
| Stage of fire applicability unclear | It was not clear whether the model targets ignition, early spread, extreme growth, or full fire lifecycle behavior | Clarify applicability explicitly. For example, target mesoscale fire expansion phases after ignition networks form, rather than ignition physics or suppression modeling. |
| Dependence on postdoc hiring | The project timeline appeared to depend heavily on quickly hiring two specialized postdocs | Add contingency planning. Explain how early development can begin with the PI and collaborators if hiring is delayed, and emphasize modular task structure that allows parallel progress. |
| Scope relative to budget unclear | The technical workload and infrastructure effort were not legible enough to justify the requested funding | Expand the task descriptions for simulations, validation campaigns, data engineering, software infrastructure, and research coordination so the workload is auditable. |
| Comparisons to existing models insufficient | Reviewers wanted a clearer explanation of how this approach improves on existing wildfire models such as FARSITE or WRF-Fire | Add a subsection explicitly comparing modeling paradigms, including reaction-diffusion and operational spread models versus the proposed generative or metabolic framing. Give concrete examples such as perimeter fusion, nonlinear expansion, and jump behavior. |
| Mechanistic link between metabolism and fire unclear | The metabolic framing risked reading as analogy rather than physical mechanism | Expand the mechanistic section to explain energy transport networks, combustion coupling, ignition propagation, and thermodynamic constraints as more than metaphor. |
| Broader impacts metrics vague | Interviews and stakeholder engagement were mentioned, but evaluation criteria were not concrete | Provide measurable broader-impacts metrics such as workshop participation, software adoption, survey instruments, and documented use cases. |
| Diversity recruitment strategy vague | Diversity goals were stated, but recruitment pathways were underspecified | Name specific partner organizations and recruitment pathways, such as tribal colleges, fire-management agencies, minority-serving institutions, and targeted outreach networks. |

## Recommended structural changes to the proposal

### 1. Reframe the scaling discovery

Instead of presenting 2/3 scaling as a fixed empirical result, present it as a testable hypothesis.

Suggested framing:

> Satellite records suggest that fire perimeters may scale with time to the two-thirds power. However, this pattern has not yet been systematically tested across sensors with different temporal resolutions. This project will evaluate whether the observed scaling reflects intrinsic fire dynamics or observational artifacts.

This directly addresses the strongest reviewer criticism and places the proposal on firmer scientific ground.

### 2. Introduce meteorology as boundary forcing

Add a subsection that explains how environmental drivers interact with internal fire dynamics.

A useful conceptual structure is:

- fire spread rate = internal propagation dynamics × environmental forcing.

Environmental forcing variables to name explicitly:

- wind fields;
- vapor pressure deficit;
- relative humidity;
- atmospheric stability.

This resolves the reviewer concern without giving up the proposal's core focus on endogenous fire-growth structure.

### 3. Add explicit model algorithms

Include short technical descriptions or pseudo-code blocks such as the following.

#### Wave model algorithm

1. Represent the landscape as a graph.
2. Assign resistance or conductance weights to edges.
3. Calculate ignition probability using a logistic or related transition function.
4. Update node states at each timestep.
5. Track energy propagation and ignition cascades through time.

#### Manifold reconstruction workflow

1. Extract sequential fire perimeters.
2. Convert them into a spatiotemporal point cloud.
3. Reconstruct a continuous surface through interpolation or related geometric methods.
4. Compute curvature, entropy, directionality, and related geometry diagnostics.

These additions help reviewers see a concrete computational research plan rather than a conceptual theory alone.

### 4. Add a quantitative validation framework

Suggested metric families include the following.

#### Perimeter similarity

- Hausdorff distance;
- Jaccard overlap.

#### Spread dynamics

- radial spread error;
- growth exponent comparison.

#### Geometry

- curvature distribution similarity;
- topological or persistence-based similarity metrics.

These metrics should be connected directly to claims in the proposal so reviewers can see how success or failure will be evaluated.

### 5. Expand the research tasks section

Suggested work packages:

1. **Scaling validation:** test scaling relationships across multiple sensors and temporal resolutions.
2. **Wave model development:** implement metabolic propagation algorithms and resistance-surface dynamics.
3. **Meteorological coupling:** integrate wind and atmospheric drivers as external forcing variables.
4. **Manifold reconstruction:** generate spatiotemporal fire surfaces from perimeter and satellite products.
5. **Model validation:** compare simulations against real fire case studies.
6. **Community platform:** release an open-source toolkit and interactive simulation interface.

## Strategic narrative adjustment

The proposal narrative should shift from:

- "We discovered the scaling law and built a model to reproduce it."

To:

- "We discovered a potential scaling law and propose testing whether it reflects fundamental fire dynamics."

This shift aligns the resubmission more closely with hypothesis-driven science and should improve panel confidence.

## Proposal-development implications

This review memo should inform at least the following proposal components:

- Project Description framing and hypothesis statements;
- research objectives and work packages;
- validation and evaluation subsections;
- staffing and management-plan contingency language;
- budget justification detail;
- broader impacts evaluation plan;
- recruitment and partnership language.

## Open questions and follow-up needs

- Confirm whether the reviewer summary here fully captures all panel concerns from the prior submission materials.
- Map each strategy item to specific sections of the next Project Description and supporting documents.
- Check all resulting proposal text against the current FIRE-MODEL solicitation and NSF guidance in `funder/` before treating any strategic recommendation as final.
