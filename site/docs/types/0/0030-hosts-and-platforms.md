<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0030 Hosts and Platforms

The host and platform metadata entities provide a simple model for the
IT infrastructure (nodes, computers, etc) that data resources are hosted on.

![UML](0030-hosts-and-platforms.svg)

## ITInfrastructure

*`ITInfrastructure`* is a type of [`Asset`](/egeria-docs/types/0/0010-base-model/#asset).

## Host

A *`Host`* is an IT infrastructure concept associated with the hardware running the systems. It provides a mechanism for describing a unit of hardware that provides the ability to host software servers.

The host can be linked to its location through the [`AssetLocation`](/egeria-docs/types/0/0025-locations/#assetlocation) relationship.

## OperatingPlatform

The *`OperatingPlatform`* is an informational structure to describe the operating system of the host. Many hosts could have the same operating platform.

--8<-- "snippets/abbr.md"
