<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# DCAT Content Pack

The *DCATContentPack* configures the integration connectors that work with the W3C [Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-3/).  DCAT is the standard that governments and many other organizations use to describe the data assets that they make available: what each dataset is about, who publishes it, how it is licensed and where it can be obtained.  The content pack lets you receive DCAT descriptions from files and Apache Kafka topics, catalog them as [assets](/concepts/asset), and publish the DCAT descriptions of the assets you choose so that a data portal can harvest them.  The connectors are supplied in the *omag-server-platform* distribution.

The connectors work with the **JSON-LD** serialization of DCAT version 3.  Documents in Turtle or RDF/XML need to be converted to JSON-LD before they are passed to Egeria.

The content pack is found in the `DCATContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the connector types for the four DCAT connectors.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

The receivers and the cataloguer are linked through the integration daemon's DCAT listener mechanism in the same way as the [Open Lineage connectors](/content-packs/open-lineage-content-pack/overview) and the [Bitol connectors](/content-packs/bitol-content-pack/overview).  The *receivers* read DCAT documents from where they are published and pass each one to the DCAT listeners registered in the same [integration daemon](/concepts/integration-daemon).  The *cataloguer* is a listener that catalogs datasets as *DataSet* assets with an asset for each distribution, data services as *DeployedAPI* assets and catalogs as *CollectionFolder*s.  Documents may also be published to the daemon through its REST API and through the [Asset Catalog OMVS](/services/omvs/asset-catalog/overview), which is also able to catalog a document directly and return the DCAT description of any asset.

The *publisher* works in the other direction.  It is not a listener: on each refresh it writes the DCAT descriptions of the assets in its publishing catalogs to the file system.

## Integration connectors

The pack defines the *DCATIntegrationGroup* (`Egeria:IntegrationGroup:DCAT`), a dynamic [integration group](/concepts/integration-group).  Each connector runs with its own user and refreshes every 60 minutes.

| Connector | Runs as | Purpose |
|---|---|---|
| DCATFilesReceiverIntegrationConnector | `DCATFilesReceiver` (user `dcatfilesnpa`) | Scans file directories for `.jsonld` and `.json` files that describe DCAT resources and publishes new and changed documents to the DCAT listeners.  It scans `loading-bay/dcat` by default (the network address of its endpoint), plus the file folders attached as `directoryToMonitor` [catalog targets](/concepts/catalog-target). |
| DCATEventReceiverIntegrationConnector | `DCATEventReceiver` (user `dcateventsnpa`) | Publishes each event received from the Apache Kafka topics attached as `topicToMonitor` catalog targets as a DCAT document to the DCAT listeners.  It has no default topic. |
| DCATCataloguerIntegrationConnector | `DCATCataloguer` (user `dcatcatnpa`) | Listens for DCAT documents and catalogs the catalogs, datasets, dataset series and data services that they describe. |
| DCATPublisherIntegrationConnector | `DCATPublisher` (user `dcatpubnpa`) | Writes a DCAT catalog for each collection attached as a `publishingCatalog` catalog target, along with the DCAT description of each asset in the collection, to `distribution-hub/dcat-catalog` by default (the network address of its endpoint). |

## Choosing the assets to publish

The DCAT Publisher is told which assets to publish through the [collections](/concepts/collection) attached to it as catalog targets with the catalog target name `publishingCatalog`.  Each collection is published as a separate DCAT catalog in its own subdirectory, named after the collection and the first eight characters of its unique identifier.  An asset is published if it is a member of one of these collections, or of a collection folder nested in it.  Any type of collection can be used.

The content pack supplies the *DCAT Publishing Catalog* root collection (`Egeria::DCATPublishingCatalog`) and attaches it to the publisher as its `publishingCatalog` catalog target.  To publish an asset, add it to this collection; to withdraw it, remove it.  Further collections can be attached to the publisher to publish further catalogs.

The publisher has one configuration property:

| Configuration property | Description |
| --- | --- |
| `defaultPublisher` | The name of the organization to show as the publisher of an asset that is not linked to an organization. |

The pack defines no governance engines, technology types or templates of its own.

## Solution blueprint

The solution blueprint for the content pack, taken from Egeria's quickstart, shows how the connectors pass documents to one another.

--8<-- "snippets/blueprints/content-packs/dcat-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then add the *DCATIntegrationGroup* to an integration daemon.  Drop DCAT JSON-LD documents into `loading-bay/dcat` to have them catalogued, and add assets to the *DCAT Publishing Catalog* to have their descriptions written to `distribution-hub/dcat-catalog`.

    The mapping between DCAT and open metadata, and the files that the publisher writes, are described in the [exchanging asset descriptions](/features/asset-description-exchange/overview) feature, and in the [connectors' README :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/dcat-integration-connectors/README.md){ target=gh }.

--8<-- "snippets/abbr.md"
