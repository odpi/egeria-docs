```mermaid
---
title: SolutionBlueprint - Open Metadata Digital Product Subscriptions Solution Blueprint [a9fa182f-69e0-4515-9e6d-bb0bcbbc5760]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
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
**Open Metadata Digital Product Catalog Components**"}
7==>|"Collection Membership"|3
8@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
8-.->3
9@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"Collection Membership"|9
10@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
10==>|"Develops [Solution Component Actor]"|9
5==>|"retrieve data [Solution Linking Wire]"|9
11@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
11==>|"maintain catalog entry [Solution Linking Wire]"|9
6==>|"remove subscription [Solution Linking Wire]"|9
12@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
12==>|"search for type of data [Solution Linking Wire]"|9
13@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
9==>|"query metadata [Solution Linking Wire]"|13
14@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
14-.->9
15@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
1==>|"Collection Membership"|15
16@{ shape: rect, label: "*Solution Component*
**Digital Product Community**"}
15==>|"notify when product changes [Solution Linking Wire]"|16
17@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
17==>|"configure subscription [Solution Linking Wire]"|15
15==>|"initiate when product changes [Solution Linking Wire]"|5
15==>|"monitor product changes [Solution Linking Wire]"|9
11==>|"set up subscription managers [Solution Linking Wire]"|15
2==>|"Collection Membership"|15
18@{ shape: stadium, label: "*Collection Membership*
**... plus 3 Items**"}
18-.->15
1==>|"Collection Membership"|5
2==>|"Collection Membership"|5
7==>|"Collection Membership"|5
19@{ shape: rect, label: "*Solution Blueprint*
**Creating a new Subscription to a Digital Product**"}
19==>|"Collection Membership"|5
20@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
20-.->5
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 19 color:#000000, fill:#f5fffa, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
> Open Metadata Digital Product Subscriptions Solution Blueprint: Description of the processing used to create and manage subscriptions to Open Metadata Digital Products. (Extracted from 6.0-SNAPSHOT)
