```mermaid
---
title: Components and Roles for Solution Blueprint - Apache Atlas Content Pack [819a7239-f1dc-43af-8501-c7a551655373]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: subproc, label: "*Solution Component*
**Configure Apache Atlas Server Cataloguer**"}
3@{ shape: rect, label: "*Solution Component*
**Apache Atlas Server**"}
4@{ shape: subproc, label: "*Solution Component*
**Print Survey Report**"}
5@{ shape: subproc, label: "*Solution Component*
**Create Apache Atlas Server in Open Metadata**"}
6@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for Apache Atlas Server**"}
7@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for Apache Atlas Server**"}
8@{ shape: subproc, label: "*Solution Component*
**Delete Apache Atlas Server from Open Metadata**"}
9@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for Apache Atlas Server**"}
10@{ shape: div-rect, label: "*Solution Component*
**Apache Atlas Exchange**"}
11@{ shape: subproc, label: "*Solution Component*
**Survey an Apache Atlas Server**"}
2==>|"configures,
[Solution Linking Wire]"|10
6==>|"step 2,
[Solution Linking Wire]"|2
11==>|"works with,
[Solution Linking Wire]"|3
10==>|"Catalog Resource,
[Solution Linking Wire]"|3
9==>|"step 3,
[Solution Linking Wire]"|4
6==>|"step 1,
[Solution Linking Wire]"|5
9==>|"step 1,
[Solution Linking Wire]"|5
12@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
12==>|"requests catalog,
[Solution Component Actor]"|6
12==>|"delete Apache Atlas Server,
[Solution Component Actor]"|7
7==>|"step 1,
[Solution Linking Wire]"|8
12==>|"requests survey,
[Solution Component Actor]"|9
9==>|"step 2,
[Solution Linking Wire]"|11
end
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 12 color:#000000, fill:#FFE599, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
click 11 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://atlas.apache.org/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/egeria-solutions/leveraging-apache-atlas/overview/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/egeria-solutions/leveraging-apache-atlas/overview/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/egeria-solutions/leveraging-apache-atlas/overview/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
```
> Apache Atlas Content Pack: Solution blueprint supporting integration connectors connecting to Apache Atlas. (Extracted from 6.0-SNAPSHOT)
