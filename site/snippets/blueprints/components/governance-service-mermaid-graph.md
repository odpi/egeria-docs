```mermaid
---
title: SolutionComponent - Governance Service [0002857a-0223-46e9-ac26-56109a3d6833]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Governance Service**"}
2@{ shape: rect, label: "*Solution Component*
**Governance Engine**"}
2==>|"Solution Composition"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-service/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/governance-engine/" "Click for more documentation" _blank
```
> Governance Service: Provides the description of a component that implements an automated governance activity. (Extracted from 6.0-SNAPSHOT)
