```mermaid
---
title: SolutionComponent - File System [5c14f90b-ecc5-4ecb-adfe-36208671bc5d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**File System**"}
2@{ shape: rect, label: "*Solution Component*
**File**"}
1==>|"Solution Composition"|2
3@{ shape: rect, label: "*Solution Component*
**Data Folder**"}
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
1==>|"Solution Composition"|4
8@{ shape: rect, label: "*Solution Component*
**Move File**"}
8==>|"works with [Solution Linking Wire]"|4
9@{ shape: rect, label: "*Solution Component*
**Survey File System Directory**"}
9==>|"works with [Solution Linking Wire]"|4
10@{ shape: rect, label: "*Solution Component*
**Survey Nested Files System Directories (Folders) and Files**"}
10==>|"works with [Solution Linking Wire]"|4
11@{ shape: rect, label: "*Solution Component*
**Copy File**"}
11==>|"works with [Solution Linking Wire]"|4
12@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 6 Items**"}
12-.->4
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
click 11 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 1 "https://egeria-project.org/types/0/0056-Resource-Managers/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> File System: A system that manages hierarchically organized files on persistent storage. (Extracted from 6.0-SNAPSHOT)
