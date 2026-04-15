```mermaid
---
title: TeamMember - TeamMembers::Department::9993 [e720f93c-2731-47a0-9411-327c154ca03d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::9993**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000033**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Kansas City Site**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
