```mermaid
---
title: SolutionBlueprint - Files Content Pack [d89b489d-9661-41ee-838f-37454ebb70bf]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Files Content Pack**"}
2@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
1==>|"Collection Membership"|2
3@{ shape: rect, label: "*Solution Component*
**File**"}
2==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Delete File**"}
4==>|"works with [Solution Linking Wire]"|3
5@{ shape: rect, label: "*Solution Component*
**Print Survey Report**"}
5==>|"works with [Solution Linking Wire]"|3
6@{ shape: rect, label: "*Solution Component*
**Survey Data File**"}
6==>|"works with [Solution Linking Wire]"|3
1==>|"Collection Membership"|3
7@{ shape: rect, label: "*Solution Component*
**Move File**"}
7==>|"works with [Solution Linking Wire]"|2
8@{ shape: rect, label: "*Solution Component*
**Survey File System Directory**"}
8==>|"works with [Solution Linking Wire]"|2
9@{ shape: rect, label: "*Solution Component*
**Survey Nested Files System Directories (Folders) and Files**"}
9==>|"works with [Solution Linking Wire]"|2
10@{ shape: rect, label: "*Solution Component*
**Copy File**"}
10==>|"works with [Solution Linking Wire]"|2
11@{ shape: rect, label: "*Solution Component*
**Catalog Files in Directory (Folder)**"}
11==>|"Catalog Resource [Solution Linking Wire]"|2
12@{ shape: rect, label: "*Solution Component*
**Open Lineage File Publisher**"}
12==>|"Catalog Resource [Solution Linking Wire]"|2
13@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 6 Items**"}
13-.->2
14@{ shape: rect, label: "*Solution Component*
**Survey CSV File**"}
1==>|"Collection Membership"|14
15@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
14==>|"metadata [Solution Linking Wire]"|15
16@{ shape: rect, label: "*Solution Component*
**CSV Data File**"}
14==>|"works with [Solution Linking Wire]"|16
17@{ shape: tag-rect, label: "*Governance Action Type*
**survey-csv-file (FileSurvey)**"}
14==>|"Implemented By"|17
1==>|"Collection Membership"|7
7==>|"metadata [Solution Linking Wire]"|15
18@{ shape: tag-rect, label: "*Governance Action Type*
**move-file (FileGovernance)**"}
7==>|"Implemented By"|18
19@{ shape: rect, label: "*Solution Component*
**Delete with Template Governance Action Process for Data Folder**"}
1==>|"Collection Membership"|19
20@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
20==>|"delete Data Folder [Solution Component Actor]"|19
21@{ shape: rect, label: "*Solution Component*
**Delete Data Folder from Open Metadata**"}
19==>|"step 1 [Solution Linking Wire]"|21
1==>|"Collection Membership"|9
9==>|"metadata [Solution Linking Wire]"|15
22@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for File System Directory**"}
22==>|"step 2 [Solution Linking Wire]"|9
23@{ shape: tag-rect, label: "*Governance Action Type*
**survey-all-folders-and-files (FileSurvey)**"}
9==>|"Implemented By"|23
24@{ shape: stadium, label: "*Collection Membership*
**... plus 24 Items**"}
1-.->24
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 22 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 23 color:#000000, fill:#53bbb4, stroke:#000000
style 13 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 24 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 14 color:#000000, fill:#dda0dd, stroke:#000000
style 15 color:#000000, fill:#dda0dd, stroke:#000000
style 16 color:#000000, fill:#dda0dd, stroke:#000000
style 17 color:#000000, fill:#53bbb4, stroke:#000000
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
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 20 color:#000000, fill:#FFE599, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
style 21 color:#000000, fill:#dda0dd, stroke:#000000
click 11 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 22 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 21 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Files Content Pack: Solution blueprint containing integration connectors for working with files. (Extracted from 6.0-SNAPSHOT)
