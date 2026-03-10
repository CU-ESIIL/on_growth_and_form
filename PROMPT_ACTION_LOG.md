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
