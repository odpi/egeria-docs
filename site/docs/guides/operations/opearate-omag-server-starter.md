# Operate OMAG Server Starter

This guide focuses on providing instructions how to operate server as stand-alone application process. This deployment choice gives you low level control of the application runtime and it requires direct interaction with your IT infrastructure.

With OMAG Server Starter each server runs in its own dedicated JVM process. All the required parameters to start a server are always determined up-front and supplied as configuration properties to the application. This approach is key to achieve immutable configuration state in case of running containerized deployment.

> Quick jump to installation steps (coming soon)

## Running OMAG Server Starter

To run the OMAG server starter application you execute command in this format:

`java <java options> -jar omag-server-{release}.jar <properties>`

or for example, to start with minimal sample configuration:

```bash
java -jar omag-server-*.jar --omag.server-config-file=classpath:samples/metadata-repository-server.yml --server.port=9080 --server.ssl.enabled=false
```

```bash
 Project Egeria - Open Metadata and Governance
    ____   __  ___ ___    ______   _____
   / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____
  / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/
 / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /
 \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/

 :: Powered by Spring Boot (v3.1.1) ::

2023-09-19T15:10:45.763+02:00  INFO 94379 --- [           main] o.o.o.s.springboot.OMAGServer            : Starting OMAGServer using Java 17.0.8.1 with PID 94379 (/server/omag-server-4.3.jar started by ***** in /server)
2023-09-19T15:10:45.765+02:00  INFO 94379 --- [           main] o.o.o.s.springboot.OMAGServer            : No active profile set, falling back to 1 default profile: "default"
2023-09-19T15:10:47.488+02:00  INFO 94379 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9080 (http)
2023-09-19T15:10:47.497+02:00  INFO 94379 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2023-09-19T15:10:47.497+02:00  INFO 94379 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.10]
2023-09-19T15:10:47.565+02:00  INFO 94379 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2023-09-19T15:10:47.566+02:00  INFO 94379 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1756 ms
2023-09-19T15:10:48.356+02:00  INFO 94379 --- [           main] EnvironmentConfiguration$$SpringCGLIB$$0 : SSL configuration started working directory: /server
2023-09-19T15:10:48.824+02:00  INFO 94379 --- [           main] o.s.b.a.e.web.EndpointLinksResolver      : Exposing 2 endpoint(s) beneath base path '/actuator'
2023-09-19T15:10:48.895+02:00  INFO 94379 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 9080 (http) with context path ''
2023-09-19T15:10:48.909+02:00  INFO 94379 --- [           main] o.o.o.s.springboot.OMAGServer            : Started OMAGServer in 3.58 seconds (process running for 4.092)
2023-09-19T15:10:48.932+02:00  INFO 94379 --- [           main] o.o.o.s.s.config.OMAGConfigHelper        : Using configuration from class path resource [samples/metadata-repository-server.yml]
2023-09-19T15:10:49.162+02:00  INFO 94379 --- [           main] o.o.o.s.springboot.OMAGServer            : Sending activation request for server: cocoMDS1 and user: OMAGServer
2023-09-19T15:10:49.341+02:00  INFO 94379 --- [           main] o.o.o.s.springboot.OMAGServer            : Activation succeeded for server: cocoMDS1

```

> Note that the java executable jar is different then in case of running OMAG server platform.

## Configuration Reference

Considering that the starter application is implemented using Spring Boot, we can use different styles to configure the server starter. It is a matter of choice in what way properties will be provided to the application: command line options, application properties or environment variables. The started application will load all and use them on startup.

!!! info "Spring application external config"
    If want to know more about how external configuration works, you can read more int the spring boot [core features](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.external-config){ target=_blank } .

OMAG server starter already has default [`application.properties`](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/server-chassis/server-chassis-spring/src/main/resources/application.properties){ target=gh } packaged within the jar distribution. These properties can ba always overwritten if they are provided to the application externally.

Below you can find reference properties that define the application behavior.

### Server Configuration File

