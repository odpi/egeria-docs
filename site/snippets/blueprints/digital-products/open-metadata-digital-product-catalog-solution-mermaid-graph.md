```mermaid
---
title: SolutionBlueprint - Open Metadata Digital Product Catalog Solution [e2c17a65-d258-4b1b-943b-eab450c53ddf]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2@{ shape: rect, label: "*Solution Component*
**Digital Product Delivery Location**"}
1==>|"Collection Membership"|2
3@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
3==>|"Consume data [Solution Component Actor]"|2
4@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
4==>|"maintain data [Solution Linking Wire]"|2
5@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
5==>|"(maybe) remove copy [Solution Linking Wire]"|2
6@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
6==>|"Collection Membership"|2
7@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
7==>|"Collection Membership"|2
8@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
8-.->2
9@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Community Solution Blueprint**"}
1==>|"Collection Membership"|9
10@{ shape: rect, label: "*Solution Component*
**Digital Product Community**"}
9==>|"Collection Membership"|10
1==>|"Collection Membership"|4
11@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
4==>|"retrieve data [Solution Linking Wire]"|11
12@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
12==>|"initiate when product changes [Solution Linking Wire]"|4
7==>|"Collection Membership"|4
13@{ shape: rect, label: "*Solution Blueprint*
**Creating a new Subscription to a Digital Product**"}
13==>|"Collection Membership"|4
14@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
14-.->4
15@{ shape: rect, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
1==>|"Collection Membership"|15
16@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
15==>|"Collection Membership"|16
17@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
15==>|"Collection Membership"|17
15==>|"Collection Membership"|11
18@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
15==>|"Collection Membership"|18
15==>|"Collection Membership"|12
1==>|"Collection Membership"|6
6==>|"Collection Membership"|11
6==>|"Collection Membership"|12
6==>|"Collection Membership"|4
1==>|"Collection Membership"|17
19@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
19==>|"Shop for data [Solution Component Actor]"|17
16==>|"add products to catalog [Solution Linking Wire]"|17
17==>|"search for type of data [Solution Linking Wire]"|11
20@{ shape: rect, label: "*Solution Blueprint*
**Searching for Digital Products**"}
20==>|"Collection Membership"|17
21@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
21-.->17
22@{ shape: stadium, label: "*Collection Membership*
**... plus 11 Items**"}
1-.->22
23@{ shape: rect, label: "*Digital Product Catalog*
**Open Metadata Digital Product Catalog**"}
23==>|"Solution Design"|1
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 22 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 23 color:#000000, fill:#f5fffa, stroke:#000000
style 13 color:#000000, fill:#f5fffa, stroke:#000000
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#f5fffa, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#DDA0DD, stroke:#000000
style 19 color:#000000, fill:#FFE599, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#f5fffa, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#f5fffa, stroke:#000000
style 20 color:#000000, fill:#f5fffa, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
style 21 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
> Open Metadata Digital Product Catalog Solution: The Open Metadata Digital Product Catalog enables the distribution of reference data and context for AI processing from the open metadata ecosystem.  The Product Catalog makes it easy to locate the right data and the subscription manager delivers the data to wherever it needs to be.  Behind the scenes, lineage and statistics on the data consumption are automatically maintained, demonstrating the value chains associated with the data. (Extracted from 6.0-SNAPSHOT)
