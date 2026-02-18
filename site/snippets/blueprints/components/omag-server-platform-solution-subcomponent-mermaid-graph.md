```mermaid
---
title: Solution Component - OMAG Server Platform [1442a1bc-f791-4fda-a3be-56fb68934a4c]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
subgraph 2 [Subcomponents]
3@{ shape: rect, label: "*Solution Component*
**Integration Daemon**"}
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
5@{ shape: rect, label: "*Solution Component*
**Engine Host**"}
6@{ shape: rect, label: "*Solution Component*
**View Server**"}
3==>|"access metadata,
[Solution Linking Wire]"|4
5==>|"access metadata,
[Solution Linking Wire]"|4
6==>|"access metadata,
[Solution Linking Wire]"|4
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-daemon/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/engine-host/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/metadata-access-server/" "Click for more documentation" _blank
```
> OMAG Server Platform: An Open Metadata and Governance (OMAG) runtime for running one to many OMAG Servers. (Extracted from 6.0-SNAPSHOT)
