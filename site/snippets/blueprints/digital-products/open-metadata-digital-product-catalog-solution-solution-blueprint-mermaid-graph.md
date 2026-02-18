```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Product Catalog Solution [c508ec4d-b3a9-4d2c-a032-301c8e5ce037]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: docs, label: "*Solution Component*
**Digital Product Community**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
4@{ shape: subproc, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
5@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
6@{ shape: subproc, label: "*Solution Component*
**Create New Product Subscription**"}
7@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
8@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
9@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
10@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
11@{ shape: lin-cyl, label: "*Solution Component*
**Metadata Access Store**"}
12@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
12==>|"Jacquard and subscription manager discussions,
[Solution Component Actor]"|2
13@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
13==>|"Product discussions,
[Solution Component Actor]"|2
14@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Digital Product Community Member**"}
14==>|"Member of,
[Solution Component Actor]"|2
8==>|"notify when product changes,
[Solution Linking Wire]"|2
15@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
15==>|"Shop for data,
[Solution Component Actor]"|3
4==>|"add products to catalog,
[Solution Linking Wire]"|3
3==>|"search for type of data,
[Solution Linking Wire]"|10
12==>|"Maintains,
[Solution Component Actor]"|4
4==>|"monitor for changes,
[Solution Linking Wire]"|11
4==>|"set up subscription managers,
[Solution Linking Wire]"|8
4==>|"maintain catalog entry,
[Solution Linking Wire]"|10
5==>|"retrieve data,
[Solution Linking Wire]"|10
5==>|"maintain data,
[Solution Linking Wire]"|7
8==>|"initiate when product changes,
[Solution Linking Wire]"|5
15==>|"Subscribe to product,
[Solution Component Actor]"|6
6==>|"read subscription requirements,
[Solution Linking Wire]"|10
6==>|"configure subscription,
[Solution Linking Wire]"|8
16@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
16==>|"Consume data,
[Solution Component Actor]"|7
9==>|"(maybe) remove copy,
[Solution Linking Wire]"|7
8==>|"monitor product changes,
[Solution Linking Wire]"|10
15==>|"Cancel product subscription,
[Solution Component Actor]"|9
9==>|"remove subscription,
[Solution Linking Wire]"|10
13==>|"Develops,
[Solution Component Actor]"|10
10==>|"query metadata,
[Solution Linking Wire]"|11
end
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 13 color:#000000, fill:#FFE599, stroke:#000000
style 14 color:#000000, fill:#FFE599, stroke:#000000
style 15 color:#000000, fill:#FFE599, stroke:#000000
style 16 color:#000000, fill:#FFE599, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
```
> Open Metadata Digital Product Catalog Solution: The Open Metadata Digital Product Catalog enables the distribution of reference data and context for AI processing from the open metadata ecosystem.  The Product Catalog makes it easy to locate the right data and the subscription manager delivers the data to wherever it needs to be.  Behind the scenes, lineage and statistics on the data consumption are automatically maintained, demonstrating the value chains associated with the data. (Extracted from 6.0-SNAPSHOT)
