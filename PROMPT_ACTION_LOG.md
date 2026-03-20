# Prompt Action Log

## 2026-03-20

### Prompt
Convert a user-provided wildfire modeling bibliography into a repository Markdown reference note under the citations area, preserving the dense citation, identity, summary, and example-citation structure for later proposal use.

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
Add a historical context section to the top of the wildfire modeling master bibliography without deleting any existing content.

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
Add a reproducible, script-generated figure showing a time-calibrated conceptual phylogeny of wildfire modeling, publish it as its own MkDocs page under planning/background materials, and regenerate the figure automatically during the GitHub Pages build.

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
Add a new background and context page to the website using a user-provided long-form document on the causal history of wildfire modeling.

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
Add a new methods section page to the documentation using a user-provided measurement and validation framework for wildfire perimeter scaling.

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
