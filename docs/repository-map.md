# Repository Map

The current repository structure is organized around proposal development and supporting analysis.

```text
on_growth_and_form/
├── background_context/
│   ├── intellectual_foundations/
│   ├── program_briefings/
│   ├── research_programs/
│   ├── scaling_and_geometry/
│   └── systems_frameworks/
├── citations/
│   ├── exports/
│   ├── notes/
│   └── pdfs/               # gitignored local library
├── docs/
│   ├── archive/
│   ├── data-infrastructure/
│   ├── literature/
│   ├── methods/
│   ├── models/
│   ├── planning/
│   ├── project-overview/
│   ├── research-program/
│   ├── start-here/
│   ├── theory/
│   ├── assets/
│   ├── drafts/
│   └── stylesheets/
├── figures/
│   ├── drafts/             # gitignored generated figures
│   ├── final/              # gitignored generated figures
│   └── source/
├── funder/
│   ├── review_criteria/
│   ├── solicitation/
│   └── templates/
├── proposal/
│   ├── biosketches/
│   ├── budget/
│   ├── current_and_pending/
│   ├── data_management_plan/
│   ├── narrative/
│   │   └── drafts/
│   ├── postdoctoral_mentoring_plan/
│   └── supplementary/
└── simulations/
    ├── config/
    ├── logs/               # gitignored run logs
    ├── results/            # gitignored outputs
    └── scripts/
```

## Notes

- The website under `docs/` is now organized around landing pages that route readers to the full long-form materials rather than replacing them with short summaries.
- `docs/start-here/` provides entry points for repository navigation and workflow guidance.
- `docs/project-overview/` carries proposal-facing context and funder alignment material.
- `docs/research-program/` functions as the work-plan section of the site.
- `docs/archive/` routes readers to retained draft and exploratory materials.
- `funder/` is for the call, requirement tracking, and funder-oriented guides.
- `background_context/` is grouped into program context, intellectual foundations, scaling/geometry, systems frameworks, and research-program notes.
- `proposal/narrative/` holds active proposal strategy and integration documents, while `proposal/narrative/drafts/` preserves numbered draft snapshots and comparison memos.
- `proposal/narrative/drafts/` preserves proposal-memory snapshots and comparison reports, while `docs/drafts/` publishes a lightweight review surface for those artifacts.
- Ignored folders are still useful locally; they are intentionally present so the working layout is clear from the start.
- If some generated figures or outputs need to be preserved in Git later, the ignore rules can be narrowed to specific file types or subfolders.
