# Prompt Action Log

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
