```mermaid
---
title: SolutionComponent - Daily Governance Action Process [2198d833-4725-4081-a41c-155316887a17]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Daily Governance Action Process**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Core Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
3==>|"requests daily process [Solution Component Actor]"|1
4@{ shape: rect, label: "*Solution Component*
**Get Day of the Week**"}
1==>|"step 1 [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Write to Audit Log**"}
1==>|"step 2 [Solution Linking Wire]"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/concepts/guard/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Daily Governance Action Process: Determines which day of the week it is today, and puts out a message on the audit log matching the assigned task for the day of the week. (Extracted from 6.0-SNAPSHOT)
