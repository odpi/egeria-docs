```mermaid
---
title: Components and Roles for Solution Blueprint - Bitol Content Pack [3e0f7f64-4563-471d-92d3-63e1cd9bc591]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: div-rect, label: "*Solution Component*
**Bitol Document Publisher**"}
3@{ shape: div-rect, label: "*Solution Component*
**Bitol Data Contract Cataloguer**"}
4@{ shape: lin-cyl, label: "*Solution Component*
**File System Directory**"}
5@{ shape: div-rect, label: "*Solution Component*
**Bitol Files Receiver**"}
6@{ shape: lin-cyl, label: "*Solution Component*
**Apache Kafka Topic**"}
7@{ shape: div-rect, label: "*Solution Component*
**Bitol Event Receiver**"}
8@{ shape: div-rect, label: "*Solution Component*
**Bitol Data Product Cataloguer**"}
9@{ shape: div-rect, label: "*Solution Component*
**Bitol File Store**"}
2==>|"distribute documents,
[Solution Linking Wire]"|9
7==>|"distribute documents,
[Solution Linking Wire]"|3
5==>|"distribute documents,
[Solution Linking Wire]"|3
5==>|"Catalog Resource,
[Solution Linking Wire]"|4
9==>|"Catalog Resource,
[Solution Linking Wire]"|4
5==>|"distribute documents,
[Solution Linking Wire]"|8
7==>|"distribute documents,
[Solution Linking Wire]"|9
7==>|"distribute documents,
[Solution Linking Wire]"|8
end
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
click 2 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/types/2/0220-Files-and-Folders/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 6 "https://kafka.apache.org/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
```
> Bitol Content Pack: Solution blueprint containing integration connectors for working with Bitol data contract (ODCS) and data product (ODPS) documents. (Extracted from 6.3-SNAPSHOT)
