```mermaid
---
title: SolutionComponent - Unity Catalog Server Exchange [a8d557c8-c914-4d70-a04e-45a48119a670]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Unity Catalog Server Exchange**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Unity Catalog Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Unity Catalog Server**"}
1==>|"Catalog Resource [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Unity Catalog Asset Exchange**"}
1==>|"handoff [Solution Linking Wire]"|4
5@{ shape: rect, label: "*Solution Component*
**Configure the Unity Catalog Server Cataloguer**"}
5==>|"configures [Solution Linking Wire]"|1
6@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|6
7@{ shape: stadium, label: "*Integration Connector*
**UnityCatalogServerIntegrationConnector**"}
1==>|"Implemented By"|7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#bdb76b, stroke:#004563
click 1 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 3 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
```
> Unity Catalog Server Exchange: Maintains the open metadata description of the catalogs found in the Unity Catalog servers linked through CatalogTarget relationships.  It hands off the cataloguing of the assets within each catalog to the ''Unity Catalog Asset Exchange''.  New catalogs linked to the metadata element for a Unity Catalog server are automatically provisioned to the corresponding Unity Catalog server instance. (Extracted from 6.0-SNAPSHOT)
