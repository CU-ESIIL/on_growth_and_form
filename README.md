# On Growth and Form: NSF Proposal Workspace

This repository is organized as a working space for an NSF FIRE-MODEL proposal on fire, growth, and form. It combines proposal writing, funder guidance, literature management, simulations, figures, and a lightweight project website.

## Repository layout

- `funder/`: official materials, requirement summaries, and funder-facing research guides for the FIRE call.
- `background_context/`: scientific framing, contextualization, and synthesis that support proposal argumentation.
  - `program_briefings/`: program-specific context notes
  - `intellectual_foundations/`: broader conceptual grounding
  - `scaling_and_geometry/`: scaling, fractal, diffusion, and wildfire-geometry notes
  - `systems_frameworks/`: event-based and data-system architecture notes
  - `research_programs/`: proposal-shaping research agendas and narrative work plans
- `proposal/`: proposal narrative and supporting components such as budget text, biosketches, and plans.
- `citations/`: tracked citation notes and exports, plus a local `pdfs/` folder for article PDFs that is ignored by Git.
- `simulations/`: scripts, configs, and generated model outputs for analysis supporting the proposal.
- `figures/`: source assets plus draft and final figure outputs.
- `docs/`: MkDocs website content documenting the proposal workflow and project status.

## Recommended workflow

1. Put sponsor documents in `funder/`.
2. Store paper PDFs in `citations/pdfs/` and keep structured notes in `citations/notes/`.
3. Run exploratory models from `simulations/scripts/` with reusable parameter files in `simulations/config/`.
4. Build visuals from `figures/source/` and publish candidate outputs to `figures/drafts/` or `figures/final/`.
5. Keep the website in `docs/` synchronized with proposal milestones and repository structure.

## Current solicitation anchor

The repository is currently oriented around the 2026 NSF FIRE-MODEL cycle described in:

- `funder/solicitation/fire_model_2026_briefing.md`
- `funder/review_criteria/fire_model_requirements_checklist.md`
- `background_context/program_briefings/fire_model_2026_background.md`
- `background_context/intellectual_foundations/on_growth_and_form_intellectual_overview.md`
- `background_context/scaling_and_geometry/diffusion_across_space_half_scaling_signature.md`
- `background_context/scaling_and_geometry/non_half_scaling_signatures_spatial_spread.md`
- `background_context/scaling_and_geometry/scaling_dimensionality_power_laws_wildfire_science.md`
- `background_context/scaling_and_geometry/superdiffusive_scaling_fractal_geometry_wildfire_perimeter_growth.md`
- `background_context/scaling_and_geometry/fire_modeling_frameworks_scaling_perspectives.md`
- `background_context/scaling_and_geometry/wildfire_scaling_regime_hypothesis.md`
- `background_context/scaling_and_geometry/wildfire_scaling_open_questions_hypotheses_empirical_tests.md`
- `background_context/systems_frameworks/environmental_data_science_stack_2030.md`
- `background_context/systems_frameworks/fired_cubedynamics_event_based_earth_system_analysis.md`
- `background_context/research_programs/wildfire_scaling_research_program_work_plan.md`
- `background_context/research_programs/wildfire_scaling_rationale_deliverables_users_impact.md`

The `funder/` files are the working home for funder-oriented material and requirement tracking. The `background_context/` files are interpretive notes used to frame the proposal scientifically.

## Website

The site is built from `docs/` and can be served locally with MkDocs.

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Website checks

The repository includes Playwright-based smoke tests for the built MkDocs site. These tests are intended to catch broken pages, failed asset loads, browser-side errors, and obvious navigation regressions before a pull request fails.

```bash
pip install -r requirements-dev.txt
python -m playwright install chromium
bash scripts/review_site.sh
```

The GitHub workflow runs these checks automatically when website-related files change. The deploy workflow also runs the same validation before publishing to GitHub Pages.

## Git behavior

- `citations/pdfs/` is ignored so article libraries do not get committed.
- Generated outputs in `simulations/results/`, `simulations/logs/`, `figures/drafts/`, and `figures/final/` are ignored by default.
- Keep durable source material, notes, configs, and scripts tracked in Git.
