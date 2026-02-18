```mermaid
---
title: SolutionBlueprint - PostgreSQL Content Pack [9c0e55dc-96b4-42de-8cd8-e4b2e2b92a38]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**PostgreSQL Content Pack**"}
2@{ shape: rect, label: "*Solution Component*
**Survey PostgreSQL Database**"}
1==>|"Collection Membership"|2
3@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for PostgreSQL Relational Database**"}
3==>|"step 2 [Solution Linking Wire]"|2
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
2==>|"metadata [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**PostgreSQL Server**"}
2==>|"works with [Solution Linking Wire]"|5
6@{ shape: tag-rect, label: "*Governance Action Type*
**survey-postgres-database (PostgreSQLSurvey)**"}
2==>|"Implemented By"|6
7@{ shape: rect, label: "*Solution Component*
**Delete PostgreSQL Database from Open Metadata**"}
1==>|"Collection Membership"|7
7==>|"metadata [Solution Linking Wire]"|4
8@{ shape: rect, label: "*Solution Component*
**Delete with Template Governance Action Process for PostgreSQL Relational Database**"}
8==>|"step 1 [Solution Linking Wire]"|7
9@{ shape: tag-rect, label: "*Governance Action Type*
**delete-postgres-database (PostgreSQLGovernance)**"}
7==>|"Implemented By"|9
10@{ shape: rect, label: "*Solution Component*
**Create PostgreSQL Server asset in Open Metadata**"}
1==>|"Collection Membership"|10
10==>|"metadata [Solution Linking Wire]"|4
11@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for PostgreSQL Server**"}
11==>|"step 1 [Solution Linking Wire]"|10
12@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for PostgreSQL Server**"}
12==>|"step 1 [Solution Linking Wire]"|10
13@{ shape: tag-rect, label: "*Governance Action Type*
**create-postgres-server (PostgreSQLGovernance)**"}
10==>|"Implemented By"|13
14@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for PostgreSQL Relational Database Schema**"}
1==>|"Collection Membership"|14
15@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
15==>|"requests catalog [Solution Component Actor]"|14
16@{ shape: rect, label: "*Solution Component*
**Configure PostgreSQL Schema Cataloguer**"}
14==>|"step 2 [Solution Linking Wire]"|16
17@{ shape: rect, label: "*Solution Component*
**Create PostgreSQL Schema in Open Metadata**"}
14==>|"step 1 [Solution Linking Wire]"|17
18@{ shape: rect, label: "*Solution Component*
**Print Survey Report**"}
1==>|"Collection Membership"|18
19@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for Data Folder**"}
19==>|"step 3 [Solution Linking Wire]"|18
18==>|"metadata [Solution Linking Wire]"|4
20@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for File System Directory**"}
20==>|"step 3 [Solution Linking Wire]"|18
21@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for Databricks Unity Catalog Server**"}
21==>|"step 3 [Solution Linking Wire]"|18
22@{ shape: rect, label: "*Solution Component*
**File**"}
18==>|"works with [Solution Linking Wire]"|22
12==>|"step 3 [Solution Linking Wire]"|18
23@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 10 Items**"}
23-.->18
1==>|"Collection Membership"|12
15==>|"requests survey [Solution Component Actor]"|12
24@{ shape: rect, label: "*Solution Component*
**Survey a PostgreSQL Server**"}
12==>|"step 2 [Solution Linking Wire]"|24
25@{ shape: stadium, label: "*Collection Membership*
**... plus 17 Items**"}
1-.->25
style 22 color:#000000, fill:#dda0dd, stroke:#000000
style 23 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#dda0dd, stroke:#000000
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#dda0dd, stroke:#000000
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#53bbb4, stroke:#000000
style 14 color:#000000, fill:#dda0dd, stroke:#000000
style 15 color:#000000, fill:#FFE599, stroke:#000000
style 16 color:#000000, fill:#dda0dd, stroke:#000000
style 17 color:#000000, fill:#dda0dd, stroke:#000000
style 18 color:#000000, fill:#dda0dd, stroke:#000000
style 19 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#53bbb4, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#53bbb4, stroke:#000000
style 20 color:#000000, fill:#dda0dd, stroke:#000000
style 21 color:#000000, fill:#dda0dd, stroke:#000000
click 11 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 22 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 24 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 18 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 5 "https://www.postgresql.org/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/egeria-solutions/leveraging-postgres/overview/" "Click for more documentation" _blank
click 20 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 21 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
```
> PostgreSQL Content Pack: Solution blueprint supporting integration connectors connecting to PostgreSQL Servers. (Extracted from 6.0-SNAPSHOT)
