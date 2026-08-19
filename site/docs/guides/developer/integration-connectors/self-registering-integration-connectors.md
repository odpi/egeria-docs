<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Self-registering integration connectors

Normally the [catalog targets](/concepts/catalog-target) for an integration connector are attached by a person, or by a [governance action service](/concepts/governance-action-service), when they decide that a particular resource should be managed by that connector.

Sometimes the connector can work out for itself which elements it should be working with.  For example, a connector that maintains a data dictionary for every data sharing hub should pick up each new data sharing hub as it is created, without anyone having to remember to connect it.

In this pattern:

* The integration connector inherits from `DynamicIntegrationConnectorBase`.
* The `start()` method is minimal, simply initializing any resources needed to perform the discovery of new metadata elements of interest.
* The discovery logic is implemented in the `refresh()` method.  It compares the existing list of catalog targets with the list of interesting metadata elements retrieved from the metadata repositories.  Any new ones are added as catalog targets.  Any that are no longer of interest are removed.
* The processing logic is implemented in the [catalog target processor](/guides/developer/integration-connectors/catalog-targets) class.
* The `disconnect()` method cleans up any resources.

Everything else about the connector is the same as any other [catalog target connector](/guides/developer/integration-connectors/catalog-targets) - the only difference is who creates the *CatalogTarget* relationships.

## Integration connector implementation

### Inheritance

The integration connector inherits from [DynamicIntegrationConnectorBase](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/integration/connectors/DynamicIntegrationConnectorBase.html).  This base class manages the lifecycle of the integration connector and calling of the catalog targets.

```java
public class MySelfRegisteringIntegrationConnector extends DynamicIntegrationConnectorBase
{
    
}
```

If the connector will also process events then it should also implement the [OpenMetadataEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/openmetadata/events/OpenMetadataEventListener.html) interface and its `processEvent()` method.  If this interface is implemented, the `DynamicIntegrationConnectorBase` will register an event listener for you.

### Start method

Typically the `start()` method simply outputs an audit log message to indicate that it is starting up.  Remember to call `super.start()` so that the catalog targets manager is created.

```java
    @Override
    public void start() throws ConnectorCheckedException, UserNotAuthorizedException
    {
        super.start();

        final String methodName = "start";

        auditLog.logMessage(methodName,
                            LiskovAuditCode.STARTING_CONNECTOR.getMessageDefinition(connectorName,
                                                                                    integrationContext.getMetadataAccessServer(),
                                                                                    integrationContext.getMetadataAccessServerPlatformURLRoot()));
    }
```

### Refresh method

The `refresh()` method has three jobs to perform:

* discover if there are new metadata elements of interest
* register any new metadata elements as catalog targets
* refresh all catalog targets - by calling `super.refresh()` at the end

The first step is to build the set of elements that are already catalog targets, so that they are not added twice.  `integrationContext.getIntegrationConnectorGUID()` returns the unique identifier of the *IntegrationConnector* element that describes this running connector, and `AssetClient` provides the methods to query and maintain its catalog targets.

```java
    @Override
    public void refresh() throws ConnectorCheckedException, UserNotAuthorizedException
    {
        final String methodName = "refresh";

        try
        {
            Set<String> knownCatalogTargets = new HashSet<>();

            AssetClient assetClient = integrationContext.getAssetClient();
            int         startFrom   = 0;

            List<OpenMetadataRootElement> catalogTargetList = assetClient.getCatalogTargets(integrationContext.getIntegrationConnectorGUID(),
                                                                                            assetClient.getQueryOptions(startFrom, integrationContext.getMaxPageSize()));

            while (catalogTargetList != null)
            {
                for (OpenMetadataRootElement catalogTarget : catalogTargetList)
                {
                    if (catalogTarget != null)
                    {
                        knownCatalogTargets.add(catalogTarget.getElementHeader().getGUID());
                    }
                }

                startFrom         = startFrom + integrationContext.getMaxPageSize();
                catalogTargetList = assetClient.getCatalogTargets(integrationContext.getIntegrationConnectorGUID(),
                                                                  assetClient.getQueryOptions(startFrom, integrationContext.getMaxPageSize()));
            }
```

