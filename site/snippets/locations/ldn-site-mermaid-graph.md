```mermaid
---
title: Location - London Site [c4e35bda-b5a3-4a00-8e89-081395c8bb95]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**London Site**"}
2@{ shape: circle, label: "*Location*
**Nightingale Cancer Research Laboratory**"}
1==>|"Nested Location"|2
3@{ shape: circle, label: "*Location*
**London Office**"}
1==>|"Nested Location"|3
4@{ shape: circle, label: "*Location*
**London Data Centre**"}
1==>|"Nested Location"|4
5@{ shape: trap-t, label: "*Location Owner*
**London Site Leader**"}
5==>|"Assignment Scope"|1
6@{ shape: trap-t, label: "*Person*
**Terri Daring**"}
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
