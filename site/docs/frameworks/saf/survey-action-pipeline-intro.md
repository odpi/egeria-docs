<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

There is a lot of common functions that are used repeatedly during the discovery process.

An *open discovery pipeline* is a specialized implementation of an [open discovery service](/concepts/open-discovery-service) that runs a set of open discovery services against a single [digital resource](/concepts/resource).  The implementation of the open discovery pipeline determines the order that these open discovery services are run. 

![Open discovery pipeline example](/guides/developer/open-discovery-services/open-discovery-pipeline-example.svg)

Each open discovery service in the pipeline is able to access the results of the open discovery services that have run before it through the [discovery context](/guides/developer/open-discovery-services/overview/#discovery-context).  The combined results of the open discovery pipeline are grouped into a single [discovery analysis report](/concepts/discovery-analysis-report) linked off of the asset.

The aim of the open discovery pipeline is to enable reusable open discovery service implementations to be choreographed together for different types of digital resource.

