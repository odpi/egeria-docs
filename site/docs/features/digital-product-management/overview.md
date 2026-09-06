<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Digital Product Management

A [digital product](/concepts/digital-product) packages data (or another digital resource) that is designed to meet a specific consumer need, together with the licenses, terms of use and service levels that its consumers can rely on.  Egeria describes digital products in open metadata using the [DigitalProduct](/types/7/0710-Digital-Products) type, organizes them into [digital product catalogs](/concepts/digital-product), and manages the [agreements](/types/7/0711-Agreements) - subscriptions and data sharing agreements - between product providers and their consumers.

The [Product Manager OMVS](/services/omvs/product-manager/overview) maintains the product definitions, the [Product Catalog OMVS](/services/omvs/product-catalog/overview) lets consumers find and subscribe to them, and the [Solution Architect OMVS](/services/omvs/solution-architect/overview) describes the solution components and solution ports through which the data flows.

## The Bitol standards

Many organizations describe their data products and the data they exchange as YAML documents held in git, using the open standards published by the [Bitol](https://bitol.io) project (part of the Linux Foundation's AI & Data foundation):

* The **Open Data Contract Standard (ODCS)** describes a dataset that one team makes available to others: its schema (with types, classifications and relationships between fields), the data quality checks it is held to, its service level agreement, support channels, pricing, team, access roles and the servers on which it resides.  A document has `kind: DataContract`.
* The **Open Data Product Standard (ODPS)** describes a data product: the data it consumes (*input ports*) and provides (*output ports*), each of which is described by an ODCS contract, together with its management ports, support channels and team.  A document has `kind: DataProduct`.

Egeria supports both standards so that documents written by product teams can be catalogued alongside the rest of the organization's metadata, and so that products and agreements defined through Egeria's own services can be published in the formats that the teams and their tooling expect.

### Mapping to open metadata

An ODPS document is catalogued as a *DigitalProduct*.  Its `domain` becomes membership of a *DigitalProductCatalog*, its `tenant` an *Organization* that scopes the product, and its status is recorded using the *ContentStatus* classification.  Each input and output port becomes a *SolutionPort* attached to a *SolutionComponent* that represents the product's implementation; the port is linked to the *Agreement* that represents its contract.  Management ports become *Endpoint*s in the product's resource list.  Team members become *PersonRole*s scoped to the product, with a *PersonRoleAppointment* when the user name maps to a known user identity.

An ODCS document is catalogued as an *Agreement* classified as a *DataSharingAgreement*.  Each schema object becomes a *DataStructure* that is an agreement item, and each property a *DataField* (nested for object and array types).  Primary keys, confidentiality and criticality are recorded as classifications on the fields; relationships between properties become *LinkedDataField* relationships; quality checks become *DataQualityRule*s governing the field or structure; the SLA becomes a *ServiceLevelObjective* governing the agreement; servers become *Endpoint*s in the agreement's resource list; and the access roles become *SecurityRole*s associated with a *SecurityAccessControl* that governs the agreement.  Properties of the standards that have no open metadata equivalent are preserved as additional properties prefixed `bitol.`, so a document can be regenerated without loss.

Every version of a document is a separate element whose qualified name includes the version, linked to its siblings through a shared *ExternalId*.  A document whose status is `retired` causes its element to be soft deleted.

### Egeria's Bitol support

The [Open Integration Framework (OIF)](/frameworks/oif/overview) provides Java beans for both document kinds, a YAML/JSON formatter, and a distribution mechanism in the [integration daemon](/concepts/integration-daemon) that mirrors its [Open Lineage support](/features/lineage-management/overview/#egerias-open-lineage-support):

* An integration connector may register a *Bitol listener* with its integration context to receive every document that is published to the daemon.
* An integration connector may publish a document (as a bean or as raw YAML/JSON) for the other listeners registered in the same daemon.
* The integration daemon's REST API (`publish-data-contract` and `publish-data-product`) and the Product Manager OMVS allow external callers to publish documents into the daemon.

The [Bitol connectors :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/bitol-integration-connectors/README.md){ target=gh } supplied by Egeria, and packaged in the [Bitol Content Pack](/content-packs/bitol-content-pack/overview), are divided into the connectors that acquire documents (the *receivers*) and the connectors that process or distribute them:

1. The **Bitol Files Receiver** monitors directories - typically a git checkout or a drop folder - and publishes the new and changed documents it finds.
2. The **Bitol Event Receiver** receives documents from Apache Kafka topics attached as catalog targets.
3. The **Bitol Data Product Cataloguer** and **Bitol Data Contract Cataloguer** register listeners and catalog each document they receive using the mapping above.
4. The **Bitol Document Publisher** listens for changes to digital products and data sharing agreements in open metadata, regenerates their documents and publishes them to the other listeners.  On each refresh it also regenerates the documents for every member of the digital product catalogs attached as catalog targets.
5. The **Bitol File Store** registers a listener and writes every document it receives to the file system as `{kind}/{id}/{version}.yaml`, so that the directory can be committed to git.

A product team can therefore commit a data contract to git and have it appear in the catalog, while a product manager working in Egeria's user interfaces sees their products written back to the same repository in the standard format.

--8<-- "snippets/abbr.md"
