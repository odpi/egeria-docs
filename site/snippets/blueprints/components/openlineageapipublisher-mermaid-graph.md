```mermaid
---
title: SolutionComponent - Open Lineage API Publisher [f993be00-e07f-452c-96d0-22813f5f9db6]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Open Lineage API Publisher**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Lineage Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Open Lineage Kafka Listener**"}
3==>|"distribute events events [Solution Linking Wire]"|1
4@{ shape: rect, label: "*Solution Component*
**Marquez Server**"}
1==>|"Catalog Resource [Solution Linking Wire]"|4
5@{ shape: stadium, label: "*Integration Connector*
**OpenLineageAPIPublisherIntegrationConnector**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://marquezproject.ai/" "Click for more documentation" _blank
```
> Open Lineage API Publisher: Publishes open lineage events to APIs linked through CatalogTarget relationships.  These open lineage events may have been received from third party processes or were generated from running Governance Action Processes in the open metadata ecosystem. (Extracted from 6.0-SNAPSHOT)
