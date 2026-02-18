```mermaid
---
title: GovernanceActionProcess - DatabricksUnityCatalogServer:CreateAndSurvey [f806f64c-56fe-4a9d-a19b-39dd4cc7995e]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Governance Action Process*
**DatabricksUnityCatalogServer:CreateAndSurvey**"}
2@{ shape: hex, label: "*Technology Type*
**Databricks Unity Catalog Server**"}
2==>|"Survey Resource [Resource List]"|1
3@{ shape: rounded, label: "*Governance Action Process Step*
**Create the DatabricksUnityCatalogServer entity**"}
1==>|"Governance Action Process Flow"|3
4@{ shape: hex, label: "*Specification Property Value*
**Log of Unity Catalog (UC) Resources**"}
1==>|"producedAnnotationType [Specification Property Assignment]"|4
5@{ shape: hex, label: "*Specification Property Value*
**Capture List of Analytical Models**"}
1==>|"producedAnnotationType [Specification Property Assignment]"|5
6@{ shape: hex, label: "*Specification Property Value*
**Profiling Associated Resources**"}
1==>|"supportedAnalysisStep [Specification Property Assignment]"|6
7@{ shape: hex, label: "*Specification Property Value*
**Check Asset**"}
1==>|"supportedAnalysisStep [Specification Property Assignment]"|7
8@{ shape: hex, label: "*Specification Property Value*
**Capture List of File Volumes**"}
1==>|"producedAnnotationType [Specification Property Assignment]"|8
9@{ shape: hex, label: "*Specification Property Value*
**serverName**"}
1==>|"supportedRequestParameter [Specification Property Assignment]"|9
10@{ shape: stadium, label: "*Specification Property Assignment*
**... plus 14 Items**"}
1-.->10
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 3 color:#FFFFFF, fill:#3079ab, stroke:#000000
style 4 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 5 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 6 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 7 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 8 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 9 color:#260d1b, fill:#d98cb6, stroke:#260d1b
style 10 color:#000000, fill:#F9F7ED, stroke:#b7c0c7
click 1 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 2 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
```
