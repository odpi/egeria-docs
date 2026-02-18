```mermaid
---
title: Solution Component - File System [5c14f90b-ecc5-4ecb-adfe-36208671bc5d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: lin-cyl, label: "*Solution Component*
**File System**"}
subgraph 2 [Subcomponents]
3@{ shape: lin-cyl, label: "*Solution Component*
**File**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**File System Directory**"}
4==>|"Solution Composition"|3
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/types/0/0056-Resource-Managers/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
```
> File System: A system that manages hierarchically organized files on persistent storage. (Extracted from 6.0-SNAPSHOT)
