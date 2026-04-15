```mermaid
---
title: Location - Edmonton Site [756ec1ed-e7cd-45a5-887a-557a0c54945a]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location*
**Edmonton Site**"}
2@{ shape: circle, label: "*Location*
**Edmonton Office**"}
1==>|"Nested Location"|2
3@{ shape: circle, label: "*Location*
**Edmonton Data Centre**"}
1==>|"Nested Location"|3
4@{ shape: circle, label: "*Location*
**Edmonton Distribution Center**"}
1==>|"Nested Location"|4
5@{ shape: circle, label: "*Location*
**Edmonton Manufacturing Center**"}
1==>|"Nested Location"|5
6@{ shape: trap-t, label: "*Location Owner*
**Edmonton Site Leader**"}
6==>|"Assignment Scope"|1
7@{ shape: hex, label: "*Reference Data Value*
**Primary Site**"}
1==>|"Reference Value Assignment"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFD700, stroke:#000000
style 3 color:#000000, fill:#FFD700, stroke:#000000
style 4 color:#000000, fill:#FFD700, stroke:#000000
style 5 color:#000000, fill:#FFD700, stroke:#000000
style 6 color:#000000, fill:#FFE599, stroke:#000000
style 7 color:#bf4086, fill:#f2d9e7, stroke:#bf4086
```
