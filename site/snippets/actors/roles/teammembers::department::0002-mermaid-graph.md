```mermaid
---
title: TeamMember - TeamMembers::Department::0002 [488d722a-7653-4071-8dca-e78680acb535]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::0002**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000004**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Sales**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
