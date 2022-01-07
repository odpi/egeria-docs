<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Software Capabilities

Many software servers are connected to the open metadata ecosystem, each with wildly differing
capabilities.

A software capability documents a specific function that an IT infrastructure asset, such as a host, software server platform and software server, is able to perform.
The open metadata type for a software capability is [`SoftwareCapability`](/egeria-docs/types/0/0042-Software-Capabilities).

## Metadata managing software capabilities

Some software capabilities create and manage metadata - in fact they are the true master of this
metadata. for example, a database manager (aka database management system or DBMS) is the true
master of metadata about database schemas.

When metadata managed by such software capabilities is shared with an
[open metadata repository cohort](/egeria-docs/concepts/cohort-member),
the members of the cohort need to take note that they should not update this metadata.

The software capabilities that are recognized as managing metadata are:

* [Asset manager](#asset-manager)
* [Master data manager](#master-data-manager)
* [Engine](#engine)
* [Tool](#tool)

The identifiers of these software capabilities are used to 
[document the provenance](/egeria-docs/features/metadata-provenance/overview)
of any metadata that comes from these technologies.
Metadata instances that are mastered by specific software capabilities are referred to
as **external instances**.

## Asset Manager

An **asset manager**
is typically a service that provides a catalog of [assets](/egeria-docs/concepts/asset).  It is responsible
for maintaining details of the assets including their characteristics,
ownership, assessments and governance requirements.

Often an asset manager is specialized for particular types of assets.
For example, you may see a **data catalog** cataloging information about data sets and data stores
for a data lake.
A Configuration Management Database (CMDB) is an asset manager of infrastructure assets.

### Open metadata support for asset managers

An asset manager may integrate with the open metadata ecosystem using one of three methods:

 * as a
[cohort member](/egeria-docs/concepts/cohort-member)
through the
[Open Metadata Repository Services (OMRS) connectors](/egeria-docs/concepts/repository-connector)
or 

* using the [Catalog Integrator Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis/catalog-integrator/overview)
through an [integration connector](/egeria-docs/concepts/integration-connector) or

* Through direct calls to the [Asset Manager Open Metadata Access Service (OMAS)](/egeria-docs/services/omas/asset-manager/overview).

The [Metadata Server Exchange](/egeria-docs/patterns/metadata-server-exchange/overview)
pattern provides more information on these options.

## Master data manager

A master data manager is a capability in a software server to manage an authoritative
collection of master data, typically about people, organizations, products and accounts.

Master data managers that hold information about the people and organizations using open metadata
integrate their data through the [Community Profile OMAS](/egeria-docs/services/omas/community-profile/overview).

## Engine

An engine is a software capability that is programmable to automate specific
processes.  Typically these processes manipulate and store data.

Below are examples of engines:

* Workflow engine - for automating processes that coordinate the activity of people and systems.
* Data movement engine - for automating the movement of data from one store to another.
* Data virtualization engine - for automating the federation and transformation
of data in response to a real-time query.
* Reporting engine - for extracting data and formatting into specific reports.
* Analytics engine - for executing analytical processes.

The metadata used by an engine relates to the processing it is performing and the
data sources it is working with.

Most engines have associated tools to create the process definitions and manage the metadata,
leaving the engines themselves to run the automated processes and create lineage metadata.

# Tool

A tool is a user program used to create definitions that automate processes.
Typically the output of a tool runs on an [engine](#engine).

Tools are the master of metadata about the processes being automated and the
data they are manipulating.

Examples of tools include:

* Analytics tool - for creating analytics - for example, a python notebook.
* Process automation tools - for creating workflows for workflow engines.


--8<-- "snippets/abbr.md"
