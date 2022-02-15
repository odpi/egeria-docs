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

    Many of the contributors to the Egeria project use the *[IntelliJ IDEA](https://www.jetbrains.com/idea/){ target=dojo-support }* IDE.  Jetbrains offers a [free community edition of IntelliJ](https://www.jetbrains.com/idea/download/) which is sufficient to work with Egeria.  You are free to use any IDE during the dojo, however the instructions will focus on IntelliJ IDEA.

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
        
        Once Egeria's core libraries are built, it is helpful to install Egeria in a directory that is easy to find.
        
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

        Egeria's services run in the [OMAG Server Platform](/concepts/omag-server-platform){ target=dojo-support }.  The jar file for the OMAG Server Platform was built by the `egeria.git` build.  It is located in the `server` directory of your Egeria install and is called `server-chassis-spring-{{release}}.jar`.  You will need an easy way to start and stop the OMAG Server Platform.   This is done with an IntelliJ *Configuration*.
        
        ??? beginner "Set up IntelliJ to run the OMAG Server Platform ..."

            ---8<-- "docs/education/egeria-dojo/developer/intellij-runs-omag-server-platform.md"

    ??? beginner "Calling Egeria's APIs (2.5 hours)"
        
        ??? beginner "Different types of APIs and their uses (30 mins)"
            
            ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis.md"

            ??? beginner "Understanding how a platform has been deployed"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-platform-deployment.md"
                
            ![EgeriaPlatformReport calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-1.svg)
            > Your development landscape showing the EgeriaPlatformReport calling EgeriaPlatform.

            ??? beginner "Understanding how a server has been configured"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-server-config.md"

            ![ServerConfig calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-2.svg)
            > Your development landscape adding ServerConfig calling EgeriaPlatform to create server configuration documents.

            ??? beginner "Understanding how a server is running"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-server-running.md"
                
            ![ServerOps calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-3.svg)
            > Your development landscape adding ServerOps calling EgeriaPlatform to start and stop servers.

            !!! education "Summary and further study"
                From this section of the developer dojo, you should have an understanding of the behaviour of the Platform Operations Services and Administration Services.
                
                * `ServerConfig` is using the Administration Services to configure different types of OMAG Servers.
                * `ServerOps` is using the Administration Services to start and stop named OMAG Servers.
                * `EgeriaPlatformReport` is blending information from the platform's deployment with information about configured servers, known servers and active servers.  This information comes both from the Administration Services and Platform Operations Services.
                
                The [`egeria-dev-projects`](https://github.com/odpi/egeria-dev-projects){ target=gh } utilities are designed to illustrate how to use these services and you may want to take time to review the code and make changes to explore new functions or customize them to your working environment.
                
                Itching to code? The next section gives you an opportunity to write your own utilities that work with the OMAS APIs.  This may be a good time to take a break :)
                   
        ??? beginner "Writing simple utilities that work with metadata. (60 mins)"
        
            In this section, you will be creating two new utilities: one called `AssetCreate` that catalogs a collection of files as assets; the other is called `AssetListen` which listens for newly created asset events and prints out details about the asset.  You can think of it as a game of catch: `AssetCreate` is throwing assets into the catalog and `AssetListen` is catching them.
            
            ??? beginner "Develop AssetListen"

                ??? beginner "Create a new IntelliJ project for AssetListen called `egeria-dojo1"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-new-project.md"
                
                ??? beginner "Create a new IntelliJ module called 'asset-listen'"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-module.md"
                
                ??? beginner "Create a new java package called `egeria.dojo.assetlisten`"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-package.md"
                
                ??? beginner "Create a new java class called `AssetListen`"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-class.md"
                
                ??? beginner "Paste in the skeleton code"
                    ---8<-- "docs/education/egeria-dojo/developer/asset-listen-skeleton.md"
                
                ??? beginner "Create a Maven POM file"
                    ---8<-- "docs/guides/developer/building-utilities/creating-pom-file-in-intellij.md"
                    ---8<-- "docs/education/egeria-dojo/developer/asset-listen-pom-skeleton.md"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-maven-module.md"

                ??? beginner "Resolve Egeria dependencies in AssetListen"

                Navigate to the `AssetListen` class and run it using the right-mouse menu as in earlier exercises.
                                
                It will fail with the certificate error.  Edit `AssetListen`'s newly created configuration and add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration to turn off the need for a certificate.
                
                ??? beginner "Add the `logback.xml` resource file to control developer logging."
                    ---8<-- "docs/guides/developer/logback/overview.md"
                
                Start `AssetListen` running and it will wait for new assets to be created.  So lets create some assets...
            
            ![AssetListen calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-4.svg)
            > Your development landscape now has AssetListen calling the mds1 server running on EgeriaPlatform to receive notifications of new assets.
            
            ??? intermediate "Develop AssetCreate"
                
                Create a new IntelliJ project called `egeria-dojo2`.  Add an IntelliJ module called `asset-create` containing an empty Java class called `egeria.dojo.assetcreate.AssetCreate`.
                 
                ??? intermediate "Paste the skeleton code into the AssetCreate class"
                    ---8<-- "docs/education/egeria-dojo/developer/asset-create-skeleton.md"
                    
                Create a `pom.xml` file for `AssetCreate`.
                
                ??? intermediate "Paste the skeleton structure into the `pom.xml` file"                
                    ---8<-- "docs/education/egeria-dojo/developer/asset-create-pom-skeleton.md"
                    
                Resolve the Egeria dependencies in your `AssetCreate` java class and add the `logback.xml` resource file to control developer logging.
                
                Navigate to the `AssetCreate` class and run it using the right-mouse menu as in earlier exercises.  It will fail with the certificate error.  Edit `AssetCreate`'s newly created configuration and add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration to turn off the need for a certificate.

            ![AssetCreate calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-5.svg)
            > Your development landscape now has added AssetCreate calling the mds1 server running on EgeriaPlatform to create new assets.  These assets arethen received by AssetListen.
               
        ??? intermediate "Handling errors (15 mins read)"
            - Meaning of InvalidParameterException, UserNotAuthorizedException and PropertyServerErrorException
    
    ??? beginner "Connector introduction (1.5 hours)"
    
        In the previous exercises you have been building utilities that run outside of the OMAG Server Platform, simply making calls to its services.  In the next two exercises you will be writing connectors that run inside the OMAG Server Platform.  Once they are written, they need to be packaged up and added to your egeria install directory so they are visible to the OMAG Server Platform.  Then you will set up the configuration of an OMAG Server to use the connector.
        
        ??? beginner "What is a connector and why do we need them? (10 mins read)"
            [Connectors](/concepts/connector) are plug-in Java clients that either perform an additional service, or, more typically, enable Egeria to integrate with a third party technology.

            The concept of a connector comes from the [Open Connector Framework (OCF)](/frameworks/ocf/overview){ target=dojo-support }. The OCF provides a common framework for components that enable one technology to call another, arbitrary technology through a common interface. The implementation of the connector is dynamically loaded based on the connector's configuration.  This is supplied in a [connection object](/concepts/connection){ target=dojo-support }.

    ??? intermediate "Developing a simple audit logging connector, step-by-step (1.5 hours)"
    
        The *Audit Log Destination Connector* is one of Egeria's runtime connectors.  This means it is used to support Egeria's runtime services - the [Open Metadata Repository Services (OMRS](/services/omrs){ target=dojo-support } in this instance.  When a service or a connector running in an OMAG Server writes a message to the [Audit Log](/concepts/audit-log){ target=dojo-support }, the OMRS is responsible for routing the audit log message to all of the destinations configured for that server.  The destinations are implemented as *Audit Log Destination Connectors* and each makes a choice on what to do with the message based on its configuration and the severity of the audit log message.
        
        If you observed the audit log messages from `mds1` on the console log, these where written out using the `ConsoleAuditLogDestinationConnector`.  When this console connector logs events, it deliberately does not include the payload of the event since it may contain sensitive information.  
        
        ```bash
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMRS-AUDIT-8009 The Open Metadata Repository Services (OMRS) has sent event of type Instance Event to the cohort topic mds1.openmetadata.repositoryservices.enterprise.mds1.OMRSTopic
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-ASSET-MANAGER-0013 The Asset Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-DATA-MANAGER-0013 The Data Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-ASSET-MANAGER-0013 The Asset Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-DATA-MANAGER-0013 The Data Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        ```
        
        However for a development environment, it is useful to be able to see the event payloads.  This exercise creates a new audit log destination connector that outputs the payload of an EVENT audit log message to the console.
        
        Create a new IntelliJ project called `egeria-dojo3` with an IntelliJ module called `event-logging-connector`.  
        
        Create a Java class called `egeria.dojo.connector.eventlogging.EventLoggingProvider.  This will contain the connector provider for your connector.  The connector provider is the factory class for the connector and also provides information to administrators and operators about the behaviour and capbility of the connector.
        
        ??? intermediate "Paste the skeleton code into the EventLoggingProvider class"
            ---8<-- "docs/education/egeria-dojo/developer/event-logging-provider-skeleton.md"
        
        Create a `pom.xml` file for the connector module.
                
        ??? intermediate "Paste the skeleton structure into the `pom.xml` file"                
            ---8<-- "docs/education/egeria-dojo/developer/event-logging-pom-skeleton.md"
        
        Create a Java class called `egeria.dojo.connector.eventlogging.EventLoggingConnector.  This will contain the actual code of the connector.
                
        ??? intermediate "Paste the skeleton code into the EventLoggingConnector class"
            ---8<-- "docs/education/egeria-dojo/developer/event-logging-connector-skeleton.md"    
                    
        Resolve the Egeria dependencies in both of the java classes for your connector.
        
        Run maven with the `clean install` options to create the jar file and you are ready to test your new connector.

        ??? intermediate "Testing your connector"
            
            ??? intermediate "Install the connector into Egeria's platform"
            
                The maven build has created a jar file in the `target` directory of your IntelliJ project.  In fact there are three jar files created:
                
                * `event-logging-connector-3.6-SNAPSHOT.jar` - this has the executable code in it.
                * `event-logging-connector-3.6-SNAPSHOT-javadoc.jar` - this has the javadoc packaged up.
                * `event-logging-connector-3.6-SNAPSHOT-sources.jar` - this has the source code packaged up.
                
                The release number used in the name is controlled by the `<version>3.6-SNAPSHOT</version>` entry in your `pom.xml` file.  The three jar files are used when publishing the module to a shared code repository such as *Maven Central*.   However, for this exercise, you only need the first one.
                
                From your `egeria-dojo3` IntelliJ project's terminal window enter the following to copy the connector's jar file into your egeria-install server lib directory, making adjustments for your connector's release as appropriate.
                ```bash
                cp target/event-logging-connector-3.6-SNAPSHOT.jar ~/egeria-install/egeria-omag-*/server/lib
                ```
                
            Restart `EgeriaPlatform` so it picks up the new classes. Use the `ServerConfig` utility and issue the following command to add your connector to the configuration document of `mds1`.
            
            ```bash
            log-event-contents mds1 egeria.dojo.connector.eventlogging.EventLoggingProvider
            ```  
            
            Start your `mds1` server using `ServerOps` and re-run `AssetCreate`.  Look at the console log of `EgeriaPlatform` and you will see the addtional logging that your connector has enabled.
            
        ![Audit log destination connector in mds1](/education/egeria-dojo/developer/developer-dojo-architecture-6.svg)
        > Your development landscape showing your new audit log destination connector running in the mds1 server logging additional information about EVENT audit log messages.

    ??? advanced "Writing an integration connector (2 hours)"
    
        Integration connectors run in an [Integration Daemon](/concepts/integration-daemon) which is a type of OMAG Server.  Its role is to either capture metadata from a third party technology and catalog it in Egeria, monitor changes to metadata in Egeria and push those changes to interested third party technologies, or both.
        
        ??? advanced "Design of an integration connector (20 mins read)"
            ---8<-- "docs/guides/developer/integration-connectors/overview.md"
       
        The integration connector that you are going to build today is very simple, but illustrates the process of building and testing integration connectors.  It will connect to Apache Kafka and retrieve a list of the topics that are defined.  It will then create `KafkaTopic` assets that will be stored in `mds1`'s metadata repository.  `mds1` will also send events to `AssetListen` about these new assets.

        Create a new project in IntelliJ called `egeria-dojo4`.  Add a module called `dojo-archive-connector` containing a Java class called `egeria.dojo.archive.DojoArchive`.
        
        Create a new IntelliJ project called `egeria-dojo4` with an IntelliJ module called `topic-cataloguing-connector`.  
                
        Create a Java class called `egeria.dojo.connector.topics.TopicCataloguingProvider` for the connector provider.
                
        ??? advanced "Paste the skeleton code into the TopicCataloguingProvider class"
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-provider-skeleton.md"
                
        Create a `pom.xml` file for the connector module.
                        
        ??? advanced "Paste the skeleton structure into the `pom.xml` file"                
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-pom-skeleton.md"
                
        Create a Java class called `egeria.dojo.connector.topics.TopicCataloguingConnectorfor the code of the connector.
                        
        ??? advanced "Paste the skeleton code into the TopicCataloguingConnectorfor class"
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-connector-skeleton.md"    
                            
        Resolve the Egeria dependencies in both of the java classes for your connector.
                
        Run maven with the `clean install` options to create the jar file and you are ready to test your new connector.
        
        ??? advanced "Testing your connector"
            Install the connector into your egeria install server lib directory.
            
            Restart `EgeriaPlatform` so it picks up the new classes. Use the `ServerConfig` utility and issue the following commands to create an integration daemon server called `daemon1` and add your connector to its configuration document.  The third command is option but installs your audit log destination connector from the previous exercise into `daemon1`.
                        
             ```bash
             create-integration-daemmon daemon1 mds1
             add-topic-connector daemon1 egeria.dojo.connector.topics.TopicCataloguingProvider
             log-event-contents daemon1 egeria.dojo.connector.eventlogging.EventLoggingProvider
             ```  
                        
             Start your servers using `ServerOps` command `start mds1 daemon1`.  The `daemon1` server will create an instance of your topic cataloguing connector.  You should see the KafkaTopic assets being catalogued and appearing as events in `AssetListen`.
        
        ![Topic cataloging connector in mds1](/education/egeria-dojo/developer/developer-dojo-architecture-8.svg)
        > Your development landscape showing your new integration connector running in the daemon1 server cataloguing new KafkaTopic assets.

    ??? expert "Working with open metadata archives (1.5 hours)"
    
        In this section you will be creating a utility that builds an *Open Metadata Archive* containing a new *Open Metadata Type* and an instance of that type.
        
        ??? expert "The structure of an archive (15 mins read)"
            --8<-- "docs/concepts/open-metadata-archive.md"
            
        Create a new project in IntelliJ called `egeria-dojo5`.  Add a module called `dojo-archive` containing a Java class called `egeria.dojo.archive.DojoArchive`.
        
        ??? expert "Paste in the skeleton code"
            ---8<-- "docs/education/egeria-dojo/developer/dojo-archive-skeleton.md"
            
        ??? expert "Create a Maven POM file"
            ---8<-- "docs/guides/developer/building-utilities/creating-pom-file-in-intellij.md"
            ---8<-- "docs/education/egeria-dojo/developer/dojo-archive-pom-skeleton.md"
            
        Add the `logback.xml` resource file to control developer logging.
        
        ??? expert "Deploying and testing your archive (30 mins)"
            
            Run `DojoArchive` to create the `dojo-archive.json` file.
            
            Copy the resulting file into your egeria install directory under content-packs.  From your IntelliJ terminal window of the egeria-dojo5 project:
            
            ```bash
            cp dojo-archive.json ~/egeria-install/egeria-omag-*/content-packs
            ```
            
            Use the `add-startup-archive mds1 content-packs/dojo-archive.json` command with `ServerConfig` to add the archive to `mds1`'s configuration document.  Restart `mds1` using `ServerOps` and observe your new MRIScan asset being received by `AssetListen`.

        ![dojo-archive loading into in mds1](/education/egeria-dojo/developer/developer-dojo-architecture-9.svg)
        > Your development landscape showing your new Open Metadata Archive loading into mds1 each time this server start up.

    ??? beginner "Congratulations, you have completed the developer day dojo"
        The Egeria community hopes you have enjoyed this dojo.  It aims to give you the skills to use IntelliJ to build utilities and connectors for Egeria.  There are, of course, many more APIs and types of connectors than you have experienced today, but they all follow similar patterns.  The links below provide some suggestions for further reading.
        
        * [Egeria's developer guide](/guides/developer){ target=dojo-support } - building on the content of this dojo
        * [Egeria's services](/services){ target=dojo-support } - to explore the APIs on offer.
        * [Egeria's Javadoc](https://odpi.github.io/egeria/index.html){ target=javadoc }


--8<-- "snippets/abbr.md"