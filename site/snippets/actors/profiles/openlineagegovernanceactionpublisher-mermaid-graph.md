```mermaid
---
title: ITProfile - OpenLineageGovernanceActionPublisher [36ee3ac8-d6ae-4462-9a32-f9e1b3f7b7a6]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**OpenLineageGovernanceActionPublisher**"}
2@{ shape: bow-rect, label: "*User Identity*
**olgapubnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**OpenLineageGovernanceActionPublisherIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> OpenLineageGovernanceActionPublisher: Publishes open lineage events whenever governance actions run in the open metadata ecosystem. (Extracted from 6.0-SNAPSHOT)
