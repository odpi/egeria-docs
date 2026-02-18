```mermaid
---
title: SolutionComponent - Cancel Product Subscription [e2005ecc-f5a6-4643-b979-a08a13f0984b]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Cancel Product Subscription**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Products Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Tabular Data Set**"}
1==>|"works with [Solution Linking Wire]"|4
5@{ shape: tag-rect, label: "*Governance Action Type*
**cancel-digital-subscription (EgeriaGovernance)**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
```
> Cancel Product Subscription: The process of cancelling an existing consumer''s subscription to a digital product. (Extracted from 6.0-SNAPSHOT)
