```mermaid
---
title: SolutionComponent - PostgreSQL Server Cataloguer [871d318b-5556-4d41-9552-6f0cbc7f411e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**PostgreSQL Server Cataloguer**"}
2@{ shape: rect, label: "*Solution Blueprint*
**PostgreSQL Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Configure PostgreSQL Server Cataloguer**"}
4==>|"configures [Solution Linking Wire]"|1
5@{ shape: rect, label: "*Solution Component*
**JDBC Database Cataloguer**"}
1==>|"handoff [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**PostgreSQL Server**"}
1==>|"Catalog Resource [Solution Linking Wire]"|6
7@{ shape: stadium, label: "*Integration Connector*
**PostgreSQLServerIntegrationConnector**"}
1==>|"Implemented By"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 6 "https://www.postgresql.org/" "Click for more documentation" _blank
```
> PostgreSQL Server Cataloguer: Maintains the open metadata elements that represent the databases in a PostgreSQL server.  Hands off the cataloguing of the schemas, tables and columns of each database to the ''PostgreSQL Database Cataloguer''. (Extracted from 6.0-SNAPSHOT)
