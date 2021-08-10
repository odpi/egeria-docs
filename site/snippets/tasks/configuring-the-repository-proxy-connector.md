<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the repository proxy connector

The mapping between a third party metadata repository and the open metadata protocols
in a [repository proxy](/egeria-docs/concepts/repository-proxy) is implemented in two connectors:

- An [OMRS repository connector](/egeria-docs/connectors/repository-connector)
- An [OMRS event mapper connector](/egeria-docs/connectors/event-mapper-connector)

They are configured as follows.

### Configure the repository connector

The OMAG server can act as a proxy to a vendor's repository.
This is done by adding the connection
for the repository proxy as the local repository.

!!! post "POST - configure the repository connector"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/repository-proxy/connection
    ```

    The request body should be the connection option to use for configuring the connector,
    which can include any connector-specific options as well as general details like the endpoint
    and credentials for the third party repository.

??? example "Example: connection to configure the IBM Information Governance Catalog repository connector"
    ```json linenums="1" hl_lines="5 9 12 13"
    {
      "class": "Connection",
      "connectorType": {
        "class": "ConnectorType",
        "connectorProviderClassName": "org.odpi.egeria.connectors.ibm.igc.repositoryconnector.IGCOMRSRepositoryConnectorProvider"
      },
      "endpoint": {
        "class": "Endpoint",
        "address": "infosvr:9446",
        "protocol":"https"
      },
      "userId": "a-user",
      "clearPassword": "a-password",
      "configurationProperties": {
        "defaultZones": ["default"]
      }
    }
    ```

    In this example, the type of connector to configure is given by the class name on line 5,
    and details about how to connect to the third party repository (IBM Information Governance Catalog)
    itself are provided on lines 9 (hostname and port), and 12-13 (credentials).

### Configure the repository's event mapper

Any open metadata repository that supports its own API may also implement an
event mapper to ensure the
[Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) is notified when
metadata is added to the repository without going through the open metadata APIs.

The event mapper is a connector that listens for proprietary events
from the repository and converts them into calls to the OMRS.
The OMRS then distributes this new metadata.

!!! post "POST - configure event mapper"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/event-mapper-details?connectorProvider={{fullyQualifiedJavaClassName}}&eventSource={{resourceName}}
    ```

    The `connectorProvider` should be set to the fully-qualified Java class name for the [connector provider](/egeria-docs/concepts/connector-provider),
    and the `eventSource` should give the details for how to access the events (for example, the hostname and port number
    of an Apache Kafka bootstrap server).
