<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Exchanging Asset Descriptions

An [asset](/concepts/asset) describes a [digital resource](/concepts/digital-resource) that is of value to the organization: a data set, a file, a database, an API.  Many organizations need to exchange the descriptions of their assets with others.  A government agency is obliged to list the data that it makes available to the public; a research organization shares its data sets with its partners; an enterprise harvests the open data it relies on into its own catalog so that it can be found, governed and traced alongside its internal data.

Egeria exchanges these descriptions using the *Data Catalog Vocabulary (DCAT)*.  Descriptions written by other organizations are catalogued as assets in open metadata, and the assets that an organization chooses to make public are written out as DCAT descriptions, along with a DCAT catalog that lists them, ready to be harvested by a data portal.

## The Data Catalog Vocabulary (DCAT)

The W3C [Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-3/) is the standard that governments and many other organizations use to describe the data assets that they make available: what each dataset is about, who publishes it, how it is licensed and where it can be obtained.  It is the basis of profiles such as DCAT-AP in Europe and DCAT-US in the United States.  DCAT describes:

* a **dataset** (`dcat:Dataset`) - a collection of data that is published or curated by a single organization;
* a **distribution** (`dcat:Distribution`) - a specific form in which a dataset can be obtained, such as a CSV file to download or an API to call;
* a **dataset series** (`dcat:DatasetSeries`) - a group of datasets that are published separately but belong together, such as the annual editions of a survey;
* a **data service** (`dcat:DataService`) - an API that provides access to one or more datasets;
* a **catalog** (`dcat:Catalog`) - a curated list of datasets, data services and other catalogs.

Egeria supports **DCAT version 3** in its **JSON-LD** serialization.  Documents in Turtle or RDF/XML need to be converted to JSON-LD before they are passed to Egeria.  Any arrangement of JSON-LD can be read: nested, flattened, with prefixes or with full IRIs.  Egeria never retrieves a JSON-LD context from the network.  A document should embed its context; one that refers to a remote context is read using the standard prefixes and names of the DCAT terms.  This is enough to read the `data.json` catalogs published by US government agencies.

## Mapping to open metadata

The resources described in a DCAT document are catalogued as follows.

| DCAT | Open metadata |
| --- | --- |
| `dcat:Dataset` | [*DataSet*](/types/2/0210-Data-Stores) asset |
| `dcat:Distribution` | [*DataFile*](/types/2/0220-Files-and-Folders) asset (if it has a `dcat:downloadURL`) or [*DataStore*](/types/2/0210-Data-Stores) asset (if it only has a `dcat:accessURL`), [anchored](/features/anchor-management/overview) to the data set and linked to it by a *DataSetContent* relationship.  A distribution that is removed from the dataset's description is deleted. |
| `dcat:DatasetSeries` | *DataSet* asset linked to its member data sets by *DataSetContent* relationships |
| `dcat:DataService` | [*DeployedAPI*](/types/2/0212-Deployed-APIs) asset, with an [*Endpoint*](/types/0/0026-Endpoints) for each `dcat:endpointURL`, linked to the data sets it serves by *DataSetContent* relationships |
| `dcat:Catalog` | [*CollectionFolder*](/types/0/0021-Collections) whose members are the catalog's datasets, data services and nested catalogs |
| `dct:title`, `dct:description`, `dct:identifier`, `dcat:version`, `dcat:landingPage` | *displayName*, *description*, *identifier*, *versionIdentifier*, *url* |
| `dcat:keyword` | [*SearchKeyword*](/types/0/0012-Search-Keywords) |
| `dct:publisher` | *Organization* linked by a [*ScopedBy*](/types/1/0120-Assignment-Scopes) relationship |
| `dct:creator` | *authors* |
| `dcat:contactPoint` | [*ContactDetails*](/types/1/0111-Contact-Details) linked by a *ContactThrough* relationship |
| `dct:license` | *LicenseType* linked by a [*License*](/types/4/0481-Licenses) relationship |
| `dct:conformsTo`, `foaf:page` | [*ExternalReference*](/types/0/0014-External-References) linked by an *ExternalReferenceLink* relationship labelled `conformsTo` or `documentation` |
| Everything else | Additional properties whose names begin `dcat.` |

