```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Product Subscriptions Solution Blueprint [a9fa182f-69e0-4515-9e6d-bb0bcbbc5760]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
4@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
5@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
6@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
6==>|"Consume data,
[Solution Component Actor]"|2
5==>|"maintain data,
[Solution Linking Wire]"|2
7@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
7==>|"Develops,
[Solution Component Actor]"|3
5==>|"retrieve data,
[Solution Linking Wire]"|3
4==>|"monitor product changes,
[Solution Linking Wire]"|3
4==>|"initiate when product changes,
[Solution Linking Wire]"|5
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
> Open Metadata Digital Product Subscriptions Solution Blueprint: Description of the processing used to create and manage subscriptions to Open Metadata Digital Products. (Extracted from 6.0-SNAPSHOT)
