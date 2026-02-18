```mermaid
---
title: Components and Roles for Solution Blueprint - Open Metadata Digital Product Subscriptions Solution Blueprint [442fc481-eb67-4a82-97d6-32147bc9790c]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Baudot Subscription Manager**"}
3@{ shape: das, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**Open Metadata Product**"}
5@{ shape: lin-cyl, label: "*Solution Component*
**Digital Product Delivery Location**"}
2==>|"monitor product changes,
[Solution Linking Wire]"|4
2==>|"initiate when product changes,
[Solution Linking Wire]"|3
3==>|"retrieve data,
[Solution Linking Wire]"|4
3==>|"maintain data,
[Solution Linking Wire]"|5
6@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
6==>|"Develops,
[Solution Component Actor]"|4
7@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
7==>|"Consume data,
[Solution Component Actor]"|5
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
> Open Metadata Digital Product Subscriptions Solution Blueprint: Description of the processing used to create and manage subscriptions to Open Metadata Digital Products. (Extracted from 6.0-SNAPSHOT)
