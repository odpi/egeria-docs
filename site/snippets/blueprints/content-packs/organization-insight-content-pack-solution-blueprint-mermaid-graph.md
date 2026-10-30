```mermaid
---
title: Components and Roles for Solution Blueprint - Organization Insight Content Pack [b36c6cc7-26f2-4b9b-b3e3-496f738c8927]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: div-rect, label: "*Solution Component*
**Babbage Analytical Engine**"}
3@{ shape: subproc, label: "*Solution Component*
**Build Zone Membership Profile**"}
2==>|"schedules,
[Solution Linking Wire]"|3
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
click 2 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Organization Insight Content Pack: Solution blueprint describing the components that deliver organization insight to the open metadata ecosystem. (Extracted from 6.3-SNAPSHOT)
