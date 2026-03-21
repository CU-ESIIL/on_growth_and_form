# CubeDynamics

## Overview

While `FIRED` defines individual fire events, environmental datasets often exist in many different formats and resolutions. Managing and analyzing these datasets consistently can be difficult.

`CubeDynamics` addresses this challenge by treating environmental data as spatiotemporal data cubes.

The central idea is that Earth system data should be organized around three core dimensions:

- space (`x`, `y`)
- time (`t`)
- variables

This structure forms a multidimensional array known as a data cube.

## What is a data cube?

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

## The grammar of cubes

`CubeDynamics` proposes a structured set of operations for working with data cubes.

This idea is inspired by concepts such as the grammar of graphics in data visualization.

Typical cube operations include:

- subsetting a cube
- slicing a cube along spatial or temporal dimensions
- aggregating variables
- combining multiple cubes
- computing derived metrics

By formalizing these operations, `CubeDynamics` creates a consistent framework for analyzing Earth system data.

## Computational benefits

The cube-based approach provides several advantages:

1. Scalability: large satellite datasets can be processed efficiently because operations apply across entire arrays rather than individual files.
2. Reproducibility: workflows become standardized and easier to reproduce.
3. Interoperability: multiple environmental datasets can be combined consistently.

For example, researchers can analyze relationships between fire activity and environmental drivers such as vegetation, climate, or topography in one structured framework.

## Related pages

- [FIRED and CubeDynamics](fired-cubedynamics.md)
- [Environmental Data Science Stack](environmental-data-science-stack.md)
- [Scaling Diagnostics](../methods/scaling-diagnostics.md)
