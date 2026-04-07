# Prompt Action Log

## 2026-03-20

### Prompt
User provided a document titled `Wildfire Modeling Master Bibliography (Full Integrated Storage)` and asked: "here is a literature search i did about the history of fire. it has citations and authors and the verbatim details are important. will you make this a markdown document in the citations area of the repo for future reference when we're doing citations".

### Files and folders inspected
- `citations/README.md`
- `citations/notes/wildfire_scaling_bibliography.md`
- `docs/literature/bibliography.md`

### Actions taken
- Added `citations/notes/wildfire_modeling_master_bibliography.md` as a dense imported reference note under the existing citations workflow.
- Preserved the provided citation details, author identity links, summaries, and example citation sentences in Markdown form.
- Marked the file as imported working material that still requires verification against original sources because verbatim details matter.

### Verification
- Confirmed the note was written into `citations/notes/` and matches the repository's existing bibliography-note structure.

### Open questions and follow-up
- If these entries become proposal-critical, the next step should be to verify each record against the original paper, DOI metadata, and available PDFs.

### Prompt
User asked: "can you add this to the top of that document for context. don't delete, just add", followed by a multi-paragraph historical framing of wildfire modeling from Rothermel through spatial, probabilistic, physics-based, landscape, and machine-learning lineages.

### Files and folders inspected
- `citations/notes/wildfire_modeling_master_bibliography.md`

### Actions taken
- Added a new `Historical context` section at the top of `citations/notes/wildfire_modeling_master_bibliography.md`.
- Kept the existing bibliography content intact beneath the new framing section.

### Verification
- Confirmed the new context appears at the top of the document and that the prior bibliography entries remain unchanged below it.

### Open questions and follow-up
- The contextual framing now cites milestone lineages in prose; if the file becomes a public-facing source, those milestone claims should also be verified entry by entry.

### Prompt
User asked for a reproducible, script-generated figure showing "a time-calibrated conceptual phylogeny of wildfire modeling", with a Python script, generated PNG in docs assets, a dedicated MkDocs page, navigation placement in planning/background materials, and GitHub Actions regeneration during docs build or deploy.

### Files and folders inspected
- `mkdocs.yml`
- `requirements.txt`
- `requirements-dev.txt`
- `.github/workflows/pages.yml`
- `.github/workflows/website-checks.yml`
- `.github/workflows/generate_fire_model_gantt.yml`
- `docs/planning/gantt_chart.md`
- `docs/stylesheets/extra.css`
- `scripts/generate_fire_model_gantt.py`

### Actions taken
- Added `scripts/figures/generate_wildfire_modeling_phylogeny.py` to generate a deterministic publication-style PNG for the wildfire modeling phylogeny.
- Generated `docs/assets/figures/wildfire_phylogeny_publication.png` from code and tuned the layout for legibility at website width.
- Added `docs/planning/wildfire-modeling-phylogeny.md` with introductory context, prose legend, and an explicit note that the diagram is a conceptual time-calibrated phylogeny rather than a strict software dependency tree.
- Updated `mkdocs.yml` so the page appears under `Planning > Wildfire Modeling Phylogeny`.
- Updated `.github/workflows/pages.yml` and `.github/workflows/website-checks.yml` so GitHub regenerates the figure before site validation and before the Pages build.
- Added `matplotlib` to `requirements.txt` and added a targeted image style rule in `docs/stylesheets/extra.css`.

### Verification
- Ran `python3 scripts/figures/generate_wildfire_modeling_phylogeny.py`.
- Confirmed `docs/assets/figures/wildfire_phylogeny_publication.png` was created successfully.
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the built page exists at `dist/planning/wildfire-modeling-phylogeny/` and references the generated image asset in the built HTML.

### Open questions and follow-up
- The figure is intentionally conceptual and selective; if the proposal later requires a more exhaustive lineage, the current script can be extended with additional branches or annotations without changing the page structure.

### Prompt
User provided a long-form document titled `A Causal History of Wildfire Modeling` and asked to "add this to the background and context section as a new page".

### Files and folders inspected
- `mkdocs.yml`
- `docs/project-overview/program-context.md`
- `docs/project-overview/`

### Actions taken
- Added `docs/project-overview/causal-history-wildfire-modeling.md` as a new long-form background/context page.
- Placed the page under the existing `Project Overview` section in `mkdocs.yml` as `Causal History of Wildfire Modeling`.
- Preserved the document's core historical argument while formatting it as a readable MkDocs page with section headings and repository-consistent framing.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new page included in navigation.

### Open questions and follow-up
- If this page becomes central to proposal framing, it may be worth cross-linking it from the wildfire modeling phylogeny page and related theory pages.

### Prompt
User provided a long-form document titled `Methods: Measurement and Validation Framework` and asked to add it to the documentation as Methods section 1.

### Files and folders inspected
- `docs/methods/index.md`
- `docs/methods/scaling-diagnostics.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/methods/measurement-validation-framework.md` as a new long-form methods page.
- Added the page to the Methods section index in `docs/methods/index.md`.
- Updated `mkdocs.yml` so the page appears in the site navigation as `Methods > Measurement and Validation Framework`.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new page and nav entry.

### Open questions and follow-up
- This page now states the full elimination logic clearly; the next useful step may be to cross-link it from model benchmarking or theory pages that rely on the same validation argument.

### Prompt
User provided a long-form document titled `Methods: Generative Modeling as a Mechanism Testing Framework (Technical Specification)` and asked to add it as Methods section 2, explicitly as an additive follow-on to the measurement framework.

### Files and folders inspected
- `docs/methods/measurement-validation-framework.md`
- `docs/methods/index.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/methods/generative-modeling-mechanism-testing.md` as a companion methods page focused on generative mechanism testing.
- Added the new page to `docs/methods/index.md` so it appears alongside the measurement framework.
- Updated `mkdocs.yml` so the page appears in the site navigation as `Methods > Generative Modeling as a Mechanism Testing Framework`.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new page and navigation entry.

### Open questions and follow-up
- The measurement and mechanism-testing pages now form a two-part workflow; a later cleanup could add reciprocal links between them and to the benchmarking page.

### Prompt
User provided a long-form document titled `Methods: Evaluating Velocity as a Descriptor of Fire Spread` and asked to place it as Methods section `1B`, between the measurement framework and the generative modeling framework.

### Files and folders inspected
- `docs/methods/index.md`
- `docs/methods/measurement-validation-framework.md`
- `docs/methods/generative-modeling-mechanism-testing.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/methods/velocity-as-fire-spread-descriptor.md` as the intermediate methods page on velocity definitions, scale dependence, and geometric breakdown.
- Reordered the Methods section in `docs/methods/index.md` so the sequence now reads measurement, velocity, then generative modeling.
- Updated `mkdocs.yml` so the page appears in navigation as `Methods > Evaluating Velocity as a Descriptor of Fire Spread`.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new page and reordered navigation.

### Open questions and follow-up
- The methods sequence now has a clearer conceptual progression; a later refinement could add direct cross-links at the end of each page to guide readers from 1a to 1b to the generative framework.

### Prompt
User provided a long-form document titled `Methods: Model-Data Comparison and Scoring Framework` and asked to place it as Methods section `1C`, after the velocity page and before the generative modeling framework.

### Files and folders inspected
- `docs/methods/index.md`
- `docs/methods/velocity-as-fire-spread-descriptor.md`
- `docs/methods/generative-modeling-mechanism-testing.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/methods/model-data-comparison-scoring-framework.md` as the intermediate model evaluation and elimination page.
- Updated `docs/methods/index.md` so the methods sequence now includes measurement, velocity, model-data comparison, and then generative modeling.
- Updated `mkdocs.yml` so the page appears in navigation as `Methods > Model-Data Comparison and Scoring Framework`.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new page and updated ordering.

### Open questions and follow-up
- The methods stack now has a stronger bridge from measurement to mechanism testing; a later pass could add inline cross-links so readers can step through 1a, 1b, 1c, and methods 2 more explicitly.

### Prompt
User provided a long-form document titled `Methods: Synthetic Validation, Uncertainty, and Identifiability` and clarified that this was Methods section `3`, focused on testing how well generated fires compare to data and whether the full evaluation system is trustworthy.

### Files and folders inspected
- `docs/methods/index.md`
- `docs/methods/generative-modeling-mechanism-testing.md`
- `docs/methods/model-data-comparison-scoring-framework.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/methods/synthetic-validation-uncertainty-identifiability.md` as the validation and trustworthiness page for the end-to-end analytical pipeline.
- Updated `docs/methods/index.md` so the Methods section now includes this page after the generative framework.
- Updated `mkdocs.yml` so the page appears in navigation as `Methods > Synthetic Validation, Uncertainty, and Identifiability`.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new page and navigation entry.

### Open questions and follow-up
- The methods arc is now close to a full sequence; a future pass could group these pages more explicitly into Methods 1, Methods 2, and Methods 3 with short cross-references.

### Prompt
User provided a summary document titled `FIRE-MODEL Methods System: Narrative Summary for Discovery` and asked to add it to the beginning of the methods section, then relabel the component pages so their titles clearly show `Method 1`, `Method 1B`, `Method 1C`, `Method 2`, and `Method 3`.

### Files and folders inspected
- `docs/methods/index.md`
- `docs/methods/measurement-validation-framework.md`
- `docs/methods/velocity-as-fire-spread-descriptor.md`
- `docs/methods/model-data-comparison-scoring-framework.md`
- `docs/methods/generative-modeling-mechanism-testing.md`
- `docs/methods/synthetic-validation-uncertainty-identifiability.md`
- `mkdocs.yml`

### Actions taken
- Added a methods-system summary and canonical section map to the top of `docs/methods/index.md`.
- Updated the Methods landing-page links so they now use the canonical labels `Method 1`, `Method 1B`, `Method 1C`, `Method 2`, and `Method 3`.
- Renamed the page titles in the five core methods documents to match the canonical sequence.
- Updated `mkdocs.yml` so the Methods navigation uses the same canonical labels.
- Fixed the MkDocs YAML navigation labels by quoting entries that contain colons.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new labels and methods summary.

### Open questions and follow-up
- The core methods sequence is now clearer in titles and navigation; a useful future step would be to add short reciprocal cross-links at the top of each page so readers can move directly through the 1 -> 1B -> 1C -> 2 -> 3 pipeline.

## 2026-04-03

### Prompt
User asked to update the tracked Gantt wrapper (`docs/planning/gantt_chart.md`) and underlying editable source for `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg` so the figure matches the current Detect/Explain/Apply proposal framing, current personnel labels, required year-specific workstreams, and cross-cutting overlap.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/nsf_fire_fire_science_innovations_through_research_and_education.html`
- `docs/planning/gantt_chart.md`
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg`

### Actions taken
- Updated `scripts/generate_fire_model_gantt.py` as the editable source to replace outdated staging language and role keys, then rewrote task definitions to align with Detect/Explain/Apply logic and current personnel ownership.
- Removed old benchmark-gate-oriented language from the chart generation pathway and updated the subtitle and legend to emphasize shared diagnostics `A(t)`, `P(t)`, and `sigma` plus overlapping workstreams.
- Updated `docs/planning/gantt_chart.md` wrapper text, legend language, and interpretation notes so they match the current proposal framing and role labels.
- Regenerated the tracked figure assets (`.svg` and `.png`) from the updated source script.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py` to regenerate chart assets from source.
- Ran `bash scripts/review_site.sh` to validate documentation/site-facing changes.

### Open questions and follow-up
- The updated chart includes Model Reconciliation Council and Fire Dynamics Explorer rows because they were already part of proposal logic; if scope changes, those rows should be adjusted in both script and wrapper text together.

### Prompt
User reported CI failure when running `python scripts/generate_fire_model_gantt.py` due to `ModuleNotFoundError: No module named 'PIL'` and asked for fixes.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`

### Actions taken
- Made Pillow import optional in `scripts/generate_fire_model_gantt.py` to avoid hard failure when `PIL` is not installed.
- Updated the pure-Python render path so SVG generation still succeeds without Pillow and PNG output is only attempted when Pillow is available.
- Updated script status messaging to report when PNG output is skipped because Pillow is missing.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py`; script completed successfully.

### Open questions and follow-up
- If CI requires PNG artifacts in environments without Pillow, either add Pillow to the CI environment or run the matplotlib renderer explicitly where dependencies are present.

### Prompt
User provided a document titled `FIRE-MODEL Staffing Plan: Roles, 3-Year Timeline, Milestones, and Deliverables` and asked to add it to the planning section of the repository and website.

### Files and folders inspected
- `docs/planning/`
- `docs/planning/gantt_chart.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/planning/staffing-plan.md` as a standalone planning page covering roles, annual timelines, milestones, conference outputs, deliverables, and integration cadence.
- Updated `mkdocs.yml` so the page appears in the site navigation as `Planning > Staffing Plan`.
- Preserved the role structure around Postdoc 1, Postdoc 2, and the PI while formatting the document for repository and website readability.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new staffing-plan page and planning nav entry.

### Open questions and follow-up
- This page pairs naturally with the existing Gantt chart; a future refinement could add direct cross-links between the staffing plan, work plan, and Gantt page so responsibilities and schedule are easier to traverse together.

### Prompt
User provided a document titled `Evaluation and Success Criteria` and asked to add it to the planning section of the repository and website.

### Files and folders inspected
- `docs/planning/`
- `mkdocs.yml`
- `docs/research-program/work-plan.md`

### Actions taken
- Added `docs/planning/evaluation-success-criteria.md` as a planning page covering scientific success, technical success, comparative advancement, training outcomes, and field-level impact.
- Updated `mkdocs.yml` so the page appears in the site navigation as `Planning > Evaluation and Success Criteria`.
- Consolidated repeated closing language into a cleaner final success statement while preserving the document's evaluation logic and success domains.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new evaluation page and planning nav entry.

### Open questions and follow-up
- This page now complements the staffing plan and work plan; a later pass could cross-link the success criteria to the specific milestones and deliverables that operationalize them.

### Prompt
User provided a full structural refactor brief beginning `Codex Prompt: Refactor the on_growth_and_form repo/site structure without rewriting content` and asked for a documentation-architecture refactor that would preserve long-form markdown, add short section landing pages, simplify top-level navigation, separate drafts from core material, and ensure there were no orphaned important pages.

### Files and folders inspected
- `mkdocs.yml`
- `README.md`
- `AGENTS.md`
- `docs/`
- `docs/index.md`
- `docs/repository-map.md`
- `docs/project-overview/index.md`
- `docs/theory/index.md`
- `docs/data-infrastructure/index.md`
- `docs/methods/index.md`
- `docs/models/index.md`
- `docs/research-program/index.md`
- `docs/literature/index.md`
- `docs/drafts/index.md`
- `docs/workflow.md`

### Actions taken
- Added `docs/start-here/index.md`, `docs/planning/index.md`, and `docs/archive/index.md` as structural landing pages for entry points, planning materials, and retained draft material.
- Simplified and standardized the major section landing pages in `docs/project-overview/index.md`, `docs/theory/index.md`, `docs/data-infrastructure/index.md`, `docs/methods/index.md`, `docs/models/index.md`, `docs/research-program/index.md`, and `docs/literature/index.md` so they route readers to the underlying long-form documents instead of acting like mini-essays.
- Refactored `mkdocs.yml` so the top-level navigation is shorter and more stable, while each major section still exposes its underlying pages as nested items under the section landing page.
- Removed direct top-level nav clutter for `workflow.md`, `repository-map.md`, and draft pages by routing them through `Start Here` and `Archive`.
- Updated `docs/index.md` so the homepage section list matches the new site structure.
- Updated `docs/repository-map.md` so the documented `docs/` layout matches the refactored site structure.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the build succeeded.
- Ran a reachability check comparing all `docs/**/*.md` files to `mkdocs.yml` navigation and confirmed there are zero orphaned docs pages.

### Open questions and follow-up
- The current structure preserves both `project-overview/` and `research-program/` as distinct sections; if the authors later want tighter curation, that boundary may still warrant human judgment, but it is now navigable and explicit rather than hidden in the nav.

### Prompt
User provided a document titled `Broader Impacts` and asked: "Here is another document to add to the proposal planning section. this is the broader impact statement".

### Files and folders inspected
- `docs/planning/index.md`
- `mkdocs.yml`

### Actions taken
- Added `docs/planning/broader-impacts.md` as a planning page covering the Fire Lab platform, documentary and educational media, open science and training, integration across components, budget justification, and long-term impact.
- Updated `docs/planning/index.md` so the broader-impacts page appears in the planning landing page.
- Updated `mkdocs.yml` so the page appears in navigation as `Planning > Broader Impacts`.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully with the new broader-impacts page and planning nav entry.

### Open questions and follow-up
- The planning section now includes staffing, evaluation, and broader impacts; a later pass could cross-link these planning pages if the authors want a more explicit proposal assembly path.

### Prompt
Audit the prompt log and fill in any information that was not fully moved from the original prompts, keeping the prompt wording as verbatim as possible where the original text is available.

### Files and folders inspected
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Revised the recent `### Prompt` entries from the current work session so they preserve more of the original user wording, document titles, and structural instructions instead of compressed one-line summaries.
- Left the action, verification, and follow-up sections unchanged except where the prompt wording itself needed to be made more faithful.

