```mermaid
---
title: SolutionComponent - Provision Unity Catalog Resource [4aba9c28-95fe-4289-9dde-67a3836ab1bf]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Solution Component*
**Provision Unity Catalog Resource**"}
2@{ shape: rect, label: "*Solution Blueprint*
**Unity Catalog Content Pack**"}
2==>|"Collection Membership"|1
3@{ shape: rect, label: "*Solution Component*
**Unity Catalog Server**"}
1==>|"works with [Solution Linking Wire]"|3
4@{ shape: rect, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogSchema**"}
4==>|"step 1 [Solution Linking Wire]"|1
5@{ shape: rect, label: "*Solution Component*
**Metadata Access Store**"}
1==>|"metadata [Solution Linking Wire]"|5
6@{ shape: rect, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogCatalog**"}
6==>|"step 1 [Solution Linking Wire]"|1
7@{ shape: rect, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogVolume**"}
7==>|"step 1 [Solution Linking Wire]"|1
8@{ shape: rect, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogTable**"}
8==>|"step 1 [Solution Linking Wire]"|1
9@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 1 Items**"}
9-.->1
10@{ shape: tag-rect, label: "*Governance Action Type*
**provision-unity-catalog-resource (UnityCatalogGovernance)**"}
1==>|"Implemented By"|10
11@{ shape: stadium, label: "*Solution Linking Wire*
**... plus 1 Items**"}
11-.->1
style 11 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#000000, fill:#f5fffa, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
style 10 color:#000000, fill:#53bbb4, stroke:#000000
click 1 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 3 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/concepts/metadata-access-store/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
```
> Provision Unity Catalog Resource: Creates a description of a Unity Catalog resource (such as a volume, table or function) for a particular Unity Catalog Server that will be picked up and added to the Unity Catalog Server by the Unity Catalog integration connector on the next refresh. (Extracted from 6.0-SNAPSHOT)
