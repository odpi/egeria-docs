```mermaid
---
title: ITProfile - OpenLineageAPIPublisher [571db680-8ca5-42c3-9de3-6df886303ca9]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**OpenLineageAPIPublisher**"}
2@{ shape: bow-rect, label: "*User Identity*
**olapipubnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**OpenLineageAPIPublisherIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> OpenLineageAPIPublisher: Publishes open lineage events to the APIs attached as catalog targets. (Extracted from 6.0-SNAPSHOT)
