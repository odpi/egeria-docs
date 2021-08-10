<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring the OMAG Server Platform

The [OMAG Server Platform](/egeria/concepts/omag-server-platform) is a JVM process that includes a Tomcat
web server and uses [Spring Boot :material-dock-window:](https://spring.io/){ target=spring } to support REST APIs.

## Default setup

- REST APIs are registered at `https://localhost:9443`. This address is called the platform's
  [platform's URL root](/egeria/concepts/omag-server/#platform-url-root)
  and is configured in a number of places in the [OMAG server's](/egeria/concepts/omag-server) configuration.
- The platform supports no specific security authorization.
- All configuration is stored in encrypted files - one for each [OMAG server](/egeria/concepts/omag-server)
  configured to run on it.

!!! attention "Useful for development, be wary for production"
    These defaults are suitable for a development environment; however, for
    production the platform should be configured with platform security because this ensures configuration
    is managed by authorized users.

## Configuring other options

![What needs to be configured in the server platform](configurability-of-platform.png)

### Configuration store

The [configuration document](/egeria/concepts/configuration-document)
is the place where the configuration for a single [OMAG server](/egeria/concepts/omag-server)
is stored. This may include security certificates and passwords.

By default, the configuration document is stored in its own encrypted file in the home
directory of the [OMAG Server Platform](/egeria/concepts/omag-server-platform), named:

```
omag.server.{serverName}.config
```

As of v2.0 of Egeria, the contents of the configuration document are
stored in an encrypted JSON format[^1].
The clear-text contents of the configuration document can still be retrieved
by accessing the admin services endpoint for retrieving the configuration
document; however, this ensures security is applied before a user is able
to retrieve the configuration document's contents:

!!! get "GET - retrieve configuration document"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/configuration/
    ```

You may also wish to:

- Move the location of the configuration documents
- Write you own alternative store for the configuration documents

All of these options are possible because the configuration document
store is implemented in a
[configuration document store connector](/egeria/concepts/configuration-document/#storage).
It is therefore possible to change the implementation or behavior
of this connector with a simple configuration change to the
OMAG Server Platform.

The configuration document store connector is configured in the OMAG Server Platform
using the following command:

!!! post "POST - configure the configuration store"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/stores/connection
    ```

    The request body should be a connection object used to create the connector to the configuration
    document store.

!!! attention "Ensure the connector is available in the classpath"
    In order to use any connector other than the default, you need to also ensure that
    the Connector and its ConnectorProvider class are available to the server platform (i.e. the
    jar file containing them is available in the `LOADER_PATH` location of the server platform).

??? example "Exmaple: (unencrypted) file store connector"
    For example, this connection would set up the (unencrypted) file store connector:

    ```json linenums="1"
    {
        "class": "Connection",
        "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "org.odpi.openmetadata.adapters.adminservices.configurationstore.file.FileBasedServerConfigStoreProvider"
        },
        "endpoint": {
            "class": "Endpoint",
            "address": "omag.server.{0}.config"
        }
    }
    ```

??? example "Example: encrypted JSON file store, non-default location"
    As another example, this connection uses the default encrypted JSON file store, but the files
    are stored in a different location (`/my-config/omag.server.{0}.config`).

    ```json linenums="1"
    {
        "class": "Connection",
        "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "org.odpi.openmetadata.adapters.adminservices.configurationstore.encryptedfile.EncryptedFileBasedServerConfigStoreProvider"
        },
        "endpoint": {
            "class": "Endpoint",
            "address": "/my-config/omag.server.{0}.config"
        }
    }
    ```

#### Determine configured store

It is possible to query the setting of the configuration document store connector
using the following command:

!!! get "GET - retrieve configured configuration document store"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/stores/connection
    ```

??? success "Response indicating default configuration store (encrypted JSON file store)"
    ```json
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200
    }
    ```

??? success "Response indicating a specific connector"
    If the response looks more like the JSON below, a connector is configured.  The
    `connectorProviderClassName` tells you which connector is being used and the `address` shows where the
    configuration documents are stored.

    ```json hl_lines="8 12"
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200,
        "connection": {
            "class": "Connection",
            "connectorType": {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.adminservices.configurationstore.file.FileBasedServerConfigStoreProvider"
            },
            "endpoint": {
                "class": "Endpoint",
                "address": "omag.server.{0}.config"
            }
        }
    }
    ```

#### Remove configured store

It is also possible to remove the configuration for the connector using
the following command:

!!! delete "DELETE - remove configured configuration store"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/stores/connection
    ```

This reverts the store to the default encrypted JSON file store.

### Platform security

The [OMAG Server Platform](/egeria/concepts/omag-server-platform)
provides both configuration and diagnostic services
for [OMAG servers](/egeria/concepts/omag-server) which in themselves
provide access to a wide variety of information and control points.

Therefore, it is necessary to provide authorization services
relating to the use of the platform services.

Egeria provides [a platform security authorization capability :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/common-services/metadata-security){ target=gh }.
It is implemented in a platform security connector
that is called whenever requests are made to the server platform services.

Security is configured for a specific platform once it is running by
using the following command.

!!! post "POST - configure platform security"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/platform/security/connection
    ```

    The request body should be a connection object used to create the platform security connector and
    the [platform URL root](/egeria/concepts/omag-server/#platform-url-root) of the platform.

??? example "Example: sample platform security connector"
    For example, this is the request body that would
    set up the [sample platform security connector](../../../../open-metadata-resources/open-metadata-samples/open-metadata-security-samples)
    provided for the Coco Pharmaceuticals case study:

    ```json
    {
        "class": "PlatformSecurityRequestBody",
        "urlRoot": "{{platformURLRoot}}",
        "platformSecurityConnection" : {
    	    "class": "Connection",
    	    "connectorType": {
    	        "class": "ConnectorType",
    	        "connectorProviderClassName": "org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaPlatformSecurityProvider"
    	    }
        }
    }
    ```

#### Determine configured security

It is possible to query the setting of the platform security connector
using the following command:

!!! get "GET - retrieve configured platform security"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/platform/security/connection
    ```

??? success "Response indicating no security"
    ```json
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200
    }
    ```

??? success "Response indicating a specific security connector"
    If the response looks more like the JSON below, a connector is configured. The
    `connectorProviderClassName` tells you which connector is being used.

    ```json hl_lines="8"
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200,
        "connection": {
            "class": "Connection",
            "connectorType": {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaPlatformSecurityProvider"
            }
        }
    }
    ```

#### Remove configured security

It is possible to remove the configuration for the connector using
the following command:

!!! delete "DELETE - remove configured platform security"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/platform/security/connection
    ```

This removes all authorization checking from the platform services.

## application.properties

Since the OMAG Server Platform is a Spring Boot application, there are other values that can be set in
its **application.properties** file found in the **resources** subdirectory:

- Defining the port that the OMAG Server Platform will listen on for
  REST API calls.
- Controlling the level of developer logging that the platform
  produces when it is running. See [Configuring logging options](omag-server-platform-logging.md) for more details.
- Defining where the connector implementations should be loaded from.

Spring provides [extensive documentation on its standard properties :material-dock-window:](https://docs.spring.io/spring-boot/docs/current/reference/html/appendix-application-properties.html){ target=spring }.

## Auto-starting servers

An [OMAG server](/egeria/concepts/omag-server) is typically started on the [OMAG Server Platform](/egeria/concepts/omag-server-platform)
using a command; however, it is possible to set up a list of servers that are automatically started
whenever the platform is started. These servers are also automatically shutdown when the platform
is shutdown.

OMAG servers can be automatically activated at startup by setting spring-boot property
`startup.server.list`, typically in the `application.properties` file.
The server names are listed without quotes. For example:

```properties
startup.server.list=cocoMDS1, cocoMDS2
```

Each server is started with the administration user id set in the spring-boot property `startup.user`.

For example:

```properties
startup.user=garygeeke
```

By default, this user id is set to the user id `system`.

When the platform shuts down, if any of the servers that were in the startup list are still running,
they will be shut down before the server completes.

!!! summary "Default setting"
    If `startup.server.list` is null then no servers are automatically started or stopped.

    ```properties
    startup.server.list=
    ```

    This is the default setting.

## Transport Layer Security (TLS)

Transport layer security describes the security applied to API calls made between servers.
The most commonly known transport layer security is SSL.

Egeria uses TLS with certificates to secure the communication to and from the
[OMAG Server Platforms](/egeria/concepts/omag-server-platform).

### Brief background on TLS

[Transport Layer Security (TLS) :material-dock-window:](https://en.wikipedia.org/wiki/Transport_Layer_Security){ target=wikipedia }
protects communications over network connections through encryption,
authentication and integrity. It is just one layer of security of many.

#### One-way SSL exchange

One-way SSL exchange is typically in use when browsing the web - since as a user
you are most concerned that the server you are connecting to is authentic.

With this approach, the server is not able to guarantee your authenticity at the transport level.
This means you can
be assured of the identity of the server, but it cannot be sure of who you are.

![SSL exchange](ssl-oneway.svg)

#### Two-way (mutual) SSL exchange

With two-way (mutual) SSL exchange, trust is established both ways.
This [mutual authentication :material-dock-window:](https://en.wikipedia.org/wiki/Mutual_authentication){ target=wikipedia }
is more typical when interconnecting different systems and applications which are known in advance.

![SSL exchange](ssl-mutual.svg)

### Certificates for the OMAG Server Platform

!!! attention "Important note on terminology"
    Egeria's [OMAG Server Platform](/egeria/concepts/omag-server-platform) is a Spring Boot based application.
    We refer to it as Egeria's "platform", which hosts Egeria [OMAG wervers](/egeria/concepts/omag-server).

    However, in the documentation relating to network communications and SSL,
    a "server" is usually seen as an application listening on a network port.
    For Egeria, this "server" would be the OMAG Server Platform.
    It is important to be aware of this terminology difference when
    reading the links and references mentioned here.

An instance of the OMAG Server Platform services requests over a REST based API
from other OMAG Server Platforms, UIs, tools and engines.
In this regard its role in SSL network requests described above is that of a
**network server**, with its callers performing the role of a **network client**.

However, since the OMAG Server Platform also makes requests to other systems
(including other OMAG Server Platforms and Apache Kafka)
it is also fulfilling a **network client** role.

As a Spring application, the OMAG Server Platform's configuration for its network server role allows
the following Spring properties to be set:

| Property | Use |
|---|---|
| `server.ssl-key-store` | Used by Tomcat/Spring Boot to locate keys that identify the server |
| `server.ssl-key-alias` | Used by Tomcat/Spring Boot to identify the alias of the key tomcat should use for itself |
| `server.ssl.key-store-password` | Used by Tomcat/Spring Boot for the keystore password (2 way SSL) |
| `server.ssl.trust-store` | Used by Tomcat/Spring Boot to understand what clients it can trust (2 way SSL) |
| `server.ssl.trust-store-password` | Used by Tomcat/Spring Boot  for the password of the truststore (2 way SSL) |
| `strict.ssl` | This is an additional parameter Egeria provides (non-standard Spring property) which if `true` causes SSL verification to be skipped entirely |

For further details on these and other less common configuration options, refer to the Spring Docs.

Since the OMAG Server Platform is also a network client the settings in the next section for
clients are also required.

### Egeria Java clients

Standard Java properties need to be set within the JVM running the Egeria client code (this includes the
OMAG Server Platform):

| Property | Use |
|---|---|
| `javax.net.ssl.keyStore` | keyStore for client to use (2 way SSL needs this) |
| `javax.net.ssl.keyStorePassword` | password for the keystore  (2 way SSL needs this) |
| `javax.net.ssl.trustStore` | trustStore for the client to use (always needs setting as Egeria makes client calls) |
| `javax.net.ssl.trustStorePassword` | password for the truststore (always - as above) |
| `strict.ssl` | For any executable jars provided by Egeria (such as samples), setting this additional parameter to `true` will cause SSL verification to be skipped. This is only recommended for test and development. |

Note that in the case of Java clients, these are system properties, and do not use Spring conventions.

### Other clients

Similar principles to those documented for Java should apply. If you need further assistance, please
contact the team on [Slack :fontawesome-brands-slack:](https://lfaifoundation.slack.com/archives/C01F40J2XA8){ target=slack }.
A pull request (or issue) with contributed documentation is also very welcome!

### Example to launch Egeria

Examples certificates are provided in the codebase under
[open-metadata-resources/open-metadata-deployment/certificates :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-deployment/certificates){ target=gh }

As an example of running the Egeria server chassis with the certificates generated above, add
the following options when launching the OMAG Server Platform jar file:

```
-Dserver.ssl.key-store=${KS}
-Dserver.ssl.key-alias=EgeriaServerChassis
-Dserver.ssl.key-store-password=egeria
-Dserver.ssl.trust-store=EgeriaCA.p12
-Dserver.ssl.trust-store-password=egeria
-Djavax.net.ssl.keyStore=EgeriaServerChassis
-Djavax.net.ssl.keyStorePassword=egeria
-Djavax.net.ssl.trustStore=EgeriaCA.p12
-Djavax.net.ssl.trustStorePassword=egeria
```

??? question "Detailed explanation"
    We have to use both `server.ssl` and `javax.net` values since the former controls how the OMAG Server Platform
    works when accepting inbound connections and the latter are needed when it acts as a network client.

    We have assumed the default keystore passwords, and also that we will use the same key regardless of whether it is the one
    that the chassis sends back to its client after they connect, or the one the chassis may send to those other repositories. They
    could be distinct if needed.

### Creating your own certificates

The example certificates are fine for development; however, it is important to have your own certificates
for a production environment.

An example script (MacOS/Linux) to create certificates is provided in [`gensamplecerts.sh` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-resources/open-metadata-deployment/certificates/gensamplecerts.sh){ target=gh }.
It is intended only as an example. It requires the `openssl` tool and `keytool`. Deployment frameworks in
cloud services may also offer support to generate certificates, and it is likely an enterprise process
will be in place in larger organizations.

The script creates a Certificate Authority and then specific certificates for different Egeria components.
It could be extended to create certificates for other clients especially if using 2 way SSL.

When the script is run it also makes use of the configuration template [`openssl.cnf` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-resources/open-metadata-deployment/certificates/openssl.cnf){ target=gh }.

Together, both set some important characteristics that are needed to allow the certificate to work properly,
especially with current browsers:

- ensuring `basicConstraints` are specified
- ensuring the certificate expiry time is not too far in the future
- ensuring `subjectAltName` is specified.

??? note "Additional notes on building diagrams"
    The rendered image files are checked in, however when updating, the diagrams can be regenerated using [PlantUML :material-dock-window:](https://plantuml.com){ target=new }

    For example: `plantuml -svg ssl-oneway.puml`

    The diagrams are best rendered to svg, however notes do not render with a background if using the IntelliJ markdown plugin.
    They do render correctly if opened directly in IntelliJ, as well as in a browser

    It's also recommended to install the IntelliJ 'PlantUML' plugin to get a real-time preview whilst updating the diagrams.

[^1]: For more details on the encrypted format, see the [encrypted file store connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-encrypted-file-store-connector){ target=gh }.

--8<-- "snippets/abbr.md"
