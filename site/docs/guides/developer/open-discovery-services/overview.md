<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Writing an Open Discovery Service

The [Open Discovery Framework (ODF)](/frameworks/odf/overview) provides components and interfaces for building open discovery services.   

An [Open Discovery Service](/guides/developer/open-discovery-services/discovery-service) provides specific analysis of the metadata and contents of
a [digital resource](/concepts/resource) on request.
The result is one or more sets of related properties that the discovery service has
discovered about the resource, its metadata, structure and/or content.
These are stored in a set of [Discovery Annotations](/guides/developer/open-discovery-services/discovery-annotation) linked off of a
[Discovery Analysis Report](/guides/developer/open-discovery-services/discovery-analysis-report).  The discovery analysis report
is linked off of the resource's asset definition in the open metadata repository.

Open discovery services run in the [Asset Analysis OMES](/services/omes/asset-analysis) that is hosted in a [Engine Host](/concepts/engine-host).


## Core Concepts

* [Discovery Analysis Report](/guides/developer/open-discovery-services/discovery-analysis-report)
* [Discovery Analysis Report Store](/guides/developer/open-discovery-services/discovery-analysis-report-store)
* [Discovery Annotation](/guides/developer/open-discovery-services/discovery-annotation)
* [Discovery Annotation Store](/guides/developer/open-discovery-services/discovery-annotation-store)
* [Discovery Asset Catalog Store](/guides/developer/open-discovery-services/discovery-asset-catalog-store)
* [Discovery Asset Store](/guides/developer/open-discovery-services/discovery-asset-store)
* [Discovery Configuration Server](/guides/developer/open-discovery-services/discovery-configuration-server)
* [Discovery Context](/guides/developer/open-discovery-services/discovery-context)
* [Discovery Engine](/guides/developer/open-discovery-services/discovery-engine)
* [Discovery Pipeline](/guides/developer/open-discovery-services/discovery-pipeline)
* [Discovery Request Type](/guides/developer/open-discovery-services/discovery-request-type)
* [Discovery Server](/guides/developer/open-discovery-services/discovery-server)
* [Discovery Service](/guides/developer/open-discovery-services/discovery-service)

## Example implementations

The definition of the connector interfaces for discovery services is defined in the [open-discovery-services :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/frameworks/open-discovery-framework/src/main/java/org/odpi/openmetadata/frameworks/discovery){ target=gh } module.

There are implementations of discovery services in the [discovery-service-connectors](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh } module.

---8<-- "snippets/abbr.md"