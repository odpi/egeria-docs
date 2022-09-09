<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Setting up your Governance Program

An organization's governance program described the cross-cutting initiatives that ensure the organization is operating efficiently and ethically with the most optimal use of resources.  Egeria supports open metadata definitions that aid the management and exchange of information that drives the governance program.

The governance program is divided into governance domains.

## Governance domains

Governance domains are the areas of an organization's operation that need a specific governance focus.  For example, a governance domain may be driving a transformation strategy, planning support for a regulation, driving an efficiency campaign or developing an assurance program for your organization.

A governance domain typically involves the ongoing cooperation of multiple teams from different business areas.  There is often a [business strategy](#governance-definitions) and a [set of targets](#measures-and-metrics) associated with the domain since its purpose is to provide some level of improvement or benefit to the organization.

Each domain is typically the responsibility of a different executive in the organization.  Different domains may use slightly different terminology and often run different tools but in fact they are very similar in the way that they operate.  Egeria allows the teams from the different governance domains to collaborate and benefit from each other's efforts.

??? info "Examples of governance domains"
    The governance domains can vary in scope and importance to the business.  In the example below, *Corporate Governance* ensures that the business operates legally. It is the key focus of the board or directors and includes financial reporting.  

    At the heart of the organization's operation are three governance domains that are often run separately, but in fact are highly dependent on one another:

    * *Data (or Information) Governance* focuses on the appropriate use and management of data.
    * *Information Security (InfoSec)* focuses on the security of the IT Systems (and sometimes the physical security of buildings and plant).
    * *IT Infrastructure* ensures systems are correctly set up and managed.so they deliver the level of service required by the business.  This governance domain often uses a taylored version of IT Infrastructure Library (ITIL).

    Software development needs governance to ensure it is properly designed, built and tested - and fit of purpose.  This governance is typically guided by a software development method, such as *Agile Development* and covers all aspects of the software development lifecycle.

    There are other domains that are more specialized.  For example:

    * *Privacy* focusses on compliance with data subject privacy.  It interacts with the data governance, software development lifecycle and IT Infrastrcuture domains.
    * *Human Capital Management* combines Human Resources (HR) and the management team of the organization to ensure the people they employ receive the training and support to build the right skills to support the business.
    * *Risk Management* assesses and, where necessary mittigates against the risks that may impact the organization.  It is often lead by the finance team because the level of risk can affect their credit rating.  However in some industries, such as banking, where the reporting and management of risk is covered by specific regulations, there is a separate organization that interfaces with the regulators.
    * *Physical Asset Management* manages the physical buildings, furnature, machinery, computers etc that the organization owns.  It is responsible for maintenance and replacement of these items.
    * *Product Assurance* ensures the products that the organization sells meet regulatory requirements and match the ethos of the organization.
    * *Procurement* focussed on the policies and rules assicuated with the products and services bought by people across the organization.  There may be a seprate procurement team that interacts with suppliers to ensure bulk discounts and quality.  They would work with other leaders in the organization to ensure the approach matches the needs of the business.
    * *Sustainability* is a relatively new governance domain that focuses on the effective use of resources to improve long-term sustainability of the organization's operations.
    
    ![Figure 2](governance-domain-examples.svg)
    > **Figure 2:** Examples of different governance domains within an organization.

Governance domains are represented by [*Governance Domain Descriptions*](/types/4/0401-Governance-Definitions).  These definitions include the *domainIdentifier* property, a *displayName* and a *description*.   The *domainIdentifier* property is an integer and by convention "0" means "applies to all domains".  For example:

| Domain Identifier | Display Name                   | Description                                                                                               |
|:------------------|:-------------------------------|:----------------------------------------------------------------------------------------------------------|
| 0                 | All                            | Governance program leadership and shared definitions.                                                     |
| 1                 | Data                           | The governance of data and its use.                                                                       |
| 2                 | Privacy                        | The support for data privacy.                                                                             |
| 3                 | Information Security (InfoSec) | The governance that ensures IT systems and the data they hold are secure.                                 |
| 4                 | IT Infrastructure              | The governance of the configuration and management of IT infrastructure and the software that runs on it. |
| 5                 | Software Development Lifecycle | The governance of the software development lifecycle.                                                     |
| 6                 | Corporate Governance           | The governance of the organization as a legal entity.                                                     |
| 7                 | Physical Asset Management      | The governance of physical assets.                                                                        | 

!!! education "Defining governance domains"
Governance domain descriptions can be defined in an [Open Metadata Archive](/concepts/open-metadata-archive) or through the Open Metadata Access Services (OMASs).

    * The [Governance Program OMAS](/services/omas/goverance-program/overview) supports the setting up of governance domains.
    * The [egeria-samples.git repository](https://github.com/odpi/egeria-samples) includes a sample called [Sample metadata archives for Coco Pharmaceuticals](https://github.com/odpi/egeria-samples/tree/master/sample-metadata-archives/coco-metadata-archives) that creates open metadata archives with basic definitions for Coco Pharmaceuticals.  This includes the definition of this organization's governance domains with their communities and governance officers.


## Governance Roles



![Governance Roles](governance-roles.svg)


!!! education "Defining governance roles"
Governance roles can be defined 
    * The [Governance Program OMAS](/services/omas/goverance-program/overview) supports the setting up of governance domains.
    * The [Community Profile OMAS](/services/omas/community-profile/overview) supports the setting up of communities and person roles.
    * The [Project Management OMAS](/services/omas/project-management/overview) supports the setting up of campaigns, projects and tasks.
    * The [egeria-samples.git repository](https://github.com/odpi/egeria-samples) includes a sample called [Sample metadata archives for Coco Pharmaceuticals](https://github.com/odpi/egeria-samples/tree/master/sample-metadata-archives/coco-metadata-archives) that creates open metadata archives with basic definitions for Coco Pharmaceuticals.  This includes the definition of this organization's governance domains with their communities and governance officers.

### Governance Leadership 

### Governance Leadership Communities




#### Governance Domain Communities



![Governance Communities](governance-domain-community.svg)

#### Governance Leaders Community

![Governance Leadership Community](governance-leadership-community.svg)



## Governance Process

Most activity within each governance domain is iteratively developer and reviewed.

The governance program OMAS provides APIs and events for tools and applications focused on defining a transformation strategy, planning support for a regulation and/or developing a governance program for your organization.

It assumes an organization wishes (or is already) operating an active governance program that is iteratively reviewed and developed.

It covers:

- [Dividing your governance program into domains](#governance-domains), such as data, security, privacy.  Each domain provides a specific focus.

- [Setting up the leadership of the domain](#governance-domain-leadership) to drive its definition and operations.  This includes:

- [Managing ]
    - Understanding the business drivers and regulations that provide the motivation and direction to the governance program.

    - Laying down the governance policies (principles, obligations and approaches) that frame the governance program.

    - Planning and defining the governance controls that detail how these governance policies will be implemented in the organization, and enumerating the implications of these decisions and the expected outcomes.

    - Defining the organization's roles and responsibilities that will support the governance program.

    - Defining the classifications and governance zones that will organize the assets being governed.

    - Defining the subject areas that will organize the data-oriented definitions such as glossary terms, valid values and quality rules.

    - Defining the

- Reviewing the impact of the governance program.

    - adjusting governance definitions and metrics as necessary.

- Reviewing the strategy, business and regulatory landscape.

    - adjusting the governance definitions and metrics as necessary.



### Governance Projects

![Governance Projects](governance-projects.svg)
![Governance Campaigns](governance-campaign.svg)



## Subject areas

Subject areas are topics or domains of knowledge that are of interest to the governance domains.  Some subject areas are common to multiple governance domains; others are specialized within a domain.  Each

![Figure 3](subject-area-definition.svg)
> **Figure 3:** Defining a subject area

Governance Program OMAS provides an [interface to create subject area definitions](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/SubjectAreasInterface.html).  The work is then handed off to the subject area owners:

* [Subject Area OMAS](/services/omas/subject-area/overview) supports the definition of glossary terms for subject areas.  
* [Digital Architecture OMAS](/services/omas/digital-architecture/overview) supports the definition of reference data and quality rules for the subject area.
* [Asset Manager OMAS](/services/omas/asset-manager/overview) supports the exchange of subject area information with other catalogs and quality tools.

!!! education "Further information"
    
    * The [Governance Program OMAS](/services/omas/goverance-program/overview) supports the setting up of subject area definitions.
    * [Common Data Definitions](/practices/common-data-definitions/overview) describes the management and use of subject areas.
    
    * The [Defining Subject Areas](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview/) scenario for Coco Pharmaceuticals walks through the process of setting up the subject areas for Coco Pharmaceuticals.
    
    * There are two code samples associated with this set of subject areas:
    
        * [Setting up the subject area definitions :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-samples/access-services-samples/governance-program-client-samples/governance-subject-area-sample){ target=gh }
        * [Setting up glossary categories for each subject area :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-samples/access-services-samples/subject-area-client-samples/subject-area-definition-sample){ target=gh } ready for subject area owners to start defining glossary terms associated with their subject area.


## Governance Definitions

A *Governance Definition* is a metadata element that describes the context or purpose for an activity that supports the organization's operation. Figure 1 shows the main types of governance definition and how they link together to create a coherent response to a business strategy or regulation.

![Figure 1](traceability-from-business-drivers-to-action.svg)
> **Figure 1:** Using governance definitions to provide traceability from business drivers and regulations to actions.


## Governance classification, tagging and linking

One of the ways to reduce the cost of governance is to define groups of similar assets/resources along with the governance definitions that apply to members of the group.  This avoids having to make decisions on how to manage each asset/resource.  The cataloguing process just needs to work out which group(s) to place the asset in.  Labels such as classifications, and tags of different types are used to identify these group assignments.  When a governance process is operating on the asset/resource, it looks up the labels and follows the governance definitions for the group.

![Figure 4](divide-and-conquer-landscape.svg)
> **Figure 4:** Different types of tags used to group assets for governance

The different types of labels used to group assets/resources are used for different purposes and may indicate how official they are:

* [Governance Zones](/concepts/governance-zone) group assets according to their use.  They are typically is used for [controlling visibility to the resource's asset definition](/features/governance-zoning/overview).

* [Governance Classifications](#setting-up-the-levels-for-your-governance-classifications) define the groups used for specific types of governance.

    * Confidence Governance Classification defines the level of confidence that should be placed in the accuracy of related data items.  This limits the scope that the data can be used in.
    * Confidentiality Governance Classification defines the level of confidentiality or secrecy needed with particular data.
    * Criticality Governance Classification defines how critical the related resources are to the continued operation of the organization.
    * Impact Governance Classification defines how much of an impact a particular situation is to the operation of the organization.
    * Retention Governance Classification defines how long a resource (typically data) must be retained by the organization.

* License Types define the contract aka (terms and conditions) that define how the asset/resource can be used.

* Certification Types define specific characteristics of an asset/resource that has been verified for a particular span of time.

* [SecurityTags](/concepts/security-tags) identify labels and properties that are used in determining which data protection rules should be executed when particular data is requests. They can be attached to assets or schema elements depending on the scope of data that the security tags apply to. The synchronized access control feature describes how security tags are set up and used.

The labels may be assigned directly to the asset, or to elements, such as schemas and glossary terms that are linked to the asset.

## Setting up the levels for your governance classifications

The values used in governance classifications show the specific group that the classified asset belongs to.  Often an organization has their own levels defined and they can be set up in [`GovernanceClassificationLevel`](/types/4/0421-Governance-Classification-Levels/) definitions.

![Figure 5](governance-program-level-definition.svg)
> **Figure 5:** Governance classifications that use governance level definitions

Egeria has a set of default values that can be set up using the [`createStandardGovernanceClassificationLevels`](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceClassificationLevelInterface.html) method.

## Measures and metrics

As important aspect of the governance program is the ability to measure its effectiveness and identify the assets that are delivering the highest value, or operating with the greatest efficiency etc.

A value that should be captured to demonstrate the effectiveness of the governance program is documented using the `GovernanceMetric` entity. It is linked to the appropriate governance definition and can be linked to a data set where the specific measurements are being gathered.

The calculation of governance metrics is often a summary of many other measurements associated with specific resources (such as data sources and processes) operating under the scope of the governance program. These resources are catalogued as [`Assets`](/concepts/asset). 

![Figure 6](governance-metrics-with-measurements-dataset.svg)
> **Figure 6:** Measuring governance through an external data set

The definition of their expected behavior or content can be captured using the `GovernanceExpectations` classification attached to the `Asset`. The measurements that support the assessment of a particular resource can be gathered and stored in a `GovernanceMeasurements` classification attached to its `Asset`.

![Figure 7](expectations-vs-measurements.svg)
> **Figure 7:** Setting expectations and gathering results in classifications

The measurement classification may be attached to a related element that describes an aspect for its operation.  For example, in figure 8 the measurement is attached to a process instance that captures a specific run of a process.  The expected values are attached to its parent process.

![Figure 8](expectations-vs-measurements-example.svg)
> **Figure 8:** Attaching the measurements to related elements


## Execution points

A governance execution point defines specific activity that is supporting governance.

There are three types:

* A Control Point is a place in the processing where a decision needs to be made. It may be a choice on whether to tolerate a reported situation or to resolve it - or it may be a decision on how to solve it.

* A Verification Point describes processing that is testing if a desired condition is true. Quality rules are examples of verification points. The result of a verification point is the output of the test. It may, for example, be a boolean, classification or a set of invalid values.

* An Enforcement Point describes processing that enforces an specific condition. For example, data may need to be encrypted at a certain point in the processing. The encryption processing is an enforcement point.

The ExecutionPointDefinition elements are created during the design of the governance program. They characterize the types of execution points that are needed to support the governance requirements. They are linked to the Governance Definition that they support using the ExecutionPointUse relationship. Typically the governance definitions linked to the governance execution point definitions are:

* Governance Processes
* Governance Procedures

Often execution points need to be integrated with the normal activity of the business, but they may also represent additional standalone activity.

The classifications ControlPoint, VerificationPoint and EnforcementPoint are used to label governance implementation elements with the type of execution point and the qualified name of the corresponding definition if any. They are often found on element such as:

* Governance Action Types
* Governance Actions

These classifications help in the review of the implementation of the governance program and can be used to drive additional audit logging. 


![Figure 9](governance-action-process-example.svg)
> Implementing the actions defined in your governance definitions.


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
