```mermaid
---
title: Person - Peter Profile [2af4303f-cc9f-4179-b213-b835e745607a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Person*
**Peter Profile**"}
2@{ shape: bow-rect, label: "*User Identity*
**peterprofile**"}
1==>|"Profile Identity"|2
3@{ shape: rounded, label: "*Contact Details*
**Work Email Address**"}
1==>|"Contact Through"|3
4@{ shape: trap-t, label: "*Solution Owner*
**Sustainability Technology Lead**"}
4==>|"Person Role Appointment"|1
5@{ shape: trap-t, label: "*Community*
**Sustainability Community**"}
4==>|"Contributor [Assignment Scope]"|5
6@{ shape: trap-t, label: "*Team Member*
**TeamMembers::Department::7432**"}
6==>|"Person Role Appointment"|1
7@{ shape: trap-b, label: "*Team*
**Chief Data Office**"}
6==>|"Contributor [Assignment Scope]"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#39add1, stroke:#004563
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
```
