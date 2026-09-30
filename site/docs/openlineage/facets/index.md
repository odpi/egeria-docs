<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Egeria's Open Lineage Facets

The [Open Lineage standard](https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.md) lets any producer add its own *custom facets* to an event, alongside the standard ones.  A custom facet is keyed `{prefix}_{name}`, and it carries a `_schemaURL` that points to an immutable, versioned JSON schema describing it.

Egeria defines two custom run facets.  Both use the `egeria` prefix, and their schemas are published here:

| Facet key                       | Schema                                                                                                  | Purpose                                                                                     |
|---------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `egeria_governanceAction`       | [EgeriaGovernanceActionRunFacet.json](/openlineage/facets/1-0-0/EgeriaGovernanceActionRunFacet.json)             | Describes the Egeria governance action (engine action) that a run represents.              |
| `egeria_informationSupplyChain` | [EgeriaInformationSupplyChainRunFacet.json](/openlineage/facets/1-0-0/EgeriaInformationSupplyChainRunFacet.json) | Names the [information supply chain](/concepts/information-supply-chain) that a run is part of. |

Published schema versions are never changed.  A change to a facet is published as a new version in a new folder, and the version is part of each facet's `_schemaURL`.


## egeria_governanceAction

The [Governance Action Open Lineage integration connector](/egeria-solutions/leveraging-open-lineage/overview/#the-open-lineage-connectors) adds this facet to the run of every Open Lineage event that it creates from an [engine action](/concepts/engine-action).  It links the run back to the governance action that produced it.

| Property                   | Description                                                                                                |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| `iscQualifiedName`         | Qualified name of the information supply chain that the governance action is part of.                      |
| `engineActionGUID`         | Unique identifier of the engine action that describes this run.                                            |
| `governanceEngineName`     | Name of the governance engine that ran the governance action.                                              |
| `requestType`              | Request type that selected the governance service.                                                         |
| `governanceActionTypeName` | Name of the governance action type that the engine action was created from.                                |
| `processName`              | Qualified name of the governance action process instance that the engine action is part of.                |
| `processStepName`          | Qualified name of the governance action process step that the engine action implements.                    |

Schema URL: `https://egeria-project.org/openlineage/facets/1-0-0/EgeriaGovernanceActionRunFacet.json#/$defs/EgeriaGovernanceActionRunFacet`

```json
"egeria_governanceAction": {
  "_producer": "https://egeria-project.org/",
  "_schemaURL": "https://egeria-project.org/openlineage/facets/1-0-0/EgeriaGovernanceActionRunFacet.json#/$defs/EgeriaGovernanceActionRunFacet",
  "iscQualifiedName": "InformationSupplyChain::Orders",
  "engineActionGUID": "d46e465b-d358-4d32-83d4-df660ff614dd",
  "governanceEngineName": "EgeriaGovernance",
  "requestType": "provision-tabular-data-set",
  "governanceActionTypeName": "Egeria:GovernanceActionType:provision-tabular-data-set",
  "processName": "Orders provisioning",
  "processStepName": "Copy orders"
}
```

When the Open Lineage Cataloguer receives an event with this facet, it uses `processName` and `processStepName` to find the elements behind the run:

* The job is catalogued as the **GovernanceActionProcess** that governs the process instance.  This is the same element that provisioning services connect their own lineage to, so the lineage from every run of the process meets there.
* The *RunMetrics* classification is kept on the **GovernanceActionProcessStep**, because each step of a process runs separately.
* The **GovernanceActionProcessInstance** represents this particular run.

The [Lovelace](/egeria-solutions/leveraging-open-lineage/overview/#analysing-the-log-store-the-lovelace-services) analysis services also use this facet to find the process step that a governance action run belongs to.


## egeria_informationSupplyChain

Any producer can add this facet to a run to say which information supply chain the run belongs to.  For example, an Apache Airflow DAG that implements part of a supply chain can add it to its runs.

| Property           | Description                                                                          |
|--------------------|--------------------------------------------------------------------------------------|
| `iscQualifiedName` | Qualified name of the information supply chain that the run is part of.  Required. |

Schema URL: `https://egeria-project.org/openlineage/facets/1-0-0/EgeriaInformationSupplyChainRunFacet.json#/$defs/EgeriaInformationSupplyChainRunFacet`

```json
"egeria_informationSupplyChain": {
  "_producer": "https://example.com/producer",
  "_schemaURL": "https://egeria-project.org/openlineage/facets/1-0-0/EgeriaInformationSupplyChainRunFacet.json#/$defs/EgeriaInformationSupplyChainRunFacet",
  "iscQualifiedName": "InformationSupplyChain::Orders"
}
```

The Open Lineage Cataloguer tags the lineage relationships that it creates from the event (for example *DataFlow* and *DataMapping*) with this information supply chain.  It also uses the supply chain when it links a physical data asset to its abstractions with *DataSetContent*: it creates one relationship per supply chain.  If a run has no `egeria_informationSupplyChain` facet, the cataloguer uses the `iscQualifiedName` from the `egeria_governanceAction` facet, if one is present.


## Related information

* [Leveraging Open Lineage](/egeria-solutions/leveraging-open-lineage/overview) - how Egeria receives, stores, catalogues and analyses Open Lineage events.
* [Open Lineage naming conventions](https://openlineage.io/docs/spec/naming/) - the rules for dataset and job namespaces and names, which Egeria follows.  Elements that only exist in open metadata use the `egeria` namespace.
* [Open Lineage specification](https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.md) - including the rules for custom facets.

--8<-- "snippets/abbr.md"
