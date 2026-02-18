```mermaid
---
title: SolutionComponent - Configure the Data Folder Cataloguer [7ff8405b-a72d-40dd-8b68-e5e96e2fcf47]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Configure the Data Folder Cataloguer**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Catalog Files in Directory (Folder)**"}
1==>|"configures [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for File System Directory**"}
4==>|"step 2 [Solution Linking Wire]"|1
5@{ shape: tag-rect, label: "*Governance Action Type*
**catalog-data-folder (FileGovernance)**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
```
> Configure the Data Folder Cataloguer: Link the Data Folder asset to the Data Folder cataloguer. (Extracted from 6.0-SNAPSHOT)
