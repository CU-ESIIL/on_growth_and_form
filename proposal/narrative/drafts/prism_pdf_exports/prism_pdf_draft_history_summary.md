# Prism PDF Draft History Summary

This document records the Prism-exported PDF drafts currently stored in this folder so future agents can see how the proposal evolved across these snapshot exports.

## Purpose

- Preserve a transparent record that Prism was used in this drafting workflow.
- Summarize what is visibly present in each exported PDF.
- Distinguish observable draft-to-draft changes from assumptions that cannot be verified from the PDF alone.

## Scope and limits

- These notes are based on the exported PDF artifacts in this folder, not on hidden Prism chat history or prompt logs.
- The PDFs do not expose a reliable prompt-by-prompt provenance trail, so this document should be read as a content-visible audit record rather than a complete reconstruction of AI interaction.
- Because the filenames are generic (`main.pdf`, `main-2.pdf`, `main 3.pdf`, `main4.pdf`), chronology below is inferred from filesystem modification time on March 21, 2026.

## Observable chronology

### 1. `main.pdf`

- File: `proposal/narrative/drafts/prism_pdf_exports/main.pdf`
- Observed modification time: `2026-03-21 16:57:41`
- Observed length: `15 pages`, approximately `5,372 extracted words`
- Apparent role in sequence: earliest Prism export currently present in the folder

Summary:
This export appears to be the first full-length NSF-aligned narrative snapshot in the current Prism sequence. It frames the project around transition-aware, multi-regime wildfire modeling, positions the proposal as a discovery program with explicit decision points, and lays out a near-full project structure with targeted section word counts. The project summary already includes the core regime-transition hypothesis, use of `FIRED` and `CubeDynamics`, benchmark development, and uncertainty-reporting goals.

Visible drafting state:
The prose is already strongly structured around NSF sections and appears to function as a substantial proposal skeleton rather than a fragmentary brainstorm. It emphasizes falsifiability, benchmark infrastructure, and mechanism discrimination, but reads as a more compact version of the later exports. The end matter includes a word-count allocation summary for the major narrative sections.

AI-use transparency note:
Because this file is a Prism export, it should be treated as an AI-mediated drafting artifact in the proposal history. The PDF itself does not identify which sentences came directly from Prism versus subsequent user editing within Prism before export.

### 2. `main-2.pdf`

- File: `proposal/narrative/drafts/prism_pdf_exports/main-2.pdf`
- Observed modification time: `2026-03-21 17:13:35`
- Observed length: `16 pages`, approximately `6,061 extracted words`
- Apparent role in sequence: second visible Prism export

Summary:
This export preserves the same overall proposal architecture as `main.pdf` but expands several sections. It keeps the regime-transition framing, the `FIRED` and `CubeDynamics` infrastructure linkage, and the explicit NSF-oriented project summary structure. Relative to the earlier file, it appears to add more theory-forward and generative-model framing, more explicit decision logic, and additional language around model comparison and transition testing.

Visible changes relative to `main.pdf`:
- The draft grows modestly in length and density rather than changing direction.
- Added text more clearly describes the project as theory-first generative modeling rather than simulation-first tuning.
- The verification and comparison framing becomes more explicit, including stronger language about information criteria, cross-validation, and transition-alignment analysis.
- The overall effect is a more methodologically explicit and auditable narrative while preserving the same core proposal thesis.

AI-use transparency note:
This export documents a visible AI-assisted revision step in Prism, but the PDF alone does not preserve the underlying prompt history or identify whether the expansion came from a fresh generation, iterative editing, pasted repository content, or a mixture of those sources.

### 3. `main 3.pdf`

- File: `proposal/narrative/drafts/prism_pdf_exports/main 3.pdf`
- Observed modification time: `2026-03-21 17:32:16`
- Observed length: `22 pages`, approximately `9,094 extracted words`
- Apparent role in sequence: major expansion draft

Summary:
This export marks a substantial shift from compact full-length draft to a much more developed narrative. The opening overview is rewritten into a stronger argumentative form: wildfire models fail most where predictions matter most; large fires reorganize rather than simply extend local spread; and regime transitions are positioned as the central scientific problem. The draft also appears to deepen the explanation of intellectual merit and strengthen the distinction between mechanism discrimination and simple predictive tuning.

Visible changes relative to `main-2.pdf`:
- The draft expands sharply in page count and extracted word count.
- The project overview is substantially rewritten, moving from a broad hazard-and-extremes opening to a sharper critique of single-process wildfire modeling.
- The narrative increasingly presents geometry and regime transition as explanatory constraints, not just descriptive features.
- The text adds stronger language about transparent failure criteria, structural diagnostics, and inference rather than calibration alone.
- Broader impacts and project description sections appear more fully developed than in the prior exports.

AI-use transparency note:
This file is especially useful as a transparency marker because it captures a clear content-level revision step rather than a cosmetic re-export. Even so, the PDF cannot tell us how much of this expansion was generated in one Prism exchange versus accumulated across multiple iterative edits inside the tool.

### 4. `main4.pdf`

- File: `proposal/narrative/drafts/prism_pdf_exports/main4.pdf`
- Observed modification time: `2026-03-21 17:47:53`
- Observed length: `24 pages`, approximately `9,922 extracted words`
- Apparent role in sequence: latest and most elaborated Prism export currently present

Summary:
This export appears to be the most developed version in the current set. It continues the stronger argumentative opening introduced in `main 3.pdf` and pushes it further: the draft now emphasizes that reorganization is visibly expressed in changing fire boundaries and that geometry functions as a governing constraint once coherent fronts emerge. The proposal’s framing becomes more assertive and conceptually unified, particularly around the claim that a single-process treatment of wildfire growth is not merely simplified but mis-specified.

Visible changes relative to `main 3.pdf`:
- The overview section is expanded again with clearer phenomenological description of fire reorganization.
- The geometry argument is sharpened from “geometry becomes a dominant constraint” to a stronger explanation of boundary structure governing growth.
- The proposal increasingly frames the scientific contribution as replacing a wrong organizing assumption, not just improving an incomplete one.
- The file length increase suggests additional elaboration across the narrative rather than a narrow local edit.

AI-use transparency note:
This export should be treated as the latest visible AI-assisted draft artifact in this folder. It provides strong evidence of iterative Prism-mediated refinement, but not a complete provenance ledger of what the user asked Prism at each step.

## High-level progression across the Prism exports

Across the four files, the visible progression is:

1. A full-length NSF-oriented proposal skeleton with section targets and the core regime-transition idea already present.
2. A denser revision that clarifies theory-first generative modeling and strengthens methodological decision logic.
3. A major expansion that rewrites the opening around wildfire reorganization, mechanism discrimination, and explicit critique of single-process assumptions.
4. A final visible elaboration that sharpens the geometry-as-constraint argument and makes the conceptual framing more forceful.

## Recommended use in this repository

- Treat these PDFs as proposal-history artifacts, not canonical source text.
- When later agents rely on ideas that appear in these exports, they should cite this summary document and the corresponding PDF artifact rather than implying that the wording originated directly in the Markdown proposal files.
- If a more complete AI-use audit trail is desired later, the missing piece is a separate human-authored note that records what was asked of Prism at each step, because that information is not recoverable from the PDFs alone.
