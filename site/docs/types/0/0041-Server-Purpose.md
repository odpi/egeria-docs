<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0041 Server Purposes

The server purpose classifications allow more detail about the type of middleware software that are embedded in an [*ITInfrastructure*](/types/0/0030-Hosts-and-Platforms) entity.  Typically, these classifications are used with [*SoftwareServerPlatform*](/types/0/0037-Software-Server-Platforms) and [*SoftwareServer*](/types/0/0040-Software-Servers) entities.

![UML](0041-Server-Purpose.svg)

## ServerPurpose classification

The *ServerPurpose* classification provides a common base type for the server purposes - so it is possible to, for example, query a list of database servers, even through they are implemented using various technologies and hence represented by entities with different open metadata types. The *deployedImplementationType* attribute allows a specific software package supporting the specific purpose.

The subtypes of the *ServerPurpose* classification are:

- [*ApplicationServer*](#applicationserver-classification) - hosting application logic.
- [*Webserver*](#webserver-classification) - hosting endpoint for HTTP requests.
- [*DatabaseServer*](#databaseserver-classification) - hosting a database management system (DBMS).
- [*IntegrationServer*](#integrationserver-classification) - hosting data movement processes.
- [*MetadataServer*](#metadataserver-classification) - manages and stores a collection of metadata.
- [*RepositoryProxy*](#repositoryproxy-classification) - Acts as an adapter for a metadata server, translating requests between different APIs, formats and protocols.
- [*StewardshipServer*](#stewardshipserver-classification) - hosting stewardship processes.
- [*GovernanceDaemon*](#governancedaemon-classification) -  hosting automated governance processing.

## ApplicationServer classification

An application server hosts what is often called "business logic".  It is the software that supports business operations such as serving customer, building goods and services, invoicing and collecting money, etc.  There are many ways to implement business logic and the popular approaches change over time.  For example, microservices are popular at the time of writing this, before that it was web services, before that it was Enterprise Java Beans.  For an organization with event a modest amount of longevity, it is common to find a mix of implementation styles supporting their business.  Each implementation style varies the type of frameworks and underlying middleware, leading to different system structures.  Hence the usefulness of being able to identify where the business logic is located.

## Webserver classification

A webserver supports HTTP requests.  This is used to support browser-based user interfaces (including websites and many applications) as well as REST API calls.  As a consequence, many platforms/servers include a webserver, so you will find them in unexpected places.  For example, Egeria's [OMAG Server Platform](/concepts/omag-server-platform) includes the [Tomcat Webserver](https://tomcat.apache.org/).  Webservers provide external access to application function and so are a potential access point for cyber attacks.  Using this classification on the appropriate IT Infrastructure entities enables a simple query to retrieve all of your HTTP access points.  If these entities are linked to an [Endpoint](/types/0/0026-Endpoints) via a *ServerEndpoint* relationship, the combination enables a report of the HTTP endpoints and the servers behind it.

## DatabaseServer classification

A database server supports data query services such as SQL.  These services used to be the preserve of specialist relational database software.  However, standards such as SQL have become ubiquitous and we see many types of services supporting data query services.  Classifying the IT infrastructure entities that provide data query services helps to identify where collections of data can be accessed directly.

## IntegrationServer classification

An integration server manages the flow of data between servers (typically application servers and database servers).  This copying of data can be done in batch or by monitoring changes to the source and sending the appropriate updates to its downstream destinations.  Examples of integration servers are:

* Extract, transformation, load (ETL) engines
* Replication engines
* Data virtualization engines/services
* Event brokers

Integration servers often include mapping and transformation logic needed to mold the data to the downstream systems needs.  So these types of servers are:

* The means by which data (and metadata) flows between the organization systems and so are very important in understanding [lineage](/features/lineage-management/overview).
* A potential place where errors in data can be introduced.

## MetadataServer classification

A metadata server is a store of metadata that describes external elements - typically people, processes and technology.  It is a means to understand and manage a digital landscape.  Egeria's [metadata access store](/concepts/metadata-access-store) is an example of a metadata server; [Apache Atlas](https://atlas.apache.org) is another.

As IT landscapes have got more complex, and the desire to extract data from this landscape for reporting, analytics and AI, there has been explosion in the number of metadata servers, often called data catalogs or configuration management databases, and the number of data tools that include a metadata server.  Understanding the location of metadata servers can help to kickstart a new initiative that needs to find existing resources.

## RepositoryProxy classification

This is a concept from Egeria.  A [repository proxy](/concepts/repository-proxy) is a metadata server that is acting as a proxy (adapter) to another metadata server.  Although it provides metadata services, calls to these services are delegated to another metadata server.

## StewardshipServer classification

A stewardship server is one where corrections are made to data outside of their origin system.

## GovernanceDaemon classification

A governance daemon is a server that is supporting governance processing.  It is typically a background server.  It often feeds work to a stewardship server.  Egeria's [governance servers](/concepts/governance-server).

--8<-- "snippets/abbr.md"
