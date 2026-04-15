```mermaid
---
title: TeamMember - TeamMembers::Department::9997 [a6180cfe-e144-49a7-bf95-302d51899626]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::9997**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000010**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**London Site**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
