```mermaid
---
title: SolutionBlueprint - Creating a new Subscription to a Digital Product [8d0d525d-d058-491e-8d96-801505900bf8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Creating a new Subscription to a Digital Product**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Digital Product Delivery Location**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Consumer**"}
4==>|"Consume data [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
5==>|"maintain data [Solution Linking Wire]"|3
6@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
6==>|"(maybe) remove copy [Solution Linking Wire]"|3
2==>|"Collection Membership"|3
7@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
7==>|"Collection Membership"|3
8@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
8==>|"Collection Membership"|3
9@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
9-.->3
10@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
1==>|"Collection Membership"|10
11@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
11==>|"Subscribe to product [Solution Component Actor]"|10
12@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
10==>|"configure subscription [Solution Linking Wire]"|12
13@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
10==>|"read subscription requirements [Solution Linking Wire]"|13
2==>|"Collection Membership"|10
8==>|"Collection Membership"|10
1==>|"Collection Membership"|5
5==>|"retrieve data [Solution Linking Wire]"|13
12==>|"initiate when product changes [Solution Linking Wire]"|5
2==>|"Collection Membership"|5
8==>|"Collection Membership"|5
14@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
14-.->5
1==>|"Collection Membership"|13
15@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
15==>|"Develops [Solution Component Actor]"|13
16@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
16==>|"maintain catalog entry [Solution Linking Wire]"|13
6==>|"remove subscription [Solution Linking Wire]"|13
17@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
17==>|"search for type of data [Solution Linking Wire]"|13
18@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
13==>|"query metadata [Solution Linking Wire]"|18
19@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
19-.->13
style 11 color:#000000, fill:#FFE599, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#FFE599, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#DDA0DD, stroke:#000000
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#f5fffa, stroke:#000000
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
```
> Creating a new Subscription to a Digital Product: Description of the processing when a consumer creates a new subscription to an Open Metadata Digital Product. (Extracted from 6.0-SNAPSHOT)
