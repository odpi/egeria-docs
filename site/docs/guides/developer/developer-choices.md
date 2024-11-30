<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

The diagram below illustrates the choices you have in developing with Egeria:

![Choices in connecting to or enhancing egeria](/guides/developer/connecting-to-egeria.svg)
> Egeria offers Python clients for utilities and applications to call the Egeria REST APIs and receive event notifications.  It is also possible to directly call the REST APIs and access the events through the [event bus APIs](/concepts/event-bus).  Finally, connectors can be plugged into the Egeria OMAG Server Platform to customize its capabilities.  Connectors may also be used to access the content of digital resources along with its metadata from the open metadata and governance ecosystem.

The numbers on the diagram refer to the following notes.  The first three interfaces are for components running outside of Egeria's runtime.

1. Egeria's services that provide access to open metadata and the associated governance functions are called the [Open Metadata View Services (OMVSs)](/services/omvs). These REST APIs use bearer tokens for user security.  They can be called directly by application such as a JavaScript Web Application. Egeria's *Python clients* wrap calls to these REST APIs. The aim of each python client is to provide a language-specific interface that manages parameter validation along with the marshalling and de-marshalling of the call parameters and responses to these services.  

2. There are also services to manage Egeria's runtime.  The [Administration Services](/services/admin-services/overview) are used for configuring servers on Egeria's platform.  The [Platform Services](/services/platform-services/overview) provide details of the capabilities available in a platform.  The [Server Operations Services](/services/server-operations) managing the startup and shutdown of servers on the platform, and their status.

3. Egeria's *[Open Metadata Access Services (OMASs)](/services/omas)* support notifications sent over Apache Kafka [topics](/concepts/basic-concepts/#topic).  They can be accessed through any Apache Kafka client.

Egeria's runtime supports a connector framework called the [Open Connector Framework (OCF)](/frameworks/ocf/overview).  This allows components to be "plugged-into" Egeria's runtime.  These components are generically called *[connectors](/concepts/connector)*.  There are different types of connectors that each perform a specific role in the runtime.  The Egeria community provide many useful connectors, described in the [connector catalog](/connectors).  You can also write your own and install them to your Egeria runtime.

4. A [digital resource connector](/concepts/digital-resource-connector) provides a common interface to a particular type of [digital resource](/concepts/digital-resource).  It typically provides access to the contents/services of the digital resource along with the metadata it holds.  The digital resource connectors are used by other connectors to access the digital resource.  It allows the other connectors to work with multiple types of digital resource since the digital resource connectors handle the differences.

5. An [integration connector](/concepts/integration-connector) is responsible for synchronizing metadata between the open metadata repositories and third party technologies.  This synchronization can flow in either (or both) directions.  It is configured to run periodically and can also be driven by event notification.  Integration connectors typically use digital resource connectors to connect to the digital resources in the third party technologies.

6. *[Governance services](/concepts/governance-service)* are specialist *connectors* that automate the maintenance of both metadata and digital resources.  They can provision data, monitor changes in metadata and configure integration connectors.
    
7. A *[Repository connector](/concepts/repository-connector)* provides access to persistent storage services.  It is used to maintain an open metadata store.

6. *Connectors* hosted in the OMAG Server platform may use open metadata to configure a third party digital service.

7. *Connectors* are also used to connect metadata stores and catalogs into the open metadata ecosystem.

8. Finally, Egeria uses *runtime connectors* in the OMAG Server Platform to access the services it needs to operate.  Many of these [runtime connectors](/connectors/#runtime-connectors) are based around files.  They can be replaced to enable Egeria to run in new types of containers or operating platforms.




