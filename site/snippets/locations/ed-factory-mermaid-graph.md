```mermaid
---
title: Location - Edmonton Manufacturing Center [9c15e0b1-003b-44f1-b1ab-1dc8ea1cd933]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**Edmonton Manufacturing Center**"}
2@{ shape: circle, label: "*Location*
**Edmonton Site**"}
2==>|"Nested Location"|1
3@{ shape: trap-t, label: "*Location Owner*
**Edmonton Factory Leader**"}
3==>|"Assignment Scope"|1
4@{ shape: hex, label: "*Reference Data Value*
**Manufacturing Facility**"}
1==>|"Reference Value Assignment"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
