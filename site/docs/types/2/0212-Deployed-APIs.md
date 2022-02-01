---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0212 Deployed APIs

Deployed APIs are [Assets](/types/0/0010-Base-Model) that provide remote access to [DeployedSoftwareComponents](/types/2/0215-Software-Components).
The **APIEndPoint** identifies the network address used to call the API
(defined in [Endpoint](/types/0/0026-Endpoints)).  

![UML](0212-Deployed-APIs.svg)

The classifications **RequestResponseInterface**, **ListenerInterface** and **PublisherInterface** can be used to
describe the style of the API.  They can appear in combination on a single API.
The structure of the API's interface is described in the [APISchema](/types/5/0536-API-Schemas).

The definition of the API's operation, parameters and responses are supported by the [API Schema Types](/types/5/0536-API-Schemas).

--8<-- "snippets/abbr.md"