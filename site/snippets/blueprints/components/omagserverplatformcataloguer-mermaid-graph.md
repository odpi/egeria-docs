```mermaid
---
title: SolutionComponent - OMAG Server Platform Cataloguer [2eed7ad8-9189-4971-ba67-2de94efc7db3]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**OMAG Server Platform Cataloguer**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
1==>|"Catalog Resource [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Configure the OMAG Server Platform Cataloguer**"}
5==>|"configures [Solution Linking Wire]"|1
6@{ shape: stadium, label: "*Integration Connector*
**OMAGServerPlatformIntegrationConnector**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> OMAG Server Platform Cataloguer: Monitors the running OMAG Server Platform instances that are catalogued in the open metadata ecosystem and maintains the metadata that describes the servers and their configuration. (Extracted from 6.0-SNAPSHOT)
