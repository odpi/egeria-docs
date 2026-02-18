```mermaid
---
title: Solution Component - Governance Action Engine [913f0e12-67e0-4b07-b085-a3aac1748f07]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**Governance Action Engine**"}
subgraph 2 [Subcomponents]
3@{ shape: rect, label: "*Solution Component*
**Governance Action Service**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-engine/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/governance-action-service/" "Click for more documentation" _blank
```
> Governance Action Engine: A governance engine that runs governance action services. (Extracted from 6.0-SNAPSHOT)
