```mermaid
---
title: TeamMember - TeamMembers::Department::3067 [bd6d9bbf-7382-4338-831b-011a8fbfde61]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::3067**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000008**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**IT Operations Team**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
