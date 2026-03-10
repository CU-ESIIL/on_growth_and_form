# On Growth and Form: NSF Proposal Workspace

This repository is organized as a working space for an NSF FIRE-MODEL proposal on fire, growth, and form. It combines proposal writing, funder guidance, literature management, simulations, figures, and a lightweight project website.

## Repository layout

- `funder/`: solicitation PDFs, templates, review criteria, and other sponsor-provided material.
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

These are working summaries built from collected program information and should be checked against the official NSF solicitation, updates page, and webinar materials before final submission drafting.

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
