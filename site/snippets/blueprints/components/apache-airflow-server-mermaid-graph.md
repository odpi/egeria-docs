```mermaid
---
title: SolutionComponent - Apache Airflow Server [6db0416a-1e7f-4e7c-aae6-8925c2148820]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Apache Airflow Server**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Runtimes Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Component*
**Apache Airflow DAG**"}
1==>|"Solution Composition"|4
5@{ shape: rect, label: "*Solution Component*
**Apache Airflow PostgreSQL Database**"}
1==>|"stores data [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Open Lineage Proxy**"}
1==>|"open lineage events [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Egeria Workspaces PostgreSQL Server**"}
1==>|"stores data [Solution Linking Wire]"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://airflow.apache.org/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0215-Software-Components/" "Click for more documentation" _blank
click 5 "https://www.postgresql.org/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 7 "https://www.postgresql.org/" "Click for more documentation" _blank
```
> Apache Airflow Server: Runs data movement and transformation pipelines. (Extracted from 6.0-SNAPSHOT)
