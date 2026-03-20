# A Causal History of Wildfire Modeling

## Status

This file is a background and contextualization note for proposal development. It is meant to sit alongside the broader program and framing materials in the repository and to help explain how wildfire modeling evolved in response to specific scientific, operational, and technological constraints.

## Pre-1970 root: practice, indices, and the limits of intuition

Before formal models, wildfire knowledge was operational and experiential. Crews relied on pattern recognition: wind, slope, fuels, and time of day. Early systems such as drought and danger indices classified conditions rather than simulated fire. They answered "how dangerous is today?" but not "where will the fire be tomorrow?" This mirrors pre-computational phases in other fields where knowledge was descriptive and local.

The scaling of fire management, with more land and more assets at risk, created pressure for portability and prediction. At the same time, firefighting technology was evolving: lookout towers, telephones, road networks, and organized crews after the Great Fire of 1910. Detection and coordination improved, but decision making still depended on human intuition. The gap between what crews could do and what they could anticipate widened. That gap is what Rothermel ultimately closes.

Wildfire modeling did not appear fully formed. It emerged through a chain of needs, constraints, borrowed ideas, and occasional moments of genuine innovation. To understand where the field is now, and why it still lacks a unifying theory, it helps to trace not just what happened, but why each step happened and what each step made possible next.

## Before models: fire as practice, not theory

In the early 20th century, wildfire knowledge lived almost entirely in the heads of practitioners. Firefighters, foresters, and land managers learned to read landscapes: dry fuels, wind shifts, slope, and weather patterns. Early fire-danger systems began to formalize some of this intuition, translating weather and fuel moisture into indices of risk. But these were not generative models. They did not attempt to simulate fire. They classified conditions.

This limitation created a bottleneck. As fire management scaled up, especially in the United States and Canada, agencies needed something more than experience. They needed a way to predict how fire would behave under new conditions. The problem was no longer just understanding fire, but making it portable, generalizable, and computable.

That pressure set the stage for the first true model.

## The first breakthrough: making fire computable

Rothermel's 1972 model did not emerge in isolation. It was built on a growing body of combustion physics, heat transfer theory, and experimental burns conducted by the U.S. Forest Service. Researchers were already measuring flame length, heat release, and fuel consumption. At the same time, engineering and physics had matured a style of modeling that reduced complex systems into energy balances and transport equations.

Rothermel's key move was to translate fire into that language. He took the messy reality of fire and expressed it as a function of a few measurable variables: fuel properties, wind, and slope. In doing so, he made fire behavior something that could be calculated with a slide rule, and later, a computer.

This innovation solved a critical problem: it allowed agencies to move from intuition to prediction. But it also introduced a constraint that would persist for decades. By framing fire as a local energy balance, the model implicitly assumed that fire behavior could be understood point by point. The larger structure of the fire, its perimeter and shape, was not part of the model. It was something that would emerge when many local calculations were combined.

That assumption would shape everything that followed.

## Consolidation: turning a model into a system

Once Rothermel made fire computable, the next challenge was usability. A model is only useful if people can apply it consistently across landscapes. This led to a series of developments that transformed a single equation into an operational system.

Albini extended the framework to include additional aspects of fire behavior, such as intensity and spotting. These extensions were not independent breakthroughs; they were responses to the realization that managers needed more than spread rate. They needed a fuller description of fire behavior, but still within the same computational framework.

At the same time, Anderson and later Scott and Burgan worked on fuel classification systems. Their problem was practical: how do you take the continuous variation of real vegetation and map it into something a model can use? Their solution was to define discrete fuel models, each representing a characteristic combination of fuel properties.

This step made large-scale modeling possible. It allowed different users to apply the same model in different places. But it also introduced a second major abstraction: continuous ecological structure was reduced to categories.

By the 1980s, wildfire modeling had become a coherent system: local spread equations, modular behavior components, and standardized fuel inputs. It worked. But it worked by simplifying the world into pieces that could be computed independently.

Meanwhile, outside of fire science, something very different was happening.

## The missed revolution: geometry and scaling

In the 1970s and 1980s, mathematicians and physicists began to realize that many natural systems could not be understood by looking only at local processes. Mandelbrot introduced fractal geometry, showing that coastlines, clouds, and other boundaries exhibit structure across scales. Percolation theory and statistical physics explored how connectivity and phase transitions emerge in complex systems.

These ideas were directly relevant to wildfire. Fire spreads across heterogeneous landscapes, forming complex, branching boundaries. It is, in many ways, a textbook example of a system where geometry matters.

