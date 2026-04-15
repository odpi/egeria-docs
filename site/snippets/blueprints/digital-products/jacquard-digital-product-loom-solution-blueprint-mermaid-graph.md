```mermaid
---
title: Components and Roles for Solution Blueprint - Jacquard Digital Product Loom [08851db5-cb2e-466b-94c0-3976dc7736a0]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
5@{ shape: lin-cyl, label: "*Solution Component*
**Metadata Access Store**"}
6@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
7@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
7==>|"Maintains,
[Solution Component Actor]"|2
2==>|"maintain catalog entry,
[Solution Linking Wire]"|4
2==>|"add products to catalog,
[Solution Linking Wire]"|3
2==>|"monitor for changes,
[Solution Linking Wire]"|5
2==>|"set up subscription managers,
[Solution Linking Wire]"|6
8@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
8==>|"Shop for data,
[Solution Component Actor]"|3
3==>|"search for type of data,
[Solution Linking Wire]"|4
9@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
9==>|"Develops,
[Solution Component Actor]"|4
4==>|"query metadata,
[Solution Linking Wire]"|5
6==>|"monitor product changes,
[Solution Linking Wire]"|4
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#000000, fill:#FFE599, stroke:#000000
```
> Jacquard Digital Product Loom: Description of the processing used to create and manage the digital products derived from open metadata in the Open Metadata Digital Product Catalog. (Extracted from 6.0-SNAPSHOT)
