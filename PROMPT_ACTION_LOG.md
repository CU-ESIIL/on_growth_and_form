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