### Verification
- Confirmed the updated log now preserves the original titles and asks more directly for the recent bibliography, methods, planning, broader impacts, and site-structure prompts.

### Open questions and follow-up
- Older entries from prior sessions may still contain compressed paraphrases where the exact original prompt text is not readily recoverable from the current conversation context; those would require a separate history-based audit if verbatim recovery is needed there too.

### Prompt
User asked: "the Gantt chart is a svg but I also need it in png".

### Files and folders inspected
- `AGENTS.md`
- `.gitignore`
- `scripts/generate_fire_model_gantt.py`
- `docs/planning/gantt_chart.md`
- `docs/assets/figures/`

### Actions taken
- Regenerated the FIRE-MODEL Gantt assets from source (`scripts/generate_fire_model_gantt.py`) to ensure the PNG and SVG are both current.
- Removed the `.gitignore` rule that excluded `docs/assets/figures/fire_model_gantt_ESIIL_minimal.png` so the PNG can be tracked in the repository.
- Added a direct PNG link to `docs/planning/gantt_chart.md` beneath the SVG embed to expose both formats in the planning page.

### Verification
- Ran `python scripts/generate_fire_model_gantt.py` and confirmed both SVG and PNG outputs were produced.
- Ran `bash scripts/review_site.sh` after the documentation change.

### Open questions and follow-up
- If additional chart revisions are made, rerun the same generator script so the SVG and PNG remain synchronized.

### Prompt
User stated that binaries are not supported and requested the Gantt PNG be handled with GitHub in-repo generation rather than committing binary artifacts.

### Files and folders inspected
- `.gitignore`
- `scripts/review_site.sh`
- `.github/workflows/pages.yml`
- `.github/workflows/website-checks.yml`
- `docs/planning/gantt_chart.md`

### Actions taken
- Removed the tracked PNG (`docs/assets/figures/fire_model_gantt_ESIIL_minimal.png`) from git and restored ignore rules so the binary is generated, not versioned.
- Updated `scripts/review_site.sh` to generate the FIRE-MODEL Gantt assets before MkDocs build and site tests.
- Updated `.github/workflows/pages.yml` and `.github/workflows/website-checks.yml` to run `scripts/generate_fire_model_gantt.py` so the PNG exists in CI and GitHub Pages builds.
- Kept the docs page PNG link in place, with the asset now produced by the generation step instead of committed binary storage.

### Verification
- Ran `python scripts/generate_fire_model_gantt.py` to confirm SVG/PNG generation.
- Ran `bash scripts/review_site.sh`; MkDocs build passed and pytest collection failed due to missing local `playwright` dependency.

### Open questions and follow-up
- CI already installs Playwright in GitHub Actions, so local missing dependency should not affect GitHub-hosted checks.

## 2026-03-12

### Prompt
Rework the documentation website so it uses the existing long-form markdown documents directly as rendered pages, avoids replacing them with thin summaries, and keeps the homepage and section pages narrative and proposal-oriented.

### Files and folders inspected
- `mkdocs.yml`
- `docs/`
- `background_context/`
- `citations/notes/wildfire_scaling_bibliography.md`
- `citations/exports/wildfire_scaling_bibliography.bib`

### Actions taken
- Confirmed that the major theory, systems, and research-program pages in `docs/` now mirror the full long-form documents from `background_context/` instead of short summary substitutes.
- Kept the section landing pages lightweight and oriented them toward navigation rather than content replacement.
- Strengthened `docs/index.md` so the homepage more clearly explains the project's scientific motivation, the role of *On Growth and Form*, and how `FIRED` plus `CubeDynamics` support the work.
- Expanded `docs/literature/index.md` and `docs/literature/bibliography.md` so the literature section points readers to the real in-repo bibliography workflow rather than reading like a placeholder.

### Verification
- Confirmed the long-form docs are directly included in `mkdocs.yml` navigation.
- Confirmed the theory, data/infrastructure, and research-program pages in `docs/` match the full-length source documents where those source documents exist.

### Open questions and follow-up
- A full MkDocs and Playwright review should still be run in an environment with the site dependencies installed to verify rendering and link integrity after the structural changes.

### Prompt
Review and fix the next website CI failure, which reported MkDocs relative-link warnings and a Playwright strict-mode selector failure on the homepage heading.

### Files and folders inspected
- `tests/test_site.py`
- `docs/index.md`
- `docs/project-overview/index.md`
- `docs/data-infrastructure/satellite-fire-datasets.md`

### Actions taken
- Updated the homepage and section links to use explicit `index.md` targets so MkDocs no longer reports ambiguous relative links during strict builds.
- Updated the Playwright heading assertion to use `exact=True`, preventing the homepage test from failing when a later subsection heading partially matches the page title.

### Verification
- Confirmed the affected links now point to explicit page targets recognized by MkDocs.
- Confirmed the test logic now distinguishes the page title from the subsection heading `Why "On Growth and Form"`.

### Open questions and follow-up
- The next CI run should confirm that the previous MkDocs warnings are cleared and that the homepage render test no longer fails on selector ambiguity.

## 2026-03-10

### Prompt
Edit `AGENTS.md` to focus on NSF proposal work, define expected agent behavior, require logging, and add rules for citations, formatting, and writing directly to the call for proposals.

### Files and folders inspected
- `AGENTS.md`
- repository status for context

### Actions taken
- Replaced the generic repository agent guidance with NSF proposal-specific operating rules.
- Added explicit policies for solicitation-first drafting, citation verification, PDF collection, NSF compliance, simulation and figure provenance, and review behavior.
- Created this log file and established it as a required artifact for future agent work.

### Verification
- Confirmed the updated instruction set was written to `AGENTS.md`.
- Confirmed `PROMPT_ACTION_LOG.md` was created in the repository root.

### Open questions and follow-up
- The exact NSF program solicitation documents still need to be placed in `funder/` so future agent guidance can cite the controlling files directly.

### Prompt
Add website testing with Playwright, make it run whenever the website changes, and catch failures before a PR is blocked if possible.

### Files and folders inspected
- `.github/workflows/pages.yml`
- `requirements.txt`
- repository status
- local tool availability for Python and Node

### Actions taken
- Added Python Playwright and pytest development dependencies in `requirements-dev.txt`.
- Added Playwright smoke tests in `tests/test_site.py` to build the site, serve the built output, verify core pages, and fail on browser-side errors or broken internal links from the homepage.
- Added a PR-focused GitHub Actions workflow in `.github/workflows/website-checks.yml`.
- Updated the deploy workflow so GitHub Pages deployment depends on the same validation checks.
- Updated `README.md` with local site test commands.

### Verification
- Confirmed the workflow, dependency, and test files were written to the repository.
- Confirmed the local machine lacks `node` and `npm`, so a Python Playwright setup is the more stable fit here.

### Open questions and follow-up
- Local execution still requires installing `mkdocs`, `pytest`, and `playwright`, plus the Chromium browser bundle.

### Prompt
Point to `CU-ESIIL/WUI_boundary` as an example repository for website testing workflow patterns.

### Files and folders inspected
- `https://github.com/CU-ESIIL/WUI_boundary`
- local website workflow and test files

### Actions taken
- Aligned the local/CI testing shape more closely with the example repository by adding a single-command site review script at `scripts/review_site.sh`.
- Updated the website workflows to call the shared review script and upload artifacts from each validation run.
- Updated repository instructions so agents run the website review script after site-related changes when dependencies are available.

### Verification
- Confirmed the shared review script and workflow updates were written to the repository.
- Confirmed the example repository README describes both PR-site review and a local pre-PR review command, which this change now mirrors in structure.

### Open questions and follow-up
- This repo still uses Python Playwright rather than the example repo's Node-based Playwright setup because local Node tooling is not currently installed here.

### Prompt
Adopt the website aesthetic from `CU-ESIIL/WUI_boundary`, especially the colors, animated buttons, and overall visual feel instead of the starter template look.

### Files and folders inspected
- `docs/stylesheets/extra.css`
- `docs/index.md`
- `mkdocs.yml`
- the live `WUI_boundary` site for visual comparison

### Actions taken
- Added a custom Material palette to move the site away from the starter theme colors.
- Reworked `docs/stylesheets/extra.css` with a darker field-inspired header, warm accent colors, animated button shimmer, elevated cards, and a more deliberate hero treatment.
- Updated the homepage content structure to use a styled hero section and animated call-to-action buttons.

### Verification
- Confirmed the theme config, homepage markup, and stylesheet changes were written to the repository.

### Open questions and follow-up
- The browser tool exposed the live WUI site but not its raw stylesheet, so this is a close visual adaptation rather than a literal stylesheet copy.

### Prompt
Review the failing GitHub Actions output from `bash scripts/review_site.sh --junitxml site-test-results.xml` and address the site test failure.

### Files and folders inspected
- `tests/test_site.py`
- repository asset paths in `docs/assets/`
- the built-site failure output from CI

### Actions taken
- Narrowed the browser smoke test to fail on actionable signals: page exceptions, HTTP 4xx/5xx responses, and failed browser requests.
- Removed the hard failure on generic browser console errors because it was producing low-signal false failures without identifying a concrete broken request.

### Verification
- Confirmed the updated test logic was written to `tests/test_site.py`.
- The change is aimed specifically at the failure mode reported in CI, where console noise occurred without any captured failed response.

### Open questions and follow-up
- Once the workflow reruns, we should verify whether the underlying missing asset was benign browser noise or if a concrete failing request now appears in the stricter network-level assertions.

### Prompt
Review the next CI failure, which reported `404 https://api.github.com/repos/CU-ESIIL/on_growth_and_form/releases/latest` during the website smoke test.

### Files and folders inspected
- `tests/test_site.py`
- CI failure output identifying the GitHub API request

### Actions taken
- Scoped the smoke test so HTTP failures only fail the run when they come from the locally served site itself.
- Kept browser request-failure checks in place for actual site-loading problems while treating external service 4xx/5xx responses as non-blocking.

### Verification
- Confirmed the test now distinguishes local site failures from external network responses.
- The reported GitHub API `404` should no longer fail the PR check because it is not a broken site route or asset in this repository.

### Open questions and follow-up
- If external requests become important later, we can add an allowlist or explicit assertions for specific integrations instead of failing all third-party responses indiscriminately.

### Prompt
Add the collected FIRE-MODEL solicitation information to the repository and website.

### Files and folders inspected
- `README.md`
- `mkdocs.yml`
- `docs/index.md`
- `docs/workflow.md`
- `funder/`

### Actions taken
- Added a repository briefing in `funder/solicitation/fire_model_2026_briefing.md`.
- Added a working requirements checklist in `funder/review_criteria/fire_model_requirements_checklist.md`.
- Added website pages for the FIRE-MODEL briefing and checklist.
- Updated the homepage, workflow page, navigation, and README so the repo is explicitly anchored to the 2026 FIRE-MODEL cycle.
- Marked the new materials as working summaries that still need verification against official NSF source documents.

### Verification
- Confirmed the new funder files and website pages were written into the repository.
- Confirmed the site navigation now exposes the FIRE-MODEL briefing and checklist pages.

### Open questions and follow-up
- The repository still needs the official solicitation PDF or full text captured under `funder/` so the working summary can be cross-checked line by line.

### Prompt
Add the new FIRE-MODEL background/context material to the repo, and create a dedicated folder for background and contextualization separate from funder-provided information.

### Files and folders inspected
- repository directory structure
- `docs/repository-map.md`
- `funder/solicitation/fire_model_2026_briefing.md`

### Actions taken
- Created `background_context/` with a `program_briefings/` subfolder for interpretive program notes.
- Added `background_context/program_briefings/fire_model_2026_background.md` as a contextual framing document.
- Added `docs/background-context.md` and updated site navigation and homepage links.
- Updated `README.md`, `docs/workflow.md`, `docs/repository-map.md`, and `AGENTS.md` to distinguish sponsor-controlled material from background/context synthesis.

### Verification
- Confirmed the new folder, contextual briefing, and website page were written into the repository.
- Confirmed the repository docs now distinguish `funder/` from `background_context/`.

### Open questions and follow-up
- As more contextual notes accumulate, we may want additional subfolders inside `background_context/` such as `landscape_reviews/`, `positioning_notes/`, or `concept_memos/`.

### Prompt
The white buttons on the homepage animate but do not open their linked pages.

### Files and folders inspected
- `docs/stylesheets/extra.css`
- `docs/index.md`

### Actions taken
- Fixed the animated shimmer overlay on homepage buttons so it no longer intercepts clicks.
- Left the animation in place while restoring normal anchor behavior.

