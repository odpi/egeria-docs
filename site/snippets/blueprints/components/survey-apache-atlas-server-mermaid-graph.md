```mermaid
---
title: SolutionComponent - Survey an Apache Atlas Server [892eb723-0bca-4f1e-b999-95604555f6f1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Survey an Apache Atlas Server**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Apache Atlas Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for Apache Atlas Server**"}
4==>|"step 2 [Solution Linking Wire]"|1
5@{ shape: rect, label: "*Solution Component*
**Apache Atlas Server**"}
1==>|"works with [Solution Linking Wire]"|5
6@{ shape: tag-rect, label: "*Governance Action Type*
**survey-apache-atlas-server (ApacheAtlasSurvey)**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-apache-atlas/overview/" "Click for more documentation" _blank
click 5 "https://atlas.apache.org/" "Click for more documentation" _blank
```
> Survey an Apache Atlas Server: Connect to a requested Apache Atlas server and create a survey report that describes the types and numbers of associated metadata instances stored. (Extracted from 6.0-SNAPSHOT)
