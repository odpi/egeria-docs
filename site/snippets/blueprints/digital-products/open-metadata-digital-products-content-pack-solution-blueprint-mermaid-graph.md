```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Products Content Pack [ea509f7a-de1f-4864-bbbd-6f373f49e132]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
3@{ shape: div-rect, label: "*Solution Component*
**Babbage Analytical Engine**"}
4@{ shape: subproc, label: "*Solution Component*
**Create New Product Subscription**"}
5@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
6@{ shape: div-rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
7@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
8@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
2==>|"metadata,
[Solution Linking Wire]"|7
3==>|"metadata,
[Solution Linking Wire]"|7
4==>|"metadata,
[Solution Linking Wire]"|7
5==>|"metadata,
[Solution Linking Wire]"|7
6==>|"metadata,
[Solution Linking Wire]"|7
8==>|"metadata,
[Solution Linking Wire]"|7
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
click 2 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Open Metadata Digital Products Content Pack: Solution blueprint showing the components that manage the Open Metadata Digital Product Catalog. (Extracted from 6.0-SNAPSHOT)
