```mermaid
---
title: Solution Component - Dr.Egeria [1ddd9283-3dc9-4220-ac42-be0894b5a930]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**Dr.Egeria**"}
subgraph 2 [Subcomponents]
3@{ shape: rect, label: "*Solution Component*
**pyegeria**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 3 "https://egeria-project.org/concepts/pyegeria/" "Click for more documentation" _blank
```
> Dr.Egeria: A markdown processor that can maintain and retrieve open metadata by processing and creating markdown documents. (Extracted from 6.0-SNAPSHOT)
