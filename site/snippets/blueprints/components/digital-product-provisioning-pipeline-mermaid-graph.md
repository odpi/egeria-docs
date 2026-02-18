```mermaid
---
title: SolutionComponent - Digital Product Provisioning Pipeline [9ab6da2d-6218-4b20-937a-76f41d326dc6]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Creating a new Subscription to a Digital Product**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Subscriptions Solution Blueprint**"}
4==>|"Collection Membership"|1
5@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
5==>|"Collection Membership"|1
6@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"retrieve data [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Digital Product Delivery Location**"}
1==>|"maintain data [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
8==>|"initiate when product changes [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#f5fffa, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
```
> Digital Product Provisioning Pipeline: This is the service that copies the product data to each of the subscribers'' delivery location. (Extracted from 6.0-SNAPSHOT)
