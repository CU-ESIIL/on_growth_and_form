# Draft Change Report: `main5.pdf` to `Project Description-8.pdf`

## Purpose

This memo records the newest Prism-exported draft transition and logs what can be confirmed from the repository artifacts.

## Source files compared

- Previous draft artifact: `proposal/narrative/drafts/prism_pdf_exports/main5.pdf`
- New draft artifact: `proposal/narrative/drafts/prism_pdf_exports/Project Description-8.pdf`

## Confirmed observable changes

1. **A new latest draft artifact was added**
   - `Project Description-8.pdf` is now present and has the newest modification time in this directory (`2026-04-03 14:56:06 UTC`).
2. **The export packaging changed substantially**
   - `main5.pdf`: `599,958` bytes
   - `Project Description-8.pdf`: `4,952,633` bytes
   - The new file is ~8.25x larger, indicating a materially different export package (likely heavier embedded assets and/or different PDF production settings).
3. **PDF internals differ from earlier Prism exports**
   - Earlier Prism snapshots in this folder are object-stream heavy and difficult to text-audit with lightweight extraction.
   - `Project Description-8.pdf` includes directly visible page objects in its PDF structure and appears to be a different export profile than the `main*.pdf` sequence.
4. **Latest-draft status in repository history has shifted**
   - The canonical "most recent Prism PDF export" marker should now point to `Project Description-8.pdf`, not `main5.pdf`.

## Content-level comparison status

A complete line-by-line textual diff between `main5.pdf` and `Project Description-8.pdf` could not be produced in this local environment because robust PDF text extraction/OCR tooling is not available and lightweight extraction produced unreliable text for the newest export.

To avoid inventing changes, this memo therefore records only **artifact-verifiable** changes and marks full prose-diff work as pending.

## Recommended follow-up (for full prose-level change accounting)

When a full PDF text extraction workflow is available (or when the draft is exported to Markdown/Word), run a section-by-section comparison and extend this memo with:

- added sections/subsections,
- removed sections/subsections,
- changed framing of intellectual merit and broader impacts,
- changed claims/mechanisms/hypotheses,
- changed validation and deliverables language,
- changed solicitation-alignment statements.

## Assumptions and cautions

- This report is intentionally conservative and only includes changes that are directly verifiable from local repository artifacts.
- No unsupported content claims are made about prose changes inside the new PDF.
