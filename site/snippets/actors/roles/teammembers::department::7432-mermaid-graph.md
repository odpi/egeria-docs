```mermaid
---
title: TeamMember - TeamMembers::Department::7432 [22147f5b-f9af-43c6-882a-351f799ddb72]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::7432**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000013**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-t, label: "*Person*
**Erin Overview**"}
1==>|"Person Role Appointment"|3
4@{ shape: trap-t, label: "*Person*
**Peter Profile**"}
1==>|"Person Role Appointment"|4
5@{ shape: trap-b, label: "*Team*
**Chief Data Office**"}
1==>|"Contributor [Assignment Scope]"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
```
