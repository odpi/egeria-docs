```mermaid
---
title: Team - Clinical Trials Team (EU) [b48f0f9c-e036-4c9b-afd5-10ef22e42e56]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team*
**Clinical Trials Team (EU)**"}
2@{ shape: odd, label: "*Business Capability*
**Clinical Trials**"}
2==>|"Owner [Collection Membership]"|1
3@{ shape: trap-b, label: "*Team*
**Amsterdam Site**"}
3==>|"Team Structure"|1
4@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::0003**"}
4==>|"Leader [Assignment Scope]"|1
5@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::0003**"}
5==>|"Contributor [Assignment Scope]"|1
6@{ shape: trap-t, label: "*Person*
**ANON 000006**"}
5==>|"Person Role Appointment"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#C0C0C0, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
```
