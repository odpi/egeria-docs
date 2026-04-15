```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Product Catalog Solution [e2c17a65-d258-4b1b-943b-eab450c53ddf]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
3@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**Product Catalog**"}
5@{ shape: docs, label: "*Solution Component*
**Digital Product Community**"}
6@{ shape: subproc, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
7@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
8@{ shape: subproc, label: "*Solution Component*
**Create New Product Subscription**"}
9@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
10@{ shape: lin-cyl, label: "*Solution Component*
**Metadata Access Store**"}
11@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
12@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
12==>|"Consume data,
[Solution Component Actor]"|2
3==>|"maintain data,
[Solution Linking Wire]"|2
7==>|"(maybe) remove copy,
[Solution Linking Wire]"|2
3==>|"retrieve data,
[Solution Linking Wire]"|11
9==>|"initiate when product changes,
[Solution Linking Wire]"|3
13@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
13==>|"Shop for data,
[Solution Component Actor]"|4
6==>|"add products to catalog,
[Solution Linking Wire]"|4
4==>|"search for type of data,
[Solution Linking Wire]"|11
14@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Digital Product Community Member**"}
14==>|"Member of,
[Solution Component Actor]"|5
15@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
15==>|"Jacquard and subscription manager discussions,
[Solution Component Actor]"|5
16@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
16==>|"Product discussions,
[Solution Component Actor]"|5
9==>|"notify when product changes,
[Solution Linking Wire]"|5
15==>|"Maintains,
[Solution Component Actor]"|6
6==>|"maintain catalog entry,
[Solution Linking Wire]"|11
6==>|"monitor for changes,
[Solution Linking Wire]"|10
6==>|"set up subscription managers,
[Solution Linking Wire]"|9
13==>|"Cancel product subscription,
[Solution Component Actor]"|7
7==>|"remove subscription,
[Solution Linking Wire]"|11
13==>|"Subscribe to product,
[Solution Component Actor]"|8
8==>|"configure subscription,
[Solution Linking Wire]"|9
8==>|"read subscription requirements,
[Solution Linking Wire]"|11
9==>|"monitor product changes,
[Solution Linking Wire]"|11
11==>|"query metadata,
[Solution Linking Wire]"|10
16==>|"Develops,
[Solution Component Actor]"|11
end
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 13 color:#000000, fill:#FFE599, stroke:#000000
style 14 color:#000000, fill:#FFE599, stroke:#000000
style 15 color:#000000, fill:#FFE599, stroke:#000000
style 16 color:#000000, fill:#FFE599, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
```
> Open Metadata Digital Product Catalog Solution: The Open Metadata Digital Product Catalog enables the distribution of reference data and context for AI processing from the open metadata ecosystem.  The Product Catalog makes it easy to locate the right data and the subscription manager delivers the data to wherever it needs to be.  Behind the scenes, lineage and statistics on the data consumption are automatically maintained, demonstrating the value chains associated with the data. (Extracted from 6.0-SNAPSHOT)
