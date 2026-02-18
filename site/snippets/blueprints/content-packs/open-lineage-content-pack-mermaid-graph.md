```mermaid
---
title: SolutionBlueprint - Open Lineage Content Pack [368cd66f-1250-491a-9da1-7f70f2963fd1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Open Lineage Content Pack**"}
2@{ shape: rect, label: "*Solution Component*
**Create and harvest Governance Action Process for Apache Kafka Topic**"}
1==>|"Collection Membership"|2
3@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
3==>|"requests harvest [Solution Component Actor]"|2
4@{ shape: rect, label: "*Solution Component*
**Set up Open Lineage Event capture**"}
2==>|"step 2 [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Create Apache Kafka Topic in Open Metadata**"}
2==>|"step 1 [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Open Lineage File Publisher**"}
1==>|"Collection Membership"|6
7@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
6==>|"Catalog Resource [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Open Lineage Kafka Listener**"}
8==>|"distribute events events [Solution Linking Wire]"|6
9@{ shape: stadium, label: "*Integration Connector*
**OpenLineageFilePublisherIntegrationConnector**"}
6==>|"Implemented By"|9
10@{ shape: rect, label: "*Solution Component*
**Marquez Server**"}
1==>|"Collection Membership"|10
11@{ shape: rect, label: "*Solution Component*
**Marquez PostgreSQL Database**"}
10==>|"stores data [Solution Linking Wire]"|11
12@{ shape: rect, label: "*Solution Component*
**Egeria Workspaces PostgreSQL Server**"}
10==>|"stores data [Solution Linking Wire]"|12
13@{ shape: rect, label: "*Solution Component*
**Open Lineage API Publisher**"}
13==>|"Catalog Resource [Solution Linking Wire]"|10
14@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Runtimes Solution Blueprint**"}
14==>|"Collection Membership"|10
15@{ shape: rect, label: "*Solution Component*
**Open Lineage Governance Action Publisher**"}
1==>|"Collection Membership"|15
16@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
15==>|"metadata [Solution Linking Wire]"|16
17@{ shape: rect, label: "*Solution Component*
**Open Metadata Topic**"}
17==>|"distribute events events [Solution Linking Wire]"|15
18@{ shape: stadium, label: "*Integration Connector*
**OpenLineageGovernanceActionPublisherIntegrationConnector**"}
15==>|"Implemented By"|18
1==>|"Collection Membership"|17
16==>|"metadata change notifications [Solution Linking Wire]"|17
19@{ shape: rect, label: "*Solution Component*
**Integration Daemon**"}
17==>|"metadata change notifications [Solution Linking Wire]"|19
20@{ shape: rect, label: "*Solution Component*
**Engine Host**"}
17==>|"metadata change notifications [Solution Linking Wire]"|20
21@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
21==>|"Collection Membership"|17
1==>|"Collection Membership"|8
8==>|"distribute events events [Solution Linking Wire]"|13
22@{ shape: rect, label: "*Solution Component*
**Open Lineage Topic**"}
22==>|"receives events [Solution Linking Wire]"|8
23@{ shape: rect, label: "*Solution Component*
**Open Lineage Cataloguer**"}
8==>|"distribute events events [Solution Linking Wire]"|23
4==>|"configures [Solution Linking Wire]"|8
24@{ shape: stadium, label: "*Implemented By*
**... plus 1 Items**"}
8-.->24
25@{ shape: stadium, label: "*Collection Membership*
**... plus 7 Items**"}
1-.->25
style 22 color:#000000, fill:#dda0dd, stroke:#000000
style 23 color:#000000, fill:#dda0dd, stroke:#000000
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 25 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#dda0dd, stroke:#000000
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#f5fffa, stroke:#000000
style 15 color:#000000, fill:#dda0dd, stroke:#000000
style 16 color:#000000, fill:#dda0dd, stroke:#000000
style 17 color:#000000, fill:#dda0dd, stroke:#000000
style 18 color:#000000, fill:#bdb76b, stroke:#004563
style 19 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#bdb76b, stroke:#004563
style 20 color:#000000, fill:#dda0dd, stroke:#000000
style 21 color:#000000, fill:#f5fffa, stroke:#000000
click 11 "https://www.postgresql.org/" "Click for more documentation" _blank
click 22 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 12 "https://www.postgresql.org/" "Click for more documentation" _blank
click 23 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/concepts/open-metadata-topic-connector/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/concepts/integration-daemon/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/egeria-solutions/leveraging-open-lineage/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 20 "https://egeria-project.org/concepts/engine-host/" "Click for more documentation" _blank
click 10 "https://marquezproject.ai/" "Click for more documentation" _blank
```
> Open Lineage Content Pack: Solution blueprint containing integration connectors for working with open lineage events. (Extracted from 6.0-SNAPSHOT)
