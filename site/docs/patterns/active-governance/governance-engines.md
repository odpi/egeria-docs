<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

The building industry has the principle of *shearing layers* in the design of a building.  This principle is as follows: 

*... Things that need to change frequently should be easy to change.  Those aspects that change infrequently can take more effort and time.*

In Egeria, the shearing layer principle is evident in the design of automated governance.  An organization that is maturing their governance capability needs to be able to move fast.  These automations need to be quick to create and quick to change.  There is no time to wait for a software developer to code each one.  

Egeria defines flexible components called [governance services](/concepts/governance-service) that can be re-configured and reused in many situations.  Collectively the governance services form a pallet of configurable governance functions.  The governance team link them together into a new process every time they need a new governance automation.

The advantage of this approach is the ability to rapidly scale out your governance capability.  The downside is that there are more moving parts and concepts to understand.

The diagram below summarizes how Egeria's governance automation works.  Descriptions of each layer follows the diagram.

![Layers of governance automation](/patterns/metadata-governance/governance-engines-layering.svg)

??? info "At the base are the governance service components"
    Governance services are [coded in java](/guides/developer/#extending-egeria-using-connectors) and packaged in Java Archives (Jar files).  They need to be passed information about the function to perform and the metadata elements on which to operate since this will different each time they are called.

    Part of the implementation is a [connector provider](/concepts/connector-provider) that is able to return a description of its governance service in the form of a [connector type](/concepts/connector-type).  The connector type provides information about how to configure and run the governance service.   This includes:

    * A description of the connector's function
    * Names of *configuration properties* that can modify the behaviour of the governance service.
    * A list of *request types* that select which function it is to perform.
    * Names of *request parameters*  that can be supplied (typically by the caller) that can override the configuration properties and/or provide the identifier(s) of any metadata element(s) to work on.
  
    * Names of supported action targets that provide links to the metadata element(s) to work on.  The [action target](/concepts/action-target) mechanism is typically used when governance services are being called in a sequence from a governance action process.  The action targets are used to pass details of the metadata elements to work on from service to service.

??? info "The governance service definitions"
    The JAR file is added to the CLASSPATH of Egeria's [platform](/concepts/omag-server-platform) where is can be loaded and inspected.  The architect extracts the connector type of the governance service implementation and creates at least one governance service definition for it.  The governance service definition is metadata that includes a [GovernanceService](/types/4/0461-Governance-Engines) entity, a [Connection](/types/2/0201-Connectors-and-Connections) entity and a [ConnectorType](/types/2/0201-Connectors-and-Connections) entity (based on the connector type extracted from the implementation) linked together.  The connection entity will include the settings for the various configuration properties described in the connector type.  If different combinations of configuration properties are desired, they are configured in different [governance service definitions](/concepts/governance-service-definition).

??? info "The governance engine definitions"
    The architect then builds a [governance engine definition](/concepts/governance-engine-definition).  This is metadata that defines a list of [governance request types](/concepts/governance-request-type).  These are the names of the functions needed by the governance team.

    Each governance request type is mapped to a governance service definition (defined above).  The governance engine definition can include a mapping from the governance request type to a request type understood by the governance service implementation (called the serviceRequestType).  Without this mapping, the governance request type is passed directly to the governance service implementation when it is called.

    Typically, the governance engine definition is packaged in a [open metadata archive](/concepts/open-metadata-archive) called a [governance engine pack](/concepts/governance-engine-pack).  This can be loaded into any platform that is going to run the governance engine/services.

![Executing governance automation](/patterns/metadata-governance/governance-engines-running.svg)

??? info "Engine actions"
    The governance engine is configured in an [Engine Host](/concepts/engine-host) server running on the platform.  The governance engine can be called by creating an [engine action](/concepts/engine-action).  This is a metadata entity that describes the governance request type and request parameters to run on a specific governance engine.  The engine action content is broadcast to all the running engine hosts via the Governance engine OMAS Out Topic.  On receiving this event, each engine host consults their active governance engines to see if the governance request type is supported.  The first engine host to detect the new engine action will claim the engine action, which changes it status from WAITING to ACTIVATING in the open metadata ecosystem.  The successful Engine Host then passes the request to its governance engine to execute and the engine action's status moves to IN_PROGRESS.  The results of the execution are also stored in the engine action including the final status (ACTIONED, INVALID or FAILED).

    Governance services produce one or more [guards](/concepts/guard) when they complete.  Guards describe the outcome of running the governance service. They are stored in the governance action entity that kicked off the governance service.  The governance action entities provide an audit trail of the automated governance actions that were requested, and their outcome.

    ![Governance Action statuses](/patterns/metadata-governance/governance-action-status.svg)

??? info "Governance action processes"
    Governance action processes are defined in metadata using a set of linked [governance action process steps](/concepts/governance-action-process-step).  They are choreographed in a [Metadata Access Server](/concepts/metadata-access-server). When the process is called to run, the metadata access server navigates to the first governance action process step in the governance action process flow.  It creates a matching engine action entity.  This is picked up by the engine host and executed in the governance engine just as if it was called independently.  The guards are returned by the engine action as it completes.  This change is detected by Governance Server OMAS which uses the guards to navigate to the next engine action process step(s) found in the governance action process flow.  A engine action is created for each of the next governance action process steps and the cycle is repeated until there are no more governance action process steps in the governance action process flow to execute.


A governance action process can be run many times with different parameters.  It can be changed, simply by updating the governance action process step metadata entities in the governance action process definition.  New processes can be created by creating the appropriate governance process definition.

If a desired request type can not be supported by the existing governance services, a developer is asked to extend a governance service implementation or create a new one that can be configured into a governance engine to support the desired governance request type.

??? example "Governance services supplied with Egeria"
    * [Governance Action Services](/concepts/governance-action-service)
    * [Survey Action Services](/concepts/survey-action-service)
    * [Repository Governance Services](/concepts/repository-governance-service)

