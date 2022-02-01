---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0445 Governance Roles

Although we aim to automate governance as much as possible, it is often necessary to
assign responsibility for specific actions to specific people.

In Figure 1, the responsibilities of someone assigned to managed a
particular aspect of governing a resource ([Referenceable](/types/0/0010-Base-Model))
is represented by a **GovernanceRole** entity.
Since **GovernanceRole** inherits from [PersonRole](/types/1/0112-People)
an individual is assigned the Governance Role through the [PersonRoleAppointment](/types/1/0112-People)
relationship.

![UML](0445-Governance-Roles.svg)
> Figure 1: Assignment of Governance Roles

Specific subtypes for GovernanceRole are also defined to group governance roles into
the typical types of responsibility.

* **GovernanceOfficer** - person leading a governance domain.
* **AssetOwner** - person responsible for the correct management of an asset.
* **SubjectAreaOwner** - person responsible for the definitions within a subject area.
* **ComponentOwner** - person responsible for a component within an asset.
* **DataItemOwner** - person responsible for the correctness of a particular type of data value throughout its
lifetime.  Often these data values flow between systems and the DataItemOwner must be sure it is correct in all places.

Ownership is assigned to a resource by adding the **Ownership** classification to it.
This classification can assign ownership to an [ActorProfile](/1/0110-Actors),
[UserIdentity](/types/1/0110-Actors) or [PersonRole](/types/1/0112-People).
It does not need to be a GovernanceRole.

??? deprecated "Deprecated types"
    - *ResponsibilityStaffContact* relationship is deprecated in favour of the more generic **GovernanceResponsibilityAssignment**.
    The original ownership types did not allow resources to be owned by a person role. They are all replaced by the more generic *Ownership* classification.
    - *AssetOwnership* - use *Ownership*
    - *AssetOwnerType** - use *Ownership* properties
    - *OwnerType* - use *Ownership* properties

--8<-- "snippets/abbr.md"