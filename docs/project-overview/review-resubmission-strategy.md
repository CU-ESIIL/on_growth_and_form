# First-Submission Review Summary and Resubmission Strategy

This page summarizes the strategic implications of the first FIRE-MODEL review cycle for the next submission.

> Status note: this is an internal strategy synthesis, not sponsor-issued guidance. Use it alongside the solicitation and checklist materials under [Funder Materials](funder-materials.md).

## Why this document is strategic, not just background

The first-round reviews are not merely contextual notes. They directly shape how the next proposal should be framed, scoped, validated, and justified. In repository terms, that makes them part of proposal strategy.

The primary working memo now lives in:

- `proposal/narrative/fire_model_resubmission_strategy.md`

That placement reflects its role in guiding the next draft of the proposal narrative and associated supporting documents.

## High-level interpretation

Reviewer feedback was directionally positive about the conceptual core, but raised concerns about execution clarity and research-plan credibility.

### Strengths reviewers emphasized

- Conceptual novelty and potentially transformative framing.
- Strong empirical motivation from satellite fire records.
- Compelling integration of geometry and fire dynamics.

### Concerns requiring direct proposal revisions

- Technical implementation detail needs to be more explicit.
- Satellite temporal sampling limits need direct treatment.
- Meteorological forcing must be integrated clearly.
- Validation metrics and evaluation pathways must be concrete.
- Work scope should be mapped more clearly to budget and staffing.

## Concern-to-strategy summary

| Concern | Resubmission action |
| --- | --- |
| 2/3 scaling could be a sampling artifact | Reframe scaling as a hypothesis and test it across sensors and temporal resolutions. |
| Meteorology is missing | Introduce wind, humidity, and VPD as external forcing terms. |
| Methods are too conceptual | Add algorithm blocks, pseudo-code, and architecture diagrams. |
| Validation is unclear | Define explicit perimeter, spread-rate, and geometry metrics. |
| Stage-of-fire applicability is ambiguous | State targeted fire-growth regimes and explicit out-of-scope regimes. |
| Timeline depends on hiring | Add contingency paths and modular task sequencing. |
| Scope vs budget is unclear | Expand work-package detail and technical workload justification. |

## Structural edits prioritized for the next draft

1. **Hypothesis framing:** present scaling as falsifiable, not settled.
2. **Meteorological coupling:** treat environment as external forcing on internal propagation.
3. **Algorithmic specificity:** make model operations and state updates explicit.
4. **Validation framework:** include metrics, thresholds, and cross-case tests.
5. **Work-package clarity:** describe deliverables, dependencies, and effort by task.

## Strategic narrative shift

- From: *"we discovered the law and now reproduce it."*
- To: *"we observed a candidate law and will test whether it is intrinsic dynamics or observational artifact."*

This shift is intended to improve reviewer confidence in scientific rigor.

## Repository source files

- Strategic memo: `proposal/narrative/fire_model_resubmission_strategy.md`
- Earlier contextual synthesis retained for history: `background_context/program_briefings/fire_model_first_submission_review_resubmission_strategy.md`
