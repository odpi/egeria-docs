<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

The diagram below illustrates the choices you have in developing with Egeria:

![Choices in connecting to or enhancing egeria](/guides/developer/connecting-to-egeria.svg)
> Egeria offers Java clients for utilities and applications to call the Egeria APIs and receive event notifications.  It is also possible to directly call the REST APIs and access the events through the [event bus APIs](/concepts/event-bus).  Finally connectors can be plugged into the Egeria OMAG Server Platform to customize its capabilities.  Connectors may also be used to access the content of digital resources along with its metadata from the open metadata and governance ecosystem

The numbers on the diagram refer to these notes:

1. Egeria's *Java clients* wrap calls to Egeria's REST APIs. The aim is to provide a language-specific interface that manages parameter validation along with the marshalling and de-marshalling of the call parameters and responses to these services.

2. Many of Egeria's *Java clients* provide the mechanism to register a listener with a [topic](/concepts/basic-concepts/#topic) that an Egeria service is publishing notifications to.  This removes all requirements for the consuming Java application to interact with the [event bus](/concepts/event-bus) technology.

3. Some of Egeria's *Java clients* also support the creation of [digital resource connectors](/concepts/digital-resource-connector) that can access the content of [digital resources](/concepts/resource) along with the [metadata about the digital resource](/concepts/asset).

4. For applications that are not written in Java, it is possible to call Egeria directly through its *REST APIs*, and access Egeria's notifications by connecting directly to the topics on the *event bus*.
    
5. Egeria's [OMAG Server Platform](/concepts/omag-server-platform) can host many types of *connectors*.  For example, there are *connectors* that automatically catalog metadata from a third party technology.

6. *Connectors* hosted in the OMAG Server platform may use open metadata to configure a third party digital service.

7. *Connectors* are also used to connect metadata stores and catalogs into the open metadata ecosystem.

8. *Governance services* are specialist *connectors* hosted in the OMAG Server Platform to automate the maintenance of both metadata and digital resources.

9. Finally, Egeria uses *connectors* in the OMAG Server Platform to access the services it needs to operate.  Many of these [runtime connectors](/connectors/#runtime-connectors) are based around files.  They can be replaced to enable Egeria to run in new types of containers or operating platforms.

---8<-- "snippets/abbr.md"


