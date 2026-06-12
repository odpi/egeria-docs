<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Self-registering integration connectors

You may wish to write an integration connector that searches for particular types of metadata elements and registered them as its own catalog targets for ongoing processing.

In this pattern:

* The integration connector inherits from `DynamicIntegrationConnectorBase`.
* The `start()` method is minimal, simply initializing any resources needed to perform the discovery of new metadata elements of interest.
* The discovery logic is implemented in the `refresh()` method.  It compares the existing list of catalog targets with the list of interesting metadata elements retrieved form the metadata repositories.  Any new ones are added as catalog targets.  Any that are no longer of interest are removed.
* The processing logic is implemented in the *Target Processor* class.
* The `disconnect()` method cleans up any resources.

## Integration connector implementation

### Inheritance

The integration connector inherits from [DynamicIntegrationConnectorBase](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/integration/connectors/DynamicIntegrationConnectorBase.html).  This base class manages the lifecycle of the integration connector and calling of the catalog targets.

```java
public class MySelfRegisteringIntegrationConnector extends DynamicIntegrationConnectorBase
{
    
}
```

If the connector will also process events then it should also implement the [OpenMetadataEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/openmetadata/events/OpenMetadataEventListener.html) interface and its `processEvent()` method.  If this interface is implemented, the `DynamicIntegrationConnectorBase` will register and event listener for you.

### Start method

Typically the `start()` method simply outputs an audit log message to indicate that it is starting up.

### Refresh method

The `refresh()` method has three jobs to perform:

* discover if there are new metadata elements of interest
* register any new metadata elements as catalog targets
* refresh all catalog targets

This code snippet shows how to discover the unique identifiers (GUIDs) of elements that are already catalog targets.
```java
try
        {
            Set<String>     = new HashSet<>();

            AssetClient assetClient = integrationContext.getAssetClient();
            int startFrom = 0;

            List<OpenMetadataRootElement> catalogTargetList  = assetClient.getCatalogTargets(integrationContext.getIntegrationConnectorGUID(),
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

            /*
             * Process any new data hubs.
             */
            CollectionClient collectionClient = integrationContext.getCollectionClient(OpenMetadataType.DATA_HUB.typeName);
            startFrom = 0;

            List<OpenMetadataRootElement> dataHubs = collectionClient.findCollections(null,
                                                                                      collectionClient.getSearchOptions(startFrom, integrationContext.getMaxPageSize()));

            while (dataHubs != null)
            {
                for (OpenMetadataRootElement dataHub : dataHubs)
                {
                    if ((dataHub != null) && (! knownCatalogTargets.contains(dataHub.getElementHeader().getGUID())) && (dataHub.getProperties() instanceof DataHubProperties dataHubProperties))
                    {
                        /*
                         * This is a new data hub.  Add it as a catalog target.
                         */
                        CatalogTargetProperties catalogTargetProperties = new CatalogTargetProperties();
                        catalogTargetProperties.setCatalogTargetName(dataHubProperties.getDisplayName() + "(" + dataHub.getElementHeader().getGUID() + ")");
                        assetClient.addCatalogTarget(integrationContext.getIntegrationConnectorGUID(),
                                                     dataHub.getElementHeader().getGUID(),
                                                     assetClient.getMakeAnchorOptions(false),
                                                     catalogTargetProperties);
                    }
                }

                startFrom = startFrom + integrationContext.getMaxPageSize();
                dataHubs  = collectionClient.findCollections(null,
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
It is up to the implementation to determine how to discover the metadata elements of interest.  However using appropriate queries, it should be possible to identify anly elements that are not in 






???+ info "Code Example"
    See the [LiskovDataHubManagerConnector](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/nanny-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/liskov/DataHubManagerConnector.java)



--8<-- "snippets/abbr.md"
