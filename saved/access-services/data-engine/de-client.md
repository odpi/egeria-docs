<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project.  -->

# Data Engine Open Metadata Access Service (OMAS) Client

There are different client implementations available:

* `DataEngineRESTClient` - Default client implementation interacting via HTTP transport mechanism and default OCF REST client.
* `DataEngineRESTConfigurationClient` - An extension to the REST interface that can be used as helper to automate configuration of the event based client by retrieving connection details used to build the client topic connector.
* `DataEngineEventClient` - Client implementation interacting via Events transport mechanism. It is using `DataEngineInTopicClientConnector` that produces events to the input topic of Data Engine access service.


HTTP based REST clients can be constructed in following way:

* No authentication embedded in the HTTP request - for test systems.
* Basic authentication using a userId and password embedded in the HTTP request.

Both constructors take the [URL root for the server platform](https://egeria-project.org/concepts/platform-url-root/)
where the Data Engine OMAS is running and its [server name](https://egeria-project.org/concepts/server-name/).

Here is a code example with the user id and password specified:

```java
DataEngineClient client = new DataEngineRESTClient   ("cocoMDS1",
                                           "https://localhost:9444",
                                           "cocoUI",
                                           "cocoUIPassword");

```
This client is set up to call the `cocoMDS1` server running on the `https://localhost:9444`
OMAG Server Platform.  The userId and password is for the application
where the client is running.  The userId of the real end user is passed
on each request.

Similarly, extended REST configuration client can help retrieving additional configuration details from the remote server can be constructed in following way:

```java
DataEngineRESTConfigurationClient client = new DataEngineRESTConfigurationClient("remoteServerName",
                                        "https://localhost:9444",
                                        "remoteUserName",
                                        "remoteUserPassword");
ConnectionResponse connectionResponse = client.getInTopicConnection("remoteServerName","remoteUserName");
```

Event based client can be constructed by injecting instance of the DataEngineInTopicClientConnector.
In the example below we can create the connector with remote configuration retrieved previously and pass it to the event based client:

```java

DataEngineInTopicClientConnector topicConnector = (DataEngineInTopicClientConnector) connectorBroker.getConnector(connectionResponse.getConnection());

DataEngineClient client = new DataEngineEventClient(dataEngineInTopicClientConnector);
```

## Client operations

Once you have an instance of the client, you can use it to create, update or delete the open metadata entities for the ETL jobs.

* [Create External Data Engine](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#createExternalDataEngine(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.Engine))
* [Get external source name](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#getExternalSourceName())
* [Set external source name](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#setExternalSourceName(java.lang.String))
* [Upsert Process](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#createOrUpdateProcess(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.Process))
* [Upsert PortImplementation](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#createOrUpdatePortImplementation(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.PortImplementation,java.lang.String))
* [Upsert Schema Type](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#createOrUpdateSchemaType(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.SchemaType))
* [Upsert Database](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertDatabase(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.Database))
* [Upsert Database Schema](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertDatabaseSchema(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.DatabaseSchema,java.lang.String))
* [Upsert Data File](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertDataFile(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.DataFile))
* [Upsert Event Type](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertEventType(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.EventType,java.lang.String))
* [Upsert Relational Table](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertRelationalTable(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.RelationalTable,java.lang.String))
* [Upsert Topic](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertTopic(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.Topic))
* [Delete Connection](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteConnection(java.lang.String,java.lang.String,java.lang.String))
* [Delete Database](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteDatabase(java.lang.String,java.lang.String,java.lang.String))
* [Delete Database Schema](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteDatabaseSchema(java.lang.String,java.lang.String,java.lang.String))
* [Delete Data File](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteDataFile(java.lang.String,java.lang.String,java.lang.String))
* [Delete Endpoint](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteEndpoint(java.lang.String,java.lang.String,java.lang.String))
* [Delete Event Type](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteEventType(java.lang.String,java.lang.String,java.lang.String))
* [Delete Folder](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteFolder(java.lang.String,java.lang.String,java.lang.String))
* [Delete Port Implementation](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deletePortImplementation(java.lang.String,java.lang.String,java.lang.String))
* [Delete Process](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteProcess(java.lang.String,java.lang.String,java.lang.String))
* [Delete Relational Table](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteRelationalTable(java.lang.String,java.lang.String,java.lang.String))
* [Delete Schema Type](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteSchemaType(java.lang.String,java.lang.String,java.lang.String))
* [Delete Topic](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#deleteTopic(java.lang.String,java.lang.String,java.lang.String))
* [Find an entity](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#find(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.rest.FindRequestBody))
* [Upsert Processing State](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#upsertProcessingState(java.lang.String,java.util.Map))
* [Get Engine's Processing State](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#getProcessingState(java.lang.String))
* [Add data flows](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html)
* [Add process hierarchy](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/dataengine/client/DataEngineClient.html#addProcessHierarchy(java.lang.String,org.odpi.openmetadata.accessservices.dataengine.model.ProcessHierarchy))
