---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging Egeria's runtime

The solution for your Egeria infrastructure is contained in the [Egeria Content Pack](/content-packs/egeria-content-pack/overview).  It makes use of its own services to ensure that Egeria's operation is observable and manageable.  The heart of the solution is the *OMAGServerPlatformCataloguer*.  This [integration connector](/concepts/integration-connector) maintains an open metadata representation of the configuration and status of the OMAG Server Platforms and the OMAG Servers they host.  These definitions, and the reference data also contained in the content pack, are used by the [Runtime Manager API](/services/omvs/runtime-manager/overview) to access live status from the runtime.

--8<-- "snippets/blueprints/content-packs/egeria-content-pack-solution-blueprint-mermaid-graph.md"

## OMAG Server Platform Cataloguer

When the Egeria Content Pack is loaded into a [metadata access store](/concepts/metadata-access-store), the OMAG Server Platform Cataloguer is automatically started in a connected [Integration Daemon](/concepts/integration-daemon).  Its first act is to extract details of the platform supporting its metadata access store, create an open metadata representation of the platform with a connection, and attach it to itself as a [catalog target](/concepts/catalog-target).  This means that it will regularly check the configuration and status of that platform and maintain the open metadata representation of it.  Additional platforms can be created and attached as required.  A platform can be deleted from open metadata to stop the cataloguing process.

The open metadata created by the OMAG Server Platform Cataloguer is pretty comprehensive.  The diagram below summarizes the platform description for the [Quickstart Environment](/egeria-workspaces/quick-start/overview).

--8<-- "snippets/it-assets/omag-server-platform-mermaid-graph.md"

And these are the server descriptions:

--8<-- "snippets/it-assets/qs-view-server-on-https-localhost:9443-mermaid-graph.md"
--8<-- "snippets/it-assets/qs-metadata-store-on-https-localhost:9443-mermaid-graph.md"
--8<-- "snippets/it-assets/qs-integration-daemon-on-https-localhost:9443-mermaid-graph.md"
--8<-- "snippets/it-assets/qs-engine-host-on-https-localhost:9443-mermaid-graph.md"

???+ info "Further details"
    * The [design of the OMAG Server Platform Cataloguer](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/egeria-system-connectors) gives more detail on how it works.
    * The [Open APIs solution](/egeria-solutions/leveraging-apis/overview) will catalog the services of the OMAG Server Platforms it detects in the open metadata repositories.
    * The [Files solution](/egeria-solutions/leveraging-files/overview) includes the **SecretsStoreCataloguer** integration connector, which catalogs secrets collections stored in various secret stores.  This includes the secrets stores used by the OMAG Server Platform.  This will give details of the user access configured for the platform.

--8<-- "snippets/abbr.md"