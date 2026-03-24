<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0401 Governance Definitions

The world of governance is divided into different governance domains that focus on a specific set of assets or activities.
Egeria aims to unify the metadata and governance activity across these governance domains.

![UML](0401-Governance-Definitions.svg)



## GovernanceDefinition entity

*GovernanceDefinition* describes an aspect of a governance program. They are authored in the metadata repository. They inherit from [AuthoredReferenceable](/types/0/0010-Base-Model), which means they have a unique identifier and link to external references for more information.

The *GovernanceDomainIdentifier* defines which governance domain this governance definition belongs to (0 for all). The following are examples of governance domains:

* DATA - the governance of data and its use.
* PRIVACY - the support for data privacy.
* SECURITY - the governance that ensures IT systems and the data they hold are secure.
* IT_INFRASTRUCTURE - the governance of the configuration and management of IT infrastructure and the software that runs on it.
* SOFTWARE_DEVELOPMENT - the governance of the software development lifecycle.
* CORPORATE - the governance of the organization as a legal entity.
* ASSET_MANAGEMENT - the governance of physical assets.

These values are set up as the valid values for the *domainIdentifier* attribute by the [Core Content Pack](/content-packs/core-content-pack/overview).

### GovernanceDefinition subtypes

The governance definitions are organized into specific subtypes and linked together to provide a complete description of the governance program.  The types for these more specialized definitions can be found on the following pages:

- [0405 Governance Drivers](/types/4/0405-Governance-Drivers) - describe the motivations behind the governance program.
- [0415 Governance Responses](/types/4/0415-Governance-Responses) - describe the policies that support each of the drivers.
- [0420 Governance Controls](/types/4/0420-Governance-Controls) - describe how the policies will be implemented.  This includes:

  * [0423 Security Definitions](/types/4/0423-Security-Definitions) - describes governance controls that focus on protecting the organization.
  * [0424 Governance Zones](/types/4/0424-Governance-Zones) - describes security controls that control how access to a collection of metadata is controlled.
  * [0430 Development Controls](/types/4/0430-Development-Controls) - describes governance controls that that focus on fulfilling unmet needs of the organization through the development of technology.
  * [0440 Organizational Controls](/types/4/0440-Organizational-Controls) - identity governance roles and manual procedures (such as approvals) that implement a governance control.
  * [0450 Governance Rollout](/types/4/0450-Governance-Rollout) - describes governance controls that are used when rolling out a governance program to the organization.
  * [0451 Notifications](/types/4/0451-Notifications) - describes governance controls that are used to notify people of changes, schedules and events.
  * [0462 Governance Actions](/types/4/0462-Governance-Actions) - describes governance controls that are used to implement governance actions.

## GovernedBy relationship

The *GovernedBy* relationship links the governance definitions to the elements they are governing.  These elements are [Referenceable](/types/0/0010-Base-Model), so they could be [Assets](/types/0/0010-Base-Model), [Processes](/types/0/0010-Base-Model), [Infrastructure](/types/0/0010-Base-Model), [People](/types/1/0112-People) and [Teams](/types/1/0115-Teams), [Glossary Terms](/types/3/0330-Terms), [Digital Services](/types/7/0710-Digital-Service) for example.

* *label* - the role of the governance definition with respect to the element it is governing.
* *description* - the description of how the governance is defined.

!!! info "Related types"
    * The role of leader of a governance domain is represented as a [*GovernanceOfficer*](/types/4/0445-Governance-Roles) entity.
    * The scope of a governance definition is represented through the [ScopedBy](/types/1/0120-Assignment-Scopes).

!!! info "Implementing Services"

    * The [Governance Officer API](/services/omvs/governance-officer/overview) provides the APIs for maintaining the definitions of the governance zones, governance definitions, subject area definitions and governance officers. It uses the *GovernedBy* relationship to link governance definitions with [subject area definitions](/types/4/0425-Subject-Areas) and [governance zone definitions](/types/4/0424-Governance-Zones).

--8<-- "snippets/abbr.md"