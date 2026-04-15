```mermaid
---
title: TeamMember - TeamMembers::Department::5656 [b8013841-b73a-409d-a0c4-7b3ab5a133f8]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::5656**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000011**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Nightingale Lab Team**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
