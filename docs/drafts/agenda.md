# Draft Review Agenda

Use this agenda whenever a new major proposal draft is added.

## Required comparison workflow

1. Identify the immediately previous draft and the new draft.
2. Write a draft-comparison memo that records:
   - what the new draft adds or strengthens,
   - what it compresses or removes,
   - what scientifically or strategically important material may have been left behind,
   - what should be restored, merged, or explicitly rejected in the next iteration.
3. Update the drafts website section so the newest comparison is visible without opening repository source files.
4. Add a visible note on the drafts website whenever the comparison identifies important left-behind material.
5. Record the prompt, files inspected, actions taken, verification, and any open questions in `PROMPT_ACTION_LOG.md`.

## Left-behind flag policy

When the comparison report finds material that should not be lost, future agents should surface it as a website note in the drafts section rather than leaving the warning buried only in repository prose.

Recommended note structure:

- short label describing the risk,
- 1–3 sentence explanation of what was dropped,
- whether the material should be restored, merged later, or intentionally retired.

## What counts as important material

Future agents should flag items such as:

- proposal elements tied directly to `FIRE-MODEL` call alignment,
- feasibility or reviewer-confidence scaffolding,
- benchmark logic, validation logic, or deliverables,
- citation-supported scientific claims that disappear in a later draft,
- assumptions that become implicit and therefore easy to forget.