| Property name           | Environment variable  | Description  | Example |
|-------------------------|-----------------------|--------------|---------|
|`omag.server-config-file`|`OMAG_SERVERCONFIGFILE`| The OMAG server configuration file defining all subsystems and respective connectors. It should be valid [configuration document structure](/concepts/configuration-document/#configuration-document-structure). Can be written in .json or .yaml file format. | See [samples](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/server-chassis/server-chassis-spring/src/main/resources/samples){ target=gh } |

!!! tip "Creating configuration document"
    The configuration document can be crafted by hand if you understand well [configuration document structure](/concepts/configuration-document/#configuration-document-structure). Safe option is to use OMAG server platform deployment and create configuration document using admin services. Refer to [Admin guide](/guides/admin/servers) to see how different server types are configured. Finally you can [retrieve](/guides/admin/servers/#retrieving-the-configuration) the valid document created for use with the server starter.

### Additional Libraries

| Property name           | Environment variable  | Description  | Example |
|-------------------------|-----------------------|--------------|---------|
| `loader.path` | `LOADER_PATH` | The Spring Boot extended class-path. This is the main mechanism used to load externally Egeria or third party connector libraries. | loader.path="/deployments/server/lib" |

### Web Server and SSL Transport

| Property name           | Environment variable  | Description  | Example |
|-------------------------|-----------------------|--------------|---------|
|`server.port` | SERVER_PORT | Server transport port | server.port=9443 |
|`server.ssl.enabled`| SERVER_SSL_ENABLED | Enables SSL transport for the embedded web server (Tomcat) | server.ssl.enabled=false disables server ssl. In this case all other server.ssl properties are not required. |
|`server.ssl.key-store`| SERVER_SSL_KEYSTORE | Java key-store file used to load the server certificates | server.ssl.key-store=keystore.p12 |
|`server.ssl.key-store-password`| SERVER_SSL_KEYSTORE_PASSWORD | Secret used by the server to access the key-store file | server.ssl.key-store-password=egeria |
|`server.ssl.keyStoreType` | SERVER_SSL_KEYSTORETYPE | The type of keystore file used | server.ssl.keyStoreType=PKCS12 |
|`server.ssl.keyAlias`| SERVER_SSL_KEYALIAS | The alias used for the ssl key | server.ssl.keyAlias=egeriaserverchassis |
|`server.ssl.trust-store` | SERVER_SSL_TRUSTSTORE | Java trust-store file used by the server | server.ssl.trust-store=truststore.p12 |
|`server.ssl.trust-store-password` | SERVER_SSL_TRUSTSTOREPASSWORD | Secret used by the server to access trust-store file | server.ssl.trust-store-password=egeria |
|`strict.ssl`| STRICT_SSL | Controls mTLS for http client, thats if ssl should be validated for outbound connections | strict.ssl=false will turn off client ssl validation for external servers (considered unsafe). |

### Logging

Default Spring Boot application [logging feature](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.logging){ target=_blank } is used as technical log implementation. Egeria [Audit Logs framework](/frameworks/alf/overview/) can be configured further via SLF4J connector to re-direct the OMAG logs to the technical logging or log directly via console connector (default).

### Application availability

The application availability state is managed in a standard way using [Actuator](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.spring-application.application-availability){ target=_blank } leveraging standard internal Spring application lifecycle and its states.

Health state is exposed via management configuration as rest endpoints that can be used as probes for managing pod lifecycle in Kubernetes.

Example using default actuator endpoints to retrieve health information:

```bash
> curl http://localhost:9080/actuator/health/livenessState 
{"status":"UP"} 

> curl http://localhost:9080/actuator/health/readinessState
{"status":"UP"}

```

### Default logging and monitoring configuration

Already configured with default `application.properties`

```properties
logging.level.org.odpi.openmetadata=error
logging.level.org.odpi.openmetadata.frameworks.auditlog=info
logging.level.org.odpi.openmetadata.serverchassis.springboot=info

management.health.defaults.enabled=false
management.health.livenessstate.enabled=true
management.health.readinessstate.enabled=true

management.endpoints.enabled-by-default=false
management.endpoint.health.enabled=true
management.endpoint.health.show-details=always
management.endpoint.metrics.enabled=true
management.endpoints.web.exposure.include=metrics,health
```

More info on customizing common Application Properties can be found in spring [reference documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties){ target=_blank }.

## Run in a Container

To run the server starter application in a container you need container image. Egeria core image offers variety of options to run Egeria OMAG applications. As part of the official distribution, the full Egeria assembly is packaged as Docker image including the OMAG server started jar. The image is based on RedHat's [ubi9/openjdk-17](https://catalog.redhat.com/software/containers/ubi9/openjdk-17-runtime/61ee7d45384a3eb331996bee){ target=_blank }

The executable jar is located in the image at following location:

`/deployments/server/omag-server-{release}.jar`

By modifying the environment variable `JAVA_APP_JAR` to point to this location, you modify the container entry point thus reusing the image configured by default to initialize OMAG server platform.

All other settings can be configured by setting the environment variables configuring the OMAG server behavior.

### Run in Docker

To run OMAG Server as Metadata Repository using sample configuration execute following command:

```bash
docker run --name omag-server -p 9443:9443 --env JAVA_APP_JAR="server/omag-server-4.3.jar" --env LOADER_PATH="/deployments/server/lib" --env OMAG_SERVERCONFIGFILE="classpath:samples/metadata-repository-server.json" quay.io/odpi/egeria:4.3
```

### Run in Kubernetes

To run in a Kubernetes environment, you need to make certain choices and properly plan the deployment resources. To showcase how simple single server deployment can be done we created [`omag-server`](https://github.com/odpi/egeria-charts/tree/main/charts/egeria-server){ target=gh } Helm chart. It can be used as quick reference for defining kubernetes deployment and configuration resources and planning more complex deployments.
