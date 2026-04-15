```mermaid
---
title: Person - Terri Daring [8abb58a3-288d-44ea-88c3-8c4951d80f8c]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Person*
**Terri Daring**"}
2@{ shape: bow-rect, label: "*User Identity*
**terridaring**"}
1==>|"Profile Identity"|2
3@{ shape: rounded, label: "*Contact Details*
**Work Email Address**"}
1==>|"Contact Through"|3
4@{ shape: trap-t, label: "*Location Owner*
**London Site Leader**"}
4==>|"Person Role Appointment"|1
5@{ shape: circle, label: "*Location*
**London Site**"}
4==>|"Assignment Scope"|5
6@{ shape: trap-t, label: "*Community*
**Sustainability Community**"}
4==>|"Contributor [Assignment Scope]"|6
7@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::9999**"}
7==>|"Person Role Appointment"|1
8@{ shape: trap-b, label: "*Team*
**Founders Team**"}
7==>|"Leader [Assignment Scope]"|8
9@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::5656**"}
9==>|"Person Role Appointment"|1
10@{ shape: trap-b, label: "*Team*
**Nightingale Lab Team**"}
9==>|"Leader [Assignment Scope]"|10
11@{ shape: trap-t, label: "*Team Leader*
**TeamLeader::Department::4302**"}
11==>|"Person Role Appointment"|1
12@{ shape: trap-b, label: "*Team*
**Board**"}
11==>|"Leader [Assignment Scope]"|12
13@{ shape: trap-t, label: "*Community Member*
**Community Member of Data Science special interest group**"}
13==>|"Person Role Appointment"|1
14@{ shape: trap-t, label: "*Community*
**Data Science special interest group**"}
13==>|"Contributor [Assignment Scope]"|14
15@{ shape: trap-t, label: "*Location Owner*
**London Lab Leader**"}
15==>|"Person Role Appointment"|1
15==>|"Contributor [Assignment Scope]"|6
16@{ shape: circle, label: "*Location*
**Nightingale Cancer Research Laboratory**"}
15==>|"Assignment Scope"|16
17@{ shape: stadium, label: "*Person Role Appointment*
**... plus 1 Items**"}
17-.->1
style 11 color:#000000, fill:#FFE599, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 13 color:#000000, fill:#FFE599, stroke:#000000
style 14 color:#000000, fill:#FFE599, stroke:#000000
style 15 color:#000000, fill:#FFE599, stroke:#000000
style 16 color:#000000, fill:#FFD700, stroke:#000000
style 17 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#39add1, stroke:#004563
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#000000, fill:#FFD700, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#000000, fill:#FFE599, stroke:#000000
style 8 color:#000000, fill:#FFE599, stroke:#000000
style 9 color:#000000, fill:#FFE599, stroke:#000000
style 10 color:#000000, fill:#FFE599, stroke:#000000
```
