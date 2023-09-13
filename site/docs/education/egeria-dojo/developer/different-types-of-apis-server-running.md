<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Now it is time to start `mds1` and observe the changes to `EgeriaPlatformReport`'s output.  For this final step, we use another utility called `ServerOps` in module `egeria-ops-utility`.  

![egeria-ops-utility module](/education/egeria-dojo/developer/egeria-ops-utility-module.png)

??? beginner "Setting up `ServerOps`"
    As before, navigate to the `ServerOps` class, run it using the right-mouse menu and then, when it fails with the certificate error, add `-Dstrict.ssl=false` to the `VM Options` and re-run `ServerOps` once you have saved the configuration.
    
    ![egeria-ops-utility configuration](/education/egeria-dojo/developer/egeria-ops-utility-configuration.png)
    
    `ServerOps` displays a menu of operations that it can perform.
    
    ```bash
    /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -Dstrict.ssl=false ... org.odpi.openmetadata.devprojects.utilities.serverops.ServerOps
    ===============================
    OMAG Server Operations Utility:    Mon Feb 14 10:39:52 GMT 2022
    ===============================
    Running against platform: https://localhost:9443 - Egeria OMAG Server Platform (version 3.12)
    Using userId: garygeeke
    
    Available servers: [mds1]
    Enter a command {start, stop, exit} along with one or more space separate server names. Press enter to execute request.
    ```

??? beginner "Starting `mds1`"

    Enter `start mds1` and press return. You will see the message `Starting mds1 ...`.  Then one of two things happens ...
    
    1. It completes successfully and you see:
    
    ```bash
    Starting mds1 ...
    Mon Feb 14 10:46:58 GMT 2022 mds1 is running the following services: [Open Metadata Repository Services (OMRS), Connected Asset Services, Asset Consumer OMAS, Community Profile OMAS, Asset Owner OMAS, Data Manager OMAS, Asset Manager OMAS, Governance Program OMAS, Digital Architecture OMAS]
                
    Available servers: [mds1]
    Enter a command {start, stop, exit} along with one or more space separate server names. Press enter to execute request.
    ```
    
    2. It seem to hang after outputting `Starting mds1 ...`.  Switch to the `EgeriaPlatform` tab and you will see many audit log messages from Egeria displayed on the console. At the end is this set of messages which indicates that Apache Kafka is not running.
    
    
    ```bash
    Mon Feb 14 10:43:02 GMT 2022 mds1 Startup OMAG-ADMIN-0202 The Asset Consumer Open Metadata Access Service (OMAS) is supporting the following governance zones: [data-lake, personal-files, personal-files]
    Mon Feb 14 10:43:02 GMT 2022 mds1 Startup OCF-KAFKA-TOPIC-CONNECTOR-0001 Connecting to Apache Kafka Topic egeria.omag.server.mds1.omas.assetconsumer.outTopic with a server identifier of e6afd331-1853-42d0-a816-bb1eeb30c7b8
    Mon Feb 14 10:43:02 GMT 2022 mds1 Startup OCF-KAFKA-TOPIC-CONNECTOR-0015 The local server is attempting to connect to Kafka, attempt 1
    Mon Feb 14 10:44:02 GMT 2022 mds1 Startup OCF-KAFKA-TOPIC-CONNECTOR-0015 The local server is attempting to connect to Kafka, attempt 2
    ```
    
    The server is waiting for Apache Kafka to start.  If this occurs start Apache Kafka (and Apache Zookeeper) ...
    
    ??? tip "Starting Apache Kafka"
        ---8<-- "snippets/tasks/task-starting-kafka.md"
    
    Once Apache Kafka is running, `mds1` completes start-up and `ServerOps` outputs the success message in its *Run* tab as shown in outcome 1.  It is possible, however, that you do not manage to get Kafka running in time and `mds1` fails to start.  If that happens just re-run the `start mds1` command of `ServerOps` once you have Kafka running.  
    
    !!! tip "Restarting servers"
        If you call `start mds1` when `mds1` is already, it has the effect of restarting `mds1`.  This is because the first step in starting a server is to stop the previous instance.  This is useful to know in later exercises when you are creating metadata in `mds1`'s repository.  Since `mds1` is using an in-memory repository, this restart will clear it to empty and you can start again.

