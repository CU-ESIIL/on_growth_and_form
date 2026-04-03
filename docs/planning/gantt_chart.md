# FIRE-MODEL Work Plan

## Overview

This figure summarizes the FIRE-MODEL project as a coordinated Detect -> Explain -> Apply program over 36 months. It links team roles, shared diagnostics, model comparison, and application-oriented release work in one timeline.

---

## Gantt Chart

![FIRE-MODEL Gantt Chart](../assets/figures/fire_model_gantt_ESIIL_minimal.svg)

---

## Figure Legend

This Gantt chart represents the FIRE-MODEL project across time, scientific logic, and role ownership.

**Time (x-axis)**  
The horizontal axis shows project months over three years:
- Year 1 = Detect
- Year 2 = Explain
- Year 3 = Apply

**Rows (y-axis)**  
Each row represents a major component of the project, grouped into high-level phases:
- Team and workflow setup
- Empirical data and diagnostics
- Generative modeling
- Integration and evaluation
- Outputs and dissemination

**Background shading (half-year emphasis)**  
The background colors indicate the dominant emphasis in each six-month block:
- Detect foundations
- Detect diagnostics
- Explain model build
- Explain mechanisms
- Apply prediction
- Apply release

**Bar colors (roles)**  
Each bar is colored by responsibility:
- Principal Investigator (Ty Tuff, CU Boulder / ESIIL)
- Postdoctoral Researcher (Modeling Lead; TBD)
- Empirical Lead (Nayani Ilangakoon, CU Boulder/Earth Lab)
- Co-Investigator (Cibele Amaral, CU Boulder / ESIIL)
- Infrastructure Lead (TBD ESIIL software engineer)
- Science Communication and Design Lead (Impact Media Lab - subcontractor)

**Bar length and position**  
Bar length indicates duration of effort. Position shows when each activity occurs relative to others.

---

## How to Interpret This Figure

The figure should be read from left to right as an overlapping scientific workflow:

1. **Detect (Year 1):** FIRED/GOFER/FEDS harmonization, unified time-resolved event data, extraction of `A(t)` and `P(t)`, estimation of `sigma = d(log P)/d(log A)`, transition detection, sensitivity checks, and cross-dataset validation.
2. **Explain (Year 2):** harmonization of competing models (`M0-M3`), regime-aware model assignment, shared diagnostic evaluation using `A(t)`, `P(t)`, and `sigma`, structural and dynamical comparison, mechanism discrimination, and reproducible benchmark generation.
3. **Apply (Year 3):** reduced geometry-constrained modeling, transition-aware gating, `beta(t)` integration, trajectory prediction and comparative gain analysis, operationalization, Fire Dynamics Explorer integration, public release, and synthesis products.

Key logic represented in the overlap:
- Workstreams overlap by design.
- Detection informs model assignment.
- Model comparison identifies required mechanisms.
- Application integrates these constraints into a predictive system.
- Validation, reproducibility, documentation, and communication continue across years.

---

## Why This Matters

This framework provides:

- A consistent workflow for wildfire event diagnostics
- A testable mechanism-discrimination program in Year 2
- A transition-aware predictive system in Year 3
- Reusable public code, data, workflows, and communication products

The Gantt chart makes explicit how these outcomes are achieved through coordinated empirical, theoretical, and computational work.
