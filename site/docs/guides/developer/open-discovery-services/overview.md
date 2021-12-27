<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Writing an Open Discovery Service

The [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview) provides components and interfaces for building open discovery services.   

An [Open Discovery Service](/egeria-docs/guides/developer/open-discovery-services/discovery-service) provides specific analysis of the metadata and contents of
a [digital resource](/egeria-docs/concepts/resource) on request.
The result is one or more sets of related properties that the discovery service has
discovered about the resource, its metadata, structure and/or content.
These are stored in a set of [Discovery Annotations](/egeria-docs/guides/developer/open-discovery-services/discovery-annotation) linked off of a
[Discovery Analysis Report](/egeria-docs/guides/developer/open-discovery-services/discovery-analysis-report).  The discovery analysis report
is linked off of the resource's asset definition in the open metadata repository.

Open discovery services run in the [Asset Analysis OMES](/egeria-docs/services/omes/asset-analysis) that is hosted in a [Engine Host](/egeria-docs/concepts/engine-host).


## Core Concepts

* [Discovery Analysis Report](/egeria-docs/guides/developer/open-discovery-services/discovery-analysis-report)
* [Discovery Analysis Report Store](/egeria-docs/guides/developer/open-discovery-services/discovery-analysis-report-store)
* [Discovery Annotation](/egeria-docs/guides/developer/open-discovery-services/discovery-annotation)
* [Discovery Annotation Store](/egeria-docs/guides/developer/open-discovery-services/discovery-annotation-store)
* [Discovery Asset Catalog Store](/egeria-docs/guides/developer/open-discovery-services/discovery-asset-catalog-store)
* [Discovery Asset Store](/egeria-docs/guides/developer/open-discovery-services/discovery-asset-store)
* [Discovery Configuration Server](/egeria-docs/guides/developer/open-discovery-services/discovery-configuration-server)
* [Discovery Context](/egeria-docs/guides/developer/open-discovery-services/discovery-context)
* [Discovery Engine](/egeria-docs/guides/developer/open-discovery-services/discovery-engine)
* [Discovery Pipeline](/egeria-docs/guides/developer/open-discovery-services/discovery-pipeline)
* [Discovery Request Type](/egeria-docs/guides/developer/open-discovery-services/discovery-request-type)
* [Discovery Server](/egeria-docs/guides/developer/open-discovery-services/discovery-server)
* [Discovery Service](/egeria-docs/guides/developer/open-discovery-services/discovery-service)

## Example implementations

There are implementations of discovery services in the [discovery-service-connectors](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors) module.

---8<-- "snippets/abbr.md"