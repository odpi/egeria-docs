---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Data engine proxy services

The data engine proxy services support the behavior of the [data engine proxy](/concepts/data-engine-proxy).

![Figure 1 - Data Engine Proxy Server](data-engine-proxy-server.svg)

This server supports intercommunication from a **Data Engine** and
the [Data Engine OMAS](/services/omas/data-engine/overview).

A data engine is a technology that processes data to either copy it to a new location,
transform it to a new format, so it can be consumed in a different way and/or
derive new values from the data.  The data engine may be retrieving data from
multiple data sources and also writing to multiple data sources.

Information about the data that the data engine is consuming and creating, along with
details of the processing it is doing is needed to provide lineage for the
data sources.  This is why it is important that we capture information about a data engine's
processing in open metadata.

The [Data Engine OMAS](/services/omas/data-engine/overview) provides the API for capturing the processing of a
data engine.

Where a Data Engine does not have direct support for publishing details of its processing to the
Data Engine OMAS, a data engine proxy connector can be written for the Data Engine that
uses the Data Engines native APIs and events to capture the required 
information and then translates it into calls to the Data Engine OMAS.

The data engine proxy connector runs inside a Data Engine Proxy Server
on the OMAG Server Platform.  The data engine proxy services are 
responsible for hosting the data engine proxy connector.

# Further information

- Configuring the Data Engine Proxy Server following the [admin guide](/guides/admin/servers/configuring-a-data-engine-proxy-server/).

- Configuring Data Engine Proxy with [IBM Data Stage connector](https://github.com/odpi/egeria-connector-ibm-information-server/tree/master/datastage-adapter).

--8<-- "snippets/abbr.md"