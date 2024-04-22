<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

  
# Open Metadata and Governance Frameworks

The open metadata and governance frameworks define the interfaces for pluggable components.  These components provide much of the customization and technology integration points offered by the open metadata and governance implementation.  

The open metadata and governance frameworks supported by Egeria are as follows:
  
* *[Audit Log Framework (ALF)](/frameworks/alf/overview)* provides interfaces and classes to enable connectors of all types to support natural language diagnostic messages for both exceptions and the audit log.

* *[Open Metadata Framework (OMF)](/frameworks/omf/overview)* defines constant values used to define the names within the open metadata type system and its supporting services. 
* 
* *[Open Connector Framework (OCF)](/frameworks/ocf/overview)* provides the interfaces and base implementations for components (called [connectors](/concepts/connector)) that access data-related assets. OCF connectors also provide [detailed metadata about the assets](/concepts/connected-asset-properties) they access.

* *[Open Integration Framework (OIF)](/frameworks/oif/overview)* provides the interfaces and base implementations for connectors (called [integration connectors](/concepts/integration-connector)) that synchronize metadata between Egeria's open metadata ecosystem and third party technologies.  The integration connectors run in an [integration daemon](/concepts/integration-daemon).

* *[Survey Action Framework (SAF)](/frameworks/saf/overview)* provides the interfaces and base implementations for connectors (called [survey action services](/concepts/survey-action-service)) that survey and extract characteristics about the real-world resources and stores them in an open metadata repository.

* *[Governance Action Framework (GAF)](/frameworks/gaf/overview)* provides the interfaces and base implementations for connectors (called [governance action services](/concepts/governance-action-service)) that take action to assess and correct a situation that is harmful to the data, or the organization in some way.  The governance action services run in a [governance action engine](/concepts/governance-action-engine) hosted on the [Engine Host](/concepts/engine-host) OMAG Server.

* *[Context Event Framework (CEF)](/frameworks/cef/overview)* provides the interfaces and base implementations for for connectors (called [context event services](/concepts/context-event-services)) that perform event management tasks.  The context event services run in an [context event engine](/concepts/context-event-engine) hosted on the [Engine Host](/concepts/engine-host) OMAG Server.


**Note:** the integration connectors, open discovery services, context event services, and the governance action services are specialized OCF connectors, making the OCF the *only* plug-in mechanism in the open metadata and governance technology.

!!! info "Related Services"
    The [framework-services](/services/framework-services) provide The Egeria client implementations that enable the  types of connectors described in the frameworks to access and maintain the metadata they need to operate.

--8<-- "snippets/abbr.md"
