<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Open Metadata Security

Open Metadata Security is optional.  When it is activated, it provides fine-grained authorization services for open metadata services, types and instances. Since each organization will have different security requirements, the security support is implemented through connectors. Egeria defines the interfaces and when it will call the connector.  You define the behavior the connector implements, and Egeria acts on the returned decision.

The [`metadata-security`](/services/metadata-security-services) module defines the base classes and interfaces for the open metadata security connectors as well as the server implementation to host and call them.

There are two types of connector:

* **[Platform metadata security connector](/concepts/platform-metadata-security-connector)** - secures access to the administration and platform services.  This includes the services to create new servers, the ability to start and stop servers as well as the ability to query whether a server is running, and if it is, what services are active.

* **[Server metadata security connector](/concepts/server-metadata-security-connector)** - secures access to the specific services of an OMAG server.  This includes access to the server's configuration document, starting and stopping the specific server, calling specific services, then within the server, access to specific Assets, Glossaries and Connections managed by the server, and finally the types and instances stored in the local repository.

The 2 types of connectors are shown in Figure 1:

![Figure 1](security-connectors.svg)
> **Figure 1:** positioning of the security connectors

Within an OMAG Server Platform there is one instance of the platform metadata security connector.  This connector is configured either through the `application.properties` file before the platform is started, or using a REST API call once the platform is running.

Once it is in place, any call to the [administration services](/services/admin-services/overview) or [platform services](/services/platform-services/overview) results in a check to the platform metadata security connector.

The open metadata server security connector is optionally configured for each OMAG server, to allow for each server to have a different implementation.  

The admin services command to configure a security connector for a server adds a connection for the server metadata security connector to the server's [configuration document](/concepts/configuration-document).  

The platform and server metadata security connectors operate independently, depending on which service is called. However there is a hand-off whenever the server's configuration document is read, either as part of a configuration request, or a request to start the server.

As the request is received, the platform connector checks that the user has access to the platform.  Assuming that is ok, the configuration document is read. If the configuration document contains the server metadata security connection, the connector is initiated using the connection.  The server connector is then called to check that the calling user has permission to access the server.

This means that whenever the configuration document is called, the calling user has to have permission to access both the platform and the server.  If the request is an administration service request, the user has to have administration access to the platform and server.  If the request is to start the server, the user has to have operator access.

![Figure 2](accessing-config-docs.svg)
> **Figure 2:** Calls to access a server's configuration document.

