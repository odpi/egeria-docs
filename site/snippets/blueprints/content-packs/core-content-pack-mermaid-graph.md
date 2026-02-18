```mermaid
---
title: SolutionBlueprint - Core Content Pack [eb83f1a4-684b-4624-bdc8-6b394ce9cdc8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Core Content Pack**"}
2@{ shape: rect, label: "*Solution Component*
**JDBC Database Cataloguer**"}
1==>|"Collection Membership"|2
3@{ shape: rect, label: "*Solution Component*
**JDBC Relational Database**"}
2==>|"Catalog Resource [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**PostgreSQL Server**"}
2==>|"works with [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
2==>|"metadata [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Configure PostgreSQL Schema Cataloguer**"}
6==>|"configures [Solution Linking Wire]"|2
7@{ shape: rect, label: "*Solution Component*
**Configure PostgreSQL Database Cataloguer**"}
7==>|"configures [Solution Linking Wire]"|2
8@{ shape: rect, label: "*Solution Component*
**PostgreSQL Server Cataloguer**"}
8==>|"handoff [Solution Linking Wire]"|2
9@{ shape: stadium, label: "*Collection Membership*
**... plus 3 Items**"}
9-.->2
10@{ shape: rect, label: "*Solution Component*
**Qualified Name Deduplication**"}
1==>|"Collection Membership"|10
10==>|"metadata [Solution Linking Wire]"|5
11@{ shape: tag-rect, label: "*Governance Action Type*
**qualified-name-dedup (Stewardship)**"}
10==>|"Implemented By"|11
12@{ shape: rect, label: "*Solution Component*
**Provision Tabular Data Set**"}
1==>|"Collection Membership"|12
13@{ shape: rect, label: "*Solution Component*
**Tabular Data Set**"}
12==>|"works with [Solution Linking Wire]"|13
12==>|"metadata [Solution Linking Wire]"|5
14@{ shape: tag-rect, label: "*Governance Action Type*
**provision-tabular-data-set (EgeriaGovernance)**"}
12==>|"Implemented By"|14
15@{ shape: rect, label: "*Solution Component*
**Set Zone Membership**"}
1==>|"Collection Membership"|15
15==>|"metadata [Solution Linking Wire]"|5
16@{ shape: tag-rect, label: "*Governance Action Type*
**set-zone-membership (AssetOnboarding)**"}
15==>|"Implemented By"|16
17@{ shape: rect, label: "*Solution Component*
**Create a software server in Open Metadata**"}
1==>|"Collection Membership"|17
17==>|"metadata [Solution Linking Wire]"|5
18@{ shape: tag-rect, label: "*Governance Action Type*
**create-software-server (AssetOnboarding)**"}
17==>|"Implemented By"|18
1==>|"Collection Membership"|13
19@{ shape: rect, label: "*Solution Component*
**Data Asset**"}
13==>|"Solution Composition"|19
20@{ shape: rect, label: "*Solution Component*
**Digital Product Provisioning Pipeline**"}
20==>|"works with [Solution Linking Wire]"|13
21@{ shape: rect, label: "*Solution Component*
**Cancel Product Subscription**"}
21==>|"works with [Solution Linking Wire]"|13
22@{ shape: stadium, label: "*Collection Membership*
**... plus 16 Items**"}
1-.->22
style 11 color:#000000, fill:#53bbb4, stroke:#000000
style 22 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#53bbb4, stroke:#000000
style 15 color:#000000, fill:#dda0dd, stroke:#000000
style 16 color:#000000, fill:#53bbb4, stroke:#000000
style 17 color:#000000, fill:#dda0dd, stroke:#000000
style 18 color:#000000, fill:#53bbb4, stroke:#000000
style 19 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 20 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
style 21 color:#000000, fill:#dda0dd, stroke:#000000
click 12 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/tabular-data-set/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/concepts/asset/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://en.wikipedia.org/wiki/Java_Database_Connectivity" "Click for more documentation" _blank
click 4 "https://www.postgresql.org/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 20 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 21 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Core Content Pack: Solution blueprint for a default setup. (Extracted from 6.0-SNAPSHOT)
