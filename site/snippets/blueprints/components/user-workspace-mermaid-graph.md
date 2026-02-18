```mermaid
---
title: SolutionComponent - User Workspace [331875c2-0876-4211-bc52-b18f1e1bb478]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**User Workspace**"}
2@{ shape: rect, label: "*Solution Component*
**Jupyter Notebook File**"}
1==>|"Solution Composition"|2
3@{ shape: trap-t, label: "*Solution Actor Role*
**Python Programmer**"}
3==>|"writes python code for [Solution Component Actor]"|2
4@{ shape: rect, label: "*Solution Component*
**pyegeria**"}
2==>|"access metadata [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Markdown Document File**"}
1==>|"Solution Composition"|5
6@{ shape: rect, label: "*Solution Component*
**Dr.Egeria**"}
5==>|"read [Solution Linking Wire]"|6
6==>|"writes [Solution Linking Wire]"|5
7@{ shape: rect, label: "*Solution Component*
**Webpage File**"}
1==>|"Solution Composition"|7
6==>|"writes [Solution Linking Wire]"|7
8@{ shape: rect, label: "*Solution Component*
**Apache Web Server**"}
7==>|"read [Solution Linking Wire]"|8
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#FFE599, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
click 2 "https://jupyter.org/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/pyegeria/" "Click for more documentation" _blank
click 5 "https://en.wikipedia.org/wiki/Markdown" "Click for more documentation" _blank
click 7 "https://en.wikipedia.org/wiki/HTML" "Click for more documentation" _blank
click 8 "https://httpd.apache.org/" "Click for more documentation" _blank
```
> User Workspace: Directory on the file systems where a user can store their files. (Extracted from 6.0-SNAPSHOT)