During a metadata and governance (OMAG) service call to a server, the security implementation in the server potentially invokes the server security connector multiple times as the request (shown as dotted white arrow) is handled by the server code. Figure 3 shows the different layers of checks.  Each layer is optional and so the server security connector can be implemented to support the most appropriate granularity of security for the situation. Details of the implementation choices are given in the [security connector API](#metadata-security-apis).

![Figure 3](layers-of-security-checks.svg)
> **Figure 3:** layers of security checks within the server

The security connectors are optional.  If they are not defined then there are no additional authorization checks performed inside the OMAG Server Platform nor the OMAG Servers hosted on the platform. As such, it is important that the open metadata platform security connector is configured as soon as the platform is started, and the server security connector is configured before the server is started for the first time.

## Metadata security APIs

Below is a description of the API of the two Open Metadata Security Connectors.

### Open metadata platform security connector interface

The connector that plugs into the platform implements the following interface.

*  **OpenMetadataPlatformSecurity** - provides the interface for a plugin connector that validates whether a calling user can access any service on an OMAG Server Platform.  It is called within the context of a specific OMAG Server Platform request.  Each OMAG Server Platform can define its own plugin connector implementation and will have its own instance of the connector. 
   
     * **validateUserForPlatform** - Check that the calling user is authorized to issue a (any) request to the OMAG Server Platform.
     * **validateUserAsAdminForPlatform** - Check that the calling user is authorized to issue administration requests to the OMAG Server Platform.
     * **validateUserAsOperatorForPlatform** - Check that the calling user is authorized to issue operator requests to the OMAG Server Platform such as starting and stopping servers.
     * **validateUserAsInvestigatorForPlatform** - Check that the calling user is authorized to issue requests for information to the OMAG Server Platform.  For example, to validate a connector or request lists of registered services.
  
### Open metadata server security connector interface

The connector that can be defined for an OMAG Server offers a series of layers of security checks.  An organization can choose which layers to make use of and which to allow all requests to pass.  Figure 2 shows the layers. Each layer is implemented in a separate interface and the connector can choose which interfaces to implement.  Below are the interfaces and methods for the different layers:

#### OpenMetadataServerSecurity

*OpenMetadataServerSecurity* provides the root interface for a connector that validates access to Open Metadata services and instances for a specific user.  There are other optional interfaces that define which actions should be validated.
 
* **validateUserForServer** - Checks that the calling user is authorized to issue a (any) request to the OMAG Server.
* **validateUserAsServerAdmin** - Checks that the calling user is authorized to update the configuration for a server.
* **validateUserAsServerOperator** - Checks that the calling user is authorized to issue operator requests to the OMAG Server.
* **validateUserAsServerInvestigator** - Checks that the calling user is authorized to issue operator requests to the OMAG Server.

#### OpenMetadataServiceSecurity

*OpenMetadataServiceSecurity* provides the interface for a plugin connector that validates whether a calling user can access a specific metadata service.  It is called within the context of a specific OMAG Server. Each OMAG Server can define its own plugin connector implementation and will have its own instance of the connector.  However, the server name is supplied so a single connector can use it for logging error messages and locating the valid user list for the server.
 
* **validateUserForService** - Checks that the calling user is authorized to issue this request.
* **validateUserForServiceOperation** - Checks that the calling user is authorized to issue this specific request.

#### OpenMetadataAssetSecurity

*OpenMetadataAssetSecurity* validates what a user is allowed to do with to Assets.  The methods are given access to the whole asset to allow a variety of values to be tested.

* **setSupportedZonesForUser** - Provides an opportunity to override the deployed module setting of [supportedZones](/features/governance-zoning) for a user specific list.
* **validateUserForAssetCreate** - Tests for whether a specific user should have the right to create an asset.
* **validateUserForAssetRead** - Tests for whether a specific user should have read access to a specific asset.
* **validateUserForAssetDetailUpdate** - Tests for whether a specific user should have the right to update an asset.  This is used for a general asset update, which may include changes to the zones and the ownership.
* **validateUserForAssetAttachmentUpdate** - Tests for whether a specific user should have the right to update elements attached directly  to an asset such as schema and connections.
* **validateUserForAssetFeedback** - Tests for whether a specific user should have the right to attach feedback - such as comments, ratings, tags and likes, to the asset.
* **validateUserForAssetDelete** - Tests for whether a specific user should have the right to delete an asset.

#### OpenMetadataConnectionSecurity

*OpenMetadataConnectionSecurity* defines the interface of a connector that is validating whether a specific user should be given access to a specific Connection object.  This connection information is retrieved from an open metadata repository.  It is used to create a Connector to an Asset.  It may include user credentials that could enhance the access to data and function within the Asset that is far above the specific user's approval.  This is why this optional check is performed by any open metadata service that is returning a Connection object (or a Connector created with the Connection object) to an external party.

* **validateUserForConnection** - Tests for whether a specific user should have access to a connection.
* **validateUserForAssetConnectionList** - Selects an appropriate connection for a user from the list of connections attached to an Asset.

#### OpenMetadataGlossarySecurity

*OpenMetadataGlossarySecurity* validates that a specific user is authorized to perform various operations on a glossary and its contents (terms and categories).

* **validateUserForGlossaryCreate** - Can the user create a new glossary?
* **validateUserForGlossaryRead** - Can the user have read access to a specific glossary and its contents?
* **validateUserForGlossaryDetailUpdate** - Can the user have the right to update the properties/classifications of the top-level glossary object?
* **validateUserForGlossaryMemberUpdate** - Can the user have the right to update the terms and categories of a glossary? These updates could be to their properties, classifications and relationships. It also includes attaching valid values but not semantic assignments since they are considered updates to the associated asset.
* **validateUserForGlossaryMemberStatusUpdate** - Can the user have the right to update the instance status of a term anchored in a specific glossary?
* **validateUserForGlossaryFeedback** - Can the user have the right to attach feedback - such as comments, ratings, tags and likes, to the glossary, or its terms and categories.
* **validateUserForGlossaryDelete** - Can the user delete a glossary and all its anchored contents, such as its terms and categories.

#### OpenMetadataRepositorySecurity

*OpenMetadataRepositorySecurity* defines security checks for accessing and maintaining open metadata types and instances in the local repository.  An instance is an entity or a relationship.  There is also a special method for changing classifications added to an entity.
  
* **validateUserForTypeCreate** - Tests for whether a specific user should have the right to create a typeDef within a repository.
* **validateUserForTypeRead** - Tests for whether a specific user should have read access to a specific typeDef within a repository.
* **validateUserForTypeUpdate** - Tests for whether a specific user should have the right to update a typeDef within a repository.
* **validateUserForTypeDelete** - Tests for whether a specific user should have the right to delete a typeDef within a repository.
* **validateUserForEntityCreate** - Tests for whether a specific user should have the right to create an instance within a repository.
* **validateUserForEntityRead** - Tests for whether a specific user should have read access to a specific instance within a repository.  May also remove content from the entity before it is passed to caller.
* **validateUserForEntitySummaryRead** - Tests for whether a specific user should have read access to a specific instance within a repository.
* **validateUserForEntityProxyRead** - Tests for whether a specific user should have read access to a specific instance within a repository.
* **validateUserForEntityUpdate** - Tests for whether a specific user should have the right to update an instance within a repository.
* **validateUserForEntityClassificationUpdate** - Tests for whether a specific user should have the right to update the classification for an entity instance within a repository.
* **validateUserForEntityDelete** - Tests for whether a specific user should have the right to delete an instance within a repository.
* **validateUserForRelationshipCreate** - Tests for whether a specific user should have the right to create an instance within a repository.
* **validateUserForRelationshipRead** - Tests for whether a specific user should have read access to a specific instance within a repository.  May also remove content from the relationship before it is passed to caller.
* **validateUserForRelationshipUpdate** - Tests for whether a specific user should have the right to update an instance within a repository.
* **validateUserForRelationshipDelete** - Tests for whether a specific user should have the right to delete an instance within a repository.
* **validateEntityReferenceCopySave** - Tests for whether a reference copy should be saved to the repository.
* **validateRelationshipReferenceCopySave** - Tests for whether a reference copy should be saved to the repository.

#### OpenMetadataEventsSecurity

*OpenMetadataEventsSecurity* defines security checks for sending and receiving events on the [open metadata repository cohorts](/concepts/cohort-member).
  
* **validateInboundEvent** - Validates whether an event received from another member of the cohort should be processed by this server.   May also remove content from the event before it is processed by the server.
* **validateOutboundEvent** - Validates whether an event should be sent to the other members of the cohort by this server.   May also remove content from the event before it is sent to the cohort.
    

## Sample connectors

There are sample implementations of the security connectors for [Coco Pharmaceuticals](/practices/coco-pharmaceuticals) in the "samples" module under [open-metadata-security-samples](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples)


--8<-- "snippets/abbr.md"
