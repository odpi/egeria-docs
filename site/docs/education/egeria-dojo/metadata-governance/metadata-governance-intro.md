<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


## The importance of metadata governance

Data, and the metadata that describes it, enables individuals and automated processes to make decisions.  As the trust grows in the availability, accuracy, timeliness and completeness of the data/metadata, its use increases and your organization sees greater value.

## Building trust

Trust is hard to build and easy to destroy.  Maintaining trust begins with authoritative sources of data/metadata that are actively managed and distributed along well known information supply networks.  This flow needs to be transparent and reliable - that is explicitly defined and verifiable through monitoring, testing and remediation.

The content of the data/metadata needs follow standards that ensure clarity both in meaning and how it should be used and managed.  Its completeness and quality needs to be appropriate for the organization's uses.  These uses will change over time.

Finally, the ecosystem that supplies and uses this data/metadata must evolve and adapt to the changing and growing needs of the organization because trust is required not just for today's operation but also into the future.

You can make your own choices on how to build trust in your data/metadata.  Egeria provides both *features* and *practices* built from industry experiences and best practices that help in the maintenance of data/metadata.  In this dojo we will cover these features and practices, enabling you to select which are appropriate to your organization and when/where to consider using them.

## Types of metadata

Metadata is often described as *data about data*.  However, this definition does not fully convey the breadth and depth of information that is needed to govern your digital operations.

### Technical metadata

The most commonly collected metadata is technical metadata that describes the way something is implemented.  For example, technical metadata includes databases and their database schema (table and column definitions), APIs and their interface specification, events and message schemas, applications, virtual containers, and computers.

Technical metadata is the easiest type of metadata to maintain since many technologies provide APIs/events to query the technical metadata for the digital resources it is managing.

You need to either gather this metadata whenever new resources are deployed into production, monitor for events that indicate that the metadata has changed or periodically call the metadata APIs to update the metadata catalog.

Collecting and maintaining technical metadata builds an inventory of your digital resources that can be used to count each type of digital resources and act as a list to work through when regular maintenance is required.  It also helps people locate specific types of digital resources.

### Consumer metadata



## Types of metadata repository

Many metadata repositories are *data catalogs*.  They focus on gathering and organizing information about data sources.  Each data source 


--8<-- "snippets/abbr.md"
