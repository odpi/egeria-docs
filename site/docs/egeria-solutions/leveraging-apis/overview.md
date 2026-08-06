---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Open APIs

Many applications and runtimes - including Egeria's own [OMAG Server Platform](/concepts/omag-server-platform) - describe their REST APIs using the [Open API Specification](https://www.openapis.org/) (formerly Swagger) and publish that description at a well-known URL. The *Leveraging your Open APIs* solution uses this published specification to automatically build and maintain an open metadata catalog of an application's APIs, without needing any custom connector written for that particular application.

This is a much lighter-weight solution than the database and event broker connectors described elsewhere: there is no survey action service, and no dedicated *CreateAndSurvey*/*CreateAsCatalogTarget* governance action processes.  Instead, a single integration connector does the work, and it can run in two different modes depending on how it is configured.

## The Open API Cataloguer

| Connector Name | Connector Type | Purpose |
|-----------------|-----------------|---------|
| **[Open API Cataloguer :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openapi-integration-connector/README.md){ target=gh }** | [Integration Connector](/concepts/integration-connector) | Retrieves an application's Open API Specification from its swagger endpoint (`GET {serverURL}/v3/api-docs`) and creates a [`DeployedAPI`](/types/2/0212-Deployed-APIs) asset for each API tag it finds. |

This connector, its connector type and the *OpenAPIsIntegrationGroup* it runs in are delivered together in the *APIsContentPack* (see [Open APIs Content Pack](/content-packs/apis-content-pack/overview)).

### How cataloguing works

On each refresh, the connector calls `GET {serverURL}/v3/api-docs` against the application it is watching.  The JSON returned is the application's Open API Specification, describing every tag, path and operation it exposes.  The connector uses this to build open metadata:

* An [`Endpoint`](/types/0/0026-Endpoints) is created (or reused) for the `serverURL` itself.
* A [`DeployedAPI`](/types/2/0212-Deployed-APIs) asset is created for each *tag* in the specification, anchored to that endpoint via the *APIEndpoint* relationship.  Its `qualifiedName` is derived from the tag name and the server's URL, so the same API is recognized again on later refreshes rather than being duplicated.

The connector also works out, for every combination of path and HTTP verb (GET, POST, PUT, DELETE), the qualified name a corresponding [`APIOperation`](/types/5/0536-API-Schemas) schema element would need - but at the time of writing, the call that actually creates that `APIOperation` element in open metadata is still commented out in the connector's source, so **only the API-level (`DeployedAPI`) cataloguing is active today**; operation-level detail is not yet populated.

### Finding applications to catalog

Unlike the connectors described in the other *Leveraging* solutions, the Open API Cataloguer does not use [catalog targets](/concepts/catalog-target).  Instead, its connection can be set up in one of two ways:

* **A fixed endpoint** - the connector's [`Connection`](/concepts/connection) specifies a single `endpoint.address`, and the connector only ever monitors that one `serverURL`.  This is the pattern shown in the [connector's own configuration example](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openapi-integration-connector/README.md#configuration){ target=gh }, and is the way to point the connector at an application that is not itself managed by Egeria.
* **Automatic discovery** - if no endpoint is configured (which is how the *APIsContentPack* sets the connector up by default), the connector instead searches open metadata for every existing [`Endpoint`](/types/0/0026-Endpoints) whose network address starts with `http`, and tries the `/v3/api-docs` request against each one in turn.  Any that respond with a valid Open API Specification get catalogued; the rest are silently ignored.

This second mode is why the *Open APIs* solution is described as extending [Leveraging Egeria's runtime](/egeria-solutions/leveraging-egeria/overview) rather than standing alone: the [OMAG Server Platform Cataloguer](/egeria-solutions/leveraging-egeria/overview#omag-server-platform-cataloguer) already creates an `Endpoint` for every OMAG Server Platform it catalogues.  Once that has happened, the Open API Cataloguer picks up the same endpoint on its next refresh (the *APIsContentPack* sets a refresh interval of 60 minutes) and, because an OMAG Server Platform publishes its own `/v3/api-docs`, automatically adds `DeployedAPI` assets for its services - with no separate configuration step required.

The connector recognizes one configuration property, `templateQualifiedName`, which lets you override the template used when creating the `DeployedAPI` assets it discovers.

??? info "Why the technology type restriction in the content pack is broader in practice"
    The reference data shipped in the *APIsContentPack* associates the Open API Cataloguer with the [OMAG Server Platform](/concepts/omag-server-platform) technology type, since that is the primary scenario it is built for. The connector code itself is not restricted to Egeria: it will catalog any [Software Server](/concepts/deployed-implementation-type) whose network address is already known to open metadata and which answers `/v3/api-docs` with a valid specification - Egeria's own runtime is simply the one it is set up to find automatically out of the box.

## Related information

* [Leveraging Egeria's runtime](/egeria-solutions/leveraging-egeria/overview) - describes the OMAG Server Platform Cataloguer, whose catalogued endpoints are what the Open API Cataloguer discovers automatically.
* [Open APIs Content Pack](/content-packs/apis-content-pack/overview) - the content pack that delivers this connector and its reference data.
* [0212 Deployed APIs](/types/2/0212-Deployed-APIs) and [0536 API Schemas](/types/5/0536-API-Schemas) - the open metadata types used to describe the cataloged APIs and their operations.
* [Integration Connector](/concepts/integration-connector) - background on how integration connectors like this one are configured and run.

--8<-- "snippets/abbr.md"
