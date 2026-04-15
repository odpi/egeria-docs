```mermaid
---
title: BusinessCapability - Human Resources [0eb932ae-f7a4-4d39-b02b-ec3cec99ed0b]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Business Capability*
**Human Resources**"}
2@{ shape: trap-b, label: "*Team*
**Human Resources**"}
1==>|"Owner [Collection Membership]"|2
3@{ shape: trap-t, label: "*Governance Representative*
**HR Sustainability Champion**"}
3==>|"Assignment Scope"|1
4@{ shape: trap-t, label: "*Person*
**Faith Broker**"}
3==>|"Person Role Appointment"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
```
