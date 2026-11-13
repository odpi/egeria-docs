<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Digital Products Content Pack

The *OpenMetadataDigitalProductsContentPack* packages the content of the open metadata ecosystem into [digital products](/concepts/digital-product) that other teams and tools can subscribe to.  It configures the connectors and governance services that build the *Open Metadata Digital Product Catalog*, keep its products up to date, and deliver the product data to each subscriber.  The connectors and services are supplied in the *omag-server-platform* distribution.

The content pack is found in the `OpenMetadataDigitalProductsContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the *Digital Product Catalogs* root collection (`Egeria::DigitalProductCatalogsRoot`), the *EgeriaGovernance* governance engine, the *Tabular Data Set* technology type and the *Digital Product Catalog Actions* folder that the governance action types are filed in.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

The content pack does not contain the product catalog itself.  Instead, it configures the *Jacquard Digital Product Loom*, named after [Joseph Marie Jacquard](https://en.wikipedia.org/wiki/Joseph_Marie_Jacquard), whose punched cards controlled the patterns woven by a loom.  When Jacquard starts, it creates the *Open Metadata Digital Product Catalog* (`DigitalProductCatalog::Jacquard::Open Metadata Digital Product Catalog`) as a member of the *Digital Product Catalogs* root collection, along with the *Open Metadata Digital Product Catalog Solution* blueprint that describes the components involved, and then defines and maintains the products in the catalog.  Jacquard will not start unless its secrets store is configured.  Each product presents an extract of open metadata as a [tabular data set](/concepts/tabular-data-set).  Alongside the products, the catalog carries a product glossary, the [perspectives](/types/1/0145-Perspectives) the products support, and a data dictionary describing their data fields.  Some families grow with the ecosystem: Jacquard generates a product for each valid metadata value set and each reference data set it finds.

Each product offers a choice of [subscriptions](/concepts/digital-subscription).  Subscribing runs the *create-digital-subscription* governance action type, which creates the digital subscription; cancelling runs *cancel-digital-subscription*.  The *Baudot Subscription Manager*, named after [Emile Baudot](https://en.wikipedia.org/wiki/%C3%89mile_Baudot), whose telegraph code carried messages to their destinations, is handed each product's [notification types](/concepts/notification-type) by Jacquard as catalog targets.  On each refresh it sends the notifications that each notification type's subscribers are due, and changes to a notification type's monitored resources are notified as they arrive.  The data itself is delivered by the *Wedgwood Data Provisioner*, named after [Thomas Wedgwood](https://en.wikipedia.org/wiki/Thomas_Wedgwood_(photographer)), into the destination that the subscriber named - a CSV file, a database table or a Kafka topic, for example.

The [Harvest and Publish](/patterns/harvest-and-publish/overview#the-open-metadata-digital-product-catalog) pattern describes the product families, the products restricted to the security team, and the subscription choices in detail.

## Integration connectors

The pack defines the *JacquardIntegrationGroup* (`Egeria:IntegrationGroup:Jacquard`), a dynamic [integration group](/concepts/integration-group).

| Connector | Runs as | Purpose |
|---|---|---|
| JacquardDigitalProductLoomIntegrationConnector | `JacquardDigitalProductLoom` (user `jacquardnpa`, refreshes every 60 minutes) | Defines and maintains the digital products, and the catalog that holds them, from the content of the open metadata repositories.  Its data set connectors open their own REST clients to the platform, so it is configured with a secrets store (`secrets/egeria-servers.omsecrets`, collection `JacquardDigitalProductLoom`) that supplies a bearer token.  Its `subscriptionManagerGUID` configuration property names the Baudot connector. |
| BaudotDigitalProductSubscriptionManagerIntegrationConnector | `BaudotDigitalProductSubscriptionManager` (user `baudotnpa`, refreshes every 10 minutes) | Notifies the subscribers of the digital products' notification types, on its refresh cycle and as their monitored resources change. |

## Governance services

The governance services are registered with the *EgeriaGovernance* engine (defined in the Core Content Pack), which runs in an [engine host](/concepts/engine-host).  Each request type has a [governance action type](/concepts/governance-action-type) of the same name (for example `EgeriaGovernance::create-digital-subscription`) in the data sharing governance domain.

| Request type | Governance service | Purpose |
|---|---|---|
| `create-digital-subscription` | Create Open Metadata Digital Product Subscription Governance Action Service | Creates a digital subscription and links it to the subscriber (if supplied).  The digital subscription's GUID is passed on as a new action target. |
| `cancel-digital-subscription` | Cancel Open Metadata Digital Product Subscription Governance Action Service | Cancels a digital subscription. |
| `provision-subscription` | Wedgwood Open Metadata Digital Product Provisioning Pipeline Governance Action Service | Provisions the data identified in a digital subscription to the requested destination. |

The three governance action types are listed as resources of the *Tabular Data Set* technology type, with the resource uses *Create Subscription*, *Cancel Subscription* and *Provision Resource*.

## The Open Metadata Digital Product Catalog

This graph of the catalog, taken from Egeria's quickstart, shows its top two levels: the product families, the data dictionary, the perspectives and the glossary.  The families that are restricted to the security team are not visible to the quickstart's user, so they do not appear.

--8<-- "snippets/collections/digital-products/open-metadata-digital-product-catalog-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then add the *JacquardIntegrationGroup* to an integration daemon, and make sure the secrets store named in Jacquard's connection holds a bearer token for the platform.

    Consumers browse and subscribe through the [Product Catalog](/services/omvs/product-catalog/overview) API, while the products and their families are defined and maintained through the [Product Manager](/services/omvs/product-manager/overview) API.

--8<-- "snippets/abbr.md"
