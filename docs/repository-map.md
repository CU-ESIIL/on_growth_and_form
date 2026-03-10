# Repository Map

The current repository structure is organized around proposal development and supporting analysis.

```text
on_growth_and_form/
├── citations/
│   ├── exports/
│   ├── notes/
│   └── pdfs/               # gitignored local library
├── docs/
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
│   ├── postdoctoral_mentoring_plan/
│   └── supplementary/
└── simulations/
    ├── config/
    ├── logs/               # gitignored run logs
    ├── results/            # gitignored outputs
    └── scripts/
```

## Notes

- The website under `docs/` documents the proposal process rather than serving as a generic project template.
- Ignored folders are still useful locally; they are intentionally present so the working layout is clear from the start.
- If some generated figures or outputs need to be preserved in Git later, the ignore rules can be narrowed to specific file types or subfolders.
