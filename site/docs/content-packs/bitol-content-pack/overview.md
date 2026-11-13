<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Bitol Content Pack

The *BitolContentPack* configures the integration connectors that work with the [Bitol](https://bitol.io) open standards - the *Open Data Contract Standard (ODCS)* and the *Open Data Product Standard (ODPS)*.  It lets you receive ODCS and ODPS YAML or JSON documents from files and Apache Kafka topics, catalog them in Egeria's [digital product](/concepts/digital-product) catalog as data sharing agreements and digital products, and generate and store the documents for the digital products and agreements that are defined in open metadata.  The connectors are supplied in the *omag-server-platform* distribution.

The content pack is found in the `BitolContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the connector types for the six Bitol connectors and the valid metadata values for the ODCS and ODPS file types (`Open Data Contract Standard (ODCS) File`, `Open Data Product Standard (ODPS) File` and their `JSON File` variants) and for the `bitol.kind` additional property.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

The connectors are linked through the integration daemon's Bitol listener mechanism in the same way as the [Open Lineage connectors](/content-packs/open-lineage-content-pack/overview).  The *receivers* read documents from where they are published and pass each one to the Bitol listeners registered in the same [integration daemon](/concepts/integration-daemon).  The two *cataloguers* and the *file store* are listeners: the cataloguers turn each document into open metadata, and the file store writes every document it is given to the file system.  The *document publisher* works in the other direction: it generates documents from the digital products and data sharing agreements in open metadata whenever they change, and passes them to the same listeners, so they reach the file store ready to be committed to a git repository.

A document is only published when its content differs from the last document generated for the same element, so a cataloguer running in the same daemon does not cause an endless exchange of identical documents.  Documents may also be published to the daemon through its REST API (`publish-data-contract` and `publish-data-product`) and through the [Product Manager OMVS](/services/omvs/product-manager/overview), which can also import or generate a document synchronously.

## Integration connectors

The pack defines the *BitolIntegrationGroup* (`Egeria:IntegrationGroup:Bitol`), a dynamic [integration group](/concepts/integration-group).  Each connector runs with its own user and refreshes every 60 minutes.

| Connector | Runs as | Purpose |
|---|---|---|
| BitolFilesReceiverIntegrationConnector | `BitolFilesReceiver` (user `bitolfilesnpa`) | Monitors file directories for ODCS and ODPS documents and publishes the new and changed documents to the Bitol listeners.  It monitors `loading-bay/bitol` by default (the network address of its endpoint), plus any *FileFolder* (such as a git checkout) attached as a `directoryToMonitor` [catalog target](/concepts/catalog-target). |
| BitolEventReceiverIntegrationConnector | `BitolEventReceiver` (user `bitoleventsnpa`) | Receives one complete ODCS or ODPS document per event from the Apache Kafka topics attached as `topicToMonitor` catalog targets.  It has no default topic. |
| BitolDataProductCataloguerIntegrationConnector | `BitolDataProductCataloguer` (user `bitolprodcatnpa`) | Catalogs each ODPS document as a *DigitalProduct* with *SolutionPort*s for its input and output ports, along with its team, support channels and references. |
| BitolDataContractCataloguerIntegrationConnector | `BitolDataContractCataloguer` (user `bitolcontcatnpa`) | Catalogs each ODCS document as an *Agreement* classified as a *DataSharingAgreement*, with its schema, quality rules, service levels, servers and security roles. |
| BitolDocumentPublisherIntegrationConnector | `BitolDocumentPublisher` (user `bitolpubnpa`) | Generates ODPS and ODCS documents from the digital products and data sharing agreements in open metadata whenever they change, and on each refresh for the members of the *DigitalProductCatalog*s attached as `productCatalog` catalog targets.  It needs no endpoint. |
| BitolFileStoreIntegrationConnector | `BitolFileStore` (user `bitolstorenpa`) | Writes every document published in the integration daemon to `distribution-hub/bitol` by default (the network address of its endpoint), or to a directory attached as a `storeDirectory` catalog target.  Each document is stored as `{kind}/{id}/{version}.yaml` (or `.json`), and documents that could not be parsed are kept under `{kind}/unparsed/`. |

The files receiver and the file store also catalog the files they read and write as data assets with the ODCS or ODPS deployed implementation type, linked to the catalogued agreement or digital product as a *Bitol Document* resource.  No catalog targets are attached to any of the connectors in the content pack.

The pack defines no governance engines, technology types or templates of its own.

## Solution blueprint

The solution blueprint for the content pack, taken from Egeria's quickstart, shows how the connectors pass documents to one another.

--8<-- "snippets/blueprints/content-packs/bitol-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then add the *BitolIntegrationGroup* to an integration daemon.  Drop ODCS and ODPS documents into `loading-bay/bitol` to have them catalogued, and pick up the generated documents from `distribution-hub/bitol`.

    The mapping between the documents and open metadata is described in the [digital product management](/features/digital-product-management/overview) feature, and in the [connectors' README :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/bitol-integration-connectors/README.md){ target=gh }.

--8<-- "snippets/abbr.md"
