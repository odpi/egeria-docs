<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# January 2023

This is January's monthly report from the Egeria community.  This is a quiet month due to the winter break, but there is still some news to be shared.

## Face-to-face Workshop - 17th-19th January 2023

This month we had a three-day face to face workshop in Amsterdam.  Thank you to ING for hosting us.  These are the main topics discussed.

### Cloud native discussion

Egeria can be consumed in multiple ways:

* as a set of standard interfaces and formats where you can supply your own implementation
* as a set of libraries that can be incorporated into an existing program
* through the [OMAG Server Platform](/concepts/omag-server-platform)

The OMAG Server Platform offers a self-service approach to setting up and operating Egeria's open metadata and governance services.  It is designed for organizations that want to offer the governance teams the ability to control their governance and metadata operations.

Some organization want the control of which servers and services are running to be held by the IT Devops team.  It is possible to use the OMAG Server Platform in this environment.  However, Egeria is written in a modular fashion and so it is also possible to offer a deployment model that is more *cloud-native*:

* Each service is deployed as a microservice.
* Each service runs stateless.
* Each service's behaviour is fixed at deployment time.

We agreed to start a new workgroup to explore the possibility of offering this type of deployment model as an alternative to using the OMAG Server Platform.  The REST APIs and eventing are consistent between the two deployment models, and it will be possible to shift workload between the two models, and have them interoperate within the cohort.

![Deployment options](/guides/planning/runtime/deployment-options.svg)

