```mermaid
---
title: SolutionComponent - Survey Apache Kafka Server [4b8e9b5d-d095-43ac-a1d0-61155ea6f1b1]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Survey Apache Kafka Server**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Apache Kafka Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Apache Kafka Server**"}
1==>|"works with [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for Apache Kafka Server**"}
5==>|"step 2 [Solution Linking Wire]"|1
6@{ shape: tag-rect, label: "*Governance Action Type*
**survey-kafka-server (ApacheKafkaSurvey)**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://kafka.apache.org/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/egeria-solutions/leveraging-apache-kafka/overview/" "Click for more documentation" _blank
```
> Survey Apache Kafka Server: Connects to an Apache Kafka server (broker) and create a survey report that lists the topics being managed. (Extracted from 6.0-SNAPSHOT)
