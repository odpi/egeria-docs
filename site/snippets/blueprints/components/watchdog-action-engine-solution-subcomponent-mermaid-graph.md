```mermaid
---
title: Solution Component - Watchdog Action Engine [0f6dc658-f299-4066-bd77-1886f7167ec1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**Watchdog Action Engine**"}
subgraph 2 [Subcomponents]
3@{ shape: rect, label: "*Solution Component*
**Watchdog Action Service**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/watchdog-action-engine/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/watchdog-action-service/" "Click for more documentation" _blank
```
> Watchdog Action Engine: A governance engine that runs watchdog action services. (Extracted from 6.0-SNAPSHOT)
