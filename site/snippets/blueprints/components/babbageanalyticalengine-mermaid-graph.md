```mermaid
---
title: SolutionComponent - Babbage Analytical Engine [2e7ec1b4-a8ba-4be6-b345-2c1735a94c7a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Babbage Analytical Engine**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Products Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Core Content Pack**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Blueprint*
**Organization Insight Content Pack**"}
4==>|"Collection Membership"|1
5@{ shape: rect, label: "*Solution Component*
**Award Karma Points**"}
1==>|"schedules [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|6
7@{ shape: stadium, label: "*Integration Connector*
**BabbageAnalyticalEngineIntegrationConnector**"}
1==>|"Implemented By"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Babbage Analytical Engine: Initiates analytical processing that generates statistics on the content and operation of the open metadata ecosystem.  The analytical processors are called lovelace analytical services. (Extracted from 6.0-SNAPSHOT)
