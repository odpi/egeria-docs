```mermaid
---
title: Components and Roles for Solution Blueprint - Creating a new Subscription to a Digital Product [45287174-1031-4e9d-9cc6-276e0ed33019]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
3@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
4@{ shape: subproc, label: "*Solution Component*
**Create New Product Subscription**"}
5@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
6@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
6==>|"Consume data,
[Solution Component Actor]"|2
3==>|"maintain data,
[Solution Linking Wire]"|2
3==>|"retrieve data,
[Solution Linking Wire]"|5
7@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
7==>|"Subscribe to product,
[Solution Component Actor]"|4
4==>|"read subscription requirements,
[Solution Linking Wire]"|5
8@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
8==>|"Develops,
[Solution Component Actor]"|5
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
```
> Creating a new Subscription to a Digital Product: Description of the processing when a consumer creates a new subscription to an Open Metadata Digital Product. (Extracted from 6.0-SNAPSHOT)
