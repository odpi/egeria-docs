<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


## The importance of metadata governance

Data, and the metadata that describes it, enables individuals and automated processes to make decisions.  As the trust grows in the availability, accuracy, timeliness and completeness of the data/metadata, its use increases and your organization sees greater value.

## Building trust

Trust is hard to build and easy to destroy.  Maintaining trust begins with authoritative sources of data/metadata that are actively managed and distributed along well known information supply chains.  This flow needs to be transparent and reliable - that is explicitly defined and verifiable through monitoring, testing and remediation.

Consider this story ...

!!! example "A tale about trust"
    --8<-- "docs/education/egeria-dojo/metadata-governance/sams-story.md"

Is there any problem with the way that the bus company is operating?  How confident do you think Sam is that the bus company will provide a reliable service to get him to work every day?  What is the impact if Sam buys a car because he decides the bus company is not to be trusted?

!!! info "Some thoughts on the case ..."
    Sam is likely to conclude that the bus company does not care about its customers - and is not focused on attracting new business by encouraging people to try new routes.  This suggests it is doomed in the long run. If he misses the bus again because the bus times change then he is motivated to look for alternative solutions.  

    His perception of the quality of the bus service is as much affected by the quality of information about the buses as the actual frequency and reliability of the service itself.

If we translate this story to the digital world, organizations often provide shared services and/or data sets that other parts of the business rely on.  It is not sufficient that these services/data sets are useful with high availability/quality.  If potential consumers can not find out about them, or existing consumers are disrupted by unexpected change, then the number of consumers will dwindle as they seek their own solutions, and the shared service looses relevance to the business.

The team providing the shared service should consider the documentation about it to be a key part of their deliverables.  Capturing this documentation as metadata and publishing it to the open metadata ecosystem increases its findability and comprehensibility.

!!! example "Meanwhile, back at the bus company ..."
    --8<-- "docs/education/egeria-dojo/metadata-governance/meanwhile-at-bus-company.md"


It is often the case that if something is not being done, either:

* no-one is responsible for it, or
* it is very low on the priorities of the person who is responsible for it, or
* the person responsible for it does not have the resources to do the work

Therefore, step one in solving such a problem is to appoint someone who is responsible for it, and ensure they have the motivation and resources to do the work.  

In metadata governance, we refer to the person responsible for ensuring that metadata about a service or dataset is complete, accurate and up-to-date as the *owner*.  The owner may not personally maintain the metadata since this may be automated, or be handled by others.  However, if there are problems with the metadata, the owner is the person responsible for sorting it out.

!!! example "Fixing the bus timetables"
    --8<-- "docs/education/egeria-dojo/metadata-governance/fixing-the-bus-timetables.md"

In the example above, the managing director identified where the action was occurring that should trigger the change.  She assigned an owner and ensured they had the resources (ie the new assistant) to ensure the updates were done.

When a change to the timetable occurred, the bus drivers' manager triggered the assistant to update the master bus timetable.  The updated timetable was then transformed into multiple formats and disseminated to all the places where their customers are likely to notice the change.  Their challenge is to both create awareness that the change has happened and provide the updated information.

We can generalise this process as follows, and this is a reusable specification pattern for metadata governance:

![Metadata Update Specification Pattern](metadata-update-specification-pattern.svg)
> A three-step specification pattern of *Trigger*, *Maintain Metadata* and *Make Visible*.

For example, if a new deployment of a database occurs, it would trigger a metadata update to capture any schema changes and then information about these changes is disseminated to the tools and consumers that need the information.

The dissemination of specific changes to metadata can also act as a trigger for other metadata updates.  For example, the publishing of changes to a database schema could trigger a data profile process of the database contents.

![Linked metadata updates](linked-metadata-updates.svg)

The specification pattern above applies whether the governance is manual or automated.  All that changes is the mechanism.  

Triggers may be time-based, or an unsolicited update to metadata by an individual.  For example, data profiling may be triggered once a week as well as whenever the schema changes.  A comment attached to a database description that reports errors in the data may trigger a data correction initiative.

!!! example "Enriching customer service"
    --8<-- "docs/education/egeria-dojo/metadata-governance/enriching-customer-service.md"
    
When metadata governance is done well, a rich conversation develops between service providers and their consumers.  This improves understanding of how the service is used, with a resulting improvement in the quality of the service.

## The open metadata ecosystem

The content of the data/metadata shared between teams needs to follow standards that ensure clarity both in meaning and how it should be used and managed.  Its completeness and quality need to be appropriate for the organization's uses.  These uses will change over time.

Finally, the ecosystem that supplies and uses this data/metadata must evolve and adapt to the changing and growing needs of the organization because trust is required not just for today's operation but also into the future.

You can make your own choices on how to build trust in your data/metadata.  Egeria provides both *mechanisms* and *practices* built from industry experiences and best practices that help in the maintenance of data/metadata.  

In this dojo we will cover these mechanisms and practices, showing how they fit in the metadata update specification pattern described above.  You can then select which are appropriate to your organization and when/where to consider using them.

## Categories of metadata

Metadata is often described as *data about data*.  However, this definition does not fully convey the breadth and depth of information that is needed to govern your digital operations.

The categories of metadata listed below help you organize your metadata needs around specific triggers that drive your metadata ecosystem.

### Technical metadata

