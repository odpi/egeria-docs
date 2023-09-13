<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# OMAG Server Platform Tutorial

The [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform) is a flexible server platform that can run different types of [OMAG Servers](/concepts/omag-server).  These servers support the open metadata and governance services needed to run the open metadata ecosystem.

## Objectives

At the end of this tutorial you will be able to perform the following tasks.

* Starting the OMAG Server Platform
* Configure open metadata and governance services in an *OMAG Server*.
* Start up the configured server.
* Make calls to the running services.
* Shutdown the server.
* Remove the configuration for the OMAG server.
* Shutdown the platform.
  
## Prerequisite Tasks

* [Download and build Egeria](../building-egeria-tutorial)
* [Familiarize yourself with the Postman test tool](/education/tutorials/postman-tutorial/overview)

## Tutorial Tasks

??? education "Starting the OMAG Server Platform"
    --8<-- "snippets/tasks/task-starting-omag-server-platform-from-jar.md"
    --8<-- "snippets/tasks/task-understanding-rest-apis.md"

??? education "Creating Configuration Documents"
    --8<-- "snippets/tasks/task-creating-configuration-documents.md"

??? education "Activating an OMAG Server in the OMAG Server Platform"
    --8<-- "snippets/tasks/task-starting-omag-server.md"

??? education "Calling the Open Metadata and Governance APIs"
    --8<-- "snippets/tasks/task-calling-omag-apis.md"
 
??? education "Shutting down a server"
    --8<-- "snippets/tasks/task-stopping-omag-server.md"
    
??? education "Deleting a server's configuration"
    --8<-- "snippets/tasks/task-deleting-omag-server.md"

??? education "Shutting down the platform"
    --8<-- "snippets/tasks/task-stopping-omag-server-platform.md"
    

## Digging Deeper

* [Running the Egeria samples](/education/tutorials/running-samples-tutorial/overview) to understand more about the different Egeria APIs.
* [Calling the OMAG Clients from Java](/education/tutorials/omag-client-tutorial/overview) to understand how to call Egeria APIs from your code.
* [Running the Open Metadata Conformance Suite](/guides/cts/overview) to understand how a technology/software product can demonstrate its conformance to the Egeria standards.

--8<-- "snippets/abbr.md"