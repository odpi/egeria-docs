```mermaid
---
title: SolutionComponent - Product Catalog [16c737cc-1dda-46b3-ab4f-79d3acf33aa1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Product Catalog**"}
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
**Searching for Digital Products**"}
5==>|"Collection Membership"|1
6@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata Product Subscriber**"}
6==>|"Shop for data [Solution Component Actor]"|1
7@{ shape: rect, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
7==>|"add products to catalog [Solution Linking Wire]"|1
8@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"search for type of data [Solution Linking Wire]"|8
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#f5fffa, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
```
> Product Catalog: Supports the process of locating the appropriate digital product by providing organized, searchable descriptions of the digital products to the product consumers. (Extracted from 6.0-SNAPSHOT)
