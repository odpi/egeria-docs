```mermaid
---
title: SolutionComponent - Survey Nested Files System Directories (Folders) and Files [9c38a6ca-4e0c-4d53-b517-6cdb78e46b35]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Survey Nested Files System Directories (Folders) and Files**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
1==>|"works with [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Report Type*
**Survey report produced by survey-all-folders-and-files (FileSurvey)**"}
1==>|"creates report [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for File System Directory**"}
6==>|"step 2 [Solution Linking Wire]"|1
7@{ shape: tag-rect, label: "*Governance Action Type*
**survey-all-folders-and-files (FileSurvey)**"}
1==>|"Implemented By"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DEB887, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#40E0D0, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/egeria-solutions/leveraging-files/overview/" "Click for more documentation" _blank
```
> Survey Nested Files System Directories (Folders) and Files: Starting from a particular directory, navigate through the hierarchy of nested directories in a file system and create a survey report that includes a description of each file encountered and a summary of the files found in each directory. (Extracted from 6.0-SNAPSHOT)
