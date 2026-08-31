<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Data Sharing Hub

A *data sharing hub* is a [collection](/concepts/collection) of data [assets](/concepts/asset) that hold authoritative data and are available for sharing - provided the requester satisfies the requirements laid down by the data owner.

The hub is the shop window.  Rather than each team negotiating access to each data store individually, the assets that an organization or team is willing to share are gathered in one place, with the conditions attached to them.  A consumer can then see what is available before asking for anything.

## Describing what is on offer

A shop window is only useful if the goods in it are labelled.  Membership of a hub therefore carries an expectation: the metadata describing the members is actively maintained and improved, rather than captured once and left to age.

Egeria takes that on.  The contents of each member are catalogued, so that what is inside it is visible and not just the store itself, and the members are surveyed repeatedly so that what is recorded about the data reflects the data as it is now rather than as it was when the member joined the hub.

From those descriptions a [data dictionary](/concepts/data-dictionary) is derived and anchored to the hub: an abstracted list of the [data fields](/concepts/data-field) and [data structures](/concepts/data-structure) found across the members.  A data field identifies similar data wherever it occurs, so a consumer can ask for the data they want once rather than once per data store, without needing to know which database or file holds it.  The generated dictionary carries the fields and their types; the descriptions that explain what the values mean are added by the people who know.  Each entry stays linked to the schema elements it was derived from, so a request expressed against the dictionary can be traced back to the data that satisfies it.

The [Harvest and Publish](/patterns/harvest-and-publish/overview) pattern describes how this is kept up to date, and how a hub feeds a catalog of [digital products](/concepts/digital-product) once the demand for particular data becomes clear.

## Requesting data

A *data sharing request* is the corresponding ask: a request to another party that they share data.  It is a type of [to do](/concepts/to-do), because satisfying it involves work by a person or a process.  The request tracks its own status and gathers the detail of what was asked for - typically a [data specification](/concepts/data-specification) describing the data required - together with the resulting data sharing agreement and any supporting resources.

Where the sharing arrangement is ongoing rather than one-off, it is usually expressed as a [digital product](/concepts/digital-product) with [digital subscriptions](/concepts/digital-subscription), which add the delivery schedule and service level commitment on top of the agreement.

???+ info "Additional information"
    * The *DataSharingHub* and *DataSharingRequest* types are described in [Model 0705 Data Sharing](/types/7/0705-Data-Sharing).
    * The [Collection Manager API](/services/omvs/collection-manager/overview) provides the interface for working with data sharing hubs.
    * The [Harvest and Publish](/patterns/harvest-and-publish/overview) pattern covers data sharing hubs alongside the Open Metadata Digital Product Catalog.

--8<-- "snippets/abbr.md"
