```mermaid
---
title: Team - Security [b698d847-193b-44c6-9c24-9abc7f94d8ca]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team*
**Security**"}
2@{ shape: odd, label: "*Business Capability*
**Governance**"}
2==>|"Owner [Collection Membership]"|1
3@{ shape: trap-b, label: "*Team*
**Board**"}
3==>|"Team Structure"|1
4@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::0001**"}
4==>|"Leader [Assignment Scope]"|1
5@{ shape: trap-t, label: "*Person*
**Ivor Padlock**"}
4==>|"Person Role Appointment"|5
6@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::0001**"}
6==>|"Contributor [Assignment Scope]"|1
7@{ shape: trap-t, label: "*Person*
**ANON 000003**"}
6==>|"Person Role Appointment"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#C0C0C0, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
