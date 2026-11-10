<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Writing a REST Client Connector

Egeria's Java clients call the REST APIs of the OMAG Servers through a small, stable interface rather than coding directly against a particular HTTP library.  The HTTP work is done by a [REST client connector](/concepts/rest-client-connector).  This means the HTTP transport used across Egeria can be changed without touching the calling code.

The definition of the connector interface for these connectors is
defined in the [rest-client-connectors-api :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/rest-client-connectors-api){ target=gh } module in the
[org.odpi.openmetadata.adapters.connectors.restclients :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/rest-client-connectors-api/src/main/java/org/odpi/openmetadata/adapters/connectors/restclients){ target=gh } Java package.  This module has no dependency on any particular HTTP library.  It contains:

* `RESTClientCalls` - the interface used by the callers.  It has generic methods for each HTTP method: `callGetRESTCall`, `callGetRESTCallNoParams`, `callPostRESTCall`, `callPostRESTCallNoParams`, `callPutRESTCall`, `callPutRESTCallNoParams`, `callDeleteRESTCall`, `callDeleteRESTCallNoParams` and `callPatchRESTCall`.  Each takes the calling method's name, the class of the expected response, a URL template with `{0}`, `{1}`, ... placeholders, (where appropriate) a request body, and the values to insert into the placeholders.
* `RESTClientConnector` - the abstract base class that every implementation extends.  It extends `ConnectorBase` and implements `RESTClientCalls`, `SecureConnectorExtension` and `AuditLoggingComponent`.  It defines the `requestTimeoutSeconds` configuration property (`REQUEST_TIMEOUT_PROPERTY`) that sets how long a call may wait for its response; the `egeria.rest.client.request.timeout.seconds` JVM system property sets the same limit for every connector that does not set it in its connection.  The default is 30 minutes.
* `RESTClientConnectorProvider` - the base class for the connector provider.  It extends `OpenConnectorProviderBase`.

## Implementations

The implementations are in the [rest-client-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors){ target=gh } module:

* [jdk-rest-client-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/jdk-rest-client-connector){ target=gh } - `JDKRESTClientConnector`, the implementation used by default.  It is built on the JDK's own `java.net.http.HttpClient`, so it adds no third-party HTTP dependency, and it supports every HTTP method that Egeria needs, including PATCH.
* [spring-rest-client-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/spring-rest-client-connector){ target=gh } - `SpringRESTClientConnector`, the original implementation built on Spring's `RestTemplate`.  It is no longer the default, but is kept for those who prefer to use Spring.

The choice of implementation is made in `RESTClientFactory` in the [rest-client-factory :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/rest-client-factory){ target=gh } module.  It builds the connection for the connector - currently with the connector type for `JDKRESTClientConnectorProvider` - and returns the connector through `getClientConnector()`.  To use a different implementation, `RESTClientFactory` must be changed to name its connector provider.

---8<-- "snippets/abbr.md"
