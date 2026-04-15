```mermaid
---
title: TeamMember - TeamMembers::Department::0008 [0bc622c3-16ca-4957-bbad-caf99a2f0baa]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::0008**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000017**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**London Information Technology Team**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
