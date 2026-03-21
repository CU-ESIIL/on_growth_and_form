# Method 2: Generative Modeling and Experimental Design

## Overview

Given a validated empirical result that wildfire perimeter grows approximately as `P(t) ~ t^(2/3)`, the goal of this section is to determine which physical processes are capable of producing that behavior. We treat this as a controlled experimental system in which candidate mechanisms are instantiated as generative models and subjected to identical measurement, comparison, and falsification criteria.

The preceding measurement analysis establishes that this scaling relationship is robust across spatial resolution, temporal sampling, and fire events, and that boundary geometry exhibits consistent, nontrivial structure. These findings motivate a mechanistic hypothesis: wildfire growth is governed by the dynamics of a two-dimensional reactive interface whose geometry controls throughput, that is, fuel conversion rate.

We therefore use the scaling exponent `beta` and associated geometric diagnostics as discriminating signatures. Distinct mechanism classes predict distinct exponent regimes and boundary statistics; models are accepted or rejected based on their ability to reproduce `beta ≈ 2/3`, observed boundary geometry such as multiscale roughness and perimeter-area relationships, and robustness across parameter and environmental variation.

All simulations and analyses are implemented within the CubeDynamics framework. Fires, observed and simulated, are represented as labeled spatiotemporal arrays, `xarray DataArrays` or `Datasets`, with dimensions `(time, y, x)` and associated coordinates and metadata. Computation is parallelized with `dask`. Measurement operators, including perimeter extraction, area, growth rates, scaling estimation, and multiscale geometry, are shared across observed and simulated data to ensure comparability. Environmental fields are attached to evolving fire boundaries using FireVase.

## Data structures, operators, and pipeline

Each fire is a cube `C(t, y, x)` with binary or probabilistic burn state, optionally accompanied by continuous fields such as spread rate, fuel, or moisture. Observed fires are derived from FIRED products, and simulated fires produce the same schema.

Core operators in CubeDynamics are:

- `extract_perimeter(C_t)`: boundary extraction via marching squares or contour tracing on binary masks; returns ordered polylines and raster edge sets.
- `compute_area(C_t)`: pixel-integral area accounting for CRS and pixel size.
- `compute_perimeter(P_t)`: length from polyline geometry, including pixel-edge correction and optional smoothing.
- `growth_rate(A_t)`: finite differences `dA/dt` with Savitzky-Golay smoothing for noise control.
- `scaling_beta(P_t, t)`: log-log regression using OLS, Theil-Sen, and Bayesian hierarchical variants with global and rolling-window estimates; returns `beta`, confidence intervals, and stability diagnostics.
- `roughness_metrics(P_t)`: multiscale perimeter, box-counting, perimeter-area exponent, fractal dimension estimates, and curvature distributions.
- `anisotropy(P_t, wind_t)`: directional growth via projection of local normals against wind vectors and ellipse fitting for shape anisotropy.

All operators are implemented as composable functions that accept and return `xarray` objects, enabling lazy evaluation and parallel execution with `dask` across many fires and parameter sweeps.

## Experimental design: mechanism elimination

### Step 1: scaling exponent as discriminating signature

For each simulated trajectory, estimate `beta` from `P(t)` versus `t` using multiple estimators, including OLS on log-log space, Theil-Sen for robustness, and optional Bayesian hierarchical models across fires.

Global `beta` is estimated from the full trajectory, while rolling `beta` uses window sizes spanning 3 to 10 time steps to assess stability. Confidence intervals are derived through bootstrap resampling and, where relevant, posterior intervals from hierarchical models such as PyMC or Bambi. Models are rejected if `beta` falls far from `2/3` or if it is unstable across time.

### Step 2: smooth-front baseline

The baseline hypothesis is that fire behaves as a smooth advancing wave with local spread.

Implementation includes reaction-diffusion systems such as Fisher-KPP, `∂u/∂t = D∇²u + ru(1-u)`, thresholded to define burned area; Eikonal or fast marching formulations, `|∇T(x)| F(x) = 1`, with speed field `F`; and finite-volume PDE solvers such as FiPy for advection-diffusion variants. Outputs are time-indexed binary burn masks with perimeters extracted at each step.

The expectation is limited roughening and an exponent closer to `1/2` or otherwise sub-`2/3`. If `beta` does not approach `2/3` and cannot be stabilized by reasonable parameterization, smooth-front dynamics are eliminated as a sufficient explanation.

### Step 3: dimensional adequacy

The next test asks whether models must embed fire as a two-dimensional interface to generate endogenous boundary growth.

