<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/released.md"

# Open Connector Framework (OCF)

The *open connector framework* (OCF), as the name suggests, is an open framework for supporting [connectors](/egeria-docs/concepts/connector). Connector provide client-side access to remote digital [assets](/egeria-docs/concepts/assets) such as data sets, APIs and software components. OCF connectors also provide access to metadata about the asset and may call the [Governance Action Framework (GAF)](/egeria-docs/frameworks/gaf) to log audit messages and execute appropriate governance actions related to the use of these assets in real-time.

## Benefits

Applications and tools benefit from using OCF connectors because:

- Network and security parameters for accessing the data resources are managed in the metadata repository as part of a named connection. The application need only supply the identifier of the connection and provided they have the appropriate security credentials then a connector is returned to them for use.
    - There is no need to hard-code user ids and passwords in the application code - nor manage key stores for this sensitive information since the metadata repository handles this.
    - If the location of the data changes, then the named connection configuration is changed in the metadata repository and the application will be connected to the new location the next time they request a connector.
- The OCF connector provides two sets of APIs. The first set provides access to the asset contents and the second set provides access to the properties of the asset stored in the open metadata repositories. This provides applications and tools with a simple mechanism to make use of metadata as they process about the asset. It is particularly useful for data science tools where these properties can help guide the end user in the use of the asset.
- OCF connectors are not limited to representing assets as they are physically implemented. An OCF connector can represent a simplified logical (virtual) data resource that is designed for the needs of a specific application or tool. This type of connector delegates the requests it receives to one or more physical data resources.

Organizations benefit from advocating the use of OCF connectors for their systems because the OCF connectors provide a consistent approach to governance enforcement and audit logging. This is particularly important in data-rich environments where individuals are able to combine data from different assets creating new, potentially sensitive insight. The common approach to auditing, and the linkage between the data accessed and the metadata that describes its characteristics help to detect and prevent such actions.

## Design rationale

The following factors influenced the design of the OCF.

- There are many existing connectors and connector frameworks in the industry today. It is important that these existing connectors can be incorporated into the OCF. Thus, the OCF includes placeholders for adapters to external connector providers and connectors.
- Application developers will only adopt a connector framework if it is easy to use. Thus, the connector interfaces allow for the use of native data APIs to minimize the effort an application developer has to take in order to use the OCF connectors.
- Governance enforcement is a complex topic, typically managed externally to the application development team. As a result, a separate framework called the [governance action framework (GAF)](/egeria-docs/frameworks/gaf) manages governance enforcement. The role of the OCF is to bridge from the asset access requests to the GAF where necessary.
- Access to the all properties known about an asset should be available to the consumers of the asset.Therefore, the OCF provides a standard interface for accessing these properties. Different providers of these properties can plug into the OCF. Egeria provides an implementation of this interface to supply asset properties stored in open metadata repositories in the [OCF metadata management common service](/egeria-docs/services/common/ocf-metadata-management).

## Terminology

There are a number of key components within the OCF:

- [Connector](/egeria-docs/concepts/connector) is a Java object for accessing an asset and its related metadata and governance functions.
- [Connection](/egeria-docs/concepts/connection) is a Java object containing the properties needed to create a connector instance.
- [Connector broker](/egeria-docs/concepts/connector-broker) is a generic factory for all OCF connectors.
- [Connector provider](/egeria-docs/concepts/connector-provider) is a factory for a specific type of connector. It is used by the connector broker.
- [Connected asset properties](/egeria-docs/concepts/connected-asset-properties) are the properties of the asset that the connector is accessing. It is hosted by a metadata server.

## Types

Open metadata repositories are able to store information needed to use OCF connectors. Details of the types involved are as follows:

- [Model 0040](/egeria-docs/types/0/0040-software-servers) defines the structure of an `Endpoint`.
- [Model 0201](/egeria-docs/types/2/0201-connectors-and-connections.md) defines the structures for `Connection`s and `ConnectorType`s.
- [Model 0205](/egeria-docs/types/2/0205-connection-linkage.md) defines the linkage between the connection and the connected asset.

!!! education "Further information"
    - The [OCF Metadata Management common services](/egeria-docs/services/common/ocf-metadata-management) supports the retrieval of connection and connected asset properties from the open metadata repository/repositories.
    - The [Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer) embeds the OCF to provide client-side support for connectors.
    - The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) make extensive use of OCF connectors for accessing open metadata repository servers and other resources. These connectors are collectively called the [OMRS connectors](/egeria-docs/concepts/connector).
    - Many of the [Open Metadata Governance Servers](/egeria-docs/concepts/governance-server) make use of OCF connectors to loosely-couple integration with a variety of underlying technologies.
    - The [developer guide](/egeria-docs/guides/developer) provides more information on writing connectors for Egeria.
    - The [connector catalog](/egeria-docs/connectors) lists the pre-built connectors supplied by Egeria.

--8<-- "snippets/abbr.md"
