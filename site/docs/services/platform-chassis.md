<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# OMAG Server Platform Chassis

The *Platform Chassis* provides the base runtime framework, such as the web server and the REST API endpoint support for the [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform).   Calls to the platform chassis are then routed to the appropriate [OMAG subsystem](/concepts/omag-subsystem).

Today, Egeria has one platform chassis implementation called [*platform-chassis-spring*](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/platform-chassis/platform-chassis-spring) that uses [Spring Boot](https://spring.io/projects/spring-boot).  Its `main()` method is located in a Java class called `OMAGServerPlatform`.

## Alternate build option

Egeria's default build will include the *full-platform* profile, that includes [all available services](/services) in the running OMAG Server Platform. 

There is a build option called `-PadminChassisOnly` that will not include any [registered services](/services/#registered-services) nor connector implementations.

Selective registered services can then be activated via the [ **loader.path** spring-boot functionality ](https://docs.spring.io/spring-boot/docs/current/reference/html/appendix-executable-jar-format.html#executable-jar-property-launcher-features).

The `-PadminChassisOnly` is used for creating a cut down OMAG Server Platform for a specific deployment.
 
## Application properties

Since the OMAG Server Platform is a Spring Boot application, it can be [customized using the application.properties](https://docs.spring.io/spring-boot/docs/current/reference/html/common-application-properties.html) file found in the platform's working directory and using environment variables.  Details of the application properties supported by the platform chassis are describe in [Configuring the OMAG Server Platform](/guides/admin/configuring-the-omag-server-platform)

## Adding a new registered service implementation to the OMAG Server Platform

When the *OMAGServerPlatform* class is called, Spring Boot does a component scan for all Spring services that are in Java packages stemming from `org.odpi.openmetadata.*` and that are visible to this module.

To make a new Java package visible to **OMAGServerPlatform**, add its **spring** package to the **build.gradle** file for **platform-chassis-spring**. It will be picked up in the component scan.

For example, this is the snippet of the build.gradle file that adds the [Asset Catalog](/services/omvs/asset-catalog/overview) API to the OMAG Server Platform.

```
        runtimeOnly project(':open-metadata-implementation:view-services:asset-catalog:asset-catalog-spring')
```


## Spring Boot Actuator

Spring Boot Actuator is used to expose operational information about the running application such as health, metrics, info, dump.  It uses HTTP endpoints or JMX beans to enable us to interact with it. 

A “discovery page” is added with links to all the endpoints. The “discovery page” is available on /actuator by default. Once this dependency is on the class-path /info and /health endpoints are available out of the box. 

In order to expose all endpoints over HTTP, use the following property:
```
management.endpoints.web.exposure.include=*
```

The `exclude` property lists the IDs of the endpoints that should not be exposed. For example, to expose everything over HTTP except the env and beans endpoints, use the following properties:

```
management.endpoints.web.exposure.include=*
management.endpoints.web.exposure.exclude=env,beans
```

The `exclude` property takes precedence over the include property.

--8<-- "snippets/abbr.md"
