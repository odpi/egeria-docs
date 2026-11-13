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
2==>|"configures,
[Solution Linking Wire]"|5
5==>|"Catalog Resource,
[Solution Linking Wire]"|3
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
click 2 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Egeria Content Pack: Solution blueprint containing integration connectors for working with Egeria's infrastructure. (Extracted from 6.3-SNAPSHOT)
