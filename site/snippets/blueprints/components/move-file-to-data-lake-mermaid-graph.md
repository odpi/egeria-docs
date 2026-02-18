```mermaid
---
title: SolutionComponent - Move File To Data Lake [18931474-d170-4394-97a9-0e627e2212ac]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Move File To Data Lake**"}
2@{ shape: rect, label: "*Solution Component*
**Weekly Measurements Onboarding Pipeline**"}
2==>|"Solution Composition"|1
3@{ shape: rect, label: "*Solution Component*
**Determine Origin of Data**"}
1==>|"provisioning complete [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Check Quality of Data**"}
1==>|"provisioning complete [Solution Linking Wire]"|4
5@{ shape: tag-rect, label: "*Governance Action Type*
**move-file (FileGovernance)**"}
1==>|"Implementation Resource"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
```
> Move File To Data Lake: Move landing area files to data lake, catalog files in data lake with lineage from the landing area and validate/certify that the data contains valid values.  The cataloguing includes lineage, retention, origin, governance zones.  The quality validation survey will add a certification to the file asset if the data contains valid values. (Extracted from V1.0)
