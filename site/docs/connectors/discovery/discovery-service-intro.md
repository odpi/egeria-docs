<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *open discovery service* is a component that performs specific analysis of the contents of a [digital resource](/concepts/resource) on request.  The aim of the open discovery service is to enable a detailed picture of the properties of a resource to be built up.

Each time an open discovery service runs, it creates a new [discovery analysis report](/concepts/discovery-analysis-report) linked off of the digital resource's [Asset](/concepts/asset) metadata element that records the results of the analysis.  

![Asset with discovery analysis reports](/guides/developer/open-discovery-services/asset-to-discovery-analysis-reports.svg)
> Each time an open discovery service runs to analyse a digital resource, a new discovery analysis report is created and attached to the resource's asset.  If the open discovery service is run regularly, it is possible to track how the contents are changing over time.

The *discovery analysis report* contains one or more sets of related properties that the discovery service has discovered about the resource, its metadata, structure and/or content.  These are stored in a set of [*discovery annotations*](/concepts/discovery-analysis-report/#discovery-annotations) linked off of the discovery analysis report.

An open discovery service is designed to run at regular intervals to gather a detailed perspective on the contents of the digital resource and how they are changing over time.  Each time it runs, it is given access to the results of previously run open discovery services, along with a review of these findings made by individuals responsible for the digital resource (such as stewards, owners, custodians).

??? info "Operation of an open discovery service"
    --8<-- "docs/guides/developer/open-discovery-services/operation-of-a-discovery-service.md"

??? info "Runtime for an open discovery service"
    Open discovery services are packaged into [Open Discovery Engines](/concepts/open-discovery-engine) that run in the [Asset Analysis OMES](/services/omes/asset-analysis/overview) hosted in an [Engine Host](/concepts/engine-host).  

    The metadata repository interface for metadata discovery tools is implemented by the [Discovery Engine OMAS](/services/omas/discovery-engine/overview) that runs in a [Metadata Access Server](/concepts/metadata-sccess-server).

    An open discovery service may be triggered by a REST call to the Asset Analysis OMES, via an [Engine Action](/concepts/engine-action) or as part of a [governance action process](/concepts/governance-action-process).

    ![Open Discovery Service](/connectors/discovery/discovery-service.svg)

