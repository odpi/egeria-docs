```mermaid
---
title: Location - Edmonton Office [d04d609e-cbef-428d-a7a5-3df437fc2eb0]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**Edmonton Office**"}
2@{ shape: circle, label: "*Location*
**Edmonton Site**"}
2==>|"Nested Location"|1
3@{ shape: trap-t, label: "*Location Owner*
**Edmonton Office Leader**"}
3==>|"Assignment Scope"|1
4@{ shape: hex, label: "*Reference Data Value*
**Office**"}
1==>|"Reference Value Assignment"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
