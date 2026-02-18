```mermaid
---
title: Components and Roles for Solution Blueprint - Egeria Content Pack [4d033711-0449-4d67-bf98-c7bfcae86b8c]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Configure the OMAG Server Platform Cataloguer**"}
3@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
4@{ shape: subproc, label: "*Solution Component*
**Delete OMAG Server Platform from Open Metadata**"}
5@{ shape: div-rect, label: "*Solution Component*
**OMAG Server Platform Cataloguer**"}
6@{ shape: subproc, label: "*Solution Component*
**Create OMAG Server Platform in Open Metadata**"}
7@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
8@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
8==>|"requests,
[Solution Component Actor]"|2
2==>|"configures,
[Solution Linking Wire]"|5
5==>|"Catalog Resource,
[Solution Linking Wire]"|3
8==>|"requests,
[Solution Component Actor]"|4
4==>|"metadata,
[Solution Linking Wire]"|7
5==>|"metadata,
[Solution Linking Wire]"|7
8==>|"requests,
[Solution Component Actor]"|6
6==>|"metadata,
[Solution Linking Wire]"|7
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
click 2 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Egeria Content Pack: Solution blueprint containing integration connectors for working with Egeria''s infrastructure. (Extracted from 6.0-SNAPSHOT)
