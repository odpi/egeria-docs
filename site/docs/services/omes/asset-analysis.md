<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Asset Analysis Open Metadata Engine Service (OMES)

The Asset Analysis OMES provides support for
[open discovery engines](/egeria-docs/frameworks/odf/#discovery-engine)
that are part of the [Open Discovery Service (ODF)](/egeria-docs/frameworks/odf).

## Open discovery engines

A discovery engine hosts [automated metadata discovery](../../../open-metadata-publication/website/metadata-discovery).

The Asset Analysis OMES is capable of hosting one or more
[discovery engines](/egeria-docs/frameworks/odf/#discovery-engine)
and supports a REST API to request that a discovery engine runs an
[discovery service](/egeria-docs/frameworks/odf/#discovery-service)
to analyse an [asset](/egeria-docs/concepts/asset) and to access the results.
The results of each of these
calls is a [discovery analysis report](/egeria-docs/frameworks/odf/#discovery-analysis-report).

The REST API also supports a request to a discovery engine to run a specific open discovery service
against each asset it has access to.

The discovery engine services call the
[Discovery Engine Open Metadata Access Service (OMAS)](/egeria-docs/services/omas/discovery-engine)
running in an open metadata server to retrieve information about assets and to
store the results of the discovery services.

--8<-- "snippets/abbr.md"
