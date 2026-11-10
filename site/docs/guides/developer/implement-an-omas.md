<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Inside an Open Metadata Access Service (OMAS)

An Open Metadata Access Service (OMAS) runs in a [metadata access server](/concepts/metadata-access-server) and works directly with the [open metadata repository services (OMRS)](/services/omrs) to retrieve and maintain open metadata.

!!! info "New function is added as view services"
    Earlier releases of Egeria had many OMASs, each designed around a particular type of consumer.  The function of these services has moved into the [open metadata frameworks](/frameworks) and the [Open Metadata View Services (OMVSs)](/services/omvs), and the `access-services` module now contains only the three shared metadata management services used by the frameworks.  If you want to add a new API to Egeria, write a view service.  The structure of each type of registered service is described in [Adding registered services](/guides/developer/#adding-registered-services).

## The access services today

The access services are listed in the `AccessServiceDescription` enum in the `admin-services-api` module:

| Service                 | Enum value                | Module                                   | URL name                                                                         |
|-------------------------|---------------------------|------------------------------------------|----------------------------------------------------------------------------------|
| OCF Metadata Management | `OCF_METADATA_MANAGEMENT` | `access-services/ocf-metadata-management` | `connected-asset`                                                                |
| GAF Metadata Management | `GAF_METADATA_MANAGEMENT` | `access-services/gaf-metadata-management` | `open-governance-service`, `governance-configuration-service`, `governance-context-service` |
| OMF Metadata Management | `OMF_METADATA_MANAGEMENT` | `access-services/omf-metadata-management` | `open-metadata-store`                                                            |

- OCF Metadata Management provides the [Connected Asset Services](/services/connected-asset-services) used to create [connectors](/concepts/connector) from the [connections](/concepts/connection) stored in open metadata.
- GAF Metadata Management supports the governance engines and integration connectors hosted in the [engine host](/concepts/engine-host) and [integration daemon](/concepts/integration-daemon): their configuration, the engine actions they run and the governance action processes that link engine actions together.
- OMF Metadata Management provides the generic retrieval and maintenance of open metadata elements, relationships and classifications that is used through the `OpenMetadataClient` interface of the [Open Metadata Framework (OMF)](/frameworks/omf/overview).  The view services, for example, call it through the `EgeriaOpenMetadataStoreClient`.

## Implementation modules

The implementation of each access service is divided into these modules:

* ***service-name*-api** - a module containing the REST beans and other objects passed on the API and in event payloads.
* ***service-name*-client** - a module containing the Java client implementation(s).
* ***service-name*-server** - a module containing the server-side implementation of the service.  It registers with the administration services, implements the REST API and the eventing interface, and calls the repository services.
* ***service-name*-spring** - a module containing the server-side REST API decorated with [Spring](/guides/contributor/runtime/#spring) annotations.  This module is designed to be replaceable with a module using other REST annotation libraries so its API should be 1-1 with the REST services class in the *service-name*-server module.
* ***service-name*-topic-connectors** - (GAF and OMF Metadata Management only) the connectors for the service's [OutTopic](/concepts/out-topic).  There is a server-side connector that publishes events and a client-side connector that receives them, for example `OMFOutTopicServerConnector` and `OMFOutTopicClientConnector`.

### Java package names

The java package name root for the access services is:

 > `org.odpi.openmetadata.frameworkservices.`*servicename*

for example, `org.odpi.openmetadata.frameworkservices.omf` and `org.odpi.openmetadata.frameworkservices.gaf`.  The OCF Metadata Management service uses `org.odpi.openmetadata.frameworkservices.ocf.metadatamanagement`.

### REST URL names

The REST URL naming convention for access service URLs is:
 
> *platformURLRoot*`/servers/{serverName}/open-metadata/access-services/`*url-name*`/users/{userId}/...`

where:

* **serverName** is the name of the metadata access server.
* **url-name** is the URL name of the service (see the table above).
* **userId** is the identifier for the calling user.

Both of these parameters are mandatory on each operation. The `...` is where the specific operations are defined.

By contrast, the view services use URLs of the form *platformURLRoot*`/servers/{serverName}/api/open-metadata/`*omvs-name*`/...` and identify the caller from the bearer token passed with the request.

## Inside the server module

Using the OMF Metadata Management service as an example, the server module contains:

* **Admin class** - `OMFOperationalServices` extends `AccessServiceAdmin` from the `admin-services-registration` module.  The administration services call its `initialize()` method when the metadata access server starts, passing the service's `AccessServiceConfig`, the enterprise OMRS topic connector, the enterprise OMRS repository connector, the audit log and the server's details.  They call its `shutdown()` method when the server stops.  `AccessServiceAdmin` provides helper methods such as `registerWithEnterpriseTopic()` for listening to OMRS events and `getTopicConnector()` for creating the OutTopic connector.
* **Registration class** - `OMFServicesRegistration.registerAccessService()` creates an `AccessServiceRegistrationEntry` from the `AccessServiceDescription` enum value, the operational status and the admin class name, and passes it to `OMAGAccessServiceRegistration.registerAccessService()`.  This tells the administration services that the service is present in the platform.
* **Instance and instance handler** - `OMFServicesInstance` holds the resources (handlers, converters, repository connector) for one server.  `OMFServicesInstanceHandler` retrieves the instance for the server named in a request, and calls the registration class.
* **REST services** - `OpenMetadataStoreRESTServices` implements each REST operation by validating the parameters, retrieving the server's instance and calling the appropriate handler.
* **Handlers, builders and converters** - the handlers run on the server side and make the calls to the repository services.  Builders create the repository services entities, classifications and relationships from the properties passed on create and update requests.  Converters build the beans returned to the caller from the repository services entities, classifications and relationships.  Many of the handlers used by the access services are shared and are located in the [generic handlers](/services/generic-handlers) module of `common-services`.
* **Event handling** - `OpenMetadataOMRSTopicListener` extends `OMRSTopicListenerBase` to receive events from the OMRS, and `OpenMetadataOutTopicPublisher` publishes the resulting events on the service's OutTopic.

## Event handling guidelines

Log each event that is picked up (inbound) to be processed by the service into its audit log using the `EVENT` severity.  Also log each event that is produced (outbound) by the service into its audit log using the `EVENT` severity.  This ensures a record is kept of the asynchronous processing done by the service.

Log the first error of a given kind via audit log as well, using the appropriate severity.  For example, if an event is picked up that triggers some logic in the service that requires it to communicate with an external system for additional information, and that system is unreachable, log that failure in communication once per external system.  Since there could be many other events that also trigger a need to communicate with that same system, it is not necessary to log this communication failure with that system every time, as this would result in many duplicate error messages and could needlessly flood the audit log.  However, it is important to log the error at least once so that appropriate problem determination of the asynchronous processing can be done from the audit log.

--8<-- "snippets/abbr.md"
