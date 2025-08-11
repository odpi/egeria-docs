<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0457 Connector Activity Reports

![UML](0457-Connector-Activity-Reports.svg)

## ConnectorActivityReport entity

The *ConnectorActivityReport* entity describes the updates made by an [integration connector](/concepts/integration-connector) during a single call to its `refresh()` method or the operations of an instance of a [governance service](/concepts/governance-service).  A report is only created if the connector made changes (create, update, delete) to the metadata.

The attributes are as follows:

* *serverName* - name of the [integration daemon](/concepts/integration-daemon) where the integration connector is running/ran or the [engine host](/concepts/engine-host) where the governance service ran.
* *connectorId* : unique identifier of the connector.  This is either the unique identifier (guid) of the [RegisteredIntegrationConnector](/types/4/0464-Dynamic-Integraiton-Groups) relationship that links the integration connector into a running integration group OR the unique identifier of the [SupportedGovernanceService](/types/4/0461-Governance-Engines) relationship that identified the governance service to run.
* *connectorName* : name of the connector.  This is either set in the integration daemon's configuration document or it is the unique identifier (guid) of the *RegisteredIntegrationConnector* relationship that links the integration connector into a running integration group.
* *createCounts* : A map of element type names to the number of instances of that type that were created and anchored to the anchor subject.
* *updateCounts* : A map of element type names to the number of instances of that type that were updated while anchored to the anchor subject.
* *deleteCounts* : A map of element type names to the number of instances of that type that were deleted while anchored to the anchor subject.
* *additionalProperties* - additional properties of importance to the integration connector.


--8<-- "snippets/abbr.md"