<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# DCAT Content Pack

The *DCATContentPack* contains the connector definitions for the integration connectors that work with the W3C [Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-3/) supplied in the *omag-server-platform* distribution.  DCAT is the standard that governments and many other organizations use to describe the data assets that they make available: what each dataset is about, who publishes it, how it is licensed and where it can be obtained.  The content pack is designed to provide a good starting point for exchanging these descriptions between Egeria's [asset](/concepts/asset) catalog and the data portals that publish and harvest them.

The connectors work with the **JSON-LD** serialization of DCAT version 3.  Documents in Turtle or RDF/XML need to be converted to JSON-LD before they are passed to Egeria.

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module and is found in the `DCATContentPack.omarchive` file.

## Contents

The content pack defines the *DCATIntegrationGroup* (`Egeria:IntegrationGroup:DCAT`) and registers four integration connectors with it:

| Connector | Role |
| --- | --- |
| DCAT Files Receiver | Scans file directories (by default `loading-bay/dcat`, plus the file folders attached as `directoryToMonitor` catalog targets) for `.jsonld` and `.json` files that describe DCAT resources, and publishes new and changed documents to the DCAT listeners in the integration daemon. |
| DCAT Event Receiver | Publishes each event received from the Apache Kafka topics attached as `topicToMonitor` catalog targets as a DCAT document to the DCAT listeners in the integration daemon. |
| DCAT Cataloguer | Listens for DCAT documents and catalogs the catalogs, datasets, dataset series and data services that they describe. |
| DCAT Publisher | Writes the DCAT description of each asset in the publishing catalog, and of the catalog itself, to the file system (by default `distribution-hub/dcat-catalog`, plus the file folders attached as `publishDirectory` catalog targets), ready to be harvested by a data portal. |

The receivers and the cataloguer are linked through the integration daemon's DCAT listener mechanism in the same way as the [Open Lineage connectors](/content-packs/open-lineage-content-pack/overview) and the [Bitol connectors](/content-packs/bitol-content-pack/overview).  Documents may also be published to the daemon through its REST API and through the [Asset Catalog OMVS](/services/omvs/asset-catalog/overview), which is also able to catalog a document directly and return the DCAT description of any asset.

## Choosing the assets to publish

The DCAT Publisher is told which assets to publish through a [collection](/concepts/collection): the *publishing catalog*.  An asset is published if it is a member of this collection, or of a collection folder nested in it.  By default, the publishing catalog is the *DCAT Publishing Catalog* root collection (`Egeria::DCATPublishingCatalog`).  This collection is supplied by the [Core Content Pack](/content-packs/core-content-pack/overview), so it is present whether or not the DCAT Content Pack is loaded.  To publish an asset, add it to this collection; to withdraw it, remove it.

The publisher has two configuration properties:

| Configuration property | Description |
| --- | --- |
| `publishingCatalog` | The qualified name (or display name) of the collection that lists the assets to publish.  The default is `Egeria::DCATPublishingCatalog`. |
| `defaultPublisher` | The name of the organization to show as the publisher of an asset that is not linked to an organization. |

## Further information

The mapping between DCAT and open metadata, and the files that the publisher writes, are described in the [exchanging asset descriptions](/features/asset-description-exchange/overview) feature, and in the [connectors' README :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/dcat-integration-connectors/README.md){ target=gh }.

--8<-- "snippets/abbr.md"
