```mermaid
---
title: SolutionComponent - Check Quality of Data [2a5763d0-c540-4a59-8268-db7c88342269]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Check Quality of Data**"}
2@{ shape: rect, label: "*Solution Component*
**Weekly Measurements Onboarding Pipeline**"}
2==>|"Solution Composition"|1
3@{ shape: rect, label: "*Solution Component*
**Report Quality Issues**"}
1==>|"quality analysis complete [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Move File To Data Lake**"}
4==>|"provisioning complete [Solution Linking Wire]"|1
5@{ shape: tag-rect, label: "*Governance Action Type*
**check-weekly-measurements-data-quality (AssetQuality@CocoPharmaceuticals)**"}
1==>|"Implementation Resource"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
```
> Check Quality of Data: Validate that the data contains valid values. The quality validation survey will add a certification to the file asset if the data contains valid values. (Extracted from V1.0)
