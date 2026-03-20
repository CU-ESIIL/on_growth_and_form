# Wildfire Modeling Master Bibliography

## Historical context

Wildfire modeling began as an effort to make fire computable. Before the modern era, agencies relied mainly on field experience, fire-danger indices, and descriptive rules. The decisive shift came with Rothermel's 1972 surface-fire spread model, which turned fuels, wind, and slope into a tractable mathematical prediction of rate of spread and intensity. That innovation was transformative because it made operational forecasting possible with the data managers actually had, but it also set the field on a path in which fire was treated primarily as a local spread process rather than as a full evolving spatial structure.

The next major step was to make fire spatial. Models such as FARSITE extended local spread equations into two-dimensional fire growth using wavefront or Huygens-style propagation, allowing users to simulate evolving perimeters over time. This was a major advance for incident support, planning, and training because it shifted the central modeling object from a point estimate of spread rate to an advancing fire boundary on a heterogeneous landscape. Minimum-travel-time methods then made this lineage more computationally efficient and laid the groundwork for probabilistic risk systems that simulate many fires rather than a single deterministic event. In that sense, the operational lineage evolved from "how fast will fire spread here?" to "how will a fire footprint grow across a landscape?" and then to "what is the distribution of possible fires over many scenarios?"

A parallel lineage emerged because empirical growth models could not fully represent plume behavior, convective feedbacks, or coupled fire-atmosphere dynamics. That led to physics-based models, marked early by coupled atmosphere-fire work in the 1990s and later by systems such as WRF-Fire. Here the innovation was not just better spread prediction but a different ontology: fire became a coupled fluid-dynamical system interacting with weather, turbulence, and heat transfer. These models greatly increased mechanistic realism and opened the door to studying extreme fire behavior, but they also introduced new burdens in computation, data, and unresolved scale interactions. In practice, the physics lineage grew because the field needed more realism under complex conditions, even as that realism became harder to operationalize.

At the same time, other branches developed around heterogeneity, emergence, and long time horizons. Cellular automata and related simulation approaches showed that complex fire patterns could arise from local probabilistic rules, while criticality and scaling perspectives suggested that wildfire regimes may exhibit scale-invariant structure. Separately, landscape-ecology models such as LANDIS and LANDIS-II embedded fire within longer-term succession, disturbance, and ecosystem change, making fire one process among many in century-scale landscape dynamics rather than only an incident-scale event. More recently, machine-learning methods have added a new lineage focused on fast prediction from large datasets. Across all of these branches, the field has steadily expanded what fire models can represent: first local spread, then perimeter growth, then coupled physics, then long-term landscape disturbance, and now data-driven prediction. The phylogeny below should be read in that spirit: not as a strict software genealogy, but as a time-calibrated map of intellectual descent and use-case divergence across the major modeling families.

## Status

This note records a user-provided working bibliography imported on 2026-03-20.

It is intended as a dense long-term storage layer for wildfire modeling literature, including citation metadata, identity links, proposal-relevant summaries, and example citation language.

## Verification status

These entries were imported as provided and have **not** yet been fully checked against original papers, publisher pages, DOI metadata, ORCID records, Google Scholar profiles, or PDFs.

Because verbatim details matter here, preserve this file as an imported reference note and verify any specific entry before treating it as final citation metadata.

## Scope

Each entry below includes:

- Full citation
- DOI or URL
- Author identity layer, including ORCID where available and Google Scholar links as provided
- Summary
- Example citation sentence

## Notes

This is a dense storage document designed for repository use, not for direct reading. It integrates citation, identity, and interpretation layers into a single reference structure.

---

## Rothermel (1972)

Rothermel, Richard C. (1972). *A Mathematical Model for Predicting Fire Spread in Wildland Fuels*. USDA Forest Service INT-115.

**DOI/URL:**  
<https://www.fs.usda.gov/rm/pubs_int/int_rp115.pdf>

**Authors:**

- Rothermel, Richard C.
- Scholar: <https://scholar.google.com/scholar?q=Richard+C+Rothermel>

**Summary:**  
This paper establishes the foundational semi-empirical formulation for surface fire spread, integrating fuel properties, wind, and slope into a rate-of-spread equation. It makes fire computable for operational use but constrains behavior to local equilibrium assumptions, with no explicit representation of cross-scale structure or emergent geometry.

