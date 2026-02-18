```mermaid
---
title: SolutionComponent - Jacquard Digital Product Loom [3bd61f93-2aca-443d-84cf-330cd50a0c1d]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Jacquard Digital Product Loom**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open Metadata Digital Products Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|3
4@{ shape: stadium, label: "*Integration Connector*
**JacquardHarvesterIntegrationConnector**"}
1==>|"Implemented By"|4
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Jacquard Digital Product Loom: Defines and maintains digital products based on the content of the open metadata repositories.  These products are assembled into a digital product catalog along with a glossary and data dictionary.  This integration connector is started when the Open Metadata Digital Product Archive is loaded.  It is responsible for detecting opportunities for open metadata digital products, creating a catalog entry for them and then maintaining last update information in the product information.  This is used to drive the distribution of open metadata updates to subscribers. (Extracted from 6.0-SNAPSHOT)
