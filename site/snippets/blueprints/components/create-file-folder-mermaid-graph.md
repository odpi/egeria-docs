```mermaid
---
title: SolutionComponent - Create File Folder in Open Metadata [44ff46f1-50f8-443c-836e-78458123340f]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Create File Folder in Open Metadata**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for File System Directory**"}
3==>|"step 1 [Solution Linking Wire]"|1
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for File System Directory**"}
5==>|"step 1 [Solution Linking Wire]"|1
6@{ shape: tag-rect, label: "*Governance Action Type*
**create-file-folder (FileGovernance)**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
```
> Create File Folder in Open Metadata: Create a FileFolder asset in open metadata to represent a file system directory.  This is typically used to request a survey or the cataloguing of the files/nested directories within the directory. (Extracted from 6.0-SNAPSHOT)
