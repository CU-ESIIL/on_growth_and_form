# FIRED and CubeDynamics: A System for Event-Based Earth System Analysis

## Overview

Modern environmental science increasingly relies on large volumes of satellite observations and Earth system datasets. While these datasets provide global coverage and high temporal resolution, they are often difficult to analyze because the raw data are stored as disconnected pixel grids or files rather than coherent environmental events.

Two complementary resources developed through Earth Lab and ESIIL address this challenge:

- `FIRED` (Fire Event Delineation), an algorithm and dataset that converts satellite burned-area pixels into coherent wildfire events
- `CubeDynamics`, a computational framework that provides a "grammar of cubes" for analyzing environmental datasets as structured spatiotemporal objects

Together, these tools form a system for transforming satellite observations into structured environmental events that can be analyzed using scalable computational methods.

This note explains each resource and describes how they function together as a unified scientific framework.

## 1. FIRED: Fire Event Delineation

### Purpose

Satellite burned-area products provide global records of fire activity, but these datasets typically represent fire as individual burned pixels detected on specific days. While this is useful for monitoring, it does not directly reveal how individual fires grow, merge, or evolve through time.

The purpose of `FIRED` is to convert these raw burned-area pixels into individual fire events with spatial and temporal structure.

In other words, `FIRED` answers the question:

Which burned pixels belong to the same fire?

### The core problem

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

### How the FIRED algorithm works

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

### Output structure of FIRED

The resulting dataset transforms pixel observations into event-level information.

Each fire event includes:

- unique fire identifier
- event start and end dates
- daily burn progression
- final fire perimeter
- total burned area

This structure enables researchers to reconstruct the evolution of fires through time.

### Scientific value of FIRED

`FIRED` converts satellite observations into a format that supports event-based fire analysis.

This enables questions such as:

- How quickly do fires grow?
- How do fire sizes vary across landscapes?
- What environmental conditions influence fire expansion?

Most importantly, `FIRED` provides time-resolved fire perimeters, which allow researchers to study the geometry of wildfire growth.

## 2. CubeDynamics: The Grammar of Cubes

### Purpose

While `FIRED` defines individual fire events, environmental datasets often exist in many different formats and resolutions. Managing and analyzing these datasets consistently can be difficult.

`CubeDynamics` addresses this challenge by treating environmental data as spatiotemporal data cubes.

The central idea is that Earth system data should be organized around three core dimensions:

- space (`x`, `y`)
- time (`t`)
- variables

This structure forms a multidimensional array known as a data cube.

### What is a data cube?

A data cube is a structured dataset where each value corresponds to a location, time, and variable.

For example, a cube may include:

- latitude
- longitude
- date
- burned area
- vegetation index
- temperature
- wind speed

Each slice of the cube represents a spatial map at a given time.

Each vertical column represents a time series at a specific location.

This representation allows environmental processes to be analyzed systematically.

### The grammar of cubes

`CubeDynamics` proposes a structured set of operations for working with data cubes.

This idea is inspired by concepts such as the "grammar of graphics" in data visualization.

Typical cube operations include:

- subsetting a cube
- slicing a cube along spatial or temporal dimensions
- aggregating variables
- combining multiple cubes
- computing derived metrics

By formalizing these operations, `CubeDynamics` creates a consistent framework for analyzing Earth system data.

### Computational benefits

The cube-based approach provides several advantages:

1. Scalability: large satellite datasets can be processed efficiently because operations apply across entire arrays rather than individual files.
2. Reproducibility: workflows become standardized and easier to reproduce.
3. Interoperability: multiple environmental datasets can be combined consistently.

For example, researchers can analyze relationships between fire activity and environmental drivers such as vegetation, climate, or topography in one structured framework.

## 3. How FIRED and CubeDynamics work together

`FIRED` and `CubeDynamics` represent two layers of an integrated analytical system.

### Layer 1: Event reconstruction

`FIRED` transforms raw satellite burned-area pixels into structured wildfire events.

This step converts pixel observations into meaningful fire objects.

### Layer 2: Spatiotemporal analysis

`CubeDynamics` provides the computational framework for analyzing these events within the broader Earth system context.

Fire events can be embedded within spatiotemporal cubes containing additional environmental variables.

## Combined workflow

```text
Satellite observations
  -> burned-area pixels
  -> FIRED event delineation
  -> fire events with daily perimeters
  -> CubeDynamics spatiotemporal cubes
  -> analytical workflows
  -> scientific insight
```

## 4. Example integrated analysis

Using the combined system, researchers can:

1. Load fire events generated by `FIRED`.
2. Load environmental cubes including vegetation indices, climate data, and fuel moisture.
3. Align these datasets spatially and temporally.
4. Compute metrics describing fire growth dynamics.

Example analyses include:

- fire perimeter growth through time
- burned area expansion
- relationships between fire spread and environmental conditions

## 5. Enabling scaling and geometry research

One particularly powerful application of this integrated system is the study of wildfire geometry and scaling behavior.

Because `FIRED` provides daily fire perimeters, researchers can reconstruct functions such as:

- perimeter as a function of time
- burned area as a function of time

Using `CubeDynamics`, these measurements can be computed across thousands of fires.

This enables questions such as:

- Do wildfire perimeters follow consistent scaling laws?
- Are wildfire boundaries fractal?
- Do scaling relationships vary across ecosystems?

Such analyses require exactly the type of event-based and cube-based infrastructure provided by `FIRED` and `CubeDynamics`.

## 6. Conceptual significance

The integration of `FIRED` and `CubeDynamics` represents a shift in how environmental phenomena are studied.

Rather than analyzing isolated pixels or individual datasets, researchers can analyze environmental events embedded within multidimensional Earth system data.

This approach supports the discovery of large-scale patterns and emergent dynamics that may not be visible through traditional analysis methods.

## Conclusion

`FIRED` and `CubeDynamics` together provide a framework for event-based environmental science.

`FIRED` reconstructs wildfire events from satellite observations, while `CubeDynamics` provides the computational grammar for analyzing those events within a broader spatiotemporal data ecosystem.

By combining event delineation with cube-based analysis, researchers can investigate complex environmental processes, including wildfire growth, in ways that integrate geometry, dynamics, and environmental context.