But wildfire modeling did not immediately adopt this perspective. The field remained focused on improving local predictions and operational tools. Geometry was visible in maps and observations, but it was not yet a target of theory.

This gap would persist until the next major transition.

## A global and cross-cultural perspective: parallel lineages of fire knowledge

While the North American narrative emphasizes suppression, computation, and operational modeling, fire has always been understood differently across regions of the world. These parallel histories developed under distinct ecological, cultural, and logistical constraints, producing different priorities and, implicitly, different models of fire.

Long before formal modeling, Indigenous fire stewardship systems across Australia, the Americas, and Africa used intentional burning to shape landscapes. These practices were not ad hoc; they were governed by deeply embedded ecological knowledge systems that integrated seasonality, vegetation response, animal behavior, and cultural objectives. In many regions, burning followed precise temporal windows, often tied to phenology, humidity conditions, and wind regimes, to produce low-intensity, patchy fires.

In Australia, Aboriginal cultural burning created fine-scale mosaics that limited fuel continuity and prevented large, high-intensity fires. In California and the western United States, many Indigenous groups used frequent burning to maintain open understories, enhance food resources such as acorns and game habitat, and reduce fuel buildup. In African savannas, early dry-season burning has long been used to regulate grazing systems and prevent late-season extreme fires. Across these systems, fire was applied repeatedly and intentionally to maintain landscape structure over time.

These practices created patch mosaics, controlled connectivity, and reduced the likelihood of large, uncontrollable fires. Critically, they operated on an implicit understanding of thresholds: when fuels become continuous, when conditions allow spread, and how fire can be used to break that continuity. Knowledge was encoded in timing, spacing, and pattern rather than equations, but it was nonetheless predictive and adaptive.

In effect, these systems managed fire as a spatially structured process, where geometry and connectivity were central. They did not model fire as a point-based spread phenomenon, but as a landscape-scale pattern that could be shaped and maintained. This represents an alternative root of fire knowledge: not reductionist, but integrative and pattern-based.

From a modern perspective, Indigenous burning systems can be interpreted as managing percolation and connectivity in fuel networks, maintaining the system below thresholds where large-scale propagation becomes likely. While this language is contemporary, the practice itself reflects a long-standing empirical understanding of cross-scale fire behavior.

Importantly, these systems also demonstrate something largely absent from modern modeling: feedback between fire outcomes and future landscape structure. Burning was not a one-time intervention, but part of a continuous process of landscape regulation.

The disruption of Indigenous burning practices through colonization and suppression policies led to increased fuel accumulation, altered ecosystem structure, and, in many regions, the conditions that now support extreme wildfire behavior. In this sense, the modern wildfire problem is not only a failure of prediction, but also a consequence of removing a long-standing system of structural control.

This perspective reframes the history of fire modeling. Importantly, these Indigenous practices can be understood as managing connectivity and thresholds across landscapes; this is a modern interpretation rather than a claim about historical terminology. Rather than beginning with Rothermel, we can recognize two parallel origins: one in formal, reductionist modeling, and one in Indigenous, pattern-based landscape management. The former enabled computation and prediction; the latter managed structure and connectivity. The absence of a framework that unites these perspectives remains a central gap in wildfire science.

In Europe, where landscapes had been intensively managed for centuries, wildfire was less dominant as a large-scale ecological force outside Mediterranean systems. As a result, fire science emphasized prevention, meteorology, and fuel moisture. Early work focused on fire danger rating and environmental drivers rather than spread dynamics. This aligns with broader European strengths in atmospheric science and statistical modeling.

Canada developed a parallel but distinct operational lineage. With vast remote forests and limited access, Canadian systems emphasized standardized prediction frameworks that integrate fuels, weather, and behavior. The Canadian Fire Behavior Prediction system represents one of the most coherent national approaches, linking fire danger and fire behavior more tightly than many U.S. systems.

Australia, facing some of the most extreme fire conditions on Earth, contributed heavily to understanding nonlinear fire behavior. Frequent blowup events, long-range spotting, and intense wind-driven fires forced researchers to confront thresholds and rapid transitions. This pushed Australian fire science closer to nonlinear dynamics and extreme event theory earlier than in many other regions.

In boreal regions such as Russia, the scale of fire exceeds the capacity for suppression. Modeling efforts therefore focused less on individual fires and more on large-scale fire regimes, climate interactions, and carbon cycling. This connects wildfire science directly to Earth system science and global change research.

