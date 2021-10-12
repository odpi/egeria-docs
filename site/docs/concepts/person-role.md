---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Person Role

A person role is a definition of a role that a person can perform.
They are defined as part of the organization definition and
describe the different types of responsibilities assumed by a person appointed to the role. 

One or more people may be appointed to a role 
Each role has an optional [head count](#head-count-limit) that indicated the maximum
number of people that should be appointed to the role.


## Head count limit

The head count limit is an optional value that can be set in a
[personal role](personal-roles.md).  This determines
how many people are funded for the role.

Open metadata does not prevent more people than this limit being
appointed to the role, but it does send a notification to indicate that
the limit has been breached.

The organization can choose to increase the head count limit or
remove one of the appointed people.

## Examples of roles

### Asset Owner

A person who is accountable for the proper use and protection of an
[Asset](/egeria-docs/concepts/asset).

The Asset Owner is supported by the [Asset Owner OMAS](/egeria-docs/concepts/omas/asset-owner/overview).

# Asset Consumer

A person who is making use of the content of one or more
[Asset](/egeria-docs/concepts/asset).  In practical terms, this is a role that most open metadata
users play at one time or another which is why there is no special labelling of
a particular user or 

The Asset Consumer is supported by the [Asset Consumer OMAS](/egeria-docs/concepts/omas/asset-consumer/overview).

# Team Leader

A team leader is a person who leads a team.  A team may have multiple leaders
although typically one person has the authority to decide if there is disagreement amongst the leaders.

# Team Member

A team member is a person who is part of a [team](team.md).



--8<-- "snippets/abbr.md