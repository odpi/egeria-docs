```mermaid
---
title: Components and Roles for Solution Blueprint - Cancelling a Subscription to a Digital Product [1f3bd116-a1b4-4d35-8bf5-03ac8d1e1210]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
3@{ shape: subproc, label: "*Solution Component*
**Cancel Product Subscription**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
5@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
5==>|"Develops,
[Solution Component Actor]"|2
3==>|"remove subscription,
[Solution Linking Wire]"|2
6@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
6==>|"Cancel product subscription,
[Solution Component Actor]"|3
3==>|"(maybe) remove copy,
[Solution Linking Wire]"|4
7@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
7==>|"Consume data,
[Solution Component Actor]"|4
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
> Cancelling a Subscription to a Digital Product: Description of the processing used to cancel a subscription to an Open Metadata Digital Product. (Extracted from 6.0-SNAPSHOT)
