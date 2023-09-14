---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Egeria Dojo - Developer Day

Egeria has an extensive set of APIs and asynchronous event interactions for retrieving and maintaining metadata.    It is also possible to write connectors that execute in Egeria's runtime and either:

- Provide Egeria with access to third party technology and resources.
- Provide the mechanism to synchronize metadata between a third party technology and the open metadata ecosystem that Egeria orchestrates.

Connectors can also be called in your applications to access third party technology along with its associated metadata.

Finally, Egeria's open metadata archives have a wide set of uses in distributing standard definitions and types.

After completing developer day of the egeria dojo you should feel comfortable calling Egeria's APIs, writing connectors and working with open metadata archives.

This dojo was last tested using Egeria release 3.14.

--8<-- "docs/education/egeria-dojo/ski-run-colours.md"

## Preparing your machine for the Dojo

!!! tip "In preparation ..."

    !!! attention "Think about your machine type ..."

        The instructions below cover fairly standard machine architectures and set ups.  If you are using, say the new M1 chip in your Mac, or Windows, or are running a work machine that has been locked down by your company, then you may need to take additional actions, install additional software and enable additional permissions. In all cases, check that the software being installed is correct for your machine type and its approved uses.
    
    Egeria's interfaces are written in Java.  It is expected that you have basic Java skills and have the Java 17 SDK installed on your machine.
    
    ??? tip "Installing Java ..."
        --8<-- "snippets/tasks/task-installing-java.md"

    You will need to build your code which needs Apache Maven installed.
    
    ??? tip "Installing Apache Maven ..."
        --8<-- "snippets/tasks/task-installing-maven.md"

    During the dojo you will running Apache Kafka to experiment with event notifications.
    
    ??? tip "Installing Apache Kafka ..."
        --8<-- "snippets/tasks/task-installing-kafka.md"

    Egeria's source is on Github ...

    ??? tip "Create a GitHub account ..."
        --8<-- "docs/education/tutorials/git-and-git-hub-tutorial/task-getting-git-hub-id.md"
    
    The dojo makes use of egeria libraries and code samples in the following git repositories and you will need a clone of them on your machine.
    
    - https://github.com/odpi/egeria
    - https://github.com/odpi/egeria-samples
    - https://github.com/odpi/egeria-dev-projects

    ??? tip "Downloading (cloning) Egeria's git repositories ..."
        --8<-- "snippets/tasks/task-cloning-egeria-source.md"

    These next steps build the Egeria platform and then install it ready for the dojo.
    
    ??? tip "Build Egeria's OMAGServerPlatform"

        From a command window, use the `pwd` command to make sure you are in the `../egeria-main-libraries/egeria` directory created when you cloned the `egeria.git` repository.
        
        ```bash
        $ pwd
        /Users/mandy-chessell/egeria-main-libraries/egeria
        $
        ```

        ???+ tip "Release 3.14 and before - patch Egeria's build"
            Open the build file that creates the distribution:
            ```bash
            vi open-metadata-distribution/open-metadata-assemblies/build.gradle
            ```
            Scroll down the file until you find the following two lines (lines 184-185):
            ```bash
                    include 'content-packs'
                    include 'sample-data'
            ```
            Press the `i` key to enter INSERT mode.  Using the arrow keys to move to the end of the lines, update the path names to the following values and then press the `ESC` key.
            ```bash
                    include 'content-packs/*'
                    include 'sample-data/*/*'
            ```
            Enter `:wq` to save and quit the file.

        Enter the following command to build the egeria libraries:

        ```bash
        ./gradlew build
        ```
        After about 15 minutes you will see the **BUILD SUCCESSFUL** message.

    ??? tip "Installing Egeria's core libraries (15 mins)"
        --8<-- "snippets/tasks/terminal-installing-egeria.md"
    
    There is a template git repository that contains a set of projects to support you as you work through the developer dojo exercises.

    ??? tip "Create a git repository for your code ..."

        ---8<-- "docs/education/egeria-dojo/developer/create-template-repository.md"

    Many of the contributors to the Egeria project use the *[IntelliJ IDEA](https://www.jetbrains.com/idea/){ target=dojo-support }* IDE.  Jetbrains offers a [free community edition of IntelliJ](https://www.jetbrains.com/idea/download/) which is sufficient to work with Egeria.  You are free to use any IDE during the dojo, however the instructions will focus on IntelliJ IDEA.

    ??? tip "Installing IntelliJ IDEA ..."
        --8<-- "snippets/tasks/task-installing-intellij.md"
      
    Congratulations, you are ready to begin.

## Dojo Activities

???+ education "Developer Dojo starts here"

    ??? beginner "Developer choices when customizing Egeria (10 mins reading)"
        --8<-- "docs/guides/developer/developer-choices.md"
        
        In this dojo, you will have an opportunity to build and run Java utilities and connectors.  However before you get to the coding, you will spend some time setting up your development and test environment.

    ??? beginner "Setting up your Test environment (30 mins)"

        Egeria's services run in the [OMAG Server Platform](/concepts/omag-server-platform){ target=dojo-support }.  The jar file for the OMAG Server Platform was built by the `egeria.git` build.  It is located in the `platform` directory of your Egeria install and is called `omag-server-platform-{{release}}.jar`.  You will need an easy way to start and stop the OMAG Server Platform.   This is done with an IntelliJ *Configuration*.
 
        Open your copy of the `egeria-dojo-developer.git` repository in a **new window** in IntelliJ.

        ??? beginner "Set up IntelliJ to run the OMAG Server Platform ..."

            ---8<-- "docs/education/egeria-dojo/developer/intellij-run-omag-server-platform.md"

    ??? beginner "Calling Egeria's APIs (2.5 hours)"
        
        Now that you have Egeria's OMAG Server Platform running, you are ready to use its APIs.
        
        ??? beginner "Different types of APIs and their uses (60 mins)"
            
            ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis.md"

            ??? beginner "Understanding how a platform has been deployed"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-platform-deployment.md"
                
                !!! education "Your development landscape ..."
                    ![EgeriaPlatformReport calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-1.svg)
                    > Your development landscape showing the EgeriaPlatformReport calling EgeriaPlatform.

            ??? beginner "Understanding how a server has been configured"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-server-config.md"
                
                !!! education "Your development landscape ..."
                    ![ServerConfig calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-2.svg)
                    > Your development landscape adding the ServerConfig utility calling EgeriaPlatform to create server configuration documents.

            ??? beginner "Understanding how a server is running"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-server-running.md"
                
                !!! education "Your development landscape ..."
                    ![ServerOps calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-3.svg)
                    > Your development landscape adding the ServerOps utility calling EgeriaPlatform to start and stop servers.

            !!! education "Summary and further study"
                From this exercise of the developer dojo, you should have an understanding of the behaviour of the Platform Services and Administration Services.
                
                * `ServerConfig` is using the Administration Services to configure different types of OMAG Servers.
                * `ServerOps` is using the Administration Services to start and stop named OMAG Servers.
                * `EgeriaPlatformReport` is blending information from the platform's deployment with information about configured servers, known servers and active servers.  This information comes both from the Administration Services and Platform Services.
                
                The [`egeria-dev-projects`](https://github.com/odpi/egeria-dev-projects){ target=gh } utilities are designed to illustrate how to use these services and you may want to take time to review the code and make changes to explore new functions or customize them to your working environment.
                
                Itching to code? The next exercise gives you an opportunity to write your own utilities that work with the OMAS APIs.  This may be a good time to take a break :)
                   
        ??? beginner "Writing simple utilities that work with metadata (60 mins)"
        
            In this exercise, you will be creating two new utilities: one called `AssetCreate` that catalogs a collection of files as assets; the other is called `AssetListen` which listens for newly created asset events and prints out details about the asset.  You can think of it as a game of catch: `AssetCreate` is throwing assets into the catalog and `AssetListen` is catching them.
            
            ??? beginner "Develop AssetListen"

                ---8<-- "docs/education/egeria-dojo/developer/develop-asset-listen-cut-paste.md"

                Navigate to the `AssetListen` class and run it using the right-mouse menu as in earlier exercises.
                                
                It will fail with the certificate error.  Edit `AssetListen`'s newly created configuration and add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration to turn off the need for a certificate.
                
                ??? beginner "Add the `logback.xml` resource file to control developer logging."
                    ---8<-- "docs/guides/developer/logback/overview.md"
                
                Start `AssetListen` running and it will wait for new assets to be created.  So lets create some assets...
            
                !!! education "Your development landscape ..."
                    ![AssetListen calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-4.svg)
                    > Your development landscape now has AssetListen calling the mds1 server running on EgeriaPlatform to receive notifications of new assets.
            
            ??? intermediate "Develop AssetCreate"
                
                Create a new IntelliJ project (in a new window) called `egeria-dojo2`. Create a new sources root called `java` under `src/main` and add an empty Java class called `egeria.dojo.assetcreate.AssetCreate` under `java`.
                 
                ??? intermediate "Paste the skeleton code into the AssetCreate class"
                    ---8<-- "docs/education/egeria-dojo/developer/asset-create-skeleton.md"
                    
                Create a `pom.xml` file for `AssetCreate`.
                
                ??? intermediate "Paste the skeleton structure into the `pom.xml` file"                
                    ---8<-- "docs/education/egeria-dojo/developer/asset-create-pom-skeleton.md"
                    
                Select the pom file and add it as a maven project. Resolve the Egeria dependencies in your `AssetCreate` java class and add the `logback.xml` resource file to control developer logging.
                
                Navigate to the `AssetCreate` class and run it using the right-mouse menu as in earlier exercises.  It will fail with the certificate error.  Edit `AssetCreate`'s newly created configuration and add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration to turn off the need for a certificate.

                Rerun `AssetCreate`.  It requests that you hit enter to create an asset.  As you repeatedly press enter, observe the assets being created:
                
                * Look in the console of `EgeriaPlatform` to see the events flowing.
                * Look at `AssetListen` to see the assets being displayed.
                
                !!! education "Your development landscape ..."
                    ![AssetCreate calling EgeriaPlatform](/education/egeria-dojo/developer/developer-dojo-architecture-5.svg)
                    > Your development landscape now has added AssetCreate calling the mds1 server running on EgeriaPlatform to create new assets.  These assets arethen received by AssetListen.
               
        ??? beginner "Handling errors (2 mins read)"
            There are three exceptions that occur on many of the OMAS APIs:
            
            - *InvalidParameterException* means that your API has not provided some needed value, or the values provided are invalid at that time.
            - *UserNotAuthorizedException* means that the specific user id provided on the request is not authorized to issue the request.
            - *PropertyServerException* means that a remote server is not available or has an error that is preventing it from servicing the request.
    
    ??? beginner "Connector introduction (5 mins read)"
    
        In the previous exercises you have been building utilities that run outside of the OMAG Server Platform, simply making calls to its services.  In the next two exercises you will be writing connectors that run inside the OMAG Server Platform.  Once they are written, they need to be packaged up and added to your egeria install directory so they are visible to the OMAG Server Platform.  Then you will set up the configuration of an OMAG Server to use the connector.
        
        ??? beginner "What is a connector and why do we need them?"
            [Connectors](/concepts/connector){ target=dojo-support } are plug-in Java clients that either perform an additional service, or, more typically, enable Egeria to integrate with a third party technology.

            The concept of a connector comes from the [Open Connector Framework (OCF)](/frameworks/ocf/overview){ target=dojo-support }. The OCF provides a common framework for components that enable one technology to call another, arbitrary technology through a common interface. The implementation of the connector is dynamically loaded based on the connector's configuration.  This is supplied in a [connection object](/concepts/connection){ target=dojo-support }.

    ??? intermediate "Developing a simple audit logging connector, step-by-step (1.5 hours)"
    
        The *Audit Log Destination Connector* is one of Egeria's runtime connectors.  This means it is used to support Egeria's runtime services - the [Open Metadata Repository Services (OMRS)](/services/omrs){ target=dojo-support } in this case.  When a service or a connector running in an OMAG Server writes a message to the [Audit Log](/concepts/audit-log){ target=dojo-support }, the OMRS is responsible for routing the audit log message to all of the destinations configured for that server.  The destinations are implemented as *Audit Log Destination Connectors* and each makes a choice on what to do with the message based on its configuration and the severity of the audit log message.
        
        If you observed the audit log messages from `mds1` on the console log, these where written out using the `ConsoleAuditLogDestinationConnector`.  When this console connector logs events, it deliberately does not include the payload of the event since it may contain sensitive information.  
        
        ```bash
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMRS-AUDIT-8009 The Open Metadata Repository Services (OMRS) has sent event of type Instance Event to the cohort topic mds1.openmetadata.repositoryservices.enterprise.mds1.OMRSTopic
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-ASSET-MANAGER-0013 The Asset Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-DATA-MANAGER-0013 The Data Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-ASSET-MANAGER-0013 The Asset Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        Mon Feb 14 20:08:40 GMT 2022 mds1 Event OMAS-DATA-MANAGER-0013 The Data Manager Open Metadata Access Service (OMAS) has sent event of type: New Element
        ```
        
        However for a development environment, it is useful to be able to see the event payloads.  This exercise creates a new audit log destination connector that outputs the payload of an EVENT audit log message to the console.
        
        Create a new IntelliJ project called `egeria-dojo3`.  Create a directory `main/java` under `src` and make `java` the sources root.
        
        Create a Java class called `egeria.dojo.connector.eventlogging.EventLoggingProvider` under `java`.  This will contain the connector provider for your connector.  The connector provider is the factory class for the connector and also provides information to administrators and operators about the behaviour and capbility of the connector.
        
        ??? intermediate "Paste the skeleton code into the EventLoggingProvider class"
            ---8<-- "docs/education/egeria-dojo/developer/event-logging-provider-skeleton.md"
        
        Create a Java class called `egeria.dojo.connector.eventlogging.EventLoggingConnector` under `java`.  This will contain the actual code of the connector.
                
        ??? intermediate "Paste the skeleton code into the EventLoggingConnector class"
            ---8<-- "docs/education/egeria-dojo/developer/event-logging-connector-skeleton.md"
            
        Create a `pom.xml` file at the top of the project (same level as `src`).
                
        ??? intermediate "Paste the skeleton structure into the `pom.xml` file"                
            ---8<-- "docs/education/egeria-dojo/developer/event-logging-connector-pom-skeleton.md"
        
        Resolve the Egeria dependencies in both of the java classes for your connector. When you are offered a choice on `InvalidParameterException`, select the one from the Open Metadata Repository Services (OMRS) - that is `import org.odpi.openmetadata.repositoryservices.ffdc.exception.InvalidParameterException;`.  
        
        ![Choice](/education/tutorials/intellij-tutorial/intellij-resolve-external-dependencies-4.png)

        The way to discover the answer is to click on the green circle next to the method name in the left-hand margin.  This takes you to the super class `OMRSAuditLogStoreConnectorBase`.  
               
        ![Navigate](/education/tutorials/intellij-tutorial/intellij-resolve-external-dependencies-5.png)
            
        Then go to the top of the file to discover which version it is using.
        
        ![Discover](/education/tutorials/intellij-tutorial/intellij-resolve-external-dependencies-6.png)
        
        Run maven with the `clean install` options to create the jar file and you are ready to test your new connector.

        ??? intermediate "Testing your connector"
            
            ??? intermediate "Install the connector into Egeria's platform ..."
            
                The maven build has created a jar file in the `target` directory of your IntelliJ project called  `event-logging-connector-3.12.jar`
                
                The release number used in the name is controlled by the `<version>4.2</version>` entry in your `pom.xml` file.  
                
                From your `egeria-dojo3` IntelliJ project's terminal window enter the following to copy the connector's jar file into your egeria-install server lib directory, making adjustments for your connector's release as appropriate.
                ```bash
                cp target/event-logging-connector*.jar ~/egeria-install/egeria-omag-*/server/lib
                ```
            
            ??? intermediate "Reconfigure mds1 to use the new connector ..."
 
                Restart `EgeriaPlatform` so it picks up the new classes. Use the `ServerConfig` utility and issue the following command to add your connector to the configuration document of `mds1`.
            
                ```bash
                log-event-contents mds1 egeria.dojo.connector.eventlogging.EventLoggingProvider
                ```  
                
            ??? intermediate "Run your test ..."

                Start your `mds1` server using `ServerOps` and re-run `AssetCreate`.  Look at the console log of `EgeriaPlatform` and you will see the addtional logging that your connector has enabled.
            
        !!! education "Your development landscape ..."
            ![Audit log destination connector in mds1](/education/egeria-dojo/developer/developer-dojo-architecture-6.svg)
            > Your development landscape showing your new audit log destination connector running in the mds1 server logging additional information about EVENT audit log messages.

    ??? advanced "Writing an integration connector (2 hours)"
    
        Integration connectors run in an [Integration Daemon](/concepts/integration-daemon) which is a type of OMAG Server.  Its role is to either capture metadata from a third party technology and catalog it in Egeria, monitor changes to metadata in Egeria and push those changes to interested third party technologies, or both.
        
        ??? advanced "Design of an integration connector (20 mins read)"
            ### Integration connectors
            
            ---8<-- "docs/connectors/integration/integration-connector-intro.md"
            
            #### Writing the connector provider for an integration connector
        
            ---8<-- "docs/guides/developer/connector-provider-intro.md"
        
            ---8<-- "docs/guides/developer/implementing-an-integration-connector-provider.md"
        
            #### Integration connector interface
        
            ---8<-- "docs/guides/developer/integration-connectors/integration-connector-interface.md"
        
       
        The integration connector that you are going to build today is very simple, but illustrates the process of building and testing integration connectors.  It will connect to Apache Kafka and retrieve a list of the topics that are defined.  It will then create `KafkaTopic` assets that will be stored in `mds1`'s metadata repository.  `mds1` will also send events to `AssetListen` about these new assets.
        
        Create a new IntelliJ project called `egeria-dojo4`.  Create a directory `main/java` under `src` and make `java` the sources root.
         
        Create a Java class called `egeria.dojo.connector.topics.TopicCataloguingAuditCode` under `java` for your connector's audit log message definitions.  Logging and error handling are an important part of a connector's design.  It did not feature in the audit log destination connector because that connector was part of the audit logging system.  However it will feature in all other connectors that your write.  
        
        ??? advanced "Paste the skeleton code into the `TopicCataloguingAuditCode` class"
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-audit-skeleton.md"

        Create a Java class called `egeria.dojo.connector.topics.TopicCataloguingErrorCode` under `java` for your connector's exception message definitions.  Exceptions are sent between processing environments and Egeria's exceptions include [First Failure Data Capture (FFDC)](/guides/diagnistic/ffdc) information in them to aid inter=system problem determination.
               
        ??? advanced "Paste the skeleton code into the `TopicCataloguingErrorCode` class"
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-error-skeleton.md"

        Create a Java class called `egeria.dojo.connector.topics.TopicCataloguingProvider` under `java` for the connector provider.
                
        ??? advanced "Paste the skeleton code into the `TopicCataloguingProvider` class"
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-provider-skeleton.md"
        
        Create a Java class called `egeria.dojo.connector.topics.TopicCataloguingConnector` under `java` for the code of the connector.
                                
        ??? advanced "Paste the skeleton code into the TopicCataloguingConnector class"
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-connector-skeleton.md"
            
        Create a `pom.xml` file for the connector at the top level of the project.
                        
        ??? advanced "Paste the skeleton structure into the `pom.xml` file"                
            ---8<-- "docs/education/egeria-dojo/developer/topic-cataloguing-connector-pom-skeleton.md"
                            
        Resolve the Egeria dependencies in all 4 of the java classes for your connector.

        Run maven with the `clean install` options to create the jar file and you are ready to test your new connector.
        
        ??? advanced "Testing your connector"
            Copy the connector jar file into your egeria install server lib directory.
            
            Restart `EgeriaPlatform` so it picks up the new classes. Use the `ServerConfig` utility and issue the following commands to create an integration daemon server called `daemon1` and add your connector to its configuration document.  The third command is option but installs your audit log destination connector from the previous exercise into `daemon1`.
                        
             ```bash
             create-integration-daemon daemon1 mds1
             ```
             ```bash
             add-topic-connector daemon1 egeria.dojo.connector.topics.TopicCataloguingProvider
             ```
             ```bash
             log-event-contents daemon1 egeria.dojo.connector.eventlogging.EventLoggingProvider
             ```  
                        
             Start your servers using `ServerOps` command `start mds1 daemon1`.  The `daemon1` server will create an instance of your topic cataloguing connector.  You should see the KafkaTopic assets being catalogued and appearing as events in `AssetListen`.
        
        !!! education "Your development landscape ..."
            ![Topic cataloging connector in mds1](/education/egeria-dojo/developer/developer-dojo-architecture-7.svg)
            > Your development landscape showing your new integration connector running in the daemon1 server cataloguing new KafkaTopic assets.

    ??? expert "Working with open metadata archives (1.5 hours)"
    
        In this exercise you will be creating a utility that builds an *Open Metadata Archive* containing a new *Open Metadata Type* and an instance of that type.
        
        ??? expert "What is an open metadata archive? (15 mins read)"
        
            --8<-- "docs/concepts/open-metadata-archive-intro.md"
            
            ??? expert "The structure of an open metadata archive"
                --8<-- "docs/concepts/open-metadata-archive-structure.md"
            
            ??? expert "How an open metadata archive is processed"
                --8<-- "docs/concepts/open-metadata-archive-processing.md"
        
        This session is marked as an expert session since it presents a challenge - to use the skills from the earlier exercises, the `egeria-samples.git` as a guide and the helper classes in `egeria.git` to build your own archive writer.
        
        ??? expert "In memory archive construction (15 mins read)"
            --8<-- "docs/guides/developer/open-metadata-archives/in-memory-archive-construction.md"
        
        ??? expert "Explore `coco-metadata-samples` (15 mins)"
            In the `egeria-samples.git` repository that you downloaded in the prereqs there is a module called `coco-metadata-archives` (under `sample-metadata-archives`). This has examples of 4 archive writers.  In particular, `CocoTypesArchiveWriter` creates an open metadata archive with type definitions and `CocoGovernanceEngineArchives` creates instances.
            
            Load this git repository into Intellij and look at the code (remembering to use `git pull` to get the latest versions).  This will help you in the exercise that follows. 

        Create a new project in IntelliJ called `egeria-dojo5`.  Add a Java class called `egeria.dojo.archive.DojoArchiveWriter`.  `DojoArchiveWriter` is the class that you will write, with its accompanying `pom.xml` and `logback.xml` file.  It extends `OMRSArchiveWriter` from the `repository-services-archive-utilities`.
        
        Your archive will write to the `egeria-dojo-archive.json` file and have header properties of:
        
        * archiveGUID        = "eede2744-5afa-4d61-89c9-e7a7447075bb";        
        * archiveName        = "DojoArchive";                                   
        * archiveLicense     = "Apache-2.0";                                  
        * archiveDescription = "An experimental open metadata archive."; 
        * archiveType        = OpenMetadataArchiveType.CONTENT_PACK;          
        * originatorName     = "Egeria Dojo Exercise";                              
        * creationDate       = new Date();
        * versionNumber      = 1L;
        * versionName        = "1.0";
        
        It will be dependent on (in fact it extends) Egeria's open metadata types.  
        
        In your archive's type store will be 1 new type:
        
        * typeGUID        = "dd54e751-87d9-4875-86a9-6da2f775e3d2"
        * typeName        = "MRIScan"
        * typeDescription = "An MRI scan for a patient."
        * superTypeName   = "DataSet" 
        
        *Note:* `DataSet` is a type of asset.  
        
        In your archive's instance store will be 1 new entity instance:
        
        * typeName        = "MRIScan"
        * qualifiedName   = "MRIScan:FlorencePaynter:" + new Date()
        * displayName     = "MRI scan for Florence Paynter"
        * description     = "MRI scan for Florence Paynter focussed on left arm."
        * governanceZones = { "data-lake" }
        
        If you want to add more to the example, think about how you would add a property called "focusArea" to the MRIScan type and populate a value in the instance.
        
        ??? expert "Deploying and testing your archive (30 mins)"
            
            Run `DojoArchiveWriter` to create the `dojo-archive.json` file.
            
            ??? expert "Copy the resulting file into your egeria install directory under `content-packs`"
                From your IntelliJ terminal window of the `egeria-dojo5` project:
            
                ```bash
                cp dojo-archive.json ~/egeria-install/egeria-omag-*/content-packs
                ```
            
            Use the `add-startup-archive mds1 content-packs/dojo-archive.json` command with the `ServerConfig` utility to add the archive to `mds1`'s configuration document.  Restart `mds1` using `ServerOps` and observe your new MRIScan asset being received by `AssetListen`.

        !!! education "Your development landscape ..."
            ![dojo-archive loading into in mds1](/education/egeria-dojo/developer/developer-dojo-architecture-8.svg)
            > Your final development landscape showing your new Open Metadata Archive loading into mds1 each time this server start up.

    ??? beginner "Congratulations, you have completed the developer day dojo"
        The Egeria community hopes you have enjoyed this dojo.  It aims to give you the skills to use IntelliJ to build utilities and connectors for Egeria.  There are, of course, many more APIs and types of connectors than you have experienced today, but they all follow similar patterns.  The links below provide some suggestions for further reading.
        
        * [Egeria's developer guide](/guides/developer){ target=dojo-support } - building on the content of this dojo
        * [Egeria's services](/services){ target=dojo-support } - to explore the APIs on offer.
        * [Egeria's Javadoc](https://odpi.github.io/egeria/index.html){ target=javadoc }


--8<-- "snippets/abbr.md"