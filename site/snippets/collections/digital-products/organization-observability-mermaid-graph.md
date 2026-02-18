```mermaid
---
title: DigitalProductFamily - Organization Observability [2b404b02-47ad-4b28-9a41-0cc4708eb9b2]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Digital Product Family*
**Organization Observability**"}
2@{ shape: rect, label: "*Digital Product Family*
**Open Metadata Digital Products**"}
2==>|"Collection Membership"|1
3@{ shape: rounded, label: "*Community*
**Open Metadata Observability special interest group**"}
3==>|"Scoped By"|1
4@{ shape: trap-t, label: "*Digital Product Manager*
**Product Manager for Organization Observability**"}
4==>|"Owner [Assignment Scope]"|1
5@{ shape: doc, label: "*License Type*
**Personal Information**"}
1==>|"subscriber''s license [Governed By]"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#838cc7, stroke:#3079ab
style 3 color:#000000, fill:#39add1, stroke:#004563
style 4 color:#000000, fill:#FFE599, stroke:#000000
style 5 color:#FFFFFF, fill:#006400, stroke:#000000
```
> Organization Observability: Each product in this folder publishes insights about the activity of the organization observed through the open metadata ecosystem.  The latest insight is published to subscribers on a regular basis.  Subscribers can maintain a history of the insight publications, or treat each one as a trigger to perform specific processing. (Extracted from 6.0-SNAPSHOT)
