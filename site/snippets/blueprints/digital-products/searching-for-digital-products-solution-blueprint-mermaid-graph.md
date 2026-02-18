```mermaid
---
title: Components and Roles for Solution Blueprint - Searching for Digital Products [b93a2f90-5b14-4736-bcc8-b54efb029fa9]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
4@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
4==>|"Develops,
[Solution Component Actor]"|2
3==>|"search for type of data,
[Solution Linking Wire]"|2
5@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
5==>|"Shop for data,
[Solution Component Actor]"|3
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
```
> Searching for Digital Products: Description of the processing when a potential consumer is searching the Open Metadata Digital Product Catalog for the right data for their project. (Extracted from 6.0-SNAPSHOT)
