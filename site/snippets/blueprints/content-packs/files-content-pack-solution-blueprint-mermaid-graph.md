```mermaid
---
title: Components and Roles for Solution Blueprint - Files Content Pack [d89b489d-9661-41ee-838f-37454ebb70bf]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Copy File**"}
3@{ shape: subproc, label: "*Solution Component*
**Survey File System Directory**"}
4@{ shape: div-rect, label: "*Solution Component*
**Secrets Store Monitor**"}
5@{ shape: subproc, label: "*Solution Component*
**Create File Folder in Open Metadata**"}
6@{ shape: subproc, label: "*Solution Component*
**Survey Data File**"}
7@{ shape: subproc, label: "*Solution Component*
**Survey File System Directory and its Files**"}
8@{ shape: subproc, label: "*Solution Component*
**Create Data Folder in Open Metadata**"}
9@{ shape: lin-cyl, label: "*Solution Component*
**CSV Data File**"}
10@{ shape: lin-cyl, label: "*Solution Component*
**File**"}
11@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for Data Folder**"}
12@{ shape: subproc, label: "*Solution Component*
**Watch for new Files in Directory (folder)**"}
13@{ shape: div-rect, label: "*Solution Component*
**Content Packs Monitor**"}
14@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for File System Directory**"}
15@{ shape: subproc, label: "*Solution Component*
**Configure the File Folder Cataloguer**"}
16@{ shape: div-rect, label: "*Solution Component*
**Maintain DataFolder's storeUpdateTime**"}
17@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for Data Folder**"}
18@{ shape: subproc, label: "*Solution Component*
**Delete File Folder from Open Metadata**"}
19@{ shape: subproc, label: "*Solution Component*
**Delete Data Folder from Open Metadata**"}
20@{ shape: subproc, label: "*Solution Component*
**Survey CSV File**"}
21@{ shape: subproc, label: "*Solution Component*
**Move File**"}
22@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for File System Directory**"}
23@{ shape: subproc, label: "*Solution Component*
**Survey Nested Files System Directories (Folders)**"}
24@{ shape: div-rect, label: "*Solution Component*
**Sample Data Files Monitor**"}
25@{ shape: subproc, label: "*Solution Component*
**Print Survey Report**"}
26@{ shape: subproc, label: "*Solution Component*
**Configure the Data Folder Cataloguer**"}
27@{ shape: subproc, label: "*Solution Component*
**Delete File**"}
28@{ shape: subproc, label: "*Solution Component*
**Survey Nested Files System Directories (Folders) and Files**"}
29@{ shape: div-rect, label: "*Solution Component*
**Catalog Files in Directory (Folder)**"}
30@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for File System Directory**"}
31@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for File System Directory**"}
32@{ shape: lin-cyl, label: "*Solution Component*
**File System Directory**"}
2==>|"works with,
[Solution Linking Wire]"|32
3==>|"works with,
[Solution Linking Wire]"|32
4==>|"Catalog Resource,
[Solution Linking Wire]"|32
31==>|"step 1,
[Solution Linking Wire]"|5
22==>|"step 1,
[Solution Linking Wire]"|5
6==>|"works with,
[Solution Linking Wire]"|10
7==>|"works with,
[Solution Linking Wire]"|32
11==>|"step 2,
[Solution Linking Wire]"|7
14==>|"step 1,
[Solution Linking Wire]"|8
11==>|"step 1,
[Solution Linking Wire]"|8
20==>|"works with,
[Solution Linking Wire]"|9
27==>|"works with,
[Solution Linking Wire]"|10
25==>|"works with,
[Solution Linking Wire]"|10
11==>|"step 3,
[Solution Linking Wire]"|25
13==>|"Catalog Resource,
[Solution Linking Wire]"|32
14==>|"step 2,
[Solution Linking Wire]"|26
22==>|"step 2,
[Solution Linking Wire]"|15
15==>|"configures,
[Solution Linking Wire]"|29
17==>|"step 1,
[Solution Linking Wire]"|19
30==>|"step 1,
[Solution Linking Wire]"|18
21==>|"works with,
[Solution Linking Wire]"|32
23==>|"works with,
[Solution Linking Wire]"|32
24==>|"Catalog Resource,
[Solution Linking Wire]"|32
31==>|"step 3,
[Solution Linking Wire]"|25
26==>|"configures,
[Solution Linking Wire]"|29
28==>|"works with,
[Solution Linking Wire]"|32
31==>|"step 2,
[Solution Linking Wire]"|28
29==>|"Catalog Resource,
[Solution Linking Wire]"|32
end
style 22 color:#000000, fill:#DDA0DD, stroke:#000000
style 23 color:#000000, fill:#DDA0DD, stroke:#000000
style 24 color:#000000, fill:#DDA0DD, stroke:#000000
style 25 color:#000000, fill:#DDA0DD, stroke:#000000
style 26 color:#000000, fill:#DDA0DD, stroke:#000000
style 27 color:#000000, fill:#DDA0DD, stroke:#000000
style 28 color:#000000, fill:#DDA0DD, stroke:#000000
style 29 color:#000000, fill:#DDA0DD, stroke:#000000
style 30 color:#000000, fill:#DDA0DD, stroke:#000000
style 31 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
style 32 color:#000000, fill:#DDA0DD, stroke:#000000
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#DDA0DD, stroke:#000000
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#DDA0DD, stroke:#000000
style 19 color:#000000, fill:#DDA0DD, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 20 color:#000000, fill:#DDA0DD, stroke:#000000
style 21 color:#000000, fill:#DDA0DD, stroke:#000000
click 22 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 23 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 24 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 25 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 26 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 27 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 28 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 29 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 30 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 31 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 32 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 11 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 18 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 20 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 21 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Files Content Pack: Solution blueprint containing integration connectors for working with files. (Extracted from 6.3-SNAPSHOT)
