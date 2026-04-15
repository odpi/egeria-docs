```mermaid
---
title: ITProfile - UnityCatalogInsideCatalogSynchronizer [8aed3a46-10cd-42c2-b576-60c50795e20b]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**UnityCatalogInsideCatalogSynchronizer**"}
2@{ shape: bow-rect, label: "*User Identity*
**uccatcatnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**UnityCatalogAssetExchange**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> UnityCatalogInsideCatalogSynchronizer: Synchronizes metadata information about the contents of catalogs found in the OSS Unity Catalog ''catalog of catalogs'' with the open metadata ecosystem. (Extracted from 6.0-SNAPSHOT)
