```mermaid
---
title: SolutionComponent - Apache Kafka [d52a42e9-87a1-4382-aa0e-d0a3a63465f6]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Apache Kafka**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Runtimes Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Open Metadata Topic**"}
1==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
4==>|"metadata change notifications [Solution Linking Wire]"|3
5@{ shape: rect, label: "*Solution Component*
**Integration Daemon**"}
3==>|"metadata change notifications [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Engine Host**"}
3==>|"metadata change notifications [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Open Lineage Governance Action Publisher**"}
3==>|"distribute events events [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Open Lineage Topic**"}
1==>|"Solution Composition"|8
9@{ shape: rect, label: "*Solution Component*
**Open Lineage Proxy**"}
9==>|"open lineage events [Solution Linking Wire]"|8
8==>|"open lineage events [Solution Linking Wire]"|5
10@{ shape: rect, label: "*Solution Component*
**Open Lineage Kafka Listener**"}
8==>|"receives events [Solution Linking Wire]"|10
11@{ shape: rect, label: "*Solution Component*
**Open Governance Topic**"}
1==>|"Solution Composition"|11
11==>|"configuration change notifications [Solution Linking Wire]"|5
11==>|"configuration change and engine action notifications [Solution Linking Wire]"|6
4==>|"open governance notifications [Solution Linking Wire]"|11
9==>|"open lineage events [Solution Linking Wire]"|1
12@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
12==>|"exchanges notifications [Solution Linking Wire]"|1
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
click 11 "https://egeria-project.org/concepts/open-metadata-topic-connector/" "Click for more documentation" _blank
click 1 "https://kafka.apache.org/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/open-metadata-topic-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/integration-daemon/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/engine-host/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 9 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
```
> Apache Kafka: Manages a reliable topic based service. (Extracted from 6.0-SNAPSHOT)