The second step retrieves the elements that this connector is interested in, and attaches any that are not already catalog targets.  The query used here determines what the connector picks up; this example uses the [collection client](/guides/developer/integration-connectors/integration-context/#the-open-metadata-clients) restricted to the `DataSharingHub` type, but any of the context's clients can be used, and a search string, classification or governance zone filter can narrow it further.

```java
            /*
             * Process any new data sharing hubs.
             */
            CollectionClient collectionClient = integrationContext.getCollectionClient(OpenMetadataType.DATA_SHARING_HUB.typeName);
            startFrom = 0;

            List<OpenMetadataRootElement> dataSharingHubs = collectionClient.findCollections(null,
                                                                                             collectionClient.getSearchOptions(startFrom, integrationContext.getMaxPageSize()));

            while (dataSharingHubs != null)
            {
                for (OpenMetadataRootElement dataSharingHub : dataSharingHubs)
                {
                    if ((dataSharingHub != null) &&
                        (! knownCatalogTargets.contains(dataSharingHub.getElementHeader().getGUID())) &&
                        (dataSharingHub.getProperties() instanceof DataSharingHubProperties dataSharingHubProperties))
                    {
                        /*
                         * This is a new data sharing hub.  Add it as a catalog target.
                         */
                        auditLog.logMessage(methodName,
                                            LiskovAuditCode.NEW_DATA_HUB.getMessageDefinition(connectorName,
                                                                                              dataSharingHubProperties.getDisplayName(),
                                                                                              dataSharingHub.getElementHeader().getGUID()));

                        CatalogTargetProperties catalogTargetProperties = new CatalogTargetProperties();

                        catalogTargetProperties.setCatalogTargetName(dataSharingHubProperties.getDisplayName() + "(" + dataSharingHub.getElementHeader().getGUID() + ")");

                        assetClient.addCatalogTarget(integrationContext.getIntegrationConnectorGUID(),
                                                     dataSharingHub.getElementHeader().getGUID(),
                                                     assetClient.getMakeAnchorOptions(false),
                                                     catalogTargetProperties);
                    }
                }

                startFrom       = startFrom + integrationContext.getMaxPageSize();
                dataSharingHubs = collectionClient.findCollections(null,
                                                                   collectionClient.getSearchOptions(startFrom, integrationContext.getMaxPageSize()));
            }
        }
        catch (Exception error)
        {
            auditLog.logMessage(methodName,
                                LiskovAuditCode.UNEXPECTED_EXCEPTION.getMessageDefinition(connectorName,
                                                                                          error.getClass().getName(),
                                                                                          methodName,
                                                                                          error.getMessage()));
        }

        super.refresh();
    }
```

The final call to `super.refresh()` is what causes `DynamicIntegrationConnectorBase` to pick up the catalog targets - including the ones just added - create a processor for each new one, and call `refresh()` on all of them.

It is up to the implementation to determine how to discover the metadata elements of interest.  However, using appropriate queries, it should be possible to identify any elements that are not yet catalog targets.  The `CatalogTargetProperties` you supply behave exactly as they would if a person had attached the target, so the connector can set the catalog target name, configuration properties, templates, metadata source name and permitted synchronization for each element it discovers.

!!! tip "Give each catalog target a meaningful name"
    The `catalogTargetName` appears in the audit log messages produced as each target is refreshed.  Including the element's display name, as this example does, makes those messages much easier for an operator to follow.

### Removing catalog targets

Elements that are no longer of interest should be removed so that the connector stops working on them:

```java
            assetClient.removeCatalogTarget(integrationContext.getIntegrationConnectorGUID(),
                                            elementGUID,
                                            assetClient.getDeleteOptions(false));
```

The framework detects the removal on the next refresh, disconnects the resource connector for that target and calls `disconnect()` on its catalog target processor.

Be careful to only remove the catalog targets that this connector created.  If people are also allowed to attach targets by hand, an over-eager clean-up will silently undo their work.

### Disconnect method

The `disconnect()` method logs a shutdown message and calls `super.disconnect()` to release the resource connectors held by the catalog targets.

```java
    @Override
    public void disconnect() throws ConnectorCheckedException
    {
        final String methodName = "disconnect";

        auditLog.logMessage(methodName,
                            LiskovAuditCode.CONNECTOR_STOPPING.getMessageDefinition(connectorName,
                                                                                    integrationContext.getMetadataAccessServer(),
                                                                                    integrationContext.getMetadataAccessServerPlatformURLRoot()));

        super.disconnect();
    }
```

Note that this does *not* remove the catalog targets from open metadata.  They are part of the connector's configuration and should survive a restart.

???+ info "Code Example"
    See the [Data Sharing Hub Manager Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/nanny-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/liskov/DataSharingHubManagerConnector.java){ target=gh } and its [target processor :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/nanny-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/liskov/DataSharingHubManagerTargetProcessor.java){ target=gh }.

??? education "Further information"
    - [Supporting catalog targets](/guides/developer/integration-connectors/catalog-targets)
    - [The integration context](/guides/developer/integration-connectors/integration-context)
    - [Catalog target](/concepts/catalog-target) concept page

--8<-- "snippets/abbr.md"
