# Wildfire Modeling Phylogeny

This figure exists to situate the proposal in the longer history of wildfire modeling and to make that history legible at a glance. Rather than treating the field as a single line of incremental improvement, it shows how major modeling ideas emerged from specific scientific and operational needs over time.

Wildfire modeling diversified into multiple lineages optimized for different use cases, including operational spread modeling, coupled physics, landscape ecology, complexity and scaling, and machine learning. The result is a field that branched into partially connected families of methods, each of which represents a different compromise among realism, computational tractability, time horizon, and intended decision context.

![Conceptual time-calibrated phylogeny of wildfire modeling](../assets/figures/wildfire_phylogeny_publication.png){ .wildfire-phylogeny-figure }

## Figure Legend

The central trunk represents the broad historical transitions that reorganized how wildfire was modeled, from early observation and fire-danger systems through computable local spread, spatial perimeter growth, probabilistic risk modeling, and the data-rich machine-learning era. Side branches represent conceptual descent or use-case divergence, meaning later models inherit an intellectual problem framing or application domain even when they are not direct software descendants of one another. Tip labels identify representative named models or landmark papers that sit at the visible ends of those lineages in this diagram. Time calibration means the horizontal position of each trunk node and branch tip corresponds to a calendar year, so the figure can be read simultaneously as a history of ideas and a map of branching modeling families.

This is a conceptual time-calibrated phylogeny of modeling ideas and use-case divergence, not a strict software dependency tree. It should be read as a historical synthesis of how the field branched into different modeling problem classes rather than as a claim that all descendants inherit code or exact implementation details from earlier systems.

This matters for the proposal because wildfire modeling did not evolve by converging on a single unified framework. Instead, it expanded by branching into different problem classes, each tuned to a distinct scientific or operational question, which is exactly the context needed for motivating a new integrative research program on growth, form, and wildfire dynamics.
