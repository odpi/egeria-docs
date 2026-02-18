```mermaid
---
title: SolutionComponent - Metadata Access Store [74385479-73a1-4e61-9c2f-a98be526acc7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Metadata Access Store**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Organization Insight Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Blueprint*
**Open APIs Content Pack**"}
3==>|"Collection Membership"|1
4@{ shape: rect, label: "*Solution Blueprint*
**Open Lineage Content Pack**"}
4==>|"Collection Membership"|1
5@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Products Content Pack**"}
5==>|"Collection Membership"|1
6@{ shape: rect, label: "*Solution Blueprint*
**Egeria Default Runtime Solution Blueprint**"}
6==>|"Collection Membership"|1
7@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
7==>|"Collection Membership"|1
8@{ shape: stadium, label: "*Collection Membership*
**... plus 1 Items**"}
8-.->1
9@{ shape: rect, label: "*Solution Component*
**Open Metadata Repository**"}
1==>|"Solution Composition"|9
10@{ shape: rect, label: "*Solution Component*
**Egeria PostgreSQL Database**"}
10==>|"Solution Composition"|9
11@{ shape: rect, label: "*Solution Component*
**Load Archive**"}
11==>|"load [Solution Linking Wire]"|9
1==>|"stores data [Solution Linking Wire]"|9
12@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
12==>|"Solution Composition"|1
13@{ shape: rect, label: "*Solution Component*
**Create New Product Subscription**"}
13==>|"metadata [Solution Linking Wire]"|1
14@{ shape: rect, label: "*Solution Component*
**Open Lineage Cataloguer**"}
14==>|"metadata [Solution Linking Wire]"|1
15@{ shape: rect, label: "*Solution Component*
**Move File**"}
15==>|"metadata [Solution Linking Wire]"|1
16@{ shape: rect, label: "*Solution Component*
**Babbage Analytical Engine**"}
16==>|"metadata [Solution Linking Wire]"|1
17@{ shape: rect, label: "*Solution Component*
**Create PostgreSQL Schema in Open Metadata**"}
17==>|"metadata [Solution Linking Wire]"|1
18@{ shape: rect, label: "*Solution Component*
**Delete OMAG Server Platform from Open Metadata**"}
18==>|"metadata [Solution Linking Wire]"|1
19@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 74 Items**"}
19-.->1
20@{ shape: hex, label: "*Software Server*
**qs-metadata-store on https:/ /localhost:9443**"}
1==>|"running instance [Implemented By]"|20
21@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 74 Items**"}
21-.->1
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#dda0dd, stroke:#000000
style 15 color:#000000, fill:#dda0dd, stroke:#000000
style 16 color:#000000, fill:#dda0dd, stroke:#000000
style 17 color:#000000, fill:#dda0dd, stroke:#000000
style 18 color:#000000, fill:#dda0dd, stroke:#000000
style 19 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#f5fffa, stroke:#000000
style 4 color:#000000, fill:#f5fffa, stroke:#000000
style 5 color:#000000, fill:#f5fffa, stroke:#000000
style 6 color:#000000, fill:#f5fffa, stroke:#000000
style 7 color:#000000, fill:#f5fffa, stroke:#000000
style 8 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 20 color:#000000, fill:#bdb76b, stroke:#004563
style 10 color:#000000, fill:#dda0dd, stroke:#000000
style 21 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
click 11 "https://egeria-project.org/concepts/open-metadata-archive/" "Click for more documentation" _blank
click 1 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 18 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/open-metadata-repository/" "Click for more documentation" _blank
click 20 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Metadata Access Store: A server that provides access to one or more open metadata repositories. (Extracted from 6.0-SNAPSHOT)
