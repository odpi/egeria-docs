```mermaid
---
title: LocationOwner - London Data Center Leader [9f066cd2-d6b8-44c8-9d05-7c230d3c4f19]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Location Owner*
**London Data Center Leader**"}
2@{ shape: trap-t, label: "*Person*
**Gary Geeke**"}
1==>|"Person Role Appointment"|2
3@{ shape: circle, label: "*Location*
**London Data Centre**"}
1==>|"Assignment Scope"|3
4@{ shape: rounded, label: "*Community*
**Sustainability Community**"}
1==>|"Contributor [Assignment Scope]"|4
5@{ shape: doc, label: "*Governance Responsibility*
**Eliminate CFC/HFC Cooling Units**"}
1==>|"Governed By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FFE599, stroke:#000000
style 3 color:#000000, fill:#FFD700, stroke:#000000
style 4 color:#000000, fill:#39add1, stroke:#004563
style 5 color:#FFFFFF, fill:#006400, stroke:#000000
```
