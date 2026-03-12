# Satellite Fire Datasets

This page summarizes the observation layer that supports the wildfire scaling program.

## Why datasets matter here

The scaling questions in this repository depend on time-resolved, spatially explicit observations of fire activity. That means burned-area and active-fire products are not just supporting data; they determine what kinds of geometric measurements are even possible.

## Core dataset families

- MODIS burned area products, especially `MCD64A1`
- VIIRS active fire detections
- FireCCI burned-area products
- MTBS for U.S. burn severity and event characterization
- event-reconstructed products such as the Global Fire Atlas and `FIRED`

## What each dataset contributes

- burned-area grids provide event footprints and progression timing
- active-fire detections provide higher-frequency fire activity indicators
- event-reconstructed products make fire trajectories analytically tractable
- regional products help with validation and context

## Relationship to the literature

The working bibliography in the repository already includes several of the key data references. See [Literature](../literature/) for the current bibliography and thematic map.

## Related pages

- [FIRED](fired.md)
- [FIRED and CubeDynamics](fired-cubedynamics.md)
- [Bibliography](../literature/bibliography.md)
