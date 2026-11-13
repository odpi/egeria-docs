<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open APIs Content Pack

The *APIsContentPack* contains the connector definition for building an API catalog from applications and servers that publish their REST APIs using the [OpenAPI specification](https://www.openapis.org/) through a swagger interface.  It configures a single integration connector that extracts each API's specification and keeps a catalog of its operations, parameters and data structures up to date.  The connector is supplied in the *omag-server-platform* distribution.

The content pack is found in the `APIsContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the technology types and the design library folders.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module, and the connector is in the [openapi-integration-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openapi-integration-connector){ target=gh } module.

## How it works

The *OpenAPICataloguer* calls `GET {serverURL}/v3/api-docs` on each server it is monitoring to retrieve the server's OpenAPI specification.  It creates a *DeployedAPI* asset for the specification, with an *APIOperation* for each combination of path and operation (GET, POST, PUT, DELETE), and parameter lists for each operation's request, response and headers.  The beans in the specification's `components/schemas` section are catalogued once per API and shared by the parameters that use them.

The connector monitors the endpoint named in its connection or, when no endpoint is configured - as is the case for the connection in this pack - every catalogued *Endpoint* whose network address starts with `http`.  It looks for these endpoints when it starts, and picks up new ones from the events reporting that an endpoint has been created.  So cataloguing a server with an `http` endpoint, for example from a template, is enough to have its APIs catalogued.  The connector is linked to the *OMAG Server Platform* technology type, so it builds a catalog of Egeria's own APIs as the platforms are catalogued.

!!! note "Catalog targets"
    The descriptions of the connector in this pack say that it catalogs the servers "attached as catalog targets", but the connector does not read catalog targets: it works from endpoints as described above.

This pack defines no templates, governance engines or governance action processes.

## Integration connectors

The pack defines the *OpenAPIsIntegrationGroup* (`Egeria:IntegrationGroup:OpenAPIs`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| OpenAPIIntegrationConnector | `OpenAPICataloguer` (user `apicatnpa`, refreshes every 10080 minutes - once a week) | Catalogs the REST APIs of the servers whose endpoints support the swagger API. |

## Solution blueprint

--8<-- "snippets/blueprints/content-packs/open-apis-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    The Open APIs Content Pack is loaded automatically into the *active-metadata-store* of Egeria's quickstart.  For other deployments, load it into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then catalog each server whose APIs you want in the catalog, with an endpoint giving its `http` or `https` network address, and the *OpenAPICataloguer* picks it up.

    [Leveraging APIs](/egeria-solutions/leveraging-apis/overview) describes how to build an API catalog with Egeria.

--8<-- "snippets/abbr.md"
