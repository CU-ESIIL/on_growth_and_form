# Data and Infrastructure

This section explains how the project moves from raw Earth observation products to structured wildfire events and scalable analytical workflows.

## Why this section matters

The wildfire scaling problem is not only theoretical. It depends on having the right infrastructure for reconstructing fire trajectories, aligning them with environmental drivers, and analyzing them consistently across many events and ecosystems.

Two systems are especially important here:

- `FIRED`, which turns burned-area pixels into fire events with progression histories
- `CubeDynamics`, which provides the spatiotemporal cube framework for large-scale analysis

## What this section covers

- [FIRED](fired.md)
- [CubeDynamics](cubedynamics.md)
- [FIRED and CubeDynamics](fired-cubedynamics.md)
- [Environmental Data Science Stack](environmental-data-science-stack.md)
- [Satellite Fire Datasets](satellite-fire-datasets.md)