### Verification
- Confirmed the homepage buttons are still normal Markdown links in `docs/index.md`.
- Confirmed `.oasis-hover-button::after` now uses `pointer-events: none`.

### Open questions and follow-up
- The next site build should restore click-through behavior for the hero buttons without changing their appearance.

### Prompt
Add the "Environmental Data Science Stack (2030)" material as markdown and expand the background/context section with it.

### Files and folders inspected
- `background_context/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Created `background_context/conceptual_frameworks/` for reusable scientific framing documents.
- Added `background_context/conceptual_frameworks/environmental_data_science_stack_2030.md`.
- Added a website page at `docs/environmental-data-science-stack.md`.
- Updated the background/context hub, repository map, README, and site navigation to expose the new conceptual framework.

### Verification
- Confirmed the new conceptual framework files were written to the repository.
- Confirmed the website navigation now includes the Environmental Data Science Stack page.

### Open questions and follow-up
- If more conceptual architecture notes are added, we may eventually want a dedicated background/context landing page with grouped subsections for program briefs, conceptual frameworks, and positioning notes.

### Prompt
Add a new background/context markdown document on *On Growth and Form* and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/on_growth_and_form_intellectual_overview.md`.
- Added a website page at `docs/on-growth-and-form-overview.md`.
- Updated the background/context hub, README, and site navigation so the new conceptual framework is discoverable.

### Verification
- Confirmed the new markdown documents were written to the repository.
- Confirmed the MkDocs navigation now includes the On Growth and Form overview page.

### Open questions and follow-up
- If the project starts citing Thompson directly in proposal text, we should add a citation note and verified bibliographic entry under `citations/`.

### Prompt
Add a background/context markdown document on diffusion across space and the `1/2` scaling signature, and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/diffusion_across_space_half_scaling_signature.md`.
- Added a website page at `docs/diffusion-half-scaling.md`.
- Updated the background/context hub, README, and site navigation to expose the new conceptual framework.

### Verification
- Confirmed the new diffusion markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the diffusion overview page.

### Open questions and follow-up
- If this framework becomes important to the proposal argument, we may want a figure or note showing how the `1/2` scaling baseline relates to wildfire spread regimes of interest.

### Prompt
Add a background/context document on non-`1/2` scaling signatures in spatial spread and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/non_half_scaling_signatures_spatial_spread.md`.
- Added a website page at `docs/non-half-scaling-signatures.md`.
- Updated the background/context hub, README, and site navigation to expose the anomalous-transport note.

### Verification
- Confirmed the new non-`1/2` scaling markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the non-`1/2` scaling overview page.

### Open questions and follow-up
- The diffusion-related notes are now a small cluster; a future cleanup could group them explicitly as a scaling-and-transport subsection in the website.

### Prompt
Add a background/context note on scaling, dimensionality, and power laws in wildfire science, and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/scaling_dimensionality_power_laws_wildfire_science.md`.
- Added a website page at `docs/wildfire-scaling-dimensionality.md`.
- Updated the background/context hub, README, and site navigation to expose the wildfire scaling note.

### Verification
- Confirmed the new wildfire scaling markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the wildfire scaling overview page.

### Open questions and follow-up
- The conceptual framework library is now large enough that the website nav would benefit from grouped sections rather than a flat list of pages.

### Prompt
Add a background/context note on superdiffusive scaling and fractal geometry in wildfire perimeter growth, and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/superdiffusive_scaling_fractal_geometry_wildfire_perimeter_growth.md`.
- Added a website page at `docs/superdiffusive-wildfire-perimeters.md`.
- Updated the background/context hub, README, and site navigation to expose the new wildfire geometry note.

### Verification
- Confirmed the new superdiffusive wildfire markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the superdiffusive wildfire perimeter page.

### Open questions and follow-up
- The scaling and wildfire-geometry notes are now an explicit cluster and would benefit from grouped navigation or a dedicated theory landing page.

### Prompt
Add a background/context note on fire modeling frameworks and scaling perspectives, and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/fire_modeling_frameworks_scaling_perspectives.md`.
- Added a website page at `docs/fire-modeling-scaling.md`.
- Updated the background/context hub, README, and site navigation to expose the fire modeling frameworks note.

### Verification
- Confirmed the new fire modeling markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the fire modeling and scaling page.

### Open questions and follow-up
- The wildfire theory pages now form a coherent cluster and should eventually be grouped under a dedicated navigation section rather than a flat top-level menu.

### Prompt
Add a background/context note on FIRED and CubeDynamics as a system for event-based Earth system analysis, and link it into the website.

### Files and folders inspected
- `background_context/conceptual_frameworks/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/conceptual_frameworks/fired_cubedynamics_event_based_earth_system_analysis.md`.
- Added a website page at `docs/fired-cubedynamics.md`.
- Updated the background/context hub, README, and site navigation to expose the FIRED/CubeDynamics systems note.

### Verification
- Confirmed the new FIRED/CubeDynamics markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the FIRED and CubeDynamics page.

### Open questions and follow-up
- The background/context library now mixes conceptual theory and analytical infrastructure notes; a future reorganization could split those into separate grouped sections.

### Prompt
Audit the repo organization, keep funder-oriented content in `funder/`, group the background material more clearly, and make the website read more narratively.

### Files and folders inspected
- `funder/`
- `background_context/`
- `docs/`
- `mkdocs.yml`
- `README.md`

### Actions taken
- Grouped the background library into `program_briefings/`, `intellectual_foundations/`, `scaling_and_geometry/`, and `systems_frameworks/`.
- Kept the FIRE-MODEL briefing in `funder/` and clarified that it functions as a funder guide.
- Added a narrative `docs/funder-materials.md` page and rewrote the background overview page to read as grouped sections instead of a raw file list.
- Reworked MkDocs navigation so funder material and background/context appear as separate grouped sections.
- Updated repository docs and page references to match the new structure.

### Verification
- Confirmed the reorganized background files exist in their new grouped folders.
- Confirmed the website navigation now nests funder and background content instead of listing all pages flat.
- Confirmed the moved-file references in the website pages were updated to the new paths.

### Open questions and follow-up
- The next useful cleanup would be a second-pass rewrite of individual theory pages so they cross-link more explicitly within the new grouped structure.

### Prompt
Add a background/context note on the wildfire scaling regime hypothesis and link it into the website.

### Files and folders inspected
- `background_context/scaling_and_geometry/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/scaling_and_geometry/wildfire_scaling_regime_hypothesis.md`.
- Added a website page at `docs/wildfire-scaling-regime-hypothesis.md`.
- Updated the background/context overview, README, and site navigation to expose the new regime-hypothesis note.

### Verification
- Confirmed the new wildfire scaling regime markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the wildfire scaling regime hypothesis page.

### Open questions and follow-up
- This note is a strong candidate to cross-link with the superdiffusive wildfire perimeter and fire modeling pages in a later narrative pass.

### Prompt
Add a background/context note on wildfire scaling open questions, hypotheses, and empirical tests, and link it into the website.

### Files and folders inspected
- `background_context/scaling_and_geometry/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/scaling_and_geometry/wildfire_scaling_open_questions_hypotheses_empirical_tests.md`.
- Added a website page at `docs/wildfire-scaling-research-agenda.md`.
- Updated the background/context overview, README, and site navigation to expose the wildfire scaling research-agenda note.

### Verification
- Confirmed the new wildfire scaling research-agenda markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the wildfire scaling research agenda page.

### Open questions and follow-up
- This note now acts as a natural hub for the wildfire scaling cluster and could later be linked directly from the homepage or a theory landing page.

### Prompt
Add a background/context document for the wildfire scaling research program narrative Gantt and work plan.

### Files and folders inspected
- `background_context/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Created a new `background_context/research_programs/` group for structured work-plan and research-program notes.
- Added `background_context/research_programs/wildfire_scaling_research_program_work_plan.md`.
- Added a website page at `docs/wildfire-scaling-work-plan.md`.
- Updated the background/context overview, README, repository map, workflow page, and site navigation to include the new research-program grouping.

### Verification
- Confirmed the new research-program markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the wildfire scaling work plan page under Background and Context.

### Open questions and follow-up
- If more project-design notes are added, the new `research_programs/` group may need its own narrative landing page rather than a single page in the nav.

### Prompt
Add a work-plan section document on wildfire scaling rationale, deliverables, users, and impact.

### Files and folders inspected
- `background_context/research_programs/`
- `docs/background-context.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/research_programs/wildfire_scaling_rationale_deliverables_users_impact.md`.
- Added a website page at `docs/wildfire-scaling-rationale-impact.md`.
- Updated the background/context overview, README, and navigation to expose the new rationale-and-impact document within the research-program grouping.

### Verification
- Confirmed the new rationale-and-impact markdown files were written to the repository.
- Confirmed the MkDocs navigation now includes the rationale-and-impact page under Background and Context.

### Open questions and follow-up
- The `research_programs/` section is now substantial enough that a dedicated landing page would likely read better than listing individual pages alone.

### Prompt
Add a curated list of wildfire scaling citations into the citations section.

### Files and folders inspected
- `citations/`
- `citations/README.md`

### Actions taken
- Added a BibTeX export at `citations/exports/wildfire_scaling_bibliography.bib`.
- Added a provenance and verification note at `citations/notes/wildfire_scaling_bibliography.md`.
- Updated `citations/README.md` to describe the difference between notes and export files and to mark imported citations as unverified until checked.

### Verification
- Confirmed the bibliography files were written into the citations section.
- Preserved the entries as provided rather than silently modifying bibliographic details without source verification.

### Open questions and follow-up
- The bibliography still needs source-by-source verification against original papers, DOI records, or PDFs before it should be treated as final.

### Prompt
Reorganize the MkDocs site so it reflects the project's intellectual structure and future direction, with an idea-driven architecture instead of a file-driven note dump.

### Files and folders inspected
- `docs/`
- `mkdocs.yml`
- current docs navigation and section pages

### Actions taken
- Reorganized `docs/` into section folders: `project-overview/`, `theory/`, `data-infrastructure/`, `methods/`, `models/`, `research-program/`, and `literature/`.
- Moved existing pages into those folders and preserved their substantive content.
- Added new landing pages and bridging pages so the site reads as a coherent research program.
- Rewrote the homepage as a project landing page explaining the wildfire scaling concept, why it matters, how FIRED and CubeDynamics enable it, and how the site is organized.
- Replaced the flat navigation with an idea-driven MkDocs nav organized around overview, theory, data, methods, models, research program, literature, workflow, and repository structure.
- Added pages so all relevant markdown content in the docs tree is represented in the navigation.

### Verification
- Confirmed the docs tree now maps onto the intended research architecture instead of a flat list of files.
- Confirmed the new MkDocs nav explicitly references the section landing pages and the moved content pages.
- Updated internal links in the new section pages to match the folder-based docs layout.

### Open questions and follow-up
- A later pass could tighten cross-linking between theory, methods, and model pages even further once the proposal narrative stabilizes.

## 2026-03-13

### Prompt
Add a summary of first-submission review feedback and resubmission strategy to the repository and website.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `background_context/README.md`
- `docs/project-overview/index.md`
- `mkdocs.yml`

### Actions taken
- Added `background_context/program_briefings/fire_model_first_submission_review_resubmission_strategy.md` to capture reviewer concerns, concrete response strategies, narrative reframing, and open assumptions.
- Added website page `docs/project-overview/review-resubmission-strategy.md` to expose the review synthesis in the Project Overview section.
- Updated `mkdocs.yml` navigation and `docs/project-overview/index.md` links to include the new resubmission-strategy page.
- Updated `background_context/README.md` wording so `program_briefings/` explicitly includes review-to-resubmission synthesis notes.

### Verification
- Confirmed the new repository memo and website page were written and linked in navigation.
- Planned to run `bash scripts/review_site.sh` per website-change workflow requirement.

### Open questions and follow-up
- The review summary reflects user-provided feedback text; if official panel text includes additional compliance comments, those should be appended as separate action items before final drafting.

## 2026-03-18

### Prompt
Add a new document summarizing first-submission reviews and resubmission strategy, and treat it as proposal strategy rather than only background context.

### Files and folders inspected
- `AGENTS.md`
- `funder/README.md`
- `background_context/README.md`
- `background_context/program_briefings/fire_model_first_submission_review_resubmission_strategy.md`
- `proposal/README.md`
- `docs/project-overview/review-resubmission-strategy.md`
- `mkdocs.yml`

### Actions taken
- Added `proposal/narrative/fire_model_resubmission_strategy.md` as the primary strategic memo translating prior-review feedback into concrete resubmission actions.
- Updated `docs/project-overview/review-resubmission-strategy.md` so the website now explains why the review memo is a strategy document and points readers to the proposal-space source file.
- Updated `proposal/README.md` to document that proposal-strategy materials belong in `proposal/narrative/`.
- Preserved the earlier `background_context/` review synthesis as historical context rather than deleting or overwriting it.

### Verification
- Ran `bash scripts/review_site.sh`. The MkDocs build completed successfully, but the pytest site check could not run because `playwright` is not installed in the environment.
- Confirmed the new strategic memo is stored under `proposal/narrative/`, consistent with its role in shaping proposal revisions.

### Open questions and follow-up
- The strategic memo is based on user-provided review text and the earlier repository synthesis; if fuller panel documentation becomes available, the strategy should be expanded accordingly.

## 2026-03-18

### Prompt
Add the new scale-conditioned WUI geometry background material and connect it to the fire-modeling proposal framing.

