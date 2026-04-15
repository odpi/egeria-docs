```mermaid
---
title: ITProfile - UnityCatalogServerSynchronizer [40e2f141-c9f4-423e-be05-430afbce837f]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**UnityCatalogServerSynchronizer**"}
2@{ shape: bow-rect, label: "*User Identity*
**ucservernpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**UnityCatalogServerIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> UnityCatalogServerSynchronizer: Synchronizes metadata about the catalogs found in the OSS Unity Catalog ''catalog of catalogs'' with the open metadata ecosystem. (Extracted from 6.0-SNAPSHOT)
