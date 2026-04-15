```mermaid
---
title: ITProfile - HarvestOpenMetadata [481954ca-a3b3-48fa-8085-8dae605c09df]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**HarvestOpenMetadata**"}
2@{ shape: bow-rect, label: "*User Identity*
**nannyomnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**HarvestOpenMetadataIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> HarvestOpenMetadata: Monitors metadata changes in the open metadata ecosystem and populates a PostgreSQL database schema. (Extracted from 6.0-SNAPSHOT)
