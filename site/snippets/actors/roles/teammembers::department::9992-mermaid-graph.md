```mermaid
---
title: TeamMember - TeamMembers::Department::9992 [c8a1b488-8f05-4e06-a09b-eebc0d1f8167]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::9992**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000036**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Edmonton Site**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
