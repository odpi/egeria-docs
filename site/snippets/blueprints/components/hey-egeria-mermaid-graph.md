```mermaid
---
title: SolutionComponent - hey_egeria [b2278203-63a6-4a4f-b142-6f75cd592415]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**hey_egeria**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Egeria Workspaces Servers Solution Blueprint**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**pyegeria**"}
1==>|"Solution Composition"|3
4@{ shape: rect, label: "*Solution Component*
**my_egeria**"}
4==>|"Solution Composition"|3
5@{ shape: rect, label: "*Solution Component*
**JupyterHub**"}
5==>|"Solution Composition"|3
6@{ shape: rect, label: "*Solution Component*
**Dr.Egeria**"}
6==>|"Solution Composition"|3
7@{ shape: rect, label: "*Solution Component*
**Pyegeria-Web**"}
7==>|"Solution Composition"|3
8@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
3==>|"access metadata [Solution Linking Wire]"|8
9@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 2 Items**"}
9-.->3
10@{ shape: rect, label: "*Solution Component*
**Load Archive**"}
1==>|"Solution Composition"|10
11@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
11==>|"calls [Solution Component Actor]"|10
12@{ shape: rect, label: "*Solution Component*
**Open Metadata Repository**"}
10==>|"load [Solution Linking Wire]"|12
13@{ shape: rect, label: "*Solution Component*
**Open Metadata Archive**"}
10==>|"reads [Solution Linking Wire]"|13
11==>|"interacts with [Solution Component Actor]"|1
14@{ shape: rect, label: "*Solution Component*
**View Server**"}
1==>|"access metadata [Solution Linking Wire]"|14
style 11 color:#000000, fill:#FFE599, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/user-interfaces/hey-egeria/overview/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/open-metadata-repository/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/open-metadata-archive/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/pyegeria/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/concepts/metadata-access-server/" "Click for more documentation" _blank
click 5 "https://jupyter.org/hub" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/open-metadata-archive/" "Click for more documentation" _blank
```
> hey_egeria: A user interface for working with Egeria and open metadata. (Extracted from 6.0-SNAPSHOT)
