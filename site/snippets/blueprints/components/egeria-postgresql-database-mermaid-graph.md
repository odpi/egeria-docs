```mermaid
---
title: SolutionComponent - Egeria PostgreSQL Database [ac2df71c-6041-42b9-b96b-ae036a32f5d8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Egeria PostgreSQL Database**"}
2@{ shape: rect, label: "*Solution Component*
**Open Metadata Repository**"}
1==>|"Solution Composition"|2
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
3==>|"Solution Composition"|2
4@{ shape: rect, label: "*Solution Component*
**Load Archive**"}
4==>|"load [Solution Linking Wire]"|2
3==>|"stores data [Solution Linking Wire]"|2
5@{ shape: rect, label: "*Solution Component*
**Egeria Workspaces PostgreSQL Server**"}
5==>|"Solution Composition"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
click 2 "https://egeria-project.org/concepts/open-metadata-repository/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/open-metadata-archive/" "Click for more documentation" _blank
click 5 "https://www.postgresql.org/" "Click for more documentation" _blank
```
> Egeria PostgreSQL Database: This database supports the different repositories used by the Egeria runtime. (Extracted from 6.0-SNAPSHOT)
