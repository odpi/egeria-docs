<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuration document properties managed by Egeria

The following properties do not need be configured explicitly, the admin services will manage them automatically.

![Egeria Managed Properties](egeria-managed-properties.svg)

## Local Server Id

The localServerId is a unique identifier for the server, it is used when accessing resource that require their callers to supply a unique identifier.  For example, when an OMAG server is accessing an Apache Kafka topic, it needs to reliably identify itself with a callerId so that the Kafka server knows which events it has received and which it has not.  The localServerId is used for this purpose when accessing the [open metadata repository cohort topics](/concepts/cohort-events) for example.

## Local Server Name

The localServerName is a unique name for the server.  This is a name you choose, and the administration services maintains the name in the configuration document.

## Local Server Type

The local server type is a classification of the type of the server based on the sections of the configuration document that have been configured.  Leave it blank and Egeria will fill it in on server start up.  There is also an administration call to query the type of server using the following call:

--8<-- "snippets/admin/calls/get-server-type-classification.md"

## Audit Trail

The audit trail lists the admin commands that have been issued against the configuration document.  It is useful in tracking down when changes occurred, particularly when diagnosing problems in the configuration.

--8<-- "snippets/abbr.md"