In tropical regions, including the Amazon and Southeast Asia, fire is often driven by human land use. Modeling emphasizes ignition patterns, deforestation dynamics, and remote sensing. Here, fire becomes a signal of socio-environmental processes rather than purely a physical phenomenon.

Taken together, these global perspectives reveal that wildfire science did not evolve as a single unified field. Instead, it diversified into regionally optimized frameworks, each capturing a different aspect of fire: suppression, spread, risk, extreme behavior, ecological dynamics, or human drivers.

The consequence is fragmentation. Each lineage is internally coherent but incomplete. No single framework integrates fire as a system that spans local processes, spatial structure, and cross-scale dynamics.

## The spatial turn: from points to perimeters

By the 1990s, computational power had increased enough to simulate fire across entire landscapes. Researchers began to ask a new question: instead of predicting spread at a point, can we simulate the growth of a fire over space and time?

FARSITE answered that question. It took the local spread equations developed in earlier decades and used them to propagate a fire perimeter across a landscape. Conceptually, it borrowed from wavefront propagation methods in physics and computational geometry. Each point on the fireline advanced according to local conditions, and the combined result was an evolving boundary.

This was a major breakthrough. It transformed fire from a scalar quantity into a spatial object. Managers could now see where a fire might go, not just how fast it might move.

But the underlying logic had not changed. The perimeter was still an emergent result of local rules. The model did not ask whether the shape of the fire obeyed any deeper constraints. It simply generated whatever shape resulted from the inputs.

At the same time, researchers in other fields were using similar computational tools to study pattern formation, often with the explicit goal of identifying universal properties. Fire modeling adopted the tools, but not the deeper questions.

## Borrowing from algorithms: fire as optimization

As spatial models became more complex, computational efficiency became a limiting factor. Simulating fire spread across large landscapes required new algorithms. This led to the adoption of ideas from graph theory and optimization, particularly minimum-travel-time methods.

These methods reframed fire spread as a problem of finding the fastest path across a network of cells, each with its own resistance to spread. This was a natural fit with advances in computer science, where shortest-path algorithms had already been developed for transportation and communication networks.

This shift made large-scale simulations feasible. It allowed models to run faster and handle more complex landscapes. But it did not change the conceptual foundation. Fire was still modeled as a process of local propagation, now embedded in a more efficient computational framework.

## The risk revolution: from one fire to many

As models became capable of simulating individual fires, the next question emerged: what if we simulate many fires? This question was driven by management needs. Agencies were less interested in predicting a single fire than in understanding the range of possible outcomes across a region.

This led to probabilistic and ensemble modeling approaches. Systems like FSim ran thousands of simulations under varying conditions to estimate burn probability and risk. This approach borrowed heavily from climate science and meteorology, where ensemble forecasting had already become standard.

The result was a new way of thinking about fire: not as a single event, but as a distribution of possible events. This was a powerful shift, enabling risk-based decision making at large scales.

But it came with a tradeoff. By focusing on aggregates, these models moved further away from the detailed structure of individual fires. Geometry became something to average over, rather than something to understand.

## Physics strikes back: coupling fire and atmosphere

While empirical and probabilistic models were advancing, another group of researchers was dissatisfied with their limitations. They turned to physics-based modeling, aiming to simulate fire as a coupled system of combustion, heat transfer, and fluid dynamics.

This work drew heavily on advances in computational fluid dynamics and atmospheric modeling. Early coupled models, such as those by Clark and colleagues, integrated fire behavior with atmospheric processes. Later systems like WRF-Fire built on existing weather models, adding fire as an interacting component.

These models represented a different philosophy. Instead of simplifying fire to make it computable, they attempted to simulate its underlying mechanisms in detail. This allowed them to capture phenomena such as plume-driven spread and fire-weather feedbacks.

However, these gains came at a cost. The models were computationally expensive, difficult to parameterize, and challenging to validate. And like the other lineages, they did not treat the geometry of fire as a primary constraint.

## Parallel insights: complexity and scaling

Around the same time, researchers began to apply ideas from complexity science to wildfire. Cellular automata models showed how complex fire patterns could emerge from simple rules. Malamud and others demonstrated that fire regimes exhibit statistical properties consistent with self-organized criticality.

These insights suggested that fire might obey scaling laws similar to those found in other complex systems. But unlike in fields such as turbulence or network theory, these ideas did not become central to model construction. They remained largely interpretive, offering explanations for observed patterns rather than constraints for predictive models.

## A brief reversal: fire influences other fields

While wildfire modeling has mostly borrowed from other disciplines, there are moments where it has contributed back. Fire has served as a real-world example of spreading processes, informing studies in percolation theory, epidemiology, and network dynamics. The statistical analysis of fire sizes and frequencies has been used as evidence for self-organized criticality, influencing research in statistical physics.