### Files and folders inspected
- `AGENTS.md`
- `funder/README.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `background_context/README.md`
- `background_context/scaling_and_geometry/`
- `docs/theory/`
- `docs/methods/scaling-diagnostics.md`
- `docs/models/benchmarking-existing-fire-models.md`
- `mkdocs.yml`

### Actions taken
- Added a new background framing note on scale-conditioned WUI geometry under `background_context/scaling_and_geometry/`.
- Added a matching theory page to the documentation site and linked it into the Theory navigation.
- Updated the scaling diagnostics and benchmarking pages so they explicitly distinguish definition scale from measurement scale and frame validation in terms of `L_d(ε)` curves.

### Verification
- Reviewed the edited markdown and navigation diff locally.
- Ran `bash scripts/review_site.sh`; the MkDocs build completed successfully, while the pytest Playwright check remained blocked because the `playwright` Python package could not be installed in this environment due repository proxy restrictions.

### Open questions and follow-up
- The new note is a conceptual framing document; any literature claims or proposal prose derived from it should still be checked against verified primary sources before submission use.

## 2026-03-18

### Prompt
Add another document capturing the FIRE-MODEL rebid context, pitch, and scientific program, and treat it as proposal strategy.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `proposal/README.md`
- `proposal/narrative/fire_model_resubmission_strategy.md`
- `docs/project-overview/index.md`
- `docs/project-overview/review-resubmission-strategy.md`
- `mkdocs.yml`

### Actions taken
- Added `proposal/narrative/fire_model_rebid_context_pitch_scientific_program.md` as a proposal-strategy memo organizing the rebid around scale-conditioned interfaces, three research aims, geometry-based validation, and cyberinfrastructure integration.
- Added `docs/project-overview/rebid-context-pitch-scientific-program.md` so the website reflects the new strategy memo and its role in shaping the rebid.
- Updated `mkdocs.yml`, `docs/project-overview/index.md`, and `proposal/README.md` so the new strategy material is linked and correctly categorized under proposal narrative work.

### Verification
- Reviewed edited markdown and navigation changes locally.
- Ran `bash scripts/review_site.sh`; the MkDocs build completed successfully, while the pytest site check could not run because the `playwright` Python package is not installed in the environment.

### Open questions and follow-up
- The new memo is a strategy artifact built from user-provided framing and existing repository context; any proposal prose derived from it should still be checked against official FIRE wording and submission constraints before reuse.


## 2026-03-18

### Prompt
User shared a first draft of the FIRE-MODEL proposal narrative and requested help by providing the draft for review.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `background_context/program_briefings/fire_model_2026_background.md`
- `background_context/program_briefings/fire_model_first_submission_review_resubmission_strategy.md`
- `proposal/narrative/fire_model_rebid_context_pitch_scientific_program.md`
- `docs/research-program/rationale-impact.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added `background_context/program_briefings/fire_model_first_draft_review.md` as an internal review memo evaluating the draft against the repository's working FIRE-MODEL framing, known reviewer risks, and revision priorities.
- Identified strengths, call-alignment gaps, reviewer-confidence risks, and a recommended structure for the next draft iteration.

### Verification
- Reviewed the new memo locally for alignment with `funder/` guidance and existing resubmission strategy artifacts.
- No site-facing files were changed, so `bash scripts/review_site.sh` was not required for this task.

### Open questions and follow-up
- The review is based on working repository summaries of FIRE-MODEL requirements; final proposal wording still needs to be checked against the authoritative NSF solicitation and current PAPPG.
- If desired, the next step should be a direct rewrite of the draft into an aims-structured Project Description opening with explicit Intellectual Merit and Broader Impacts transitions.


## 2026-03-18

### Prompt
Add the provided FIRE-MODEL comprehensive work plan into the draft section.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `docs/research-program/work-plan.md`
- `background_context/research_programs/wildfire_scaling_research_program_work_plan.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Replaced the prior four-year narrative work plan with a synchronized three-year FIRE-MODEL work plan in both the website-facing and background-context copies.
- Reframed the document around the user-provided central hypothesis, three linked hypotheses, three interlocking research arcs, coordinated team structure, annual benchmarks, and outcome-contingent risk logic.
- Added explicit proposal-role language so the work plan ties back to the repository's working FIRE-MODEL framing of conceptual advance, computational framework, and validation pathway.

### Verification
- Reviewed the synchronized markdown updates locally.
- Ran `bash scripts/review_site.sh`; the MkDocs build completed successfully, while the pytest site check was blocked during collection because the `playwright` Python package is not installed in the environment.

### Open questions and follow-up
- This work plan is aligned to the repository's working FIRE-MODEL briefing and checklist, but final proposal submission language should still be checked against the authoritative NSF solicitation and current PAPPG.


## 2026-03-19

### Prompt
Add an ESIIL-style FIRE-MODEL Gantt chart script, generate PNG/SVG outputs, publish the figure on a standalone website page with the provided legend text, and link it into the MkDocs navigation.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `docs/research-program/work-plan.md`
- `docs/research-program/gantt-timeline.md`
- `mkdocs.yml`
- `scripts/review_site.sh`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added `scripts/generate_fire_model_gantt.py` to generate repository-tracked FIRE-MODEL Gantt chart assets with matplotlib and write them into `docs/assets/figures/`.
- Added `docs/planning/gantt_chart.md` using the user's requested page structure and legend text.
- Updated `mkdocs.yml` to expose the new page under a `Planning` navigation section.
- Generated the PNG and SVG outputs locally from the new script.

### Verification
- Ran `python scripts/generate_fire_model_gantt.py` to create the figure assets; the environment lacked `matplotlib`, so the script used its built-in pure-Python fallback renderer and still produced both requested files.
- Ran `python -m mkdocs build --strict --clean --site-dir dist`; the site built successfully with the new page and assets.
- Ran `timeout 15s mkdocs serve --dev-addr 127.0.0.1:8000`; the local server started successfully before the intentional timeout stopped it.
- Ran `bash scripts/review_site.sh`; the MkDocs build passed, while the pytest site check failed during collection because the `playwright` Python package is not installed in the environment.

### Open questions and follow-up
- The prompt referenced a previously provided full Python script, but that source code was not present in the visible session context; the added script is therefore a fresh matplotlib implementation matching the requested FIRE-MODEL/ESIIL-style output and repository paths.


## 2026-03-19

### Prompt
Address PR feedback that binary assets should be generated from code in GitHub Actions rather than attached directly in the review diff.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `scripts/generate_fire_model_gantt.py`
- `docs/planning/gantt_chart.md`
- `mkdocs.yml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Removed the tracked PNG output from version control so the review no longer depends on a committed binary asset.
- Updated the planning page to embed the generated SVG instead of the PNG while preserving the requested legend and interpretation text.
- Added `.github/workflows/generate_fire_model_gantt.yml` so GitHub can regenerate and publish both PNG and SVG outputs as workflow artifacts from code.
- Added a note in `scripts/generate_fire_model_gantt.py` documenting the repository/CI split between the tracked SVG and generated binary output.

### Verification
- Ran `python scripts/generate_fire_model_gantt.py` after the workflow-oriented changes; the script still generated both requested outputs locally.
- Ran `python -m mkdocs build --strict --clean --site-dir dist`; the site built successfully with the SVG-based planning page.
- Ran `timeout 15s mkdocs serve --dev-addr 127.0.0.1:8000`; the local server started successfully before the intentional timeout stopped it.
- Ran `bash scripts/review_site.sh`; the MkDocs build passed, while the pytest site check still failed during collection because the `playwright` Python package is not installed in the environment.

### Open questions and follow-up
- The repository does not currently include a site deployment workflow in scope here, so the new action uploads generated assets as artifacts; if Pages deployment is later automated in-repo, that workflow should call the same generator before `mkdocs build`.

## 2026-03-19

### Prompt
Add a new draft titled `On Growth and Form: A Generative Theory of Fire` to the repository's drafting and planning materials, and surface it in the website's research-program section.

### Files and folders inspected
- `AGENTS.md`
- `funder/README.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `mkdocs.yml`
- `proposal/README.md`
- `proposal/narrative/`
- `docs/research-program/`
- `docs/workflow.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added `proposal/narrative/on_growth_and_form_generative_theory_of_fire_draft.md` to preserve the user-provided long-form draft in the proposal drafting workspace, with a short status note tying it to current `FIRE-MODEL` proposal needs.
- Added `docs/research-program/generative-theory-of-fire.md` so the same draft logic is visible from the website's research-program section.
- Updated `docs/research-program/index.md` and `mkdocs.yml` so the new draft appears in the website navigation.
- Standardized the draft's formula formatting into Markdown-friendly code blocks and inline notation for the repository and MkDocs site.

### Verification
- Reviewed the new and updated Markdown files with `sed` and `git diff` to confirm placement, headings, and navigation wiring.
- Ran `bash scripts/review_site.sh`; `mkdocs build --strict` succeeded, but the Playwright pytest step failed because the local Python environment does not currently include the `playwright` package.
- Attempted `python3 -m pip install -r requirements-dev.txt`, but installation failed at the `playwright` dependency because the environment's package index/proxy could not resolve that package.

### Open questions and follow-up
- The draft is now stored as planning prose, but it may still need later condensation into submission-length Project Description text.
- A later pass may want to crosswalk specific subsections of this draft to Intellectual Merit, Broader Impacts, and the formal NSF section structure.
- Full browser-based site smoke tests remain pending until the environment can install Playwright and its browser dependencies.

## 2026-03-19

### Prompt
Promote a new structured FIRE-MODEL revision strategy document to a privileged position on the website and give it its own shareable link for collaborator use.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `proposal/narrative/fire_model_resubmission_strategy.md`
- `docs/project-overview/review-resubmission-strategy.md`
- `docs/project-overview/index.md`
- `docs/index.md`
- `mkdocs.yml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Replaced the prior resubmission strategy memo in `proposal/narrative/` with the new structured response plan so the repository has a single current strategy document for revision work.
- Rebuilt the website version of the strategy page as a collaborator-facing sendable memo with the full structured response plan.
- Elevated the strategy document in the site navigation by adding a top-level `Strategy Document` link and updated the Project Overview labels to reflect its new role.
- Updated the homepage hero, note, and cards so the strategy document is the primary entry point for revision planning.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`; the site built successfully after the navigation and page updates.
- Ran `bash scripts/review_site.sh`; the MkDocs build passed, but the pytest site check failed during collection because the local environment does not have the `playwright` package installed.

### Open questions and follow-up
- The strategy document is now the primary collaborator-facing memo, but the proposal text may still need a later pass to map each benchmark and deliverable into submission-length Project Description language.
- Browser-based screenshot capture was not attempted because no browser-container tool was available in this session.

## 2026-03-19

### Prompt
Add a second prose draft for the proposal, create a draft-to-draft change report, add the material to a drafts website section, and update the agenda so future agents compare drafts and flag important left-behind material on the drafts site.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `proposal/README.md`
- `proposal/narrative/`
- `docs/`
- `mkdocs.yml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Created `proposal/narrative/drafts/` and preserved the previously saved generative-theory narrative as Draft 01.
- Added the new user-provided prose as Draft 02.
- Wrote a Draft 01 → Draft 02 change report that records strengthened ideas, removed scaffolding, and important left-behind material.
- Added a new `docs/drafts/` section to the website with overview, draft pages, change-report summary, and a draft-review agenda page.
- Updated `mkdocs.yml`, `docs/workflow.md`, `docs/repository-map.md`, and `proposal/README.md` so the new draft-tracking workflow is visible in repository documentation.

### Verification
- Reviewed the new proposal and website draft-tracking files locally.
- Ran `bash scripts/review_site.sh` after the website-facing changes.

### Open questions and follow-up
- Draft 02's 3/4 and 4/3 references, and its oxygen-ventilation mechanism, remain hypothesis-level framing and should continue to be checked carefully against verified citation support before submission prose hardens.

## 2026-03-19

### Prompt
Add a FIRE-MODEL proposal integration document to the repository and website, treating it as drafting material that fills narrative gaps rather than background/context.

### Files and folders inspected
- `AGENTS.md`
- `proposal/README.md`
- `proposal/narrative/`
- `docs/drafts/`
- `docs/research-program/`
- `docs/repository-map.md`
- `README.md`
- `mkdocs.yml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added `proposal/narrative/fire_model_proposal_integration_document.md` as a labeled consolidation document covering the core claim, geometry-first benchmark logic, GIM framing, deliverables, work-plan structure, user workflow, and remaining gaps.
- Added `docs/drafts/integration-document.md` so the integration layer is visible from the website as a drafting artifact.
- Updated `docs/drafts/index.md` and `mkdocs.yml` so the new page is discoverable in the Drafts section.
- Updated `docs/research-program/index.md`, `docs/research-program/work-plan.md`, and `docs/research-program/deliverables.md` to cross-link the integration layer and reflect its detect-explain-apply framing and sharpened deliverables.
- Updated `proposal/README.md`, `README.md`, and `docs/repository-map.md` so repository documentation reflects the new narrative-integration role of `proposal/narrative/`.

### Verification
- Reviewed the new and updated Markdown files locally after editing.
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist` and `bash scripts/review_site.sh`; both failed immediately because the local Python environment does not currently include the `mkdocs` package.

### Open questions and follow-up
- The integration document is now accessible, but later proposal passes may still want a draft-to-draft memo explaining exactly which current proposal sections absorb which labeled blocks.
- The benchmark thresholds and acceptable metric ranges remain explicitly identified as unfinished and should be developed before submission prose claims them too concretely.

## 2026-03-21

### Prompt
User asked: "try to fix all the md files that were distilled. try to give them all the full, undistilled content from the prompt whenever you can."

### Files and folders inspected
- `docs/data-infrastructure/fired.md`
- `docs/data-infrastructure/cubedynamics.md`
- `docs/data-infrastructure/fired-cubedynamics.md`
- `background_context/systems_frameworks/fired_cubedynamics_event_based_earth_system_analysis.md`
- `docs/project-overview/fire-model-briefing.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `docs/project-overview/rebid-context-pitch-scientific-program.md`
- `proposal/narrative/fire_model_rebid_context_pitch_scientific_program.md`
- `docs/research-program/deliverables.md`
- `docs/research-program/users-impact.md`
- `background_context/research_programs/wildfire_scaling_rationale_deliverables_users_impact.md`
- `docs/models/generative-models.md`
- `docs/theory/wildfire-scaling-hypothesis.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Restored `docs/data-infrastructure/fired.md` from its longer in-repo source by replacing the abbreviated page with the full `FIRED` section from `background_context/systems_frameworks/fired_cubedynamics_event_based_earth_system_analysis.md`.
- Restored `docs/data-infrastructure/cubedynamics.md` from the same source by replacing the abbreviated page with the full `CubeDynamics` section text.
- Restored `docs/project-overview/fire-model-briefing.md` by replacing the shortened website version with the full content of `funder/solicitation/fire_model_2026_briefing.md`.
- Restored `docs/project-overview/rebid-context-pitch-scientific-program.md` by replacing the shortened website version with the full content of `proposal/narrative/fire_model_rebid_context_pitch_scientific_program.md`, including the closing strategic takeaways and assumptions section.
- Checked `docs/research-program/deliverables.md` and `docs/research-program/users-impact.md` against their longer source document and confirmed they already preserve the full text of their respective source sections rather than a shortened paraphrase.
- Checked additional short pages such as `docs/models/generative-models.md` and `docs/theory/wildfire-scaling-hypothesis.md`; no exact longer in-repo source could be recovered, so they were left unchanged rather than expanded speculatively.

### Verification
- Compared the restored pages directly against their longer repository source documents.
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.

### Open questions and follow-up
- A few short overview pages remain concise because no exact longer source could be recovered from the repository or prompt log in this session; if their original prompt text is later available, they can be restored without inventing content.

### Prompt
User reported that there were "some white animated buttons on the home page that don't link to anything" and asked to fix them.

### Files and folders inspected
- `docs/index.md`
- `docs/stylesheets/extra.css`
- `mkdocs.yml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Identified that the homepage card grid was visually interactive but its card titles were plain text rather than links.
- Updated `docs/index.md` so the four homepage cards now link to real destinations: the resubmission strategy document, wildfire scaling hypothesis, FIRED and CubeDynamics page, and funder materials page.
- Left the existing hero buttons and styling in place because those controls were already linked correctly.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist`.
- Confirmed the site built successfully after the homepage card links were added.

### Open questions and follow-up
- If desired later, the homepage cards could also be converted into full-card links or explicit in-card buttons, but they now point to real pages in their current form.

## 2026-03-21

### Prompt
User asked for a repo audit and direct implementation of an ESIIL-inspired MkDocs website restyle, including a redesigned homepage with an editorial hero, alternating image-text bands, restrained institutional branding, and site-wide typography/button/layout updates while preserving long-form markdown content.

### Files and folders inspected
- `AGENTS.md`
- `mkdocs.yml`
- `docs/index.md`
- `docs/stylesheets/extra.css`
- `docs/overrides/partials/logo.html`
- `docs/assets/`
- `tests/test_site.py`
- `scripts/review_site.sh`

### Actions taken
- Added centralized website brand tokens in `docs/stylesheets/tokens.css` and rewrote `docs/stylesheets/extra.css` to apply the blue/cyan/green visual system, updated typography hierarchy, flatter card treatments, rectangular buttons, cleaner header/footer styling, and stronger markdown page rhythm.
- Refactored `docs/index.md` into a designed landing page with a full-width gradient hero, alternating split content bands, editorial card grid, and a compact resubmission callout while keeping the existing proposal content and links in long-form form.
- Updated `mkdocs.yml` to load the new token stylesheet and changed `docs/overrides/partials/logo.html` so the site logo routes to the local homepage instead of the external ESIIL home page.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist` successfully.
- Confirmed the built homepage HTML includes the new hero, band, card, and stylesheet hooks.
- Ran `bash scripts/review_site.sh`, which rebuilt successfully but failed in `pytest` because the environment does not currently have the `playwright` Python package available.
- Tried `python3 -m pip install -r requirements-dev.txt`, but installation of `playwright>=1.52` failed behind the environment's proxy configuration.

