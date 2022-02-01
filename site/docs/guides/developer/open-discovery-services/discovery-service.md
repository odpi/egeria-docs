<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Discovery Service

A discovery service is a component that performs analysis of specific
[Asset](/concepts/asset) on request.

It is implemented as a specialized [Open Connector Framework (OCF)](/frameworks/ocf/overview)
connector.  The interface and base class are provided by the [Open Discovery Framework (ODF)](/frameworks/odf/overview).

A discovery service is initialized with a connector to the Asset it is to analyze and details of
the results of other discovery services that have run before it if it is part of a
[discovery pipeline](discovery-pipeline.md).

The results of a discovery service are stored in [Annotations](discovery-annotation.md).


---8<-- "snippets/abbr.md"