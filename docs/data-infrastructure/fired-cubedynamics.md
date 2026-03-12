# FIRED and CubeDynamics

This page describes the combined system rather than the parts in isolation.

## Why the combination matters

`FIRED` and `CubeDynamics` solve different parts of the same analytical problem.

- `FIRED` reconstructs the event.
- `CubeDynamics` provides the analytical frame around the event.

Together they make it possible to move from burned pixels to research questions about trajectory, geometry, and scaling.

## Combined workflow

```text
satellite observations
  -> event reconstruction with FIRED
  -> fire trajectories and daily perimeters
  -> environmental alignment in CubeDynamics
  -> geometric and scaling diagnostics
  -> model comparison and scientific interpretation
```

## Why this is central to the project

Without this combination, the project would either have:

- events without a scalable analytical system, or
- a scalable analytical system without coherent fire events

The proposal depends on having both.

## In-repo source file

- `background_context/systems_frameworks/fired_cubedynamics_event_based_earth_system_analysis.md`
