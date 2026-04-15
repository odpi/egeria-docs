```mermaid
---
title: Team - Finance Team [d18a0983-d70d-4e8c-9edd-3704a15b655f]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team*
**Finance Team**"}
2@{ shape: odd, label: "*Business Capability*
**Finance**"}
2==>|"Owner [Collection Membership]"|1
3@{ shape: trap-b, label: "*Team*
**Board**"}
3==>|"Team Structure"|1
4@{ shape: trap-b, label: "*Team*
**Accounts Team**"}
1==>|"Team Structure"|4
5@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::6788**"}
5==>|"Leader [Assignment Scope]"|1
6@{ shape: trap-t, label: "*Person*
**Reggie Mint**"}
5==>|"Person Role Appointment"|6
7@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::6788**"}
7==>|"Contributor [Assignment Scope]"|1
8@{ shape: trap-t, label: "*Person*
**ANON 000014**"}
7==>|"Person Role Appointment"|8
9@{ shape: trap-t, label: "*Person*
**Tom Tally**"}
7==>|"Person Role Appointment"|9
10@{ shape: trap-t, label: "*Person*
**Sidney Seeker**"}
7==>|"Person Role Appointment"|10
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#C0C0C0, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#000000, fill:#FFE599, stroke:#000000
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
