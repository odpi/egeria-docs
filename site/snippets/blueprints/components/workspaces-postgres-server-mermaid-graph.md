```mermaid
---
title: SolutionComponent - Egeria Workspaces PostgreSQL Server [235a335a-f010-43ee-b785-3774380b5058]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Egeria Workspaces PostgreSQL Server**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Runtimes Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Unity Catalog PostgreSQL Database**"}
1==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Working Unity Catalog**"}
4==>|"stores data [Solution Linking Wire]"|3
5@{ shape: rect, label: "*Solution Component*
**Apache Airflow PostgreSQL Database**"}
1==>|"Solution Composition"|5
6@{ shape: rect, label: "*Solution Component*
**Apache Airflow Server**"}
6==>|"stores data [Solution Linking Wire]"|5
7@{ shape: rect, label: "*Solution Component*
**Marquez PostgreSQL Database**"}
1==>|"Solution Composition"|7
8@{ shape: rect, label: "*Solution Component*
**Marquez Server**"}
8==>|"stores data [Solution Linking Wire]"|7
9@{ shape: rect, label: "*Solution Component*
**Egeria PostgreSQL Database**"}
1==>|"Solution Composition"|9
10@{ shape: rect, label: "*Solution Component*
**Open Metadata Repository**"}
9==>|"Solution Composition"|10
11@{ shape: rect, label: "*Solution Component*
**Superset PostgreSQL Database**"}
1==>|"Solution Composition"|11
12@{ shape: rect, label: "*Solution Component*
**Apache Superset**"}
12==>|"stores data [Solution Linking Wire]"|11
13@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
13==>|"stores data [Solution Linking Wire]"|1
8==>|"stores data [Solution Linking Wire]"|1
4==>|"stores data [Solution Linking Wire]"|1
12==>|"stores data [Solution Linking Wire]"|1
6==>|"stores data [Solution Linking Wire]"|1
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
click 11 "https://www.postgresql.org/" "Click for more documentation" _blank
click 1 "https://www.postgresql.org/" "Click for more documentation" _blank
click 12 "https://superset.apache.org/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 3 "https://www.postgresql.org/" "Click for more documentation" _blank
click 4 "https://www.unitycatalog.io/" "Click for more documentation" _blank
click 5 "https://www.postgresql.org/" "Click for more documentation" _blank
click 6 "https://airflow.apache.org/" "Click for more documentation" _blank
click 7 "https://www.postgresql.org/" "Click for more documentation" _blank
click 8 "https://marquezproject.ai/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/open-metadata-repository/" "Click for more documentation" _blank
```
> Egeria Workspaces PostgreSQL Server: Hosts relational databases for the Egeria Workspaces deployment. (Extracted from 6.0-SNAPSHOT)
