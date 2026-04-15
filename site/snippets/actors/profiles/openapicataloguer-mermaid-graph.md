```mermaid
---
title: ITProfile - OpenAPICataloguer [dd414cee-d7bc-4f91-9e43-669a20aba5e8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**OpenAPICataloguer**"}
2@{ shape: bow-rect, label: "*User Identity*
**apicatnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**OpenAPIIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
4@{ shape: rounded, label: "*Contribution Record*
**Contribution record for OpenAPICataloguer**"}
1==>|"Contribution"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
style 4 color:#000000, fill:#39add1, stroke:#004563
```
> OpenAPICataloguer: Catalogs the REST APIs found in servers attached as catalog targets that support the swagger API. (Extracted from 6.0-SNAPSHOT)
