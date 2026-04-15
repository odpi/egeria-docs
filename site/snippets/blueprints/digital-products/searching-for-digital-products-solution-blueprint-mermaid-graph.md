```mermaid
---
title: Components and Roles for Solution Blueprint - Searching for Digital Products [6bfa0952-a5db-4707-ae96-b1f3cfe8b817]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
4@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
4==>|"Shop for data,
[Solution Component Actor]"|2
2==>|"search for type of data,
[Solution Linking Wire]"|3
5@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
5==>|"Develops,
[Solution Component Actor]"|3
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
```
> Searching for Digital Products: Description of the processing when a potential consumer is searching the Open Metadata Digital Product Catalog for the right data for their project. (Extracted from 6.0-SNAPSHOT)
