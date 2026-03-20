# Draft Change Report: On Growth and Form — Draft 01 to Draft 02

## Purpose

This memo records the substantive changes between the first saved generative-theory fire draft and the newly added second draft. Its purpose is to preserve proposal memory, make rhetorical and scientific shifts explicit, and flag material that may need to be restored or re-integrated in later drafts.

## Source files compared

- `proposal/narrative/drafts/on_growth_and_form_generative_theory_of_fire_draft_01.md`
- `proposal/narrative/drafts/on_growth_and_form_generative_theory_of_fire_draft_02.md`

## High-level shift

Draft 02 is a more compressed and more essay-like opening. Compared with Draft 01, it shifts the narrative center of gravity:

- away from a full proposal architecture and toward a conceptual thesis;
- away from an explicit model hierarchy and toward a threshold-regime story;
- away from a detailed computational machine and toward a physically motivated argument about coherence, transport, and oxygen supply; and
- away from execution detail and toward a more unified scientific voice inspired by *On Growth and Form*.

In short: Draft 02 sharpens the proposal's big idea, but it leaves behind some of the reviewer-confidence scaffolding that Draft 01 had already started to build.

## What Draft 02 adds or strengthens

### 1. Stronger opening voice and intellectual framing

Draft 02 opens with a tighter and more memorable statement of the proposal's motivating analogy to *On Growth and Form*. It makes the case that wildfire should be understood as a physical growth system rather than only a spread problem.

### 2. A clearer threshold-regime narrative

Draft 02 more explicitly distinguishes two fire regimes:

- an early fragmented regime dominated by local ignition variability; and
- a coherent regime in which the fire organizes into a continuous front and geometry begins to control behavior.

This transition is presented as a threshold with qualitative consequences rather than a smooth continuation of the same dynamics.

### 3. A stronger transport-limited scaling argument

Draft 02 strengthens the claim that once a fire becomes coherent, it may enter the same broad class of transport-limited systems as biological distribution networks and roughening or turbulent interfaces. The 3/4 and 4/3 motifs are made more central to the argument than they were in Draft 01.

### 4. A new oxygen-ventilation mechanism

The most important scientific addition is the explicit oxygen-supply story. Draft 02 proposes that coherent rapid spread depends on atmospheric ventilation being able to meet combustion demand at the fireline. This gives the threshold claim a mechanistic candidate rather than leaving it purely geometric.

### 5. A more concise falsifiability statement

Draft 02 states a clear rejection criterion: if the expected scaling signatures fail to appear after the predicted threshold crossing, the hypothesis is rejected. That directness is useful and should likely be preserved.

### 6. A cleaner two-model contrast

Instead of the longer `M0–M3` ladder in Draft 01, Draft 02 presents a more intuitive contrast between:

- a wave-based local spread model; and
- a geometric model for coherent front growth.

That simplification may help readability in early proposal sections.

## What Draft 02 reduces, compresses, or removes

### 1. Explicit FIRE-MODEL execution architecture

Draft 01 contained a large amount of proposal machinery: intake layer, generative engine, coupling layer, measurement layer, experiment layer, calibration layer, benchmark layer, work-plan logic, and concrete module names. Draft 02 removes almost all of that implementation structure.

### 2. Detailed model hierarchy and mechanism ladder

Draft 01 made the theory-first strategy concrete through the `M0–M3` model hierarchy. Draft 02 compresses this into a two-model contrast and therefore loses some of the proposal's explicit incremental test design.

### 3. Dimensionless-groups and regime-space formulation

Draft 01 stated a formal plan to define reduced dimensionless controls (`Π₁–Π₅`) and map fire behavior through regime space. Draft 02 keeps the threshold idea but drops this more formal mathematical framing.

### 4. Concrete data/benchmarking system design

Draft 01 described the case-object standard, harmonized data-intake layer, measurement system, ensemble experiments, calibration logic, and benchmarking logic. Draft 02 mentions time-resolved perimeters, meteorology, and fuels, but not the workflow needed to make that credible at NSF proposal level.

### 5. Deliverables and feasibility signals

Draft 01 gave reviewers more evidence that the team has a plan for execution, modular implementation, and high-throughput experimentation. Draft 02 sacrifices much of that feasibility language for conceptual elegance.

## Important material at risk of being left behind

These items appear substantively important for later proposal drafts and should be treated as restore-if-missing elements rather than optional ornament.

### Flag 1. Explicit model-hierarchy logic

Draft 01's reduced-to-richer hierarchy is valuable because it shows how the project will determine when added complexity is scientifically necessary. Draft 02 should not permanently lose that structure.

### Flag 2. Benchmark and evaluation architecture

The proposal still needs to explain how observations, model classes, uncertainty, and benchmark criteria will be linked. Draft 02 currently under-specifies this.

### Flag 3. Data and workflow credibility

Draft 01's case-object, ingestion, and analysis-pipeline logic gave the project operational credibility. Draft 02 should be paired with that machinery elsewhere in the Project Description.

### Flag 4. Deliverables reviewers can remember

Draft 01 made it easier to infer concrete outputs such as reusable diagnostics, benchmark workflows, and open computational products. Draft 02 needs those outputs reattached in later sections.

### Flag 5. Explicit call alignment

Draft 02 is stronger as scientific prose than as solicitation-facing prose. Future revisions should preserve the new conceptual force while reintroducing direct FIRE-MODEL language on predictive modeling systems, cross-scale integration, validation, and computational deliverables.

## Recommended synthesis for the next draft

The best next step is probably not to choose between the drafts, but to combine them.

- Keep Draft 02's opening paragraphs, coherence-threshold story, oxygen mechanism, and concise falsifiability language.
- Reintroduce from Draft 01 the model hierarchy, computational workflow, benchmark architecture, and clearer feasibility/deliverable signals.
- Make the oxygen-threshold mechanism one candidate organizing principle inside the larger model-and-validation architecture rather than the whole proposal.

## Assumptions and cautions

- This change report compares narrative emphasis, not line-by-line wording only.
- The 3/4 and 4/3 references remain conceptually important but should still be checked carefully for citation support and scope before they appear in submission prose.
- The oxygen-ventilation threshold is a promising mechanism statement, but it remains a hypothesis and should continue to be framed as testable rather than established.
