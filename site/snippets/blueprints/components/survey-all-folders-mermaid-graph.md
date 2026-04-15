```mermaid
---
title: SolutionComponent - Survey Nested Files System Directories (Folders) [b6c523a0-7318-4dd9-8b69-0e1e4aa08d1f]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Survey Nested Files System Directories (Folders)**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Files Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Report Type*
**Survey report produced by survey-all-folders (FileSurvey)**"}
1==>|"creates report [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**File System Directory**"}
1==>|"works with [Solution Linking Wire]"|5
6@{ shape: tag-rect, label: "*Governance Action Type*
**survey-all-folders (FileSurvey)**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DEB887, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#40E0D0, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
```
> Survey Nested Files System Directories (Folders): Starting from a particular directory, navigate through the hierarchy of nested directories in a file system and create a survey report that includes a summary of the files found in each directory. (Extracted from 6.0-SNAPSHOT)
