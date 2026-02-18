```mermaid
---
title: Solution Component - Engine Host [ca709899-e15f-4552-a681-355f691fded4]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**Engine Host**"}
subgraph 2 [Subcomponents]
3@{ shape: rect, label: "*Solution Component*
**Governance Engine**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/engine-host/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/governance-engine/" "Click for more documentation" _blank
```
> Engine Host: A server that runs governance engines. (Extracted from 6.0-SNAPSHOT)
