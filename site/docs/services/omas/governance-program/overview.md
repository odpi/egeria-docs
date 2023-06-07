<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Governance Program Open Metadata Access Service (OMAS)

The Governance Program OMAS provides APIs and events for tools and applications focused on defining a transformation strategy, planning support for a regulation and/or developing a [governance program](/guides/planning/governance-program/overview) for your organization.

## Governance domains

[Governance domains](/guides/planning/governance-program/overivew/#governance-domains) are the areas of an organization's operation that need a specific governance focus.  Governance domains are represented by *[Governance Domain Descriptions](/types/4/0401-Governance-Definitions)* that are referenced by the *domainIdentifier* property.  This is an integer and by convention "0" means "applies to all domains".

Governance domains are managed through the [GovernanceDomainManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceDomainManager.html) client implementing the [GovernanceDomainInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceDomainInterface.html)

It is possible to set up a default list of domains using the [`createStandardGovernanceDomains()`](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceDomainInterface.html) method. This will give you the following governance domain definitions:

| Domain Identifier | Domain Name | Description                                                                                                           |
| :-------- | :-------- |:----------------------------------------------------------------------------------------------------------------------|
| 1 | DATA | The governance of data and its use. |
| 2 | PRIVACY | The support for data privacy. |
| 3 | SECURITY | The governance that ensures IT systems and the data they hold are secure. |
| 4 | IT_INFRASTRUCTURE | The governance of the configuration and management of IT infrastructure and the software that runs on it. |
| 5 | SOFTWARE_DEVELOPMENT | The governance of the software development lifecycle.|
| 6 | CORPORATE | The governance of the organization as a legal entity.|
| 7 | ASSET_MANAGEMENT | The governance of physical assets.| 


## Governance role

Governance roles identify the additional responsibilities that exist in the organization in order to support the governance domain.  The governance roles are set up during the work to establish the governance domain.  People are appointed to these roles (many of which are part-time, augmenting the existing roles in the organization) as the governance domain is rolled out.

Governance roles are set up through the [GovernanceRoleManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceRoleManager.html) client that implements the [GovernanceRolesInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceRolesInterface.html).  People can also be appointed to the governance roles through the [Community Profile OMAS](/services/omas/community-profile/overview) since they are types of *PersonRoles* and all methods that work with person roles can be used to work with governance roles.

## Subject areas

Subject areas are topics or domains of knowledge that are of interest to the governance leaders.  

Governance Program OMAS provides an [interface to create subject area definitions](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/SubjectAreasInterface.html) that is implemented by the [SubjectAreaManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/SubjectAreaManager.html) client.  The work is then handed off to the subject area owners:

* [Subject Area OMAS](/services/omas/subject-area/overview) supports the definition of glossary terms for subject areas.  
* [Digital Architecture OMAS](/services/omas/digital-architecture/overview) supports the definition of reference data and quality rules for the subject area.
* [Asset Manager OMAS](/services/omas/asset-manager/overview) supports the exchange of subject area information with other catalogs and quality tools.

!!! education "Further information"
    
    * [Common Data Definitions](/practices/common-data-definitions/overview) describes the management and use of subject areas.
    
    * The [Defining Subject Areas](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview/) scenario for Coco Pharmaceuticals walks through the process of setting up.
    
    * There are two code samples associated with this set of subject areas:
    
        * [Setting up the subject area definitions :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/access-services-samples/governance-program-client-samples/governance-subject-area-sample){ target=gh }
        * [Setting up glossary categories for each subject area :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/access-services-samples/subject-area-client-samples/subject-area-definition-sample){ target=gh } ready for subject area owners to start defining glossary terms associated with their subject area.


## Governance Definitions

A [*Governance Definition*](/types/4/0401-Governance-Definition) is a metadata element that describes the context or purpose for an activity that supports the organization's operation.  Governance definitions can be maintained and linked through the [GovernanceDefinitionManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceDefinitionManager.html) client which supports the [GovernanceDefinitionsInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceDefinitionsInterface.html)


## Governance classification, tagging and linking

One of the ways to reduce the cost of governance is to define groups of similar assets/resources along with the governance definitions that apply to members of the group.  This avoids having to make decisions on how to manage each asset/resource.  The cataloguing process just needs to work out which group(s) to place the asset in.  Labels such as classifications, and tags of different types are used to identify these group assignments.  When a governance process is operating on the asset/resource, it looks up the labels and follows the governance definitions for the group.

The different types of labels used to group assets/resources are used for different purposes and may indicate how official they are:

* [Governance Zones](/concepts/governance-zone) group assets according to their use.  They are typically is used for [controlling visibility to the resource's asset definition](/features/governance-zoning/overview). Governance zones are managed through the [GovernanceZoneManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceZoneManager.html) client implementing the [GovernanceZonesInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceZonesInterface.html).

* [Governance Classifications](#setting-up-the-levels-for-your-governance-classifications) define the groups used for specific types of governance.

    * Confidence Governance Classification defines the level of confidence that should be placed in the accuracy of related data items.  This limits the scope that the data can be used in.
    * Confidentiality Governance Classification defines the level of confidentiality or secrecy needed with particular data.
    * Criticality Governance Classification defines how critical the related resources are to the continued operation of the organization.
    * Impact Governance Classification defines how much of an impact a particular situation is to the operation of the organization.
    * Retention Governance Classification defines how long a resource (typically data) must be retained by the organization.

* [License Types](/types/4/0481-Licenses) define the contract aka (terms and conditions) that define how the asset/resource can be used. License 
types and the linking to assets is managed through the [RightsManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/RightsManager.html) client implementing the [RightsManagementInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/RightsManagementInterface.html).

* [Certification Types](/types/4/0482-Certifications) define specific characteristics of an asset/resource that has been verified for a particular span of time.  Certification types and the process of certifying assets is managed through the [CertificationManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/CertificationManager.html) client implementing the [CertificationManagerInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/CertificationManagementInterface.html)

* [SecurityTags](/concepts/security-tags) identify labels and properties that are used in determining which data protection rules should be executed when particular data is requests. They can be attached to assets or schema elements depending on the scope of data that the security tags apply to. The synchronized access control feature describes how security tags are set up and used.

The labels may be assigned directly to the asset, or to elements, such as schemas and glossary terms that are linked to the asset.  Security tags are managed through the [Asset Owner OMAS](/services/omas/asset-owner/overview).

## Setting up the levels for your governance classifications

The values used in governance classifications show the specific group that the classified asset belongs to.  Often an organization has their own levels defined ,and they can be set up in [`GovernanceClassificationLevel`](/types/4/0421-Governance-Classification-Levels/) definitions.

Egeria has a set of default values that can be set up using the [`createStandardGovernanceClassificationLevels`](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceClassificationLevelInterface.html) method.  Alternatively you can set up your own values through the [GovernanceClassificationManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceClassificationLevelManager.html) client.

## Governance Status Identifiers

Many entities, relationships and classifications have a *statusIdentifier* property.  This indicates the confidence in the setting up of the element.  Generally,

* Positive values relate to statuses which mean the element is ok to use.
* Zero means the element has just been created, but not vetted, so use with caution.
* Negative values mean that the element is not to be trusted because it is, for example, obsolete or incorrect.

The meanings of specific *statusIdentifiers* can be set up using the [GovernanceStatusLevelManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceStatusLevelManager.html) that implements the [GovernanceStatusLevelInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceStatusLevelInterface.html).

## Measures and metrics

As important aspect of the governance program is the ability to [measure its effectiveness](/guides/planning/goverance-program/overview/#measures-and-metrics) and identify the assets that are delivering the highest value, or operating with the greatest efficiency etc.  Governance metrics can be managed through the [GovernanceMetricsManager](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/GovernanceMetricsManager.html) client that supports the [GovernanceMetricsInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceMetricsInterface.html)


## Related OMASs

- The [Community Profile OMAS](/services/omas/community-profile/overview) supports the definition of the profiles for people and teams that will support the governance program.  These are linked to the governance roles defined by the governance program.

* The [Project Management OMAS](/services/omas/project-management/overview) supports the rollout of the governance program by commissioning campaigns and projects to implement the governance controls and the collection of measurements to assess the success of the program.

* The [Digital Architecture OMAS](/services/omas/digital-architecture/overview) provides the setup of the digital landscape that supports the governance program.  This includes the definitions of the information supply chains and solution components that support the organization's activities.

* The [Digital Service OMAS](/services/omas/digital-service/overview) documents the business capabilities along with their digital services that are supported by the governance program.

* The [Governance Engine OMAS](/services/omas/governance-engine/overview) supports the implementation of technical controls and the choreography of their execution.

* The [Stewardship Action OMAS](/services/omas/stewardship-action/overview) supports the stewards as they manage the exceptions detected to the governance program.
  
* The [Data Privacy OMAS](/services/omas/data-privacy/overview) supports the operational aspects of managing privacy as part of the organization's activities.

* The [Subject Area OMAS](/services/omas/subject-area/overview) supports the definitions of the vocabularies associated with a subject area.

* The [Data Manager OMAS](/services/omas/data-manager/overview) support the automated cataloging of assets and configuration of technology that is managing them.

* The [Security Manager OMAS](/services/omas/security-manager/overview) support the configuration of technology that is managing the security of assets.

* The [Security Officer OMAS](/services/omas/security-officer/overview) support the definitions of users and groups and related definitions that make up the user directory.

* The [Asset Manager OMAS](/services/omas/asset-manager/overview) supports the automated exchange of governance definitions between catalogs and asset managers to create a consistent rollout of governance requirements.
  
* The [Asset Owner OMAS](/services/omas/asset-owner/overview) supports the linking of governance definitions and classifications to assets to define how they should be governed.

* The [Asset Consumer OMAS](/services/omas/asset-consumer/overview) supports the visibility of the governance definitions and classification by consumers of the assets.


--8<-- "snippets/abbr.md"
