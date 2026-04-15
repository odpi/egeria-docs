```mermaid
---
title: SolutionComponent - Baudot Subscription Manager [08994027-1d3c-404e-9c9a-a0866248e4e0]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Baudot Subscription Manager**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
4==>|"Collection Membership"|1
5@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
5==>|"Collection Membership"|1
6@{ shape: rect, label: "*Solution Component*
**Digital Product Community**"}
1==>|"notify when product changes [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
7==>|"configure subscription [Solution Linking Wire]"|1
8@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
1==>|"initiate when product changes [Solution Linking Wire]"|8
9@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"monitor product changes [Solution Linking Wire]"|9
10@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
10==>|"set up subscription managers [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#f5fffa, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
```
> Baudot Subscription Manager: This is the service that monitors for changes in registered products and notifies subscribers when changes occur. (Extracted from 6.0-SNAPSHOT)
