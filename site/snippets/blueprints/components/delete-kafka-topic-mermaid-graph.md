```mermaid
---
title: SolutionComponent - Delete an Apache Kafka Topic from Open Metadata [6546488f-d8a2-415d-9d03-6ab72ba14c40]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Delete an Apache Kafka Topic from Open Metadata**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Core Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Delete with Template Governance Action Process for Apache Kafka Topic**"}
4==>|"step 1 [Solution Linking Wire]"|1
5@{ shape: tag-rect, label: "*Governance Action Type*
**delete-kafka-topic (AssetOnboarding)**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-apache-kafka/overview/" "Click for more documentation" _blank
```
> Delete an Apache Kafka Topic from Open Metadata: Delete the asset from the metadata store. (Extracted from 6.0-SNAPSHOT)
