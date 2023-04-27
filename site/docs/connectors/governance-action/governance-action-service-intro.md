<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

A governance action service is a specialized [connector](/concepts/connector) that performs monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities on request.  Some governance action services invoke functions in external engines that are working with data and related assets.

A governance action service runs in the [Governance Action Open Metadata Engine Service (OMES)](/services/omes/governance-action) hosted by the [Engine Host OMAG Server](/concepts/engine-host).

![Governance Action Service](/connectors/governance-action/governance-action-service.svg)

Governance action services implement interfaces defined by the [Governance Action Framework (GAF)](/frameworks/gaf/overview). The GAF offers embeddable functions and APIs to simplify the implementation of governance action services, and their integration into the broader digital landscape, whilst being resilient and with good performance.

It is possible to implement complex governance actions in a single governance action service.  Alternatively there are five specialized types of governance action services that help you to break down your governance function into reusable components that can be choreographed by [governance action processes](/concepts/governance-action-process) to maximise the flexibility of your governance automation.  When a governance action service completes, it produces [guards](/concepts/guard) that define what needs to be done next along with a list of [action targets](/concepts/action-target).
  
* *[Watchdog Governance Action Service](/guides/developer/governance-action-services/overview/#watchdog-context-methods)* listens for changes to metadata and initiates new [governance actions](/concepts/governance-action), [governance action processes](/concepts/governance-action-process) or an [incident report](/concepts/incident-report).
  
* *[Verification Governance Action Service](/guides/developer/governance-action-services/overview/#verification-context-methods)* validates that a rule or policy is being followed.  This is often a test that the metadata elements, relationships and classification are set up as they should be.  For example, it may check that a new asset has an owner, is set up with [governance zones](/concepts/governance-zone) and includes a connection and a schema there possible.  Verification governance action services 
  
* *[Triage Governance Action Service](/guides/developer/governance-action-services/overview/#triage-context-methods)* runs triage rules to determine how to manage a situation or request, such as a request for action from an [open discovery service](/guides/developer/open-discovery-services/overview). Often this involves a human decision maker.   It may initiate an external workflow, wait for manual decision or create a [ToDo](/concepts/to-do) for a specific person.
  
* *[Remediation Governance Action Service](/guides/developer/governance-action-services/overview/#remediation-context-methods)* makes updates to metadata elements, relationships between them and classifications. Examples of remediation governance action services include:
  
    * Classification and linking of metadata elements such as adding owners, governance zones and origin classifications to assets.
    * Duplicate detection, linking and consolidating.

* *[Provisioning Governance Action Service](/guides/developer/governance-action-services/overview/#provisioning-governance-action-service)*  invokes a provisioning service whenever a provisioning request is made.  Typically, the provisioning service is an external service.  It may also create lineage metadata to describe the work of the provisioning service if the provisioning service is not able to create lineage itself.

The interfaces for governance action services is defined in the [governance-action-framework :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/frameworks/governance-action-framework) module.

??? education "Governance action service example - data onboarding process"

    The governance action services are best understood through examples.  Consider an onboarding process where new files are being copied into a landing area.  They need to be catalogued in open metadata and moved into the data lake folder.

    ![Data onboarding scenario](/guides/developer/governance-action-services/data-onboarding-example-scenario.svg)

    !!! education "Operation of the data onboarding process"
        
        ??? education "Initialization"
            At the start, there is an integration connector called *Data Files Monitoring Integration Connector* that will detect new files in the landing area folder and create an Asset metadata element to describe the file.

            There is also governance action service called *New Asset Watchdog* that has registered a listener for new Asset metadata elements.

            ![Data onboarding startup](/guides/developer/governance-action-services/data-onboarding-example-1.svg)

        ??? education "New files arrive"

            When a new file arrives, *Data Files Monitoring Integration Connector* detects is and catalogues it as an Asset in open metadata.  This triggers a call to *New Asset Watchdog* which then creates a governance action to initate a provisioning governance action service .

            ![Data onboarding startup](/guides/developer/governance-action-services/data-onboarding-example-2.svg)

        ??? education "Provisioning to the data lake"

            The governance action identifies the governance action service called *Clinical Trial Provisioning* and so it is started in the engine host.  It moves the file to the data lake folder and adds lineage metadata to describe the data movement and the new Asset for the file in the data lake.  The original asset is still in the metadata repository since it is needed to show the source of the data movement.

            ![Data onboarding startup](/guides/developer/governance-action-services/data-onboarding-example-3.svg)

        ??? education "Archive the asset for the landing area"

            The result of the provisioning removes the file from the landing area folder.  This is detected by *Data Files Monitoring Integration Connector* which then archives the corresponding Asset.  This addes a [Memento](/types/0/0010-Base-Model) classification to the Asset which means it is only retrievable on lineage requests.

            ![Data onboarding startup](/guides/developer/governance-action-services/data-onboarding-example-4.svg)

    This is a summary of the flow:
    
    ![Data onboarding overview](/guides/developer/governance-action-services/data-onboarding-example-overview.svg)

    1. New file detected by the Integration Connector.
    2. An Asset describing the file is created in the Metadata Access Server.
    3. New Asset event passed to Watchdog Governance Action Service.
    4. New Governance Action created that results in notification to Engine Host.
    5. Engine Host claims Governance Action and activates Provisioning Governance Action Service.
    6. Provisioning Governance Action Service moves file and writes lineage.
    7. Deleted file is detected by the Integration Connector.
    8. File's Asset is archived (adding a [Memento](/types/0/0010-Base-Model) classification to the Asset).

    Since the watchdog governance action service calls the provisioning governance action process explicitly via the governance action, their implementations are somewhat tied together.  The alternative is that the watchdog governance action service can invoke a [governance action process](/concepts/governance-action-process) that will choreograph the execution of one or more governance services based on a flow definition managed in open metadata.  The governance action process separates the implementation of the watchdog governance action service from the follow-on governance actions since changes to the follow-on processing is maintained through open metadata rather than requiring code changes to the watchdog governance action service code.
  
