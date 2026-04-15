```mermaid
---
title: TeamMember - TeamMembers::Department::6877 [6dfa5c28-1b9c-47c5-b0b0-0df634fa80ef]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::6877**"}
2@{ shape: trap-t, label: "*Person*
**Sally Counter**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-t, label: "*Person*
**ANON 000015**"}
1==>|"Person Role Appointment"|3
4@{ shape: trap-b, label: "*Team*
**Accounts Team**"}
1==>|"Contributor [Assignment Scope]"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
```
