```mermaid
---
title: TeamMember - TeamMembers::Department::0005 [d180158a-d085-457a-942b-df8d1f35f260]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Team Member*
**TeamMembers::Department::0005**"}
2@{ shape: trap-t, label: "*Person*
**ANON 000009**"}
1==>|"Person Role Appointment"|2
3@{ shape: trap-b, label: "*Team*
**Amsterdam Depot**"}
1==>|"Contributor [Assignment Scope]"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
```
