<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Egeria Dojo - Developer Day

Egeria has an extensive set of APIs and asynchronous event interactions for retrieving and maintaining metadata.    It is also possible to write connectors that execute in Egeria's runtime and either:

- Provide Egeria access to third party technology and resources.
- Provide the mechanism to synchronize metadata between a third party technology and the open metadata ecosystem that Egeria orchestrates.

Connectors can also be called in your applications to access third party technology along with its associated metadata.

Finally, Egeria's open metadata archives have a wide set of uses in distributing standard definitions and types.

After completing developer day of the egeria dojo you should feel comfortable with calling Egeria's APIs,  writing connectors and working with open metadata archives.

!!! tip "In preparation ..."
    Egeria's interfaces are written in Java.  It is expected that you have basic Java skills and have the Java 11 SDK installed on your machine.  

    The exercises make use of code samples in the following git repositories and yo may wish to have a clone of them on your machine.
    - https://github.com/odpi/egeria-dev-projects
    - https://github.com/odpi/egeria-samples

???+ education "Developer Dojo starts here"

    ??? beginner "Calling Egeria's APIs (2.5 hours)"
        ??? beginner "Different types of APIs and their uses (30 mins)"
            - Why are there so many APIs
            - How to choose the right API
            - Where is the documentation
        ??? beginner "Setting up your IDE to use Egeria (15 mins)"
            - Setting up dependencies and test environment  
        ??? beginner "Writing a simple client program that creates, updates, finds and deletes metadata. (60 mins)"
            - Initializing a client
            - Creating properties
            - Using GUIDs and qualifiedNames
            - Eventually consistent operation
            - Get and find operations
            - Element headers and classifications
        ??? beginner "Extending your client program to listen for events from Egeria. (15 mins)"
            - Registering a listener to receive events
        ??? beginner "Handling errors (30 mins)"
            - FFDC, audit logs and exceptions
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
            - Connector types and connector catagories
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
        ??? intermediate "Testing your connector (60 mins)"
            - Installling, configuring and driving the connector
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
        
    ??? beginner "Working with open metadata archives (1.5 hours)"
        ??? beginner "The structure of an archive (15 mins)"
            - header, types and instances
            - role of archives
        ??? beginner "Setting up your archive header and dependency list (15 mins)"
            - versions, archive GUID and dependency list
        ??? beginner "Using the archive utilities (30 mins)"
            - look up dependent elements
            - build new elements
        ??? beginner "Deploying and testing your archive (30 mins)"
            - Configuring metadata access store
            - How the content of the archive is distributed across the open metadata ecosystem



--8<-- "snippets/abbr.md"