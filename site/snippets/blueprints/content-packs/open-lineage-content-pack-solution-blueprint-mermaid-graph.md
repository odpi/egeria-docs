```mermaid
---
title: Components and Roles for Solution Blueprint - Open Lineage Content Pack [368cd66f-1250-491a-9da1-7f70f2963fd1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: div-rect, label: "*Solution Component*
**Open Lineage File Publisher**"}
3@{ shape: lin-cyl, label: "*Solution Component*
**File System Directory**"}
4@{ shape: div-rect, label: "*Solution Component*
**Open Lineage Cataloguer**"}
5@{ shape: das, label: "*Solution Component*
**Open Lineage Topic**"}
6@{ shape: div-rect, label: "*Solution Component*
**Open Lineage Kafka Listener**"}
7@{ shape: div-rect, label: "*Solution Component*
**Open Lineage API Publisher**"}
8@{ shape: das, label: "*Solution Component*
**Open Metadata Topic**"}
9@{ shape: div-rect, label: "*Solution Component*
**Open Lineage Governance Action Publisher**"}
10@{ shape: lin-cyl, label: "*Solution Component*
**Marquez Server**"}
11@{ shape: subproc, label: "*Solution Component*
**Summarise OpenLineage Data Quality**"}
12@{ shape: subproc, label: "*Solution Component*
**Set up Open Lineage Event capture**"}
13@{ shape: subproc, label: "*Solution Component*
**Profile OpenLineage Runs**"}
14@{ shape: subproc, label: "*Solution Component*
**Refine OpenLineage Data Scope**"}
15@{ shape: div-rect, label: "*Solution Component*
**Open Lineage Postgres Publisher**"}
16@{ shape: processes, label: "*Solution Component*
**Create and harvest Governance Action Process for Apache Kafka Topic**"}
17@{ shape: rect, label: "*Solution Component*
**Open Lineage Proxy**"}
6==>|"distribute events events,
[Solution Linking Wire]"|2
2==>|"Catalog Resource,
[Solution Linking Wire]"|3
6==>|"distribute events events,
[Solution Linking Wire]"|4
5==>|"receives events,
[Solution Linking Wire]"|6
17==>|"open lineage events,
[Solution Linking Wire]"|5
12==>|"configures,
[Solution Linking Wire]"|6
6==>|"distribute events events,
[Solution Linking Wire]"|7
6==>|"distribute events,
[Solution Linking Wire]"|15
7==>|"Catalog Resource,
[Solution Linking Wire]"|10
8==>|"distribute events events,
[Solution Linking Wire]"|9
16==>|"step 2,
[Solution Linking Wire]"|12
end
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#DDA0DD, stroke:#000000
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
click 11 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/egeria-solutions/leveraging-open-lineage/overview/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/features/lineage-management/overview/#egerias-open-lineage-support" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/open-metadata-topic-connector/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 10 "https://marquezproject.ai/" "Click for more documentation" _blank
```
> Open Lineage Content Pack: Solution blueprint containing integration connectors for working with open lineage events. (Extracted from 6.3-SNAPSHOT)
