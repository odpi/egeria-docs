```mermaid
---
title: Components and Roles for Solution Blueprint - Unity Catalog Content Pack [548661f1-e792-4acd-8dc2-0aa41187d6d2]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for Databricks Unity Catalog Server**"}
3@{ shape: div-rect, label: "*Solution Component*
**Unity Catalog Server Exchange**"}
4@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Catalog**"}
5@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for Databricks Unity Catalog Server**"}
6@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogCatalog**"}
7@{ shape: subproc, label: "*Solution Component*
**Create an OSS Unity Catalog Server in Open Metadata**"}
8@{ shape: div-rect, label: "*Solution Component*
**Unity Catalog Asset Exchange**"}
9@{ shape: subproc, label: "*Solution Component*
**Configure the Unity Catalog Server Cataloguer**"}
10@{ shape: subproc, label: "*Solution Component*
**Create a Databricks Unity Catalog Server in Open Metadata**"}
11@{ shape: subproc, label: "*Solution Component*
**Provision Unity Catalog Resource**"}
12@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogVolume**"}
13@{ shape: rect, label: "*Solution Component*
**Unity Catalog Server**"}
14@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for Unity Catalog Server**"}
15@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogFunction**"}
16@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for Unity Catalog Server**"}
17@{ shape: subproc, label: "*Solution Component*
**Delete an OSS Unity Catalog Server from Open Metadata**"}
18@{ shape: subproc, label: "*Solution Component*
**Print Survey Report**"}
19@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for Unity Catalog Server**"}
20@{ shape: rect, label: "*Solution Component*
**Databricks Unity Catalog Server**"}
21@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Volume**"}
22@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogSchema**"}
23@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Server**"}
24@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for Databricks Unity Catalog Server**"}
25@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogTable**"}
26@{ shape: subproc, label: "*Solution Component*
**Delete a Databricks Unity Catalog Server from Open Metadata**"}
27@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Schema**"}
2==>|"step 1,
[Solution Linking Wire]"|26
3==>|"handoff,
[Solution Linking Wire]"|8
9==>|"configures,
[Solution Linking Wire]"|3
3==>|"Catalog Resource,
[Solution Linking Wire]"|13
4==>|"works with,
[Solution Linking Wire]"|13
5==>|"step 2,
[Solution Linking Wire]"|23
5==>|"step 1,
[Solution Linking Wire]"|10
5==>|"step 3,
[Solution Linking Wire]"|18
6==>|"step 1,
[Solution Linking Wire]"|11
14==>|"step 1,
[Solution Linking Wire]"|7
16==>|"step 1,
[Solution Linking Wire]"|7
8==>|"Catalog Resource,
[Solution Linking Wire]"|13
14==>|"step 2,
[Solution Linking Wire]"|9
24==>|"step 2,
[Solution Linking Wire]"|9
24==>|"step 1,
[Solution Linking Wire]"|10
25==>|"step 1,
[Solution Linking Wire]"|11
22==>|"step 1,
[Solution Linking Wire]"|11
12==>|"step 1,
[Solution Linking Wire]"|11
11==>|"works with,
[Solution Linking Wire]"|13
15==>|"step 1,
[Solution Linking Wire]"|11
21==>|"works with,
[Solution Linking Wire]"|13
27==>|"works with,
[Solution Linking Wire]"|13
23==>|"works with,
[Solution Linking Wire]"|13
16==>|"step 2,
[Solution Linking Wire]"|23
16==>|"step 3,
[Solution Linking Wire]"|18
19==>|"step 1,
[Solution Linking Wire]"|17
end
style 22 color:#000000, fill:#DDA0DD, stroke:#000000
style 23 color:#000000, fill:#DDA0DD, stroke:#000000
style 24 color:#000000, fill:#DDA0DD, stroke:#000000
style 25 color:#000000, fill:#DDA0DD, stroke:#000000
style 26 color:#000000, fill:#DDA0DD, stroke:#000000
style 27 color:#000000, fill:#DDA0DD, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#DDA0DD, stroke:#000000
style 15 color:#000000, fill:#DDA0DD, stroke:#000000
style 16 color:#000000, fill:#DDA0DD, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#DDA0DD, stroke:#000000
style 19 color:#000000, fill:#DDA0DD, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 20 color:#000000, fill:#DDA0DD, stroke:#000000
style 21 color:#000000, fill:#DDA0DD, stroke:#000000
click 22 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 23 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 24 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 25 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 26 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 27 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 11 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 13 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 14 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 18 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 20 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 21 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
```
> Unity Catalog Content Pack: Solution blueprint supporting the exchange of metadata between the open metadata ecosystem and Unity Catalog (UC). (Extracted from 6.3-SNAPSHOT)
