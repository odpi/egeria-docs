```mermaid
---
title: SolutionComponent - Apache Airflow DAG [1687e842-6f66-4871-b844-3f96a9f4391f]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Apache Airflow DAG**"}
2@{ shape: rect, label: "*Solution Component*
**Apache Airflow Server**"}
2==>|"Solution Composition"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
click 1 "https://egeria-project.org/types/2/0215-Software-Components/" "Click for more documentation" _blank
click 2 "https://airflow.apache.org/" "Click for more documentation" _blank
```
> Apache Airflow DAG: A python component that implements a micro-workflow that runs in Apache Airflow.  DAG stands for Directed Acyclic Graph, which describes the structure of its implementation. (Extracted from 6.0-SNAPSHOT)
