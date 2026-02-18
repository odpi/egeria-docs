```mermaid
---
title: SolutionComponent - Unity Catalog Asset Exchange [0102f808-2ee3-42d4-a769-95c891517876]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Unity Catalog Asset Exchange**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Unity Catalog Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Unity Catalog Server**"}
1==>|"Catalog Resource [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Unity Catalog Server Exchange**"}
4==>|"handoff [Solution Linking Wire]"|1
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|5
6@{ shape: stadium, label: "*Integration Connector*
**UnityCatalogAssetExchange**"}
1==>|"Implemented By"|6
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Unity Catalog Asset Exchange: Exchanges the metadata found in a Unity Catalog Catalog with the open metadata ecosystem.  The open metadata ecosystem can provide enrichment of the description of Unity Catalog assets and search across Unity Catalog server instances.  It can also be used to provision new assets to Unity Catalog. (Extracted from 6.0-SNAPSHOT)
