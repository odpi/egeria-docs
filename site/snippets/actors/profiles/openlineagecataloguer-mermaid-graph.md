```mermaid
---
title: ITProfile - OpenLineageCataloguer [f3276fb0-0cc6-4e3f-a437-c8e186662191]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**OpenLineageCataloguer**"}
2@{ shape: bow-rect, label: "*User Identity*
**olcatnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**OpenLineageCataloguerIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
4@{ shape: rounded, label: "*Contribution Record*
**Contribution record for OpenLineageCataloguer**"}
1==>|"Contribution"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
style 4 color:#000000, fill:#39add1, stroke:#004563
```
> OpenLineageCataloguer: Catalogs the resources detailed in the open lineage events received by the integration daemon. (Extracted from 6.0-SNAPSHOT)
