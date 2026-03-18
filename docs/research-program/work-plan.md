# Wildfire Scaling Research Program: Comprehensive Work Plan

## Role in the FIRE-MODEL proposal

This work plan is a repository-ready program document for the `FIRE-MODEL` concept. It is intended to strengthen the project description's treatment of research strategy, team structure, milestones, and deliverables in a way that supports the proposal's conceptual advance, computational framework, and validation pathway described in the working FIRE briefing and checklist.

## Purpose of this document

This document captures the full execution logic for the wildfire scaling research program. It is not only draft proposal prose. It is also a working reference for collaborators and future contributors that records:

- the scientific motivation and linked hypotheses,
- the execution strategy across the project period,
- the team structure and why that structure is necessary,
- benchmarked deliverables, and
- the logical flow from measurement to mechanism to model evaluation.

## Core scientific framing

The project is motivated by a central hypothesis:

> Wildfire growth exhibits regime-dependent geometric scaling that constrains its evolution, and this structure is either intrinsic to fire dynamics or imposed by environmental forcing.

This framing reflects a broader conceptual shift in how wildfire behavior is studied. In this project, fire is not treated only as a local spread process. It is treated as a **spatiotemporal growth system with emergent geometry**.

The work plan is organized to test three linked hypotheses.

### H1 — Existence of structure

Wildfire growth trajectories exhibit consistent scaling relationships and identifiable regime structure across events.

### H2 — Origin of structure

Observed scaling behavior arises either:

- from intrinsic perimeter dynamics and coupled growth, or
- from externally imposed structure such as wind, fuels, and topography.

### H3 — Model implication

If such structure exists, current fire models fail to capture it in ways that are not detectable using standard evaluation metrics alone.

## Why this requires a coordinated team

The central question cannot be answered through a single analytical pathway.

- Empirical analysis alone cannot decisively distinguish intrinsic from environmentally forced structure.
- Generative modeling alone cannot establish whether any proposed mechanism is relevant to real wildfire trajectories.
- Model evaluation alone cannot reveal missing organizing principles unless the empirical and generative work have already identified what to test.

For that reason, the project is structured around three tightly coupled components that must remain aligned through shared observables and diagnostics:

1. empirical detection of structure,
2. generative testing of mechanism, and
3. translation into model evaluation.

Each component is substantial enough to function as a research program in its own right. Running them in parallel is what makes the central hypothesis test decisive rather than suggestive.

### Team structure and justification

This work plan assumes the following minimum team structure:

- **Postdoctoral Researcher 1** leads empirical trajectory construction, quality control, and scaling analysis.
- **Postdoctoral Researcher 2** leads generative modeling, mechanism testing, and model-space exploration.
- **Principal Investigator** leads integration, cross-arc synthesis, and translation into wildfire model evaluation and open-science products.

This structure is justified because the project must deliver a conceptual advance, a computational modeling framework, and a validation pathway, all of which are emphasized in the repository's current FIRE-MODEL planning materials.

## Project architecture: three interlocking arcs

### Arc 1 — Empirical growth structure

**Goal:** Determine whether scaling and regime structure exist in wildfire growth trajectories.

### Arc 2 — Generative mechanism testing

**Goal:** Determine what classes of processes can generate the observed structure.

### Arc 3 — Evaluation and translation

**Goal:** Use discovered structure to diagnose and improve wildfire models.

These three arcs run in parallel, but they converge at defined annual benchmarks so that each year produces both scientific output and decision-relevant evidence.

## Three-year execution logic

- **Year 1:** Build the system to measure wildfire growth as geometry.
- **Year 2:** Determine whether scaling structure exists and identify candidate mechanisms.
- **Year 3:** Translate the findings into a diagnostic framework for evaluating and improving wildfire models.

## Year 1 — Build the measurement system

### Scientific objective

Establish a validated system for measuring wildfire growth geometry from empirical trajectories.

### Empirical work (Postdoctoral Researcher 1)

- Construct `FIRED`-based wildfire trajectories with synchronized area and perimeter histories.
- Develop a QA/QC framework for trajectory reliability, resolution sensitivity, and measurement provenance.
- Implement first-generation scaling diagnostics, including:
  - local exponent estimation,
  - normalization strategies for cross-fire comparison, and
  - collapse detection workflows.

### Generative work (Postdoctoral Researcher 2)

- Build a minimal model hierarchy spanning:
  - stochastic growth,
  - percolation-like spread, and
  - cellular automata with environmental forcing.
- Align model outputs with the same observables and diagnostics used for empirical trajectories.

### Integration and translation (PI)

- Define the shared observables that connect data, minimal models, and later model evaluation.
- Ensure that empirical and synthetic outputs are comparable through common diagnostics and metadata conventions.

### Year 1 deliverables

