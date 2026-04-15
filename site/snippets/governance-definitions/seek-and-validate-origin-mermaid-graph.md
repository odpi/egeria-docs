```mermaid
---
title: GovernanceActionProcessStep - Seek and validate origin [0f8092b5-efb3-4442-9ad7-76d2078c4b46]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Governance Action Process Step*
**Seek and validate origin**"}
2@{ shape: rounded, label: "*Governance Action Process Step*
**Move Weekly Measurements File**"}
2==>|"Next Governance Action Process Step"|1
3@{ shape: rounded, label: "*Governance Action Process Step*
**Set retention period**"}
1==>|"Next Governance Action Process Step"|3
1==>|"Next Governance Action Process Step"|3
4@{ shape: rounded, label: "*Governance Action Engine*
**Asset Onboarding Engine**"}
1==>|"Governance Action Executor"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 3 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 4 color:#000000, fill:#39add1, stroke:#004563
```
