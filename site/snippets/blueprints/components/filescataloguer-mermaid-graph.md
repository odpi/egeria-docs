```mermaid
---
title: SolutionComponent - Catalog Files in Directory (Folder) [aa8914ac-b557-4595-b248-e1f252b77cf2]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Catalog Files in Directory (Folder)**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
1==>|"Catalog Resource [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Configure the File Folder Cataloguer**"}
5==>|"configures [Solution Linking Wire]"|1
6@{ shape: rect, label: "*Solution Component*
**Configure the Data Folder Cataloguer**"}
6==>|"configures [Solution Linking Wire]"|1
7@{ shape: stadium, label: "*Integration Connector*
**GeneralFilesMonitorIntegrationConnector**"}
1==>|"Implemented By"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Catalog Files in Directory (Folder): Create an open metadata representation of the files in the directories linked to this connector through the CatalogTarget relationship. (Extracted from 6.0-SNAPSHOT)
