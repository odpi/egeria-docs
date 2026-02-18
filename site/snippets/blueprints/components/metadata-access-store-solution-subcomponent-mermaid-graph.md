```mermaid
---
title: Solution Component - Metadata Access Store [74385479-73a1-4e61-9c2f-a98be526acc7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
subgraph 2 [Subcomponents]
3@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Repository**"}
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/open-metadata-repository/" "Click for more documentation" _blank
```
> Metadata Access Store: A server that provides access to one or more open metadata repositories. (Extracted from 6.0-SNAPSHOT)
