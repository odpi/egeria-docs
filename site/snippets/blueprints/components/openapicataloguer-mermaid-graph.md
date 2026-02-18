```mermaid
---
title: SolutionComponent - Open API Cataloguer [22bcb015-84ab-4503-9619-231896c33828]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Open API Cataloguer**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Open APIs Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**OMAG Server Platform**"}
1==>|"Catalog Resource [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|4
5@{ shape: stadium, label: "*Integration Connector*
**OpenAPIIntegrationConnector**"}
1==>|"Implemented By"|5
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Open API Cataloguer: Maintains open metadata descriptions of Open API specification extracted from a running application/server/platform. (Extracted from 6.0-SNAPSHOT)
