```mermaid
---
title: Components and Roles for Solution Blueprint - Jacquard Digital Product Loom [bfa05ac2-02eb-48db-9066-de2d335ac562]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
3@{ shape: subproc, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
4@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
5@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
6@{ shape: lin-cyl, label: "*Solution Component*
**Metadata Access Store**"}
7@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
7==>|"Develops,
[Solution Component Actor]"|2
2==>|"query metadata,
[Solution Linking Wire]"|6
4==>|"monitor product changes,
[Solution Linking Wire]"|2
3==>|"maintain catalog entry,
[Solution Linking Wire]"|2
5==>|"search for type of data,
[Solution Linking Wire]"|2
8@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
8==>|"Maintains,
[Solution Component Actor]"|3
3==>|"add products to catalog,
[Solution Linking Wire]"|5
3==>|"monitor for changes,
[Solution Linking Wire]"|6
3==>|"set up subscription managers,
[Solution Linking Wire]"|4
9@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
9==>|"Shop for data,
[Solution Component Actor]"|5
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#000000, fill:#FFE599, stroke:#000000
```
> Jacquard Digital Product Loom: Description of the processing used to create and manage the digital products derived from open metadata in the Open Metadata Digital Product Catalog. (Extracted from 6.0-SNAPSHOT)
