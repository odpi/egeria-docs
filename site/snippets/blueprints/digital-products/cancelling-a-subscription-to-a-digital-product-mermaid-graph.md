```mermaid
---
title: SolutionBlueprint - Cancelling a Subscription to a Digital Product [91eb2348-9673-4760-90b7-b9d633718026]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Cancelling a Subscription to a Digital Product**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
4==>|"Cancel product subscription [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
3==>|"remove subscription [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Digital Product Delivery Location**"}
3==>|"(maybe) remove copy [Solution Linking Wire]"|6
2==>|"Collection Membership"|3
7@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
7==>|"Collection Membership"|3
1==>|"Collection Membership"|6
8@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
8==>|"Consume data [Solution Component Actor]"|6
9@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
9==>|"maintain data [Solution Linking Wire]"|6
2==>|"Collection Membership"|6
10@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
10==>|"Collection Membership"|6
7==>|"Collection Membership"|6
11@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
11-.->6
1==>|"Collection Membership"|5
12@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
12==>|"Develops [Solution Component Actor]"|5
9==>|"retrieve data [Solution Linking Wire]"|5
13@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
13==>|"maintain catalog entry [Solution Linking Wire]"|5
14@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
14==>|"search for type of data [Solution Linking Wire]"|5
15@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
5==>|"query metadata [Solution Linking Wire]"|15
16@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
16-.->5
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#DDA0DD, stroke:#000000
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#f5fffa, stroke:#000000
```
> Cancelling a Subscription to a Digital Product: Description of the processing used to cancel a subscription to an Open Metadata Digital Product. (Extracted from 6.0-SNAPSHOT)
