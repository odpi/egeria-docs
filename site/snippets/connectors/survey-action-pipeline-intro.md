<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

There is a lot of common functions that are used repeatedly during the surveying process.

A *survey action pipeline* is a specialized implementation of a [survey action service](/concepts/survey-action-service) that runs a set of survey action services against a single [digital resource](/concepts/digital-resource).  The implementation of the pipeline determines the order that these services are run. 

![Survey action pipeline example](/frameworks/saf/survey-action-pipeline-example.svg)

Each service in the pipeline is able to access the results of the services that have run before it through the [survey context](/frameworks/saf/overview/#survey-context).  The combined results of the pipeline are grouped into a single [survey report](/concepts/survey-report) linked off of the asset.

The aim of the survey action pipeline is to enable reusable survey action service implementations to be choreographed together for different types of digital resource.

