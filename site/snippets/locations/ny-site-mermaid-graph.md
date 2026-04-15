```mermaid
---
title: Location - New York Site [d1345380-39d1-445c-930e-e1ec60f12820]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**New York Site**"}
2@{ shape: circle, label: "*Location*
**New York Office**"}
1==>|"Nested Location"|2
3@{ shape: circle, label: "*Location*
**Salk Cancer Research Laboratory**"}
1==>|"Nested Location"|3
4@{ shape: circle, label: "*Location*
**New York Data Center**"}
1==>|"Nested Location"|4
5@{ shape: trap-t, label: "*Location Owner*
**New York Site Leader**"}
5==>|"Assignment Scope"|1
6@{ shape: trap-t, label: "*Person*
**Zach Now**"}
5==>|"Person Role Appointment"|6
7@{ shape: hex, label: "*Reference Data Value*
**Primary Site**"}
1==>|"Reference Value Assignment"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFD700, stroke:#000000
style 4 color:#000000, fill:#FFD700, stroke:#000000
style 5 color:#000000, fill:#FFE599, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
