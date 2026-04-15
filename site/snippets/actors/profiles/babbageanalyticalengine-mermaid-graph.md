```mermaid
---
title: ITProfile - BabbageAnalyticalEngine [fcd8338d-e629-496b-854b-942e9026e206]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**BabbageAnalyticalEngine**"}
2@{ shape: bow-rect, label: "*User Identity*
**babbagenpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**BabbageAnalyticalEngineIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
4@{ shape: rounded, label: "*Contribution Record*
**Contribution record for BabbageAnalyticalEngine**"}
1==>|"Contribution"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
style 4 color:#000000, fill:#39add1, stroke:#004563
```
> BabbageAnalyticalEngine: Initiates analytical processing using the Governance Action Types that are attached as catalog targets. (Extracted from 6.0-SNAPSHOT)
