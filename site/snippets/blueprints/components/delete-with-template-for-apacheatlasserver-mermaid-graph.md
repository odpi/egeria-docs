```mermaid
---
title: SolutionComponent - Delete with Template Governance Action Process for Apache Atlas Server [f0494380-3170-4198-b4d8-2dc6b665fb54]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Delete with Template Governance Action Process for Apache Atlas Server**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Apache Atlas Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
3==>|"delete Apache Atlas Server [Solution Component Actor]"|1
4@{ shape: rect, label: "*Solution Component*
**Delete Apache Atlas Server from Open Metadata**"}
1==>|"step 1 [Solution Linking Wire]"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/egeria-solutions/leveraging-apache-atlas/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Delete with Template Governance Action Process for Apache Atlas Server: Delete the asset for Apache Atlas Server using the same template properties that were used to create it.  This will delete all of the metadata anchored to the asset and relationships to other entities such as the catalog target relationships. (Extracted from 6.0-SNAPSHOT)
