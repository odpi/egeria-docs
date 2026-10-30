```mermaid
---
title: SolutionBlueprint - Organization Insight Content Pack [b36c6cc7-26f2-4b9b-b3e3-496f738c8927]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Organization Insight Content Pack**"}
2@{ shape: rect, label: "*Collection Folder*
**Content Pack Contents**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Babbage Analytical Engine**"}
1==>|"Collection Membership"|3
4@{ shape: rect, label: "*Solution Component*
**Build Zone Membership Profile**"}
3==>|"schedules [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Summarise OpenLineage Data Quality**"}
3==>|"schedules [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Refine OpenLineage Data Scope**"}
3==>|"schedules [Solution Linking Wire]"|6
7@{ shape: rect, label: "*Solution Component*
**Build Member Popularity Profile**"}
3==>|"schedules [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Profile OpenLineage Runs**"}
3==>|"schedules [Solution Linking Wire]"|8
9@{ shape: stadium, label: "*Collection Membership*
**... plus 4 Items**"}
9-.->3
1==>|"Collection Membership"|4
10@{ shape: tag-rect, label: "*Governance Action Type*
**build-zone-membership-profile (EgeriaGovernance)**"}
4==>|"Implemented By"|10
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#8fbc8f, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#40E0D0, stroke:#000000
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Organization Insight Content Pack: Solution blueprint describing the components that deliver organization insight to the open metadata ecosystem. (Extracted from 6.3-SNAPSHOT)