**Example citation:**  
"Operational fire models remain grounded in Rothermel-type local spread equations that do not encode cross-scale geometric constraints."

---

## Albini (1976)

Albini, Frank A. (1976). *Estimating Wildfire Behavior and Effects*. USDA Forest Service INT-30.

**DOI/URL:**  
<https://www.fs.usda.gov/rm/pubs_int/int_gtr030.pdf>

**Authors:**

- Albini, Frank A.
- Scholar: <https://scholar.google.com/scholar?q=Frank+A+Albini>

**Summary:**  
Albini extends the empirical spread framework to additional fire behavior metrics such as intensity and spotting, reinforcing the paradigm of fire as a modular system composed of separable processes.

**Example citation:**  
"Early extensions treated fire behavior as separable modules such as spread, intensity, and spotting."

---

## Scott & Burgan (2005)

Scott, Joe H.; Burgan, Robert E. (2005). *Standard Fire Behavior Fuel Models*. RMRS-GTR-153.

**DOI/URL:**  
<https://www.fs.usda.gov/rm/pubs/rmrs_gtr153.pdf>

**Authors:**

- Scott, Joe H.
- ORCID: <https://orcid.org/0000-0002-5506-8321>
- Scholar: <https://scholar.google.com/scholar?q=Joe+H+Scott+fire>
- Burgan, Robert E.
- Scholar: <https://scholar.google.com/scholar?q=Robert+E+Burgan>

**Summary:**  
This work standardizes fuel classifications for use in fire behavior models, enabling consistent application across landscapes while discretizing continuous ecological structure.

**Example citation:**  
"Fuel heterogeneity is typically reduced to discrete classes, limiting representation of continuous scaling behavior."

---

## Finney et al. (2011)

Finney, Mark A.; McHugh, Charles W.; Grenfell, Isaac C.; Riley, Karin L.; Short, Karen C. (2011). *A Simulation of Probabilistic Wildfire Risk Components for the Continental United States*.

**DOI:**  
<https://doi.org/10.1007/s00477-010-0431-2>

**Authors:**

- Finney, Mark A.
- ORCID: <https://orcid.org/0000-0002-6584-1754>
- Scholar: <https://scholar.google.com/scholar?q=Mark+A+Finney>
- McHugh, Charles W.
- Scholar: <https://scholar.google.com/scholar?q=Charles+W+McHugh+fire>
- Grenfell, Isaac C.
- Scholar: <https://scholar.google.com/scholar?q=Isaac+C+Grenfell>
- Riley, Karin L.
- Scholar: <https://scholar.google.com/scholar?q=Karin+L+Riley+fire>
- Short, Karen C.
- Scholar: <https://scholar.google.com/scholar?q=Karen+C+Short+fire>

**Summary:**  
This paper introduces ensemble-based simulation for wildfire risk, shifting focus from deterministic fire prediction to probabilistic estimation of burn likelihood and exposure.

**Example citation:**  
"Ensemble simulation frameworks treat fire as a statistical regime rather than a single deterministic trajectory."

---

## Coen et al. (2013)

Coen, Janice L.; Cameron, M.; Michalakes, J.; Patton, E. G.; Riggan, P. J.; Yedinak, K. M. (2013). *WRF-Fire: Coupled Weather-Wildland Fire Modeling*.

**DOI:**  
<https://doi.org/10.1175/JAMC-D-12-023.1>

**Authors:**

- Coen, Janice L.
- ORCID: <https://orcid.org/0000-0003-3372-183X>
- Scholar: <https://scholar.google.com/scholar?q=Janice+L+Coen>
- Cameron, M.
- Scholar: <https://scholar.google.com/scholar?q=M+Cameron+WRF-Fire>
- Michalakes, J.
- Scholar: <https://scholar.google.com/scholar?q=Jan+Michalakes>
- Patton, E. G.
- Scholar: <https://scholar.google.com/scholar?q=E+G+Patton+NCAR>
- Riggan, P. J.
- Scholar: <https://scholar.google.com/scholar?q=Philip+J+Riggan>
- Yedinak, K. M.
- Scholar: <https://scholar.google.com/scholar?q=K+M+Yedinak>

