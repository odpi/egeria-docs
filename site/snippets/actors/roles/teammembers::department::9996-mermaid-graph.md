```mermaid
---
title: TeamMember - TeamMembers::Department::9996 [462f3b31-214d-4ccb-85d9-fcfc3714cfd2]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::9996**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000018**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**New York Site**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
