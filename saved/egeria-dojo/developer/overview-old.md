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
    Egeria's interfaces are written in Java.  It is expected that you have basic Java skills and have the Java 17 SDK installed on your machine.
    
    ??? tip "Installing Java ..."
        --8<-- "snippets/tasks/task-installing-java.md"

    You will need to build Egeria's source which needs Apache Maven installed.
    
    ??? tip "Installing Apache Maven ..."
        --8<-- "snippets/tasks/task-installing-maven.md"

    During the dojo you will running Apache Kafka to experiment with event notifications.
    
    ??? tip "Installing Apache Kafka ..."
        --8<-- "snippets/tasks/task-installing-kafka.md"

    The dojo makes use of egeria libraries and code samples in the following git repositories and you will need a clone of them on your machine.
    
    - https://github.com/odpi/egeria
    - https://github.com/odpi/egeria-samples
    - https://github.com/odpi/egeria-dev-projects
    
    ??? tip "Downloading (cloning) Egeria's git repositories ..."
        --8<-- "snippets/tasks/task-cloning-egeria-source.md"

    Many of the contributors to the Egeria project use the *[IntelliJ IDEA](https://www.jetbrains.com/idea/)* IDE.  Jetbrains offers a [free community edition of IntelliJ](https://www.jetbrains.com/idea/download/) which is sufficient to work with Egeria.  You are free to use any IDE during the dojo, however the instructions will focus on IntelliJ IDEA.

    ??? tip "Installing IntelliJ IDEA ..."
        --8<-- "snippets/tasks/task-installing-intellij.md"
      
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
            --8<-- "snippets/tasks/terminal-installing-egeria.md"

    ??? beginner "Setting up your Test environment (30 mins)"
    
        The `egeria-dev-projects.git` repository contains the utilities to support your Egeria test environment. This was one of the git repositories that you cloned in the prerequisite tasks.  Open this git repository in IntelliJ.
        
        ??? tip "Opening egeria-dev-projects.git in IntelliJ IDEA ..."
            Use **File**->**Open...** and select the top-level `egeria-dev-projects` directory that was downloaded from GitHub in the file selection window. Click the **Open** button.

        Now build the `egeria-dev-projects` code ...
        
        ??? beginner "Building egeria-dev-projects.git in IntelliJ IDEA ..."
            --8<-- "docs/education/tutorials/intellij-tutorial/intellij-building-egeria-dev-projects-git.md"

        Egeria's services run in the [OMAG Server Platform](/concepts/omag-server-platform).  The jar file for the OMAG Server Platform was built by the `egeria.git` build.  It is located in the `platform` directory of your Egeria install and is called `omag-server-platform-{{release}}.jar`.  You will need an easy way to start and stop the OMAG Server Platform.   This is done with an IntelliJ *Configuration*.
        
        ??? beginner "Set up IntelliJ to run the OMAG Server Platform ..."

            ---8<-- "docs/education/egeria-dojo/developer/intellij-runs-omag-server-platform.md"

    ??? beginner "Calling Egeria's APIs (2.5 hours)"
        
        ??? beginner "Different types of APIs and their uses (30 mins)"
            
            ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis.md"

            ??? beginner "Understanding how a platform has been deployed"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-platform-deployment.md"

            ??? beginner "Understanding how a server has been configured"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-server-config.md"

            ??? beginner "Understanding how a server is running"
                ---8<-- "docs/education/egeria-dojo/developer/different-types-of-apis-server-running.md"

            !!! education "Summary and further study"
                From this section of the developer dojo, you should have an understanding of the behaviour of the Platform Services and Administration Services.
                
                * `ServerConfig` is using the Administration Services to configure different types of OMAG Servers.
                * `ServerOps` is using the Administration Services to start and stop named OMAG Servers.
                * `EgeriaPlatformReport` is blending information from the platform's deployment with information about configured servers, known servers and active servers.  This information comes both from the Administration Services and Platform Services.
                
                The `egeria-dev-projects` utilities are designed to illustrate how to use these services and you may want to take time to review the code and make changes to explore new functions or customize them to your working environment.
                
                Itching to code? The next section gives you an opportunity to write your own utilities that work with the OMAS APIs.  This may be a good time to take a break :)
                   
        ??? beginner "Writing a simple client program that creates, updates, finds and deletes metadata. (60 mins)"
        
            In this section, you will be creating two new utilities: one called `AssetCreate` that catalogs a collection of files as assets; the other is called `AssetListen` which listens for newly created asset events and prints out details about the asset.  You can think of it as a game of catch: `AssetCreate` is throwing assets into the catalog and `AssetListen` is catching them.
            
            ??? beginner "Develop AssetCreate"
                ??? beginner "Create a new project for AssetCreate"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-new-project.md"
                ??? beginner "Create a new java package"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-package.md"
                ??? beginner "Create a new java class"
                    ---8<-- "docs/education/tutorials/intellij-tutorial/intellij-add-java-class.md"
                ??? beginner "Paste in the skeleton code"
                    ---8<-- "docs/education/egeria-dojo/developer/asset-create-skeleton.md"
                ??? beginner "Create a Maven POM file"
                    ---8<-- "docs/guides/developer/building-utilities/creating-pom-file-in-intellij.md"
                    
            ??? beginner "Develop AssetListen"
                Create a new IntelliJ project called `egeria-dojo2` that contains an empty Java class called `egeria.dojo.assetlisten.AssetListen`.

                ??? tip "Hint if you are not sure what to do  ..."
                    The java package is `egeria.dojo.assetlisten` and the Java class name is `AssetListen`.
                    
                Paste in the 

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