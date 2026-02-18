```mermaid
---
title: SolutionComponent - Open Lineage Proxy [19af8706-17b9-4367-865f-2181dcb51646]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Open Lineage Proxy**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Lineage Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Runtimes Solution Blueprint**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
4==>|"Collection Membership"|1
5@{ shape: rect, label: "*Solution Component*
**Open Lineage Topic**"}
1==>|"open lineage events [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Apache Kafka**"}
1==>|"open lineage events [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Apache Airflow Server**"}
7==>|"open lineage events [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 5 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 6 "https://kafka.apache.org/" "Click for more documentation" _blank
click 7 "https://airflow.apache.org/" "Click for more documentation" _blank
```
> Open Lineage Proxy: Consolidates open lineage events from data engines and pipes them to Apache Kafka. (Extracted from 6.0-SNAPSHOT)
