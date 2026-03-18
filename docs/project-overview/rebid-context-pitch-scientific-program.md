# Rebid Context, Pitch, and Scientific Program

This page summarizes a proposal-strategy memo for the FIRE-MODEL rebid. It is not sponsor-issued guidance. Its purpose is to help the repository keep the conceptual pitch, scientific aims, and validation logic aligned as the next proposal draft is developed.

> Status note: use this strategy page together with the solicitation and checklist materials under [Funder Materials](funder-materials.md).

## Why this page belongs in proposal strategy

This material does more than provide background theory. It proposes how the rebid should frame the scientific object, articulate the conceptual advance, organize the aims, and explain the validation pathway.

The primary source memo now lives in:

- `proposal/narrative/fire_model_rebid_context_pitch_scientific_program.md`

That placement reflects its role in shaping the Project Description and related sponsor-facing materials.

## Core thesis

The rebid strategy centers on one claim: wildfire perimeters and related environmental boundaries should be treated as **scale-conditioned interfaces**.

That means their geometry depends on both:

- how the boundary is defined; and
- the scale at which it is measured.

In this framing, boundary geometry is not just descriptive output. It becomes a primary observable for understanding, comparing, and validating wildfire dynamics.

## Why this matters for FIRE-MODEL

The memo is designed to make several FIRE-MODEL expectations easier to answer in a coherent way:

- **Conceptual advance:** geometry becomes central to wildfire modeling rather than an afterthought.
- **Computational framework:** the proposal organizes around a generative interface model and multi-scale geometry pipeline.
- **Validation pathway:** models are tested against `L_d(ε)` curves and related geometric diagnostics.
- **Cross-scale dynamics:** the proposal directly addresses how observed structure changes with definition and measurement scale.

## Scientific program structure

### Aim 1 — Define the object

Build a formal, data-driven framework for scale-conditioned environmental interfaces across multiple fire datasets and sensor definitions.

### Aim 2 — Explain the form

Link observed interface geometry to generative processes using minimal coupled models, reaction–diffusion and percolation analogs, and synthetic-interface experiments.

### Aim 3 — Validate using geometry

Establish a multi-scale validation framework in which wildfire models are evaluated by whether they reproduce observed geometric signatures across scales.

## Strategic modeling contribution

The memo proposes a **Generative Interface Model (GIM)** as the central modeling contribution.

Its distinguishing feature is that it is constrained by multi-scale interface geometry, not only by endpoint similarity or final-perimeter overlap.

## Key validation shift

The main validation shift is from single-metric or endpoint comparison to functional comparison of geometric observables, including:

- `L_d(ε)` curves;
- exponent stability;
- curvature and roughness diagnostics;
- sensitivity to subsampling and observation structure.

## Related in-repo strategy sources

- Primary rebid strategy memo: `proposal/narrative/fire_model_rebid_context_pitch_scientific_program.md`
- Prior review-driven strategy memo: `proposal/narrative/fire_model_resubmission_strategy.md`
- Historical review synthesis: `background_context/program_briefings/fire_model_first_submission_review_resubmission_strategy.md`
