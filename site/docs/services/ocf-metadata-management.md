---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# OCF Metadata Management

OCF metadata management implements the *Connected Asset Services* from the [Open Connector Framework (OCF)](/frameworks/ocf/overview). These services are available through all [Open Metadata Access Services (OMASs)](/services/omas).

## Connected Asset Services

An OCF connector supports a method called [`getConnectedAssetProperties`](/concepts/connected-asset-properties).  It is intended to return metadata about its resource.  By default this method returns null because it needs to be configured with the location of the metadata repositor(y/ies) it is to call. If the connector is created by one of the OMAS clients listed above, this method is configured to retrieve metadata from the same open metadata repository as the OMAS.  This metadata includes details of the structure, origin, meaning and governance requirements associated with the resource.


--8<-- "snippets/abbr.md"
