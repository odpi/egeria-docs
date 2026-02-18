```mermaid
---
title: SolutionComponent - Set up Data Lake [fb32bef2-e79f-4893-b500-2e547f24d482]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Set up Data Lake**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Clinical Trial Management Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Weekly Measurements Data Lake Folder**"}
1==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Weekly Measurements Onboarding Pipeline**"}
4==>|"save new files [Solution Linking Wire]"|3
5@{ shape: rect, label: "*Solution Component*
**Populate Sandbox**"}
3==>|"read certified files [Solution Linking Wire]"|5
6@{ shape: trap-t, label: "*Actor Role*
**Certified Data Engineer**"}
6==>|"Initiator [Solution Component Actor]"|1
7@{ shape: tag-rect, label: "*Governance Action Type*
**set-up-data-lake (ClinicalTrials@CocoPharmaceuticals)**"}
1==>|"Implementation Resource"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#53bbb4, stroke:#000000
```
> Set up Data Lake: Set up the data stores for receiving data from the hospitals - this includes the file system directory and Unity Catalog Volume for incoming patient measurements, along with the data set collection for certified measurement files. (Extracted from V1.0)
