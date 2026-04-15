```mermaid
---
title: ITProfile - OpenLineageFilePublisher [98e8f487-6c70-4514-83ec-46527e2f6756]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**OpenLineageFilePublisher**"}
2@{ shape: bow-rect, label: "*User Identity*
**olfilepubnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**OpenLineageFilePublisherIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> OpenLineageFilePublisher: Publishes open lineage events as JSON files to each of the file directories attached as catalog targets. (Extracted from 6.0-SNAPSHOT)
