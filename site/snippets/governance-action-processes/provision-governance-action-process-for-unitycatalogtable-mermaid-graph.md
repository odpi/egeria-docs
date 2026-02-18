```mermaid
---
title: GovernanceActionProcess - Provision Governance Action Process for UnityCatalogTable [b6decef4-e72d-4f13-9041-8f5c0ea4d323]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rounded, label: "*Governance Action Process*
**Provision Governance Action Process for UnityCatalogTable**"}
2@{ shape: hex, label: "*Technology Type*
**Unity Catalog Table**"}
2==>|"Survey Resource [Resource List]"|1
3@{ shape: rounded, label: "*Governance Action Process Step*
**Create the new element**"}
1==>|"Governance Action Process Flow"|3
style 1 color:#000000, fill:#e0ab18, stroke:#004563
style 2 color:#f2d9e7, fill:#732650, stroke:#f2d9e7
style 3 color:#FFFFFF, fill:#3079ab, stroke:#000000
click 1 "https://egeria-project.org/egeria-solutions/leveraging-unity-catalog/overview/" "Click for more documentation" _blank
click 2 "https://github.com/unitycatalog/unitycatalog" "Click for more documentation" _blank
```
> Provision Governance Action Process for UnityCatalogTable: Create a DeployedImplementationType{Unity Catalog Table} element in the correct metadata collection so that it is provisioned into unity catalog. (Extracted from 6.0-SNAPSHOT)
