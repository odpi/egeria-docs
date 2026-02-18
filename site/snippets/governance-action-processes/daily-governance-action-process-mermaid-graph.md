```mermaid
---
title: GovernanceActionProcess - Daily Governance Action Process [dde1e255-6d0c-4589-b4a6-17e7d01db5ab]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Governance Action Process*
**Daily Governance Action Process**"}
2@{ shape: rounded, label: "*Governance Action Process Step*
**Get the day of the Week**"}
1==>|"Governance Action Process Flow"|2
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#FFFFFF, fill:#3079ab, stroke:#000000
click 1 "https://egeria-project.org/concepts/guard/" "Click for more documentation" _blank
```
> Daily Governance Action Process: Determines which day of the week it is today, and puts out a message on the audit log matching the assigned task for the day of the week. (Extracted from 6.0-SNAPSHOT)
