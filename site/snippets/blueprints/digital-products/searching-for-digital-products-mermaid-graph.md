```mermaid
---
title: SolutionBlueprint - Searching for Digital Products [6bfa0952-a5db-4707-ae96-b1f3cfe8b817]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Searching for Digital Products**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
4==>|"Shop for data [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
5==>|"add products to catalog [Solution Linking Wire]"|3
6@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
3==>|"search for type of data [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
7==>|"Collection Membership"|3
2==>|"Collection Membership"|3
8@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
8-.->3
1==>|"Collection Membership"|6
9@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
9==>|"Develops [Solution Component Actor]"|6
10@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
10==>|"retrieve data [Solution Linking Wire]"|6
5==>|"maintain catalog entry [Solution Linking Wire]"|6
11@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
11==>|"remove subscription [Solution Linking Wire]"|6
12@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
6==>|"query metadata [Solution Linking Wire]"|12
13@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
13-.->6
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#FFE599, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
```
> Searching for Digital Products: Description of the processing when a potential consumer is searching the Open Metadata Digital Product Catalog for the right data for their project. (Extracted from 6.0-SNAPSHOT)
