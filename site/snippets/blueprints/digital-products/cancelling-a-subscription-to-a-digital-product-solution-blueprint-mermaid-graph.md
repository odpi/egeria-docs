```mermaid
---
title: Components and Roles for Solution Blueprint - Cancelling a Subscription to a Digital Product [91eb2348-9673-4760-90b7-b9d633718026]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
5@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
5==>|"Cancel product subscription,
[Solution Component Actor]"|2
2==>|"remove subscription,
[Solution Linking Wire]"|4
2==>|"(maybe) remove copy,
[Solution Linking Wire]"|3
6@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
6==>|"Consume data,
[Solution Component Actor]"|3
7@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
7==>|"Develops,
[Solution Component Actor]"|4
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
> Cancelling a Subscription to a Digital Product: Description of the processing used to cancel a subscription to an Open Metadata Digital Product. (Extracted from 6.0-SNAPSHOT)
