
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0424 Governance Zones

A **GovernanceZone** entity describes a collection of elements that are used, or processed in a specific way.
The governance zone definitions define the governance zones in use in the organization and
how they are used.  It is possible to then attach governance policies and other controls to the zone
definitions using the [GovernedBy](0401-Governance-Definitions.md) relationship to show how elements assigned
to a zone should be managed and governed.

Linking the zones in a hierarchy implies that the governance definitions linked to a zone that is higher in
the hierarchy also apply to all governance zones linked underneath it.  However, the access control checks
implemented by the [security connectors](/features/metadata-security/overview) have no awareness of these relationship which means that such parent-child relationships for access control need to be manually managed in the user directory.

An element may belong to many Governance Zones.  This is defined in the *ZoneMembership* classification.
A classification is used rather than a relationship between the element and the GovernanceZone definition to improve
the performance of the processing since the classification flows with the element.

![UML](0424-Governance-Zones.svg)

There is more information on governance zones in [governance zoning](/features/governance-zoning/overview/).

## GovernanceZone entity

The *GovernanceZone* entity is a [SecurityAccessControl](/types/4/0423-Security-Definitions) that describes a collection of elements that have the same visibility.

## ZoneHierarchy relationship

The *ZoneHierarchy* relationship links a parent zone to its children.

## ZoneMembership classification

The *ZoneMembership* classification is used to record the zones that an element is a member of.

## ZoneMembershipProfile classification

The *ZoneMembershipProfile* classification is used to record the number of elements in the attached governance zone for each open metadata type.

* *totalMembership* is the number of elements in the zone.
* *typeMembership* is a map from open metadata type name to the number of elements of that type in the zone.
* *analysisTime* is the time when these counts were made.

???+ info "Related information"

    * [Governance Zones in Action](/features/governance-zoning/overview/)
    * [Model 0423 Security Definitions](/types/4/0423-Security-Definitions) show how the security lists assign to a governance zone are captured in open metadata.
    * The access control enabled by the governance zones is implemented in the [security connectors](/features/metadata-security/overview).
    * The *ZoneMembershipProfile* classification is updated by a [Lovelace service](/patterns/metadata-insight/overview).



--8<-- "snippets/abbr.md"