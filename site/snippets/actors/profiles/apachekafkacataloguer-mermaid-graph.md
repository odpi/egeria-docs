```mermaid
---
title: ITProfile - ApacheKafkaCataloguer [442f6b0f-dfd6-46f9-bbd7-ce02706682dd]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*I T Profile*
**ApacheKafkaCataloguer**"}
2@{ shape: bow-rect, label: "*User Identity*
**kafkacatnpa**"}
1==>|"Profile Identity"|2
3@{ shape: stadium, label: "*Integration Connector*
**KafkaTopicIntegrationConnector**"}
3==>|"I T Infrastructure Profile"|1
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#FF8C00, stroke:#000000
style 3 color:#000000, fill:#BDB76B, stroke:#004563
```
> ApacheKafkaCataloguer: Catalogs the topics found in Apache Kafka Servers attached as catalog targets. (Extracted from 6.0-SNAPSHOT)