The most commonly collected metadata is *technical metadata* that describes the way something is implemented.  For example, technical metadata for common [digital resources](/concepts/resource) includes:

* The databases and their database schema (table and column definitions) configured in a database server.
* APIs and their interface specification implemented by applications and other software services to request actions and query data.
* The events and their schemas used to send notifications between applications, services and servers to help synchronized their activity.
* The files stored on the file system.

Technical metadata is the easiest type of metadata to maintain since many technologies provide APIs/events to query the technical metadata for the digital resources it is managing.

To keep your technical metadata up-to-date you need to consider the following types of metadata update triggers:

* whenever new digital resources are deployed into production, 
* events that indicate that the digital resources have changed
* regular scanning of the deployment to validate that all technical metadata has been captured.

Collecting and maintaining technical metadata builds an inventory of your digital resources that can be used to count each type of digital resources and act as a list to work through when regular maintenance is required.  It also helps people locate specific types of digital resources.

### Data content analysis results

The technical metadata typical describes the structure and configuration for digital resources.  Analysis tools can add to this information by analysing the data content of the digital resources.  The results create a characterization of the data content that helps potential consumers select the digital resources that they need.

Data content analysis is often triggered periodically, based on the update frequency that the digital resource experiences.  It can also be triggered when the technical metadata is first catalogued or updated.

### Consumer metadata

*Consumer metadata* includes the comments, reviews, tags added by the users that are consuming the metadata and the digital resources it describes.  This metadata is gathered from the tools through which the users consume the metadata and the digital resources.  It is then used to assess the value and popularity of the metadata and digital resources to their consumers.

Metadata update triggers should focus around the tools where the consumer metadata is captured.  Typically, each piece of consumer feedback is treated as a separate trigger.


### Common definitions

*Common definitions* describe standards for your data and its use.  They are organized into [subject areas](/concepts/subject-area), also known as topic areas or data domains, and their aim is to create a common understanding and processing across your digital landscape, improving the consistency of the data copies supporting your organization.

Updates to the related common definitions are typically edited offline and then disseminated together as a new release.  Therefore, the metadata update trigger is often related to the release of a collection of common definitions.

### Governance metadata

*Governance metadata* describe the requirements of a particular [Governance Domain](/concepts/governance-domain) and their associated controls, metrics and implementations.  They are managed in releases in a similar way to common definitions.  Therefore, their releases act a triggers. 


### Organizational metadata

*Organizational metadata* describe the teams, people, roles, projects and communities in the organization.  This metadata is used to coordinate the responsibilities and activities of the people in the organization.  For example, roles can be defined for the owners of specific resources, and they can be linked to the profiles of the individuals appointed as owner.  This information can be used to route requests and feedback to the right person.

Organization metadata is often managed in existing applications run by Human Resources and Corporate Security.  Therefore, updates in these applications are used to trigger updates to the organizational metadata in the open metadata ecosystem.

Governance action can trigger the creation of new roles and appointments to these roles.  These elements can be then be disseminated on to the appropriate applications for information, verification and/or approval.

### Process metadata

Data is copied, combined and transformed by applications, services, processes and activities running in the digital landscape.  Capturing the structure of this processing shows which components are accessing and changing the data.  This information is a key element in providing [lineage](/concepts/lineage), used for traceability, impact analysis and data observability.

The capture and maintenance of process metadata is typically triggered as process implementations are deployed into production.

### Operational metadata

*Operational metadata* describes the activity running in the digital landscape.  For example, process metadata could describe the steps in an ETL job that copies data from one database to another.  The operational metadata which capture how often it runs, how many rows it processed and the errors it found.

Operational metadata is often captured in log files.  As they are created, they trigger the cataloging and linking of their information into the other types of metadata.  

### Metadata relationships and classifications

The other types of trigger to consider is when/where the metadata elements described above can be connected together and augmented.

This linking and augmentation of metadata has a multiplying effect on the value of your metadata.  

You can think of the metadata described above as the facts about your organization's resources and operation.  *Metadata relationships* that show how one element relates to another begin to show the context in which decisions are made and these resources are used.

*Metadata classifications* are used to label metadata as having particular characteristics.  This helps group together  similar elements, or elements that represent resources that need similar processing

## Types of metadata repository

Many metadata repositories are *data catalogs*.  They focus on gathering and organizing information about data sources for a team of data professionals.  Each data source is catalogued under the guidance of its users.  There is some automation for maintaining the catalogued data sources.  The aim is to provide the metadata needed by the local team.

There are also metadata repositories that focus on providing metadata to the whole enterprise. These repositories have a focus on common definitions and automation of metadata maintenance and stewardship.  They are deployed and controlled as a centralized service.  Some of these repositories are specialized for different types of use cases and often includes support for governance - for example, it may have a focus on Data Governance, IT Infrastructure Governance or Security Governance.

There are many tools and platforms that capture metadata as part of their operation.  For example, a relational database has structural information about the data it stores (called the database schema) that is used to identify the data that should be returned by a query.

This metadata is then useful in tools that are building queries to the database - such as reporting, profiling and application development tools.

## Summary

Hopefully the discussion above has help to illustrate that metadata is varied and can be built into a rich knowledge base that drives organizational change through increased visibility of an organization's operation, communication and collaboration.


--8<-- "snippets/abbr.md"
