```mermaid
---
title: SolutionBlueprint - Searching for Digital Products [b93a2f90-5b14-4736-bcc8-b54efb029fa9]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Searching for Digital Products**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"Collection Membership"|3
4@{ shape: trap-t, label: "*Digital Product Manager*
**Open Metadata Product Manager**"}
4==>|"Develops [Solution Component Actor]"|3
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
3==>|"query metadata [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
6==>|"retrieve data [Solution Linking Wire]"|3
7@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
7==>|"monitor product changes [Solution Linking Wire]"|3
8@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
8==>|"read subscription requirements [Solution Linking Wire]"|3
9@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
9==>|"remove subscription [Solution Linking Wire]"|3
10@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 8 Items**"}
10-.->3
11@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
1==>|"Collection Membership"|11
12@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
12==>|"Shop for data [Solution Component Actor]"|11
13@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
13==>|"add products to catalog [Solution Linking Wire]"|11
11==>|"search for type of data [Solution Linking Wire]"|3
2==>|"Collection Membership"|11
14@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
14==>|"Collection Membership"|11
15@{ shape: rect, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
15==>|"Collection Membership"|11
16@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
16-.->11
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#f5fffa, stroke:#000000
style 15 color:#000000, fill:#f5fffa, stroke:#000000
style 16 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
```
> Searching for Digital Products: Description of the processing when a potential consumer is searching the Open Metadata Digital Product Catalog for the right data for their project. (Extracted from 6.0-SNAPSHOT)
