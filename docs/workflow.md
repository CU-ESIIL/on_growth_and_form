# Proposal Workflow

## Working sequence

1. Add NSF solicitation and sponsor guidance to `funder/`, starting from the current FIRE-MODEL briefing and replacing summaries with official source files whenever possible.
2. Draft the narrative and compliance documents in `proposal/`.
3. Save literature PDFs locally in `citations/pdfs/` and capture reusable notes in `citations/notes/`.
4. Run exploratory or supporting analyses from `simulations/scripts/`.
5. Build proposal graphics from `figures/source/` and export candidate images as needed.

## Folder expectations

### `funder/`

- `solicitation/`: calls, program descriptions, FAQs.
- `templates/`: sponsor-provided templates and formatting examples.
- `review_criteria/`: merit review guidance and checklist material.

### `background_context/`

- `program_briefings/`: context notes tied to the program itself.
- `intellectual_foundations/`: broader conceptual framing.
- `scaling_and_geometry/`: wildfire scaling, transport, and perimeter-geometry notes.
- `systems_frameworks/`: analytical and data-system frameworks.
- `research_programs/`: proposal-shaping research agendas and work-plan narratives.
- Keep this separate from `funder/` so funder-facing guidance and scientific framing do not get mixed together.

### `proposal/`

- `narrative/`: project summary, project description, and section drafts.
- `narrative/drafts/`: numbered draft snapshots and draft-to-draft change reports for proposal-memory tracking.
- `budget/`: budget justifications and internal calculation notes.
- `biosketches/`: team biosketch drafts.
- `current_and_pending/`: current and pending support material.
- `data_management_plan/`: NSF data management planning text.
- `postdoctoral_mentoring_plan/`: mentoring plan text when relevant.
- `supplementary/`: other required supplementary documents.

### `citations/`

- `notes/`: tracked reading notes, synthesis tables, and citation metadata.
- `exports/`: sharable bibliographies or clean exports.
- `pdfs/`: ignored local article library.

### `simulations/`

- `scripts/`: model code and runner scripts.
- `config/`: parameter files and scenario definitions.
- `results/`: ignored generated outputs.
- `logs/`: ignored run logs.

### `figures/`

- `source/`: tracked notebooks, scripts, vector art, and layered files.
- `drafts/`: ignored working exports.
- `final/`: ignored submission-ready exports unless you decide later to version them.

## Git policy

Keep text, scripts, parameter files, and notes in version control. Avoid committing article PDFs or bulky generated outputs unless there is a specific archival reason.

## FIRE-MODEL-specific reminder

- Treat `funder/solicitation/fire_model_2026_briefing.md` as a funder guide and orientation aid, not a substitute for the official NSF call.
- Treat `background_context/` as the place for contextualization and positioning notes that help shape the proposal argument.
- Check submission dates, track definitions, page and formatting rules, and required documents against the authoritative NSF materials before final drafting.
