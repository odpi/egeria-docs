```mermaid
---
title: SolutionComponent - Onboard Hospital [e9c2f911-ffcb-40c6-aeee-8c4d43811576]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Onboard Hospital**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Clinical Trial Management Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: trap-t, label: "*Actor Role*
**Certified Data Engineer**"}
3==>|"Initiator [Solution Component Actor]"|1
4@{ shape: tag-rect, label: "*Governance Action Type*
**onboard-hospital (ClinicalTrials@CocoPharmaceuticals)**"}
1==>|"Implementation Resource"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#53bbb4, stroke:#000000
```
> Onboard Hospital: Set up the onboarding pipeline for a participating hospital.  This fails if the hospital is not certified. (Extracted from V1.0)
