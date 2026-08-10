<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Open APIs

Many applications and runtimes - including Egeria's own [OMAG Server Platform](/concepts/omag-server-platform) - describe their REST APIs using the [Open API Specification](https://www.openapis.org/) (formerly Swagger) and publish that description at a well-known URL. The *Leveraging your Open APIs* solution uses this published specification to automatically build and maintain an open metadata catalog of an application's APIs, without needing any custom connector written for that particular application.

This is a much lighter-weight solution than the database and event broker connectors described elsewhere: there is no survey action service, and no dedicated *CreateAndSurvey*/*CreateAsCatalogTarget* governance action processes.  Instead, a single integration connector does the work, and it can run in two different modes depending on how it is configured.

## The Open API Cataloguer

| Connector Name | Connector Type | Purpose |
|-----------------|-----------------|---------|
| **[Open API Cataloguer :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openapi-integration-connector/README.md){ target=gh }** | [Integration Connector](/concepts/integration-connector) | Retrieves an application's Open API Specification from its swagger endpoint (`GET {serverURL}/v3/api-docs`) and builds a full [`DeployedAPI`](/types/2/0212-Deployed-APIs) schema from it - every operation, and the structure of its request, response and header content. |

This connector, its connector type and the *OpenAPIsIntegrationGroup* it runs in are delivered together in the *APIsContentPack* (see [Open APIs Content Pack](/content-packs/apis-content-pack/overview)).

### How cataloguing works

On each refresh, the connector calls `GET {serverURL}/v3/api-docs` against the application it is watching.  The JSON returned is the application's Open API Specification, describing every tag, path, operation and schema it exposes.  The connector uses this to build a complete [API schema](/types/5/0536-API-Schemas) in open metadata, all anchored to a single `DeployedAPI` asset:

* An [`Endpoint`](/types/0/0026-Endpoints) is created (or reused) for the `serverURL` itself.
* One [`DeployedAPI`](/types/2/0212-Deployed-APIs) asset is created for the whole specification (not one per tag), anchored to that endpoint via the *APIEndpoint* relationship and self-anchored, so everything catalogued beneath it is anchored to it too.  Its `qualifiedName` is derived from the server's URL, so the same API is recognized again on later refreshes rather than being duplicated.  The specification's tags are recorded as a comma-separated `tags` additional property on the asset, rather than each becoming its own asset.
* An [`APISchemaType`](/types/5/0536-API-Schemas) is created underneath the `DeployedAPI`, linked via the *Schema* relationship - this is the root of everything else.
* For every path/HTTP-verb combination, an [`APIOperation`](/types/5/0536-API-Schemas) is created (linked to the `APISchemaType` via the *APIOperations* relationship), with its `path` and `command` set from the specification, its display name taken from the operation's `operationId` (falling back to `"{COMMAND} {path}"` if none is given), and its description from the operation's `description` or `summary`.  The operation's own `summary`, `deprecated` flag and `tags` are recorded as additional properties.

### The request, response and header structure

For each `APIOperation`, the connector builds out up to three [`APIParameterList`](/types/5/0536-API-Schemas) structures, each linked to the operation via the matching relationship - only created if there is something to catalogue:

* **Request** (*APIRequest* relationship) - one [`APIParameter`](/types/5/0536-API-Schemas) for every URL parameter (path or query, not header), plus one more named "Request Body" if the operation defines one.
* **Response** (*APIResponse* relationship) - one `APIParameter` per HTTP status code the operation documents (e.g. `200`, `404`), each carrying the structure of that status code's response body underneath it.
* **Header** (*APIHeader* relationship) - a "Headers" group holding any header-passed parameters, and a "Security" group holding one entry per distinct security scheme the operation requires (falling back to the specification's global `security` requirement if the operation doesn't declare its own), deduplicated so a scheme referenced by multiple requirements only appears once.

Whichever of these creates a parameter with a request/response body attached, the connector resolves the body's schema from its `content` map - preferring `application/json` if present, otherwise using whatever content type is listed first - and then recurses into that schema's own `properties` to catalogue every nested field as a further `APIParameter`, each classified with [`TypeEmbeddedAttribute`](/types/5/0505-Schema-Attributes) so its data type (for primitives) or structure (for objects and arrays) is recorded.  A `$ref` pointing into the specification's `components.schemas` is resolved and expanded the same way; a `$ref` that is already being expanded higher up the same branch of the recursion is not re-expanded, so a circular schema (an object that refers back to itself) does not send the connector into an infinite loop.

??? info "What isn't covered yet"
    Cataloguing is purely additive: on each refresh, the connector creates any `DeployedAPI`, `APIOperation` or `APIParameter` it hasn't seen before (matched by `qualifiedName`), but it never removes or archives an element that has since disappeared from the specification - if an operation is deleted from the application, its catalogued `APIOperation` is left behind. The `templateQualifiedName` configuration property is still recognized and logged, but nothing in the connector's current implementation actually applies it when creating the `DeployedAPI` asset.

### Finding applications to catalog

Unlike the connectors described in the other *Leveraging* solutions, the Open API Cataloguer does not use [catalog targets](/concepts/catalog-target).  Instead, its connection can be set up in one of two ways:

* **A fixed endpoint** - the connector's [`Connection`](/concepts/connection) specifies a single `endpoint.address`, and the connector only ever monitors that one `serverURL`.  This is the pattern shown in the [connector's own configuration example](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openapi-integration-connector/README.md#configuration){ target=gh }, and is the way to point the connector at an application that is not itself managed by Egeria.
* **Automatic discovery** - if no endpoint is configured (which is how the *APIsContentPack* sets the connector up by default), the connector instead searches open metadata for every existing [`Endpoint`](/types/0/0026-Endpoints) whose network address starts with `http`, and tries the `/v3/api-docs` request against each one in turn.  Any that respond with a valid Open API Specification get catalogued; the rest are silently ignored.

This second mode is why the *Open APIs* solution is described as extending [Leveraging Egeria's runtime](/egeria-solutions/leveraging-egeria/overview) rather than standing alone: the [OMAG Server Platform Cataloguer](/egeria-solutions/leveraging-egeria/overview#omag-server-platform-cataloguer) already creates an `Endpoint` for every OMAG Server Platform it catalogues.  Once that has happened, the Open API Cataloguer picks up the same endpoint on its next refresh (the *APIsContentPack* sets a refresh interval of 60 minutes) and, because an OMAG Server Platform publishes its own `/v3/api-docs`, automatically builds the `DeployedAPI` and its full operation schema for that platform - with no separate configuration step required.

The connector also recognizes a `templateQualifiedName` configuration property, though see the note above - it is not currently applied to anything the connector creates.

??? info "Why the technology type restriction in the content pack is broader in practice"
    The reference data shipped in the *APIsContentPack* associates the Open API Cataloguer with the [OMAG Server Platform](/concepts/omag-server-platform) technology type, since that is the primary scenario it is built for. The connector code itself is not restricted to Egeria: it will catalog any [Software Server](/concepts/deployed-implementation-type) whose network address is already known to open metadata and which answers `/v3/api-docs` with a valid specification - Egeria's own runtime is simply the one it is set up to find automatically out of the box.

## Related information

* [Leveraging Egeria's runtime](/egeria-solutions/leveraging-egeria/overview) - describes the OMAG Server Platform Cataloguer, whose catalogued endpoints are what the Open API Cataloguer discovers automatically.
* [Open APIs Content Pack](/content-packs/apis-content-pack/overview) - the content pack that delivers this connector and its reference data.
* [0212 Deployed APIs](/types/2/0212-Deployed-APIs) and [0536 API Schemas](/types/5/0536-API-Schemas) - the open metadata types used to describe the cataloged APIs and their operations.
* [Integration Connector](/concepts/integration-connector) - background on how integration connectors like this one are configured and run.

--8<-- "snippets/abbr.md"
