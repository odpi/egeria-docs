```mermaid
---
title: SolutionComponent - Configure PostgreSQL Server Cataloguer [015d6b33-e6bc-4d77-822c-4a9d536ef542]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Configure PostgreSQL Server Cataloguer**"}
2@{ shape: rect, label: "*Solution Blueprint*
**PostgreSQL Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for PostgreSQL Server**"}
3==>|"step 2 [Solution Linking Wire]"|1
4@{ shape: rect, label: "*Solution Component*
**PostgreSQL Server Cataloguer**"}
1==>|"configures [Solution Linking Wire]"|4
5@{ shape: tag-rect, label: "*Governance Action Type*
**catalog-postgres-server (PostgreSQLGovernance)**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
```
> Configure PostgreSQL Server Cataloguer: Link the PostgreSQL server asset to the PostgreSQL Server cataloguer. (Extracted from 6.0-SNAPSHOT)
