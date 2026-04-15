```mermaid
---
title: TeamMember - TeamMembers::Department::0001 [17c5ab26-ca5f-48c6-8dbe-ed3aaf0d6df9]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::0001**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000003**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Security**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
