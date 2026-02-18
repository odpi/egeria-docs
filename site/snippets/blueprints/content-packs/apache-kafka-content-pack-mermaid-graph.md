```mermaid
---
title: SolutionBlueprint - Apache Kafka Content Pack [a3c6e079-3630-46e9-bf90-339c21964a4e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Blueprint*
**Apache Kafka Content Pack**"}
2@{ shape: rect, label: "*Solution Component*
**Apache Kafka Cataloguer**"}
1==>|"Collection Membership"|2
3@{ shape: rect, label: "*Solution Component*
**Configure Apache Kafka Server Cataloguer**"}
3==>|"configures [Solution Linking Wire]"|2
4@{ shape: rect, label: "*Solution Component*
**Apache Kafka Server**"}
2==>|"Catalog Resource [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
2==>|"metadata [Solution Linking Wire]"|5
6@{ shape: stadium, label: "*Integration Connector*
**KafkaTopicIntegrationConnector**"}
2==>|"Implemented By"|6
1==>|"Collection Membership"|3
7@{ shape: rect, label: "*Solution Component*
**Create and catalog Governance Action Process for Apache Kafka Server**"}
7==>|"step 2 [Solution Linking Wire]"|3
8@{ shape: tag-rect, label: "*Governance Action Type*
**catalog-apache-kafka-server (ApacheKafkaGovernance)**"}
3==>|"Implemented By"|8
9@{ shape: rect, label: "*Solution Component*
**Apache Kafka Topic**"}
1==>|"Collection Membership"|9
10@{ shape: rect, label: "*Solution Component*
**Delete with Template Governance Action Process for Apache Kafka Server**"}
1==>|"Collection Membership"|10
11@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
11==>|"delete Apache Kafka Server [Solution Component Actor]"|10
12@{ shape: rect, label: "*Solution Component*
**Delete Apache Kafka Server from Open Metadata**"}
10==>|"step 1 [Solution Linking Wire]"|12
13@{ shape: rect, label: "*Solution Component*
**Create Apache Kafka Server in Open Metadata**"}
1==>|"Collection Membership"|13
13==>|"metadata [Solution Linking Wire]"|5
7==>|"step 1 [Solution Linking Wire]"|13
14@{ shape: rect, label: "*Solution Component*
**Create and Survey Governance Action Process for Apache Kafka Server**"}
14==>|"step 1 [Solution Linking Wire]"|13
15@{ shape: tag-rect, label: "*Governance Action Type*
**create-apache-kafka-server (ApacheKafkaGovernance)**"}
13==>|"Implemented By"|15
1==>|"Collection Membership"|14
11==>|"requests survey [Solution Component Actor]"|14
16@{ shape: rect, label: "*Solution Component*
**Survey Apache Kafka Server**"}
14==>|"step 2 [Solution Linking Wire]"|16
17@{ shape: rect, label: "*Solution Component*
**Print Survey Report**"}
14==>|"step 3 [Solution Linking Wire]"|17
18@{ shape: stadium, label: "*Collection Membership*
**... plus 3 Items**"}
1-.->18
style 11 color:#000000, fill:#FFE599, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#dda0dd, stroke:#000000
style 15 color:#000000, fill:#53bbb4, stroke:#000000
style 16 color:#000000, fill:#dda0dd, stroke:#000000
style 17 color:#000000, fill:#dda0dd, stroke:#000000
style 18 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#bdb76b, stroke:#004563
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#53bbb4, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
click 12 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 13 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 14 "https://egeria-project.org/egeria-solutions/leveraging-apache-kafka/overview/" "Click for more documentation" _blank
click 4 "https://kafka.apache.org/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/egeria-solutions/leveraging-apache-kafka/overview/" "Click for more documentation" _blank
click 9 "https://kafka.apache.org/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/egeria-solutions/leveraging-apache-kafka/overview/" "Click for more documentation" _blank
```
> Apache Kafka Content Pack: Solution blueprint supporting integration connectors connecting to Apache Kafka. (Extracted from 6.0-SNAPSHOT)
