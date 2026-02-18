```mermaid
---
title: SolutionComponent - Create PostgreSQL Schema in Open Metadata [c9779e50-9585-4e65-9cd7-4bc00757fe97]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Create PostgreSQL Schema in Open Metadata**"}
2@{ shape: rect, label: "*Solution Blueprint*
**PostgreSQL Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for PostgreSQL Relational Database Schema**"}
4==>|"step 1 [Solution Linking Wire]"|1
5@{ shape: tag-rect, label: "*Governance Action Type*
**create-postgres-schema (PostgreSQLGovernance)**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
```
> Create PostgreSQL Schema in Open Metadata: Create an open metadata element that represents a PostgreSQL schema using the properties supplied on the request.  These properties are used to populate a standard template that includes the asset for the schema and the connection.  The tables and columns are not cataloged by this component. (Extracted from 6.0-SNAPSHOT)
