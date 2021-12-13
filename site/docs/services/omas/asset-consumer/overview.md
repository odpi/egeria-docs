<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/released.md"

!!! attention "Broken Links"

    We are still working on this content -- you may find some broken links. Until resolved, You can
    find additional information in the [Egeria repository](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/access-services/asset-consumer/asset-consumer-client/docs/user)


# Asset Consumer Open Metadata Access Service (OMAS)

## Overview
The Asset Consumer OMAS provides services to an individual who wants to work
with [assets](/egeria-docs/concepts/asset) such as:

* data stores, data sets and data feeds
* reports
* APIs
* functions such as analytical services

It supports:

* the retrieval of [connection](/egeria-docs/concepts/connection) objects from the open metadata repositories.  A connection object is used to create a connector to an asset.
* the creation of a [connector](/egeria-docs/concepts/connector) based on the properties in a connection object.
* the retrieval of properties about an asset.  These properties are called the [connected asset properties](/egeria-docs/concepts/connected-asset-properties).
* the adding of feedback (comments, ratings and likes) to an asset.
* the attachment of [informal tags](/egeria-docs/concepts/informal-tag) to an asset.
* the adding of an audit log record for an asset.
* the publishing of notifications about assets on Asset Consumer OMAS's [out topic](/egeria-docs/concepts/out-topic).

Adding feedback through the Asset Consumer OMAS results in [Karma Points](/egeria-docs/concepts/karma-point) being awarded to the individual.  These are maintained in the individual's profile.  A karma point is awarded for each contribution of feedback through the API. (The awarding of Karma points is managed by the [Community Profile OMAS](/egeria-docs/services/omas/community-profile/overview).)

The connectors returned by the Asset Consumer OMAS are [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview) connectors.  The caller can use the connector to access the contents of the asset itself and the properties about the asset it is accessing.   This service is provided by the [OCF Metadata Management Common Service](/egeria-docs/services/ocf-metadata-management).

## User Guide

The Asset Consumer OMAS is designed for use by an application that is accessing data sources and services through
[connectors](/egeria-docs/concepts/connector).
These data sources and services are called [Assets](/egeria-docs/concepts/asset),
hence the name of this OMAS is **Asset Consumer**.

Typically the first action to take is to
[create the connector](creating-a-connector.md) to 
get [access to the asset content and its properties](working-with-connectors.md).
Connectors are created from
[Connection](/egeria-docs/concepts/connection)
objects.
Connection objects can be created by the calling application, or stored
in one of the open metadata repositories that are accessible to the Asset Consumer OMAS.

Alternatively, if the consumer only needs access to the asset's properties, they can use the
Asset Consumer OMAS to
[locate the identifier of the asset](locating-the-connected-asset.md)
and then [retrieve the asset properties](retrieving-asset-properties.md).

Within the asset properties are links to glossary terms.
It is possible to
[look up the full description of a term](looking-up-meanings-of-terms.md)
to further understand the asset.

There are also capabilities to 
[log messages about the asset](logging-messages-about-an-asset.md),
[add feedback to the asset](adding-feedback-to-an-asset.md)
in terms of likes, star ratings, reviews and comments,
and [add tags to the asset](tagging-an-asset.md).

## Interface choices

The Asset Consumer OMAS offers the following types of interface:

* [Java client](../../asset-consumer-client/docs/user/java-client), 
* [REST API](../../asset-consumer-server/docs/user) and 
* [Out Topic Events](../../asset-consumer-client/docs/user/java-events) for receiving events about assets.

Connectors are only available through the Java client.

## Configuration

Details of how to configure the Asset Consumer OMAS can be found [here](../../asset-consumer-server/docs/configuration)

## Scenarios

This is the list of documented scenarios:

* [Working with Connectors (overview)](working-with-connectors.md)
* [Creating a connector](creating-a-connector.md)
* [Locating the connected asset](locating-the-connected-asset.md)
* [Retrieving asset properties](retrieving-asset-properties.md)
* [Logging audit messages about an event](logging-messages-about-an-asset.md)
* [Adding Feedback to an Asset](adding-feedback-to-an-asset.md)
* [Looking up the meanings of terms assigned to an asset](looking-up-meanings-of-terms.md)
* [Adding descriptive tags to an asset](tagging-an-asset.md)


--8<-- "snippets/abbr.md"
