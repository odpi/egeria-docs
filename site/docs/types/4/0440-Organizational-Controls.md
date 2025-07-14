<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0440 Organizational Controls

Organizational controls describe governance controls that are implemented through people, organizational structures and responsibilities plus manual procedures and rules.  *0440* defines the description of the business domain where the organizational controls are performed.

![UML](0440-Organizational-Controls.svg)

Linked to the *OrganizationalControl* via the [*GovernanceDefinitionScope*](/types/4/0401-Governance-Definitions) relationship are the business capabilities that are part of the scope of the control.

## BusinessCapability entity

*BusinessCapability* describes the business responsibility or services provided by a team in an organization.  It is linked to the owning team using the *BusinessCapabilityTeam* relationship.

## BusinessCapabilityType enum

*BusinessCapabilityType* lists the broad categories of business capability.

## BusinessCapabilityTeam relationship


## DigitalSupport relationship



## DigitalResourceOrigin classification

*[Assets](/types/0/0010-Basic-Model)* entities describe [digital resources](/concepts/digital-resource) used by an organization.  The *DigitalResourceOrigin* classification describes the part of the organization that the resource originated in.  For example, it may show that a data set with personal information originated from the Swiss part of the organization and is therefore subject to specific controls.

??? deprecated "Deprecated types"
    - *BusinessCapabilityControls* relationship is deprecated in favour of the more generic [*GovernanceDefinitionScope*](/types/4/0401-Governance-Definitions).

--8<-- "snippets/abbr.md"