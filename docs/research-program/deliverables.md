# Deliverables

## Major deliverables

### 1. Global fire growth trajectory dataset

The project will produce a standardized dataset describing how fires grow through time. Using satellite burned-area products and the `FIRED` event reconstruction system, the research team will reconstruct daily fire perimeters for many wildfire events.

Each fire will include:

- perimeter length through time
- burned area through time
- geometric complexity metrics
- environmental metadata

#### Why this matters

Most fire datasets record final burned area or ignition locations. Few datasets capture the dynamic geometry of fire growth. This dataset would provide a large-scale empirical foundation for studying wildfire expansion as a spatial process.

It also becomes reusable infrastructure for research questions beyond the scaling hypothesis.

### 2. Open-source scaling diagnostics

The project will develop analytical tools for measuring geometric scaling relationships in wildfire growth.

These tools will include methods for:

- perimeter-time scaling analysis
- fractal dimension estimation
- scaling collapse diagnostics
- geometric comparison of fire trajectories

The diagnostics will be released as modules within `CubeDynamics` so that other researchers can apply them to both observational data and model outputs.

#### Why this matters

Current wildfire models are typically evaluated using local metrics such as spread rate or burn severity. Scaling diagnostics introduce a new way to test models: whether they reproduce the large-scale geometry of real fires.

### 3. Empirical characterization of wildfire scaling

The project will analyze many fire trajectories to determine:

- whether a consistent perimeter growth exponent exists
- when scaling appears during a fire's lifetime
- how scaling varies across ecosystems and climates

This work fills a gap between detailed fire behavior experiments and statistical studies of fire regimes.

#### Why this matters

Understanding the geometry of wildfire expansion provides insight into how local spread processes scale up to landscape-scale fire behavior.

### 4. Mechanistic modeling experiments

The project will test candidate mechanisms capable of generating wildfire scaling patterns.

Minimal models will represent processes such as:

- diffusion-like spread
- connectivity-driven spread across heterogeneous fuels
- anisotropic wind-driven propagation
- long-distance spotting

Each model will generate synthetic fire trajectories that can be analyzed using the same scaling diagnostics applied to satellite observations.

#### Why this matters

This approach connects empirical observations with underlying physical processes and helps identify which mechanisms shape wildfire growth geometry.

### 5. Benchmark analysis of existing fire models

The scaling diagnostics will be applied to outputs from wildfire simulators such as:

- `FARSITE`
- `WRF-Fire`
- `FIRETEC`

This will reveal whether current fire models reproduce the geometric scaling properties observed in real fires.

#### Why this matters

This provides a new benchmark for wildfire model validation based on emergent system behavior rather than only local spread rates.

### 6. Theoretical framework for wildfire growth geometry

The final deliverable is a conceptual synthesis explaining how wildfire growth emerges from interactions among:

- fuel connectivity
- atmospheric forcing
- landscape heterogeneity
- fire spread physics

This framework links wildfire science with broader theories of spatial dynamics and complex systems.
