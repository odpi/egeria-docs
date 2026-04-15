```mermaid
---
title: SolutionBlueprint - Jacquard Digital Product Loom [08851db5-cb2e-466b-94c0-3976dc7736a0]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
4==>|"Maintains [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
3==>|"maintain catalog entry [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
3==>|"add products to catalog [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
3==>|"monitor for changes [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
3==>|"set up subscription managers [Solution Linking Wire]"|8
9@{ shape: stadium, label: "*Collection Membership*
**... plus 2 Items**"}
9-.->3
1==>|"Collection Membership"|6
10@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
10==>|"Shop for data [Solution Component Actor]"|6
6==>|"search for type of data [Solution Linking Wire]"|5
11@{ shape: rect, label: "*Solution Blueprint*
**Searching for Digital Products**"}
11==>|"Collection Membership"|6
2==>|"Collection Membership"|6
12@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
12-.->6
1==>|"Collection Membership"|5
13@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
13==>|"Develops [Solution Component Actor]"|5
14@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
14==>|"retrieve data [Solution Linking Wire]"|5
15@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
15==>|"remove subscription [Solution Linking Wire]"|5
5==>|"query metadata [Solution Linking Wire]"|7
16@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
16-.->5
1==>|"Collection Membership"|7
2==>|"Collection Membership"|7
17@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
17==>|"Collection Membership"|7
1==>|"Collection Membership"|8
18@{ shape: rect, label: "*Solution Component*
**Digital Product Community**"}
8==>|"notify when product changes [Solution Linking Wire]"|18
19@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
19==>|"configure subscription [Solution Linking Wire]"|8
8==>|"initiate when product changes [Solution Linking Wire]"|14
8==>|"monitor product changes [Solution Linking Wire]"|5
2==>|"Collection Membership"|8
20@{ shape: stadium, label: "*Collection Membership*
**... plus 3 Items**"}
20-.->8
style 11 color:#000000, fill:#f5fffa, stroke:#000000
style 12 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 13 color:#000000, fill:#FFE599, stroke:#000000
style 14 color:#000000, fill:#DDA0DD, stroke:#000000
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 17 color:#000000, fill:#f5fffa, stroke:#000000
style 18 color:#000000, fill:#DDA0DD, stroke:#000000
style 19 color:#000000, fill:#DDA0DD, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
> Jacquard Digital Product Loom: Description of the processing used to create and manage the digital products derived from open metadata in the Open Metadata Digital Product Catalog. (Extracted from 6.0-SNAPSHOT)
