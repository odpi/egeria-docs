<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Developer Guide

This guide supports developers wishing to customize Egeria to run in additional environments, exchange metadata with additional third party technologies and/or augment existing tools and utilities. 

--8<-- "docs/guides/developer/developer-choices.md"

## Getting Started

The developer guide is organized as follows:

- [Working with the open metadata and governance APIs](#working-with-the-open-metadata-and-governance-apis) - Using Egeria's open metadata and governance APIs to create new services or to augment existing services.

- [Working with the platform APIs](#working-with-the-platform-apis) - Using Egeria APIs to configure and operate Egeria's [OMAG Server Platform](/concepts/omag-server-platform).

- [Using connectors](#using-connectors) - initializing and calling a digital resource connector from external services and other connectors.

- [Building connectors](#extending-egeria-using-connectors) - How to write new [connectors](/concepts/connector) to integrate different technologies together.

- [Building open metadata archives](#building-open-metadata-archives) - Working with [Open Metadata Archives](/concepts/open-metadata-archive) to add new open metadata types or standard metadata definitions that can be shared and loaded into multiple metadata repositories.

- [Adding your own registered services](#adding-registered-services) - Extending Egeria by adding new [registered services](/concepts/omag-subsystem/#registered-services).

- [Build considerations](#build-principles) - Best practises for building extensions to Egeria.


## Working with the open metadata and governance APIs

The open metadata and governance APIs are provided by the [Open Metadata View Services (OMVSs)](/services/omvs).  
The OMVSs run in the [view server](/concepts/view-server) and are designed to be consumed by user interface code typically written in JavaScript.  These interfaces are called directly as REST API calls.  In addition, there is the [Python Client](/guides/developer/python-clients/overview) that enables you to call Egeria's services using the python programming language.



## Working with the platform APIs

The platform APIs fall into three categories:

* Configuring the [OMAG Server Platform](/concepts/omag-server-platform) and [OMAG Servers](/concepts/omag-server).
* Starting and stopping OMAG Servers
* Querying the status of the platform and its servers.

The Java clients for a specific platform API are located in its `-client` module.  For example, the clients for the [Administration Services](/services/admin-services/overview) are in the `admin-services-client` module.

Each Java client has multiple constructors.  The parameters are passed in different combinations to control security and logging.  For example, the configuration clients from the administration services take:

* `serverName` - the name of the OMAG Server to configure.
* `serverPlatformRootURL` - the [platform url root](/concepts/platform-url-root) of the OMAG Server Platform.
* `secretStoreProvider`, `secretStoreLocation` and `secretStoreCollection` - the class name of the connector provider for a [secrets store connector](/concepts/secrets-store-connector), the location of the secrets store and the name of the collection of secrets within it.  The client uses these secrets to authenticate with the platform.  Alternatively, a map of already initialized secrets store connectors can be passed (`secretsStoreConnectorMap`).
* `delegatingUserId` - the optional user identifier of the external user that the client is making the request on behalf of.
* `auditLog` - logging destination for audit log messages.

The constructor may throw `InvalidParameterException` if there is an issue setting up the client-side components based on the supplied parameters.

Below is an example of using the [Administration Services](/services/admin-services/overview) to construct its `MetadataAccessStoreConfigurationClient` client.  As the name suggests, this client is used to configure a new [metadata access store](/concepts/metadata-access-store) server.

??? example "Example: Creating the configuration client for a Metadata Access Store"
    ```java linenums="1"
    MetadataAccessStoreConfigurationClient client = new MetadataAccessStoreConfigurationClient(serverName,
                                                                                               platformURLRoot,
                                                                                               secretStoreProvider,
                                                                                               secretStoreLocation,
                                                                                               secretStoreCollection,
                                                                                               delegatingUserId,
                                                                                               auditLog);
    ```

Once the client is created, use it to call the API it offers which is documented using [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/MetadataAccessStoreConfigurationClient.html){ target=javadoc }.  
For example, the code below sets up the descriptive properties of the server.

??? example "Example: Calling the configuration client for a Metadata Access Store"
    ```java linenums="1"
    client.setServerDescription("Metadata Access Store called " + serverName + " running on platform " + platformURLRoot);
    client.setServerUserId(serverName + "npa");
    client.setServerType(null); // Let the admin service set up the server types
    client.setOrganizationName(organizationName);
    client.setMaxPageSize(maxPageSize);
    ```

!!! education "Further information"

    - [Administration Services](/services/admin-services/overview) for both configuring the OMAG Server Platform and OMAG Servers as well as starting and stopping them.
    - [Platform Services](/services/platform-services/overview) for querying the status of the platform.
    - [Egeria's Javadoc](https://odpi.github.io/egeria/index.html).

## What is a connector?

--8<-- "docs/guides/developer/inside-a-connector.md"

## Using connectors

--8<-- "docs/guides/developer/using-connectors.md"

## Extending Egeria using connectors

Egeria has extended the basic concept of the OCF connector and created specialized connectors for different purposes. The following types of connectors are supported by the Egeria subsystems with links to the documentation and implementation examples.

| Type of Connector                             | Description                                                                      | Documentation                                                                                 | Implementation Examples                                                                                                                                                                                                                             |
|:----------------------------------------------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integration Connector                         | Implements metadata exchange with third party tools.                             | [Building Integration Connectors](/guides/developer/integration-connectors)          | [integration-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors){ target=gh }                                                                      |
| Survey Action Service                         | Implements automated metadata discovery.                                         | [Building Survey Action Services](/guides/developer/survey-action-services/overview)          | [file-survey-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/file-survey-connectors){ target=gh }                                                                  |
| Governance Action Service                     | Implements automated governance.                                                 | [Building Governance Action Services](/guides/developer/governance-action-services/overview)  | [governance-action-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors){ target=gh }                                                          |
| Watchdog Action Service                       | Monitors open metadata for a situation and notifies those who need to know.      | [Building Watchdog Action Services](/guides/developer/watchdog-action-services/overview)      | [watchdog :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/governanceactions/watchdog){ target=gh } |
| Repository Governance Service                 | Maintains open metadata archives from the content of the repositories.           | [Building Repository Governance Services](/guides/developer/repository-governance-services/overview) | [dynamic-archiver-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/dynamic-archiver-connectors){ target=gh } |
| Configuration Document Store                  | Persists the configuration document for an OMAG Server.                          | [Configuration Document Store Connectors](/concepts/configuration-document/#storage)          | [configuration-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh }                                                      |
| Platform Security Connector                   | Manages service authorization for the OMAG Server Platform.                      | [Metadata Security Connectors](/features/metadata-security)                                   | [metadata-security-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/metadata-security-connectors){ target=gh }                                                              |
| Server Security Connector                     | Manages service and metadata instance authorization for an OMAG Server.          | [Metadata Security Connectors](/features/metadata-security)                                   | [metadata-security-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/metadata-security-connectors){ target=gh }                                                              |
| Secrets Store Connector                       | Retrieves secrets (passwords, certificates, ...) from a secure store at runtime. | [Secrets Store Connectors](/concepts/secrets-store-connector)                                 | [secrets-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/secrets-store-connectors){ target=gh }                                                                      |
| Metadata Collection (repository) Store        | Interfaces with a metadata repository API for retrieving and storing metadata.   | [OMRS Repository Connectors](/concepts/repository-connector)                                  | [open-metadata-collection-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh } |
| Metadata Collection (repository) Event Mapper | Maps events from a third party metadata repository to open metadata events.      | [OMRS Event Mappers](/concepts/event-mapper-connector)                                        | none                                                                                                                                                                                                                                                |
| Open Metadata Archive Store                   | Reads an open metadata archive from a particular type of store.                  | [OMRS Open Metadata Archive Store Connector](/concepts/open-metadata-archive-store-connector) | [open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh }                   |
| Audit Log Store                               | Audit logging destination                                                        | [OMRS Audit Log Store Connector](/concepts/audit-log-destination-connector)                         | [audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh }                                           |
| Cohort Registry Store                         | Local store of membership of an open metadata repository cohort.                 | [OMRS Cohort Registry Store](/concepts/cohort-registry-store-connector)                       | [cohort-registry-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors){ target=gh }                   |
| Open Metadata Topic Connector                 | Connects to a topic on an external event bus such as Apache Kafka.               | [Open Metadata Topic Connectors](/concepts/open-metadata-topic-connector)                     | [open-metadata-topic-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors){ target=gh }                                 |
| Digital Resource Connector                    | Provides access to a third party technology.                                     | [Building digital resource connectors](/guides/developer/resource-connectors/overview)        | [file-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors){ target=gh }                                                              |

You can write your own connectors to integrate additional types of technology or extend the capabilities of Egeria - and if you think your connector is more generally useful, you could consider [contributing it to the Egeria project](/guides/community).

## Building open metadata archives

--8<-- "snippets/concepts/open-metadata-archive-intro.md"
--8<-- "docs/guides/developer/open-metadata-archives/in-memory-archive-construction.md"

??? example "Open metadata archive examples"
    * [Defining new types](/guides/developer/open-metadata-archives/defining-new-types)
    * [Code samples of archive builders containing Coco Pharmaceuticals metadata :material-github:](https://github.com/odpi/egeria-samples/tree/main/sample-metadata-archives/coco-metadata-archives){ target=gh }

## Adding registered services
  
Registered services are optional services that plug into Egeria's [OMAG Server Platform](/concepts/omag-server-platform). There are 3 types:
  
  - [Open Metadata Access Services (OMAS)](/services/omas) provide the shared metadata management services used by Egeria's frameworks.  These services run in a [Metadata Access Server](/concepts/metadata-access-server).  Today there are three: OCF Metadata Management (the Connected Asset Services), GAF Metadata Management (the Open Governance Framework services) and OMF Metadata Management (the Open Metadata Store Services).  They are listed in the `AccessServiceDescription` enum.
  
  - [Open Metadata Engine Services (OMES)](/services/omes) provide specialist APIs that support specific types of governance engines.  These services run in an [Engine Host](/concepts/engine-host) and call the access services in a metadata access server to retrieve and maintain open metadata.  They are listed in the `EngineServiceDescription` enum.
   
  - [Open Metadata View Services (OMVS)](/services/omvs) provide specialist REST APIs for browser-based user interfaces (UIs) and the Python clients.  These services run in a [View Server](/concepts/view-server) and call the access services in a metadata access server to retrieve and maintain open metadata.  They are listed in the `ViewServiceDescription` enum.

The `AccessServiceDescription`, `EngineServiceDescription` and `ViewServiceDescription` enums are in the `org.odpi.openmetadata.adminservices.configuration.registration` package of the `admin-services-api` module.  A new registered service needs an entry in the appropriate enum.  In recent releases, new function has been added as view services.

The modules used by each type of registered service in the Egeria project are shown in the table below:

| Module naming                 | Description                                              | OMAS | OMES | OMVS |
|-------------------------------|----------------------------------------------------------|------|------|------|
| *moduleName*-api              | Client java interface(s), property beans and rest beans. | CP   | CP   | N    |
| *moduleName*-client           | Java client implementation.                              | CP   | C    | N    |
| *moduleName*-topic-connectors | Java connectors for sending and receiving events.        | OCP  | N    | N    |
| *moduleName*-server           | Server-side REST and event management implementation.    | P    | P    | P    |
| *moduleName*-spring           | Server-side REST API.                                    | P    | P    | P    |

**Key:**

* CP - Required and runs in external clients plus in the OMAG Server Platform.
* C - Required and runs in external clients.
* P - Required and runs in the OMAG Server Platform.
* OCP - Optional and when provided runs in external clients plus in the OMAG Server Platform.
* N - Not implemented/needed.

A view service has no `-api` or `-client` module because its callers use its REST API directly, or through the [Python clients](/guides/developer/python-clients/overview).  Its `-server` module calls the access services through Java clients such as `EgeriaOpenMetadataStoreClient` from the OMF Metadata Management `omf-metadata-client` module, often wrapped in one of the handler classes from the [Open Metadata Framework (OMF)](/frameworks/omf/overview).

The `-server` module of a registered service typically contains:

* An admin class that extends the admin base class for its type of service (`AccessServiceAdmin`, `EngineServiceAdmin` or `ViewServiceAdmin`).  The admin services call its `initialize()` method when the server starts and its `shutdown()` method when the server stops.
* A registration class that passes a registration entry (for example, a `ViewServiceRegistrationEntry` naming the enum value and the admin class) to the platform's registration class (for example, `OMAGViewServiceRegistration.registerViewService()`).
* An instance class that holds the service's resources for each server, an instance handler that retrieves the instance for a server (and calls the registration class), and a REST services class that implements the REST API.  The REST services class of a view service extends `TokenController`, whose `getUser()` method returns the caller's identity from the bearer token passed on the request.

For example, the [Data Officer OMVS :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/view-services/data-officer){ target=gh } has `DataOfficerAdmin`, `DataOfficerRegistration`, `DataOfficerInstance`, `DataOfficerInstanceHandler` and `DataOfficerRESTServices` classes in its `data-officer-server` module, and the `DataOfficerResource` class in its `data-officer-spring` module.

Inside the registered service's spring module are one or more REST APIs implemented using [Spring Annotations](/guides/contributor/runtime/#spring).  On start up, the OMAG Server Platform issues a *Component Scan* of the `org.odpi.openmetadata.*` packages to gather details of its REST APIs.  This process loads the spring module which in turn loads the server and api modules of registered services it finds, and they are [initialized as part of the platform's capabilities](/concepts/omag-server-platform/#inside-the-omag-server-platform) and are callable via the platform's root URL and port.  To be found, the spring module must be on the platform's CLASSPATH: Egeria's own registered services are added as `runtimeOnly` dependencies in the `build.gradle` file of the [platform-chassis-spring :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/platform-chassis/platform-chassis-spring){ target=gh } module.

For a step-by-step walk through of writing a new view service, from its `ViewServiceDescription` entry to calling it from an HTTP client collection, see [Writing an Open Metadata View Service](/guides/developer/view-services/overview).

The best guide for building registered services are the existing implementations found in [egeria.git](https://github.com/odpi/egeria/tree/main/open-metadata-implementation){ target=gh }.  You can see the way the code is organized and the services that they depend on.

## Build principles

### Which build tool?
Egeria's approach is to use [Gradle](https://gradle.org/){ target = gradle } to build Egeria extensions, and Egeria itself. 

Egeria's own code is built with Gradle because of the following [benefits](https://gradle.org/maven-vs-gradle/){ target = gradle }:

 - Much quicker builds due to caching, incremental compile,change detection, parallelism
 - better flexibility in defining build tasks
 - A more vibrant community with current [discussions](https://discuss.gradle.org){ target = gradle }

Our examples will focus on Gradle, but you may also use [Maven](https://maven.apache.org){ target = maven}. 


### Use stable versions from official repositories

Egeria core libraries, and other java-oriented artifacts created by the Egeria team are published to [Maven Central](https://search.maven.org){ target = maven } (technically this is in fact just an index)

 - Code releases (for example '6.2') go to the *Releases* repository, and will typically be picked up by default by Java build tools
 - Snaphots, which are typically produced by Egeria projects as part of code merge, go to the *Snapshots* repository. This typically needs configuration in a build file

Additionally, when compilation is done locally, a local repository may be populated with artifacts. It is not recommended to use a local build for dependencies in code you develop unless working on core Egeria libraries.

It is recommended to:

 - Depend on releases if possible (ie unless requiring a new feature/fix in code being developed). This is *essential* if your extension is to be stable and read to use
 - Use snapshots if requiring unreleased artifacts, but be aware that the contents can change, or go away
 - Only use a local repository if actively making simultaneous changes to multiple repos, for example if developing a new view service alongside an integration connector. It's inadvisable to check in code with any dependency on local repositories or jars as behaviour will differ depending on the local environment.

### Example build.gradle fragments

```
repositories {
    // If only using mavenCentral you likely will not need a repository section at all
    mavenCentral()
    // Uncomment to use snapshots ie egeria 6.3-SNAPSHOT
    //maven { url("https://central.sonatype.com/repository/maven-snapshots/") }
    // Uncomment to pick up from local ~/.m2 - but can be unpredictable. recommend to use maven central and snapshots
    // mavenLocal()
}
```

If using repositories that may change contents without version - such as snapshots or local repo, ensure gradle always picks up current contents. Not needed when using stable versions.
```
configurations.all {
     // check for updates every build - critical when using Snapshots
     resolutionStrategy.cacheChangingModulesFor 0, 'seconds'
    }
```
## Keep up to date

Aim to keep new connectors, applications etc up to date with Egeria releases, and ensure the version is current when initially creating and contributing.

If your code is hosted on GitHub, [Dependabot](https://github.com/dependabot){ target = gh } is a useful tool for keeping all your dependencies up to date, including on Egeria artifacts.

## Use dependency constraints, especially for multi module projects

[Dependency constraints](https://docs.gradle.org/current/userguide/dependency_constraints.html){ target = gradle } help ensure that anytime you use a dependency in your project, it's the same version, especially in the case of transitive dependencies.

In a [multi-module project](https://docs.gradle.org/current/userguide/multi_project_builds.html){ target = gradle } they should go in the top level `build.gradle` within `AllProjects()` or `SubProjects()`

A [dependency](https://docs.gradle.org/current/userguide/declaring_dependencies.html){ target = gradle} can then be referenced without a version

### Example build.gradle fragment
```
# Use variables to keep things clear
ext {
    egeriaversion = '6.2'
    thriftversion = '0.13.0'
}
# Setup constraints
dependencies {
     constraints {
          // this will ensure a consistent version used whenever we refer to this dependency
          implementation "org.odpi.egeria:audit-log-framework:${egeriaversion}"
          implementation "org.apache.thrift:libthrift:${thriftversion}"
          }
     // This will inherit from our egeria dependency constraints
     implementation platform("org.odpi.egeria:egeria:${egeriaversion}")
     }
```

Later when using a dependency
```
dependencies
    {
         compileOnly "org.odpi.egeria:open-connector-framework"
    }
```
## Minimise chance for duplicate contents

This is primarily a concern for building connectors, or other components that run within the OMAG Server Platform. In this environment we already have a lot of Egeria code on the classpath so ideally we want to only add what's needed, not duplicate what is already there.

This is to get a balance of:

 - ease of use in deploying the connector
 - avoid clashing library versions
 - minimize size of artifact

Some terms that you may hear of

 - 'thin' jar - often taken to mean just your code, ie no dependencies
 - 'fat' or 'uber' jar - often taken to mean your code and all it's dependencies.

To achieve a sensible balance what we actually want is to:

 - include your code
 - omit anything already in the platform
 - add in other dependencies that your code calls

To do this, you will often want to build a jar with dependencies, but with care taken over use of 'scope'. Often this will mean Egeria dependencies will be `compileOnly` or `testCompileOnly` (The equivalent in maven is 'provided').

If this is not done, there's a risk of having two different versions of core libraries present in the classpath. This could cause either your code, or other Egeria code to malfunction. 

Careful scoping combined with maintaining currency, minimizes this risk.

Other techniques to avoid this issue include:

- Using sharding to rename classes
- Using a dedicated class loader (this requires framework place, and not supported by Egeria at this time).

### Example build.gradle fragment
```
     compileOnly "org.odpi.egeria:open-connector-framework"
     implementation "org.apache.thrift:libthrift"
```
## Complex dependency manipulation

- If you need to have a dependency, but it has vulnerabilities, then may need to exclude libraries with vulnerabilities; for example if they being brought in, but your code is not using them.
For an example on how this has been done see [the HMS connector](https://github.com/odpi/egeria-connector-hivemetastore/blob/main/build.gradle){ target = gh }.
- If you need to pick up a dependency, but there are multiple versions around at runtime, then  this build file uses `forceResolution` strategy to force
a particular dependency version; for an example of this see [the HMS connector](https://github.com/odpi/egeria-connector-hivemetastore/blob/main/build.gradle){ target = gh }.
- you need to ensure that appropriate versions of jars are available at runtime so that classes can be found.


## Summary

Egeria is designed to simplify the effort necessary to integrate different technologies so that they can actively share and consume metadata from each other.

It focuses on providing five types of integration interfaces.

- [Connectors](#what-is-a-connector) that translate between third party APIs and open metadata APIs. These connectors are hosted in the Egeria servers and support the active exchange of metadata with these technologies.
- [Connectors](/guides/developer/using-connectors) for accessing popular type of data sources that also retrieve open metadata about the data source. This allows applications and tools to understand the structure, meaning, profile, quality and lineage of the data they are using.
- [Python clients](/guides/developer/python-clients/overview) for applications to call the [view services' REST](/services/omvs) interfaces, each of which are crafted for particular types of user and task.
- REST APIs for the Egeria Services. These include the [view services](/services/omvs), [access services](/services/omas), [admin services](/services/admin-services/overview) and [platform services](/services/platform-services/overview).
- Kafka topics with JSON payloads for asynchronous communication (both in and out) with the open metadata ecosystem.
  [Learn more ...](/concepts/out-topic)


--8<-- "snippets/abbr.md"
