<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *open discovery service* is a component that performs analysis of the contents of a specific [digital resource](/egeria-docs/concepts/resource) and adds the results to a [discovery analysis report](/egeria-docs/concepts/discovery-analysis-report) linked off of the resources's [Asset](/egeria-docs/concepts/asset) metadata element.

![Open Discovery Service](/egeria-docs/connectors/discovery/discovery-service.svg)

An open discovery service is implemented as a specialized [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview) connector.  The interface and base class are provided by the [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview).  It is initialized with a connector to the Asset it is to analyze and details of the results of other discovery services that have run before it if it is part of a [discovery pipeline](/egeria-docs/concepts/open-discovery-service/#open-discovery-pipeline).


--8<-- "snippets/abbr.md"