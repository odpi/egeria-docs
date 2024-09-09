<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# February 2023

This is February's monthly report from the Egeria community.  This month's focus has been in preparing for the 4.0 release.

## Core Egeria

If you are working in the *main* branch of Egeria, you will notice that the release version is set to `4.0-SNAPSHOT` indicating that the next release will be `4.0`.  We are updating the major version number for three reasons:

* the level of Java has moved from Java 11 to 17 in all builds
* the maven build is being removed.
* there are performance enhancements that are not strictly backward compatible for [repository connector](/concepts/repository-connector) implementation.

!!! info "Core Egeria Releases"
    * [Release 4.0](/release-notes/4-0) is expected to release by April 2023.  It will use Java 17 and be built with Gradle.

### Moving to Gradle

The [Core Egeria](https://github.com/odpi/egeria) repository is now building exclusively using gradle in all GitHub pipelines.  The maven option is still present in the repository, but will be removed will be removed once all known consumers of Egeria are ready.

* The egeria-dev-projects.git repository has also moved to gradle and Java 17.
* The egeria-samples.git will move from maven to gradle in the next week or so.
* The Egeria Development Dojo will use gradle in the exercises.  However, this is still work in progress, but is expected to be completed before the V4.0 release.

### Performance improvements in Core Egeria

In recent months, there have been a number of significant performance enhancements made to the core libraries in the [OMAG Server Platform](/concepts/omag-server-platform).  These have resulted in halving the time to execute for some requests.  Part of this work has focused on the marshalling and unmarshalling of elements both in REST APIs and Events.

One change has reduced the number of fields in the type description in an open metadata instance (entity, relationship and classification).  This will impact repository connector implementations that build their own instance type elements.

This diagram illustrates the changes:

![OpenMetadata Instance Structure](/concepts/open-metadata-instances-structure.svg)

## Connectors

### JDBC connector

The [JDBC Connectors](https://github.com/odpi/egeria-connector-jdbc) are now officially released onto Maven Central.  The next step is to add them to the [open connectors archive](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-connector-archives) so that they are picked up by the OMAG services.

### HMS connector

The [Egeria HMS connector](https://github.com/odpi/egeria-connector-hivemetastore) has been enhanced in 3 ways this month:

* The gradle build has been improved to bring in the latest dependencies. There is now a new optional property that can be set on the gradle build to create
a HMS connector that will work with the [IBM Cloud&#174 Data Engine service](https://cloud.ibm.com/catalog/services/data-engine-previously-sql-query); to do this the
  property *ibmhive* in the gradle build; on the command line specify: `./gradlew build -Pibmhive`
* Junits have been added so the coverage is now over 70%.
* The HMS connector now correctly extracts columns from HMS external tables that have been created from [Apache Spark&trade;](https://spark.apache.org/) dataframes.  

## Cloud-native workgroup

The work of the cloud native workgroup continues to make progress.  The team are focused on building a simple proof of concepts around an [integration daemon](/concepts/integration-connector) running a single [integration connector](/concepts/integration-connector).  If you wish to follow along, or join in, please follow the [cloud native discussions](https://github.com/odpi/egeria/discussions/categories/cloud-native).

## New framework - The Open Integration Framework (OIF)

In development for version 4.0 is a new framework called the [Open Integration Framework (OIF)](/frameworks/oif/overview).  It provides the interfaces for an [integration connector](/concepts/integration-connector).  These interfaces were originally implemented partly in the [integration daemon services](/services/integration-daemon-services) and the [administration services](/services/admin-services/overview).  The introduction of the OIF creates a cleaner interface for integration connectors.  However, it does have an impact on existing integration connectors:

* The build script for the connector needs to include the OIF as a dependency (replacing the integration-daemon-services-api module). For example, for Gradle use:
```
       compileOnly ':open-metadata-implementation:frameworks:open-integration-framework'
```

* The package names for the integration connector interfaces change from `org.odpi.openmetadata.governanceservers.integrationdaemonservices.connectors` to `org.odpi.openmetadata.frameworks.integration.connectors`.

## Events

### Webinar series

On 13th March 2023 we will record another webinar called *"Building a sustainability initiative"*.

Tom Tally is a recent graduate with ambitions to become a director at Coco Pharmaceuticals.  Even though she has only been in the company three years, she is already the manager of the accounts department.  In order to give her a stretch assignment, she is asked to lead the new sustainability initiative at Coco Pharmaceuticals.  She is given two experienced leaders, Erin Overview and Stew Faster, to help her.  The challenge is to create an ongoing attention to sustainability across Coco Pharmaceuticals' complex business.

This webinar takes you through Tom's journey to set up and operate Coco Pharmaceuticals sustainability initiative and the role that Egeria plays.

* Presenters: Mandy Chessell and Dan Wolfson
* Time: 15:00 UTC
* [Zoom Conference Link](https://zoom-lfx.platform.linuxfoundation.org/meeting/92563720721?password=6812f50c-c1a6-4d07-ad6d-7aa63e793285)

### Community meetings

Over the last few community meetings ...

* We reviewed release 3.15
* We reviewed Egeria's services to manage [metadata valid values](/guides/planning/valid-values/overview). This included a demo.
* We had a lively discussion on a proposal to create lineage abstractions for business users using [Information Supply Chains](/types/7/0720-Information-Supply-Chains) and [Solution Components](/types/7/0735-Solution-Ports-and-Wires).

The call on 22nd February 2023 was cancelled.

### Annual project review

The Egeria project annual review by the [Technical Advisory Board (TAC)](https://wiki.lfaidata.foundation/pages/viewpage.action?pageId=7733341) of the LF AI and Data foundation is still on for 9th March 2023.  The topics we intend to cover are:

* Statistics about the project.
* The status of our bid to achieve the gold CII badge.  This is currently blocked by an issue with the badge application.
* Demonstrations of our project's increasing maturity.
    * The growth in the number of git repositories.
    * Monthly newsletters.
    * Our new Dojos.
    * The security/quality scanning along with the work of the security workgroup.
    * The number of releases we have delivered.
    * The growth of the website's content.
    * The number of technologies integrated with Egeria.
    * The presence of Pragmatic Data Research Ltd to guide vendors and consuming organizations on Egeria Adoption.
* Future development items, such as
    * Cloud native operations
    * Metadata observability
    * Common UI
    * Python clients

## New documentation pages

Each month we will select one or more new pages that where added/updated in the last month to [https://egeria-project.org](https://egeria-project.org) so you can keep up-to-date with how it is evolving.

* [Integration groups](/concepts/integration-group)
* [Types for integration groups](/types/4/0464-Dynamic-Integration-Groups)
* [Description of the Governance Server OMAS](/services/omas/governance-server/overview)


## Connecting with the project

!!! info "Connecting with the project"
    Go to our [community guide](/guides/community) to find out how to find out more about the activities of the Egeria project. 

--8<-- "snippets/abbr.md"