These contributions are important, but they are indirect. Fire provides data and examples, rather than a unifying theoretical framework that other fields adopt.

## The data era: machine learning arrives

In the past decade, machine learning has transformed wildfire modeling, as it has many other fields. Large datasets, satellite observations, and increased computational power have enabled models that can learn complex relationships directly from data.

These models are powerful predictors. They can identify patterns that are difficult to capture with traditional approaches. But they also inherit a familiar limitation: they do not impose structural constraints. They learn what is in the data, but they do not explain why those patterns exist.

## Co-evolution with firefighting technology: a feedback loop

The evolution of wildfire modeling is inseparable from the evolution of firefighting technology. The two progressed in a repeating loop:

1. New technology expands operational reach: engines, aircraft, radios, GIS, satellites, sensors.
2. Expanded reach increases uncertainty: fires move faster and decisions scale up.
3. Modeling emerges to manage that uncertainty: Rothermel, FARSITE, MTT, FSim, WRF-Fire, and machine learning systems.
4. Models enable more strategic use of technology: pre-positioning, line placement, evacuations, and fuels planning.

Early hand-crew eras limited action to where people could physically reach. As engines, bulldozers, and aircraft arrived mid-century, suppression could outpace intuition, creating demand for computable spread models. Rothermel-type equations became decision tools tied directly to safety and tactics. With GIS and GPS in the 1990s, spatial growth models like FARSITE became feasible and transformed firefighting into a spatial planning problem. Minimum-travel-time algorithms imported from computer science enabled landscape-scale optimization.

In the 2000s, remote sensing and large datasets enabled probabilistic risk systems such as FSim, shifting questions from single-fire prediction to distributions of outcomes for policy and planning. In parallel, advances in computational fluid dynamics and atmospheric modeling enabled coupled fire-weather systems such as WRF-Fire, increasing mechanistic realism but also computational burden. Today, drones, real-time satellites, and AI move the field toward streaming data assimilation and adaptive decision systems.

Across this co-evolution, both technology and models increased scale, speed, and realism, but neither imposed cross-scale structural constraints on fire. Geometry remained an output, not a target.

## Where this leaves the field

Looking back, each stage of wildfire modeling can be understood as a response to a specific limitation of the previous stage:

- Empirical knowledge lacked generality, so Rothermel made fire computable.
- Local models lacked spatial context, so FARSITE made fire spatial.
- Deterministic models lacked uncertainty, so FSim made fire probabilistic.
- Empirical models lacked realism, so physics-based models added coupling.
- Mechanistic models lacked flexibility, so machine learning added prediction.

Each step solved a problem. Each step enabled the next.

But none of these steps addressed a deeper question that other fields eventually confronted: are there constraints that govern the structure of the system across scales?

That question remains largely open in wildfire modeling.

## Additional context to strengthen historical accuracy

### Early systems and key figures

Early U.S. fire-danger rating efforts evolved into the National Fire Danger Rating System, formalized in the 1970s, building on prior indices and meteorological observations. Foundational work by researchers such as Harry T. Gisborne and later C. E. Van Wagner and James G. Byram helped formalize concepts like fire intensity, including Byram's fireline intensity in 1959, explicitly distinguishing between fire danger and fire behavior.

### Fuels and experimental fire science

Extensive empirical fuels research provided the quantitative foundation upon which all operational fire models depend. Parallel to modeling, extensive empirical research programs measured fuel loads, fuel moisture, and combustion characteristics through field plots and experimental burns conducted by the U.S. Forest Service and Canadian agencies. These datasets were essential for parameterizing Rothermel-type models and fuel classifications. This fuels science effort represents a major empirical backbone of the field rather than a minor supporting component.

### Fire ecology and the shift from suppression to use

Suppression initially succeeded operationally by increasing detection and rapid response, but over decades it altered fuel structure and continuity, which in turn shifted fire regimes and created new modeling needs.

The role of fire in ecosystems was not always understood as beneficial. Following the Great Fire of 1910, U.S. federal policy strongly emphasized total suppression, culminating in the 10 a.m. policy of the U.S. Forest Service, which aimed to control all fires by 10 a.m. the day after detection. This doctrine was supported by expanding firefighting infrastructure, including lookout networks, road systems, and rapid-response crews. Fire was framed primarily as a destructive force to be eliminated, and modeling efforts during this period focused on supporting suppression logistics rather than understanding ecological function.

