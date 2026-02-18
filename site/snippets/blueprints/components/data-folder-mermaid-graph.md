```mermaid
---
title: SolutionComponent - Data Folder [db92678c-a734-4dbb-b7dd-aeaa0905462d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Data Folder**"}
2@{ shape: rect, label: "*Solution Component*
**File**"}
1==>|"Solution Composition"|2
3@{ shape: rect, label: "*Solution Component*
**File System**"}
3==>|"Solution Composition"|2
4@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
4==>|"Solution Composition"|2
5@{ shape: rect, label: "*Solution Component*
**Delete File**"}
5==>|"works with [Solution Linking Wire]"|2
6@{ shape: rect, label: "*Solution Component*
**Print Survey Report**"}
6==>|"works with [Solution Linking Wire]"|2
7@{ shape: rect, label: "*Solution Component*
**Survey Data File**"}
7==>|"works with [Solution Linking Wire]"|2
8@{ shape: rect, label: "*Solution Component*
**Maintain DataFolder''s storeUpdateTime**"}
8==>|"Catalog Resource [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/0/0056-Resource-Managers/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
```
> Data Folder: A directory (folder) that holds files representing a single data source. (Extracted from 6.0-SNAPSHOT)
