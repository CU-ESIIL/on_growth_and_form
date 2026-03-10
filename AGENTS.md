# AGENTS.md

## Mission
- Treat this repository as a working environment for an NSF proposal on fire, growth, and form.
- Optimize for proposal quality, traceability, and compliance rather than generic software output.
- Treat the solicitation, program description, and any NSF-issued guidance in `funder/` as the controlling documents for writing decisions.
- Write directly to the call for proposals. If repository content conflicts with the solicitation, the solicitation wins.

## Primary Priorities
- Keep all work aligned with NSF review criteria, required sections, page limits, formatting constraints, and submission instructions.
- Make small, auditable edits that preserve proposal history and reasoning.
- Keep proposal text, supporting analyses, figures, and website documentation synchronized.
- Surface uncertainty explicitly. Do not fill gaps with invented facts, invented requirements, or invented citations.

## Expected Agent Behavior
- Read the relevant funder materials before drafting or revising proposal content.
- Identify which solicitation requirement a draft section is trying to satisfy.
- Prefer improving the proposal against NSF criteria over making stylistic changes with no review value.
- Preserve the distinction between source material, analysis artifacts, and polished proposal prose.
- When asked to write, revise, or review, state assumptions clearly in the repository artifacts you update.
- Flag missing required documents, unresolved compliance issues, and unsupported claims.

## Required Workflow
- Inspect repository structure and relevant proposal files before editing.
- Check `funder/` first when the task involves proposal language, section requirements, formatting, or submission strategy.
- Update related docs when structure, workflow, or outputs change.
- Record each meaningful user prompt and resulting agent action in `PROMPT_ACTION_LOG.md`.
- Run `bash scripts/review_site.sh` after website-facing changes to `docs/`, `mkdocs.yml`, website assets, or site workflows whenever the local environment supports it.
- Preserve historical context; avoid destructive rewrites unless explicitly requested.

## Prompt and Action Logging
- `PROMPT_ACTION_LOG.md` is required project memory for agent activity.
- For each meaningful task, add a new dated entry with:
  - the user prompt or a concise paraphrase,
  - the files or folders inspected,
  - the actions taken,
  - any verification performed,
  - open questions, assumptions, or follow-up needs.
- Keep entries brief, factual, and chronological.
- If no file changes were made, log the analysis outcome when it materially affects proposal direction.

## Citation Policy
- Never invent citations, author lists, publication years, titles, journal names, volume numbers, page ranges, DOIs, URLs, or bibliographic endings.
- Verify citation details against the original paper, publisher page, Crossref record, or another primary bibliographic source whenever possible.
- Prefer obtaining and storing the original PDF in `citations/pdfs/` whenever possible and permitted.
- If only secondary citation data is available, say so explicitly in notes or draft text.
- Keep literature synthesis and claim support in tracked files under `citations/notes/` or other appropriate repository locations.
- Do not cite a paper in proposal prose unless the citation has been checked or is clearly marked as needing verification.

## Proposal Writing Policy
- Write to NSF’s required and implicit questions: why this work matters, why now, why this team, why this approach, and what broader impacts and intellectual merit it delivers.
- Anchor section structure to the solicitation and NSF templates rather than generic grant-writing conventions.
- Respect NSF formatting requirements when drafting text intended for submission.
- Keep claims specific, evidence-based, and proportionate to the available support.
- When using simulation results or figures to support an argument, make the provenance of those outputs clear.

## Funder Documents Policy
- Store sponsor-provided PDFs, templates, review criteria, and guidance in `funder/`.
- Do not paraphrase a requirement when quoting or closely interpreting the solicitation would be safer.
- When summarizing funder requirements, preserve the original meaning and point back to the relevant source document.
- If a requirement is ambiguous, note the ambiguity and avoid overcommitting the proposal to an unverified interpretation.

## Simulations and Figures Policy
- Keep reusable code in `simulations/scripts/` and reusable parameters in `simulations/config/`.
- Treat `simulations/results/`, `simulations/logs/`, `figures/drafts/`, and `figures/final/` as generated output areas.
- Document enough context that a future contributor can understand what a simulation or figure was intended to support in the proposal.
- Do not let exploratory outputs silently become proposal evidence without clear provenance and review.

## Documentation and Website Policy
- Treat `docs/` as the proposal website and process documentation.
- Update the site when repository structure, workflow, or proposal framing materially changes.
- Keep the website accurate, concise, and aligned with the actual state of the proposal workspace.

## Review Policy
- For reviews, prioritize compliance risks, unsupported claims, missing evidence, citation problems, and mismatches with NSF requirements.
- Call out where text appears to answer the wrong question or misses the solicitation’s framing.
- Distinguish clearly between confirmed issues and hypotheses that still require checking against funder documents.

## Data, Rights, and Research Integrity
- Document data provenance, access constraints, licensing, and citation requirements for any dataset introduced into the proposal workflow.
- Respect copyright, licensing, privacy, and Indigenous data sovereignty constraints.
- Do not silently ingest external content into the repo.

## Decision Logging
- Record meaningful structural, strategic, citation, and compliance decisions in repository documentation.
- When in doubt, prefer leaving a short traceable note over relying on memory.
