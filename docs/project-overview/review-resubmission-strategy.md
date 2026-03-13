# First-Submission Review Summary and Resubmission Strategy

This page summarizes internal notes from the first FIRE-MODEL proposal review cycle and captures the resulting resubmission strategy.

> Status note: this is an internal planning synthesis, not sponsor-issued guidance. Use this page with the solicitation and checklist materials under [Funder Materials](funder-materials.md).

## High-level interpretation

Reviewer feedback was directionally positive about the conceptual core, but raised concerns about execution clarity.

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
| 2/3 scaling could be a sampling artifact | Reframe scaling as a hypothesis and test it across sensors/temporal resolutions. |
| Meteorology is missing | Introduce wind/humidity/VPD as external forcing terms. |
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

## Source file in repository

- `background_context/program_briefings/fire_model_first_submission_review_resubmission_strategy.md`
