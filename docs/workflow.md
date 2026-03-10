# Proposal Workflow

## Working sequence

1. Add NSF solicitation and sponsor guidance to `funder/`.
2. Draft the narrative and compliance documents in `proposal/`.
3. Save literature PDFs locally in `citations/pdfs/` and capture reusable notes in `citations/notes/`.
4. Run exploratory or supporting analyses from `simulations/scripts/`.
5. Build proposal graphics from `figures/source/` and export candidate images as needed.

## Folder expectations

### `funder/`

- `solicitation/`: calls, program descriptions, FAQs.
- `templates/`: sponsor-provided templates and formatting examples.
- `review_criteria/`: merit review guidance and checklist material.

### `proposal/`

- `narrative/`: project summary, project description, and section drafts.
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
