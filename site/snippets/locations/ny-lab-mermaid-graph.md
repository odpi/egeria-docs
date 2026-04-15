```mermaid
---
title: Location - Salk Cancer Research Laboratory [e1b42e4e-0ee3-4b08-9ef7-303be2a197f5]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**Salk Cancer Research Laboratory**"}
2@{ shape: circle, label: "*Location*
**New York Site**"}
2==>|"Nested Location"|1
3@{ shape: trap-t, label: "*Location Owner*
**New York Lab Leader**"}
3==>|"Assignment Scope"|1
4@{ shape: trap-t, label: "*Person*
**Tessa Tube**"}
3==>|"Person Role Appointment"|4
5@{ shape: hex, label: "*Reference Data Value*
**Research Laboratory**"}
1==>|"Reference Value Assignment"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
