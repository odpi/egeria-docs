```mermaid
---
title: Solution Component - Weekly Measurements Onboarding Pipeline [7f5dca65-50b4-4103-9ac7-3a406a09047a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: subproc, label: "*Solution Component*
**Weekly Measurements Onboarding Pipeline**"}
subgraph 2 [Subcomponents]
3@{ shape: subproc, label: "*Solution Component*
**Report Quality Issues**"}
4@{ shape: subproc, label: "*Solution Component*
**Determine Origin of Data**"}
5@{ shape: subproc, label: "*Solution Component*
**Move File To Data Lake**"}
6@{ shape: subproc, label: "*Solution Component*
**Check Quality of Data**"}
7@{ shape: subproc, label: "*Solution Component*
**Publish Asset**"}
8@{ shape: subproc, label: "*Solution Component*
**Set Retention Period**"}
3==>|"quality assessment complete,
[Solution Linking Wire]"|7
6==>|"quality analysis complete,
[Solution Linking Wire]"|3
4==>|"origin determined,
[Solution Linking Wire]"|8
5==>|"provisioning complete,
[Solution Linking Wire]"|4
5==>|"provisioning complete,
[Solution Linking Wire]"|6
8==>|"classifications assigned,
[Solution Linking Wire]"|7
end
1==>2
style 1 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#b0c4de, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
```
> Weekly Measurements Onboarding Pipeline: Move landing area files to data lake, catalog files in data lake with lineage from the landing area and validate/certify that the data contains valid values.  The cataloguing includes lineage, retention, origin, governance zones.  The quality validation survey will add a certification to the file asset if the data contains valid values. (Extracted from V1.0)
