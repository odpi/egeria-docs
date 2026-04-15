```mermaid
---
title: Team - Global Manufacturing Office [9303a3b7-193b-4c4c-878f-d1d54294aabb]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team*
**Global Manufacturing Office**"}
2@{ shape: odd, label: "*Business Capability*
**Manufacturing**"}
2==>|"Owner [Collection Membership]"|1
3@{ shape: trap-b, label: "*Team*
**Board**"}
3==>|"Team Structure"|1
4@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::4332**"}
4==>|"Leader [Assignment Scope]"|1
5@{ shape: trap-t, label: "*Person*
**Stew Faster**"}
4==>|"Person Role Appointment"|5
6@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::4332**"}
6==>|"Contributor [Assignment Scope]"|1
7@{ shape: trap-t, label: "*Person*
**ANON 000030**"}
6==>|"Person Role Appointment"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#C0C0C0, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
