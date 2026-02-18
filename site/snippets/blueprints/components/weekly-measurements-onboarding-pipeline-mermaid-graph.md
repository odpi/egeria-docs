```mermaid
---
title: SolutionComponent - Weekly Measurements Onboarding Pipeline [7f5dca65-50b4-4103-9ac7-3a406a09047a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Weekly Measurements Onboarding Pipeline**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Clinical Trial Management Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Report Quality Issues**"}
1==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**Publish Asset**"}
3==>|"quality assessment complete [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Check Quality of Data**"}
5==>|"quality analysis complete [Solution Linking Wire]"|3
6@{ shape: rect, label: "*Solution Component*
**Determine Origin of Data**"}
1==>|"Solution Composition"|6
7@{ shape: rect, label: "*Solution Component*
**Set Retention Period**"}
6==>|"origin determined [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Move File To Data Lake**"}
8==>|"provisioning complete [Solution Linking Wire]"|6
1==>|"Solution Composition"|8
8==>|"provisioning complete [Solution Linking Wire]"|5
1==>|"Solution Composition"|5
1==>|"Solution Composition"|4
7==>|"classifications assigned [Solution Linking Wire]"|4
1==>|"Solution Composition"|7
9@{ shape: trap-t, label: "*Actor Role*
**Clinical Trial Manager**"}
9==>|"Steward [Solution Component Actor]"|1
10@{ shape: trap-t, label: "*Actor Role*
**Certified Data Engineer**"}
10==>|"Steward [Solution Component Actor]"|1
11@{ shape: rect, label: "*Solution Component*
**Landing Folder Cataloguer**"}
11==>|"request onboarding [Solution Linking Wire]"|1
12@{ shape: rect, label: "*Solution Component*
**Weekly Measurements Data Lake Folder**"}
1==>|"save new files [Solution Linking Wire]"|12
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#FFE599, stroke:#000000
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
> Weekly Measurements Onboarding Pipeline: Move landing area files to data lake, catalog files in data lake with lineage from the landing area and validate/certify that the data contains valid values.  The cataloguing includes lineage, retention, origin, governance zones.  The quality validation survey will add a certification to the file asset if the data contains valid values. (Extracted from V1.0)
