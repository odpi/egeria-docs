```mermaid
---
title: SolutionComponent - Open Governance Topic [145b6fd1-6267-429a-90f3-851a2dc1350e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Open Governance Topic**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Apache Kafka**"}
3==>|"Solution Composition"|1
4@{ shape: rect, label: "*Solution Component*
**Integration Daemon**"}
1==>|"configuration change notifications [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Engine Host**"}
1==>|"configuration change and engine action notifications [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
6==>|"open governance notifications [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/open-metadata-topic-connector/" "Click for more documentation" _blank
click 3 "https://kafka.apache.org/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-daemon/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/engine-host/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Open Governance Topic: Provides notifications when governance server configuration (Governance engines, governance services, integration groups, and integration connectors) changes.  It also transmits changes to engine actions to allow the engine host to initiate the actions. (Extracted from 6.0-SNAPSHOT)
