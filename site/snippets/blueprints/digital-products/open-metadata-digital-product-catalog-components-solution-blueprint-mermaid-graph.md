```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Product Catalog Components [60f86dc1-f4c1-4f70-a22f-6cfcf3dea5ed]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
3@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
4@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
5@{ shape: subproc, label: "*Solution Component*
**Create New Product Subscription**"}
6@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
7@{ shape: subproc, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
8@{ shape: lin-cyl, label: "*Solution Component*
**Metadata Access Store**"}
9@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
10@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
10==>|"Consume data,
[Solution Component Actor]"|2
4==>|"maintain data,
[Solution Linking Wire]"|2
3==>|"(maybe) remove copy,
[Solution Linking Wire]"|2
11@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
11==>|"Cancel product subscription,
[Solution Component Actor]"|3
6==>|"initiate when product changes,
[Solution Linking Wire]"|4
11==>|"Subscribe to product,
[Solution Component Actor]"|5
5==>|"configure subscription,
[Solution Linking Wire]"|6
7==>|"set up subscription managers,
[Solution Linking Wire]"|6
12@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
12==>|"Maintains,
[Solution Component Actor]"|7
7==>|"add products to catalog,
[Solution Linking Wire]"|9
7==>|"monitor for changes,
[Solution Linking Wire]"|8
11==>|"Shop for data,
[Solution Component Actor]"|9
end
style 11 color:#000000, fill:#FFE599, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
> Open Metadata Digital Product Catalog Components: Description of the processing used to create and manage the digital products derived from open metadata. (Extracted from 6.0-SNAPSHOT)
