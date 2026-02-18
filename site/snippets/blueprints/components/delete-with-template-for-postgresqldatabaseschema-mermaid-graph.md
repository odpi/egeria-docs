```mermaid
---
title: SolutionComponent - Delete with Template Governance Action Process for PostgreSQL Relational Database Schema [1fa79d4f-7f60-49ad-8792-cbbc09b0a31e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Delete with Template Governance Action Process for PostgreSQL Relational Database Schema**"}
2@{ shape: rect, label: "*Solution Blueprint*
**PostgreSQL Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
3==>|"delete PostgreSQL Relational Database Schema [Solution Component Actor]"|1
4@{ shape: rect, label: "*Solution Component*
**Delete PostgreSQL Schema from Open Metadata**"}
1==>|"step 1 [Solution Linking Wire]"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Delete with Template Governance Action Process for PostgreSQL Relational Database Schema: Delete the asset for PostgreSQL Relational Database Schema using the same template properties that were used to create it.  This will delete all of the metadata anchored to the asset and relationships to other entities such as the catalog target relationships. (Extracted from 6.0-SNAPSHOT)