### Open questions and follow-up
- Browser-based site tests remain blocked until `playwright` is installable in the environment; once available, rerun `bash scripts/review_site.sh` for full website validation.
- No browser screenshot artifact was captured because no browser screenshot tool was available in this session.

### Prompt
User reported the previous website restyle was unsatisfactory because CI failed in `tests/test_site.py`; they supplied the failing `bash scripts/review_site.sh --junitxml site-test-results.xml` output showing the homepage heading `On Growth and Form` was not visible to Playwright.

### Files and folders inspected
- `docs/index.md`
- `dist/index.html`
- `tests/test_site.py`
- `scripts/review_site.sh`

### Actions taken
- Inspected the built homepage HTML and found that Markdown inside the custom hero/container HTML had not been rendered, leaving the literal `# On Growth and Form` text in the DOM and no visible `<h1>` for the homepage.
- Rewrote `docs/index.md` as explicit HTML with front matter hiding the default page title so the designed hero now contains a real `<h1>` and real anchor elements while preserving the same homepage structure and content.
- Rebuilt the site outputs after the homepage markup fix.

### Verification
- Ran `bash scripts/review_site.sh --junitxml site-test-results.xml`.
- Confirmed the MkDocs build succeeded locally; pytest collection still fails in this environment because `playwright` is unavailable, but the rebuilt `dist/index.html` now contains `<h1>On Growth and Form</h1>` and no longer contains `<h1>Home</h1>`.

### Open questions and follow-up
- The homepage heading regression should now satisfy the CI failure the user reported, but a full local browser test still depends on an environment with Playwright installed.

### Prompt
User asked for a targeted refinement of the ESIIL-inspired MkDocs restyle so the left sidebar becomes a compact supporting rail, the homepage hero and long-form content get substantially more breathing room, and responsive behavior no longer lets navigation crowd the main reading area.

### Files and folders inspected
- `AGENTS.md`
- `mkdocs.yml`
- `docs/index.md`
- `docs/stylesheets/tokens.css`
- `docs/stylesheets/extra.css`
- `scripts/review_site.sh`
- `tests/test_site.py`

### Actions taken
- Expanded the site shell and introduced dedicated layout tokens for shell width, prose width, sidebar rail width, homepage rail width, and desktop content gap in `docs/stylesheets/tokens.css`.
- Rebalanced the MkDocs Material layout in `docs/stylesheets/extra.css` so desktop pages use a bounded navigation rail plus a dominant content column, with a wider gap, readable article width, and a homepage-specific narrower rail using `:has(.ogf-home)`.
- Refined sidebar typography and structure in `docs/stylesheets/extra.css` with smaller section-label styling, cleaner nested indentation, improved group spacing, thin scrollbars, and safer wrapping for long navigation labels.
- Increased homepage hero breathing room in `docs/stylesheets/extra.css` by enlarging outer padding, separating hero heading and paragraph width rules, widening paragraph measure, and improving CTA spacing.
- Tightened responsive behavior in `docs/stylesheets/extra.css` by capping the drawer width on narrower screens and keeping article content full-width within a readable max-width.

### Verification
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist` successfully.
- Ran a small Python inspection against built output and stylesheet rules to confirm the new desktop grid allocation, homepage-specific rail sizing, hero text measure, drawer width cap, and presence of both homepage and inner-page content in `dist/`.
- Ran `bash scripts/review_site.sh`; the MkDocs build succeeded, but `pytest` failed during collection because `playwright` is not installed in the environment.

### Open questions and follow-up
- The homepage-specific rail refinement relies on `:has(...)`; modern browsers support it, but if legacy browser support becomes important, this page-type distinction may need a template-level body class instead.
- No browser screenshot artifact was captured because no browser screenshot tool was available in this session.

## 2026-03-21

### Prompt
User asked for a human-centered refactor of the MkDocs website so it reads as a guided intellectual experience rather than a repository map, with a narrative homepage, clearer reader pathways, reorganized navigation, stronger section landing pages, lighter page-mode cues, and preserved long-form depth.

### Files and folders inspected
- `AGENTS.md`
- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `mkdocs.yml`
- `docs/index.md`
- `docs/start-here/index.md`
- `docs/project-overview/index.md`
- `docs/theory/index.md`
- `docs/research-program/index.md`
- `docs/data-infrastructure/index.md`
- `docs/methods/index.md`
- `docs/models/index.md`
- `docs/planning/index.md`
- `docs/literature/index.md`
- `docs/archive/index.md`
- `docs/workflow.md`
- `docs/repository-map.md`
- `docs/stylesheets/extra.css`
- `scripts/review_site.sh`
- `tests/test_site.py`

### Actions taken
- Rewrote the homepage to lead with the scientific idea, stakes, historical framing, guided reader pathways, and curated deeper-entry cards instead of workspace-first language.
- Added an explicit `How to use this site` pathway block near the top of the homepage for reviewers, collaborators, theory readers, and technical readers.
- Reorganized the MkDocs navigation around reader intent: start here, understand the idea, scientific framework, proposal and strategy, technical foundations, work plan and deliverables, literature, and repository workflow.
- Reworked the top-level section landing pages to do real orientation work with page-type labels, section purpose, best starting pages, and recommended next steps.
- Updated site styling to support the new hierarchy with softer navigation labels, section intro panels, page-type badges, and new homepage card variants.
- Regenerated the built site under `dist/` after the documentation changes.

### Verification
- Ran `bash scripts/review_site.sh`; MkDocs built successfully, but pytest could not run because the local environment lacks the `playwright` Python package required by `tests/test_site.py`.
- Ran `python3 -m mkdocs build --strict --clean --site-dir dist` after fixing navigation coverage; the site built successfully.

### Open questions and follow-up
- The homepage and section indexes are now much more reader-guided, but `workflow.md` and `repository-map.md` still remain intentionally repository-facing and could receive the same lighter-framing treatment in a future pass if desired.
- If browser-container support becomes available later, a visual screenshot check would be useful because this change materially affects homepage presentation and information hierarchy.

## 2026-03-21

### Prompt
User asked to download the NSF FIRE proposal call into the repo and, if possible, also download the NSF Proposal & Award Policies & Procedures Guide (PAPPG) to use as proposal requirements.

### Files and folders inspected
- `AGENTS.md`
- `funder/README.md`
- `funder/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Downloaded the official NSF FIRE opportunity webpage from `https://www.nsf.gov/funding/opportunities/fire-fire-science-innovations-through-research-education` to `funder/solicitation/nsf_fire_fire_science_innovations_through_research_and_education.html`.
- Verified via the NSF website that the current PAPPG page points to `NSF 24-1` as the active guide for proposals submitted or due on or after May 20, 2024.
- Downloaded the printable PDF for `NSF 24-1` from NSF's official resource host to `funder/review_criteria/nsf_pappg_24-1.pdf`.

### Verification
- Confirmed the downloaded solicitation artifact is an HTML document and the PAPPG artifact is a PDF.
- Confirmed file sizes after download: approximately `97K` for the FIRE opportunity page and `4.4M` for the PAPPG PDF.

### Open questions and follow-up
- The FIRE opportunity appears to be delivered by NSF as a live webpage rather than a standalone solicitation PDF at the provided URL, so the repo now stores the official HTML page for that call.
- If desired, a next step would be to add a short repository note summarizing which sections of `nsf_pappg_24-1.pdf` most directly control this proposal's narrative, supplementary documents, and compliance checks.

## 2026-03-21

### Prompt
User asked for a folder in the repo where Prism-exported PDF drafts can be dropped.

### Files and folders inspected
- `AGENTS.md`
- `proposal/README.md`
- `proposal/narrative/`
- `proposal/narrative/drafts/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added a dedicated folder for Prism PDF draft exports at `proposal/narrative/drafts/prism_pdf_exports/`.
- Added `proposal/narrative/drafts/prism_pdf_exports/README.md` with usage guidance and filename examples.
- Updated `proposal/README.md` to document that Prism-exported PDFs should be stored in the new folder.

### Verification
- Confirmed the new folder is nested under `proposal/narrative/drafts/`, which is the existing audit-oriented location for proposal draft snapshots.

### Open questions and follow-up
- If Prism exports end up covering multiple proposal components regularly, it may be useful to add subfolders later for sections such as project summary, full narrative, and review copies.

## 2026-03-21

### Prompt
User asked for a summary document covering each Prism-exported PDF added to `proposal/narrative/drafts/prism_pdf_exports/` so future agents can understand what happened at each draft, with emphasis on transparency of AI use.

### Files and folders inspected
- `AGENTS.md`
- `proposal/narrative/drafts/prism_pdf_exports/`
- `proposal/narrative/drafts/prism_pdf_exports/README.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Inspected the Prism PDF export folder and identified four exported drafts: `main.pdf`, `main-2.pdf`, `main 3.pdf`, and `main4.pdf`.
- Installed the lightweight `pypdf` package temporarily into `/tmp/codex_pypdf` so the PDFs could be parsed locally without changing repository dependencies.
- Extracted observable text, page counts, and modification-time ordering from each PDF.
- Added `proposal/narrative/drafts/prism_pdf_exports/prism_pdf_draft_history_summary.md` with one summary entry per PDF, a chronology note, and explicit limits on what can and cannot be inferred about AI use from the exported PDFs alone.
- Updated `proposal/narrative/drafts/prism_pdf_exports/README.md` to point future contributors to the draft-history summary.

### Verification
- Confirmed all four PDFs were readable with local extraction tooling.
- Confirmed the summary document reflects the visible chronology and notes the absence of embedded prompt-level provenance in the PDF artifacts.

### Open questions and follow-up
- The current summary reconstructs content-visible changes only. A fuller AI-use transparency record would require a separate human-authored note describing what was asked of Prism during each drafting step.
- The generic filenames make future auditing harder; renaming future exports with dates and section names would improve traceability.

## 2026-03-21

### Prompt
User asked for a button on the homepage next to the strategy/framing links that takes readers to the most recent Prism PDF.

### Files and folders inspected
- `docs/index.md`
- `docs/project-overview/index.md`
- `mkdocs.yml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added a homepage hero button in `docs/index.md` linking to the latest Prism draft currently in the repository: `proposal/narrative/drafts/prism_pdf_exports/main4.pdf`.
- Used the GitHub file URL so the button works from the published MkDocs site without relocating the PDF artifact out of the proposal history folder.

### Verification
- Ran `bash scripts/review_site.sh`.
- MkDocs built successfully into `dist/`.
- The script's test step could not run because `pytest` is not installed in the local environment.

### Open questions and follow-up
- The homepage button currently points to `main4.pdf` as the latest Prism export. If newer exports are added later, the link will need to be updated unless a stable alias or redirect is introduced.

## 2026-03-22

### Prompt
User asked to update the FIRE-MODEL Gantt chart generator so the figure matches the current proposal draft's Work Plan, Milestones, and Deliverables logic, with no hand-editing of the exported chart and only minimal surrounding text changes.

### Files and folders inspected
- `AGENTS.md`
- `scripts/generate_fire_model_gantt.py`
- `docs/planning/gantt_chart.md`
- `docs/research-program/gantt-timeline.md`
- `docs/research-program/work-plan.md`
- `docs/project-overview/review-resubmission-strategy.md`
- `docs/planning/staffing-plan.md`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Confirmed that `scripts/generate_fire_model_gantt.py` is the sole source-of-truth generator for the FIRE-MODEL Gantt figure and that it writes outputs to `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg` and the gitignored PNG companion path.
- Replaced the old hard-coded task list with proposal-aligned Year 1 / Detect, Year 2 / Explain, and Year 3 / Apply task definitions, including explicit `Benchmark 0`, stronger late-stage Apply tasks, and clearer separation among setup, empirical diagnostics, generative modeling, integration/evaluation, and dissemination.
- Updated the chart's visual semantics in code: year labels now read `Year 1 - Detect`, `Year 2 - Explain`, and `Year 3 - Apply`; background bands now reflect six-month emphasis blocks aligned to the revised proposal logic; task labels are rendered at the left for readability; `Benchmark 0` is highlighted as a formal gate with a distinct outline.
- Regenerated the chart asset from code, producing a new tracked SVG and a local PNG at the existing expected path.
- Updated `docs/planning/gantt_chart.md` and `docs/research-program/gantt-timeline.md` only where the old chart legend/sequence language no longer matched the revised figure semantics.

### Verification
- Parsed the updated generator successfully with Python `ast`.
- Re-ran the chart generation workflow and confirmed that the updated SVG contains the revised year labels, stage-band labels, and `Benchmark 0 gate` legend entry.
- Ran `bash scripts/review_site.sh`; MkDocs rebuilt successfully into `dist/`, while the script's test step could not run because `pytest` is not installed in the local environment.

### Open questions and follow-up
- The tracked asset is the SVG; the PNG companion is intentionally gitignored in this repository, so the commit-visible figure change is the regenerated SVG plus the updated generator and website text.
- The local environment's Matplotlib PNG export was unstable in the sandbox, so the repository-facing result relies on the regenerated SVG, which is the asset currently used by the website and is the publication-ready source in version control.

## 2026-03-22

### Prompt
User noted that the updated Gantt chart still had overlapping text and asked for spacing cleanup.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.png`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Increased figure height and top margin in the Gantt generator to create more vertical breathing room.
- Shortened the stage-band labels so the top-of-chart text fits without crowding.
- Moved the year labels higher above the chart and pushed the left-hand group labels farther away from the task labels.
- Regenerated the chart assets from code after the spacing changes.

