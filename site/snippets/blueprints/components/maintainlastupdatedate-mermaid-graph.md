```mermaid
---
title: SolutionComponent - Maintain DataFolder''s storeUpdateTime [871aa27d-a74b-48f5-9c29-ddbcd09c94c7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Maintain DataFolder''s storeUpdateTime**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Data Folder**"}
1==>|"Catalog Resource [Solution Linking Wire]"|4
5@{ shape: stadium, label: "*Integration Connector*
**MaintainDataFolderLastUpdateDateIntegrationConnector**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
```
> Maintain DataFolder''s storeUpdateTime: Monitors changes to the files in the directory associated with a DataFolder and maintains the storeUpdateTime attribute in the DataFolder with the data/time that ome of the files was created/changed. (Extracted from 6.0-SNAPSHOT)
