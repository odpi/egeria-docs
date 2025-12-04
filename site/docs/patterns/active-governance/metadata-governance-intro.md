<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


## The importance of metadata governance

Data, and the metadata that describes it, enables individuals and automated processes to make decisions.  As the trust grows in the availability, accuracy, timeliness, usefulness and completeness of the data/metadata, its use increases and your organization sees greater value.

## Building trust

Trust is hard to build and easy to destroy.  Maintaining trust begins with authoritative sources of data/metadata that are actively managed and distributed along well known information supply chains.  This flow needs to be transparent and reliable - that is, explicitly defined and verifiable through monitoring, inspection, testing and remediation.  It needs to be tailored to meet the specific needs of its consumers.

Consider this story ...

!!! example "A tale about trust"
    --8<-- "docs/patterns/metadata-governance/sams-story.md"

Is there any problem with the way that the bus company is operating?  How confident do you think Sam is that the bus company will provide a reliable service to get him to work every day?  What is the impact if Sam buys a car or uses a bike because he decides the bus company is not to be trusted?

!!! info "Some thoughts on the case ..."
    Sam is likely to conclude that the bus company does not care about its customers - and is not focused on attracting new business by encouraging people to try new routes.  This suggests it is doomed in the long run. If he misses the bus again because the bus times change then he is motivated to look for alternative solutions.  

    **His perception of the quality of the bus service is as much affected by the quality of information about the buses as the actual frequency and reliability of the service itself.**

If we translate this story to the digital world, organizations often provide shared services and/or data sets that other parts of the business rely on.  It is not sufficient that these services/data sets are useful with high availability/quality.  If potential consumers can not find out about them, or existing consumers are disrupted by unexpected change, then the number of consumers will dwindle as they seek their own solutions, and the shared service looses relevance to the business.

The team providing the shared service should consider the documentation about it to be a key part of their deliverables.  Capturing this documentation as metadata and publishing it to the open metadata ecosystem increases its findability and comprehensibility.

!!! example "Meanwhile, back at the bus company ..."
    --8<-- "docs/patterns/metadata-governance/meanwhile-at-bus-company.md"

It is often the case that if something is not being done, either:

* no-one is responsible for it, or
* it is very low on the priorities of the person who is responsible for it, or
* the person responsible for it does not have the resources to do the work.

Therefore, step one in solving such a problem is to appoint someone who is responsible for it, and ensure they have the motivation and resources to do the work.  

In metadata governance, we refer to the person responsible for ensuring that metadata about a service or dataset is complete, accurate and up-to-date as the *owner*.  The owner may not personally maintain the metadata since this may be automated, or be handled by others.  However, if there are problems with the metadata, the owner is the person responsible for sorting it out.

!!! example "Fixing the bus timetables"
    --8<-- "docs/patterns/metadata-governance/fixing-the-bus-timetables.md"

In the example above, the managing director identified where the action was occurring that should trigger the change.  She assigned an owner and ensured they had the resources (ie the new assistant) to ensure the updates were done.

When a change to the timetable occurred, the bus drivers' manager triggered the assistant to update the master bus timetable.  The updated timetable was then transformed into multiple formats and disseminated to all the places where their customers are likely to notice the change.  Their challenge is to both create awareness that the change has happened and provide the updated information.

## Metadata governance three-step process

We can generalise this process as follows, creating a reusable specification pattern for all forms of governance:

![Governance Specification Pattern](/patterns/metadata-governance/governance-specification-pattern.svg)
> A three-step specification pattern of *Trigger*, *Take Action* and *Make Visible*.

For metadata governance, the *Take Action* is typically an update to metadata.   For example, if a new deployment of a database occurs in the digital world, it could trigger a metadata update to capture any schema changes and then information about these changes is disseminated to the tools and consumers that need the information.

The dissemination of specific changes to metadata can also act as a trigger for other metadata updates.  For example, the publishing of changes to a database schema could trigger a data profiling process against the database contents.  The data profiling process adds new metadata elements to the existing metadata, and hence the knowledge graph of metadata grows.

![Linked metadata updates](/patterns/metadata-governance/linked-metadata-updates.svg)

The specification pattern above applies whether the governance is manual or automated.  All that changes is the mechanism.  

Triggers may be time-based, or an unsolicited update to metadata by an individual.  For example, data profiling may be triggered once a week as well as whenever the schema changes.  A comment attached to a database description that reports errors in the data may trigger a data correction initiative.

Consider metadata as a collection of linked facts making up a knowledge graph that describes the resources and their use by the organization.  The role of the tools, people and open metadata technology is to build, maintain and consume this knowledge graph to improve the operation of the organization.

!!! example "Enriching customer service"
    --8<-- "docs/patterns/metadata-governance/enriching-customer-service.md"

When metadata governance is done well, a rich conversation develops between service providers and their consumers that can lead to both improvements in the quality of the services and the expansion in the variety and amount of consumption; the real value of the service is measured by consumption.

New uses for the services will then emerge ... growing the vitality and value to the organization.



