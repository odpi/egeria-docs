```mermaid
---
title: SolutionComponent - Delete an OSS Unity Catalog Server from Open Metadata [835b4fe4-03cf-4f4d-b0b5-e25d7dfe3299]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Delete an OSS Unity Catalog Server from Open Metadata**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Unity Catalog Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Delete with Template Governance Action Process for Databricks Unity Catalog Server**"}
3==>|"step 1 [Solution Linking Wire]"|1
4@{ shape: rect, label: "*Solution Component*
**Delete with Template Governance Action Process for Unity Catalog Server**"}
4==>|"step 1 [Solution Linking Wire]"|1
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|5
6@{ shape: tag-rect, label: "*Governance Action Type*
**delete-unity-catalog-server (UnityCatalogGovernance)**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Delete an OSS Unity Catalog Server from Open Metadata: Delete asset from the metadata repository. (Extracted from 6.0-SNAPSHOT)
