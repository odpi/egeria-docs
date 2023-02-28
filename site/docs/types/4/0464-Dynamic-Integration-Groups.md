<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0464 Integration Groups

The types in this model are used to create [integration group](/concepts/integration-group) definitions.

![UML](0464-Dynamic-Integration-Groups.svg)

## IntegrationGroup entity

An [integration group](/concepts/integration-group) is a [software capability](/types/0/0042-Software-Capabilities) that is able to run specific [integration connectors](/concepts/integration-connector) on demand.

## RegisteredIntegrationConnector relationship

The integration connectors to run in an *integration group* are specified via the *RegisteredIntegrationConnector* relationships.

- `connectorName` sets up the name of the connector. This name is used for routing refresh calls to the connector as well as being used for diagnostics. Ideally it should be unique amongst the connectors for the integration service.
- `connectorUserId` sets up the user id for the connector - if this is null, the integration daemon's userId is used on requests to the Open Metadata Access Service (OMAS).
- `metadataSourceQualifiedName` sets up the qualified name of the metadata source for this integration connector. This is the qualified name of an appropriate software capability element stored in open metadata. This software capability is accessed via the partner OMAS and is used to control the origin information [- known as metadata provenance](/features/metadata-provenance/overview) in any metadata elements created by the integration connector.  The default value is *null*, which means all metadata elements created by the integration connector will have *local cohort* provenance values and can be updated by other process in the open metadata ecosystem.  If it is set up with a valid qualified name, the metadata elements will have external source provenance values and only the integration connector is able to update the values.
- `startDate` sets up a date/time that determines when the integration connector can start running.
- `refreshTimeInterval` sets up the number of minutes between each call to the connector to refresh the metadata. Zero means that refresh is only called at server start up and whenever the refresh REST API request is made to the integration daemon. If the refresh time interval is greater than 0 then additional calls to refresh are added spaced out by the refresh time interval.
- `stopDate` sets up a date/time that determines when the integration connector must stop running.
- `permittedSynchronization` is an optional property that defines the permitted directions of metadata flow between the third party technology and open metadata. If the integration connector attempts to flow metadata in a direction that is not permitted, it receives the `UserNotAuthorizedException`. The default for this value is set up automatically in the integration service's descriptive information so this value only needs to be set if it is necessary to restrict the behavior of the connector. These are the different values for this property and their effect:
    
    - `TO_THIRD_PARTY` - The third party technology is logically downstream of open metadata. This means the open metadata ecosystem is the originator and owner of the metadata being synchronized. Any updates detected in the third technology are overridden by the latest open metadata values.
    - `FROM_THIRD_PARTY` - The third party technology is logically upstream (the originator and owner of the metadata). Any updates made in open metadata are not passed to the third party technology and the third party technology is requested to refresh the open metadata version.
    - `BOTH_DIRECTIONS` - Metadata exchange is permitted in both directions. Synchronization is halted on a specific element if potentially clashing updates have occurred both in the third party technology and open metadata. Such conflicts are logged on the audit log and resolved through manual stewardship.

## IntegrationConnector entity

*[Integration connectors](/concepts/integration-connector)* are specialist [connectors](/concepts/connector).  They are represented in open metadata using the *IntegrationConnector* entity which is a specialization of *[DeployedConnector](/types/2/0215-Software-Components)*.  This entity is linked to a *[Connection](/types/2/0201-Connectors-and-Connections)* entity via a *[ConnectionToAsset](/types/2/0205-Connection-Linkage)* relationship.

An integration connector can be linked to multiple integration groups via the *RegisteredIntegrationConnector* relationship.  It can only be linked to a specific integration group once.  If multiple instances of the same integration connector implementation is to be specified in a group. each one is represented by an *IntegrationConnector* entity linked to its own *Connection* entity that describes its required behaviour.

The `usesBlockingCalls` attribute sets up whether the connector should be started in its own thread to allow it to block on a listening call.

## CatalogTarget

The *CatalogTarget* relationship links an *IntegrationConnector* entity to another entity that the integration connector is to update.  For example, if an integration connector is configured to catalog a database and its [*Database*](/types/2/0224-Databases) entity is already created, the *CatalogTarget* would link the *IntegrationConnector* entity with the *Database* entity.  This prevents the integration connector from recreating the Database entity when it runs.

--8<-- "snippets/abbr.md"