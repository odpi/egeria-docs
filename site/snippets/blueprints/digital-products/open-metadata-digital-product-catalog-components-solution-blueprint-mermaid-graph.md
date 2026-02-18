```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Product Catalog Components [516950e8-ed42-4288-808c-dcd661b43bf2]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Create New Product Subscription**"}
3@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
5@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
6@{ shape: subproc, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
7@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
8@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
9@{ shape: lin-cyl, label: "*Solution Component*
**Metadata Access Store**"}
10@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
10==>|"Subscribe to product,
[Solution Component Actor]"|2
2==>|"configure subscription,
[Solution Linking Wire]"|8
3==>|"maintain data,
[Solution Linking Wire]"|5
8==>|"initiate when product changes,
[Solution Linking Wire]"|3
10==>|"Shop for data,
[Solution Component Actor]"|4
6==>|"add products to catalog,
[Solution Linking Wire]"|4
11@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
11==>|"Consume data,
[Solution Component Actor]"|5
7==>|"(maybe) remove copy,
[Solution Linking Wire]"|5
12@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
12==>|"Maintains,
[Solution Component Actor]"|6
6==>|"monitor for changes,
[Solution Linking Wire]"|9
6==>|"set up subscription managers,
[Solution Linking Wire]"|8
10==>|"Cancel product subscription,
[Solution Component Actor]"|7
end
style 11 color:#000000, fill:#FFE599, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
> Open Metadata Digital Product Catalog Components: Description of the processing used to create and manage the digital products derived from open metadata. (Extracted from 6.0-SNAPSHOT)
