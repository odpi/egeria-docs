```mermaid
---
title: SolutionComponent - PostgreSQL Relational Database Schema [c6d87bb4-a663-4e6c-a009-537cd15fb763]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**PostgreSQL Relational Database Schema**"}
2@{ shape: rect, label: "*Solution Component*
**Harvest Surveys**"}
2==>|"Catalog Resource [Solution Linking Wire]"|1
3@{ shape: rect, label: "*Solution Component*
**Harvest Open Metadata**"}
3==>|"Catalog Resource [Solution Linking Wire]"|1
4@{ shape: rect, label: "*Solution Component*
**Harvest Activity**"}
4==>|"Catalog Resource [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
click 1 "https://www.postgresql.org/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
```
> PostgreSQL Relational Database Schema: A database schema hosted on a PostgreSQL relational database server capable of being called through a JDBC Driver. (Extracted from 6.0-SNAPSHOT)
