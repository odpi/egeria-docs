<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Product Manager API

The Product Manager API provides a REST API to support user interfaces (UIs)
relating to the definition and maintenance of digital products and digital product families.

## Key Features

The Product Manager API supports the following key features:

* **Digital Product Creation**: Create a [digital product](/concepts/digital-product) in a single request, optionally linking it to its product manager, community, folders and product families, guiding questions, product asset, licenses and governance definitions, and data specification.
* **Subscription Types**: Add *one-time*, *periodic* or *ongoing-update* [subscription](/concepts/digital-subscription) types to a digital product.  Each creates a [notification type](/concepts/notification-type) that is serviced by the Baudot Subscription Manager, together with the governance action process that consumers run to subscribe.
* **Digital Product Dependency Management**: Link and unlink dependent digital products to represent product hierarchies and usage.
* **Product Manager Assignment**: Assign and detach product managers to digital products to define responsibility and ownership.
* **Bitol Support**: Publish [Bitol](https://bitol.io) Open Data Product Standard (ODPS) and Open Data Contract Standard (ODCS) documents to an [integration daemon](/concepts/integration-daemon) for cataloguing and distribution, and generate the ODPS document for a digital product, or the ODCS document for a data sharing agreement, directly from open metadata.  See [digital product management](/features/digital-product-management/overview).

## Further information

* [Product Manager API Overview](https://egeria-project.org/services/omvs/product-manager/overview/)
* [Digital Product Concept](https://egeria-project.org/concepts/digital-product/)

Sample requests for the REST API can be found in `Egeria-api-product-manager.http`.

--8<-- "snippets/abbr.md"






