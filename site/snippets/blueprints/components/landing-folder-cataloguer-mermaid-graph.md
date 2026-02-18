```mermaid
---
title: SolutionComponent - Landing Folder Cataloguer [07705e15-efff-4f80-8992-f04ac85e0ef1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Landing Folder Cataloguer**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Clinical Trial Management Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Weekly Measurements Onboarding Pipeline**"}
1==>|"request onboarding [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Hospital Landing Area Folder**"}
4==>|"detect new files [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
```
> Landing Folder Cataloguer: Integration connector that is cataloguing files arriving in the hospital landing area folders and invoking the onboarding pipeline. (Extracted from V1.0)
