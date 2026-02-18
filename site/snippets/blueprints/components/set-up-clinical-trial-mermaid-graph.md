```mermaid
---
title: SolutionComponent - Set up clinical trial [849b0b42-f465-452b-813c-477d6398e082]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Set up clinical trial**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Clinical Trial Management Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: trap-t, label: "*Actor Role*
**Clinical Trial Sponsor**"}
3==>|"Initiator [Solution Component Actor]"|1
4@{ shape: tag-rect, label: "*Governance Action Type*
**set-up-clinical-trial (ClinicalTrials@CocoPharmaceuticals)**"}
1==>|"Implementation Resource"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#53bbb4, stroke:#000000
```
> Set up clinical trial: Generates the project, and governance action processes needed to drive a clinical trial. (Extracted from V2.0)
