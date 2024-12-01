<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Using the Java Clients

Egeria's Java clients are primarily written for use by Egeria's runtime.  They allow the [View Server](/concepts/view-server) and [governance servers](/concepts/governance-server) to call the [Open Metadata Access Services (OMASs)](/services/omas), [Administration Services](/services/admin-services/overview), [Platform Services](/services/platform-services/overview) and [Server Operation Services](/services/server-operations).  They wrap calls to Egeria's REST APIs. The aim is to provide a language-specific interface that manages parameter validation along with the marshalling and de-marshalling of the call parameters and responses to these services.

Many of Egeria's Java clients provide the mechanism to register a listener with a topic that an Egeria service is publishing notifications to. This removes all requirements for the consuming Java application to interact with the event bus technology.

Some of Egeria's Java clients also support the creation of digital resource connectors that can access the content of digital resources along with the metadata about the digital resource.

The Javadoc for these clients are:

* [Asset Consumer OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetconsumer/client/package-summary.html)
* [Asset Manager OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetmanager/client/package-summary.html)
* [Asset Owner OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetowner/client/package-summary.html)
* [Community Profile OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/communityprofile/client/package-summary.html)
* [Data Manager OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datamanager/client/package-summary.html)
* [Data Science OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datascience/client/package-summary.html)
* [Design Model OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/designmodel/client/package-summary.html)
* [Digital Architecture OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/digitalarchitecture/client/package-summary.html)
* [Digital Service OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/digitalservice/client/package-summary.html)
* [Governance Program OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/package-summary.html)
* [Governance Server OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceserver/client/package-summary.html)
* [IT Infrastructure OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/itinfrastructure/client/package-summary.html)
* [Project Management OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/projectmanagement/client/package-summary.html)
* [Security Manager OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/securitymanager/client/package-summary.html)
* [Software Developer OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/softwaredeveloper/client/package-summary.html)
* [Stewardship Action OMAS](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/stewardshipaction/client/package-summary.html)

--8<-- "snippets/abbr.md"