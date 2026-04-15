```mermaid
---
title: Location - Rosalind Franklin Factory [58ae74f3-efb3-4720-b86e-eea279c4cfa4]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**Rosalind Franklin Factory**"}
2@{ shape: circle, label: "*Location*
**Winchester Site**"}
2==>|"Nested Location"|1
3@{ shape: trap-t, label: "*Location Owner*
**Winchester Factory Leader**"}
3==>|"Assignment Scope"|1
4@{ shape: trap-t, label: "*Person*
**Stew Faster**"}
3==>|"Person Role Appointment"|4
5@{ shape: hex, label: "*Reference Data Value*
**Manufacturing Facility**"}
1==>|"Reference Value Assignment"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
