```mermaid
---
title: Person - Polly Tasker [f609961b-071c-4362-94db-82974a1558bb]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Person*
**Polly Tasker**"}
2@{ shape: bow-rect, label: "*User Identity*
**pollytasker**"}
1==>|"Profile Identity"|2
3@{ shape: rounded, label: "*Contact Details*
**Work Email Address**"}
1==>|"Contact Through"|3
4@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::0004**"}
4==>|"Person Role Appointment"|1
5@{ shape: trap-b, label: "*Team*
**Global Information Technology Team**"}
4==>|"Contributor [Assignment Scope]"|5
6@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::3082**"}
6==>|"Person Role Appointment"|1
7@{ shape: trap-b, label: "*Team*
**Software Development and Testing Team**"}
6==>|"Leader [Assignment Scope]"|7
8@{ shape: trap-t, label: "*Governance Officer*
**Governance Officer for Software Development Assurance**"}
8==>|"Person Role Appointment"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#39add1, stroke:#004563
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
```
