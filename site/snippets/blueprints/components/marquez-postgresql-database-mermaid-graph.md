```mermaid
---
title: SolutionComponent - Marquez PostgreSQL Database [3093e1c1-f4bf-4406-8c80-a252393f0071]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Marquez PostgreSQL Database**"}
2@{ shape: rect, label: "*Solution Component*
**Egeria Workspaces PostgreSQL Server**"}
2==>|"Solution Composition"|1
3@{ shape: rect, label: "*Solution Component*
**Marquez Server**"}
3==>|"stores data [Solution Linking Wire]"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://www.postgresql.org/" "Click for more documentation" _blank
click 2 "https://www.postgresql.org/" "Click for more documentation" _blank
click 3 "https://marquezproject.ai/" "Click for more documentation" _blank
```
> Marquez PostgreSQL Database: This database supports the catalog storage for Marquez. (Extracted from 6.0-SNAPSHOT)
