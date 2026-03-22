# FIRE-MODEL Work Plan

## Overview

This figure summarizes the FIRE-MODEL project as a coordinated effort linking people, scientific benchmarks, and deliverables over time. It is designed to show how empirical measurement, generative modeling, and model evaluation are integrated into a single workflow.

---

## Gantt Chart

![FIRE-MODEL Gantt Chart](../assets/figures/fire_model_gantt_ESIIL_minimal.svg)

---

## Figure Legend

This Gantt chart represents the FIRE-MODEL project across three dimensions: time, scientific progress, and team roles.

**Time (x-axis):**
The horizontal axis shows project months over a three-year timeline with quarter boundaries and year-level labels:
- Year 1 - Detect
- Year 2 - Explain
- Year 3 - Apply

**Rows (y-axis):**
Each row represents a major component of the project, grouped into high-level phases:
- Team and workflow setup
- Empirical data and diagnostics
- Generative modeling
- Integration and evaluation
- Outputs and dissemination

**Background shading (quarter emphasis):**
The background colors indicate the dominant emphasis within each six-month block:
- pipeline stability and measurement reliability
- shared observables and the Benchmark 0 gate
- model contrasts and transition testing
- validation and sufficiency mapping
- benchmark packaging and external user testing
- release readiness, transfer, and synthesis

**Bar colors (roles):**
Each bar is colored by responsibility:
- Blue: Principal Investigator (integration, evaluation, reporting)
- Green: Postdoc 1 (empirical data and diagnostics)
- Teal: Postdoc 2 (generative modeling and simulation)
- Muted tone: shared team efforts (papers, releases, synthesis)

**Benchmark 0 gate:**
The highlighted brown-outlined bar marks the formal Year 1 decision gate that compares single-law and multi-regime explanations using AIC/BIC, cross-validation, change-point analysis, and alignment against transport-demand transitions.

**Bar length and position:**
Bar length indicates duration of effort. Position shows when each activity occurs relative to others.

---

## How to Interpret This Figure

The figure should be read from left to right as a decision-gated scientific workflow:

1. Year 1 emphasizes setup, data governance, event stabilization, trajectory assembly, QA/QC, observables, and Benchmark 0.
2. Year 2 emphasizes model library buildout, controlled contrasts, regime detection, ablations, calibration audits, validation, and sufficiency mapping.
3. Year 3 emphasizes benchmark packaging, external user testing, release readiness, onboarding, transfer, and synthesis reporting.

This structure keeps scientific deliverables and benchmark infrastructure legible within one figure while preserving the proposal's Detect → Explain → Apply logic.

---

## Why This Matters

This framework provides:

- A consistent way to measure wildfire growth geometry
- A mechanism-based explanation of observed scaling patterns
- A new benchmark for evaluating fire models
- Reusable tools and datasets for the broader community

The Gantt chart makes explicit how these outcomes are achieved through coordinated empirical, theoretical, and computational work.
