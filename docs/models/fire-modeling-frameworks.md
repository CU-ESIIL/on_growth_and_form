# Fire Modeling Frameworks and Scaling Perspectives

## Overview

Wildfire modeling has historically focused on predicting local fire spread rates based on combustion physics, fuel characteristics, weather, and terrain. Operational fire simulators have become increasingly sophisticated in representing these physical processes. However, comparatively little attention has been devoted to understanding the large-scale geometric and scaling properties of wildfire perimeters that emerge from these local dynamics.

This note reviews dominant wildfire modeling frameworks and evaluates them from the perspective of spatial scaling and interface growth dynamics.

The goal is not to critique existing models but to clarify how they conceptualize fire spread and where opportunities exist to incorporate scaling-based insights.

## 1. Rate-of-spread models (Rothermel framework)

The foundational framework for operational wildfire modeling originates from the Rothermel (1972) surface fire spread model.

The Rothermel model predicts the rate of spread (`ROS`) of a fire front based on factors including:

- fuel load
- fuel moisture
- wind speed
- slope

Conceptually the model computes a local velocity for the fire front:

```text
ROS = f(fuel, wind, slope, moisture)
```

Fire simulators then propagate the fire perimeter across a landscape using this local velocity field.

Major operational tools built on this framework include:

- FARSITE
- FlamMap
- Prometheus
- BEHAVE

### Geometric interpretation

In these models the fire is represented as a moving one-dimensional boundary embedded in a two-dimensional landscape.

Each point on the boundary spreads outward according to a locally computed rate of spread.

This formulation implicitly treats wildfire spread as a front propagation problem.

## 2. Huygens wavelet propagation

Many fire simulators propagate fire fronts using a geometric approach inspired by Huygens' principle.

In this approach:

- each point on the fire perimeter generates a small expanding wavelet
- the envelope of these wavelets forms the new perimeter

This method allows fire perimeters to evolve dynamically across heterogeneous landscapes.

However, the approach assumes that the expanding front remains geometrically smooth at small scales.

Consequently, fractal interface roughness or scaling behavior is not explicitly represented.

## 3. Elliptical fire growth models

A widely used extension of rate-of-spread models assumes that fire growth at each perimeter point forms an ellipse whose shape depends on wind and slope.

### Key characteristics

- the major axis aligns with wind direction
- the minor axis represents backing fire

This approach captures directional spread but still assumes a smooth perimeter geometry.

From a scaling perspective, elliptical growth models emphasize anisotropic velocity fields rather than fractal boundary dynamics.

## 4. Cellular automata fire models

A different class of wildfire models uses cellular automata (`CA`) to simulate fire spread.

In these models:

- landscapes are represented as grids
- each cell ignites based on neighboring cells
- stochastic rules govern spread probability

These models can generate:

- irregular burn patterns
- scale-dependent clustering
- fractal fire scars

Cellular automata models therefore naturally produce complex spatial patterns and have occasionally been used to study scaling properties of wildfire spread.

However, most `CA` models have been used primarily as exploratory tools rather than as operational fire simulators.

## 5. Percolation-based fire models

Some theoretical wildfire models interpret fire spread as a percolation process on landscapes.

In this framework:

- vegetation patches act as connected nodes
- fire spreads through connected fuel pathways

When fuel connectivity approaches a critical threshold, fire clusters become fractal structures with universal scaling properties.

Percolation theory predicts that cluster boundaries near criticality exhibit a fractal dimension close to:

```text
D ≈ 4/3
```

This prediction is notable because it matches fractal dimensions observed in several natural interface systems.

## 6. Physics-based computational fire models

More sophisticated fire models explicitly simulate combustion physics and atmospheric interactions.

Examples include:

- FIRETEC
- WFDS (Wildland-Urban Interface Fire Dynamics Simulator)
- WRF-Fire
- CAWFE

These models solve coupled equations describing:

- turbulent flow
- heat transfer
- combustion
- atmospheric feedback

In these models wildfire spread emerges as a result of physical interactions rather than prescribed spread rules.

However, even these high-fidelity models rarely analyze the scaling geometry of fire perimeters produced by the simulations.

## 7. Implicit geometric assumptions of current models

Across modeling frameworks, several implicit geometric assumptions are common:

1. Fire spread is governed by local velocity rules.
2. The fire perimeter behaves as a smooth advancing interface.
3. Large-scale fire geometry emerges from accumulated local spread decisions.

What most models do not explicitly examine are:

- fractal boundary dimensions
- scaling laws of perimeter growth
- universal exponents governing interface expansion

Most wildfire models focus on local physics rather than emergent scaling geometry.

## 8. Diffusion vs interface propagation

Wildfire spread is sometimes loosely compared to diffusion, but operational models actually behave differently.

Diffusion systems follow equations such as:

```text
∂C/∂t = D ∇²C
```

In contrast, wildfire simulators often solve front propagation equations of the form:

```text
∂φ/∂t + R |∇φ| = 0
```

where `φ` represents the evolving fire front.

These equations describe advancing interfaces rather than diffusive spreading.

Thus classical fire models do not explicitly assume diffusion.

Instead they assume locally determined front velocity.

## 9. The missing scaling perspective

Although wildfire models can capture local spread physics, the field has devoted relatively little attention to the large-scale scaling behavior of wildfire perimeters.

Satellite observations now allow researchers to examine:

- perimeter growth through time
- fractal boundary geometry
- scaling relationships between area, perimeter, and time

Emerging evidence suggests that wildfire perimeters may exhibit:

```text
P(t) ~ t^(2/3)
```

consistent with fractal interface growth with dimension near:

```text
D ≈ 4/3
```

Understanding how local fire spread processes produce these emergent scaling laws represents an important open research question.

## 10. Research opportunity

A promising direction for wildfire science is to bridge two perspectives:

1. Local fire spread physics, which governs ignition and short-range propagation.
2. Emergent geometric scaling, which governs large-scale fire perimeter growth.

Understanding how microscopic processes generate macroscopic fractal geometry could significantly improve theoretical understanding of wildfire dynamics.

This approach connects wildfire science to broader fields including:

- statistical physics
- percolation theory
- fractal geometry
- interface growth dynamics

## Conclusion

Modern wildfire models provide powerful tools for predicting fire behavior based on physical processes.

However, the geometric scaling behavior of wildfire perimeters remains relatively unexplored.

Incorporating scaling perspectives into wildfire modeling may provide new insights into the emergent spatial dynamics of large fires and help link local spread mechanisms with landscape-scale fire patterns.
