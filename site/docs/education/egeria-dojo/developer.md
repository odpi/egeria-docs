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

!!! education "Dojo starts here"

    ???+ beginner "Calling Egeria's APIs (2.5 hours)"
        !!! beginner "Different types of APIs and their uses (30 mins)"
           - How to choose the right API
        !!! beginner "Setting up your IDE to use Egeria (15 mins)"  
        !!! beginner "Writing a simple client program that creates, updates, finds and deletes metadata. (60 mins)"
        !!! beginner "Extending your client program to listen for events from Egeria. (15 mins)"
        !!! beginner "Handling errors (30 mins)"
    
    ???+ beginner "Connector introduction (1.5 hours)"
        !!! beginner "What is a connector and why do we need them? (15 mins)"
        !!! beginner "Basic structure and lifecycle of a connector (15 mins)"
        !!! beginner "The anatomy of the connection object (15 mins)"
        !!! beginner "Extending your client program to set up connections and make use of connectors to access resources. (45 mins)"
    
    ???+ beginner "Developing a simple connector, step-by-step (1.5 hours)"
        !!! beginner "Setting up a new connector project (30 mins)"
        !!! beginner "Updating an Audit Log Connector (30 mins)"
        !!! beginner "Testing your connector (30 mins)"
        
    ???+ intermediate "Writing an integration connector (5 hours)"
        !!! intermediate "Design of an integration connector (30 mins)"
        !!! intermediate "Working with the context (30 mins)"
        !!! intermediate "Receiving events from Egeria (30 mins)"
        !!! intermediate "Testing your connector (60 mins)"
        !!! advanced "Nested connectors (60 mins)"
        !!! advanced "Configurable connectors (30 mins)"
        !!! advanced "Multi-threaded connectors (30 mins)"
        !!! advanced "Blocking connectors (30 mins)"
        
    ???+ beginner "Working with open metadata archives (1.5 hours)"
        !!! beginner "The structure of an archive (15 mins)"
        !!! beginner "Setting up your archive header and dependency list (15 mins)"
        !!! beginner "Using the archive utilities (30 mins)"
        !!! beginner "Deploying and testing your archive (30 mins)"



--8<-- "snippets/abbr.md"