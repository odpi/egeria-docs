```mermaid
---
title: TeamMember - TeamMembers::Department::0003 [2e1d9684-3717-4d1e-9932-089146196abe]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::0003**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000006**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Clinical Trials Team (EU)**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