??? beginner "Review the expanded information from `EgeriaPlatformReport`"
 
    Now that `mds1` is running, re-run `EgeriaPlatformReport` and you see that information about the server's type along with the operational status of the server and the services have been added.  For example:
    
    ```bash
    Platform servers
          Server: mds1
             Type: Metadata Access Store
             Description: Metadata Access Store called mds1 running on platform https://localhost:9443
             UserId: cocoMDS1npa
             Security Connector
                Implementation: org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaServerSecurityProvider
                Location: <null>
             Local Repository
                Local Repository Mode: Open Metadata Native
                Local Repository Connector
                   Implementation: org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider
                   Location: <null>
                Local Repository Remote Connector
                   Implementation: org.odpi.openmetadata.adapters.repositoryservices.rest.repositoryconnector.OMRSRESTRepositoryConnectorProvider
                   Location: https://localhost:9443/servers/mds1
             Last Start Time: Mon Feb 14 11:31:24 GMT 2022
             Server Active Status: Running
             History
                Start Time: Mon Feb 14 10:43:01 GMT 2022
                End Time: Mon Feb 14 11:31:09 GMT 2022
                Start Time: Mon Feb 14 11:31:09 GMT 2022
                End Time: Mon Feb 14 11:31:24 GMT 2022
             Services
                Service: Asset Manager OMAS
                   Service Status: Running
                   Service Options
                      SupportedZones: [quarantine, trash-can, data-lake]
                      PublishZones: [data-lake, personal-files, personal-files]
                      DefaultZones: [quarantine]
                   Connectors
                      InTopic
                         Implementation: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
                         Location: egeria.omag.server.mds1.omas.assetmanager.inTopic
                         Configuration Properties: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
                      OutTopic
                         Implementation: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
                         Location: egeria.omag.server.mds1.omas.assetmanager.inTopic
                         Configuration Properties: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
                Service: Open Metadata Repository Services (OMRS)
                   Service Status: Running
                Service: Connected Asset Services
                   Service Status: Starting
    ```
    The [markdown version of the report](/education/egeria-dojo/developer/egeria-platform-report-mds1-running){ target=dojo-support } makes it easier to study the new information.
    
    The additional information about the servers is coming from the *Platform Services* 
    
    ```java linenums="1"
        List<String> serverList = platformServicesClient.getKnownServers(clientUserId);
    
        if (serverList != null)
        {
            for (String serverName : serverList)
            {
                if (serverName != null)
                {
                    ServerStatus platformServerStatus = platformServicesClient.getServerStatus(clientUserId, serverName);
                    
                    /*
                     * Add code here
                     */
                }
            }
        }
    
    ```
    The `platformServerStatus` returned from `getServerStatus` includes:
    
    - `serverName` - Name of the server.
    - `isActive` - Boolean flag indicating whether it is active (running) on the server.
    - `serverStartTime` - The most recent date/time that the server started.
    - `serverEndTime` - The most recent date/time that the server stopped.
    - `serverHistory` - The list of start and stop times for the previous restarts of the server.
    
    The *Administration Services* also provide information about the services running within a server.
    
    ```java linenums="1"
    OMAGServerOperationsClient serverOperationsClient = new OMAGServerOperationsClient(clientUserId,
                                                                                       serverName,
                                                                                       platformURLRoot);
    
    ServerServicesStatus adminServerStatus = serverOperationsClient.getServerStatus();
    
    ```
    The `adminServerStatus` returned from `getServerStatus` includes:

    - `serverName` - Name of the server.
    - `serverType` - Derived by the administration services when it starts the server.  It is based on an assessment of the services requested in the configuration document.
    - `serverStartTime` - The most recent date/time that the server started.
    - `serverActiveStatus` - The running status of the server, which is one of 5 values:
        - `Unknown` - The state of the server is unknown.  This is equivalent to a null value.
        - `Starting` - The server is starting.
        - `Running` - The server has completed start up and is running.
        - `Stopping` - The server has received a request to shutdown.
        - `Inactive` - The server is not running.
    - `services` - The list of the services of the server.  For each entry:
        - `serviceName` - the name of the service.
        - `serviceStatus` - the running status of the service, which is one of 5 values:
            - `Unknown` - The state of the service is unknown.  This is equivalent to a null value.
            - `Starting` - The service is starting.
            - `Running` - The service has completed start up and is running.
            - `Stopping` - The service has received a request to shutdown.
            - `Inactive` - The service is not running.
    
 
    
    
    