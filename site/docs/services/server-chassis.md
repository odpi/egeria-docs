---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# OMAG Server Chassis

The *Server Chassis* provides the base server framework, such as the web server and the REST API endpoint support for the [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform).   Calls to the server chassis are then routed to the appropriate [OMAG subsystem](/concepts/omag-subsystem).

Today, Egeria has one server chassis implementation called [*server-chassis-spring*](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/server-chassis/server-chassis-spring) that uses [Spring Boot](https://spring.io/projects/spring-boot).  Its `main()` method is located in a Java class called `OMAGServerPlatform`.

## Maven build profiles

Egeria's default maven build will include the *full-platform* profile, that includes [all available services](/services) in the running OMAG Server Platform. 

There is a build option called `-DadminChassisOnly` that will not include any [registered services](/services/#registered-services).

Selective registered services can then be activated using the [ **loader.path** spring-boot functionality ](https://docs.spring.io/spring-boot/docs/current/reference/html/appendix-executable-jar-format.html#executable-jar-property-launcher-features).

The `-DadminChassisOnly` is used for creating a cut down OMAG Server Platform
for a specific deployment.
 
## Application properties

Since the OMAG Server Platform is a Spring Boot application, it can be
[customized using the application.properties](https://docs.spring.io/spring-boot/docs/current/reference/html/common-application-properties.html) file found in the `resources` directory and using environment variables.

For example, OMAG servers can be automatically activated at startup by setting spring-boot property `startup.server.list`, typically in the `application.properties` file. The server names are listed without quotes. For example:

```
startup.server.list=cocoMDS1, cocoMDS2
```

Each server is started with the administration user id set in the spring-boot property `startup.user`.

For example:
```
startup.user=garygeeke
```
By default, this user id is set to the user id `system`.

When the platform shuts down, if any of the servers that were in the startup list are still running, they will be shut down before the server completes.

If `startup.server.list` is null then no servers are automatically started or stopped.

```
startup.server.list=
```

## Adding a new subsystem to the OMAG Server Platform

When the **OMAGServerPlatform** class is called, Spring Boot does a component scan for all Spring services that are in Java packages stemming from `org.odpi.openmetadata.*` and that are visible to this module.

To make a new Java package visible to **OMAGServerPlatform**, add its **spring** package to the **pom.xml** file for **server-chassis-spring** and it will be picked up in the component scan.

For example, this is the snippet of XML in the pom.xml file that adds the [Asset Owner OMAS](/services/omas/asset-owner/overview) services to the OMAG server platform.

```xml
<dependency>
    <groupId>org.odpi.egeria</groupId>
    <artifactId>asset-owner-spring</artifactId>
</dependency>
```

## Swagger

Swagger API documentation is generated with the chassis and is documented in [Swagger Generation](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/server-chassis/server-chassis-spring/SwaggerGeneration.md).

## Spring Boot Actuator

Spring Boot Actuator is used to expose operational information about the running application such as health, metrics, info, dump.  It uses HTTP endpoints or JMX beans to enable us to interact with it. 

A “discovery page” is added with links to all the endpoints. The “discovery page” is available on /actuator by default. Once this dependency is on the class-path /info and /health endpoints are available out of the box. 

In order to expose all endpoints over HTTP, use the following property:
```
management.endpoints.web.exposure.inlude=*
```

The `exclude` property lists the IDs of the endpoints that should not be exposed. For example, to expose everything over HTTP except the env and beans endpoints, use the following properties:

```
management.endpoints.web.exposure.include=*
management.endpoints.web.exposure.exclude=env,beans
```

The exclude property takes precedence over the include property.

--8<-- "snippets/abbr.md"