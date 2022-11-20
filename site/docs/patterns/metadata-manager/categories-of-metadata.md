<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


## Categories of metadata

Metadata is often described as *data about data*.  However, this definition does not fully convey the breadth and depth of information that is needed to govern your digital operations.

The categories of metadata listed below help you organize your metadata needs around specific triggers that drive your metadata ecosystem.

### Technical metadata

The most commonly collected metadata is *technical metadata* that describes the way something is implemented.  For example, technical metadata for common [digital resources](/concepts/resource) includes:

* The databases and their database schema (table and column definitions) configured in a database server.
* APIs and their interface specification implemented by applications and other software services to request actions and query data.
* The events and their schemas used to send notifications between applications, services and servers to help synchronize their activity.
* The files stored on the file system.

Technical metadata is the easiest type of metadata to maintain since many technologies provide APIs/events to query the technical metadata for the digital resources it manages.

To keep your technical metadata up-to-date you need to consider the following types of metadata update triggers:

* whenever new digital resources are deployed into production, 
* events that indicate that the digital resources have changed
* regular scanning of the deployed IT environment to validate that all technical metadata has been captured (and nothing rogue has been added).

Ideally you want your metadata governance to engage in the lifecycles that drive changes in the technical metadata - for example, adding management of technical metadata as part of the software development lifecycle (SDLC) or CI/CD pipelines.

Collecting and maintaining technical metadata builds an inventory of your digital resources that can be used to count each type of digital resources and act as a list to work through when regular maintenance is required.  It also helps people locate specific types of digital resources.

### Data content analysis results

The technical metadata typically describes the structure and configuration for digital resources. Analysis tools can add to this information by analysing the data content of the digital resources. The results create a characterization of the data content that helps potential consumers select the digital resources best suited for their needs.

Data content analysis is often triggered periodically, based on the update frequency that the digital resource typically experiences.  It can also be triggered when the technical metadata is first catalogued or updated.  If the digital resource is really important, and used in Analytics/AI you need to check more often to validate that no significant changes have occurred.

### Consumer metadata

*Consumer metadata* includes the comments, reviews, tags added by the users that are consuming the metadata and the digital resources it describes.  This metadata is gathered from the tools through which the users consume the metadata and the digital resources.  It is then used to assess the value and popularity of the metadata and digital resources to the broader community.

Metadata update triggers should focus around the tools where the consumer feedback is captured.  Typically, each piece of consumer feedback is treated as a separate trigger.  The feedback should then be distributed to the tools that are used by the owning team.  This could trigger changes to the resource.  Ideally, the owning team should be able to respond and demonstrate they are listening and taking action.

### Common definitions

*Common definitions* describe standards for your data and its use.  It typically involves:

* [Glossary definitions](/practices/common-data-definitions/anatomy-of-a-glossary) describing the meaning of data values, 
* [Reference data](/types/5/0545-Reference-Data) describing valid values and mappings for data values,
* [Technical controls](/types/4/0430-Technical-Controls) defining quality rules and processing rules - such as anonymization/encryption requirements, 
* [Terms and conditions](/types/4/0483-Terms-And-Conditions) of use,
* [Governance action classifications](/types/4/0422-Governance-Action-Classifications) such as level of confidentiality, expected retention period, how critical this type of data is ...,
* [Data classes](/concepts/data-class) are logical types for data used to characterize data during analysis.
* [Standard/preferred schemas](/concepts/schema) and [associated implementation snippets](/types/5/0504-Implementation-Snippets) to guide developers to improve the consistency of data representation across the digital landscape.

Common definitions are organized into [subject areas](/concepts/subject-area), also known as topic areas, and their aim is to create a common understanding of the content and standard processing rules across your digital landscape, improving the consistency of the values in different stores of data supporting your organization.
[Assets](/concepts/asset) that are managed using the subject area's common definitions are said to be part of the subject area's domain.  This is called the *Subject Area Domain* and is synonymous with *Data Domain* - although a subject area domain may manage assets that are not data assets (such as systems and infrastructure) which is why open metadata uses a more generic name.

Updates to the related common definitions are typically edited offline, collected, and then disseminated together as a new release. Therefore, the metadata update trigger is often related to the release of a collection of common definitions.

### Governance metadata

*Governance metadata* describe the requirements of a particular [Governance Domain](/concepts/governance-domain) and their associated controls, metrics and implementations.  They are managed in releases in a similar way to common definitions.  Therefore, their releases act a triggers to further actions. 

### Organizational metadata

*Organizational metadata* describe the teams, people, roles, projects and communities in the organization.  This metadata is used to coordinate the responsibilities and activities of the people in the organization.  For example, roles can be defined for the owners of specific resources, and they can be linked to the profiles of the individuals appointed as owner.  This information can be used to route requests and feedback to the right person.

Organization metadata is often managed in existing applications run by Human Resources and Corporate Security.  Therefore, updates in these applications are used to trigger updates to the organizational metadata in the open metadata ecosystem.

Governance actions can trigger the creation of new roles and appointments to these roles.  These elements can be then be disseminated to the appropriate applications for information, verification and/or approval.

### Business context metadata

An organization has capabilities, facilities and services.  The digital resources it uses serve these purposes.  When decisions need to be made as to which digital resources to invest in, it is helpful to understand which part of the business will be impacted.

Information about the organization's capabilities, facilities and services is called *business context*.  Often individuals core role is focuses on these aspects.  Thinking them to the digital resources that they depend on (often invisible to these individuals) helps to raise awareness of the mutual dependency and understanding of the impact/value of change at either level.

Triggers that detect change in digital resources (for example an outage) can result in information flowing to the appropriate business teams.  If the change (or outage) is extensive, the linked business context can be used to prioritize the associated work.

### Process metadata

Data is copied, combined and transformed by applications, services, processes and activities running in the digital landscape.  Capturing the structure of this processing shows which components are accessing and changing the data.  This *Process Metadata* is a key element in providing [lineage](/concepts/lineage), used for traceability, impact analysis and data observability.

The capture and maintenance of process metadata is typically triggered as process implementations are deployed into production.

### Operational metadata

*Operational metadata* describes the activity running in the digital landscape.  For example, process metadata could describe the steps in an ETL job that copies data from one database to another.  The operational metadata captures how often it runs, how many rows it processed and the errors it found.

Operational metadata is often captured in log files. As they are created, they trigger the cataloging and linking of their information into other types of metadata.

## Metadata relationships and classifications

The other types of trigger to consider is when/where the metadata elements described above can be connected together and augmented.

This linking and augmentation of metadata has a multiplying effect on the value of your metadata.  

You can think of the metadata described above as the facts about your organization's resources and operation.  *Metadata relationships* that show how one element relates to another, begin to show the context in which decisions are made and these resources are used.

*Metadata classifications* are used to label metadata as having particular characteristics.  This helps group together similar elements, or elements that represent resources that need similar processing

!!! summary "Summary"

    Hopefully the discussion above has helped to illustrate that metadata is varied and can be built into a rich knowledge base that drives organizational objectives  through increased visibility, utilization and management of an organization's digital assets.

--8<-- "snippets/abbr.md"
