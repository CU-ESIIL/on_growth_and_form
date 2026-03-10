<section class="ogf-hero" markdown>

<span class="ogf-kicker">NSF Proposal Workspace</span>

# On Growth and Form

This site tracks the working structure for an NSF proposal focused on fire, growth, and form. The repository is set up to keep sponsor materials, proposal text, literature, simulations, and figures in distinct places so drafting and analysis stay reproducible.

[View Workflow](workflow.md){ .md-button .md-button--primary .oasis-hover-button }
[Open Repository](https://github.com/CU-ESIIL/on_growth_and_form){ .md-button .ogf-button-secondary .oasis-hover-button }

</section>

<div class="grid cards" markdown>

- **Funder Materials**

  ---

  Keep solicitations, templates, and review guidance in `funder/`.

- **Literature**

  ---

  Store citation notes in Git and keep article PDFs local under `citations/pdfs/`.

- **Analysis**

  ---

  Separate simulation code, configs, and outputs so figures can be regenerated cleanly.

</div>

!!! note "Proposal-first organization"
    The repository favors tracked source material and reproducible scripts, while heavy PDFs and generated outputs stay out of Git by default.