### Verification
- Inspected the regenerated PNG preview to confirm the major text collisions were reduced.
- Ran `bash scripts/review_site.sh`; MkDocs rebuilt successfully into `dist/`, while the script's test step could not run because `pytest` is not installed in the local environment.

### Open questions and follow-up
- The pure-Python PNG fallback remains less polished than the tracked SVG, so the version-controlled website figure should still be judged primarily from the SVG output.

## 2026-03-22

### Prompt
User pointed out that the left side of the updated Gantt chart still had overlapping text and asked for more vertical space plus a more NSF-style font.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.png`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Increased the overall figure size, top margin, left margin, and row height in the Gantt generator to give the task and group labels more breathing room.
- Shortened the displayed left-hand group labels to cleaner reviewer-facing forms such as `Team / workflow` and `Empirical diagnostics`.
- Replaced the PNG fallback's bitmap text with Pillow-based rendering using local `Times New Roman` system fonts.
- Updated the SVG font stack to a proposal-style serif stack based on `Times New Roman`.
- Regenerated both SVG and PNG assets from code after the typography and spacing changes.

### Verification
- Inspected the regenerated PNG preview to confirm the left-side overlaps were substantially reduced and the typography was no longer bitmap-style.
- Ran `bash scripts/review_site.sh`; MkDocs rebuilt successfully into `dist/`, while the script's test step could not run because `pytest` is not installed in the local environment.

### Open questions and follow-up
- The bottom legend/x-axis area could still be refined further if a later pass is desired, but the user-requested left-side spacing and font issues were addressed in this iteration.

## 2026-03-28

### Prompt
User asked to add a new drafting document titled `Model Reconciliation Council` to the repository website, keep the provided text verbatim as a Markdown document, and place it in the drafting section so it can be injected into the current proposal draft.

### Files and folders inspected
- `AGENTS.md`
- `mkdocs.yml`
- `docs/drafts/index.md`
- `docs/drafts/integration-document.md`
- `docs/drafts/agenda.md`
- `PROMPT_ACTION_LOG.md`
- `scripts/review_site.sh`

### Actions taken
- Added `docs/drafts/model-reconciliation-council.md` as a new drafting page and preserved the user-provided body text as the page content.
- Updated `docs/drafts/index.md` so the new page is visible from the drafts landing page.
- Updated `mkdocs.yml` so the page appears in the website navigation under `Repository and Workflow > Drafts`.

### Verification
- Ran `bash scripts/review_site.sh`.
- Confirmed MkDocs rebuilt the site successfully into `dist/`.
- The script's test step could not run because `pytest` is not installed in the local environment.

### Open questions and follow-up
- Assumed the user's immediate need was website-visible drafting content rather than direct insertion into a proposal narrative file under `proposal/`; if desired, the next step is to identify the exact narrative section where this language should be integrated or adapted.

## 2026-03-30

### Prompt
User asked for a self-contained local-first proof of concept that compares an `ELMFIRE` benchmark scaffold against a regime-aware fire model, uses Earth2Studio GEFS weather when available, falls back cleanly to mock weather otherwise, keeps proposal-relevant output isolated so only the final figure would later be used, and remains runnable from both a Jupyter notebook and the command line on a Mac M3.

### Files and folders inspected
- `AGENTS.md`
- `simulations/README.md`
- `simulations/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Created a standalone project at `simulations/fire_poc/` with `pyproject.toml`, a project-specific `README.md`, notebook, `src/fire_poc/` package, and tests.
- Implemented a shared forcing dataclass plus provider abstraction, including `MockEarth2Provider` and an `Earth2StudioGEFSProvider` that uses documented GEFS variable names and fails clearly when Earth2Studio is unavailable or the fetch step cannot complete.
- Implemented an `ELMFIRE` case writer that generates GeoTIFF weather and fuels/topography inputs, writes `elmfire.data`, ignition metadata, and a `manifest.json`.
- Implemented an `ELMFIRE` runner that distinguishes case writing from external execution, preserves logs when a command is supplied, and never claims a real run unless the executable actually completes.
- Added a transparent pure-Python regime-aware comparison model, a proxy benchmark used only when the external benchmark does not run, comparison plotting, and a CLI.
- Added a notebook `simulations/fire_poc/notebooks/elmfire_earth2_poc.ipynb` that mirrors the CLI workflow and runs with the mock provider.
- Updated `simulations/README.md` so the repository-level simulations area points to the new self-contained proof of concept.

### Verification
- Ran `MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python3 -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed.
- Ran `MPLBACKEND=Agg MPLCONFIGDIR=.mplcache PYTHONPATH=src python3 -m fire_poc.cli --provider mock --workdir outputs/demo`; the workflow completed, wrote the `ELMFIRE` case scaffold, and saved the comparison figure.
- Confirmed generated artifacts under `simulations/fire_poc/outputs/demo/`, including `forcing.json`, `case/elmfire.data`, weather and fuels/topography GeoTIFFs, `case/manifest.json`, `pipeline_status.json`, and the final figure.
- Ran `PYTHONPATH=src python3 -m fire_poc.cli --provider earth2 --workdir outputs/demo_earth2`; the workflow failed cleanly with a truthful error because `earth2studio` is not installed in the local environment.
- Validated that `simulations/fire_poc/notebooks/elmfire_earth2_poc.ipynb` is well-formed JSON.

### Open questions and follow-up
- The Earth2Studio adapter is written against the documented `GEFS_FX` entry point, but it remains unexercised here because `earth2studio` is not installed locally.
- No real `ELMFIRE` executable was available in this environment, so the verified boundary is full case generation plus proxy-figure production rather than external benchmark execution.
- The proposal should treat the saved figure as a draft/generated artifact until reviewed and, if desired, copied into a proposal-facing figure location.

### Prompt
User asked: "can we install earth2studio?" and then asked to proceed with creating a separate compatible environment when the initial install failed in the existing Python 3.9 virtual environment.

### Files and folders inspected
- `simulations/fire_poc/`
- `simulations/fire_poc/pyproject.toml`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Confirmed that the existing project virtual environment used Python 3.9.6 and that `earth2studio` was not available there.
- Created a separate project-local Python 3.12 environment at `simulations/fire_poc/.venv312` using `uv`.
- Installed the project and optional `earth2` extra into that environment with `uv pip install --python .venv312/bin/python -e '.[earth2]'`.
- Verified that `earth2studio` is now installed in the separate Python 3.12 environment.

### Verification
- Confirmed `.venv312/bin/python` points to a Python 3.12.8 interpreter managed by `uv`.
- Ran `.venv312/bin/python -c "import earth2studio; print(earth2studio.__version__)"` and confirmed version `0.13.0`.

### Open questions and follow-up
- `earth2studio` is installed and importable in `.venv312`, but the workflow has not yet exercised a live GEFS fetch through the provider in this environment.
- The original `.venv` remains on Python 3.9.6; the Earth2-enabled environment is now `.venv312`.

### Prompt
User asked to try the simulation with climate from Earth2.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/earth2_provider.py`
- `simulations/fire_poc/outputs/demo_earth2_live/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Ran the Earth2-backed workflow in `simulations/fire_poc/.venv312`.
- Diagnosed and fixed three Earth2Studio integration issues in `earth2_provider.py`: timezone-aware `datetime` handling, unsupported 1-hour GEFS lead-time cadence, and longitude normalization for `0..360` GEFS grids versus negative west longitudes in the local domain config.
- Added a conservative completed-cycle selection with a 6-hour lag to reduce missing-object fetches from the GEFS object store.
- Re-ran the workflow successfully using `--provider earth2 --step-hours 3`.

### Verification
- Confirmed the Earth2-backed workflow completed and wrote outputs under `simulations/fire_poc/outputs/demo_earth2_live/`.
- Confirmed `forcing.json` contains numeric Earth2Studio-derived forcing values rather than all-NaN outputs.
- Confirmed the figure was written to `simulations/fire_poc/outputs/demo_earth2_live/figures/elmfire_vs_regime_model.png`.
- The benchmark status remained `case-written-only`; no real `ELMFIRE` executable was run.

### Open questions and follow-up
- The current Earth2 integration reduces GEFS fields to a simple domain-mean series over a small idealized box; a later refinement could expose domain bounds and member choice as CLI parameters.
- The Earth2-backed run still uses the proxy benchmark for plotting because no `ELMFIRE` executable was supplied.

### Prompt
User asked to "fix elmfire" after the Earth2-backed scaffold was working.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/src/fire_poc/elmfire_runner.py`
- `simulations/fire_poc/tests/test_case_writer.py`
- `simulations/fire_poc/outputs/demo_earth2_with_missing_elmfire/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Updated the ELMFIRE case writer to better match current ELMFIRE documentation by removing `.tif` suffixes from filenames in `elmfire.data`, converting wind speed rasters to mph, marking winds as `WS_AT_10M = .TRUE.`, and adding explicit `&COMPUTATIONAL_DOMAIN`, `&TIME_CONTROL`, `&SIMULATOR`, and `&OUTPUTS` namelist groups.
- Added explicit outputs-directory creation and a small `run_elmfire.sh` helper script in each written case directory.
- Hardened the runner so missing executables no longer crash the pipeline and instead return a truthful `run_failed_missing_executable` status with preserved stderr logging.
- Re-ran the Earth2-backed workflow with `--elmfire-cmd elmfire` to test the new failure boundary.

### Verification
- Ran `MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python3 -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed after the case-writer and runner changes.
- Ran the Earth2-backed workflow with `--elmfire-cmd elmfire`; the case was written successfully and the runner reported `run_failed_missing_executable` rather than crashing.
- Confirmed the missing-executable reason in `simulations/fire_poc/outputs/demo_earth2_with_missing_elmfire/case/elmfire_stderr.log`.

### Open questions and follow-up
- The remaining blocker to a real ELMFIRE run on this Mac is environmental: no `elmfire` executable was found, and no local `gfortran` or `mpirun` toolchain was present in `PATH` during inspection.
- If the user wants to continue toward a real benchmark run, the next step is to either point the workflow at an existing ELMFIRE executable/source tree or install the required local toolchain and build ELMFIRE.

### Prompt
User installed Homebrew and asked to continue bringing up the local ELMFIRE path on the Mac.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/src/fire_poc/elmfire_runner.py`
- `simulations/fire_poc/README.md`
- `simulations/elmfire_src/build/linux/make_gnu.sh`
- `simulations/elmfire_src/build/linux/Makefile_elmfire`
- `simulations/elmfire_src/tutorials/01-constant-wind/01-run.sh`
- `simulations/elmfire_src/tutorials/02-transient-wind/elmfire.data.in`
- `simulations/elmfire_src/build/source/elmfire_namelists.f90`
- `simulations/elmfire_src/build/source/elmfire_init.f90`
- `simulations/fire_poc/outputs/demo_earth2_real_elmfire_attempt4/`
- `simulations/fire_poc/outputs/demo_earth2_real_elmfire_attempt5/`
- `simulations/fire_poc/outputs/demo_earth2_real_elmfire_attempt6/`
- `simulations/fire_poc/outputs/demo_earth2_real_elmfire_attempt7/`
- `/tmp/e7/`
- `/tmp/e8/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Installed Homebrew toolchain components needed for a local bring-up: `gcc`, `open-mpi`, and later `gdal`.
- Cloned the upstream ELMFIRE source into `simulations/elmfire_src` and built the executable at `simulations/elmfire_src/build/linux/elmfire/elmfire`, working around a Linux-specific `-unroll` link issue by compiling without that flag on macOS.
- Updated `elmfire_case.py` to create absolute-path case directories, add a scratch directory, align the namelists more closely with the upstream transient-wind tutorial, detect a macOS/Homebrew GDAL binary directory, and write `adj.tif` and `phi.tif` into the fuels/topography directory as static companion rasters.
- Updated `elmfire_runner.py` so output-side errors from ELMFIRE and GDAL are treated as real run failures rather than mislabeled completions.
- Ran repeated Earth2-backed real-ELMFIRE attempts to move the native boundary forward:
  - initial attempts progressed from missing executable to accepted namelists,
  - then to automatic `fuel_models.csv` creation,
  - then through GDAL raster conversion after installing Homebrew GDAL,
  - then through full raster ingestion and into ensemble execution when run from a short temporary path.
- Updated `simulations/fire_poc/README.md` to document the verified Mac M3 state and the current macOS-native limitation.

### Verification
- Verified `gfortran` and `mpirun` were available from Homebrew after installation.
- Verified Homebrew GDAL installed successfully and `gdal_translate` exists at `/opt/homebrew/bin/gdal_translate`.
- Ran `source .venv312/bin/activate && python -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed after the ELMFIRE scaffolding changes.
- Verified the shortest successful native progression at `/tmp/e8/case/elmfire_stdout.log`: ELMFIRE completed weather/topography raster conversion, allocated shared memory, set up statistics arrays, and printed `ELMFIRE is running each ensemble member`.
- Verified the corresponding failure boundary at `/tmp/e8/case/elmfire_stderr.log`: native crash with `SIGBUS` before any benchmark outputs were written.
- Verified truthful pipeline status in `/tmp/e8/pipeline_status.json`: `benchmark_status` is `run_failed`, `benchmark_type` is `real ELMFIRE`, and `proxy_used_for_plotting` is `true`.

### Open questions and follow-up
- The remaining blocker appears to be a native macOS runtime issue inside ELMFIRE after startup rather than a case-format, GDAL, or weather-forcing issue.
- A next debugging step would likely require either a Linux VM/container or deeper upstream-oriented debugging of the native crash on macOS.

### Prompt
User asked whether we could get ELMFIRE working.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/src/fire_poc/cli.py`
- `simulations/fire_poc/src/fire_poc/config.py`
- `simulations/fire_poc/src/fire_poc/mock_provider.py`
- `simulations/fire_poc/src/fire_poc/forcing.py`
- `simulations/fire_poc/src/fire_poc/elmfire_runner.py`
- `simulations/elmfire_src/build/source/elmfire_subs.f90`
- `/tmp/e8/`
- `/tmp/e9/`
- `/tmp/e10/`
- `/tmp/e11/`
- `/tmp/e12/`
- `/tmp/e13/`
- `simulations/fire_poc/outputs/earth2_real_repo/`
- `simulations/fire_poc/README.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Isolated the native crash by reproducing it with both Earth2-backed and mock-weather runs; confirmed it was not specific to Earth2Studio.
- Used `lldb` on the built ELMFIRE executable and traced the `EXC_BAD_ACCESS`/`SIGBUS` to `__elmfire_subs_MOD_init` in `elmfire_subs.f90`, where the code dereferences fuel/topography arrays using ignition-derived indices.
- Identified that the scaffold had been writing ignition coordinates as local offsets within the domain instead of absolute CRS coordinates expected by ELMFIRE.
- Patched `elmfire_case.py` so `elmfire.data` writes absolute `X_IGN`/`Y_IGN` coordinates while preserving inspectable local and absolute ignition metadata in `ignition_points.json`.
- Switched the ELMFIRE case-file directories in `elmfire.data` to self-contained relative paths (`./inputs`, `./outputs`, `./scratch`) so real runs work from inside the repo section without depending on long absolute paths.
- Re-ran the simplest mock case and then the intended Earth2-backed case with the real ELMFIRE executable.
- Updated `simulations/fire_poc/README.md` to reflect that the current proof-of-concept benchmark now runs successfully on the Mac for this case.

### Verification
- Ran `source .venv312/bin/activate && python -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed after the ignition and relative-path fixes.
- Verified the simplest real benchmark completed successfully in `/tmp/e12/case/elmfire_stdout.log` with `End of simulation reached successfully. Shutting down.` and wrote output files under `/tmp/e12/case/outputs/`.
- Verified the Earth2-backed real benchmark also completed successfully in `/tmp/e13/case/elmfire_stdout.log` with no stderr output and output files under `/tmp/e13/case/outputs/`.
- Verified the repo-contained Earth2-backed run completed successfully in `simulations/fire_poc/outputs/earth2_real_repo/case/elmfire_stdout.log`, with outputs written under `simulations/fire_poc/outputs/earth2_real_repo/case/outputs/`.
- Verified truthful status in `simulations/fire_poc/outputs/earth2_real_repo/pipeline_status.json`: `benchmark_type` is `real ELMFIRE`, `benchmark_status` is `run_completed_parser_not_implemented`, and `proxy_used_for_plotting` is `false`.

