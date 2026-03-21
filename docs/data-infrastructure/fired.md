# FIRED

## Overview

Satellite burned-area products provide global records of fire activity, but these datasets typically represent fire as individual burned pixels detected on specific days. While this is useful for monitoring, it does not directly reveal how individual fires grow, merge, or evolve through time.

The purpose of `FIRED` is to convert these raw burned-area pixels into individual fire events with spatial and temporal structure.

In other words, `FIRED` answers the question:

Which burned pixels belong to the same fire?

## The core problem

Raw satellite fire products such as MODIS `MCD64A1` represent fire activity as a time series of burned pixels.

For example:

- Day 1: several burned pixels appear
- Day 2: additional burned pixels appear nearby
- Day 3: the burn scar expands

Without additional analysis, it is unclear whether these pixels represent:

- one growing fire
- multiple nearby fires
- overlapping burn scars

`FIRED` reconstructs these observations into coherent fire events.

## How the FIRED algorithm works

`FIRED` uses a spatiotemporal clustering algorithm.

The process typically follows these steps:

1. Ingest burned-area data from satellite products such as MODIS burned-area grids.
2. Identify burned pixels for each day using burn dates.
3. Cluster pixels in space and time using adjacency and a defined temporal window.
4. Construct fire events by aggregating clusters into single event histories.

The output is a dataset where each fire includes:

- spatial footprint
- start date
- duration
- daily progression polygons

## Output structure of FIRED

The resulting dataset transforms pixel observations into event-level information.

Each fire event includes:

- unique fire identifier
- event start and end dates
- daily burn progression
- final fire perimeter
- total burned area

This structure enables researchers to reconstruct the evolution of fires through time.

## Scientific value of FIRED

`FIRED` converts satellite observations into a format that supports event-based fire analysis.

This enables questions such as:

- How quickly do fires grow?
- How do fire sizes vary across landscapes?
- What environmental conditions influence fire expansion?

Most importantly, `FIRED` provides time-resolved fire perimeters, which allow researchers to study the geometry of wildfire growth.

## Related pages

- [FIRED and CubeDynamics](fired-cubedynamics.md)
- [Fire Growth Trajectories](../methods/fire-growth-trajectories.md)
- [Satellite Fire Datasets](satellite-fire-datasets.md)
