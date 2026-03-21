# Method 1B: Evaluating Velocity as a Descriptor of Fire Spread

## Overview

Wildfire spread is commonly described using a rate of spread or velocity, often treated as a well-defined property of the fire front. In this section, we test that assumption directly. Rather than accepting velocity as a fundamental variable, we treat it as a measurable quantity whose definition may depend on how the fire boundary is represented.

Building on the measurement framework established previously, we compute multiple definitions of fire spread velocity from the same underlying fire trajectories and evaluate their consistency, stability, and relationship to boundary geometry. In particular, we test whether these definitions converge to a consistent description of motion or diverge as fire behavior becomes more complex.

The goal is to determine whether velocity can serve as a reliable, scale-consistent descriptor of wildfire dynamics, or whether it breaks down under realistic fire behavior, including heterogeneous growth, anisotropy, and boundary deformation.

All calculations are implemented within the CubeDynamics framework, using shared data cubes and perimeter extraction operators to ensure that all velocity estimates are derived from identical underlying data.

## Conceptual framework

A wildfire is not a rigid object translating through space, but a deforming, branching interface that evolves over time. As a result, velocity is not uniquely defined. Different methods of measuring motion emphasize different aspects of the system, including bulk displacement, local boundary advance, and directional spread.

Crucially, velocity is defined as a change in position through time, and therefore depends on how position itself is defined. In a system where the boundary is continuously deforming, branching, and changing topology, there is no single, unambiguous definition of position. As a result, velocity inherits this ambiguity and becomes inherently dependent on representation, scale, and measurement method.

We therefore treat velocity as a family of measurements rather than a single quantity. Each definition is computed and evaluated independently, and agreement or divergence between them is used as a diagnostic of whether velocity is a meaningful descriptor of the system.

## Experimental design: velocity definitions and tests

### Step 1: compute centroid-based velocity

We compute the centroid of the burned area at each time step and measure its displacement through time. This provides a bulk velocity representing overall fire movement. However, this measure ignores deformation of the boundary and can remain small even when the fire is expanding rapidly. The test is whether centroid velocity correlates with fire growth and whether it captures periods of rapid expansion.

### Step 2: compute perimeter-normal velocity

We estimate local velocities along the fire boundary by measuring displacement of perimeter points between successive time steps. This produces a distribution of local spread rates rather than a single value.

We evaluate the variance of local velocities along the boundary and how this variance changes as the boundary becomes more complex. If local velocities vary widely, that indicates that a single global velocity is not representative.

### Step 3: compute area-equivalent velocity

We define an effective velocity based on area growth, translating changes in burned area into an equivalent radial expansion rate. This provides a scalar measure that is directly tied to total growth. We compare this to centroid- and boundary-based velocities to test consistency.

### Step 4: compute directional velocities

We project fire growth along different directions, particularly along and across environmental gradients such as wind direction. This produces directional velocities that capture anisotropic behavior. We evaluate whether directional velocities diverge under strong forcing and whether a single velocity value can summarize this behavior.

### Step 5: compare velocity definitions

We compare all velocity measures across time, spatial scale, and growth stage. In practice, that means comparing them across spatial resolution, temporal sampling interval, and fire-life-stage segmentation.

We evaluate agreement between velocity definitions, divergence as boundary roughness increases, and stability under resampling and changing measurement resolution. This step explicitly tests whether velocity is scale-dependent, meaning that its value changes as a function of how the system is observed. Such dependence would indicate that velocity is not an intrinsic property of the fire, but an artifact of measurement.

If different velocity definitions produce inconsistent or unstable values, or vary systematically with scale, velocity is not a well-posed quantity.

### Step 6: relate velocity to boundary geometry

We test whether discrepancies in velocity estimates are related to boundary complexity. Specifically, we compare velocity divergence to perimeter length, roughness metrics, and fractal dimension.

This step directly links the instability of velocity to the geometric properties of the fire boundary identified in the measurement section. If divergence increases with boundary complexity, that indicates that velocity breaks down as the interface becomes more irregular, supporting the hypothesis that boundary geometry, not velocity, is the more fundamental descriptor of fire growth.

### Step 7: evaluate velocity across growth regimes

We segment fires into growth stages, such as early, expansion, and late, and compute velocity measures within each stage. We then test whether velocity definitions agree in early stages but diverge later, and whether they remain stable or become increasingly inconsistent. This determines whether velocity is only meaningful under limited conditions.

### Step 8: evaluate velocity under extreme conditions

We isolate periods of rapid growth and strong environmental forcing and compute all velocity measures. The key questions are whether velocity definitions diverge under extreme conditions and whether they fail to capture rapid, directional spread.

If velocity becomes unstable or inconsistent under these conditions, it cannot serve as a reliable descriptor of extreme fire behavior.

## Inference

We evaluate whether velocity can serve as a consistent and meaningful descriptor of wildfire spread by testing consistency across definitions, stability across scales and time, and sensitivity to boundary complexity and environmental forcing.

If velocity measures diverge, vary with definition, become unstable as the boundary evolves, or depend systematically on measurement scale, we conclude that velocity is not a well-defined or sufficient state variable for wildfire dynamics.

Because velocity is a derived quantity that depends on how the fire boundary is represented, failure of convergence across definitions and scales indicates that it cannot serve as a primary descriptor of wildfire spread in a system characterized by deformation, heterogeneity, and multi-scale dynamics.

## Outcome

This analysis provides a direct empirical test of the validity of velocity-based descriptions of wildfire spread. By demonstrating that velocity becomes ambiguous, definition-dependent, and scale-dependent as boundary complexity increases, it establishes that velocity cannot serve as a primary state variable for wildfire spread across realistic conditions.

These results show that alternative descriptors, such as boundary geometry, scaling relationships, and interface evolution, are required because they remain well-defined even when velocity does not.

This conclusion provides the conceptual and empirical foundation for the generative modeling framework that follows, in which wildfire growth is described in terms of interface evolution and geometry rather than uniform spread velocity. In particular, it motivates the use of geometry- and scaling-based diagnostics that remain stable under deformation and form the basis of the mechanism-testing framework developed in the subsequent methods section.
