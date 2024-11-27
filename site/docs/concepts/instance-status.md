<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Element/Instance status

Most types of metadata element (instances) may be in one of two status:

- ACTIVE - this means it is visible in the repositories.
- DELETED - this means it has been soft-deleted and can only be retrieved via a special query.  For repositories that support history, it is possible to move the element back to the status it was before it was deleted using the `restore()` method.

Some elements have an advanced lifecycle which means they can pass through multiple statuses during their lifetime.  

Egeria does not define the order or conditions that must be met to change status.  This is left to the deploying organization to decide their own governance processes.

## Valid status values

The list of valid values for status is defined by the [Open Metadata Framework (OMF)](/frameworks/omf/overview)'s *ElementStatus* enum.  These are matched by the [Open Metadata Repository Services (OMRS)](/services/omrs) in its *InstanceStatus* enum.  This is the complete list.

| Java/JSON name          | Ordinal | Name                    | Description                                               |
|-------------------------|---------|-------------------------|-----------------------------------------------------------|
| UNKNOWN                 | 0       | Unknown                 | Unknown instance status.                                  |
| DRAFT                   | 1       | Draft                   | The content is incomplete.                                |
| PREPARED                | 2       | Prepared                | The content is ready for review.                          |
| PROPOSED                | 3       | Proposed                | The content is in review.                                 |
| APPROVED                | 4       | Approved                | The content is approved.                                  |
| REJECTED                | 5       | Rejected                | The request or proposal is rejected.                      |
| APPROVED_CONCEPT        | 6       | Approved concept        | The request or proposal is approved for development.      |
| UNDER_DEVELOPMENT       | 7       | Under development       | The instance is being developed.                          |
| DEVELOPMENT_COMPLETE    | 8       | Development complete    | The development of the instance is complete.              |
| APPROVED_FOR_DEPLOYMENT | 9       | Approved for deployment | The instance is approved for deployment.                  |
| STANDBY                 | 10      | StandBy                 | The instance is deployed in standby mode.                 |
| ACTIVE                  | 15      | Active                  | The instance is approved and in use.                      |
| FAILED                  | 20      | Failed                  | The instance is not in use due to failure.                |
| DISABLED                | 21      | Disabled                | The instance is shutdown or disabled.                     |
| COMPLETE                | 22      | Complete                | The activity associated with the instance is complete.    |
| DEPRECATED              | 30      | Deprecated              | The instance is out of date and should not be used.       |
| OTHER                   | 50      | Other                   | The instance is in a locally defined state.               |
| DELETED                 | 99      | Deleted                 | The instance has been deleted and is no longer available. |

## Open Metadata Types with advanced lifecycles

The table below summarizes the types with advanced lifecycles and the instances that are permitted.  In all cases the default initial status is DRAFT.

| Type Name                     | DRAFT | PREPARED | PROPOSED | APPROVED | REJECTED | APPROVED_CONCEPT | UNDER_DEVELOPMENT | DEVELOPMENT_COMPLETE | APPROVED_FOR_DEPLOYMENT | STANDBY | ACTIVE | FAILED | DISABLED | COMPLETE | DEPRECATED | OTHER | DELETED |
|-------------------------------|-------|----------|----------|----------|----------|------------------|-------------------|----------------------|-------------------------|---------|--------|--------|----------|----------|------------|-------|---------|
| Process                       | X     |          | X        | X        |          |                  |                   |                      |                         |         | X      |        |          |          |            |       | X       | 
| ControlledGlossaryTerm        | X     | X        | X        | X        | X        |                  |                   |                      |                         |         | X      |        |          |          | X          | X     | X       | 
| GovernanceDefinition          | X     |          | X        | X        |          |                  |                   |                      |                         |         | X      |        |          |          | X          | X     | X       | 
| DigitalService                | X     | X        | X        | X        | X        | X                | X                 | X                    | X                       |         | X      |        | X        |          | X          | X     | X       | 
| InformationSupplyChain        | X     | X        | X        | X        | X        |                  |                   |                      |                         |         | X      |        | X        |          | X          | X     | X       | 
| InformationSupplyChainSegment | X     | X        | X        | X        | X        |                  |                   |                      |                         |         | X      |        | X        |          | X          | X     | X       | 
| SolutionComponent             | X     | X        | X        | X        | X        |                  |                   |                      |                         |         | X      |        | X        |          | X          | X     | X       | 
| SolutionPort                  | X     | X        | X        | X        | X        |                  |                   |                      |                         |         | X      |        | X        |          | X          | X     | X       | 
| SolutionBlueprint             | X     | X        | X        | X        | X        |                  |                   |                      |                         |         | X      |        | X        |          | X          | X     | X       | 



## Defining advanced lifecycles in new types

When new types are being defined with an advanced lifecycle, a list of valid instance status values is set into the type definition (TypeDef).

```java

        ArrayList<InstanceStatus> validInstanceStatusList = new ArrayList<>();

        validInstanceStatusList.add(InstanceStatus.DRAFT);
        validInstanceStatusList.add(InstanceStatus.PROPOSED);
        validInstanceStatusList.add(InstanceStatus.APPROVED);
        validInstanceStatusList.add(InstanceStatus.ACTIVE);
        validInstanceStatusList.add(InstanceStatus.DELETED);

        entityDef.setValidInstanceStatusList(validInstanceStatusList);
        entityDef.setInitialStatus(InstanceStatus.DRAFT);
        
```



