---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0424 Governance Zones

A **GovernanceZone** entity describes a collection of Assets that are used, or processed in a specific way.
The governance zone definitions define the governance zones in use in the organization and
how they are used.  It is possible to then attach governance policies and controls to the zone
definitions using the [GovernedBy](0401-Governance-Definitions.md) relationship to show how assets assigned
to a zone should be managed and governed.

Linking the zones in a hierarchy implies that the governance definitions linked to a zone that is higher in
the hierarchy also apply to all governance zones linked underneath it.

An Asset may belong to many Governance Zones.  This is defined in the **AssetZoneMembership** classification.
A classification is used rather than a relationship between Asset and GovernanceZoneDefinition to improve
the performance of the asset processing since the classification flows with the Asset.

![UML](0424-Governance-Zones.svg)

There is more information on governance zones in [governance zoning](/features/governance-zoning/overview/).

??? deprecated "Deprecated types"
    - **ZoneGovernance** - use [GovernedBy](0401-Governance-Definitions.md).

--8<-- "snippets/abbr.md"