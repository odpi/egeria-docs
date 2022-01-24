<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


An *open discovery pipeline* is a specialized implementation of an [open discovery service](/egeria-docs/guides/developer/open-discovery-services/overview) that runs a set of open discovery services against a single [resource](/egeria-docs/concepts/resource).  The implementation of the open discovery pipeline determines the order that these open discovery services are run.

The aim of the open discovery pipeline is to enable a detailed picture of the properties of a resource to be built up by the open discovery services it calls.  Each open discovery service is able to access the results of the open discovery services that have run before it.

The results created by each open discovery service in a pipeline are stored in [Annotations](/egeria-docs/guides/developer/open-discovery-services/discovery-annotation) that are available through the [discovery context](/egeria-docs/guides/developer/open-discovery-services/discovery-context).  The combined results of the open discovery pipeline are grouped into the [discovery analysis report](/egeria-docs/guides/developer/open-discovery-services/discovery-analysis-report).


---8<-- "snippets/abbr.md"