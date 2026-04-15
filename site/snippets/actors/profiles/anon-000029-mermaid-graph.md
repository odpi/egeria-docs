```mermaid
---
title: Person - ANON 000029 [e73da093-04e8-43af-9a46-2f78dfdeed78]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Person*
**ANON 000029**"}
2@{ shape: bow-rect, label: "*User Identity*
**ANON 000029**"}
1==>|"Profile Identity"|2
3@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::0016**"}
3==>|"Person Role Appointment"|1
4@{ shape: trap-b, label: "*Team*
**Winchester Manufacturing Office**"}
3==>|"Contributor [Assignment Scope]"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
```
