```mermaid
---
title: Components and Roles for Solution Blueprint - Unity Catalog Content Pack [548661f1-e792-4acd-8dc2-0aa41187d6d2]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Components and Actors]
2@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for Unity Catalog Server**"}
3@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Volume**"}
4@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogTable**"}
5@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogSchema**"}
6@{ shape: subproc, label: "*Solution Component*
**Delete an OSS Unity Catalog Server from Open Metadata**"}
7@{ shape: subproc, label: "*Solution Component*
**Create a Databricks Unity Catalog Server in Open Metadata**"}
8@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Server**"}
9@{ shape: subproc, label: "*Solution Component*
**Configure the Unity Catalog Server Cataloguer**"}
10@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Schema**"}
11@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for Databricks Unity Catalog Server**"}
12@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogFunction**"}
13@{ shape: rect, label: "*Solution Component*
**Unity Catalog Server**"}
14@{ shape: div-rect, label: "*Solution Component*
**Unity Catalog Server Exchange**"}
15@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogCatalog**"}
16@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for Databricks Unity Catalog Server**"}
17@{ shape: processes, label: "*Solution Component*
**Provision Governance Action Process for UnityCatalogVolume**"}
18@{ shape: subproc, label: "*Solution Component*
**Provision Unity Catalog Resource**"}
19@{ shape: processes, label: "*Solution Component*
**Create and Survey Governance Action Process for Unity Catalog Server**"}
20@{ shape: subproc, label: "*Solution Component*
**Delete a Databricks Unity Catalog Server from Open Metadata**"}
21@{ shape: processes, label: "*Solution Component*
**Delete with Template Governance Action Process for Databricks Unity Catalog Server**"}
22@{ shape: subproc, label: "*Solution Component*
**Print Survey Report**"}
23@{ shape: subproc, label: "*Solution Component*
**Create an OSS Unity Catalog Server in Open Metadata**"}
24@{ shape: rect, label: "*Solution Component*
**Databricks Unity Catalog Server**"}
25@{ shape: div-rect, label: "*Solution Component*
**Unity Catalog Asset Exchange**"}
26@{ shape: subproc, label: "*Solution Component*
**Survey Unity Catalog Catalog**"}
27@{ shape: processes, label: "*Solution Component*
**Create and catalog Governance Action Process for Unity Catalog Server**"}
28@{ shape: trap-t, label: "*Solution Actor Role*
**Open Metadata User**"}
28==>|"delete Unity Catalog Server,
[Solution Component Actor]"|2
2==>|"step 1,
[Solution Linking Wire]"|6
3==>|"works with,
[Solution Linking Wire]"|13
28==>|"provision asset,
[Solution Component Actor]"|4
4==>|"step 1,
[Solution Linking Wire]"|18
28==>|"provision asset,
[Solution Component Actor]"|5
5==>|"step 1,
[Solution Linking Wire]"|18
21==>|"step 1,
[Solution Linking Wire]"|6
16==>|"step 1,
[Solution Linking Wire]"|7
11==>|"step 1,
[Solution Linking Wire]"|7
16==>|"step 2,
[Solution Linking Wire]"|8
19==>|"step 2,
[Solution Linking Wire]"|8
8==>|"works with,
[Solution Linking Wire]"|13
27==>|"step 2,
[Solution Linking Wire]"|9
9==>|"configures,
[Solution Linking Wire]"|14
11==>|"step 2,
[Solution Linking Wire]"|9
10==>|"works with,
[Solution Linking Wire]"|13
28==>|"requests catalog,
[Solution Component Actor]"|11
28==>|"provision asset,
[Solution Component Actor]"|12
12==>|"step 1,
[Solution Linking Wire]"|18
18==>|"works with,
[Solution Linking Wire]"|13
25==>|"Catalog Resource,
[Solution Linking Wire]"|13
26==>|"works with,
[Solution Linking Wire]"|13
14==>|"Catalog Resource,
[Solution Linking Wire]"|13
14==>|"handoff,
[Solution Linking Wire]"|25
28==>|"provision asset,
[Solution Component Actor]"|15
15==>|"step 1,
[Solution Linking Wire]"|18
28==>|"requests survey,
[Solution Component Actor]"|16
16==>|"step 3,
[Solution Linking Wire]"|22
28==>|"provision asset,
[Solution Component Actor]"|17
17==>|"step 1,
[Solution Linking Wire]"|18
28==>|"requests survey,
[Solution Component Actor]"|19
19==>|"step 3,
[Solution Linking Wire]"|22
19==>|"step 1,
[Solution Linking Wire]"|23
28==>|"delete Databricks Unity Catalog Server,
[Solution Component Actor]"|21
27==>|"step 1,
[Solution Linking Wire]"|23
28==>|"requests catalog,
[Solution Component Actor]"|27
end
style 22 color:#000000, fill:#dda0dd, stroke:#000000
style 23 color:#000000, fill:#dda0dd, stroke:#000000
style 24 color:#000000, fill:#dda0dd, stroke:#000000
style 25 color:#000000, fill:#dda0dd, stroke:#000000
style 26 color:#000000, fill:#dda0dd, stroke:#000000
style 27 color:#000000, fill:#dda0dd, stroke:#000000
style 28 color:#000000, fill:#FFE599, stroke:#000000
style 10 color:#000000, fill:#dda0dd, stroke:#000000
style 11 color:#000000, fill:#dda0dd, stroke:#000000
style 12 color:#000000, fill:#dda0dd, stroke:#000000
style 13 color:#000000, fill:#dda0dd, stroke:#000000
style 14 color:#000000, fill:#dda0dd, stroke:#000000
style 15 color:#000000, fill:#dda0dd, stroke:#000000
style 16 color:#000000, fill:#dda0dd, stroke:#000000
style 17 color:#000000, fill:#dda0dd, stroke:#000000
style 18 color:#000000, fill:#dda0dd, stroke:#000000
style 19 color:#000000, fill:#dda0dd, stroke:#000000
style 1 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 2 color:#000000, fill:#dda0dd, stroke:#000000
style 3 color:#000000, fill:#dda0dd, stroke:#000000
style 4 color:#000000, fill:#dda0dd, stroke:#000000
style 5 color:#000000, fill:#dda0dd, stroke:#000000
style 6 color:#000000, fill:#dda0dd, stroke:#000000
style 7 color:#000000, fill:#dda0dd, stroke:#000000
style 8 color:#000000, fill:#dda0dd, stroke:#000000
style 9 color:#000000, fill:#dda0dd, stroke:#000000
style 20 color:#000000, fill:#dda0dd, stroke:#000000
style 21 color:#000000, fill:#dda0dd, stroke:#000000
click 22 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 23 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 24 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 25 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 26 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 27 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 10 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 11 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 12 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 13 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
click 14 "https://egeria-project.org/concepts/integration-connector/" "Click for more documentation" _blank
click 15 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 16 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 17 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 18 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 19 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 2 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 3 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 4 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 5 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 6 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 7 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 8 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 9 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 20 "https://egeria-project.org/concepts/governance-action-type/" "Click for more documentation" _blank
click 21 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
```
> Unity Catalog Content Pack: Solution blueprint supporting the exchange of metadata between the open metadata ecosystem and Unity Catalog (UC). (Extracted from 6.0-SNAPSHOT)
