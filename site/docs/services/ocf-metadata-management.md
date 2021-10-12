---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/released.md"

# OCF Metadata Management

OCF metadata management provides common services for
[Open Metadata Access Services (OMASs)](/egeria-docs/services/omas) that are supporting
the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview).

Connectors defined in the OCF are client-side Java objects.  They support a method called
`getConnectedAssetProperties`.  If the connector is created by one of the OMAS clients,
this method is configured to retrieve metadata from the same open metadata repository as
this OMAS.  The primary purpose of the OCF Metadata Management module is to support the
REST APIs behind `getConnectedAssetProperties`.  It has also grown to providing common
handlers for OMASs working with similar metadata (such as the [Asset Owner OMAS](/egeria-docs/services/omas/asset-owner/overview)).
In particular, it manages the filtering of [Assets](/egeria-docs/concepts/asset)
based on their [Governance Zones](/egeria-docs/concepts/governance-zone) and the implementation
of specific [metadata security methods](/egeria-docs/features/metadata-security) related to assets.

--8<-- "snippets/abbr.md"
