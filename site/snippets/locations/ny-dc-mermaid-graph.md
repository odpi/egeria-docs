```mermaid
---
title: Location - New York Data Center [25a89c2c-cd5a-4091-851f-5da9203f9e1a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**New York Data Center**"}
2@{ shape: circle, label: "*Location*
**New York Site**"}
2==>|"Nested Location"|1
3@{ shape: trap-t, label: "*Location Owner*
**New York Data Center Leader**"}
3==>|"Assignment Scope"|1
4@{ shape: trap-t, label: "*Person*
**Gary Geeke**"}
3==>|"Person Role Appointment"|4
5@{ shape: hex, label: "*Reference Data Value*
**Data centre/center**"}
1==>|"Reference Value Assignment"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
