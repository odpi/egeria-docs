<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Planning for security

The Egeria runtimes have been designed so that they can be deployed securely.  However, the security of your solution depends on a combination of the deployment environment as well as Egeria itself.

## Understanding the threats to your solution

The first phase in securing your solution is to understand the threats that need to be guarded against.  This understanding is developed through [Threat Modelling](https://owasp.org/www-community/Threat_Modeling){target=_blank}.  **OWASP** has an excellent guidance pave called the [Threat Modelling Process](https://owasp.org/www-community/Threat_Modeling_Process){target=_blank} that explains how to identify the threats that could compromise your system.

## Threat model baseline for egeria ecosystem


### Step 1: Decompose the Application

Egeria ecosystem applications are the building blocks for creating automated and integrated open metadata management solution.

To decompose Egeria applications, it is very important to undestand the [OMAG Server Platform](/concepts/omag-server-platform){target=_blank}. This is a java based server application that is designed to run one or more logical application instances called OMAG Servers. Different application components can be configured and combined to provide runtime services that define the function of a single OMAG Server instance. 

??? education "Functional levels"
    | Level | Description |
    | ---------- | ---------- |    
    | Platform      | Runtime process. Provide inbound entry points, controls transoprt and enables admin services |
    | Server | Application instances. Provides function by managing lifecycle for a logical group of services, hosts connectors and maintains connections to access various technologies |
    | Service | Service units. Provide operations to validate and process server requests, process and distribute events or access storage |

Different server capabilites can be enabled by combining services in new server instances.
In practice, an organization will deploy different server types to implement solution for a specific use-case. 

Users, tools or other technology platforms access the Egeria ecosystem by interacting with OMAG Server applications.

#### Application users

Users can access Egeria applications for different purposes and by different means. Some common user types:

| ID | Name | Description|
| --- | --- | --- |
| 1 | Egeria User | Personal user accounts. In many scenarios logon and access the application using one of the User Interfaces available. In most cases these users have asociated corporate role or profile that determines the ability to access specific views or APIs that allow contorlled access to data provided by Egeria application. |
| 2 | External application | Users that are in most cases identified by non peronal accounts representing other external applications or systems accessing data. Usually those users interact with Open Matadata Access Services. |
| 3 | Internal application | Users that are used to identify internal applications or components such as other OMAG servers interacting. |

The user access is always specific to the usage scenario of an organization. In reallity funcional roles or profiles are assigned to different users responsible for specific activities in the organization.
Egeria ecosystem is designed to keep track of user access and enable access control with high level of granularity.

??? education "Metadata security levels"
    ![Metadata Security Layers](/features/metadata-security/layers-of-security-checks.svg)
    
    More details on [Metadata security](/features/metadata-security/overview){target=_blank}
    


#### External dependencies 

In an organization, Egeria applications such as OMAG Servers will always interact with external systems that are out of control of the development team therefore it is very important that the operators are aware of such extenral depdendencies in production.

Common external dependencies for Egeria ecosystem:

| ID | Description | Recommendation |
| ------ | ------ | ------ |
| 1 | Operating system security patch level | OMAG servers should always run in a secure linux environment. This includes the installation of the latest operating system and application security patches. |
| 2 | Java Virtual Machine software | Use latest stable Java runtime. Recomendation is to run OMAG server using well supported OpenJDK distribution. |
| 3 | Network access segmentation and Firewalls | Network design is important. Egeria applications should be properly deployed in private network segments behind firewalls. Depending on the use-case only specific services and endpoints should be exposed to user access networks (i.e. Web Server or API Gateway) |   
| 4 | Backend storage technology | OMAG servers can be configured with technology connectors that access database systems. Example is JanusGraph database on Apache Cassandra. Such database system should also run with up-to date version |
| 5 | Event processing technology | OMAG servers can rely on technology connectors to Apache Kafka for event streaming. Where possible, supported up-to data Kafka distributions with highly-available configuration should be used |
| 6 | Web Server and API Gateway | There are various technology options here (i.e. NGINX). Organization should rely on secure distributions runnign up to date sofware packages supporting TLS communication |


#### Entry and Exit points

Example entry and exit points for a common deployment configuration with User Interface application:

| ID | Name | Description | Trust Levels |
| ------ | ------ | ------ | ------ |
| 1 | HTTPS Web Access Port | UIs should be only acessible via TLS. All pages should be accessed via this entry point. Based on determined trust level and configured permissions page details are visible or not | (1) (2) (3) |
| 1.1 | Login Page | Login page is visible for all users | (1) |
| 1.2 | Login API function | Login function is implemented with REST API call that identifies the user and generates user access token | (2) (3) |
| 1.3 | Asset Catalog Page | Asset details can be only visible for authenticated users | (2) |
| 1.4 | Asset Catalog Web API function | Asset details retruned only to authenticated web users and users with access to Asset Catalog Access Service API | (2) |
| 1.5 | Asset Lineage Page | Asset lineage information is only visible for authenticated users | (2) |
| 1.6 | Asset Lineage Web API function | Asset lineage information is returned only to autheticated web users and users with access to Lineage Services API | (2) |
| 2 | HTTPS REST Service API Port | API endpoints should be only accessible via trusted TLS ebabled channel. Based on credetianls provided trust level is determined and access control logic applied | (4)(5)(6)(7)(8) |
| 2.1 | Admin Services API Port | This API endpoint provides ability for user/application to administer OMAG Platform and operate OMAG Servers | (6) |
| 2.2 | Access Services API Port | This API endpoint provides ability for user/application to access metadata | (7) |
| 3 | Kafka Topic | Service access via topic addresses on trusted secure kafka broker via SSL. Application access control logic can be further applied based on the credetials | (9) |


#### Assets 


| ID | Name | Description | Trust Level |
| --- | --- | --- | --- |
| 1 | OMAG Platform | Assets related to Egeria Ecosystem | |
| 1.1 | OMAG Server Configuration Document | OMAG Server configuration contains service definition, endpoints and credentials for connecting to external systems | (6) |
| 1.1 | OMAG Server availability | OMAG Servers should be available and accessible over agreed period of time | (6) |
| 1.1 | Database availability | | |
| 1.1 | Eventbus availability | | |
| 2 | Open Metadata Access Services | | |
| 2.1 | Ability to execute federated search | | |
| 2.2 | Ability retrieve asset information  | | |
| 2.2 | Ability retrieve preserve and store lineage for assets | | |
| 3 | Web Application | | |
| 3.1 | Asset Catalog | | |
| 3.2 | Asset Lineage | | |
| 3.3 | Glossary Author | | |



#### Trust levels

| ID | Name | Description |
| ------ | ------ | ------ |
| 1 | Anonymous | User connected to the secure web port without providing credentials |
| 2 | Egeria user with valid login credentials | User connected to the secure web port with correct credentials |
| 3 | Egeria user with invalid login credentials | User connected to the secure web port providing invalid credentials |
| 4 | Anonymous Service API caller | User or application connecting to API Service with no credentials |
| 5 | Service API caller with invalid credentials | Application/system connecting to any API service endpoint with invalid credentials |
| 6 | Admin Services API caller | Administration user or admin application connecting to administration API endpoint |
| 7 | Access Services API caller | Application/system connecting to Access Service endpoint with valid credentials |
| 8 | Repository Services API caller | Application/system connecting to Repository Service endpoint with valid credentials |
| 9 | Trusted Kafka client with secure access to topic | User with valid access to topic address. Trust established by the Secure Kafka Broker |


#### DFD Diagram explaining server types and general data flows

Servers with similar function are grouped together in [Types of OMAG Server](/concepts/omag-server/#types-of-omag-server){target=_blank}. There are common data flow patterns that can be recognized per server type. The complexity of data flowing between Egeria applications depends on the use case and the landscape configured.


*Below sections are work in progress*

### Step 2: Determine and rank threads
### Step 3: Determine Countermeasures and mitigations
### Complementing Code Review


!!! education "Further information on Egeria's security features"
    * [Configuring TLS and certificates](/guides/admin/omag-server-platform-transport-level-security)
    * [Metadata security plugins](/features/metadata-security/overview)
    * [Synchronizing security authorization information](/features/synchronized-access-control/overview)

--8<-- "snippets/abbr.md"