The workgroup is up and running.  If you wish to follow along, or join in, please follow the [cloud native discussions](https://github.com/odpi/egeria/discussions/categories/cloud-native).

### Data product/data-mesh discussion

There are multiple data product/data-mesh projects in progress within the various organizations contributing to Egeria.  Many are still gathering requirements.   Once we have our individual organization requirements in place, we agreed that we would have a workgroup to go through the Egeria support for data products and data-mesh.

### Integration simplification

There was concern expressed that it is hard to show business value with Egeria without pre-built integrations to the necessary vendor products.  We reviewed the existing pre-built integrations and discovered that there are a good number of integrations that people were not aware of.  We then discussed how easy it was to find out which technologies have pre-built connectors included with Egeria.  This information is in the [Connector catalog](/connectors) however it may not be sufficient.  We agreed to have a review of the connector catalog to determine how it can be improved.

![Integrated technologies, January 2023](integrated-technologies-jan2023.png)

### Certificates and passwords

We had a discussion on the management of secrets in Egeria's deployment.  It is possible to encode certificates and other secrets in the connection objects found in the configuration and the metadata.  It is also possible to dynamically inject secrets into the connection object of an asset through the server security connector. It was felt that it should also be possible to retrieve the secrets from an external secrets store.  This would allow greater security around these values and also allow a connector to dynamically retrieve new secret values whenever they expire.

We agreed to create a new type of connector for a secrets store (SecuritySecretsConnector).  This would offer a name-value map interface.  We would implement two versions of this connector (one using environment variables and the other using a file).  A connection for the new connector could be embedded in the connection object of the connector that needs the secret.

### Database support

The JDBC connectors have additionally been tested with both IBM's DB2 database and the Oracle database.  With the previous testing of PostgreSQL, MariaDB and Trino we how have five verified databases.   We agreed that this function is mature enough to create a 1.0 release on Maven central.

There is still some discussion on how databases should be uniquely named, particularly in cloud-based scenarios, or where a database is deployed in different environments - such as dev, test and prod.

We agreed to support a qualified name template that would be set up the in Connection's configuration properties.  This template would be a string with specific placeholders for the connection URL, database name retrieved from the database manager, etc.  The Database Integration OMIS would support a new method on its context to generate the qualified name using the template.  This could be used by the connector implementation.

### User interfaces

Cezar Sirbu demonstrated how to incorporate Egeria's common web components into a new React UI.  This proved that the components are reusable outside the Egeria UIs, which may be useful to vendors or organizations wishing to consume Egeria from an existing UI.

The new general user interface using this technology is pencilled in to be included in the helm charts for the V4.0 release of Egeria.

Focus now moves to the services that support the web components.  Today we have the view services that run in the OMAG Server Platform and the services that run in the Egeria UI Platform.  The view services also run in the Egeria UI platform, so this platform has the potential to offer the common back-end services for all UIs (effectively replacing the [Presentation Server](/concepts/presentation-server).  The next step is to validate that it is possible to support pluggable user directories.  There needs to one user directory per tenant to support authentication of incoming users.

We are also looking for volunteers to help convert the remaining components from the React UI to the new style of web components using TypeScript.

### Release policy

We agreed that we would reduce the number of releases from 10 to 6 per year.  This is due to the rising effort to create a new release given the large number of repositories involved.

In order to mitigate the fact that the release includes a lot of testing, and it is the point at which we move to the latest dependencies to resolve detected security vulnerabilities, we agreed:

* To invest in the CTS - both in its test coverage and in an automated scheduled execution of the tests. (See [CTS Enhancements](#conformance-test-suite-cts-enhancements)).
* To enable the existing FVT suite to run against the XTDB repository connector.
* To add more tests to the FVT suite
* To continue to update our dependencies as recommended by *dependabot* every month.

## Connectors

There is a new connector to support the cataloguing of schemas documented in the [Confluent schema registry](https://www.confluent.io/product/confluent-platform/data-compatibility/).  It can be found in the [egeria-connector-integration-event-schema.git](https://github.com/odpi/egeria-connector-integration-event-schema) git repository.

## Conformance Test Suite (CTS) enhancements

The CTS provides an intense test of an OMRS repository connector implementation.  We use it as part of the release verification.  It has fallen behind the current implementation of the interface, since no new tests have been added for a couple of years.  Starting with 3.15, new tests, improved diagnostics and performance enhancements are being added to improve the coverage of the CTS.  Thanks to Nigel Jones, we also have the ability to run the CTS every day through a GitHub action.  This will allow regressions in the inmemory, graph and XTDB repositories to be picked up quickly. 

## Core Egeria

!!! info "Core Egeria Releases"
    * [Release 3.15](/release-notes/3-15) branched on 31st January 2023.  This will be the last release on Java 11 with support for a Maven build.
    * [Release 4.0](/release-notes/4-0) is expected to release in March 2023.  It will use Java 17 and be built with Gradle.

## Events

### Webinar series

On 9th January 2023 we recorded another webinar, this one entitled, *"What next after you have built a catalog. Part 2: making it real"*.  [Link to video](https://www.youtube.com/watch?v=1BPHUgzsUos)

### Community meetings

Over the last few community meetings ...

* We reviewed the design of the [governance action process](/patterns/metadata-governance/overview) choreography.
* On the last community call of 2022, we had the traditional *Review of the Year* celebration that highlighted the achievements of 2022.
* The 2023 community calls began with a review of the Asset Consumer OMAS, Connected Asset Services and Open Metadata Store.
* The following week, Dan Wolfson took us through the design and implementation of a new Python client for Asset Consumer OMAS.
* Last week was a review of the items various members of the community plan to contribute this year.

### Annual Project Review

The Egeria project annual review by the [Technical Advisory Board (TAC)](https://wiki.lfaidata.foundation/pages/viewpage.action?pageId=7733341) of the LF AI and Data foundation is scheduled for 9th March 2023.

## New documentation pages

Each month we will select one or more new pages that where added/updated in the last month to [https://egeria-project.org](https://egeria-project.org) so you can keep up-to-date with how it is evolving.

* [Categories of Metadata](/patterns/metadata-manager/categories-of-metadata)
* [Description of a Digital Service](/types/7/0710-Digital-Service)

## Moving to Gradle

Our build technology for the Java based projects has used both Maven and Gradle.  We plan to move entirely to gradle in the next few months, so you will see:

* Repositories such as egeria-dev-projects.git and egeria-samples.git move from maven to gradle.
* The Egeria Development Dojo will use gradle in the exercises.

The [Core Egeria](https://github.com/odpi/egeria) repository has offered both a maven and a gradle option.  The maven option will be removed once we are sure the gradle build is able to support the release process.

## Connecting with the project

!!! info "Connecting with the project"
    Go to our [community guide](/guides/community) to find out how to find out more about the activities of the Egeria project. 

--8<-- "snippets/abbr.md"
