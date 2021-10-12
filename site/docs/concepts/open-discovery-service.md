<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Discovery Service

An open discovery service is a component that performs analysis of the contents of a specific
resource and adds the results to a [discovery analysis report](/egeria-docs/concepts/discovery-analysis-report)
linked off of the resources's [Asset](/egeria-docs/concepts/asset) on request.

It is implemented as a specialized [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview)
connector.  The interface and base class are provided by the [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview).

A discovery service is initialized with a connector to the Asset it is to analyze and details of
the results of other discovery services that have run before it if it is part of a
[discovery pipeline](#discovery-pipeline).

## Discovery Pipeline

A discovery pipeline is a specialized implementation of an open discovery service
that runs a set of discovery services against a single asset.  The implementation of
the discovery pipeline determines the order that these discovery services are run.

The aim of the discovery pipeline is to enable a detailed picture of the properties
of an asset to be built up by the discovery services it calls.  Each discovery service
is able to access the results of the discovery services that have run before it.

--8<-- "snippets/abbr.md"