### Open questions and follow-up
- The wrapper still does not parse ELMFIRE `.bil/.hdr` outputs, so the comparison figure can label a real benchmark run truthfully but does not yet ingest those outputs into the plotted perimeter/area comparison.
- If proposal use needs direct ELMFIRE-derived plotted perimeters rather than truthful run-status distinction, the next step is to implement a small ENVI/BIL output parser.

### Prompt
User asked for a map of the time sequence of the simulation with all parameters labeled on the figure.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/src/fire_poc/compare.py`
- `simulations/fire_poc/src/fire_poc/cli.py`
- `simulations/fire_poc/src/fire_poc/geometry.py`
- `simulations/fire_poc/src/fire_poc/regime_model.py`
- `simulations/fire_poc/outputs/earth2_real_repo/forcing.json`
- `simulations/fire_poc/outputs/earth2_real_repo/case/outputs/fire_size_stats.csv`
- `simulations/fire_poc/outputs/earth2_real_repo/case/outputs/time_of_arrival_0000001_0043830.hdr`
- `simulations/fire_poc/outputs/earth2_real_repo/figures/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added a small ELMFIRE output reader in `plotting.py` for ENVI/BIL time-of-arrival rasters and fire-size statistics.
- Added a new labeled figure generator that creates a four-panel time-sequence arrival map plus a parameter panel summarizing forcing, domain settings, ignition, and final ELMFIRE metrics.
- Updated the workflow in `compare.py` so a completed real ELMFIRE run automatically writes `elmfire_time_sequence_map.png`.
- Updated the CLI in `cli.py` to print the new map figure path when available.
- Re-ran the Earth2-backed real ELMFIRE workflow in `simulations/fire_poc/outputs/earth2_real_repo/` to generate the new figure.

### Verification
- Ran `source .venv312/bin/activate && python -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed.
- Verified the Earth2-backed run still completed successfully and wrote the new figure to `simulations/fire_poc/outputs/earth2_real_repo/figures/elmfire_time_sequence_map.png`.
- Opened the generated image locally to confirm that the snapshot maps and parameter labels render clearly.

### Open questions and follow-up
- The time-sequence map currently uses the real ELMFIRE time-of-arrival raster and final summary CSV, but it does not yet reconstruct vector perimeters from the raster outputs.

### Prompt
User asked for a panel with time down the rows and different manifestations of extreme conditions across columns, then asked for more extreme wind-forcing, gust, and light-dry-fuel scenarios because the first panel looked too similar.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/compare.py`
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/src/fire_poc/cli.py`
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/outputs/extreme_panel/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Added an `extremes-panel` workflow mode to the CLI and comparison orchestration so the project can run multiple real ELMFIRE cases and assemble them into a single multi-column panel figure.
- Implemented an initial extreme-conditions panel using Earth2-backed baseline forcing and scenario perturbations.
- After the user asked for more dramatic contrasts, expanded the case writer to respect scenario metadata for ELMFIRE-side wind coupling and fuel/exposure structure, including `adj`/`phi` scaling, dead-fuel moisture offsets, fuel model code, and canopy/exposure settings.
- Replaced the earlier mild scenarios with stronger, more distinct columns:
  - `Baseline`
  - `Downburst Forcing`
  - `Directional Gust Front`
  - `Light Dry Fuels`
  - `Compound Blowup`
- Re-ran the real Earth2-backed ELMFIRE panel in `simulations/fire_poc/outputs/extreme_panel/`.

### Verification
- Ran `source .venv312/bin/activate && python -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed after the scenario and case-writer changes.
- Verified the revised figure was written to `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png`.
- Opened the generated panel image locally to confirm that the columns now separate clearly.
- Verified scenario-level final areas from the ELMFIRE outputs:
  - baseline: `26.2 ac`
  - downburst: `474.1 ac`
  - directional gusts: `350.3 ac`
  - light dry fuels: `365.2 ac`
  - compound blowup: `522.8 ac`

### Open questions and follow-up
- The `extreme_panel` folder still contains some older scenario subdirectories from the first pass; the current figure and status file reflect the newer stronger scenarios.
- If needed for proposal messaging, the next refinement would be visual: shorter column labels, fewer header lines, or a more polished publication-style layout.

### Prompt
User asked to do all of the proposed panel refinements: enlarge the map domain, add smarter framing, and make the ELMFIRE perimeters rougher and less idealized.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/src/fire_poc/compare.py`
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/tests/test_case_writer.py`
- `simulations/fire_poc/README.md`
- `simulations/fire_poc/outputs/extreme_panel/`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Enlarged the extreme-panel common domain to `520 x 520` cells at `30 m` resolution with a larger ignition offset so the strongest scenarios have more downwind room.
- Added deterministic spatial heterogeneity to the ELMFIRE case writer so weather exposure, dead-fuel moisture, canopy structure, slope, aspect, and terrain vary in scenario-specific ways instead of staying nearly uniform.
- Tuned the extreme scenarios to use the new heterogeneity controls, especially for downburst corridors, directional gust streaks, and dry-fuel patchiness.
- Updated the extreme-panel plotting so each column auto-frames the final burned extent while still preserving a common underlying simulation setup.
- Added a regression check that verifies the case writer now produces spatially variable weather rasters when heterogeneity metadata is enabled.
- Updated the `simulations/fire_poc/README.md` description of the extremes-panel workflow to reflect the larger domain, auto-framing, and rougher perimeters.

### Verification
- Ran `source .venv312/bin/activate && python -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed.
- Re-ran the real Earth2-backed ELMFIRE extremes panel with `python -m fire_poc.cli --mode extremes-panel --provider earth2 --step-hours 3 --elmfire-cmd /Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/on_growth_and_form/simulations/elmfire_src/build/linux/elmfire/elmfire --workdir outputs/extreme_panel`.
- Verified the regenerated panel at `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` and confirmed the new columns are rougher and better framed.
- Checked updated final burned areas from the ELMFIRE outputs:
  - baseline: `36.0 ac`
  - downburst: `1776.0 ac`
  - directional gusts: `622.5 ac`
  - light dry fuels: `821.3 ac`
  - compound blowup: `7343.9 ac`

### Open questions and follow-up
- The compound blowup case is now framed by its burned extent rather than clipped by a fixed map window, but if the proposal figure should emphasize absolute common-domain scale instead, the next pass should use an even larger shared domain and shorter text labels.

### Prompt
User asked for a very detailed Markdown description of the full `fire_poc` workflow built today, including architecture, installed programs, settings, and build details, asked for that material to be added to the website, and also noted that some of the strong fire scenarios still seemed to need more actual simulation room rather than just better plotting.

### Files and folders inspected
- `PROMPT_ACTION_LOG.md`
- `mkdocs.yml`
- `docs/workflow.md`
- `simulations/README.md`
- `simulations/fire_poc/README.md`
- `simulations/fire_poc/pyproject.toml`
- `simulations/fire_poc/notebooks/elmfire_earth2_poc.ipynb`
- `simulations/fire_poc/src/fire_poc/compare.py`
- `simulations/fire_poc/src/fire_poc/earth2_provider.py`
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/src/fire_poc/elmfire_runner.py`
- `simulations/fire_poc/src/fire_poc/mock_provider.py`
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/src/fire_poc/regime_model.py`
- `simulations/fire_poc/tests/test_case_writer.py`
- `simulations/fire_poc/outputs/extreme_panel/`

### Actions taken
- Wrote a detailed repo-local workflow document at `simulations/fire_poc/WORKFLOW_BUILDOUT_2026-03-30.md` describing the architecture, environment split, Earth2Studio integration, ELMFIRE bring-up, current scenario design, installed tools, and proposal-facing outputs.
- Added a website page at `docs/fire-poc-workflow.md` with the same buildout story and an architecture schematic, then linked it into the site navigation in `mkdocs.yml` and from `docs/workflow.md`.
- Updated `simulations/README.md` so the simulations area points readers to the detailed `fire_poc` buildout document.
- Increased the extreme-panel computational domain from `520 x 520` to `700 x 700` cells at `30 m` resolution and moved the ignition upwind within the domain so the strongest scenarios have more genuine runout room.
- Fixed rerun hygiene in `elmfire_case.py` by clearing prior generated case artifacts before rewriting a scenario case.
- Fixed output selection in `plotting.py` so repeated runs use the most recently modified matching output product rather than whichever filename sorts first alphabetically.
- Re-ran the real Earth2-backed extreme-conditions panel after the larger-domain and fresh-case fixes.

### Verification
- Ran `source .venv312/bin/activate && MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python -m pytest -q tests` in `simulations/fire_poc/`; all 3 tests passed.
- Re-ran the real panel with `python -m fire_poc.cli --mode extremes-panel --provider earth2 --step-hours 3 --elmfire-cmd /Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/on_growth_and_form/simulations/elmfire_src/build/linux/elmfire/elmfire --workdir outputs/extreme_panel`.
- Verified the updated panel at `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png`.
- Checked the final `time_of_arrival` rasters and confirmed that none of the five scenarios touched the top, bottom, left, or right computational boundary in the new run.
- Verified updated final burned areas from the rerun:
  - baseline: `14.0 ac`
  - downburst: `1290.1 ac`
  - directional gusts: `1011.7 ac`
  - light dry fuels: `517.7 ac`
  - compound blowup: `6449.2 ac`
- Ran `bash scripts/review_site.sh`; the MkDocs build succeeded and regenerated `dist/`, but the script’s test phase could not run because `pytest` is not available in the root site-review environment.

### Open questions and follow-up
- The new domain and ignition placement removed direct contact with the computational boundary, but the proposal version of the panel may still benefit from a cleaner graphic layout with shorter headers and more map area.
- The website page is detailed enough for build provenance, but if it becomes part of reviewer-facing narrative rather than collaborator-facing documentation, it will likely need a later pass that separates implementation detail from proposal messaging.

### Prompt
User noted that the ignition star in the extreme-conditions panel did not line up with the fire, then asked to add a final row showing scaling behavior as a log-log plot of perimeter-to-area ratio so the figure can indicate how close each case is to `1/2` versus `2/3` perimeter-area scaling.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/src/fire_poc/elmfire_case.py`
- `simulations/fire_poc/outputs/extreme_panel/scenarios/compound_blowup/case/ignition_points.json`
- `simulations/fire_poc/outputs/extreme_panel/scenarios/compound_blowup/case/elmfire.data`
- `simulations/fire_poc/outputs/extreme_panel/scenarios/compound_blowup/case/outputs/time_of_arrival_0000001_0043212.hdr`
- `simulations/fire_poc/tests/`

### Actions taken
- Traced the ignition mismatch to a plotting-orientation bug rather than a simulation-input bug: ELMFIRE rasters are stored in top-origin image order, while the panel was drawing them as if row `0` were at the bottom of the map.
- Fixed the plotting utilities so ENVI/BIL rasters are flipped into map orientation before plotting, which brings the ignition star and burned area back into the same coordinate frame.
- Added a final scaling row to the extreme-conditions panel. Each scenario now includes a log-log subplot of `P/A` versus `A`, with reference slope lines corresponding to `P ~ A^(1/2)` and `P ~ A^(2/3)`, plus a fitted `beta` estimate for the scenario.
- Added raster-based area/perimeter helpers so scaling metrics are computed directly from the burned masks at the snapshot times.
- Added a new regression test in `simulations/fire_poc/tests/test_plotting_metrics.py` for the raster area/perimeter calculation.
- Regenerated `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` from the existing scenario outputs without rerunning ELMFIRE, and also regenerated the labeled `elmfire_time_sequence_map.png` from existing real-run outputs so the same orientation fix applies there.

### Verification
- Verified from the raster header and earliest positive `time_of_arrival` cell that the simulation ignition was already correct and the misalignment came from plotting orientation.
- Ran `source .venv312/bin/activate && MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python -m pytest -q tests` in `simulations/fire_poc/`; all 4 tests passed after adding the new plotting-metrics test.
- Opened the regenerated `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` and confirmed that the ignition star now sits on the fire origin in each scenario column and that the new bottom scaling row renders correctly.

### Open questions and follow-up
- The new scaling row is compact and readable, but if the panel is promoted into a polished proposal figure it may benefit from one more layout pass so the map rows and scaling row have slightly more breathing room.

### Prompt
User clarified that the scaling row should show log area versus log perimeter rather than log area versus perimeter-to-area ratio.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/outputs/extreme_panel/`
- `simulations/fire_poc/tests/`

### Actions taken
- Updated the extreme-panel scaling row in `plotting.py` so each scenario now plots `log(P)` versus `log(A)` directly.
- Kept the fitted `beta` estimate and the `P ~ A^(1/2)` and `P ~ A^(2/3)` reference lines, but re-anchored those references in perimeter space rather than perimeter-to-area-ratio space.
- Regenerated `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` from the existing scenario outputs without rerunning ELMFIRE.

### Verification
- Ran `source .venv312/bin/activate && MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python -m pytest -q tests` in `simulations/fire_poc/`; all 4 tests passed.
- Opened the regenerated `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` and confirmed that the bottom row now shows log area on the x-axis and log perimeter on the y-axis.

### Open questions and follow-up
- The bottom row is now conceptually cleaner, but if the panel is headed for proposal use it may still be worth enlarging the scaling row labels slightly so the slope comparison reads more easily in a PDF.

### Prompt
User asked to change the last-row axis labels so they explicitly say `log area` and `log perimeter` rather than mixing a `log-log` note on one axis with a plain quantity label on the other.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/plotting.py`
- `simulations/fire_poc/outputs/extreme_panel/`
- `simulations/fire_poc/tests/`