**Summary:**  
WRF-Fire couples atmospheric dynamics with fire behavior, allowing feedbacks between fire and weather systems and representing a major advance in mechanistic modeling.

**Example citation:**  
"Coupled atmosphere-fire models allow bidirectional feedbacks between fire behavior and atmospheric dynamics."

---

## Malamud et al. (1998)

Malamud, Bruce D.; Morein, Gilad; Turcotte, Donald L. (1998). *Forest Fires: An Example of Self-Organized Critical Behavior*. *Science*.

**DOI:**  
<https://doi.org/10.1126/science.281.5384.1840>

**Authors:**

- Malamud, Bruce D.
- ORCID: <https://orcid.org/0000-0002-7748-197X>
- Scholar: <https://scholar.google.com/scholar?q=Bruce+D+Malamud>
- Morein, Gilad
- Scholar: <https://scholar.google.com/scholar?q=Gilad+Morein>
- Turcotte, Donald L.
- Scholar: <https://scholar.google.com/scholar?q=Donald+L+Turcotte>

**Summary:**  
This paper demonstrates that wildfire regimes exhibit scale-invariant behavior consistent with self-organized criticality, providing a statistical physics framework for understanding fire patterns.

**Example citation:**  
"Fire regimes exhibit scale-invariant dynamics consistent with critical systems."

---

## Scheller et al. (2007)

Scheller, Robert M.; Domingo, John B.; Sturtevant, Brian R.; Williams, Jeffrey S.; Rudy, Amanda; Gustafson, Eric J.; Mladenoff, David J. (2007). *LANDIS-II*.

**DOI:**  
<https://doi.org/10.1016/j.ecolmodel.2006.10.009>

**Authors:**

- Scheller, Robert M.
- ORCID: <https://orcid.org/0000-0003-0785-2709>
- Scholar: <https://scholar.google.com/scholar?q=Robert+M+Scheller>
- Domingo, John B.
- Scholar: <https://scholar.google.com/scholar?q=John+B+Domingo+LANDIS>
- Sturtevant, Brian R.
- Scholar: <https://scholar.google.com/scholar?q=Brian+R+Sturtevant>
- Williams, Jeffrey S.
- Scholar: <https://scholar.google.com/scholar?q=Jeffrey+S+Williams+fire>
- Rudy, Amanda
- Scholar: <https://scholar.google.com/scholar?q=Amanda+Rudy+LANDIS>
- Gustafson, Eric J.
- Scholar: <https://scholar.google.com/scholar?q=Eric+J+Gustafson>
- Mladenoff, David J.
- Scholar: <https://scholar.google.com/scholar?q=David+J+Mladenoff>

**Summary:**  
LANDIS-II provides a modular framework for simulating forest succession and disturbance over long timescales, integrating fire within broader ecosystem dynamics.

**Example citation:**  
"Landscape models integrate fire as one process within long-term ecosystem dynamics."

---

## Jain et al. (2020)

Jain, Piyush; Coogan, Sean C. P.; Subramanian, Subash; Crowley, Mark; Taylor, Stephen; Flannigan, Mike D. (2020). *Machine Learning Applications in Wildfire Science*. *Environmental Reviews*.

**DOI:**  
<https://doi.org/10.1139/er-2020-0019>

**Authors:**

- Jain, Piyush
- Scholar: <https://scholar.google.com/scholar?q=Piyush+Jain+wildfire>
- Coogan, Sean C. P.
- Scholar: <https://scholar.google.com/scholar?q=Sean+C+P+Coogan>
- Subramanian, Subash
- Scholar: <https://scholar.google.com/scholar?q=Subash+Subramanian+wildfire>
- Crowley, Mark
- Scholar: <https://scholar.google.com/scholar?q=Mark+Crowley+wildfire>
- Taylor, Stephen
- Scholar: <https://scholar.google.com/scholar?q=Stephen+Taylor+wildfire>
- Flannigan, Mike D.
- Scholar: <https://scholar.google.com/scholar?q=Mike+D+Flannigan>

**Summary:**  
This review synthesizes machine learning approaches to wildfire prediction, highlighting their ability to capture nonlinear relationships and their limitations in interpretability and extrapolation.

**Example citation:**  
"Machine learning models capture complex nonlinear relationships but lack explicit mechanistic grounding."
