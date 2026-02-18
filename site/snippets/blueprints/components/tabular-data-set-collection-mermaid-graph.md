```mermaid
---
title: SolutionComponent - Tabular Data Set Collection [1c06aeff-cee7-4d0d-87c5-65876a8a395e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Tabular Data Set Collection**"}
2@{ shape: rect, label: "*Solution Component*
**Tabular Data Set**"}
1==>|"Solution Composition"|2
3@{ shape: rect, label: "*Solution Component*
**Data Asset**"}
2==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
4==>|"works with [Solution Linking Wire]"|2
5@{ shape: rect, label: "*Solution Component*
**Provision Tabular Data Set**"}
5==>|"works with [Solution Linking Wire]"|2
6@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
6==>|"works with [Solution Linking Wire]"|2
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/asset/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Tabular Data Set Collection: A collection of tabular data sets. (Extracted from 6.0-SNAPSHOT)
