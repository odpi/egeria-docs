```mermaid
---
title: SolutionComponent - Tabular Data Set [5ec9db1a-14e8-4e36-b727-7a3fdfa511ea]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Tabular Data Set**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Core Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Data Asset**"}
1==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Tabular Data Set Collection**"}
4==>|"Solution Composition"|1
5@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
5==>|"works with [Solution Linking Wire]"|1
6@{ shape: rect, label: "*Solution Component*
**Provision Tabular Data Set**"}
6==>|"works with [Solution Linking Wire]"|1
7@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
7==>|"works with [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/asset/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Tabular Data Set: A logical collection of data, either at rest or in motion, organized into a tabular (columnar) format. (Extracted from 6.0-SNAPSHOT)
