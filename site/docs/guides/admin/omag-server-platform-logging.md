<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Configuring debug logging options for OMAG Server Platform

## Options for logging system using the Spring Boot Platform Chassis

The OMAG Server Platform is written using Spring Boot. As such, it comes with support for variety of logging options.
You can always check the options in the official guidelines [here](https://docs.spring.io/spring-boot/docs/current/reference/html/howto.html#howto-logging). 

Spring itself uses abstraction layer and chooses the logging implementation during runtime based on content of the classpath.
The OMAG Server Platform uses web starter by default, which brings basic logging options from JCL and the *Logback* logging system.

## Configuring the logging that is produced

As described in the Spring documentation, you can control log levels for specific category logger using system or application properties:

```properties
logging.level.root=ERROR
logging.level.org.springframework.web=DEBUG
logging.level.org.odpi.openmetadata=ERROR
```

## Routing debug logging to the appropriate destination(s)

The application properties control what is produced, a `logback.xml` file in the OMAG Server Platform's class path (ie in a directory specified in the `-Dloader.path`) controls the destination of the debug logging.

There is an example `logback.xml` file in the [`egeria.git`](https://github.com/odpi/egeria/blob/main/logback.xml) repository.  It controls the destination of the debug logging coming from the platform as well as providing a specific destination for the redirected audit logging coming from an OMAG Server.

## Connecting OMAG Audit Logging for an OMAG Server

While the default logging framework enables a generic interface for debug logging, this is not adequate option for diagnostic and auditing of the open metadata ecosystem.  This is provided by Egeria's [Audit Log Framework (ALF)](/frameworks/alf/overview) described in the [Diagnostics Guide](/guides/diagnostic/overview).
 
The Audit Log Framework is configured in an OMAG Server's [configuration document](/concepts/configuration-document).  It allows you to choose the destination of the audit log records produced by the servers running on the platform.  
By default, the server's audit log records are summarized and output to the console - system standard output (stdout) - as a destination. 
  
The SLF4J logging destination transforms the audit log records into debug messages and publishes them to a dedicated logger category:

```properties
logging.level.org.odpi.openmetadata.frameworks.auditlog=INFO
```

Using SLF4J audit log destination, you can also have granular logger category control using the naming pattern below:

`logging.level.org.odpi.openmetadata.frameworks.auditlog.{omag-server-name}.{originator-component-name}`

> Note that the category is defined by omitting the empty space characters.

Example:

```properties
logging.level.org.odpi.openmetadata.frameworks.auditlog.omag-server-1=INFO
logging.level.org.odpi.openmetadata.frameworks.auditlog.omag-server-2.RepositoryContentManager=ERROR
```

Although this approach loses part of the information available from the audit log record, it does allow the output to be routed via logback.  This is an advantage if the organization is already using this type of logging for its IT operations.  The audit log records can also be routed to a different destination for the consumption of the users and stewards of th open metadata ecosystem.

## Example logging configuration

See [example of configuring Egeria's Audit Log, and debug logging, to output JSON via the console](omag-server-platform-logging-jsonexample.md)

--8<-- "snippets/abbr.md"
