# NSF FIRE-MODEL First-Submission Review Summary and Resubmission Strategy

## Status and provenance

This document captures reviewer and panel feedback from the first FIRE-MODEL submission and translates that feedback into concrete revision actions for the next proposal cycle. It is an internal synthesis artifact in `background_context/`, not an NSF-issued document.

Because this is a reviewer-summary memo rather than a solicitation requirement document, all final proposal choices should still be checked against official FIRE and PAPPG guidance in `funder/`.

## Purpose

The goal is to convert strong conceptual reception into stronger confidence in technical execution, feasibility, and validation.

Core interpretation from the reviews:

- the conceptual novelty was viewed positively;
- confidence was reduced by unclear implementation detail, validation plans, treatment of meteorology, and handling of sensor limitations.

## Executive summary of panel outcome

### Strengths reviewers identified

- Novel conceptual framework for wildfire dynamics.
- Potentially transformative perspective on fire growth.
- Strong empirical motivation based on global satellite fire records.
- Compelling integration of geometric and dynamical thinking.

### Primary concerns reviewers raised

- Insufficient implementation detail for model construction and computation.
- Limited treatment of satellite temporal sampling limitations.
- Missing explicit treatment of meteorological drivers.
- Validation pathway and metrics not sufficiently concrete.
- Scope and work volume not clearly mapped to requested budget.

Working interpretation: reviewers liked the idea but lacked confidence in execution clarity.

## Reviewer concern-to-action table

| Reviewer concern | What reviewers likely meant | Resubmission strategy |
| --- | --- | --- |
| Satellite-derived 2/3 scaling may be biased by sampling | MODIS/VIIRS revisit intervals can miss fast spread dynamics and distort inferred scaling exponents | Explicitly discuss sampling limits. Add an objective that tests robustness with higher-frequency and complementary data (e.g., GOES, VIIRS active fire streams, perimeter products). Frame 2/3 scaling as a hypothesis to test, not an assumed law. |
| Meteorological drivers missing | Wind, humidity, and atmospheric state strongly influence spread; omission suggested an incomplete process model | Introduce meteorology as external forcing in the modeling architecture. Use wind, humidity, and VPD as boundary/forcing terms while preserving focus on internal fire propagation dynamics. |
| Insufficient technical detail | Conceptual framing was stronger than algorithmic specificity | Add explicit algorithm descriptions, pseudo-code, and architecture figures. Clarify update rules, ignition-probability logic, and manifold reconstruction workflow. |
| Validation plan unclear | Reviewers did not see how first-principles modeling would be tested against observed fires | Add explicit metrics and a case-study validation matrix: perimeter similarity, spread-rate errors, geometry metrics, and cross-case validation plans. |
| Stage-of-fire applicability unclear | Intended regime (ignition, early spread, extreme growth, full lifecycle) was ambiguous | Define model applicability explicitly, such as mesoscale expansion after ignition networks emerge, and delimit what is out of scope. |
| Dependence on postdoc hiring | Timeline risk if recruitment is delayed | Add contingency language and modular sequencing so PI/collaborators can initiate core tasks before full hiring completion. |
| Scope relative to budget unclear | Workload-to-budget linkage was not legible | Expand task detail, simulation campaigns, data engineering work, and validation effort to make budget justification auditable. |
| Comparisons to existing models insufficient | Distinctions from FARSITE/WRF-Fire-like paradigms were underdeveloped | Add a dedicated comparison subsection: assumptions, strengths, limitations, and specific behaviors better captured by the proposed framework. |
| Mechanistic link between metabolism and fire unclear | Metabolic framing read as analogy rather than mechanism | Strengthen mechanistic argument around transport networks, combustion coupling, and thermodynamic constraints. |
| Broader impacts metrics vague | Outreach plans lacked measurable outcomes | Define concrete metrics (participation, adoption, user studies, feedback instruments, documented use cases). |
| Diversity recruitment strategy vague | Inclusion goals lacked implementation pathways | Name recruitment partners and mechanisms (e.g., tribal colleges, agencies, minority-serving institutions, targeted outreach channels). |

## Recommended structural revisions

### 1) Reframe scaling as a testable hypothesis

Shift from "we discovered the law" to "we observed a candidate scaling relation that requires rigorous multi-sensor testing." This aligns with reviewer concerns about observational artifacts and with NSF preference for falsifiable framing.

### 2) Integrate meteorology as forcing, not replacement theory

Use a multiplicative or coupled structure where environmental forcing modulates internal propagation dynamics. This addresses omitted drivers while preserving the core conceptual contribution.

### 3) Make algorithms explicit

Add concise algorithm blocks for both the wave-propagation model and manifold reconstruction pipeline, including state variables, update rules, and outputs.

### 4) Add quantitative validation framework

Define metrics and decision thresholds up front (e.g., Hausdorff distance, Jaccard overlap, spread-rate error, curvature distributions, topology-aware similarity) and connect each metric to model claims.

### 5) Expand work packages and execution detail

Use task-level work packages that make sequence, dependencies, and deliverables transparent:

1. scaling robustness tests,
2. wave-model implementation,
3. meteorological coupling,
4. manifold reconstruction,
5. validation across case studies,
6. community platform release and documentation.

## Strategic narrative adjustment

Preferred framing for the resubmission:

- From: "We discovered the scaling law and built a model to reproduce it."
- To: "We identified a candidate scaling relation and propose a falsifiable program to test whether it reflects intrinsic fire dynamics versus observational limitations."

This repositioning improves scientific credibility and aligns with panel expectations for rigor.

## Bottom line checklist for rewrite priorities

1. Address satellite sampling limitations directly.
2. Add meteorological forcing in model formulation.
3. Increase technical and algorithmic specificity.
4. Define explicit quantitative validation metrics.
5. Expand and clarify work package scope relative to budget.

## Assumptions and open items

- This summary assumes the reviewer notes provided are complete and representative of panel concerns.
- Before final drafting, map each strategy item to explicit FIRE and PAPPG compliance locations (Project Description sections, Broader Impacts plan, Management Plan language, and Budget Justification).
- If official panel summaries include additional compliance comments (e.g., data management, postdoc mentoring, risk management), add those as separate actionable items.
