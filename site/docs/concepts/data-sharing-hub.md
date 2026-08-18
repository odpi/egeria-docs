<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Data Sharing Hub

A *data sharing hub* is a [collection](/concepts/collection) of data [assets](/concepts/asset) that hold authoritative data and are available for sharing - provided the requester satisfies the requirements laid down by the data owner.

The hub is the shop window.  Rather than each team negotiating access to each data store individually, the assets that an organization or team is willing to share are gathered in one place, with the conditions attached to them.  A consumer can then see what is available before asking for anything.

## Requesting data

A *data sharing request* is the corresponding ask: a request to another party that they share data.  It is a type of [to do](/concepts/to-do), because satisfying it involves work by a person or a process.  The request tracks its own status and gathers the detail of what was asked for - typically a [data specification](/concepts/data-specification) describing the data required - together with the resulting data sharing agreement and any supporting resources.

Where the sharing arrangement is ongoing rather than one-off, it is usually expressed as a [digital product](/concepts/digital-product) with [digital subscriptions](/concepts/digital-subscription), which add the delivery schedule and service level commitment on top of the agreement.

???+ info "Additional information"
    * The *DataSharingHub* and *DataSharingRequest* types are described in [Model 0705 Data Sharing](/types/7/0705-Data-Sharing).
    * The [Collection Manager API](/services/omvs/collection-manager/overview) provides the interface for working with data sharing hubs.

--8<-- "snippets/abbr.md"
