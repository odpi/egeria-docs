```mermaid
---
title: Solution Component - Tabular Data Set [5ec9db1a-14e8-4e36-b727-7a3fdfa511ea]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: lin-cyl, label: "*Solution Component*
**Tabular Data Set**"}
subgraph 2 [Subcomponents]
3@{ shape: lin-cyl, label: "*Solution Component*
**Data Asset**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/asset/" "Click for more documentation" _blank
```
> Tabular Data Set: A logical collection of data, either at rest or in motion, organized into a tabular (columnar) format. (Extracted from 6.0-SNAPSHOT)
