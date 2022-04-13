<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *open discovery service* is a component that performs specific analysis of the contents of a [digital resource](/concepts/resource) on request.  Each time it runs, it creates a new [discovery analysis report](/concepts/discovery-analysis-report) linked off of the digital resource's [Asset](/concepts/asset) metadata element.  

![Asset with discovery analysis reports](/guides/developer/open-discovery-services/discovery-analysis-report-structure.svg)

The *discovery analysis report* contains one or more sets of related properties that the discovery service has discovered about the resource, its metadata, structure and/or content.  These are stored in a set of [*discovery annotations*](/guides/developer/open-discovery-services/overview/#discovery-annotations) linked off of the discovery analysis report.

![Structure of discovery analysis reports](/guides/developer/open-discovery-services/discovery-analysis-report-structure.svg)

An open discovery service is designed to run at regular intervals to gather a detailed perspective on the contents of the digital resource and how they are changing over time.  Each time it runs, it is given access to the results of previously run open discovery services, along with an review of these findings made by individuals responsible for the digital resource (such as stewards, owners, custodians).

!!! info "Operation of an open discovery service"
    --8<-- "docs/guides/developer/open-discovery-services/operation-of-a-discovery-service.md"

!!! info "Runtime for an open discovery service"
    Open discovery services run in the [Asset Analysis OMES](/services/omes/asset-analysis) that is hosted in a [Engine Host](/concepts/engine-host).

    ![Open Discovery Service](/connectors/discovery/discovery-service.svg)


--8<-- "snippets/abbr.md"