# FIRED

`FIRED` is the event-reconstruction layer of the project.

## What FIRED does

Satellite burned-area products tell us which pixels burned and when. `FIRED` asks the more useful event-level question: which of those burned pixels belong to the same fire?

By clustering burned pixels through space and time, `FIRED` reconstructs:

- individual wildfire events
- event start and end dates
- daily perimeter or progression structure
- total burned area

## Why FIRED matters for this project

The scaling questions in this repository depend on trajectories, not just end states. We need to know how fire perimeter and area change through time, not only where a burn scar ended up.

That makes `FIRED` foundational for:

- fire growth trajectories
- perimeter-time scaling analysis
- scaling-regime detection
- comparison across many fires

## Related pages

- [FIRED and CubeDynamics](fired-cubedynamics.md)
- [Fire Growth Trajectories](../methods/fire-growth-trajectories.md)
- [Satellite Fire Datasets](satellite-fire-datasets.md)
