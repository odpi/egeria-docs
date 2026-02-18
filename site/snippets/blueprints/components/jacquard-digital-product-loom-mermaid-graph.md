```mermaid
---
title: SolutionComponent - Jacquard Digital Product Loom [5e6bf652-b0e6-44b0-90c4-f9e5b5fef455]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Jacquard Digital Product Loom**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Solution**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Product Catalog Components**"}
4==>|"Collection Membership"|1
5@{ shape: trap-t, label: "*Person Role*
**Open Metadata Digital Product Loom (Jacquard) Support Role**"}
5==>|"Maintains [Solution Component Actor]"|1
6@{ shape: rect, label: "*Solution Component*
**Product Catalog**"}
1==>|"add products to catalog [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"monitor for changes [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Baudot Subscription Manager**"}
1==>|"set up subscription managers [Solution Linking Wire]"|8
9@{ shape: rect, label: "*Solution Component*
**Open Metadata Product**"}
1==>|"maintain catalog entry [Solution Linking Wire]"|9
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
```
> Jacquard Digital Product Loom: Defines and maintains digital products based on the content of the open metadata repositories.  These products are assembled into a digital product catalog along with a glossary and data dictionary.  This integration connector is started when the Open Metadata Digital Product Archive is loaded.  It is responsible for detecting opportunities for open metadata digital products, creating a catalog entry for them and then maintaining last update information in the product information.  This is used to drive the distribution of open metadata updates to subscribers. (Extracted from 6.0-SNAPSHOT)
