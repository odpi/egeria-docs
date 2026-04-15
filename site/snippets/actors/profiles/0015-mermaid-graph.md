```mermaid
---
title: Team - Winchester Manufacturing Office [9e81727c-db51-4ab5-ad2d-8461a457ad88]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team*
**Winchester Manufacturing Office**"}
2@{ shape: odd, label: "*Business Capability*
**Manufacturing**"}
2==>|"Owner [Collection Membership]"|1
3@{ shape: trap-b, label: "*Team*
**Winchester Site**"}
3==>|"Team Structure"|1
4@{ shape: trap-b, label: "*Team*
**Winchester Manufacturing Office**"}
1==>|"Team Structure"|4
5@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::0015**"}
5==>|"Contributor [Assignment Scope]"|1
6@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::0015**"}
6==>|"Leader [Assignment Scope]"|1
7@{ shape: trap-t, label: "*Person*
**Stew Faster**"}
6==>|"Person Role Appointment"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#C0C0C0, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
