```mermaid
---
title: SoftwareServer - qs-metadata-store on https://localhost:9443 [9f871549-1b82-45da-a146-319dd8164943]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Software Server*
**qs-metadata-store on https:/ /localhost:9443**"}
2@{ shape: card, label: "*Software Server [Template]*
**~ {serverName} ~**"}
1==>|"Sourced From"|2
3@{ shape: rounded, label: "*Endpoint*
**qs-metadata-store endpoint**"}
1==>|"Server Endpoint"|3
4@{ shape: hex, label: "*Software Server Platform*
**OMAG Server Platform**"}
1==>|"Deployed On"|4
5@{ shape: rounded, label: "*A P I Manager*
**Open Metadata Repository Access APIs**"}
1==>|"Supported Software Capability"|5
6@{ shape: rounded, label: "*Inventory Catalog*
**Local repository capability for server qs-metadata-store.**"}
1==>|"Supported Software Capability"|6
7@{ shape: rounded, label: "*Virtual Connection*
**qs-metadata-store connection**"}
1==>|"Asset Connection"|7
8@{ shape: rounded, label: "*Connection*
**qs-metadata-store secrets store connection**"}
7==>|"restAPIBearerToken [Embedded Connection]"|8
9@{ shape: rounded, label: "*Connector Type*
**YAML File Secrets Store Connector**"}
8==>|"Connection Connector Type"|9
10@{ shape: rounded, label: "*Endpoint*
**qs-metadata-store secret store endpoint**"}
8==>|"Connect To Endpoint"|10
11@{ shape: rounded, label: "*Connector Type*
**Metadata Access Server Connector**"}
7==>|"Connection Connector Type"|11
7==>|"Connect To Endpoint"|3
12@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
12==>|"running instance [Implemented By]"|1
style 11 color:#000000, fill:#39add1, stroke:#004563
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 2 color:#004563, fill:#b0e0e6, stroke:#004563
style 3 color:#000000, fill:#39add1, stroke:#004563
style 4 color:#000000, fill:#BDB76B, stroke:#004563
style 5 color:#000000, fill:#39add1, stroke:#004563
style 6 color:#000000, fill:#39add1, stroke:#004563
style 7 color:#000000, fill:#39add1, stroke:#004563
style 8 color:#000000, fill:#39add1, stroke:#004563
style 9 color:#000000, fill:#39add1, stroke:#004563
style 10 color:#000000, fill:#39add1, stroke:#004563
click 1 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/omag-server-platform/" "Click for more documentation" _blank
```
> qs-metadata-store on https://localhost:9443: A metadata store that supports Open Metadata Access Services (OMASs) with event notifications.  It provides metadata to qs-view-server, qs-engine-host and qs-integration-daemon. (Extracted from 6.0-SNAPSHOT)