One-dimensional boundary evolution is implemented as explicit polyline evolution with local speed rules but no embedding in a field. Two-dimensional embedded models instead use raster fields where burning occupies cells and boundaries emerge from the field dynamics. Diagnostics include perimeter growth independent of area, the emergence of new boundary segments, and roughness metrics. One-dimensional models that cannot generate increasing interface length are excluded, and only two-dimensional embeddings proceed.

### Step 4: roughening-interface dynamics

The hypothesis here is that interface roughening drives growth through an increasing reactive boundary.

Implementation includes stochastic cellular growth in the Eden family, where frontier cells ignite neighbors with probability modulated by local heterogeneity; KPZ-inspired updates, where a height or interface field evolves through local growth, lateral spreading, and noise before being mapped to raster occupancy; and heterogeneity fields sampled either as spatial random fields or from observed layers.

Retained models must reproduce `beta ≈ 2/3` together with realistic roughness evolution, perimeter-area scaling, and multiscale perimeter structure.

### Step 5: geometry to throughput coupling

This step tests the hypothesis that growth rate scales with interface length or complexity, that is, that growth is throughput-limited.

We compute `A(t)`, `P(t)`, `dA/dt`, and `D(t)`, then fit relationships such as `dA/dt = α P(t) + ε` and `dA/dt = α P(t) f(D) + ε`, comparing them with AIC, BIC, or cross-validation. Support for the throughput mechanism is strongest when growth scales stably with perimeter and, where relevant, with geometric complexity.

### Step 6: connectivity baseline

The next null asks whether static fuel connectivity alone explains geometry and growth.

Site or bond percolation is simulated on grids with occupancy probability `p`, and ignition spreads through connected clusters. Connected-component labeling is used to track clusters. If geometry matches observed fires but `beta` does not approach `2/3`, connectivity is interpreted as necessary but insufficient rather than as a complete explanation.

### Step 7: network-constrained transport

This step tests whether spread follows structured pathways that impose transport constraints.

Graphs embedded in two dimensions are used, with nodes representing fuel patches and edges representing pathways, and spread proceeds stochastically along edges. Hybrid models combine network transport with raster spread by allowing edges to seed local spread in the surrounding field. Candidate mechanisms are retained only if both `beta` and geometry match robustly.

### Step 8: interface-environment coupling

Here the goal is to determine whether scaling is intrinsic, externally forced, or coupled with environment.

Using FireVase, perimeter segments are intersected with co-registered environmental rasters such as wind vectors, vapor pressure deficit, and moisture proxies at each time step. Segment-level statistics are aggregated as means, quantiles, and directional alignments.

Three tests follow. First, interface-conditioned scaling estimates `beta` within environmental bins. Second, exposure-geometry analysis relates roughness or length to the fraction of boundary under favorable conditions. Third, coupled growth models of the form `dA/dt ~ P + env + P×env` quantify interactions. Mechanisms are classified as intrinsic when `beta` is invariant, forced when `beta` varies with environment, and coupled when interactions are significant.

### Step 9: growth regimes

Mechanisms may be phase-dependent, so we identify regimes using change points in `dA/dt` and rolling `beta`, via Bayesian change-point models or threshold heuristics. Time indices are labeled with stage identifiers and propagated as cube coordinates. The question is whether scaling is regime-specific or persistent.

### Step 10: extreme and fast-fire regimes

A viable mechanism must also reproduce extreme, anisotropic growth.

Extreme windows are defined through thresholds on `dA/dt`, wind alignment, and vapor pressure deficit. Within those windows, we measure `beta`, anisotropy, and roughness, and then simulate matched forcing scenarios, whether through advection fields in PDE models or biased probabilities in cellular models. Models that fail to reproduce rapid, directional expansion together with the associated geometry are rejected.

### Step 11: robustness and sensitivity

Finally, valid mechanisms should produce `beta ≈ 2/3` across broad parameter ranges rather than only under narrow tuning.

We therefore perform global sensitivity analysis through SALib, using Sobol or Morris designs, and run parameter sweeps across heterogeneity, rates, connectivity, and forcing. Provenance is recorded for each run, including parameters, random seeds, and diagnostics. Mechanisms are preferred when they exhibit wide and stable regions of parameter space yielding the target exponent and geometry.

## Inference

These steps are applied sequentially, and mechanism classes are eliminated whenever they fail the criteria for `beta`, geometry, robustness, or extreme-fire behavior. The survivors define the minimal necessary ingredients: a two-dimensional evolving interface, endogenous roughening, heterogeneous connectivity, constrained transport, and geometry-environment coupling.

## Outcome

The result is a constrained, testable account of wildfire growth that links observed scaling and boundary geometry to underlying processes. The architecture built around CubeDynamics and FireVase provides a reusable, extensible platform in which new model classes can be added and evaluated under identical measurement conditions.
