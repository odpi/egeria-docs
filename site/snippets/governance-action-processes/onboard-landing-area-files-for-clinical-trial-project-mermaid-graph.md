```mermaid
---
title: GovernanceActionProcess - Onboard Landing Area Files For Clinical Trial Project [da0442bf-818f-406b-99dc-83b72605cc98]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Governance Action Process*
**Onboard Landing Area Files For Clinical Trial Project**"}
2@{ shape: rounded, label: "*Governance Action Process Step*
**Move Weekly Measurements File**"}
1==>|"Governance Action Process Flow"|2
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#FFFFFF, fill:#3079ab, stroke:#000000
```
> Onboard Landing Area Files For Clinical Trial Project: Ensures that new files added to the landing are correctly catalogued in the data lake.

This process performs the follow function:
     1) The physical file is moved to the data lake and renamed,
     2) A new asset is created for the new file,
     3) Lineage is created between the original file asset and the new file asset,
     4) The owner and origin are assigned,
     5) The governance zones are assigned to make the new asset visible to the research team. (Extracted from V1.0)