Each element is given a qualified name built from the IRI of the resource it represents (or the resource's identifier or title if it has no IRI), so sending a description again updates the elements rather than creating new ones.  Properties that are not part of DCAT, such as those added by the DCAT-AP and DCAT-US profiles, are preserved in the `dcat.otherProperties` additional property and written out again when the asset is published.

## Receiving descriptions

A DCAT document reaches Egeria in one of four ways:

* **In a file** - the *DCAT Files Receiver* scans directories for `.jsonld` and `.json` files that describe DCAT resources.  By default, it scans the `loading-bay/dcat` directory under the platform's working directory.  Other directories are added by attaching their file folders to the connector as `directoryToMonitor` [catalog targets](/concepts/catalog-target).
* **On an Apache Kafka topic** - the *DCAT Event Receiver* treats each event received from the topics attached to it as `topicToMonitor` catalog targets as a DCAT document.
* **Through an integration daemon's REST API** - a document is sent to the [integration daemon](/concepts/integration-daemon) through its `publish-dcat-document` request, or through the *publish-document* request of the [Asset Catalog OMVS](/services/omvs/asset-catalog/overview/#exchanging-dcat-descriptions-of-assets).
* **Directly through the Asset Catalog OMVS** - the *import-document* request catalogs a document straight away, without an integration daemon, and returns the unique identifiers of the elements that describe its resources.

In the first three cases, the document is passed to the *DCAT listeners* registered in the integration daemon.  The *DCAT Cataloguer* is such a listener: it catalogs what each document describes, using the mapping above.

## Publishing descriptions

The *DCAT Publisher* is told which assets to publish through the [collections](/concepts/collection) attached to it as [catalog targets](/concepts/catalog-target) with the catalog target name `publishingCatalog`.  Each of these *publishing catalogs* is published as a separate DCAT catalog.  An asset is published if it is a member of a publishing catalog, or of a collection folder nested in it.  Any type of collection can be used; it does not need to be a root collection.  The [DCAT Content Pack](/content-packs/dcat-content-pack/overview) supplies the *DCAT Publishing Catalog* root collection (`Egeria::DCATPublishingCatalog`) and attaches it to the publisher, so it works as soon as the content pack is loaded.  To publish an asset, add it to a publishing catalog; to withdraw it, remove it.  Collection folders nested in a publishing catalog are a way to organize the published assets, and a further catalog is published by attaching another collection to the publisher.

The publisher writes to the directory named in the network address of the endpoint in its connection.  By default, this is the `distribution-hub/dcat-catalog` directory under the platform's working directory.  Each catalog has its own subdirectory, named after the collection and the first eight characters of its unique identifier (for example, `DCAT-Publishing-Catalog-9b07a6ef`).  On each refresh, the publisher writes the following files to each catalog's subdirectory.  A file is only written when its content has changed.

* `catalog.jsonld` - the publishing catalog as a `dcat:Catalog`, along with the description of every published asset.
* `datasets/<name>.jsonld` - one file for each asset published as a `dcat:Dataset`.
* `data-services/<name>.jsonld` - one file for each asset published as a `dcat:DataService`.

The file of an asset that has been removed from a publishing catalog is deleted.  When a collection is detached from the publisher, its subdirectory is deleted.

Only collections are published: any other kind of element attached as a catalog target is ignored and reported in the audit log.  If a collection cannot be published, the publisher carries on with its other collections and withdraws none of the published catalogs on that refresh, so a temporary problem does not remove a catalog that a data portal is harvesting.

The type of the asset determines how it is described:

* A *DeployedAPI* asset is published as a data service.
* A *DataSet* asset is published as a dataset whose distributions are the assets that supply its data.
* Any other type of asset is published as a dataset with a single distribution.

An asset that was catalogued from a DCAT description keeps its original IRI; any other asset is identified by `urn:uuid:` followed by its unique identifier.

The publisher has one configuration property:

| Configuration property | Description |
| --- | --- |
| `defaultPublisher` | The name of the organization to show as the publisher of an asset that is not linked to an organization. |

The DCAT description of a single asset, whether or not it is in the publishing catalog, is returned by the *dcat-document* request of the [Asset Catalog OMVS](/services/omvs/asset-catalog/overview/#exchanging-dcat-descriptions-of-assets).

## Egeria's DCAT support

The [Open Integration Framework (OIF)](/frameworks/oif/overview) provides Java beans for catalogs, datasets, dataset series, distributions and data services, a formatter that reads and writes their JSON-LD serialization, the mapping between the documents and open metadata, and a distribution mechanism in the [integration daemon](/concepts/integration-daemon) that mirrors its [Open Lineage support](/features/lineage-management/overview/#egerias-open-lineage-support):

* An [integration connector](/concepts/integration-connector) may register a *DCAT listener* with its integration context to receive every document that is published to the daemon.
* An integration connector may publish a document for the other listeners registered in the same daemon.
* The integration daemon's REST API (`publish-dcat-document`) and the Asset Catalog OMVS allow external callers to publish documents into the daemon.

The [DCAT connectors :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/dcat-integration-connectors/README.md){ target=gh } supplied by Egeria are packaged in the [DCAT Content Pack](/content-packs/dcat-content-pack/overview), in an [integration group](/concepts/integration-group) called `Egeria:IntegrationGroup:DCAT`:

1. The **DCAT Files Receiver** scans directories and publishes the new and changed documents it finds.
2. The **DCAT Event Receiver** publishes the documents it receives from Apache Kafka topics.
3. The **DCAT Cataloguer** registers a listener and catalogs each document it receives.
4. The **DCAT Publisher** writes a DCAT catalog for each collection attached to it as a `publishingCatalog` catalog target, along with the DCAT description of each asset in the collection.

An organization can therefore drop the catalog published by a partner into a directory and have its datasets appear as assets in open metadata, while the assets that its own teams add to a publishing catalog are written out in the standard format for others to harvest.

--8<-- "snippets/abbr.md"