By the mid-20th century, ecologists and foresters began to observe that strict suppression was producing unintended consequences. Forests in many regions, particularly in the western United States, were becoming denser, with increased fuel accumulation and altered species composition. Researchers such as Harold Biswell and others demonstrated through field experiments that frequent, low-intensity fires played a critical role in maintaining ecosystem structure, especially in fire-adapted systems like ponderosa pine forests.

These insights led to a gradual but significant shift in policy and practice beginning in the 1960s and 1970s. Prescribed burning, intentionally setting controlled fires under specific conditions, emerged as a tool for fuel reduction and ecological restoration. Later, let-burn or managed-wildfire policies allowed naturally ignited fires to burn under monitored conditions when risks were acceptable. This represented a fundamental change: fire was no longer only an adversary, but also a process to be managed and, in some cases, encouraged.

This transition had direct implications for modeling. Instead of focusing solely on short-term suppression outcomes, models now needed to account for long-term effects of repeated burning, fuel dynamics, and vegetation change. This shift contributed to the development of landscape-scale models such as LANDIS and LANDIS-II, which simulate interactions among fire, succession, and climate over decades to centuries. It also increased demand for models that could evaluate tradeoffs among suppression, prescribed fire, and ecological outcomes.

Despite these advances, tension remains between suppression-driven and ecology-driven approaches. Operational firefighting still prioritizes immediate control and risk reduction, while ecological management emphasizes long-term resilience and fuel treatment. This duality continues to shape both modeling priorities and technological development, reinforcing the fragmentation of the field into distinct but overlapping lineages.

### Physics-based modeling nuance

Physics-based wildfire modeling builds on both atmospheric science and combustion science. While coupled models derived from atmospheric frameworks advanced fire-weather interaction, combustion modeling and fire engineering, including heat transfer and flame dynamics, were already mature disciplines that informed wildfire applications. These models face persistent challenges in scale coupling, parameterization, and validation due to the multiscale and heterogeneous nature of wildfire systems.

### Why fire modeling adopted paradigms differently

Unlike laboratory sciences such as turbulence or materials science, wildfire operates across heterogeneous landscapes with limited experimental control, sparse observations, and strong stochastic forcing. These constraints historically favored empirical and operational approaches over the search for universal laws, helping explain why scaling and structural constraints have been less central in fire modeling despite their success in other fields.

### Clarifying the structural gap

Across model classes, fire perimeter geometry is typically generated but not treated as a primary validation target. Models are evaluated based on spread rate, burned area, or risk metrics rather than whether they reproduce consistent multiscale structure. This distinction is central: geometry is an output, not a constraint.

## The next step: from simulation to constraint

This proposal builds on pattern-based understandings of fire, including Indigenous landscape burning, by formalizing structural constraints that govern fire across scales.

## Final synthesis: from pattern to principle

Across the history traced here, two complementary strands recur. One strand makes fire computable: reductionist models, spatial simulators, probabilistic ensembles, and coupled physics that improve prediction and decision support. The other strand manages fire as pattern and connectivity: Indigenous mosaic burning, ecological insights about fuel structure, and observations of scaling and criticality in fire regimes.

What is missing is a bridge that turns pattern into principle.

A useful way to see that bridge is through connectivity and thresholds. When fuels form a connected network, fire can propagate across scales; when connectivity is broken into mosaics, propagation is constrained. In statistical physics, this is described by percolation; in ecology, by fuel continuity; in practice, by the deliberate creation of patchy landscapes. These are different languages for the same underlying idea: structure controls spread.

The proposal advances this by asking whether fire systems exhibit predictable scaling relationships that link local spread processes to emergent perimeter geometry and landscape-scale outcomes. If such relationships exist, they can serve as constraints: not just generating fire shapes, but limiting which shapes and growth patterns are possible under given conditions.

This reframes modeling. Instead of validating only rates of spread or burned area, models can be evaluated against multiscale structure, for example whether simulated perimeters reproduce consistent geometric properties across resolutions and conditions. In this view, geometry is not an incidental output; it is a testable signature of the underlying dynamics.

By integrating empirical fuels science, advances in computation and physics, and long-standing pattern-based fire stewardship, the goal is to move wildfire science from a collection of specialized models toward a constrained, cross-scale framework. Such a framework would not replace existing tools; it would organize them, providing a common set of expectations about how fire should behave across scales.

If earlier innovations made fire computable, spatial, probabilistic, and physically realistic, the next step is to make it structurally constrained and therefore comparable, testable, and ultimately more predictable in the ways that matter for both science and management.
