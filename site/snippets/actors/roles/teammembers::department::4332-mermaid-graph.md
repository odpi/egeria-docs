```mermaid
---
title: TeamMember - TeamMembers::Department::4332 [73ba6338-186f-496a-9db7-e711cd48ddfd]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::4332**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000030**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Global Manufacturing Office**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
