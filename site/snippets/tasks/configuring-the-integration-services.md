<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the integration services

The [integration services](/egeria-docs/services/omis) (or Open Metadata Integration Services (OMIS) to give them
their full name) run in an [integration daemon](/egeria-docs/concepts/integration-daemon).

Each integration service hosts one or more [integration connectors](/egeria-docs/connectors/integration-connector).
An integration connector is responsible for the exchange of metadata with a specific deployment of a third party technology.
For example, the [database integrator](/egeria-docs/services/omis/database-integrator) integration service
supports integration connectors that work with relational databases (RDBMS).
A deployment of this integration service in an integration daemon may host, say,
two integration connectors each loading metadata from their own relational database server.

![The configuration document contents for an integration service](integration-service-config.png)

The descriptive information and operational status are filled out automatically by the
administration services based on the `integrationServiceURLMarker` value that you supply.
The other values are supplied on the configuration call.

### List integration services

It is possible to get a description of each of the registered integration services using the following command:

!!! get "GET - list integration services"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/server-platform/registered-services/integration-services
    ```

    Note the `integrationServiceURLMarker` for the integration service that you want to configure.

### Configure an integration service

Each integration service is configured with the network location of the
[metadata access point](/egeria-docs/concepts/metadata-access-point) /
[metadata server](/egeria-docs/concepts/metadata-server)
running the appropriate [OMAS](/egeria-docs/services/omas).
There are a set of options that the integration service supports
along with the list of configuration properties for the integration connectors that will be run in the
integration service.
The integration connector's configuration properties defines which connector implementation
to use and how it should be operated.

!!! post "POST - configure an integration service"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/integration-services/{{integrationServiceURLMarker}}
    ```

    With a request body like the following:

    ```json
    {
      "class": "IntegrationServiceRequestBody",
      "omagserverPlatformRootURL": "{MDServerURLRoot}",
      "omagserverName": "{MDServerName}",
      "integrationConnectorConfigs":
      [ 
        {
          "class": "IntegrationConnectorConfig",
          "connectorName": " ... ",             
          "connectorUserId": " ... ",           
          "connection":
          { 
            "class": "Connection",
            "connectorType":
            {
              "class": "ConnectorType",
              "connectorProviderClassName": "{connector provider class name}"
            },
            "endpoint":
            {
              "class": "Endpoint",
              "address" : "..."
            }
          },               
          "metadataSourceQualifiedName": " ... ",
          "refreshTimeInterval": "60", 
          "usesBlockingCalls": "false",
          "permittedSynchronization": " ... "
        }
      ]      
    }
    ```

Detailed description of the properties:

- `connectorName` sets up the name of the connector. This name is used for routing refresh calls to the connector as well        
  as being used for diagnostics. Ideally it should be unique amongst the connectors for the integration service.
- `connectorUserId` sets up the user id for the connector - if this is null, the integration daemon's userId is used
  on requests to the Open Metadata Access Service (OMAS). 
- `connection` sets up the connection for the integration connector.              
- `metadataSourceQualifiedName` sets up the qualified name of the metadata source for this integration connector. This
  is the qualified name of an appropriate software server capability stored in open metadata. This software server
  capability is accessed via the partner OMAS.
- `refreshTimeInterval` sets up the number of minutes between each call to the connector to refresh the metadata. Zero means that refresh
  is only called at server start up and whenever the refresh REST API request is made to the integration daemon.
  If the refresh time interval is greater than 0 then additional calls to refresh are added spaced out by the refresh time interval.
- `usesBlockingCalls` sets up whether the connector should be started in its own thread to allow it to block on a listening call.
- `permittedSynchronization` is an optional property that defines the permitted directions of metadata flow
  between the third party technology and open metadata. If the integration connector
  attempts to flow metadata in a direction that is not permitted, it receives the `UserNotAuthorizedException`.
  The default for this value is set up automatically in the integration service's descriptive information so this
  value only needs to be set if it is necessary to restrict the behavior of the
  connector. These are the different values for this property and their effect:
    - `TO_THIRD_PARTY` - The third party technology is logically downstream of open metadata. This means the open metadata
      ecosystem is the originator and owner of the metadata being synchronized. Any updates detected
      in the third technology are overridden by the latest open metadata values.
    - `FROM_THIRD_PARTY` - The third party technology is logically upstream (the originator and owner of the metadata).
      Any updates made in open metadata are not passed to the third party technology and the
      third party technology is requested to refresh the open metadata version.
    - `BOTH_DIRECTIONS` - Metadata exchange is permitted in both directions. Synchronization is halted on a specific
      element if potentially clashing updates have occurred both in the third party technology and
      open metadata. Such conflicts are logged on the audit log and resolved through manual stewardship.
