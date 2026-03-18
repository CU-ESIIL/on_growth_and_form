# Benchmarking Existing Fire Models

This page focuses on how scaling diagnostics can be used to evaluate operational or physics-based fire models.

## Why benchmarking matters

Many fire models are assessed mainly through local spread rates, final extent, or behavior under specific conditions. This project adds another question:

Do the simulated fires exhibit the same large-scale perimeter geometry as observed fires once definition scale and measurement scale are made explicit?

## Candidate benchmark outputs

- perimeter growth exponent
- area-perimeter scaling
- boundary roughness or fractal dimension
- presence or absence of a regime-specific scaling interval
- `L_d(ε)` curves for observed and simulated perimeters under aligned boundary definitions
- sensitivity of inferred geometry to sensor resolution, temporal aggregation, and smoothing choices

## What this contributes

This gives wildfire modeling a new evaluation language based on emergent geometry, not only on local behavior rules. It also reframes validation as a curve-matching problem across scales rather than a point comparison at one chosen perimeter definition or map resolution.

## Related pages

- [Fire Modeling Frameworks](fire-modeling-frameworks.md)
- [Scaling Diagnostics](../methods/scaling-diagnostics.md)
- [Wildfire Scaling Work Plan](../research-program/work-plan.md)
- [Scale-Conditioned WUI Geometry](../theory/scale-conditioned-wui-geometry.md)