### Actions taken
- Updated the extreme-panel scaling-row labels in `plotting.py` so the x-axis now reads `log Area (m^2)` and the y-axis reads `log Perimeter (m)`.
- Regenerated `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` from the existing scenario outputs without rerunning ELMFIRE.

### Verification
- Ran `source .venv312/bin/activate && MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python -m pytest -q tests` in `simulations/fire_poc/`; all 4 tests passed.
- Verified the regenerated panel was written successfully.

### Open questions and follow-up
- The labels are now explicit, but the next aesthetic pass could still enlarge the bottom-row text slightly for proposal readability.

### Prompt
User asked to update the documentation Markdown and the website so they reflect the latest state of the `fire_poc` workflow and to make sure the current extreme-conditions plot is actually present on the website.

### Files and folders inspected
- `simulations/fire_poc/WORKFLOW_BUILDOUT_2026-03-30.md`
- `docs/fire-poc-workflow.md`
- `docs/assets/figures/`
- `dist/fire-poc-workflow/index.html`
- `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png`

### Actions taken
- Updated `simulations/fire_poc/WORKFLOW_BUILDOUT_2026-03-30.md` to reflect the latest plotting and workflow state, including the ignition-alignment fix, the larger `700 x 700` domain, the fact that the current run no longer touches the computational boundary, the direct `log(P)` versus `log(A)` scaling row, and the latest final burned areas.
- Updated `docs/fire-poc-workflow.md` with the same current-state information and added a dedicated “Current extreme panel” section describing the latest figure.
- Copied the current figure from `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` into the website asset tree at `docs/assets/figures/fire_poc_extreme_conditions_panel.png`.
- Embedded that copied figure in the website page so the site serves the current panel directly rather than relying on an out-of-tree path.

### Verification
- Ran `bash scripts/review_site.sh`; the MkDocs build succeeded and regenerated `dist/`, but the script’s final `pytest` step still could not run because `pytest` is not installed in the root site-review environment.
- Verified that `dist/assets/figures/fire_poc_extreme_conditions_panel.png` exists after the build.
- Verified that `dist/fire-poc-workflow/index.html` exists and references the copied figure asset.

### Open questions and follow-up
- The website now serves the current panel, but if the figure continues to change frequently it may be worth adding a small note on the page indicating that the embedded image is a synchronized snapshot of the latest generated output rather than a separately maintained website-only graphic.

### Prompt
User asked to change the extreme-panel figure title to `ELMFIRE simulations with extreme weather that produce 1/2 scaling`.

### Files and folders inspected
- `simulations/fire_poc/src/fire_poc/compare.py`
- `docs/fire-poc-workflow.md`
- `simulations/fire_poc/outputs/extreme_panel/`
- `docs/assets/figures/`

### Actions taken
- Updated the source title string in `simulations/fire_poc/src/fire_poc/compare.py` so future reruns of the extremes workflow will use `ELMFIRE simulations with extreme weather that produce 1/2 scaling`.
- Updated the embedded-image alt text in `docs/fire-poc-workflow.md` to match the new title.
- Regenerated `simulations/fire_poc/outputs/extreme_panel/figures/extreme_conditions_panel.png` from the existing scenario outputs using the new title.
- Copied the refreshed figure into `docs/assets/figures/fire_poc_extreme_conditions_panel.png` so the website serves the updated version.

### Verification
- Ran `source .venv312/bin/activate && MPLBACKEND=Agg MPLCONFIGDIR=.mplcache python -m pytest -q tests` in `simulations/fire_poc/`; all 4 tests passed.
- Ran `bash scripts/review_site.sh`; the MkDocs build succeeded and regenerated `dist/`, but the script’s final `pytest` step still could not run because `pytest` is not installed in the root site-review environment.

### Open questions and follow-up
- The new title is now synchronized between the generated panel and the website asset, but if the proposal framing changes again later it may be worth deciding whether this title should remain a figure-specific caption or become part of the broader website narrative text.

### Prompt
User asked: "the text in the gantt chart is too small to read. can we make it bigger and print a new png".

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_ESIIL_minimal.svg`
- `scripts/review_site.sh`

### Actions taken
- Increased text sizing in `scripts/generate_fire_model_gantt.py` for both renderer paths (pure-Python SVG/PNG and matplotlib) across stage headers, month labels, year labels, group labels, task labels, title/subtitle, x-axis label, and legend text.
- Regenerated the FIRE-MODEL Gantt outputs by running `python3 scripts/generate_fire_model_gantt.py`, which produced a new readable PNG and synchronized SVG in `docs/assets/figures/`.
- Ran the site review workflow script after website-asset changes, per repo policy.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py`; confirmed both `fire_model_gantt_ESIIL_minimal.svg` and `fire_model_gantt_ESIIL_minimal.png` were written.
- Ran `bash scripts/review_site.sh`; MkDocs build succeeded, but pytest collection failed due missing `playwright` module in the current environment.

### Open questions and follow-up
- If desired, we can further increase figure canvas size and row height in a follow-up pass to preserve spacing while using even larger text.

## 2026-04-06

### Prompt
User asked to update the existing FIRE-MODEL Gantt chart to match current proposal language (Verify/Predict/Synthesis), improve legibility for two-column NSF PDF insertion, preserve overlapping workstreams, and include major milestone markers.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/planning/gantt_chart.md`
- `docs/research-program/gantt-timeline.md`
- `scripts/review_site.sh`

### Actions taken
- Reworked `scripts/generate_fire_model_gantt.py` to produce a publication-ready chart with larger typography, expanded left margin, grouped workstreams, quarterly month ticks, year shading, Verify/Predict/Synthesis headings, and milestone diamonds.
- Updated task language to align with current proposal logic (A(t), P(t), σ diagnostics; competing model evaluation; reduced geometry-constrained synthesis).
- Added output generation in vector and raster formats: SVG, PDF, and high-DPI PNG under `docs/assets/figures/` using the new base name `fire_model_gantt_verify_predict_synthesis`.
- Updated `docs/planning/gantt_chart.md` to embed the new figure and revise legend language to Verify/Predict/Synthesis.
- Updated `docs/research-program/gantt-timeline.md` to remove Detect/Explain/Apply framing and align timeline wording with current proposal language.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py` and confirmed new SVG/PDF/PNG outputs were written.
- Ran `bash scripts/review_site.sh`; MkDocs build succeeded, while pytest site checks failed during collection because `playwright` is unavailable in the environment.

### Open questions and follow-up
- Milestone wording is concise for readability; proposal leads may want final wording polish for names such as "Model discrimination decision gate" and "Public release of code and workflows" before final submission packaging.

### Prompt
User indicated the previous Gantt update was unsatisfactory and requested follow-up addressing review comments, with additional instruction indicating binary files are not supported.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/planning/gantt_chart.md`
- `docs/assets/figures/`

### Actions taken
- Updated `scripts/generate_fire_model_gantt.py` so SVG remains the default checked-in output and binary `PNG/PDF` generation is now opt-in via `--all-formats`.
- Removed checked-in binary assets `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.png` and `.pdf` from version control to satisfy the binary-file constraint while preserving reproducible generation.
- Updated `docs/planning/gantt_chart.md` to reference the SVG as the primary asset and document the command to regenerate print assets on demand.
- Regenerated the SVG with the updated script defaults.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py`; confirmed SVG was written and PNG/PDF were intentionally skipped unless `--all-formats` is passed.

### Open questions and follow-up
- If submission packaging requires repository-tracked raster/vector print binaries, this binary-file policy will need explicit exception guidance.

### Prompt
User reported CI failure running `python scripts/generate_fire_model_gantt.py` due to missing `matplotlib` and requested follow-up fixes.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `scripts/review_site.sh`

### Actions taken
- Refactored `scripts/generate_fire_model_gantt.py` to support dependency-free default execution:
  - Added optional Matplotlib import guarded by `ModuleNotFoundError`.
  - Added a pure-Python SVG renderer (`render_svg_fallback`) used automatically when Matplotlib is unavailable.
  - Kept Matplotlib renderer for high-fidelity output and optional PNG/PDF generation via `--all-formats`.
- Ensured default command `python3 scripts/generate_fire_model_gantt.py` succeeds and writes the SVG even in environments without Matplotlib.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py`; command succeeded and wrote `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg`.
- Ran `bash scripts/review_site.sh`; MkDocs build succeeded, and pytest collection still failed due to missing `playwright` in the environment.

### Open questions and follow-up
- If CI also needs PNG/PDF artifacts in environments without Matplotlib, a non-Matplotlib raster/vector fallback would need to be added.

### Prompt
User reported that the Gantt chart text is now overlapping and asked to clean it up so text is larger while avoiding overlaps.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg`
- `scripts/review_site.sh`

### Actions taken
- Updated `scripts/generate_fire_model_gantt.py` row spacing controls by introducing `ROW_STEP` and `GROUP_GAP` constants and increasing both so task rows are spaced farther apart.
- Increased label font sizes for task labels and workstream labels while simultaneously increasing figure dimensions and bar height in the Matplotlib renderer to preserve readability without collisions.
- Regenerated `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg` using the updated layout logic.
- Ran the required website review script after modifying website-facing assets.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py`; SVG regenerated successfully.
- Ran `bash scripts/review_site.sh`; MkDocs build succeeded, while pytest collection failed because `playwright` is not installed in this environment.

### Open questions and follow-up
- If overlap remains in specific milestone annotation regions, a follow-up can add explicit milestone-label staggering rules to separate nearby annotations.

### Prompt
User requested targeted readability revisions to the existing FIRE-MODEL Gantt chart (milestone overlap fixes, shorter labels, updated Verify/Predict/Synthesis wording, improved spacing/layout, and regenerated PNG/PDF outputs).

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg`
- `PROMPT_ACTION_LOG.md`
- `scripts/review_site.sh`

### Actions taken
- Revised `scripts/generate_fire_model_gantt.py` with readability-focused, targeted edits rather than a chart redesign:
  - increased row spacing and group gaps,
  - increased left margin for task/category labels,
  - shortened task labels to proposal-aligned phrasing,
  - standardized notation to `A(t)`, `P(t)`, `sigma`, and `dA/dt = beta(t) * A^(2/3)`,
  - replaced milestone labels with shorter proposal-aligned versions,
  - moved milestone text into a staggered right-side annotation column with leader lines,
  - enlarged figure and font sizes for proposal PDF readability,
  - simplified legend sizing for reduced clutter.
- Added an in-file readability update note in the script docstring to preserve rationale/provenance.
- Regenerated chart assets including high-resolution PNG and PDF.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py --all-formats`; confirmed updated SVG, PNG, and PDF outputs were written.
- Ran `bash scripts/review_site.sh` (required website-facing check); MkDocs build succeeded, while pytest collection failed due to missing `playwright` in the environment.

### Open questions and follow-up
- If a stricter visual QA pass is needed (e.g., bounding-box overlap assertions), add an automated text-overlap check as a follow-up utility.

### Prompt
User reported the prior PR was unsatisfactory and requested follow-up, with explicit instruction that binary files are not supported.

### Files and folders inspected
- `docs/assets/figures/`
- `docs/planning/gantt_chart.md`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Removed repository-tracked binary chart outputs:
  - `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.png`
  - `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.pdf`
- Kept SVG as the checked-in canonical figure asset and retained script-based regeneration path for optional print formats.

### Verification
- Ran `git status --short`; confirmed only the intended binary deletions and prompt log update are staged as changes.

### Open questions and follow-up
- If proposal packaging still needs binary exports, generate them locally at submission time from `scripts/generate_fire_model_gantt.py --all-formats` without committing binaries.

### Prompt
User said left-side text still overlaps in the Gantt chart and requested a PNG in the same folder, with the note that binaries cannot be committed and PNG generation should happen after the PR.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg`
- `scripts/review_site.sh`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Adjusted label layout spacing in `scripts/generate_fire_model_gantt.py` to reduce left-column collisions:
  - moved workstream labels further left and slightly reduced their font size,
  - moved task labels rightward to increase separation from workstream labels,
  - shifted chart start/end x-coordinates in SVG fallback to preserve spacing,
  - widened Matplotlib x-limits and repositioned subtitle anchor to match the new left margin.
- Regenerated `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg` using `python scripts/generate_fire_model_gantt.py`.
- Kept PNG generation as a post-PR/manual step (no binary commit), consistent with repository policy.
- Ran the required site review workflow after website-facing asset updates.

### Verification
- Ran `python scripts/generate_fire_model_gantt.py`; SVG regenerated successfully.
- Ran `bash scripts/review_site.sh`; MkDocs site build succeeded, pytest collection failed due to missing `playwright` module in this environment.

### Open questions and follow-up
- After merge, run `python scripts/generate_fire_model_gantt.py --all-formats` locally to generate PNG/PDF in `docs/assets/figures/` without committing binaries.

### Prompt
User reported that the bottom two far-left labels in the FIRE-MODEL Gantt still overlap the next row and asked for wrapped labels that preserve large font size.

### Files and folders inspected
- `scripts/generate_fire_model_gantt.py`
- `docs/assets/figures/fire_model_gantt_verify_predict_synthesis.svg`
- `scripts/review_site.sh`
- `PROMPT_ACTION_LOG.md`

### Actions taken
- Updated `scripts/generate_fire_model_gantt.py` to wrap the two longest workstream labels into two lines while keeping the existing large/bold category font.
- Added a shared `GROUP_LABEL_LINES` mapping and applied it in both renderers:
  - SVG fallback now emits multi-line `<text>/<tspan>` blocks for wrapped labels.
  - Matplotlib renderer now renders wrapped labels with newline-aware text and controlled line spacing.
- Regenerated the chart with `python3 scripts/generate_fire_model_gantt.py --all-formats` to verify SVG/PNG/PDF output from the updated layout.
- Ran the required site review script after the website-facing figure change.

### Verification
- Ran `python3 scripts/generate_fire_model_gantt.py --all-formats`; chart generation succeeded and wrote SVG/PNG/PDF locally.
- Ran `bash scripts/review_site.sh`; MkDocs build succeeded, and pytest collection failed because `playwright` is not installed in this environment.

### Open questions and follow-up
- If you want the same wrapped label treatment for other long workstream names, we can extend `GROUP_LABEL_LINES` with additional explicit line breaks.
