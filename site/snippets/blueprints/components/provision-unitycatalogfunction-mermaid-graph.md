```mermaid
---
title: SolutionComponent - Provision Governance Action Process for UnityCatalogFunction [3d720673-7241-461b-b6f7-2c2b7f6ce99d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogFunction**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Unity Catalog Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
3==>|"provision asset [Solution Component Actor]"|1
4@{ shape: rect, label: "*Solution Component*
**Provision Unity Catalog Resource**"}
1==>|"step 1 [Solution Linking Wire]"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Provision Governance Action Process for UnityCatalogFunction: Create a DeployedImplementationType{Unity Catalog Function} element in the correct metadata collection so that it is provisioned into unity catalog. (Extracted from 6.0-SNAPSHOT)
