<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Egeria Dojo - Developer Day

Egeria has an extensive set of APIs and asynchronous event interactions for retrieving and maintaining metadata.    It is also possible to write connectors that execute in Egeria's runtime and either:

- Provide Egeria access to third party technology and resources.
- Provide the mechanism to synchronize metadata between a third party technology and the open metadata ecosystem that Egeria orchestrates.

Connectors can also be called in your applications to access third party technology along with its associated metadata.

Finally, Egeria's open metadata archives have a wide set of uses in distributing standard definitions and types.

After completing developer day of the egeria dojo you should feel comfortable with calling Egeria's APIs, writing connectors and working with open metadata archives.

--8<-- "docs/education/egeria-dojo/ski-run-colours.md"

## Preparing your machine for the Dojo

!!! tip "In preparation ..."
    Egeria's interfaces are written in Java.  It is expected that you have basic Java skills and have the Java 11 SDK installed on your machine.
    
    ??? tip "Installing Java ..."
        --8<-- "docs/education/tutorials/building-egeria-tutorial/task-installing-java.md"

    You will need to build Egeria's source which needs Apache Maven installed.
    
    ??? tip "Installing Apache Maven ..."
        --8<-- "docs/education/tutorials/building-egeria-tutorial/task-installing-maven.md"

    During the dojo you will running Apache Kafka to experiment with event notifications.
    
    ??? tip "Installing Apache Kafka ..."
        --8<-- "docs/education/tutorials/kafka-tutorial/task-installing-kafka.md"

    The dojo makes use of egeria libraries and code samples in the following git repositories and you will needd a clone of them on your machine.
    
    - https://github.com/odpi/egeria
    - https://github.com/odpi/egeria-samples
    - https://github.com/odpi/egeria-dev-projects
    
    ??? tip "Downloading (cloning) Egeria's git repositories ..."
        --8<-- "docs/education/tutorials/git-and-git-hub-tutorial/task-downloading-egeria-source.md"

    Many of the contributors to the Egeria project use the *[IntelliJ IDEA](https://www.jetbrains.com/idea/)* IDE.  Jetbrains offers a [free community edition of IntelliJ](https://www.jetbrains.com/idea/download/) which is sufficient to work with Egeria.  You are free to use any IDE during the dojo, however the instructions will focus on IntelliJ IDEA.

    ??? tip "Installing IntelliJ IDEA ..."
        --8<-- "docs/education/tutorials/intellij-tutorial/task-installing-intellij.md"
      
    Congratulations, you are ready to begin.

## Dojo Activities

???+ education "Developer Dojo starts here"

    ??? beginner "Developer choices when customizing Egeria (15 mins reading)"
        --8<-- "docs/guides/developer/developer-choices.md"
        
        In this dojo, you will have an opportunity to build and run Java utilities and connectors.  However before you get to the coding, you will spend some time setting up your development and test environment.
        
    ??? beginner "Setting up your IDE to use Egeria (30 mins)"
        
        You need to bring the main `egeria.git` code into IntelliJ to build its platform and clients.
        
        ??? beginner "Building Egeria's core libraries (15 mins)"
            --8<-- "docs/education/tutorials/intellij-tutorial/task-loading-egeria-into-intellij.md"
            
            Now build the egeria.git repository.  For the Dojo, it is OK to use the *Quick Build* option when offered.
            
            --8<-- "docs/education/tutorials/intellij-tutorial/intellij-building-egeria-git.md"
        
        Once Egeria's core libraries are built, it is helpful to install Egeria in a directory that is easy to find
        
        ??? beginner "Installing Egeria's core libraries (15 mins)"
            ### Installing Egeria
            --8<-- "docs/education/tutorials/intellij-tutorial/intellij-open-terminal.md"
            --8<-- "docs/education/tutorials/building-egeria-tutorial/terminal-installing-egeria.md"

    ??? beginner "Setting up your Test environment (30 mins)"
    
        The `egeria-dev-projects.git` repository contains the utilities to support your Egeria test environment. This was one of the git repositories that you cloned in the prerequisite tasks.  Open this git repository in IntelliJ.
        
        ??? tip "Opening egeria-dev-projects.git in IntelliJ IDEA ..."
            Use **File**->**Open...** and select the top-level `egeria-dev-projects` directory that was downloaded from GitHub in the file selection window. Click the **Open** button.

        Now build the `egeria-dev-projects` code ...
        
        ??? beginner "Building egeria-dev-projects.git in IntelliJ IDEA ..."
            --8<-- "docs/education/tutorials/intellij-tutorial/intellij-building-egeria-dev-projects-git.md"

        Egeria's services run in the [OMAG Server Platform](/concepts/omag-server-platform).  The jar file for the OMAG Server Platform was built by the `egeria.git` build.  It is located in the `server` directory of your Egeria install and is called `server-chassis-spring-{{release}}.jar`.  You will need an easy way to start and stop the OMAG Server Platform.   This is done with an IntelliJ *Configuration*.
        
        ??? beginner "Set up IntelliJ to run the OMAG Server Platform ..."
            ### Creating a configuration for OMAG Server Platform
            From your `egeria-dev-projects` IntelliJ window, look for a box called `Add Configuration...`
            ![Add Configuration](/education/egeria-dojo/developer/intellij-add-configuration.png)
            Click on it and a wizard window opens. Open the list of *Templates* on the left hand column.
            ![Configuration Templates](/education/egeria-dojo/developer/intellij-configuration-templates.png)
            Scroll down to *Jar Application* template and select it.  A form appears on the right-hand side.
            ![Jar Application Template](/education/egeria-dojo/developer/intellij-jar-application-template.png)
            Enter:
            
            * `EgeriaPlatform` at the top under `Name:`
            * `Path to Jar` is set to the directory where the OMAG Server Platform jar is located
            * `VM Options` is set to `-Dstrict.ssl=false -Dloader.path=server/lib -Dserver.port=9443`.  This turns of SSL checking, points to the `lib` directory where you will be adding your new connector jar files and requests that the OMAG Server listents on port `9443`.
            * `Working Directory` is set to the parent directory above the directory with the OMAG Server Platform jar.  This directory includes the `truststore.p12` certificate file needed for the platform to start successfully.
            
            The example below is from a machine where the directory used to install Egeria was `/Users/mandy-chessell/egeria-install`. Notice the directory name needs to be specified in full, - the `~` notation does not work here. In this example, the Egeria release used was `3.6-SNAPSHOT`.
            ![OMAG Server Platform Configuration](/education/egeria-dojo/developer/intellij-omag-server-platform-configuration.png)

            Once you have entered these values, click `OK`.  The `Add Configurations ...` box has been replaced by a drop-down menu that includes your new configuration called `EgeriaPlatform` is in the configurations box.
            
            ![EgeriaPlatform in configurations menu](/education/egeria-dojo/developer/intellij-egeria-platform-in-menu.png)
            
            If you click on the down arrow next to `EgeriaPlatform` you will see `Add Configurations ...` has been replaced by `Edit configurations...`.  You will use this option later to add configurations for other utilities as the dojo progresses.

            ![Edit configurations](/education/egeria-dojo/developer/intellij-edit-configurations.png)

            With `EgeriaPlatform` showing in the configurations box, click the green triangle and a *Run* tab opens showing the platform is starting up.  The first line of the output is the call used to start the platform.  You should be able to see the options that you added to the `EgeriaPlatform` configuration.  After the command is the console output of the OMAG Server Platform. When you see the `OMAG server platform ready for more configuration` message, it is ready for work.
            
            ```bash
            /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -Dstrict.ssl=false -Dloader.path=server/lib -Dserver.port=9443 -Dfile.encoding=UTF-8 -jar /Users/mandy-chessell/egeria-install/egeria-omag-3.6-SNAPSHOT/server/server-chassis-spring-3.6-SNAPSHOT.jar
             Project Egeria - Open Metadata and Governance
                ____   __  ___ ___    ______   _____                                 ____   _         _     ___
               / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
              / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
             / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
             \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/
            
             :: Powered by Spring Boot (v2.6.3) ::
            
            2022-02-14 07:52:43.693  INFO 85347 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Starting OMAGServerPlatform using Java 11.0.12 on Amandas-MacBook-Pro.local with PID 85347 (/Users/mandy-chessell/egeria-install/egeria-omag-3.6-SNAPSHOT/server/server-chassis-spring-3.6-SNAPSHOT.jar started by mandy-chessell in /Users/mandy-chessell/egeria-install/egeria-omag-3.6-SNAPSHOT)
            2022-02-14 07:52:43.696  INFO 85347 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : No active profile set, falling back to default profiles: default
            2022-02-14 07:52:46.583  INFO 85347 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9443 (https)
            2022-02-14 07:52:47.741  WARN 85347 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : strict.ssl is set to false! Invalid certificates will be accepted for connection!
            2022-02-14 07:52:50.421  INFO 85347 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 9443 (https) with context path ''
            2022-02-14 07:52:50.436  INFO 85347 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Started OMAGServerPlatform in 7.476 seconds (JVM running for 8.348)
            Mon Feb 14 07:52:50 GMT 2022 No OMAG servers listed in startup configuration
            Mon Feb 14 07:52:50 GMT 2022 OMAG server platform ready for more configuration
            ```

            The *Run* tab where the OMAG Server Platform is running includes a control panel that allows you to start, restart, stop and control the scrolling of output of the program that is running.  If you hover your mouse over the controls, the hover-text indicates what it does.  
            
            ![Run tab control panel](/education/egeria-dojo/developer/intellij-run-tab-control-panel.png)
            
            Feel free to experiment with the control - but be sure that the OMAG Server Platform is running when you finish as it is needed for the next step.
            
    ??? beginner "Calling Egeria's APIs (2.5 hours)"
        ??? beginner "Different types of APIs and their uses (30 mins)"
            Egeria's APIs can be broken down into three main categrories:
            
            - APIs to configure Egeria
            - APIs to operate Egeria
            - APIs to work with open metadata and governance
            
            It is useful to see them running to appreciate the differences between them.
            
            In `egeria-dev-projects`, there is a module called `egeria-platform-report`.  This contains a utility that reports on the status of a running OMAG Server Platform.  Navigate down the contents of `egeria-platform-report` until you come across a java class called `EgeriaPlatformReport`.
            
            ![egeria-platform-report](/education/egeria-dojo/developer/egeria-platform-report-module.png)
            
            Select `EgeriaPlatformReport` and then `Run 'EgeriaPlatformReport...main()'` from the right-mouse menu.
            
            A new *Run* tab appears next to `EgeriaPlatform` and `EgeriaPlatformReport` runs but fails:
            
            ```bash
            /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java ... org.odpi.openmetadata.devprojects.reports.platform.EgeriaPlatformReport
            ===============================
            OMAG Server Platform Report:    Sun Feb 13 22:13:33 GMT 2022
            ===============================
            Running against platform: https://localhost:9443
            Using userId: garygeeke
            
            Platform report for: https://localhost:9443
               Platform deployment
            There was an org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException exception when calling the platform.  Error message is: OMAG-COMMON-503-001 A client-side exception was received from API call getPlatformOrigin to OMAG Server EgeriaPlatform at https://localhost:9443.  The error message was CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.ResourceAccessException was received by method getPlatformOrigin from API call https://localhost:9443/open-metadata/platform-services/users/{1}/server-platform/origin to server EgeriaPlatform on platform https://localhost:9443.  The error message was I/O error on GET request for "https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platform/origin": PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target; nested exception is javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
            
            Process finished with exit code 255

            ```
            This is because it does not have a valid security certification.  You will notice that IntelliJ has added a new configuration for `EgeriaPlatformReport'
            
            ![egeria-platform-report configuration](/education/egeria-dojo/developer/egeria-platform-report-configuration.png)
           
            Click on the white down arrow of the configurations box and select `Edit Configurations...`.  Select the configuration for `EgeriaPlatformReport` to show its configuration form.
           
            Add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration.  This turns off the need for a certificate. 
            
            ![egeria-platform-report configuration fixed](/education/egeria-dojo/developer/egeria-platform-report-configuration-fixed.png)
            
            Re-run `EgeriaPlatformReport` by clicking on the green arrow on the *Run* tab.  There is more output this time even though it still seems to fail in the end. It begins with the report header that records the platform it is running against.
            
            ```bash
            ===============================
            OMAG Server Platform Report:    Mon Feb 14 07:57:05 GMT 2022
            ===============================
            Running against platform: https://localhost:9443
            Using userId: garygeeke
            
            Platform report for: https://localhost:9443
            ```
            
            Then `EgeriaPlatfromReport` starts to call the Egeria APIs that are used for configuring and managing the OMAG Server Platform.
            
            ```bash
               Platform deployment
                  Egeria version: Egeria OMAG Server Platform (version 3.6-SNAPSHOT)
                  Configuration document store connector: <null>
                  Platform security connector: <null>
            ```
            
            The `Egeria version` is retrieved using the `getPlatformOrigin` method of the [Platform Operations Services](/services/platform-services/overview/).
            
            ```java linenums="1"
            PlatformServicesClient platformServicesClient = new PlatformServicesClient("MyPlatform", platformURLRoot);
                 
            String platformOrigin = platformServicesClient.getPlatformOrigin(clientUserId);
            ```
            The connectors configured for the platform are retreived using the [Administration Service's `OMAGServerPlatformConfiguratinClient`](/services/admin-services/overview/#configuring-the-omag-server-platform)
            
            ```java linenums="1"
 
            OMAGServerPlatformConfigurationClient platformConfigurationClient = new OMAGServerPlatformConfigurationClient(clientUserId, platformURLRoot);
            
            Connection configurationStoreConnection = platformConfigurationClient.getConfigurationStoreConnection();
            Connection platformSecurityConnection   = platformConfigurationClient.getPlatformSecurityConnection();
            ```

            Next is the list of *Registered services*.  These are optional services that can be plugged into the `OMAG Server Platform` and provide the services to retrieve and maintain/govern open metadata. The list that you see is the default set of services installed with the platform.  
            ```bash      
               Registered services
                  Data Manager OMAS: Capture changes to the data stores and data set managed by a data manager such as a database server, content manager or file system.
                  Subject Area OMAS: Document knowledge about a subject area
                  Design Model OMAS: Exchange design model content with tools and standard packages
                  Glossary View OMAS: Support glossary terms visualization
                  Asset Manager OMAS: Manage metadata from a third party asset manager
                  Security Officer OMAS: Set up rules and security tags to protect data
                  IT Infrastructure OMAS: Manage information about the deployed IT infrastructure
                  Data Science OMAS: Create and manage data science definitions and models
                  Community Profile OMAS: Define personal profile and collaborate
                  Discovery Engine OMAS: Support for automated metadata discovery engines
                  Data Engine OMAS: Exchange process models and lineage with a data engine
                  Digital Architecture OMAS: Design of the digital services for an organization
                  Asset Owner OMAS: Manage an asset
                  Stewardship Action OMAS: Manage exceptions and actions from open governance
                  Governance Program OMAS: Manage the governance program
                  Digital Service OMAS: Manage a digital service's lifecycle
                  Asset Lineage OMAS: Store asset lineage
                  Analytics Modeling OMAS: Provides metadata information for Analytics Modeling.
                  Asset Consumer OMAS: Access assets through connectors
                  Asset Catalog OMAS: Search and understand your assets
                  DevOps OMAS: Manage a DevOps pipeline
                  Software Developer OMAS: Interact with software development tools
                  Project Management OMAS: Manage governance related projects
                  Governance Engine OMAS: Set up an operational governance engine
                  Data Privacy OMAS: Manage governance of privacy
                  Security Manager OMAS: Manages exchange of metadata with a security service
                  Archive Manager OMES: Maintains open metadata archives based on the activity in the connected cohorts.
                  Governance Action OMES: Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.
                  Asset Analysis OMES: Analyses the content of an asset's real world counterpart, generates annotations in an open discovery report that is attached to the asset in the open metadata repositories.
                  Files Integrator OMIS: Extract metadata about files stored in a file system or file manager.
                  Topic Integrator OMIS: Exchange metadata with third party event-based brokers.
                  API Integrator OMIS: Exchange metadata with third party API Gateways.
                  Security Integrator OMIS: Distribute security properties to security enforcement points.
                  Search Integrator OMIS: Store metadata with a third party technology that is focused on search efficiency.
                  Database Integrator OMIS: Extract metadata such as schema, tables and columns from database managers.
                  Lineage Integrator OMIS: Manage capture of lineage from a third party tool.
                  Catalog Integrator OMIS: Exchange metadata with third party data catalogs.
                  Analytics Integrator OMIS: Exchange metadata with third party analytics tools.
                  Display Integrator OMIS: Exchange metadata with applications that display data to users.
                  Organization Integrator OMIS: Load information about the teams and people in an organization and return collaboration activity.
                  Glossary Author OMVS: View Service for glossary authoring.
                  Dynamic Infrastructure and Operations OMVS: Explore and operate an open metadata ecosystem.
                  Repository Explorer OMVS: Explore open metadata instances.
                  Type Explorer OMVS: Explore the open metadata types in a repository or cohort.
                  Server Author OMVS: Author servers.
            ```
            The registered are also retrieved through the [Platform Operations Services](/services/platform-services/overview/) using the `getXXXServices` method as follows:
            
            ```java linenums="1"
            List<RegisteredOMAGService> registeredOMASs = platformServicesClient.getAccessServices(clientUserId);
            List<RegisteredOMAGService> registeredOMESs = platformServicesClient.getEngineServices(clientUserId);
            List<RegisteredOMAGService> registeredOMISs = platformServicesClient.getIntegrationServices(clientUserId);
            List<RegisteredOMAGService> registeredOMVSs = platformServicesClient.getViewServices(clientUserId);
            ```
           
            Finally, `EgeriaPlatformReport` calls the [Adminstration Services](/services/admin-services/overview) to request the list of configured servers.  At this stage, there are none.  In fact, the directory where they are kept has not even been created which is why an exception occurs.  It is printed out to show which directory (`data/servers`), relative to the working directory set up in the `EgeriaPlatform` configuration (`~/egeria-install/egeria-omag*`).
            ```bash      
               Platform servers
            There was an org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException exception when calling the platform.  Error message is: OMAG-ADMIN-500-002 Method retrieveAllServerConfigs returned an unexpected exception of org.odpi.openmetadata.frameworks.connectors.ffdc.OCFRuntimeException with message ENCRYPTED-DOC-STORE-400-014  Unable to retrieve the encrypted configuration files; exception was java.nio.file.NoSuchFileException with message data/servers, while attempting access file data/servers/null/config/null.config
            
            Process finished with exit code 255
            ```
            The next step will create a server configuration document that will also create the configuration directory and resolve this issue.  `EgeriaPlatformReport` also creates a [markdown](/guides/contributor/markdown) document called `egeria-platform-report.md` that contains its output.  This [version of egeria-platform-report.md](/education/egeria-dojo/developer/egeria-platform-report-no-servers) is included for your reference.
            
            Servers are configured through the [Administration Services](/services/admin-services/overview/#configure-an-omag-server).  It involves a sequence of calls that sets up its name and properties, the registered services that it will run along with the connectors that it will host.
            
            In `egeria-dev-projects` is a module called `egeria-config-utility`.  It contains a utility called `ServerConfig` that includes the method calls to create different types of servers, to make changes to a server's configuration and to delete a server's configuration. Navigate to the `ServerConfig` class and run it using the right-mouse menu as before.
            
            ![egeria-config-utility module](/education/egeria-dojo/developer/egeria-config-utility-module.png)

            It will also fail with the certificate error.  Edit `ServerConfig`'s newly created configuration and add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration to turn off the need for a certificate. 
            
            ![egeria-config-utility configuration](/education/egeria-dojo/developer/egeria-config-utility-configuration.png)
                       
            When you restart `ServerConfig`, it displays a menu:
            
            ```bash
            /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -Dstrict.ssl=false ... org.odpi.openmetadata.devprojects.utilities.serverconfig.ServerConfig
            ===============================
            OMAG Server Operations Utility:    Mon Feb 14 09:33:07 GMT 2022
            ===============================
            Running against platform: https://localhost:9443 - Egeria OMAG Server Platform (version 3.6-SNAPSHOT)
            Using userId: garygeeke
            
            Enter a command along with the server name and any optional parameters. Press enter to execute request.
              - create-metadata-store     <serverName>  
              - create-integration-daemon <serverName> <metadataStoreServerName> 
              - add-topic-connector       <serverName> <optionalConnectorProviderClassName> 
              - log-event-contents        <serverName> <optionalConnectorProviderClassName> 
              - add-cohort-member         <serverName> <optionalCohortName> 
              - delete-server             <serverName>  
              - exit  
            ```
            Enter `create-metadata-store mds1` in the space under the menu and press return. You should see a message `Configuring metadata store: mds1` and the menu is redisplayed.
            
            ![egeria-config-utility creating mds1](/education/egeria-dojo/developer/egeria-config-utility-creating-mds1.png)

            Rerun `EgeriaPlatformReport` (select from the configurations box dropdown) and you notice that the exception relating to the missing configuration directory has gone and the report now displays details of the new `mds1` server. [Markdown version of report for reference](/education/egeria-dojo/developer/egeria-platform-report-mds1-configured).
            
            There is a lot of detail - much of it retrieved from the server's [configuration document](/concepts/configuration-document).  The [Administration Services' `ConfigurationManagementClient`](/services/admin-services/overview/#managing-configuration-documents) is able to retrieve, update and deploy configuration documents to different OMAG Server Platforms.  `EgeriaPlatformReport` used the following method call to retrieve all of the available configuration documents before printing them out to the report.
            
            ```java linenums="1"
            ConfigurationManagementClient configurationManagementClient = new ConfigurationManagementClient(clientUserId, platformURLRoot);
            
            Set<OMAGServerConfig> configuredServers = configurationManagementClient.getAllServerConfigurations();
            ```
            Particular points to note about the `mds1` server configuration:
            
            * The type of the server is null - this is determined when the server is started and Egeria is interpreting/validating the server's configuration document.  You will see that value filled in at the next step in the dojo.
            * The server is running with a userId of `cocoMDS1npa` and a security connector of `org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaServerSecurityProvider`.  The security connector authorizes requests to Egeria and `cocoMDS1npa` is one of the userIds it recognizes.  You can change these hard-coded values in `ServerConfig` to experiment with different security settings.
            
            ```bash
               Platform servers
                  Server: mds1
                     Type: <null>
                     Description: Metadata Access Store called mds1 running on platform https://localhost:9443
                     UserId: cocoMDS1npa
                     Security Connector
                        Implementation: org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaServerSecurityProvider
                        Location: <null>
            ```
            
            * The `mds1` server is using an in-memory local metadata repository.  This means that its metadata repository is emptied each time the server is started up - which is very useful when testing new utilities.  The remote connector for the local repository is the connector that other servers would use to call `mds1`.  It is sent out on [cohort registration exchanges](/features/cohort-operation/overview) whenever `mds1` registers with a [cohort](/concepts/cohort-member.)
            
            ```bash
                     Local Repository
                        Local Repository Mode: Open Metadata Native
                        Local Repository Connector
                           Implementation: org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider
                           Location: <null>
                        Local Repository Remote Connector
                           Implementation: org.odpi.openmetadata.adapters.repositoryservices.rest.repositoryconnector.OMRSRESTRepositoryConnectorProvider
                           Location: https://localhost:9443/servers/mds1
            ```
            * Finally, the [Open Metadata Access Services (OMASs)](/services/omas) are listed including: [Asset Manager OMAS](/services/omas/asset-manager/overview), [Community Profile OMAS](/services/omas/community-profile/overview), [Data Manager OMAS](/services/omas/data-manager/overview), [Digital Architecture OMAS](/services/omas/digital-architecture/overview), [Asset Consumer OMAS](/services/omas/asset-consumer/overview), [Governance Program OMAS](/services/omas/governance-program/overview) and [Asset Owner OMAS](/services/omas/asset-owner/overview).  Below is a snippet from the report showing Asset Manager OMAS.
            ```bash
                     Services
                        Service: Asset Manager OMAS
                           Service Options
                              SupportedZones: [quarantine, trash-can, data-lake]
                              PublishZones: [data-lake, personal-files, personal-files]
                              DefaultZones: [quarantine]
                           Connectors
                              InTopic
                                 Implementation: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
                                 Location: egeria.omag.server.mds1.omas.assetmanager.inTopic
                                 Configuration Properties: {producer={bootstrap.servers=localhost:9092}, local.server.id=fab57cdc-e7fb-4f23-8237-376c9fda492b, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
                              OutTopic
                                 Implementation: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
                                 Location: egeria.omag.server.mds1.omas.assetmanager.inTopic
                                 Configuration Properties: {producer={bootstrap.servers=localhost:9092}, local.server.id=fab57cdc-e7fb-4f23-8237-376c9fda492b, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
            ```
            The `Service Options` control the behaviour of the OMAS.  `SupportedZones` defines the [governance zones that an asset must belong](/features/governance-zoning/overview) to in order to be retrievable through the OMAS.  `DefaultZones` defines the governace zones assigned to a new asset created through this interface and `PublishZones` are the governance zones that are set in the asset when the publishXXX() method is called (more later).
            
            You can also see from the implementation that the Asset Manager OMAS is configured to use Apache Kafka for its [In Topic](/concepts/in-topic) and [Out Topic](/concepts/out-topic).
            
            Now it is time to start `mds1` and observer the changes to `EgeriaPlatformReport`'s output.  For this final step, we use another utility called `ServerOps` in module `egeria-ops-utility`.  
            
            ![egeria-ops-utility module](/education/egeria-dojo/developer/egeria-ops-utility-module.png)
            
            As before, navigate to the `ServerOps` class, run it using the right-mouse menu and then, when it fails with the certificate error, add `-Dstrict.ssl=false` to the `VM Options` and re-run `ServerOps` once you have savethe configuration.
            
            ![egeria-ops-utility configuration](/education/egeria-dojo/developer/egeria-ops-utility-configuration.png)

            `ServerOps` displays a menu of operations that is can perform.
            
            ```bash
            /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -Dstrict.ssl=false ... org.odpi.openmetadata.devprojects.utilities.serverops.ServerOps
            ===============================
            OMAG Server Operations Utility:    Mon Feb 14 10:39:52 GMT 2022
            ===============================
            Running against platform: https://localhost:9443 - Egeria OMAG Server Platform (version 3.6-SNAPSHOT)
            Using userId: garygeeke
            
            Available servers: [mds1]
            Enter a command {start, stop, exit} along with one or more space separate server names. Press enter to execute request.
            ```
            
            Enter `start mds1` and press return. You will see the message `Starting mds1 ...`.  Then one of three things happens ...
            
            1. It completes successfully and you see:
            
            ```bash
            Starting mds1 ...
            Mon Feb 14 10:46:58 GMT 2022 mds1 is running the following services: [Open Metadata Repository Services (OMRS), Connected Asset Services, Asset Consumer OMAS, Community Profile OMAS, Asset Owner OMAS, Data Manager OMAS, Asset Manager OMAS, Governance Program OMAS, Digital Architecture OMAS]
                        
            Available servers: [mds1]
            Enter a command {start, stop, exit} along with one or more space separate server names. Press enter to execute request.
            ```
            2. It seem to hang after outputing `Starting mds1 ...`.  Switch to the `EgeriaPlatform` tab and you will see many audit log messages from Egeria displayed on the console. At the end is this set of messages which indicates that Apache Kafka is not running.
            
            ```bash
            Mon Feb 14 10:43:02 GMT 2022 mds1 Startup OMAG-ADMIN-0202 The Asset Consumer Open Metadata Access Service (OMAS) is supporting the following governance zones: [data-lake, personal-files, personal-files]
            Mon Feb 14 10:43:02 GMT 2022 mds1 Startup OCF-KAFKA-TOPIC-CONNECTOR-0001 Connecting to Apache Kafka Topic egeria.omag.server.mds1.omas.assetconsumer.outTopic with a server identifier of e6afd331-1853-42d0-a816-bb1eeb30c7b8
            Mon Feb 14 10:43:02 GMT 2022 mds1 Startup OCF-KAFKA-TOPIC-CONNECTOR-0015 The local server is attempting to connect to Kafka, attempt 1
            Mon Feb 14 10:44:02 GMT 2022 mds1 Startup OCF-KAFKA-TOPIC-CONNECTOR-0015 The local server is attempting to connect to Kafka, attempt 2
            ```
            
            The server is waiting for Apache Kafka to start.  If this occurs start kafka...
            
            !!! tip "Starting Apache Kafka"
                ---8<-- "docs/education/tutorials/kafka-tutorial/task-starting-kafka.md"
            
            Once Apache Kafka is running, `mds1` completes start-up and `ServerOps` outputs the success message in its *Run* tab as shown in outcome 1.
            
            3. The start of the `mds1` server fails to start.
            ```bash
            Starting mds1 ...
            Mon Feb 14 10:46:58 GMT 2022 mds1 is running the following services: [Open Metadata Repository Services (OMRS), Connected Asset Services, Asset Consumer OMAS, Community Profile OMAS, Asset Owner OMAS, Data Manager OMAS, Asset Manager OMAS, Governance Program OMAS, Digital Architecture OMAS]
            
            Available servers: [mds1]
            Enter a command {start, stop, exit} along with one or more space separate server names. Press enter to execute request.
            ```
            It is possible that you do not manage to get Kafka running in time and `mds1` fails to start.  If that happens just re-run the `start mds1` command of `ServerOps` once you have Kafka running.  
            
            !!! tip "Restarting servers"
                If you call `start mds1` when `mds1` is already, it has the effect of restarting `mds1`.  This is because the first step in startign a server is to stop the previous instance.  This is useful to know in later exercises when you are creating metadata in `mds1`'s repository.  Since `mds1` is using an in-memory repository, this restart will clear it to empty and you can start again.
            
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
            The [markdown version of the report](/education/egeria-dojo/developer/egeria-platform-report-mds1-running) makes it easier to study the new information.
            
            !!! education "Summary and further study"
                From this section of the developer dojo, you should have an understanding of the behaviour of the Platform Operations Services and Administration Services.
                
                * `ServerConfig` is using the Administration Services to configure different types of OMAG Servers.
                * `ServerOps` is using the Administration Services to start and stop named OMAG Servers.
                * `EgeriaPlatformReport` is blending information from the platform's deployment with information about configured servers, known servers and active servers.  This information comes both from the Administration Services and Platform Operations Services.
                
                The `egeria-dev-projects` utilities are designed to illustrate how to use these services and you may want to take time to review the code and make changes to explore new functions or customize them to your working environment.
                
                The next section gives you an opportunity to write your own utilities that work with the OMAS APIs.  This may be a good time to take a break :)
        
        ??? beginner "Writing a simple client program that creates, updates, finds and deletes metadata. (60 mins)"
            ??? beginner "Create a new project for your utility"
                ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-new-project.md"
            ??? beginner "Create a new java package"
                ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-package.md"
            ??? beginner "Create a new java class"
                ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-class.md"
            ??? beginner "Paste in the skeleton code"
                ---8<-- "docs/education/egeria-dojo/developer/asset-set-up-skeleton.md"
            ??? beginner "Create a Maven POM file"
                ---8<-- "docs/guides/developer/building-utilities/creating-pom-file-in-intellij.md"

            - Write AssetCreate.
            - AssetListen will display assets
            - Initializing a client
            - Creating properties
            - Using GUIDs and qualifiedNames
            - Eventually consistent operation
            - Get and find operations
            - Element headers and classifications
        ??? beginner "Extending your client program to listen for events from Egeria. (15 mins)"
            - Registering a listener to receive events
        ??? beginner "Handling errors (15 mins read)"
            - Meaning of InvalidParameterException, UserNotAuthorizedException and PropertyServerErrorException
    
    ??? beginner "Connector introduction (1.5 hours)"
        ??? beginner "What is a connector and why do we need them? (15 mins)"
            - Providing pluggability
        ??? beginner "Basic structure and lifecycle of a connector (15 mins)"
            - Connector provider
            - Connection
            - Connector instance and connector instance id
            - Audit log
            - Initialize, start, disconnect
            - The specialised connector interface
        ??? beginner "The anatomy of the connection object (15 mins)"
            - Connector types and connector categories
            - Endpoints
        ??? beginner "Extending your client program to set up connections and make use of connectors to access resources. (45 mins)"
            - Creating connectors through the Asset Consumer OMAS client
            - Using connected asset properties
    
    ??? beginner "Developing a simple connector, step-by-step (1.5 hours)"
        ??? beginner "Setting up a new connector project (30 mins)"
            - dependencies
            - build approach
        ??? beginner "Updating an Audit Log Connector (30 mins)"
            - Understanding the interface and base class
        ??? beginner "Testing your connector (30 mins)"
            - Installing the connector in Egeria's platform
        
        - Then use AssetSetUp and AssetLookUp to explore more options.

    ??? intermediate "Writing an integration connector (5 hours)"
        ??? intermediate "Design of an integration connector (30 mins)"
            - How the integration connector runs in the integration daemon
            - Additional lifecycle methods - refresh
            - Synchronization directions
            - Disconnecting
        ??? intermediate "Working with the context (30 mins)"
            - What is the context and how and when can you use it
        ??? intermediate "Receiving events from Egeria (30 mins)"
            - Implementing and registering a listener
        ??? intermediate "Handling errors (30 mins)"
            - FFDC, audit logs and exceptions
        ??? intermediate "Testing your connector (60 mins)"
            - Installing, configuring and driving the connector
            - Verifying the metadata is correct
        ??? advanced "Nested connectors (60 mins)"
            - Why nest connectors
            - VirtualConnections
            - Access embedded connector instances
        ??? advanced "Configurable connectors (30 mins)"
            - Using configuration properties
            - Using incoming events
        ??? advanced "Multi-threaded connectors (30 mins)"
            - Listening for third party events
            - Starting up and shutting down
        ??? advanced "Blocking connectors (30 mins)"
            - Using the engage method to be allocated Egeria thread
        
    ??? expert "Working with open metadata archives (1.5 hours)"
        ??? beginner "The structure of an archive (15 mins read)"
            --8<-- "docs/concepts/open-metadata-archive.md"
        ??? beginner "Setting up your archive header and dependency list (15 mins)"
            - versions, archive GUID and dependency list
        ??? beginner "Using the archive utilities (30 mins)"
            - look up dependent elements
            - build new elements
        ??? beginner "Deploying and testing your archive (30 mins)"
            - Adding archive to metadata access store
            - How the content of the archive is distributed across the open metadata ecosystem



--8<-- "snippets/abbr.md"