- validated trajectory dataset,
- QA/QC documentation,
- scaling diagnostics pipeline (`v1`),
- generative modeling framework (`v1`),
- initial dissemination through a conference or workshop contribution, and
- NSF annual reporting materials.

### Year 1 benchmark

By the end of Year 1, the team can reliably measure wildfire growth as a geometric process and detect candidate structure beyond null expectations.

## Year 2 — Detect structure and identify mechanism

### Scientific objective

Test whether regime-dependent scaling exists across fires and determine what mechanisms can or cannot generate it.

### Empirical work (Postdoctoral Researcher 1)

- Conduct ensemble scaling analysis across wildfire trajectories.
- Apply change-point or related regime-detection methods to identify shifts in growth behavior.
- Perform collapse analysis across normalized trajectories to test whether diverse fires share common structure.

### Environmental conditioning

- Integrate wind, fuels, and topographic context into the empirical analysis.
- Compare observed results against null and surrogate datasets.
- Test whether candidate scaling structure persists, weakens, or disappears after conditioning on environmental forcing.

### Generative work (Postdoctoral Researcher 2)

- Run parameter sweeps across the minimal model hierarchy.
- Conduct forcing-ablation experiments to isolate which ingredients are necessary for stable or transient scaling behavior.

### Key output: phase diagram

A central Year 2 synthesis product is a phase diagram mapping scaling behavior as a function of:

- forcing intensity, such as wind or advection strength, and
- spatial connectivity, such as fuel continuity or percolation state.

The phase diagram will identify regions associated with:

- stable scaling,
- no scaling, and
- transient or regime-switching behavior.

### Integration and interpretation (PI)

- Align empirical and generative results using the shared diagnostics established in Year 1.
- Interpret whether the evidence supports intrinsic organization, environmental imposition, or mixed causation.

### Year 2 deliverables

- ensemble scaling results,
- robustness and null-model tests,
- empirical manuscript in preparation or submission,
- generative manuscript in preparation or submission,
- conference dissemination, and
- NSF annual reporting materials.

### Year 2 benchmark

By the end of Year 2, the team determines whether regime-dependent scaling exists across fires and identifies minimal mechanisms capable of producing or failing to produce it.

## Year 3 — Translate to model evaluation and application

### Scientific objective

Convert the empirical and generative findings into a framework for diagnosing wildfire models.

### Evaluation work (PI-led with full team support)

- Apply the developed diagnostics to existing wildfire models.
- Evaluate model behavior in terms of:
  - regime-detection accuracy,
  - scaling fidelity, and
  - trajectory geometry.

### Key insight sought

The project is designed to identify model failure modes that are difficult to detect with standard performance metrics alone, including:

- models that reproduce an average rate of spread while producing incorrect geometry, and
- models that miss or blur regime transitions visible in observed fire trajectories.

### Toolkit development (team)

- Package the diagnostics into `CubeDynamics`.
- Build reproducible workflows so the evaluation system can be reused by future researchers and model developers.

### Open-science deliverables

- curated data release,
- code release,
- workflow documentation, and
- reusable benchmarking materials.

### Synthesis

- Integrate the empirical, generative, and evaluation results into a unified framework for wildfire growth as a structured spatiotemporal process.
- Translate the findings into practical guidance for diagnosing and improving next-generation wildfire models.

### Year 3 deliverables

- model benchmarking results,
- operational diagnostics toolkit,
- open-source data and workflows,
- benchmarking and synthesis manuscripts,
- final dissemination products, and
- NSF final reporting materials.

### Year 3 benchmark

By the end of Year 3, the project delivers a practical and scientific framework for diagnosing and improving wildfire models based on growth structure.

## Risk structure and outcome logic

The project is designed to produce useful outcomes under multiple scientific scenarios.

### Case 1 — No scaling found

- Establish limits of predictability in wildfire growth geometry.
- Provide null benchmarks that future wildfire models should not overinterpret.

### Case 2 — Scaling found but primarily forced

- Show how strongly wildfire growth structure depends on environmental organization.
- Motivate improved representation of forcing fields and landscape structure in models.

### Case 3 — Intrinsic scaling found

- Identify a new organizing principle for wildfire growth.
- Create a strong basis for rethinking wildfire model design and evaluation around emergent geometry.

Each of these outcomes is scientifically meaningful, publishable, and useful for the `FIRE-MODEL` objective of advancing wildfire prediction frameworks.

## Final perspective

This work plan is structured so that:

- each year produces meaningful scientific output,
- each project arc can stand on its own, and
- all arcs contribute to a decisive test of the central hypothesis.

The combination of empirical data analysis, generative experimentation, and wildfire model evaluation is what makes the program both feasible and scientifically powerful. As a repository artifact, this document should function both as a roadmap for execution and as a reference explaining how each component contributes to the broader scientific goal.
