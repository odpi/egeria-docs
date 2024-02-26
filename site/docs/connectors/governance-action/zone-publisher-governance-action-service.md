<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Zone Publisher Governance Action Service

!!! info "Connector summary"

    - Connector Category: [Governance Action Service](/concepts/governance-action-service)
    - Hosting Service: [Governance Action OMES](/services/omes/governance-action/overview)
    - Hosting Server: [Engine Host](/concepts/engine-host)
    - Source Module: [governance-action-connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors)
    - Jar File Name: `governance-action-connectors.jar`
    - ConnectorProviderClassName: `org.odpi.openmetadata.adapters.connectors.governanceactions.remediation.ZonePublisherGovernanceActionProvider`
    
An asset's [governance zones](/concepts/governance-zone) determines its visibility to callers. Its zone membership is maintained in the [Asset Zone Membership](/types/4/0424-Governance-Zones) classification.  

The *Zone Publisher* Governance Action Service sets the supplied governance zone names into the assets supplied as action targets.

* If there is at least one asset, their zones are updated, and the output guard is set to zone-assigned.
* If no Assets are passed as action targets the output guard is no-targets-detected.

![Figure 1](zone-publisher-governance-action-service.svg)
> **Figure 1:** Operation of the Zone Publisher governance action service


## Configuration

This connector uses the [Governance Action OMES](/services/omes/governance-action/overview) running in the [Engine Host](/concepts/engine-host).

This is its connection definition to use when creating the definition of the governance action service using the [Governance Engine OMAS](/services/omas/governance-engine/overview). 
Note that `publishZones` can be specified in either the configuration properties or the request parameters.  The value in the request parameters overrides the configuration properties value. 


```json
{
   "connection" : { 
                      "class" : "Connection",
                      "connectorType" : 
                      {
                           "class" : "ConnectorType",
                           "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.governanceactions.remediation.ZonePublisherGovernanceActionProvider"           
                      },
                      "configurationProperties" : 
                      {
                           "publishZones" : "zone1,zone2"
                      }
                  }
}

```

## Governance Action Settings

When this governance action service is called through an [engine action](/concepts/engine-action) it supports the following options.

#### Request Types and Parameters

Origin seeker does not specifically recognize any request types or request parameters.

#### Action Targets

The asset that needs an origin classification is linked to the governance action as an action target.  The unique identifier (guid) can be passed as a parameter when the governance action or governance action process is initiated.

#### Completion Status and Guards

These are the responses that Zone Publisher produces:

- `CompletionStatus.ACTIONED` with guard `zone-assigned` if the zones are successfully assigned to the assets.
- `CompletionStatus.INVALID` with guard `no-zones-detected` if the `publishZones` property is not set up in either the configuration properties or the request parameters.
- `CompletionStatus.INVALID` with guard `no-targets-detected` if no assets are passed as action targets. 

## Examples of use

The [Open Metadata Labs](/education/open-metadata-labs/overview): this connector is configured in the `governDL01` engine host server as part of the **automated curation** asset management lab.

## Related Information

* See the  [Governance Zoning](/features/governance-zoning/overview/) feature for more information on how to use governance zones.
* [Designing a Remediation Governance Action Service](/guides/developer/governance-action-services/overview/#remediation-context-methods).



----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.
